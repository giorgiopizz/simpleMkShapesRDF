Steps = {
    "DATAl1loose2018v9": {
        "isChain": True,
        "do4MC": False,
        "do4Data": True,
        "selection": '"((nElectron+nMuon)>0)"',
        "subTargets": [
            "lumiMask",
            "leptonMaker",
            "lepSel",
            "jetSelUL",
            # "CleanFatJet",
            # "rochesterDATA",
            "l2Kin",
            # "l3Kin",
            # "l4Kin",
            # "trigData",
            # "formulasDATA",
        ],
    },
    "MCl1loose2018v9": {
        "isChain": True,
        "do4MC": True,
        "do4Data": False,
        "selection": '"((nElectron+nMuon)>0)"',
        "subTargets": [
            "leptonMaker",
            "lepSel",
            "jetSelUL",
        ]
        #'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'qqHTheoryUncertainty', 'DressedLeptons','EFTGen'],
    },
    "MCCorr2018v9": {
        "isChain": True,
        "do4MC": True,
        "do4Data": False,
        "subTargets": [
            "baseW",
            "jmeCalculator_18UL",
            # "JERsMCUL",
            # # "FatJERsMCUL",
            # "btagPerJet_DeepCSV_UL",
            # "btagPerJet_DeepJet_UL",
            # "JetPUID_SF_UL",
            # "rochesterMC",
            # "trigMC",
            "leptonSF",
            # "puW",
            "l2Kin",
            # # "l3Kin",
            # # "l4Kin",
            # "formulasMC",
            # # "EmbeddingVeto",
            # # "wwNLOEWK",
            # # "wwNLOEWK2",
            # # "wzNLOEWK",
            # # "zzNLOEWK",
            # # "zNLOEWK",
            # # "wNLOEWK",
            # # "qqHTheoryUncertainty",
            # # "CleanFatJet",
            # # "BoostedWtagSF",
            # "leptonMVAFiller",
            "finalSnapshot",
        ],
    },
    "MCFull2018v9": {
        "isChain": True,
        "do4MC": True,
        "do4Data": False,
        "subTargets": [
            "MCl1loose2018v9",
            "MCCorr2018v9",
        ],
    },
    "MCUL18_debugJES": {
        "isChain": True,
        "do4MC": True,
        "do4Data": False,
        "subTargets": [
            "jmeCalculator_18UL_debugJES",
            "finalSnapshot_debugJES",
        ],
    },
    "leptonMaker": {
        "isChain": False,
        "do4MC": True,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.LeptonMaker",
        "declare": "leptonMaker = lambda : LeptonMaker()",
        "module": "leptonMaker()",
    },
    "lepSel": {
        "isChain": False,
        "do4MC": True,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.LeptonSel",
        "declare": 'leptonSel = lambda : LeptonSel("Loose", 1)',
        "module": "leptonSel()",
    },
    "jetSelUL": {
        "isChain": False,
        "do4MC": True,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.JetSel",
        # jetid=2,pujetid='loose',minpt=15.0,maxeta=4.7, UL2016fix=False "
        "declare": 'jetSel = lambda : JetSel(2,"loose",15.0,4.7,False)',
        "module": "jetSel()",
    },
    "lumiMask": {
        "isChain": False,
        "do4MC": False,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.LumiMask",
        "declare": "lumiMask = lambda : LumiMask(lumiFile)",
        "module": "lumiMask()",
    },
    "baseW": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.BaseW",
        "declare": "baseW = lambda : BaseW(sampleName, files, xs_db)",
        "module": "baseW()",
    },
    "jmeCalculator_18UL_debugJES": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.JMECalculator",
        "declare": 'jmeCalculator = lambda : JMECalculator("Summer19UL18_V5_MC", "Summer19UL18_JRV2_MC", "AK4PFchs", do_JER=False)',
        "module": "jmeCalculator()",
    },
    "jmeCalculator_18UL": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.JMECalculator",
        "declare": 'jmeCalculator = lambda : JMECalculator("Summer19UL18_V5_MC", "Summer19UL18_JRV2_MC", "AK4PFchs")',
        "module": "jmeCalculator()",
    },
    "l2Kin": {
        "isChain": False,
        "do4MC": True,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.l2KinProducer",
        "declare": "l2Kin = lambda : l2KinProducer()",
        "module": "l2Kin()",
    },
    "leptonSF": {
        "isChain": False,
        "do4MC": False,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.LeptonSF",
        "declare": "leptonSF = lambda : LeptonSF(('RPLME_FW/processor/data/scale_factor/Full2018v9/electron.json.gz'))",
        "module": "leptonSF()",
    },
    "finalSnapshot_debugJES": {
        "isChain": False,
        "do4MC": True,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.Snapshot",
        "declare": "snapshot = lambda : Snapshot('output.root', ['CleanJet_*', 'Jet_*'])",
        "module": "snapshot()",
    },
    "finalSnapshot": {
        "isChain": False,
        "do4MC": True,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.Snapshot",
        "declare": "snapshot = lambda : Snapshot('output.root', ['Lepton_*', 'CleanJet_*', 'Jet_*', 'Electron_*', 'Muon_*'])",
        "module": "snapshot()",
    },
}