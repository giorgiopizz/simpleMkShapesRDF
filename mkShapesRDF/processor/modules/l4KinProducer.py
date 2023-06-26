# Reference python module: https://github.com/latinos/LatinoAnalysis/blob/UL_production/NanoGardener/python/modules/l4KinProducer.py
# Actual variables definitions: https://github.com/latinos/LatinoAnalysis/blob/master/Gardener/python/variables/ZWWVar.C

from mkShapesRDF.processor.framework.module import Module


class l4KinProducer(Module):
    def __init__(self):
        super().__init__("l4KinProducer")

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

        # df = df.Define(
        #     "Lepton_charge", "ROOT::Math::PtEtaPhiMVector" "(TkMET_pt, 0, TkMET_phi, 0)"
        # )

        df = df.Define(
            "_isAllOk","Lepton_pt[Lepton_pt > 0].size() >= 4 ? (Lepton_pt[0] > 25 && Lepton_pt[1] > 15 && Lepton_pt[2] > 10 && Lepton_pt[3] > 10 && Lepton_pt[4] < 10) && ( abs(Lepton_pdgId[0])/Lepton_pdgId[0] + abs(Lepton_pdgId[1])/Lepton_pdgId[1] + abs(Lepton_pdgId[2])/Lepton_pdgId[2] + abs(Lepton_pdgId[3])/Lepton_pdgId[3] == 0) : 0"
        )

        # df = df.Define(
        #     "_isOk",
        #     "Lepton_pt[Lepton_pt > 0].size() >= 2 && MET_4DV.E()>0",
        #     excludeVariations=["JES*", "MET*"],
        # )

        # df = df.Define("_lepOk", "Lepton_pt[Lepton_pt > 0].size()")
        # df = df.Define("_tkMetOk", "TkMET_4DV.E() > 0")
        # df = df.Define("_jetOk", "CleanJet_pt[CleanJet_pt > 0].size()")

        # Variables yet to be implemented:
        ##############################

        # 'pfmetPhi_zh4l',
        # 'z0Mass_zh4l',
        # 'z0Pt_zh4l',
        # 'z1Mass_zh4l',
        # 'z1Pt_zh4l',
        # 'zaMass_zh4l',
        # 'zbMass_zh4l',
        # 'flagZ1SF_zh4l',
        # 'z0DeltaPhi_zh4l',
        # 'z1DeltaPhi_zh4l',
        # 'zaDeltaPhi_zh4l',
        # 'zbDeltaPhi_zh4l',
        # 'minDeltaPhi_zh4l',
        # 'z0DeltaR_zh4l',
        # 'z1DeltaR_zh4l',
        # 'zaDeltaR_zh4l',
        # 'zbDeltaR_zh4l',
        # 'lep1Mt_zh4l',
        # 'lep2Mt_zh4l',
        # 'lep3Mt_zh4l',
        # 'lep4Mt_zh4l',
        # 'minMt_zh4l',
        # 'z1Mt_zh4l',
        # 'mllll_zh4l',
        # 'chllll_zh4l',
        # 'z1dPhi_lep1MET_zh4l',
        # 'z1dPhi_lep2MET_zh4l',
        # 'z1mindPhi_lepMET_zh4l',

        # four-leptons variables
        prefix = "new_fw_"

        df = df.Define(
            prefix + "pfmetPhi_zh4l", "_isAllOk ? MET_4DV.Phi() : -9999.0"
        )


        df = df.DropColumns("Lepton_4DV")
        df = df.DropColumns("CleanJet_4DV")
        df = df.DropColumns("MET_4DV")
        df = df.DropColumns("TkMET_4DV")

        df = df.DropColumns("_isAllOk")

        return df
