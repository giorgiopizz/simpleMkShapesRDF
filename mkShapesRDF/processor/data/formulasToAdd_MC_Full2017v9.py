# Formulas to be added, in python language.
# Call to branches have to be in the form branchName (i.e. no "event.").
# If you want to use logical operators, the have to be the c++ ones (i.e "&&" not " and ")

from mkShapesRDF.processor.data.LeptonSel_cfg import ElectronWP
from mkShapesRDF.processor.data.LeptonSel_cfg import MuonWP

formulas = {}

# from https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2#2018_2017_data_and_MC_UL

METFilter_Common = """(
                    Flag_goodVertices*
                    Flag_globalSuperTightHalo2016Filter*
                    Flag_HBHENoiseFilter*
                    Flag_HBHENoiseIsoFilter*
                    Flag_EcalDeadCellTriggerPrimitiveFilter*
                    Flag_BadPFMuonFilter*
                    Flag_BadPFMuonDzFilter*
                    Flag_ecalBadCalibFilter
                    )"""

METFilter_DATA = METFilter_Common + "*" + "(Flag_eeBadScFilter)"

formulas["METFilter_MC"] = METFilter_DATA

# Common Weights


if "genWeight" in df.GetColumnNames():
    formulas["XSWeight"] = "baseW*genWeight"
else:
    formulas["XSWeight"] = "baseW"


formulas["SFweight2l"] = """(nLepton > 1) ? (puWeight*
                              (HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL ||
                               HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ ||
                               HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ ||
                               HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ ||
                               HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8 ||
                               HLT_IsoMu27 ||
                               HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL ||
                               HLT_Ele35_WPTight_Gsf )*
                             TriggerSFWeight_2l*
                             Lepton_RecoSF[0]*
                             Lepton_RecoSF[1]*
                             EMTFbug_veto) : 0.0
                          """

formulas["SFweight3l"] = """(nLepton > 2) ? (puWeight*
                              (HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL ||
                               HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ ||
                               HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ ||
                               HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ ||
                               HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8 ||
                               HLT_IsoMu27 ||
                               HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL ||
                               HLT_Ele35_WPTight_Gsf)*
                             TriggerSFWeight_3l*
                             Lepton_RecoSF[0]*
                             Lepton_RecoSF[1]*
                             Lepton_RecoSF[2]*
                             EMTFbug_veto) : 0.0
                         """

formulas["SFweight4l"] = """(nLepton > 3) ? (puWeight*
                              (HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL ||
                               HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ ||
                               HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ ||
                               HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ ||
                               HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8 ||
                               HLT_IsoMu27 ||
                               HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL ||
                               HLT_Ele35_WPTight_Gsf)*
                             TriggerSFWeight_4l*
                             Lepton_RecoSF[0]*
                             Lepton_RecoSF[1]*
                             Lepton_RecoSF[2]*
                             Lepton_RecoSF[3]*
                             EMTFbug_veto) : 0.0
                         """

## MonoHiggs
if "MHTriggerEffWeight_2l" in df.GetColumnNames():
    # # MonoHiggs
    formulas["SFweight2lMH"] = """(nLepton > 1) ? 
                                  (puWeight*
                                   MHTriggerEffWeight_2l*
                                   Lepton_RecoSF[0]*
                                   Lepton_RecoSF[1]*
                                   EMTFbug_veto) : 0.0
                               """
else:
    formulas["SFweight2lMH"] = "0.0"

# Lepton WP
muWPlist = [wp for wp in MuonWP["Full2017v9"]["TightObjWP"]]
eleWPlist = [wp for wp in ElectronWP["Full2017v9"]["TightObjWP"]]

