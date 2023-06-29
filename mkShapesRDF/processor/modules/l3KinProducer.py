# Reference python module: https://github.com/latinos/LatinoAnalysis/blob/UL_production/NanoGardener/python/modules/l3KinProducer.py

from mkShapesRDF.processor.framework.module import Module
import ROOT

class l3KinProducer(Module):
    def __init__(self):
        super().__init__("l3KinProducer")

    def runModule(self, df, values):
        df = df.Define(
            "Lepton_4DV",
            "ROOT::VecOps::Construct<ROOT::Math::PtEtaPhiMVector>"
            "(Lepton_pt, Lepton_eta, Lepton_phi, "
            "ROOT::RVecF(Lepton_pt.size(), 0))",
        )

        df = df.Define(
            "CleanJet_4DV",
            "ROOT::VecOps::Construct<ROOT::Math::PtEtaPhiMVector>"
            "(CleanJet_pt, CleanJet_eta, CleanJet_phi,"
            # "Take(Jet_mass, CleanJet_jetIdx))",
            "CleanJet_mass)",
        )

        df = df.Define(
            "MET_4DV", "ROOT::Math::PtEtaPhiMVector" "(PuppiMET_pt, 0, PuppiMET_phi, 0)"
        )

        df = df.Define(
            "TkMET_4DV", "ROOT::Math::PtEtaPhiMVector" "(TkMET_pt, 0, TkMET_phi, 0)"
        )

        df = df.Define(
            "l3_isOk",
            "Lepton_pt[Lepton_pt > 0].size() >= 3",
            excludeVariations=["JES*", "MET*"],
        )

        # df = df.Define(
        #     "_isOk3l",
        #     "Lepton_pt[Lepton_pt > 0].size() >= 3 && MET_4DV.E()>0",
        #     excludeVariations=["JES*", "MET*"],
        # )

        df = df.Define(
            "_WH3l_isOk",
            "(abs( Sum( abs(Lepton_pdgId)/Lepton_pdgId ) ) <= 1) && l3_isOk",
            excludeVariations=["JES*", "MET*"],
        )

        df = df.Define("_lepOk",   "Lepton_pt[Lepton_pt > 0].size()")
        df = df.Define("_tkMetOk", "TkMET_4DV.E() > 0")
        df = df.Define("_jetOk",   "CleanJet_pt[CleanJet_pt > 0].size()")


        # Variables yet to be implemented:
        ##############################

        #         # for ZH3l, "l" in these variables *always* refers to the lepton not associated with the Z
        #         'ZH3l_njet'      : (["F"], {}),
        #         'ZH3l_Z4lveto'   : (["F"], {}),
        #         'ZH3l_dmjjmW'    : (["F"], {}),
        #         'ZH3l_mTlmet'    : (["F"], {}),
        #         'ZH3l_pdgid_l'   : (["F"], {}),
        #         'ZH3l_dphilmetjj': (["F"], {}),
        #         'ZH3l_dphilmetj' : (["F"], {}),
        #         'ZH3l_pTlmetjj'  : (["F"], {}),
        #         'ZH3l_pTlmetj'   : (["F"], {}),
        #         'ZH3l_mTlmetjj'  : (["F"], {}),
        #         'ZH3l_mTlmetj'  : (["F"], {}),
        #         'ZH3l_pTZ'       : (["F"], {}),
        #         'ZH3l_checkmZ'   : (["F"], {}),
        
        #         'AZH_mA_minus_mH': (["F"], {}),
        #         'AZH_Amass':  (["F"], {}),
        #         'AZH_Hmass' : (["F"], {}),
        #         'AZH_ChiSquare' : (["F"], {}),

        # Variables definitions
        prefix = "new_fw_"
        Zmass  = 91.1876

        ROOT.gInterpreter.Declare("""
        float Get_minmllDiffToZ(ROOT::VecOps::RVec<ROOT::Math::PtEtaPhiMVector> leptons_vector, ROOT::RVecF leptons_pdgId){
            float minmllDiffToZ = 9999.0;
            float mllDiffToZ    = 9999.0;
            if (leptons_vector.size() < 3) return minmllDiffToZ;
            for (uint i = 0; i < 3; i++){
                for (uint j = i; j < 3; j++){
                    if ( abs(leptons_pdgId[i])/leptons_pdgId[i] != abs(leptons_pdgId[j])/leptons_pdgId[j] ) continue;
                    minmllDiffToZ = abs( (leptons_vector[i] + leptons_vector[j]).M() - 91.1876 );
                    if ( mllDiffToZ < minmllDiffToZ ) minmllDiffToZ = mllDiffToZ;
                }
            }
        return minmllDiffToZ;
        }
        """)

        df = df.Define(
            prefix + "WH3l_ZVeto",
            "_WH3l_isOk ? Get_minmllDiffToZ(Lepton_4DV, Lepton_pdgId) : -9999.0",
        )

        ROOT.gInterpreter.Declare("""
        bool Compare_charge(ROOT::RVecF leptons_pdgId){
            if (leptons_pdgId.size() < 3) return false;
            for (uint i = 0; i < 3; i++){
                for (uint j = i; j < 3; j++){
                    if ( abs(leptons_pdgId[i])/leptons_pdgId[i] == abs(leptons_pdgId[j])/leptons_pdgId[j] ) return true;
                }
            }
        return false;
        }
        """)

        df = df.Define(
            prefix + "WH3l_flagOSSF",
            "_WH3l_isOk ? Compare_charge(Lepton_pdgId) : false",
        )

        df = df.Define(
            prefix + "WH3l_njet",
            "_WH3l_isOk ? CleanJet_pt[CleanJet_pt > 40 && abs(CleanJet_eta) < 4.7].size() : -9999.0",
        )

        ROOT.gInterpreter.Declare("""
        ROOT::RVecF Get_mtlmet(ROOT::VecOps::RVec<ROOT::Math::PtEtaPhiMVector> leptons_vector, ROOT::Math::PtEtaPhiMVector met){
            ROOT::RVecF mtlmet_vector;
            if (leptons_vector.size() < 3) return ROOT::RVecF(3, -9999.0);
            for (uint i = 0; i < 3; i++){
                if (leptons_vector[i].Pt() <= 0) break;
                mtlmet_vector.push_back(sqrt( 2 * leptons_vector[i].Pt() * met.Pt() * (1 - cos(abs( DeltaPhi(leptons_vector[i].Phi(),met.Phi() ) ))))) ;
            }
        return mtlmet_vector;
        }
        """)
        df = df.Define(
            prefix + "WH3l_mtlmet",
            "_WH3l_isOk ? Get_mtlmet(Lepton_4DV,MET_4DV) : ROOT::RVecF(3, -9999.0)", 
        )

        ROOT.gInterpreter.Declare("""
        ROOT::RVecF Get_dphilmet(ROOT::VecOps::RVec<ROOT::Math::PtEtaPhiMVector> leptons_vector, ROOT::Math::PtEtaPhiMVector met){
            ROOT::RVecF dphilmet_vector;
            if (leptons_vector.size() < 3) return ROOT::RVecF(3, -9999.0);
            for (uint i = 0; i < 3; i++){
                if (leptons_vector[i].Pt() <= 0) break;
                dphilmet_vector.push_back( abs(DeltaPhi(leptons_vector[i].Phi(),met.Phi())) );
            }
        return dphilmet_vector;
        }
        """)
        df = df.Define(
            prefix + "WH3l_dphilmet",
            "_WH3l_isOk ? Get_dphilmet(Lepton_4DV,MET_4DV) : ROOT::RVecF(3, -9999.0)", 
        )

        ROOT.gInterpreter.Declare("""
        ROOT::RVecF Get_mOSll(ROOT::VecOps::RVec<ROOT::Math::PtEtaPhiMVector> leptons_vector, ROOT::RVecF leptons_pdgId){
            ROOT::RVecF mOSll_vector;
            if (leptons_vector.size() < 3) return ROOT::RVecF(3, -9999.0);
            for (uint i = 0; i < 3; i++){
                for (uint j = i; j < 3; j++){
                    if (leptons_pdgId[i]*leptons_pdgId[j] < 0)
                        mOSll_vector.push_back( (leptons_vector[i]+leptons_vector[j]).M() );
                    else
                        mOSll_vector.push_back(-9999.0);
                }
            }
        return mOSll_vector;
        }
        """)
        df = df.Define(
            prefix + "WH3l_mOSll",
            "_WH3l_isOk ? Get_mOSll(Lepton_4DV,Lepton_pdgId) : ROOT::RVecF(3, -9999.0)", 
            excludeVariations=["JES*", "MET*"],
        )

        ROOT.gInterpreter.Declare("""
        ROOT::RVecF Get_drOSll(ROOT::VecOps::RVec<ROOT::Math::PtEtaPhiMVector> leptons_vector, ROOT::RVecF leptons_pdgId){
            ROOT::RVecF drOSll_vector;
            if (leptons_vector.size() < 3) return ROOT::RVecF(3, -9999.0);
            for (uint i = 0; i < 3; i++){
                for (uint j = i; j < 3; j++){
                    if (leptons_pdgId[i]*leptons_pdgId[j] < 0)
                        drOSll_vector.push_back( DeltaR(leptons_vector[i].Eta(),leptons_vector[i].Phi(),leptons_vector[j].Eta(),leptons_vector[j].Phi() ) );
                    else
                        drOSll_vector.push_back(-9999.0);
                }
            }
        return drOSll_vector;
        }
        """)
        df = df.Define(
            prefix + "WH3l_drOSll",
            "_WH3l_isOk ? Get_drOSll(Lepton_4DV,Lepton_pdgId) : ROOT::RVecF(3, -9999.0)", 
            excludeVariations=["JES*", "MET*"],
        )

        ROOT.gInterpreter.Declare("""
        ROOT::RVecF Get_ptOSll(ROOT::VecOps::RVec<ROOT::Math::PtEtaPhiMVector> leptons_vector, ROOT::RVecF leptons_pdgId){
            ROOT::RVecF ptOSll_vector;
            if (leptons_vector.size() < 3) return ROOT::RVecF(3, -9999.0);
            for (uint i = 0; i < 3; i++){
                for (uint j = i; j < 3; j++){
                    if (leptons_pdgId[i]*leptons_pdgId[j] < 0)
                        ptOSll_vector.push_back( (leptons_vector[i]+leptons_vector[j]).Pt() );
                    else
                        ptOSll_vector.push_back(-9999.0);
                }
            }
        return ptOSll_vector;
        }
        """)
        df = df.Define(
            prefix + "WH3l_ptOSll",
            "_WH3l_isOk ? Get_ptOSll(Lepton_4DV,Lepton_pdgId) : ROOT::RVecF(3, -9999.0)", 
            excludeVariations=["JES*", "MET*"],
        )

        df = df.Define(
            prefix + "WH3l_chlll",
            "_WH3l_isOk ? abs(Lepton_pdgId[0])/Lepton_pdgId[0] + abs(Lepton_pdgId[1])/Lepton_pdgId[1] + abs(Lepton_pdgId[2])/Lepton_pdgId[2] : -9999.0", 
            excludeVariations=["JES*", "MET*"],
        )

        df = df.Define(
            prefix + "WH3l_mlll",
            "_WH3l_isOk ? (Lepton_4DV[0] + Lepton_4DV[1] + Lepton_4DV[2]).M() : -9999.0", 
            excludeVariations=["JES*", "MET*"],
        )

        df = df.Define(
            prefix + "WH3l_ptlll",
            "_WH3l_isOk ? (Lepton_4DV[0] + Lepton_4DV[1] + Lepton_4DV[2]).Pt() : -9999.0", 
            excludeVariations=["JES*", "MET*"],
        )

        df = df.Define(
            prefix + "WH3l_ptWWW",
            "_WH3l_isOk ? (Lepton_4DV[0] + Lepton_4DV[1] + Lepton_4DV[2] + MET_4DV).Pt() : -9999.0", 
        )

        df = df.Define(
            prefix + "WH3l_dphilllmet",
            "_WH3l_isOk ? DeltaPhi( (Lepton_4DV[0] + Lepton_4DV[1] + Lepton_4DV[2]).Phi(), MET_4DV.Phi()) : -9999.0", 
        )

        df = df.Define(
            prefix + "WH3l_mtWWW",
            "_WH3l_isOk ? sqrt(2*{0}WH3l_ptlll*MET_4DV.Pt()*(1. - cos({0}WH3l_dphilllmet))) : -9999.0".format(prefix), 
        )
        

        ROOT.gInterpreter.Declare("""
        float Get_ptW(ROOT::VecOps::RVec<ROOT::Math::PtEtaPhiMVector> leptons_vector, ROOT::RVecF leptons_pdgId){
            float dR = 9999.0;
            float mindR = 9999.0;
            float ptW = -9999.0;
            ROOT::RVecF ptOSll_vector;
            if (leptons_vector.size() < 3) return -9999.0;
            for (uint i = 0; i < 3; i++){
                for (uint j = i; j < 3; j++){
                    for (uint k = j; k < 3; k++){
                        if (leptons_pdgId[i]*leptons_pdgId[j] < 0){
                            dR = DeltaR(leptons_vector[i].Eta(),leptons_vector[i].Phi(),leptons_vector[j].Eta(),leptons_vector[j].Phi());
                            if (dR < mindR) {
                                mindR = dR;
                                ptW = leptons_vector[k].Pt();
                            }
                        }
                    }
                }
            }
        return ptW;
        }
        """)
        df = df.Define(
            prefix + "WH3l_ptW",
            "_WH3l_isOk ? Get_ptW(Lepton_4DV, Lepton_pdgId) : -9999.0", 
            excludeVariations=["JES*", "MET*"],
        )

        df = df.DropColumns("_WH3l_isOk")
        df = df.DropColumns("_isOk3l")
        df = df.DropColumns("l3_isOk")

        df = df.DropColumns("_lepOk")
        df = df.DropColumns("_tkMetOk")
        df = df.DropColumns("_jetOk")

        df = df.DropColumns("Lepton_4DV")
        df = df.DropColumns("CleanJet_4DV")
        df = df.DropColumns("MET_4DV")
        df = df.DropColumns("TkMET_4DV")

        return df
