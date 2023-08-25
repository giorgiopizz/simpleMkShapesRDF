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
            "finalSnapshot_DATA",
        ],
    },
    "JES_16HIPM": {
        "isChain": True,
        "do4MC": True,
        "do4Data": False,
        "subTargets": [
            "JES_modules_16HIPMUL",
            "l2Kin",
            "l3Kin",
            "l4Kin",
            "formulasMC2018v9",
            "finalSnapshot_JES_16",
        ],
        "outputFolder": "MCl1loose2016v9__MCCorr2016v9NoJERInHorn__l2tightOR2016v9__RDF",
    },
    "JES_16noHIPM": {
        "isChain": True,
        "do4MC": True,
        "do4Data": False,
        "subTargets": [
            "JES_modules_16noHIPMUL",
            "l2Kin",
            "l3Kin",
            "l4Kin",
            "formulasMC2018v9",
            "finalSnapshot_JES_16",
        ],
        "outputFolder": "MCl1loose2016v9__MCCorr2016v9NoJERInHorn__l2tightOR2016v9__RDF",
    },
    "JES_17": {
        "isChain": True,
        "do4MC": True,
        "do4Data": False,
        "subTargets": [
            "JES_modules_17UL",
            "l2Kin",
            "l3Kin",
            "l4Kin",
            "formulasMC2017v9",
            "finalSnapshot_JES_17",
        ],
        "outputFolder": "MCl1loose2017v9__MCCorr2017v9NoJERInHorn__l2tightOR2017v9__RDF",
    },
    "JES_18": {
        "isChain": True,
        "do4MC": True,
        "do4Data": False,
        "subTargets": [
            "JES_modules_18UL",
            "l2Kin",
            "l3Kin",
            "l4Kin",
            "formulasMC2018v9",
            "finalSnapshot_JES_18",
        ],
        "outputFolder": "MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9__RDF",
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
            "PromptParticlesGenVars",
            "GenVar",
            "GenLeptonMatch",
            "HiggsGenVars",
            "TopGenVars",
            "WGammaStar",
            "DressedLeptons",
        ]
        # 'wwNLL','ggHTheoryUncertainty', 'qqHTheoryUncertainty', 'EFTGen'],
    },
    "MCCorr2018v9": {
        "isChain": True,
        "do4MC": True,
        "do4Data": False,
        "subTargets": [
            "baseW",
            # "JES_modules_18UL",
            # "JERsMCUL",
            # # "FatJERsMCUL",
            "btagPerJet_DeepCSV_2018UL",
            "btagPerJet_DeepJet_2018UL",
            # "JetPUID_SF_UL",
            # "rochesterMC",
            # "trigMC",
            # "leptonSF",
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
        ],
    },
    "MCFull2018v9": {
        "isChain": True,
        "do4MC": True,
        "do4Data": False,
        "subTargets": [
            "MCl1loose2018v9",
            "MCCorr2018v9",
            "finalSnapshot_MC",
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
    "PromptParticlesGenVars": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.PromptParticlesGenVarsProducer",
        "declare": "PromptParticlesGenVars = lambda : PromptParticlesGenVarsProducer()",
        "module": "PromptParticlesGenVars()",
    },
    "GenVar": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.GenVarProducer",
        "declare": "GenVar = lambda : GenVarProducer()",
        "module": "GenVar()",
    },
    "GenLeptonMatch": {
        "isChain": False,
        "do4MC": True,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.GenLeptonMatchProducer",
        "declare": "GenLeptonMatch = lambda : GenLeptonMatchProducer()",
        "module": "GenLeptonMatch()",
    },
    "HiggsGenVars": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.HiggsGenVarsProducer",
        "declare": "HiggsGenVars = lambda : HiggsGenVarsProducer()",
        "module": "HiggsGenVars()",
    },
    "TopGenVars": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.TopGenVarsProducer",
        "declare": "TopGenVars = lambda : TopGenVarsProducer()",
        "module": "TopGenVars()",
    },
    "WGammaStar": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.WGammaStarProducer",
        "declare": "WGammaStar = lambda : WGammaStarProducer()",
        "module": "WGammaStar()",
    },
    "DressedLeptons": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.DressedLeptonProducer",
        "declare": "DressedLeptons = lambda : DressedLeptonProducer(0.3)",
        "module": "DressedLeptons()",
    },
    "baseW": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.BaseW",
        "declare": "baseW = lambda : BaseW(sampleName, files, xs_db, RPLME_genEventSumw)",
        "module": "baseW()",
    },
    "JES_modules_16HIPMUL": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.JMECalculator",
        "declare": 'jmeCalculator = lambda : JMECalculator("Summer19UL16APV_V7_MC", "Summer20UL16APV_JRV3_MC", \
            jet_object="AK4PFchs", do_Jets=True, do_MET=True, do_Unclustered=False, met_collections = ["PuppiMET", "MET", "RawMET"],\
            do_JER=False, store_nominal=False, store_variations=True)',
        "module": "jmeCalculator()",
    },
    "JES_modules_16noHIPMUL": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.JMECalculator",
        "declare": 'jmeCalculator = lambda : JMECalculator("Summer19UL16_V7_MC", "Summer20UL16_JRV3_MC", \
            jet_object="AK4PFchs", do_Jets=True, do_MET=True, do_Unclustered=False, met_collections = ["PuppiMET", "MET", "RawMET"],\
            do_JER=False, store_nominal=False, store_variations=True)',
        "module": "jmeCalculator()",
    },
    "JES_modules_17UL": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.JMECalculator",
        "declare": 'jmeCalculator = lambda : JMECalculator("Summer19UL17_V5_MC", "Summer19UL17_JRV2_MC", \
            jet_object="AK4PFchs", do_Jets=True, do_MET=True, do_Unclustered=False, met_collections = ["PuppiMET", "MET", "RawMET"],\
            do_JER=False, store_nominal=False, store_variations=True)',
        "module": "jmeCalculator()",
    },
    "JES_modules_18UL": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.JMECalculator",
        "declare": 'jmeCalculator = lambda : JMECalculator("Summer19UL18_V5_MC", "Summer19UL18_JRV2_MC", \
            jet_object="AK4PFchs", do_Jets=True, do_MET=True, do_Unclustered=False, met_collections = ["PuppiMET", "MET", "RawMET"],\
            do_JER=False, store_nominal=False, store_variations=True)',
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
    "l3Kin": {
        "isChain": False,
        "do4MC": True,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.l3KinProducer",
        "declare": "l3Kin = lambda : l3KinProducer()",
        "module": "l3Kin()",
    },
    "l4Kin": {
        "isChain": False,
        "do4MC": True,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.l4KinProducer",
        "declare": "l4Kin = lambda : l4KinProducer()",
        "module": "l4Kin()",
    },
    "formulasMC2017v9": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.GenericFormulaAdder",
        "declare": "formulasMC2017v9 = lambda : GenericFormulaAdder(pathToConfigFile='RPLME_FW/processor/data/formulasToAdd_MC_Full2017v9.py')",
        "module": "formulasMC2017v9()",
    },
    "formulasMC2018v9": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.GenericFormulaAdder",
        "declare": "formulasMC2018v9 = lambda : GenericFormulaAdder(pathToConfigFile='RPLME_FW/processor/data/formulasToAdd_MC_Full2018v9.py')",
        "module": "formulasMC2018v9()",
    },
    "leptonSF": {
        "isChain": False,
        "do4MC": False,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.LeptonSF",
        "declare": "leptonSF = lambda : LeptonSF(('RPLME_FW/processor/data/scale_factor/Full2018v9/electron.json.gz'))",
        "module": "leptonSF()",
    },
    "btagPerJet_DeepCSV_2018UL": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.btagSFProducerLatinos",
        "declare": 'btagPerJet_DeepCSV_2018UL = lambda : btagSFProducerLatinos(2018, "deepCSV", ["shape"], "shape", "RPLME_FW/processor/data/jsonpog-integration/POG/BTV/2018_UL/btagging.json.gz", ["jes","jesAbsolute","jesAbsolute_2018","jesBBEC1","jesBBEC1_2018","jesEC2","jesEC2_2018","jesFlavorQCD","jesHF","jesHF_2018","jesRelativeBal","jesRelativeSample_2018"])',
        "module": "btagPerJet_DeepCSV_2018UL()",
    },
    "btagPerJet_DeepJet_2018UL": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.btagSFProducerLatinos",
        "declare": 'btagPerJet_DeepJet_2018UL = lambda : btagSFProducerLatinos(2018, "deepJet", ["shape"], "shape", "RPLME_FW/processor/data/jsonpog-integration/POG/BTV/2018_UL/btagging.json.gz", ["jes","jesAbsolute","jesAbsolute_2018","jesBBEC1","jesBBEC1_2018","jesEC2","jesEC2_2018","jesFlavorQCD","jesHF","jesHF_2018","jesRelativeBal","jesRelativeSample_2018"])',
        "module": "btagPerJet_DeepJet_2018UL()",
    },
    "finalSnapshot_MC": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.Snapshot",
        "declare": "snapshot = lambda : Snapshot( \
                tmpOutputFilename='output.root', \
                columns=['*'], \
                eosPath='RPLME_EOSPATH', outputFilename='RPLME_OUTPUTFILENAME', \
                includeVariations=False, splitVariations=False, storeNominals=True )",
        "module": "snapshot()",
    },
    "finalSnapshot_JES_16": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.Snapshot",
        "declare": "snapshot = lambda : Snapshot( \
                tmpOutputFilename='output.root', \
                columns=['*'], \
                eosPath='RPLME_EOSPATH', outputFilename='RPLME_OUTPUTFILENAME', \
                includeVariations=True, splitVariations=True, storeNominals=False,\
                outputMap={\
                    'JES':['JESAbsolute', 'JESAbsolute_2016', 'JESBBEC1', 'JESBBEC1_2016', 'JESEC2', 'JESEC2_2016', 'JESHF', 'JESHF_2016', 'JESRelativeBal', 'JESRelativeSample_2016', 'JESFlavorQCD', 'JESTotal']\
                    } )",
        "module": "snapshot()",
    },
    "finalSnapshot_JES_17": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.Snapshot",
        "declare": "snapshot = lambda : Snapshot( \
                tmpOutputFilename='output.root', \
                columns=['*'], \
                eosPath='RPLME_EOSPATH', outputFilename='RPLME_OUTPUTFILENAME', \
                includeVariations=True, splitVariations=True, storeNominals=False,\
                outputMap={\
                    'JES':['JESAbsolute', 'JESAbsolute_2017', 'JESBBEC1', 'JESBBEC1_2017', 'JESEC2', 'JESEC2_2017', 'JESHF', 'JESHF_2017', 'JESRelativeBal', 'JESRelativeSample_2017', 'JESFlavorQCD', 'JESTotal']\
                    } )",
        "module": "snapshot()",
    },
    "finalSnapshot_JES_18": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.Snapshot",
        "declare": "snapshot = lambda : Snapshot( \
                tmpOutputFilename='output.root', \
                columns=['*'], \
                eosPath='RPLME_EOSPATH', outputFilename='RPLME_OUTPUTFILENAME', \
                includeVariations=True, splitVariations=True, storeNominals=False,\
                outputMap={\
                    'JES':['JESAbsolute', 'JESAbsolute_2018', 'JESBBEC1', 'JESBBEC1_2018', 'JESEC2', 'JESEC2_2018', 'JESHF', 'JESHF_2018', 'JESRelativeBal', 'JESRelativeSample_2018', 'JESFlavorQCD', 'JESTotal']\
                    } )",
        "module": "snapshot()",
    },
    "finalSnapshot_Variations": {
        "isChain": False,
        "do4MC": True,
        "do4Data": False,
        "import": "mkShapesRDF.processor.modules.Snapshot",
        "declare": "snapshot = lambda : Snapshot( \
                tmpOutputFilename='output.root', \
                columns=['*'], \
                eosPath='RPLME_EOSPATH', outputFilename='RPLME_OUTPUTFILENAME', \
                includeVariations=True, splitVariations=True, storeNominals=False )",
        "module": "snapshot()",
    },
    "finalSnapshot_DATA": {
        "isChain": False,
        "do4MC": False,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.Snapshot",
        "declare": "snapshot = lambda : Snapshot( \
                tmpOutputFilename='output.root', \
                columns=['*'], \
                eosPath='RPLME_EOSPATH', outputFilename='RPLME_OUTPUTFILENAME', \
                includeVariations=False, splitVariations=False, storeNominals=True )",
        "module": "snapshot()",
    },
    "histogram": {
        "isChain": False,
        "do4MC": True,
        "do4Data": True,
        "import": "mkShapesRDF.processor.modules.Histogram",
        "declare": "histogram = lambda : Histogram( \
                outputFilename='output2.root', \
                variables=[(('mjj', 'mjj', 100, 10, 1000), 'new_fw_mjj', 'baseW * genWeight')] \
                    )",
        "module": "histogram()",
    },
}