for eleWP in eleWPlist:
  for muWP in muWPlist:

    formulas[f"LepSF2l__ele_{eleWP}__mu_{muWP}"] = f"""(nLepton > 1) ? 
                                                       Lepton_tightElectron_{eleWP}_IdIsoSF[0]*
                                                       Lepton_tightElectron_{eleWP}_IdIsoSF[1]*
                                                       Lepton_tightMuon_{muWP}_IdIsoSF[0]*
                                                       Lepton_tightMuon_{muWP}_IdIsoSF[1] 
                                                       : 0.0 
                                                    """
  
    formulas[f"LepSF3l__ele_{eleWP}__mu_{muWP}"] = f"""(nLepton > 2) ?
                                                       Lepton_tightElectron_{eleWP}_IdIsoSF[0]*
                                                       Lepton_tightElectron_{eleWP}_IdIsoSF[1]*
                                                       Lepton_tightElectron_{eleWP}_IdIsoSF[2]*
                                                       Lepton_tightMuon_{muWP}_IdIsoSF[0]*
                                                       Lepton_tightMuon_{muWP}_IdIsoSF[1]*
                                                       Lepton_tightMuon_{muWP}_IdIsoSF[2]
                                                       : 0.0
                                                    """
  
    formulas[f"LepSF4l__ele_{eleWP}__mu_{muWP}"] = f"""(nLepton > 3) ?
                                                       Lepton_tightElectron_{eleWP}_IdIsoSF[0]*
                                                       Lepton_tightElectron_{eleWP}_IdIsoSF[1]*
                                                       Lepton_tightElectron_{eleWP}_IdIsoSF[2]*
                                                       Lepton_tightElectron_{eleWP}_IdIsoSF[3]*
                                                       Lepton_tightMuon_{muWP}_IdIsoSF[0]*
                                                       Lepton_tightMuon_{muWP}_IdIsoSF[1]*
                                                       Lepton_tightMuon_{muWP}_IdIsoSF[2]*
                                                       Lepton_tightMuon_{muWP}_IdIsoSF[3]
                                                       : 0.0
                                                    """
  
    formulas[f"LepCut2l__ele_{eleWP}__mu_{muWP}"] = f"""(nLepton > 1) ? 
                                                        ((Lepton_isTightElectron_{eleWP}[0]>0.5 || Lepton_isTightMuon_{muWP}[0]>0.5) &&
                                                         (Lepton_isTightElectron_{eleWP}[1]>0.5 || Lepton_isTightMuon_{muWP}[1]>0.5))
                                                        : 0.0
                                                     """

  
    formulas[f"LepCut3l__ele_{eleWP}__mu_{muWP}"] = f"""(nLepton > 2) ? 
                                                        ((Lepton_isTightElectron_{eleWP}[0]>0.5 || Lepton_isTightMuon_{muWP}[0]>0.5) &&
                                                         (Lepton_isTightElectron_{eleWP}[1]>0.5 || Lepton_isTightMuon_{muWP}[1]>0.5) &&
                                                         (Lepton_isTightElectron_{eleWP}[2]>0.5 || Lepton_isTightMuon_{muWP}[2]>0.5))
                                                        : 0.0
                                                    """
  
    formulas[f"LepCut4l__ele_{eleWP}__mu_{muWP}"] = f"""(nLepton > 3) ?
                                                        ((Lepton_isTightElectron_{eleWP}[0]>0.5 || Lepton_isTightMuon_{muWP}[0]>0.5) &&
                                                         (Lepton_isTightElectron_{eleWP}[1]>0.5 || Lepton_isTightMuon_{muWP}[1]>0.5) &&
                                                         (Lepton_isTightElectron_{eleWP}[2]>0.5 || Lepton_isTightMuon_{muWP}[2]>0.5) &&
                                                         (Lepton_isTightElectron_{eleWP}[3]>0.5 || Lepton_isTightMuon_{muWP}[3]>0.5))
                                                        : 0.0
                                                     """

