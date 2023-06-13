from mkShapesRDF.processor.framework.module import Module

class l2KinProducer(Module):
    def __init__(self):
        super().__init__("l2KinProducer")

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
            "(CleanJet_pt, CleanJet_eta, CleanJet_phi, "
            "Take(Jet_mass, CleanJet_jetIdx))",
        )

        df = df.Define(
            "MET_4DV", "ROOT::Math::PtEtaPhiMVector" "(PuppiMET_pt, 0, PuppiMET_phi, 0)"
        )

        df = df.Define(
            "TkMET_4DV", "ROOT::Math::PtEtaPhiMVector" "(TkMET_pt, 0, TkMET_phi, 0)"
        )

        df = df.Define(
            "_isOk",
            "Lepton_pt[Lepton_pt > 0].size() >= 2 && MET_4DV.E()>0",
            excludeVariations=["JES*", "MET*"],
        )

        df = df.Define("_lepOk", "Lepton_pt[Lepton_pt > 0].size()")
        df = df.Define("_tkMetOk", "TkMET_4DV.E() > 0")
        df = df.Define("_jetOk", "CleanJet_pt[CleanJet_pt > 0].size()")

        # FIXME complete l2kin module!

        # Variables to be implemented:
        ##############################

        #            'mcoll',
        #            'mcollWW',
        #            'mTe',
        #            'choiMass',
        #            'mT2',
        #            'channel',
        #            'mllWgSt',
        #            'drllWgSt',
        #            'mllThird',
        #            'mllOneThree',
        #            'mllTwoThree',
        #            'drllOneThree',
        #            'drllTwoThree',
        #            'ht',
        #            'vht_pt',
        #            'vht_phi',                   
        #            'PfMetDivSumMet',
        #            'upara',
        #            'uperp',

        # dilepton variables
        prefix = "new_fw_"
        df = df.Define(
            prefix + "mll", 
            "_isOk ? (Lepton_4DV[0] + Lepton_4DV[1]).M() : -9999.0"
        )
        df = df.Define(
            prefix + "dphill",
            "_isOk ? DeltaPhi(Lepton_phi[0], Lepton_phi[1]) : -9999.0",
        )
        df = df.Define(
            prefix + "yll", 
            "_isOk ? (Lepton_4DV[0] + Lepton_4DV[1]).Rapidity() : -9999.0"
        )
        df = df.Define(
            prefix + "ptll", 
            "_isOk ? (Lepton_4DV[0] + Lepton_4DV[1]).Pt() : -9999.0"
        )
        df = df.Define(
            prefix + "dphillmet",
            "_isOk ? abs(DeltaPhi((Lepton_4DV[0] + Lepton_4DV[1]).Phi(),MET_4DV.Phi())) : -9999.0"
        )
        df = df.Define(
            prefix + "mth",
            "_isOk ? sqrt(2. * {0}ptll * MET_4DV.Pt() * (1. - cos({0}dphillmet))) : -9999.0".format(prefix)
        )
        df = df.Define(
            prefix + "mTi",
            "_isOk ? (Lepton_4DV[0] + Lepton_4DV[1] + MET_4DV).M() : -9999.0",
        )
        df = df.Define(
            prefix + "mR",
            "_isOk ? sqrt(0.5*({0}mll*{0}mll - MET_4DV.Pt()*{0}ptll*cos({0}dphillmet) + sqrt(({0}mll*{0}mll + {0}ptll*{0}ptll)*({0}mll*{0}mll + MET_4DV.Pt()*MET_4DV.Pt())))) : -9999.0".format(prefix)
        )
        df = df.Define(
            prefix + "drll",
            "_isOk ? DeltaR(Lepton_eta[0], Lepton_eta[1], Lepton_phi[0], Lepton_phi[1]) : -9999.0",
        )
        df = df.Define(
            prefix + "detall", 
            "_isOk ? abs(Lepton_eta[0] - Lepton_eta[1]) : -9999.0"
        )
        df = df.Define(
            prefix + "dphilmet",
            "_isOk ? abs(DeltaPhi(Lepton_4DV[0].Phi(), MET_4DV.Phi())) < abs(DeltaPhi(Lepton_4DV[1].Phi(), MET_4DV.Phi())) ? abs(DeltaPhi(Lepton_4DV[0].Phi(), MET_4DV.Phi())) : abs(DeltaPhi(Lepton_4DV[1].Phi(), MET_4DV.Phi())) : -9999.0"
        )
        df = df.Define(
            prefix + "dphilmet1",
            "Lepton_4DV[0].Pt() > 0 && MET_4DV.E() > 0 ? abs(DeltaPhi(Lepton_4DV[0].Phi(), MET_4DV.Phi())) : -9999.0"
        )
        df = df.Define(
            prefix + "dphilmet2",
            "_isOk ? abs(DeltaPhi(Lepton_4DV[1].Phi(), MET_4DV.Phi())) : -9999.0"
        )
        df = df.Define(
            prefix + "mtw1",
            "Lepton_4DV[0].Pt() > 0 && MET_4DV.E() > 0 ? sqrt(2. * Lepton_4DV[0].Pt() * MET_4DV.Pt() * (1. - cos({0}dphilmet1))) : -9999.0".format(prefix)
        )
        df = df.Define(
            prefix + "mtw2",
            "_isOk ? sqrt(2. * Lepton_4DV[1].Pt() * MET_4DV.Pt() * (1. - cos({0}dphilmet2))) : -9999.0".format(prefix)
        )
        df = df.Define(
            prefix + "projpfmet",
            "_isOk ? {0}dphilmet < 0.5*TMath::Pi() ? sin({0}dphilmet) * MET_4DV.Pt() : MET_4DV.Pt() : -9999.0".format(prefix)
        )
        df = df.Define(
            prefix + "dphil1tkmet",
            "_isOk && _tkMetOk ? abs(DeltaPhi(Lepton_4DV[0].Phi(), TkMET_4DV.Phi())) : -9999.0"
        )
        df = df.Define(
            prefix + "dphil2tkmet",
            "_isOk && _tkMetOk ? abs(DeltaPhi(Lepton_4DV[1].Phi(), TkMET_4DV.Phi())) : -9999.0"
        )
        df = df.Define(
            prefix + "dphiltkmet",
            "_isOk && _tkMetOk ? min({0}dphil1tkmet, {0}dphil2tkmet) : -9999.0".format(prefix)
        )
        df = df.Define(
            prefix + "projtkmet",
            "_isOk && _tkMetOk ? {0}dphiltkmet < 0.5*TMath::Pi() ? sin({0}dphiltkmet) * TkMET_4DV.Pt() : TkMET_4DV.Pt() : -9999.0".format(prefix)
        )
        df = df.Define(
            prefix + "projtkmet",
            "_isOk && _tkMetOk ? min({0}projtkmet, {0}projpfmet) : -9999.0".format(prefix)
        )
        df = df.Define(
            prefix + "pTWW",
            "_isOk ? (Lepton_4DV[0] + Lepton_4DV[1] + MET_4DV).Pt() : -9999.0"
        )
        df = df.Define(
            prefix + "pTHjj",
            "_isOk && _jetOk>=2 ? (Lepton_4DV[0] + Lepton_4DV[1] + CleanJet_4DV[0] + CleanJet_4DV[1] + MET_4DV).Pt() : -9999.0"
        )
        df = df.Define(
            prefix + "recoil",
            "_isOk ? abs((Lepton_4DV[0] + Lepton_4DV[1] + MET_4DV).Pt()) : -9999.0"
        )

        df = df.Define(prefix + "pt1", "Lepton_pt[0] > 0 ? Lepton_pt[0] : -9999.0")
        df = df.Define(prefix + "eta1", "Lepton_pt[0] > 0 ? Lepton_eta[0] : -9999.0")
        df = df.Define(prefix + "phi1", "Lepton_pt[0] > 0 ? Lepton_phi[0] : -9999.0")
        df = df.Define(prefix + "pt2", "_isOk ? Lepton_pt[1] : -9999.0")
        df = df.Define(prefix + "eta2", "_isOk ? Lepton_eta[1] : -9999.0")
        df = df.Define(prefix + "phi2", "_isOk ? Lepton_phi[1] : -9999.0")


        # Lepton(s)-Jet(s) variables
        df = df.Define(
            prefix + "dphilljet",
            "_isOk && _jetOk>=1 ? abs(DeltaPhi((Lepton_4DV[0] + Lepton_4DV[1]).Phi(), CleanJet_4DV[0].Phi())) : -9999.0"
        )
        df = df.Define(
            prefix + "dphilljetjet",
            "_isOk && _jetOk>=2 ? abs(DeltaPhi((Lepton_4DV[0] + Lepton_4DV[1]).Phi(), (CleanJet_4DV[0] + CleanJet_4DV[1]).Phi())) : -9999.0"
        )
        df = df.Define(
            prefix + "dphilljetjet_cut",
            "_isOk && _jetOk>=2 && CleanJet_4DV[0].Pt()>15.0 && CleanJet_4DV[1].Pt()>15.0 ? abs(DeltaPhi((Lepton_4DV[0] + Lepton_4DV[1]).Phi(), (CleanJet_4DV[0] + CleanJet_4DV[1]).Phi())) : -9999.0"
        )
        df = df.Define(
            prefix + "dphijet1met",
            "_isOk && _jetOk>=1 ? abs(DeltaPhi(CleanJet_4DV[0].Phi(), MET_4DV.Phi())) : -9999.0"
        )
        df = df.Define(
            prefix + "dphijet2met",
            "_isOk && _jetOk>=2 ? abs(DeltaPhi(CleanJet_4DV[1].Phi(), MET_4DV.Phi())) : -9999.0"
        )
        df = df.Define(
            prefix + "dphilep1jet1",
            "_isOk && _jetOk>=1 ? abs(DeltaPhi(Lepton_4DV[0].Phi(), CleanJet_4DV[0].Phi())) : -9999.0"
        )
        df = df.Define(
            prefix + "dphilep1jet2",
            "_isOk && _jetOk>=2 ? abs(DeltaPhi(Lepton_4DV[0].Phi(), CleanJet_4DV[1].Phi())) : -9999.0"
        )
        df = df.Define(
            prefix + "dphilep2jet1",
            "_isOk && _jetOk>=1 ? abs(DeltaPhi(Lepton_4DV[1].Phi(), CleanJet_4DV[0].Phi())) : -9999.0"
        )
        df = df.Define(
            prefix + "dphilep2jet2",
            "_isOk && _jetOk>=2 ? abs(DeltaPhi(Lepton_4DV[1].Phi(), CleanJet_4DV[1].Phi())) : -9999.0"
        )
        df = df.Define(
            prefix + "detaj1l1",
            "_isOk && _jetOk>=1 ? abs(CleanJet_eta[0] - Lepton_eta[0]) : -9999.0"
        )
        df = df.Define(
            prefix + "detaj1l2",
            "_isOk && _jetOk>=1 ? abs(CleanJet_eta[0] - Lepton_eta[1]) : -9999.0"
        )
        df = df.Define(
            prefix + "detaj2l1",
            "_isOk && _jetOk>=2 ? abs(CleanJet_eta[1] - Lepton_eta[0]) : -9999.0"
        )
        df = df.Define(
            prefix + "detaj2l2",
            "_isOk && _jetOk>=2 ? abs(CleanJet_eta[1] - Lepton_eta[1]) : -9999.0"
        )
        df = df.Define(
            prefix + "mindetajl",
            "_isOk && _jetOk>=2 ? min({0}detaj1l1, min({0}detaj1l2, min({0}detaj2l1, {0}detaj2l2))) : -9999.0".format(prefix)
        )
        df = df.Define(
            prefix + "dphilep1jj",
            "_isOk && _jetOk>=2 ? abs(DeltaPhi( Lepton_4DV[0].Phi(), (CleanJet_4DV[0] + CleanJet_4DV[1]).Phi() ) ) : -9999.0"
        )
        df = df.Define(
            prefix + "dphilep2jj",
            "_isOk && _jetOk>=2 ? abs(DeltaPhi(Lepton_4DV[1].Phi(), (CleanJet_4DV[0] + CleanJet_4DV[1]).Phi())) : -9999.0"
        )
        df = df.Define(
            prefix + "maxdphilepjj",
            "_isOk && _jetOk>=2 ? max({0}dphilep1jj, {0}dphilep2jj) : -9999.0".format(prefix)
        )
        df = df.Define(
            prefix + "dphilljet_cut",
            "_isOk && _jetOk>=1 && CleanJet_4DV[0].Pt()>15.0 ? abs(DeltaPhi((Lepton_4DV[0] + Lepton_4DV[1]).Phi(), CleanJet_4DV[0].Phi())) : -9999.0"
        )
        df = df.Define(
            prefix + "dphijet1met_cut",
            "_isOk && _jetOk>=1 && CleanJet_4DV[0].Pt()>15.0 ? abs(DeltaPhi(CleanJet_4DV[0].Phi(), MET_4DV.Phi())) : -9999.0"
        )
        df = df.Define(
            prefix + "dphijet2met_cut",
            "_isOk && _jetOk>=2 && CleanJet_4DV[1].Pt()>15.0 ? abs(DeltaPhi(CleanJet_4DV[1].Phi(), MET_4DV.Phi())) : -9999.0"
        )

        # dijets variables
        df = df.Define(
            prefix + "njet",
            "CleanJet_pt [CleanJet_pt > 30 && CleanJet_eta < 4.7].size()"
        )
        df = df.Define(
            prefix + "ptjj",
            "_jetOk >=2 ? (CleanJet_4DV[0] + CleanJet_4DV[1]).Pt() : -9999.0"
        )
        df = df.Define(
            prefix + "mjj",
            "_jetOk >=2 ? (CleanJet_4DV[0] + CleanJet_4DV[1]).M() : -9999.0"
        )
        df = df.Define(
            prefix + "dphijj",
            "_jetOk >= 2 ? DeltaPhi(CleanJet_phi[0], CleanJet_phi[1]) : -9999.0"
        )
        df = df.Define(
            prefix + "drjj",
            "_isOk ? DeltaR(CleanJet_eta[0], CleanJet_eta[1], CleanJet_phi[0], CleanJet_phi[1]) : -9999.0"
        )
        df = df.Define(
            prefix + "detajj",
            "_jetOk >=2 ? abs(CleanJet_eta[0] - CleanJet_eta[1]) : -9999.0"
        )
        df = df.Define(
            prefix + "dphijjmet",
            "_isOk && _jetOk>=2 ? abs(DeltaPhi((CleanJet_4DV[0] + CleanJet_4DV[1]).Phi(),MET_4DV.Phi())) : -9999.0"
        )
        df = df.Define(
            prefix + "dphijjmet_cut",
            "_isOk && _jetOk>=2 && CleanJet_4DV[0].Pt()>15.0 && CleanJet_4DV[1].Pt()>15.0 ? abs(DeltaPhi((CleanJet_4DV[0] + CleanJet_4DV[1]).Phi(),MET_4DV.Phi())) : -9999.0"
        )
        df = df.Define(
            prefix + "jetpt1_cut",
            "_isOk && _jetOk>=1 && CleanJet_4DV[0].Pt()>15.0 ? CleanJet_4DV[0].Pt() : -9999.0"
        )
        df = df.Define(
            prefix + "jetpt2_cut",
            "_isOk && _jetOk>=2 && CleanJet_4DV[0].Pt()>15.0 && CleanJet_4DV[1].Pt()>15.0 ? CleanJet_4DV[1].Pt() : -9999.0"
        )
        df = df.Define(
            prefix + "m2ljj20",
            "_isOk && _jetOk>=1 && CleanJet_4DV[0].Pt()>30.0 ? CleanJet_4DV[1].Pt()>20.0 ? (Lepton_4DV[0] + Lepton_4DV[1] + CleanJet_4DV[0] + CleanJet_4DV[1]).M() : (Lepton_4DV[0] + Lepton_4DV[1] + CleanJet_4DV[0]).M() : -9999.0"
        )
        df = df.Define(
            prefix + "m2ljj30",
            "_isOk && _jetOk>=1 && CleanJet_4DV[0].Pt()>30.0 ? CleanJet_4DV[1].Pt()>30.0 ? (Lepton_4DV[0] + Lepton_4DV[1] + CleanJet_4DV[0] + CleanJet_4DV[1]).M() : (Lepton_4DV[0] + Lepton_4DV[1] + CleanJet_4DV[0]).M() : -9999.0"
        )

        # For VBF training
        df = df.Define(
            prefix + "ptTOT_cut",
            "_isOk && _jetOk>=2 && CleanJet_4DV[0].Pt()>15.0 && CleanJet_4DV[1].Pt()>15.0 ? (Lepton_4DV[0] + Lepton_4DV[1] + CleanJet_4DV[0] + CleanJet_4DV[1] + MET_4DV).Pt() : -9999.0"
        )
        df = df.Define(
            prefix + "mTOT_cut",
            "_isOk && _jetOk>=2 && CleanJet_4DV[0].Pt()>15.0 && CleanJet_4DV[1].Pt()>15.0 ? (Lepton_4DV[0] + Lepton_4DV[1] + CleanJet_4DV[0] + CleanJet_4DV[1] + MET_4DV).M() : -9999.0"
        )
        df = df.Define(
            prefix + "OLV1_cut",
            "_isOk && _jetOk>=2 && CleanJet_4DV[0].Pt()>15.0 && CleanJet_4DV[1].Pt()>15.0 ? 2*(Lepton_4DV[0].Eta() - 0.5*((CleanJet_4DV[0] + CleanJet_4DV[1]).Eta())) / ((CleanJet_4DV[0] - CleanJet_4DV[1]).Eta()) : -9999.0"
        )
        df = df.Define(
            prefix + "OLV2_cut",
            "_isOk && _jetOk>=2 && CleanJet_4DV[0].Pt()>15.0 && CleanJet_4DV[1].Pt()>15.0 ? 2*(Lepton_4DV[1].Eta() - 0.5*((CleanJet_4DV[0] + CleanJet_4DV[1]).Eta())) / ((CleanJet_4DV[0] - CleanJet_4DV[1]).Eta()) : -9999.0"
        )
        df = df.Define(
            prefix + "Ceta_cut",
            "_isOk && _jetOk>=2 && CleanJet_4DV[0].Pt()>15.0 && CleanJet_4DV[1].Pt()>15.0 ? {0}OLV1_cut + {0}OLV2_cut : -9999.0".format(prefix)
        )

        # WHSS
        #            'mlljj20_whss',
        #            'mlljj30_whss',
        #            'WlepPt_whss',
        #            'WlepMt_whss'



        df = df.DropColumns("Lepton_4DV")
        df = df.DropColumns("CleanJet_4DV")
        df = df.DropColumns("MET_4DV")
        df = df.DropColumns("TkMET_4DV")

        df = df.DropColumns("_isOk")
        df = df.DropColumns("_lepOk")
        df = df.DropColumns("_tkMetOk")
        df = df.DropColumns("_jetOk")

        return df