for eleWP in eleWPlist:

  formulas[f"LepSF2l__ele_{eleWP}__Up"] = f"""(nLepton > 1) ?
                                              ((abs(Lepton_pdgId[0]) == 11)*(Lepton_tightElectron_{eleWP}_TotSF_Up[0])/(Lepton_tightElectron_{eleWP}_TotSF[0])+
                                               (abs(Lepton_pdgId[0]) == 13)) * 
                                              ((abs(Lepton_pdgId[1]) == 11)*(Lepton_tightElectron_{eleWP}_TotSF_Up[1])/(Lepton_tightElectron_{eleWP}_TotSF[1])+
                                               (abs(Lepton_pdgId[1]) == 13)) 
                                              : 0.0
                                           """

  formulas[f"LepSF2l__ele_{eleWP}__Do"] = f"""(nLepton > 1) ?
                                              ((abs(Lepton_pdgId[0]) == 11)*(Lepton_tightElectron_{eleWP}_TotSF_Down[0])/(Lepton_tightElectron_{eleWP}_TotSF[0])+
                                               (abs(Lepton_pdgId[0]) == 13)) * 
                                              ((abs(Lepton_pdgId[1]) == 11)*(Lepton_tightElectron_{eleWP}_TotSF_Down[1])/(Lepton_tightElectron_{eleWP}_TotSF[1])+
                                               (abs(Lepton_pdgId[1]) == 13)) 
                                              : 0.0
                                           """

  formulas[f"LepSF3l__ele_{eleWP}__Up"] = f"""(nLepton > 2) ?
                                              ((abs(Lepton_pdgId[0]) == 11)*(Lepton_tightElectron_{eleWP}_TotSF_Up[0])/(Lepton_tightElectron_{eleWP}_TotSF[0])+
                                               (abs(Lepton_pdgId[0]) == 13)) *
                                              ((abs(Lepton_pdgId[1]) == 11)*(Lepton_tightElectron_{eleWP}_TotSF_Up[1])/(Lepton_tightElectron_{eleWP}_TotSF[1])+
                                               (abs(Lepton_pdgId[1]) == 13)) *
                                              ((abs(Lepton_pdgId[2]) == 11)*(Lepton_tightElectron_{eleWP}_TotSF_Up[2])/(Lepton_tightElectron_{eleWP}_TotSF[2])+
                                               (abs(Lepton_pdgId[2]) == 13))
                                              : 0.0
                                           """

  formulas[f"LepSF3l__ele_{eleWP}__Do"] = f"""(nLepton > 2) ?
                                              ((abs(Lepton_pdgId[0]) == 11)*(Lepton_tightElectron_{eleWP}_TotSF_Down[0])/(Lepton_tightElectron_{eleWP}_TotSF[0])+
                                               (abs(Lepton_pdgId[0]) == 13)) *
                                              ((abs(Lepton_pdgId[1]) == 11)*(Lepton_tightElectron_{eleWP}_TotSF_Down[1])/(Lepton_tightElectron_{eleWP}_TotSF[1])+
                                               (abs(Lepton_pdgId[1]) == 13)) *
                                              ((abs(Lepton_pdgId[2]) == 11)*(Lepton_tightElectron_{eleWP}_TotSF_Down[2])/(Lepton_tightElectron_{eleWP}_TotSF[2])+
                                               (abs(Lepton_pdgId[2]) == 13))
                                              : 0.0
                                           """

  formulas[f"LepSF4l__ele_{eleWP}__Up"] = f"""(nLepton > 3) ?
                                              ((abs(Lepton_pdgId[0]) == 11)*(Lepton_tightElectron_{eleWP}_TotSF_Up[0])/(Lepton_tightElectron_{eleWP}_TotSF[0])+
                                               (abs(Lepton_pdgId[0]) == 13)) *
                                              ((abs(Lepton_pdgId[1]) == 11)*(Lepton_tightElectron_{eleWP}_TotSF_Up[1])/(Lepton_tightElectron_{eleWP}_TotSF[1])+
                                               (abs(Lepton_pdgId[1]) == 13)) *
                                              ((abs(Lepton_pdgId[2]) == 11)*(Lepton_tightElectron_{eleWP}_TotSF_Up[2])/(Lepton_tightElectron_{eleWP}_TotSF[2])+
                                               (abs(Lepton_pdgId[2]) == 13)) *
                                              ((abs(Lepton_pdgId[3]) == 11)*(Lepton_tightElectron_{eleWP}_TotSF_Up[3])/(Lepton_tightElectron_{eleWP}_TotSF[3])+
                                               (abs(Lepton_pdgId[3]) == 13))
                                              : 0.0
                                           """

  formulas[f"LepSF4l__ele_{eleWP}__Do"] = f"""(nLepton > 3) ?
                                              ((abs(Lepton_pdgId[0]) == 11)*(Lepton_tightElectron_{eleWP}_TotSF_Down[0])/(Lepton_tightElectron_{eleWP}_TotSF[0])+
                                               (abs(Lepton_pdgId[0]) == 13)) *
                                              ((abs(Lepton_pdgId[1]) == 11)*(Lepton_tightElectron_{eleWP}_TotSF_Down[1])/(Lepton_tightElectron_{eleWP}_TotSF[1])+
                                               (abs(Lepton_pdgId[1]) == 13)) *
                                              ((abs(Lepton_pdgId[2]) == 11)*(Lepton_tightElectron_{eleWP}_TotSF_Down[2])/(Lepton_tightElectron_{eleWP}_TotSF[2])+
                                               (abs(Lepton_pdgId[2]) == 13)) *
                                              ((abs(Lepton_pdgId[3]) == 11)*(Lepton_tightElectron_{eleWP}_TotSF_Down[3])/(Lepton_tightElectron_{eleWP}_TotSF[3])+
                                               (abs(Lepton_pdgId[3]) == 13))
                                              : 0.0
                                           """

for muWP in muWPlist:
  formulas[f"LepSF2l__mu_{muWP}__Up"] = f"""(nLepton > 1) ?
                                            ((abs(Lepton_pdgId[0]) == 13)*(Lepton_tightMuon_{muWP}_TotSF_Up[0])/(Lepton_tightMuon_{muWP}_TotSF[0])+
                                             (abs(Lepton_pdgId[0]) == 11)) *
                                            ((abs(Lepton_pdgId[1]) == 13)*(Lepton_tightMuon_{muWP}_TotSF_Up[1])/(Lepton_tightMuon_{muWP}_TotSF[1])+
                                             (abs(Lepton_pdgId[1]) == 11))
                                            : 0.0
                                         """
  
  formulas[f"LepSF2l__mu_{muWP}__Do"] = f"""(nLepton > 1) ?
                                            ((abs(Lepton_pdgId[0]) == 13)*(Lepton_tightMuon_{muWP}_TotSF_Down[0])/(Lepton_tightMuon_{muWP}_TotSF[0])+
                                             (abs(Lepton_pdgId[0]) == 11)) *
                                            ((abs(Lepton_pdgId[1]) == 13)*(Lepton_tightMuon_{muWP}_TotSF_Down[1])/(Lepton_tightMuon_{muWP}_TotSF[1])+
                                             (abs(Lepton_pdgId[1]) == 11))
                                            : 0.0
                                         """
                                          
  formulas[f"LepSF3l__mu_{muWP}__Up"] = f"""(nLepton > 2) ?
                                            ((abs(Lepton_pdgId[0]) == 13)*(Lepton_tightMuon_{muWP}_TotSF_Up[0])/(Lepton_tightMuon_{muWP}_TotSF[0])+
                                             (abs(Lepton_pdgId[0]) == 11)) *
                                            ((abs(Lepton_pdgId[1]) == 13)*(Lepton_tightMuon_{muWP}_TotSF_Up[1])/(Lepton_tightMuon_{muWP}_TotSF[1])+
                                             (abs(Lepton_pdgId[1]) == 11)) *
                                            ((abs(Lepton_pdgId[2]) == 13)*(Lepton_tightMuon_{muWP}_TotSF_Up[2])/(Lepton_tightMuon_{muWP}_TotSF[2])+
                                             (abs(Lepton_pdgId[2]) == 11))
                                            : 0.0
                                         """
  
  formulas[f"LepSF3l__mu_{muWP}__Do"] = f"""(nLepton > 2) ?
                                            ((abs(Lepton_pdgId[0]) == 13)*(Lepton_tightMuon_{muWP}_TotSF_Down[0])/(Lepton_tightMuon_{muWP}_TotSF[0])+
                                             (abs(Lepton_pdgId[0]) == 11)) *
                                            ((abs(Lepton_pdgId[1]) == 13)*(Lepton_tightMuon_{muWP}_TotSF_Down[1])/(Lepton_tightMuon_{muWP}_TotSF[1])+
                                             (abs(Lepton_pdgId[1]) == 11)) *
                                            ((abs(Lepton_pdgId[2]) == 13)*(Lepton_tightMuon_{muWP}_TotSF_Down[2])/(Lepton_tightMuon_{muWP}_TotSF[2])+
                                             (abs(Lepton_pdgId[2]) == 11))
                                            : 0.0
                                         """
  
  formulas[f"LepSF4l__mu_{muWP}__Up"] = f"""(nLepton > 3) ?
                                            ((abs(Lepton_pdgId[0]) == 13)*(Lepton_tightMuon_{muWP}_TotSF_Up[0])/(Lepton_tightMuon_{muWP}_TotSF[0])+
                                             (abs(Lepton_pdgId[0]) == 11)) *
                                            ((abs(Lepton_pdgId[1]) == 13)*(Lepton_tightMuon_{muWP}_TotSF_Up[1])/(Lepton_tightMuon_{muWP}_TotSF[1])+
                                             (abs(Lepton_pdgId[1]) == 11)) *
                                            ((abs(Lepton_pdgId[2]) == 13)*(Lepton_tightMuon_{muWP}_TotSF_Up[2])/(Lepton_tightMuon_{muWP}_TotSF[2])+
                                             (abs(Lepton_pdgId[2]) == 11)) *
                                            ((abs(Lepton_pdgId[3]) == 13)*(Lepton_tightMuon_{muWP}_TotSF_Up[3])/(Lepton_tightMuon_{muWP}_TotSF[3])+
                                             (abs(Lepton_pdgId[3]) == 11))
                                            : 0.0
                                         """
  
  formulas[f"LepSF4l__mu_{muWP}__Do"] = f"""(nLepton > 3) ?
                                            ((abs(Lepton_pdgId[0]) == 13)*(Lepton_tightMuon_{muWP}_TotSF_Down[0])/(Lepton_tightMuon_{muWP}_TotSF[0])+
                                             (abs(Lepton_pdgId[0]) == 11)) *
                                            ((abs(Lepton_pdgId[1]) == 13)*(Lepton_tightMuon_{muWP}_TotSF_Down[1])/(Lepton_tightMuon_{muWP}_TotSF[1])+
                                             (abs(Lepton_pdgId[1]) == 11)) *
                                            ((abs(Lepton_pdgId[2]) == 13)*(Lepton_tightMuon_{muWP}_TotSF_Down[2])/(Lepton_tightMuon_{muWP}_TotSF[2])+
                                             (abs(Lepton_pdgId[2]) == 11)) *
                                            ((abs(Lepton_pdgId[3]) == 13)*(Lepton_tightMuon_{muWP}_TotSF_Down[3])/(Lepton_tightMuon_{muWP}_TotSF[3])+
                                             (abs(Lepton_pdgId[3]) == 11))
                                            : 0.0
                                         """

formulas["GenLepMatch2l"] = "(nLepton > 1) ? Lepton_genmatched[0]*Lepton_genmatched[1] : 0.0"

formulas["GenLepMatch3l"] = "(nLepton > 2) ? Lepton_genmatched[0]*Lepton_genmatched[1]*Lepton_genmatched[2] : 0.0"

formulas["GenLepMatch4l"] = "(nLepton > 3) ? Lepton_genmatched[0]*Lepton_genmatched[1]*Lepton_genmatched[2]*Lepton_genmatched[3] : 0.0"
