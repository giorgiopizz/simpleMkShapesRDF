# Cross section DB for Ultra-Legacy samples
# Units in pb
#
# Detailed references at: https://docs.google.com/spreadsheets/d/1IEfle0H1V3ih2JVFpYckmTd-ACTBqgBRIsFydegGgPQ/edit?usp=sharing
#
# References
#
# 	A	https://twiki.cern.ch/twiki/bin/view/CMS/StandardModelCrossSectionsat13TeV
# 	B	https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO
# 	C	https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt1314TeV
# 	D	https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec
# 	E	https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
#       F       https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt13TeV
# 	F2	https://github.com/latinos/LatinoAnalysis/blob/master/Tools/python/HiggsXSection.py
# 	G	https://twiki.cern.ch/twiki/bin/view/CMS/GenXsecTaskForce
# 	H	http://arxiv.org/pdf/1307.7403v1.pdf
# 	I	https://twiki.cern.ch/twiki/bin/viewauth/CMS/HowToGenXSecAnalyzer
# 	J	https://svnweb.cern.ch/cern/wsvn/LHCDMF/trunk/doc/tex/TTBar_Xsecs_Appendix.tex
# 	K	https://twiki.cern.ch/twiki/bin/view/CMS/HiggsWW13TeVProductionMassScan (powheg numbers)
# 	L	https://twiki.cern.ch/twiki/bin/view/CMS/HiggsWW13TeVProduction (powheg numbers)
#       M       https://github.com/shu-xiao/MadGraphScanning/blob/master/diffCrossSection/madGraph.txt
#       N       MCM
#       O       https://twiki.cern.ch/twiki/pub/LHCPhysics/LHCHXSWG/Higgs_XSBR_YR4_update.xlsx
#       P       https://drive.google.com/file/d/0B7mfFpGbPaMvb0ZtMlJfdXhJb2M/view
#       Q       #https://indico.cern.ch/event/448517/session/0/contribution/16/attachments/1164999/1679225/Long_Generators_WZxsec_05_10_15.pdf
# 	R	https://cms-pdmv.cern.ch/mcm/requests?page=0&prepid=B2G-RunIISummer15GS*&dataset_name=TTbarDMJets_*scalar_Mchi-*_Mphi-10000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
#       S       https://docs.google.com/spreadsheets/d/1b4qnWfZrimEGYc1z4dHl21-A9qyJgpqNUbhOlvCzjbE/edit?usp=sharing
#       T       https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR
#       U       https://twiki.cern.ch/twiki/pub/CMS/MonoHCombination/crossSection_ZpBaryonic_gq0p25.txt
# 	V	https://twiki.cern.ch/twiki/bin/viewauth/CMS/SameSignDilepton2016
#       W       https://cms-gen-dev.cern.ch/xsdb/
#       Z       http://cms.cern.ch/iCMS/analysisadmin/cadilines?line=SMP-18-006
#       Y       https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBSMAt13TeV
#       A1      https://indico.cern.ch/event/673253/contributions/2756806/attachments/1541203/2416962/20171016_VJetsXsecsUpdate_PH-GEN.pdf
# 	X	Unknown! - Cross section not yet there

xs_db = {}

### W+jets
xs_db['WJetsToLNu']                   	= ['xsec=61526.7',	'kfact=1.00',		'ref=E']
xs_db['WJetsToLNu-LO']                	= ['xsec=61526.7',	'kfact=1.00',		'ref=E']
xs_db['WJetsToLNu_Sherpa']                	= ['xsec=61526.7',	'kfact=1.00',		'ref=E']

# XSDB: WJets-LO XS = 53870 pb
# WJets-NNLO XS = 61526.7 pb
# k-fact = 1.14
xs_db['WJetsToLNu_HT70To100']                 = ['xsec=1264.0',        'kfact=1.14',           'ref=W']   
xs_db['WJetsToLNu_HT100To200']          	= ['xsec=1256.00',	'kfact=1.14',		'ref=W']
xs_db['WJetsToLNu_HT200To400']          	= ['xsec=335.500',	'kfact=1.14',		'ref=W']
xs_db['WJetsToLNu_HT400To600']           	= ['xsec=45.2500',	'kfact=1.14',		'ref=W']
xs_db['WJetsToLNu_HT600To800']          	= ['xsec=10.9700',	'kfact=1.14',		'ref=W']
xs_db['WJetsToLNu_HT800To1200']         	= ['xsec=4.93300',	'kfact=1.14',		'ref=W']
xs_db['WJetsToLNu_HT1200To2500']        	= ['xsec=1.16000',	'kfact=1.14',		'ref=W']
xs_db['WJetsToLNu_HT2500ToInf']         	= ['xsec=0.02678',	'kfact=1.00',		'ref=I']

xs_db['WJetsToLNu_Pt-100To250']               = ['xsec=763.7',	        'kfact=1.0',		'ref=W']  
xs_db['WJetsToLNu_Pt-250To400']               = ['xsec=27.55', 	'kfact=1.0',		'ref=W']
xs_db['WJetsToLNu_Pt-400To600']               = ['xsec=3.477', 	'kfact=1.0',		'ref=W']
xs_db['WJetsToLNu_Pt-600ToInf']               = ['xsec=0.5415',	'kfact=1.0',		'ref=W']

# Sum of XS: 53330 + 8875 + 3338 = 65543
# NNLO XS = 61526.7
# k factor = 61526.7 / 65543
xs_db['WJetsToLNu_0J']                        = [ 'xsec=53330',        'kfact=0.94',           'ref=W' ]
xs_db['WJetsToLNu_1J']                        = [ 'xsec=8875',         'kfact=0.94',           'ref=W' ]
xs_db['WJetsToLNu_2J']                        = [ 'xsec=3338',         'kfact=0.94',           'ref=W' ]


### DY
xs_db['DYJetsToLL_M-10to50']          	= ['xsec=18610.0',	'kfact=1.000',		'ref=E']
xs_db['DYJetsToLL_M-10to50-LO']               = ['xsec=18610.0',       'kfact=1.000',          'ref=E']
xs_db['DYJetsToLL_M-10to50_NLO']              = ['xsec=20490.0',      'kfact=1.000',          'ref=W']

xs_db['DYJetsToLL_M-50']                      = ['xsec=6077.22',       'kfact=1.000',          'ref=E']
xs_db['DYJetsToLL_M-50-LO']      	        = ['xsec=6077.22',	'kfact=1.000',		'ref=E']
xs_db['DYJetsToLL_M-50-LO_ext1']     	        = ['xsec=6077.22',	'kfact=1.000',		'ref=E']

xs_db['DYJetsToTT_MuEle_M-50']                = ['xsec=250.997',       'kfact=1.000',          'ref=E']  # (6077.22/3)*(0.352)^2

# DYJetsToLL_M-50 = 6077.22 --> 5129 + 951.5 + 361.4 = 6441.9 --> k-factor = 0.94
xs_db['DYJetsToLL_0J']                        = [ 'xsec=5129',         'kfact=0.94',           'ref=W' ]
xs_db['DYJetsToLL_1J']                        = [ 'xsec=951.5',        'kfact=0.94',           'ref=W' ]
xs_db['DYJetsToLL_2J']                        = [ 'xsec=361.4',        'kfact=0.94',           'ref=W' ]

xs_db['DYJetsToLL_M-50_HT-70to100']           = ['xsec=146.5',   	'kfact=1.23',	        'ref=W'] 
xs_db['DYJetsToLL_M-50_HT-100to200']          = ['xsec=160.7',	        'kfact=1.23',	        'ref=W'] 
xs_db['DYJetsToLL_M-50_HT-200to400']          = ['xsec=48.63',	        'kfact=1.23',	        'ref=W'] 
xs_db['DYJetsToLL_M-50_HT-400to600']          = ['xsec=6.993',	        'kfact=1.23',	        'ref=W'] 
xs_db['DYJetsToLL_M-50_HT-600to800']          = ['xsec=1.761',	        'kfact=1.23',	        'ref=W'] 
xs_db['DYJetsToLL_M-50_HT-800to1200']         = ['xsec=0.8021',	'kfact=1.23',	        'ref=W'] 
xs_db['DYJetsToLL_M-50_HT-1200to2500']        = ['xsec=0.1937',	'kfact=1.23',	        'ref=W'] 
xs_db['DYJetsToLL_M-50_HT-2500toInf']         = ['xsec=0.003514',	'kfact=1.23',	        'ref=W'] 

xs_db['DYJetsToLL_M-4to50_HT-100to200']       = ['xsec=204.',          'kfact=1.000',          'ref=W']
xs_db['DYJetsToLL_M-4to50_HT-200to400']       = ['xsec=54.39',         'kfact=1.000',          'ref=W']
xs_db['DYJetsToLL_M-4to50_HT-400to600']       = ['xsec=5.697',         'kfact=1.000',          'ref=W']
xs_db['DYJetsToLL_M-4to50_HT-600toInf']       = ['xsec=1.85',          'kfact=1.000',          'ref=W']

xs_db['EWKZ2Jets_ZToLL_M-50']                 = ['xsec=6.215',         'kfact=1.000',          'ref=W']

### Wgamma
xs_db['WGToLNuG']                             = ['xsec=412.7',         'kfact=1.000',          'ref=W']
xs_db['Wg_AMCNLOFXFX_01J_PDF']                = ['xsec=191.8',         'kfact=1.000',          'ref=I']
xs_db['Wg_AMCNLOFXFX_01J']                    = ['xsec=191.8',         'kfact=1.000',          'ref=I']
 
### WW
xs_db['WWTo2L2Nu']	                 	= ['xsec=12.178',	'kfact=1.000',		'ref=E']
xs_db['WWTo2L2Nu_TuneCP5Up']                	= ['xsec=12.178',	'kfact=1.000',		'ref=E']		
xs_db['WWTo2L2Nu_TuneCP5Down']               	= ['xsec=12.178',	'kfact=1.000',		'ref=E']		

# 1.4*0.0368 --> 1.4 is a k-factor, 0.0368 comes from XSDB, divided by 1000
xs_db['GluGluToWWToENEN']      	        = ['xsec=0.05152',	'kfact=1.000',		'ref=W']
xs_db['GluGluToWWToENMN']              	= ['xsec=0.05152',	'kfact=1.000',		'ref=W']
xs_db['GluGluToWWToENTN']              	= ['xsec=0.05152',	'kfact=1.000',		'ref=W']
xs_db['GluGluToWWToMNEN']              	= ['xsec=0.05152',	'kfact=1.000',		'ref=W']
xs_db['GluGluToWWToMNMN']              	= ['xsec=0.05152',	'kfact=1.000',		'ref=W']
xs_db['GluGluToWWToMNTN']              	= ['xsec=0.05152',	'kfact=1.000',		'ref=W']
xs_db['GluGluToWWToTNEN']              	= ['xsec=0.05152',	'kfact=1.000',		'ref=W']
xs_db['GluGluToWWToTNMN']              	= ['xsec=0.05152',	'kfact=1.000',		'ref=W']
xs_db['GluGluToWWToTNTN']              	= ['xsec=0.05152',	'kfact=1.000',		'ref=W']


### WZ
xs_db['WZ']			                = ['xsec=47.130',	'kfact=1.000',		'ref=E']

xs_db['WZTo3LNu']		                = ['xsec=4.666',  	'kfact=1.000',		'ref=X'] # X = https://cms.cern.ch/iCMS/jsp/openfile.jsp?tp=draft&files=AN2019_156_v8.pdf
xs_db['WZTo3LNu_mllmin4p0']	                = ['xsec=4.666',   	'kfact=1.000',		'ref=X'] # X = https://cms.cern.ch/iCMS/jsp/openfile.jsp?tp=draft&files=AN2019_156_v8.pdf BUT KEEPING INCLUSIVE VALUE!!! NEED TO CHECK!
xs_db['WZTo3LNu_mllmin0p1']	                = ['xsec=4.666',   	'kfact=1.000',		'ref=X'] # X = https://cms.cern.ch/iCMS/jsp/openfile.jsp?tp=draft&files=AN2019_156_v8.pdf BUT KEEPING INCLUSIVE VALUE!!! NEED TO CHECK!
xs_db['WZTo2Q2L_mllmin4p0']	                = ['xsec=5.5950',	'kfact=1.000',		'ref=E'] # KEEPING INCLUSIVE VALUE!!! NEED TO CHECK!
xs_db['WZTo1L3Nu']                            = ['xsec=3.033',         'kfact=1.000',          'ref=E']

xs_db['WZJJ_Inclusive']                       = ['xsec=0.01627',       'kfact=1.000',          'ref=W']
xs_db['WZJJ_LL']                              = ['xsec=0.001375',      'kfact=1.000',          'ref=W']
xs_db['WZJJ_TL']                              = ['xsec=0.003186',      'kfact=1.000',          'ref=W']
xs_db['WZJJ_LT']                              = ['xsec=0.002824',      'kfact=1.000',          'ref=W']
xs_db['WZJJ_TT']                              = ['xsec=0.008854',      'kfact=1.000',          'ref=W']

xs_db['WZG']                                  = ['xsec=0.04345',       'kfact=1.000',          'ref=E']

### ZZ
xs_db['ZZ']                                   = ['xsec=16.52300', 	'kfact=1.000',		'ref=E']
xs_db['ZZTo2Q2L']                             = ['xsec=2.33',  	'kfact=1.000',		'ref=E'] # 16.523 * (3*0.033658)*(0.69911)*2
xs_db['ZZTo2Q2L_mllmin4p0']                   = ['xsec=2.33',  	'kfact=1.000',		'ref=E'] # KEEPING INCLUSIVE VALUE!!! NEED TO CHECK!
xs_db['ZZTo2Nu2Q']                            = ['xsec=4.62',  	'kfact=1.000',		'ref=E'] # 16.52300 * (0.20)*(0.69911)*2
xs_db['ZZTo4L']                               = ['xsec=1.325', 	'kfact=1.000',		'ref=E']
xs_db['ZZTo4L_M-1toInf']                      = ['xsec=1.374', 	'kfact=1.000',		'ref=E'] # KEEPING INCLUSIVE VALUE!!! NEED TO CHECK!
xs_db['ZZTo2L2Nu']                            = ['xsec=0.667', 	'kfact=1.000',		'ref=E'] # 16.52300 *(3*0.033658)*(0.20)*2
xs_db['ZZTo2Q2Nu']                            = ['xsec=4.62',  	'kfact=1.000',		'ref=E'] # 16.52300 *(3*0.69911)*(0.20)*2
xs_db['ZZTo4Q']                               = ['xsec=8.076', 	'kfact=1.000',		'ref=E'] # 16.52300*(0.69911)**2

xs_db['ZZGTo4L']                              = ['xsec=0.02202',	'kfact=1.000',		'ref=W']

### ZG
xs_db['ZGToLLG']                              = ['xsec=51.1',          'kfact=1.000',          'ref=W']


### Top
xs_db['TTJets-LO']                            = ['xsec=831.76',	'kfact=1.000',		'ref=E']

xs_db['TT_DiLept'] 	             	        = ['xsec=87.310',	'kfact=1.000',		'ref=E']

xs_db['TTTo2L2Nu'] 	             	        = ['xsec=87.310',	'kfact=1.000',		'ref=E']
xs_db['TTTo2L2Nu_TuneCP5Up']         	        = ['xsec=87.310',	'kfact=1.000',		'ref=E']
xs_db['TTTo2L2Nu_TuneCP5Down']       	        = ['xsec=87.310',	'kfact=1.000',		'ref=E']
xs_db['TTTo2L2Nu_hdampUp']         	        = ['xsec=87.310',	'kfact=1.000',		'ref=E']
xs_db['TTTo2L2Nu_hdampDown']         	        = ['xsec=87.310',	'kfact=1.000',		'ref=E']

xs_db['TTJets_DiLept']                        = ['xsec=87.310',        'kfact=1.000',          'ref=E']

xs_db['TTToSemiLeptonic']                     = ['xsec=364.35',	'kfact=1.000',	        'ref=E']  # 831.76 * 0.6760 * 0.1080 * 3 * 2
xs_db['TTToSemiLeptonic_TuneCP5Up']           = ['xsec=364.35',	'kfact=1.000',	        'ref=E']
xs_db['TTToSemiLeptonic_TuneCP5Down']         = ['xsec=364.35',	'kfact=1.000',	        'ref=E']
xs_db['TTToSemiLeptonic_hdampUp']             = ['xsec=364.35',	'kfact=1.000',	        'ref=E']
xs_db['TTToSemiLeptonic_hdampDown']           = ['xsec=364.35',	'kfact=1.000',	        'ref=E']

xs_db['ST_t-channel_top']                     = ['xsec=44.07048',	'kfact=1.000',		'ref=D']
xs_db['ST_t-channel_top_TuneCP5Up']           = ['xsec=44.07048',	'kfact=1.000',		'ref=D']
xs_db['ST_t-channel_top_TuneCP5Down']         = ['xsec=44.07048',	'kfact=1.000',		'ref=D']
xs_db['ST_t-channel_top_hdampUp']             = ['xsec=44.07048',	'kfact=1.000',		'ref=D']
xs_db['ST_t-channel_top_hdampDown']           = ['xsec=44.07048',	'kfact=1.000',		'ref=D']
xs_db['ST_t-channel_top_5f']                  = ['xsec=136.02',        'kfact=1.000',          'ref=Z']

xs_db['ST_t-channel_antitop']                 = ['xsec=26.2278',       'kfact=1.000',		'ref=D']
xs_db['ST_t-channel_antitop_TuneCP5Up']       = ['xsec=26.2278',       'kfact=1.000',		'ref=D']
xs_db['ST_t-channel_antitop_TuneCP5Down']     = ['xsec=26.2278',       'kfact=1.000',		'ref=D']
xs_db['ST_t-channel_antitop_hdampUp']         = ['xsec=26.2278',       'kfact=1.000',		'ref=D']
xs_db['ST_t-channel_antitop_hdampDown']       = ['xsec=26.2278',       'kfact=1.000',		'ref=D']
xs_db['ST_t-channel_antitop_5f']              = ['xsec=80.95',         'kfact=1.000',		'ref=D']

# What does noHad mean?
# We want both of the Ws not to decay hadronically? --> 35.85 * (1 - 0.6741)^2
xs_db['ST_tW_antitop']                        = ['xsec=35.85',		'kfact=1.000',		'ref=D']
xs_db['ST_tW_antitop_noHad']                  = ['xsec=3.808',         'kfact=1.000',          'ref=D'] # 35.85 * (1 - 0.6741)^2 - previously XS = 1
xs_db['ST_tW_antitop_noHad_TuneCP5Up']        = ['xsec=3.808',         'kfact=1.000',          'ref=D'] # 35.85 * (1 - 0.6741)^2 - previously XS = 1
xs_db['ST_tW_antitop_noHad_TuneCP5Down']      = ['xsec=3.808',         'kfact=1.000',          'ref=D'] # 35.85 * (1 - 0.6741)^2 - previously XS = 1
xs_db['ST_tW_antitop_noHad_hdampUp']          = ['xsec=3.808',         'kfact=1.000',          'ref=D'] # 35.85 * (1 - 0.6741)^2 - previously XS = 1
xs_db['ST_tW_antitop_noHad_hdampDown']        = ['xsec=3.808',         'kfact=1.000',          'ref=D'] # 35.85 * (1 - 0.6741)^2 - previously XS = 1
xs_db['ST_tW_antitop_noHad_PDF']              = ['xsec=3.808',         'kfact=1.000',          'ref=D'] # 35.85 * (1 - 0.6741)^2 - previously XS = 1

xs_db['ST_tW_top']                            = ['xsec=35.85',		'kfact=1.000',		'ref=D']
xs_db['ST_tW_top_noHad']                      = ['xsec=3.808',         'kfact=1.000',          'ref=D'] # 35.85 * (1 - 0.6741)^2 - previously XS = 1
xs_db['ST_tW_top_noHad_TuneCP5Up']            = ['xsec=3.808',         'kfact=1.000',          'ref=D'] # 35.85 * (1 - 0.6741)^2 - previously XS = 1
xs_db['ST_tW_top_noHad_TuneCP5Down']          = ['xsec=3.808',         'kfact=1.000',          'ref=D'] # 35.85 * (1 - 0.6741)^2 - previously XS = 1
xs_db['ST_tW_top_noHad_hdampUp']              = ['xsec=3.808',         'kfact=1.000',          'ref=D'] # 35.85 * (1 - 0.6741)^2 - previously XS = 1
xs_db['ST_tW_top_noHad_hdampDown']            = ['xsec=3.808',         'kfact=1.000',          'ref=D'] # 35.85 * (1 - 0.6741)^2 - previously XS = 1
xs_db['ST_tW_top_noHad_PDF']                  = ['xsec=3.808',         'kfact=1.000',          'ref=D'] # 35.85 * (1 - 0.6741)^2 - previously XS = 1

# All ST_s-channel xs_db are "leptonDecays" --> t->Wb->lvb
xs_db['ST_s-channel']                         = ['xsec=3.34368',	'kfact=1.000',		'ref=D'] # 10.32 * (3*0.108) --> the W boson decays leptonically
xs_db['ST_s-channel_TuneCP5Up']               = ['xsec=3.34368',	'kfact=1.000',		'ref=D'] # 10.32 * (3*0.108) --> the W boson decays leptonically
xs_db['ST_s-channel_TuneCP5Down']             = ['xsec=3.34368',	'kfact=1.000',		'ref=D'] # 10.32 * (3*0.108) --> the W boson decays leptonically
xs_db['ST_s-channel_TuneCP5CR1']              = ['xsec=3.34368',	'kfact=1.000',		'ref=D'] # 10.32 * (3*0.108) --> the W boson decays leptonically
xs_db['ST_s-channel_TuneCP5CR2']              = ['xsec=3.34368',	'kfact=1.000',		'ref=D'] # 10.32 * (3*0.108) --> the W boson decays leptonically
xs_db['ST_s-channel_erdON']                   = ['xsec=3.34368',	'kfact=1.000',		'ref=D'] # 10.32 * (3*0.108) --> the W boson decays leptonically
xs_db['ST_s-channel_JMENano']                 = ['xsec=3.34368',	'kfact=1.000',		'ref=D'] # 10.32 * (3*0.108) --> the W boson decays leptonically
# Exception: here, the W decays hadronically ("hadronicDecays") --> t->Wb->qq'b
xs_db['ST_s-channel_had']                     = ['xsec=7.05062',	'kfact=1.000',		'ref=D'] # 10.32 * (0.6832)  --> the W boson decays hadronically

xs_db['TTWJetsToQQ']                          = ['xsec=0.4377',        'kfact=1.000',          'ref=W']      
xs_db['TTZToQQ']                              = ['xsec=0.5297',        'kfact=1.000',          'ref=E']
xs_db['TTZToQQ_Dilept']                       = ['xsec=0.0568',        'kfact=1.000',          'ref=W']

xs_db['TTWJetsToLNu']                         = ['xsec=0.2161',	'kfact=1.000',		'ref=E']	
xs_db['TTWJetsToLNu_TuneCP5Up']               = ['xsec=0.2161',	'kfact=1.000',		'ref=E']	
xs_db['TTWJetsToLNu_TuneCP5Down']             = ['xsec=0.2161',	'kfact=1.000',		'ref=E']	

xs_db['TTZToLLNuNu_M-10']                     = ['xsec=0.2439',	'kfact=1.000',		'ref=W']
xs_db['TTZToLLNuNu_M-10_TuneCP5Up']           = ['xsec=0.2439',	'kfact=1.000',		'ref=W']
xs_db['TTZToLLNuNu_M-10_TuneCP5Down']         = ['xsec=0.2439',	'kfact=1.000',		'ref=W']

xs_db['tZq_ll']   				= ['xsec=0.07580',	'kfact=1.000',	        'ref=E']
xs_db['tZq_ll_TuneCP5Up']   			= ['xsec=0.07580',	'kfact=1.000',	        'ref=E']
xs_db['tZq_ll_TuneCP5Down'] 			= ['xsec=0.07580',	'kfact=1.000',	        'ref=E']

xs_db['tZq_ll_4f']                            = ['xsec=0.0761',        'kfact=1.000',          'ref=W']
xs_db['tZq_ll_4f_TuneCP5Up']                  = ['xsec=0.0761',        'kfact=1.000',          'ref=W']
xs_db['tZq_ll_4f_TuneCP5Down']                = ['xsec=0.0761',        'kfact=1.000',          'ref=W']


## VVV
xs_db['WWW']			        	= ['xsec=0.2158',	'kfact=1.000',		'ref=W']
xs_db['WWW_ext1']			        = ['xsec=0.2158',	'kfact=1.000',		'ref=W']
                                               
xs_db['WWZ']				        = ['xsec=0.1707',	'kfact=1.000',		'ref=W']
xs_db['WWZ_ext1']     			= ['xsec=0.1707',	'kfact=1.000',		'ref=W']
                                               
xs_db['WZZ']	 			        = ['xsec=0.05709',	'kfact=1.000',		'ref=W']
xs_db['WZZ_ext1']			        = ['xsec=0.05709',	'kfact=1.000',		'ref=W']
                                               
xs_db['ZZZ']				        = ['xsec=0.01476',	'kfact=1.000',		'ref=W']
xs_db['ZZZ_ext1']			        = ['xsec=0.01476',	'kfact=1.000',		'ref=W']
                                               
xs_db['WWG']                                  = ['xsec=0.2147',        'kfact=1.000',          'ref=E']

xs_db['WWW_DiLeptonFilter']			= ['xsec=0.007205',	'kfact=1.000',		'ref=W']

xs_db['WWZTo4L2Nu']				= ['xsec=0.001809',	'kfact=1.000',		'ref=W'] # 0.1707*(3*0.108)*(3*0.108)*(3*0.033658)


### QCD
xs_db['QCD_Pt_15to20_bcToE']    		= ['xsec=186200',	'kfact=1.000',  	'ref=I']
xs_db['QCD_Pt_20to30_bcToE']    		= ['xsec=303800',	'kfact=1.000',  	'ref=I']
xs_db['QCD_Pt_30to80_bcToE']    		= ['xsec=362300',	'kfact=1.000',  	'ref=I']
xs_db['QCD_Pt_80to170_bcToE']    		= ['xsec=33700',		'kfact=1.000',  	'ref=I']
xs_db['QCD_Pt_170to250_bcToE']    		= ['xsec=2125',		'kfact=1.000',  	'ref=I']
xs_db['QCD_Pt_250toInf_bcToE']    		= ['xsec=562.5',		'kfact=1.000',  	'ref=I']

xs_db['QCD_HT200to300']                       = ['xsec=1555000',       'kfact=1.000',          'ref=W']
xs_db['QCD_HT300to500']                       = ['xsec=324500' ,       'kfact=1.000',          'ref=W']
xs_db['QCD_HT500to700']                       = ['xsec=30310'  ,       'kfact=1.000',          'ref=W']
xs_db['QCD_HT700to1000']                      = ['xsec=6444'   ,       'kfact=1.000',          'ref=W']
xs_db['QCD_HT1000to1500']                     = ['xsec=1127'   ,       'kfact=1.000',          'ref=W']
xs_db['QCD_HT1500to2000']                     = ['xsec=109.8'  ,       'kfact=1.000',          'ref=W']
xs_db['QCD_HT2000toInf']                      = ['xsec=21.98'  ,       'kfact=1.000',          'ref=W']

xs_db['QCD_Pt_15to30']                        = ['xsec=1244000000',    'kfact=1.000',          'ref=W']
xs_db['QCD_Pt_30to50']                        = ['xsec=106500000',     'kfact=1.000',          'ref=W']


### Signals - XS are dummy and taken from YR4 N3LO

# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR
# BR (H-->WW) = 0.2152
# BR (H-->tt) = 0.06256
# BR (H-->ZZ) = 0.02641

# ggH - XS = 48.52 pb
# 58.52*0.2152*(3*0.108)*(3*0.108)
xs_db['GluGluHToWWTo2L2Nu_M125']    		= ['xsec=1.32200',	'kfact=1.000',	'ref=F']
xs_db['GluGluHToWWTo2L2Nu_M125_TuneCP5Up']    = ['xsec=1.32200',       'kfact=1.000',  'ref=F']
xs_db['GluGluHToWWTo2L2Nu_M125_TuneCP5Down']  = ['xsec=1.32200',       'kfact=1.000',  'ref=F']
xs_db['GluGluHToWWTo2L2Nu_M125_Powheg']       = ['xsec=1.32200',       'kfact=1.000',  'ref=F']
xs_db['GluGluHToWWTo2L2Nu_M125_noPDF']        = ['xsec=1.32200',       'kfact=1.000',  'ref=F']
xs_db['GluGluHToWWTo2L2Nu_M125_Pohweg_noPDF'] = ['xsec=1.32200',       'kfact=1.000',  'ref=F']

xs_db['GGHjjToWWTo2L2Nu_minloHJJ_M125']       = ['xsec=1',             'kfact=1.000',  'ref=X'] 

# 48.52*0.06256
xs_db['GluGluHToTauTau_M125']    		= ['xsec=3.0354',	'kfact=1.000',	'ref=F']
xs_db['GluGluHToTauTau_M125_Powheg'] 		= ['xsec=3.0354',	'kfact=1.000',	'ref=F']
xs_db['GluGluHToTauTau_M125_FXFX'] 		= ['xsec=3.0354',	'kfact=1.000',	'ref=F']

# 48.52*0.02641*(3*0.033658)*(3*0.033658)
xs_db['GluGluHToZZTo4L_M125']    		= ['xsec=0.01306',	'kfact=1.000',	'ref=F']
xs_db['GluGluHToZZTo4L_M125_TuneCP5Up']       = ['xsec=0.01306',       'kfact=1.000',  'ref=F']
xs_db['GluGluHToZZTo4L_M125_TuneCP5Down']     = ['xsec=0.01306',       'kfact=1.000',  'ref=F']

# VBF - XS = 3.779 pb
# 3.779*0.2152*(3*0.108)*(3*0.108) 
xs_db['VBFHToWWTo2L2Nu_M125']    		= ['xsec=0.08537',	'kfact=1.000',	'ref=F']
xs_db['VBFHToWWTo2L2Nu_M125_TuneCP5Up']       = ['xsec=0.08537',       'kfact=1.000',  'ref=F'] 
xs_db['VBFHToWWTo2L2Nu_M125_TuneCP5Down']     = ['xsec=0.08537',       'kfact=1.000',  'ref=F']
xs_db['VBFHToWWTo2L2Nu_M125_noPDF']           = ['xsec=0.08537',       'kfact=1.000',  'ref=F']   

# 3.779*0.06256
xs_db['VBFHToTauTau_M125']    		= ['xsec=0.236',  	'kfact=1.000',	'ref=F']

# WH - XS(W+H) = 0.8380 pb and XS(W-H) = 0.5313 pb
# 0.5313*0.2152
xs_db['HWminusJ_HToWW_M125']    		= ['xsec=0.114',  	'kfact=1.000',	'ref=F']
# 0.05967*0.2152*(3*0.108)*(3*0.108) 
xs_db['HWminusJ_HToWWTo2L2Nu_WToLNu_M125']    = ['xsec=0.001348',      'kfact=1.000',  'ref=F'] 

# 0.8380*0.2152
xs_db['HWplusJ_HToWW_M125']                   = ['xsec=0.1803',        'kfact=1.000',  'ref=F']
# 0.09404*0.2152*(3*0.108)*(3*0.108) 
xs_db['HWplusJ_HToWWTo2L2Nu_WToLNu_M125']     = ['xsec=0.002124',      'kfact=1.000',  'ref=F']  

# ZH -  XS = 0.8824 pb 
# XS(ggZH) = 0.1227 pb
# XS(HZJ)  = 0.8824 - 0.1227 = 0.7597 pb
# 0.7597*0.2152
xs_db['HZJ_HToWW_M125']    	        	= ['xsec=0.1635',	'kfact=1.000',	'ref=F']
# 0.7597*0.2152*(3*0.033658)*(3*0.108)*(3*0.108)
xs_db['HZJ_HToWWTo2L2Nu_ZTo2L_M125']    	= ['xsec=0.0017329',	'kfact=1.000',	'ref=F']

# 0.1227*0.2152
xs_db['ggZH_HToWW_M125']        		= ['xsec=0.0264',	'kfact=1.000',	'ref=F']
# 0.1227*0.2152*(3*0.033658)*(3*0.108)*(3*0.108)
xs_db['ggZH_HToWWTo2L2Nu_ZTo2L_M125']         = ['xsec=0.000279889',   'kfact=1.000',  'ref=F']

xs_db['GluGluHToZZTo4L_MiNLOHJJ_M125']            = ['xsec=1',         'kfact=1.000',  'ref=X']
xs_db['GluGluHToZZTo4L_MiNLOHJJ_M125_TuneCP5Up']  = ['xsec=1',         'kfact=1.000',  'ref=X']
xs_db['GluGluHToZZTo4L_MiNLOHJJ_M125_TuneCP5Down']= ['xsec=1',         'kfact=1.000',  'ref=X']

# ttH - XS = 0.5065
# 0.5065*(1-0.5809)
xs_db['ttHToNonbb_M125']       		= ['xsec=0.2123',	'kfact=1.000',	'ref=F']


# Additional Higgs signals with non-SM parameters 
# All XS set to 1. I haven't even looked at them
xs_db['H0PM_ToWWTo2L2Nu']                     = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['H0PH_ToWWTo2L2Nu']                     = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['H0PHf05_ToWWTo2L2Nu']                  = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['H0M_ToWWTo2L2Nu']                      = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['H0Mf05_ToWWTo2L2Nu']                   = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['H0L1_ToWWTo2L2Nu']                     = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['H0L1f05_ToWWTo2L2Nu']                  = ['xsec=1',             'kfact=1.000',  'ref=X']

xs_db['VBF_H0PM_ToWWTo2L2Nu']                 = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['VBF_H0PH_ToWWTo2L2Nu']                 = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['VBF_H0PHf05_ToWWTo2L2Nu']              = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['VBF_H0M_ToWWTo2L2Nu']                  = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['VBF_H0Mf05_ToWWTo2L2Nu']               = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['VBF_H0L1_ToWWTo2L2Nu']                 = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['VBF_H0L1Zgf05_ToWWTo2L2Nu']            = ['xsec=1',             'kfact=1.000',  'ref=X']

xs_db['WH_H0PM_ToWWTo2L2Nu']                  = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['WH_H0PH_ToWWTo2L2Nu']                  = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['WH_H0PHf05_ToWWTo2L2Nu']               = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['WH_H0M_ToWWTo2L2Nu']                   = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['WH_H0Mf05_ToWWTo2L2Nu']                = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['WH_H0L1_ToWWTo2L2Nu']                  = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['WH_H0L1f05_ToWWTo2L2Nu']               = ['xsec=1',             'kfact=1.000',  'ref=X']

xs_db['ZH_H0PM_ToWWTo2L2Nu']                  = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['ZH_H0PH_ToWWTo2L2Nu']                  = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['ZH_H0PHf05_ToWWTo2L2Nu']               = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['ZH_H0M_ToWWTo2L2Nu']                   = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['ZH_H0Mf05_ToWWTo2L2Nu']                = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['ZH_H0L1_ToWWTo2L2Nu']                  = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['ZH_H0L1f05_ToWWTo2L2Nu']               = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['ZH_H0LZgf05_ToWWTo2L2Nu']              = ['xsec=1',             'kfact=1.000',  'ref=X']

xs_db['GGHjj_H0PM_ToWWTo2L2Nu']               = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['GGHjj_H0M_ToWWTo2L2Nu']                = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['GGHjj_H0Mf05_ToWWTo2L2Nu']             = ['xsec=1',             'kfact=1.000',  'ref=X']

xs_db['ttH_H0PM_ToWWTo2L2Nu']                 = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['ttH_H0M_ToWWTo2L2Nu']                  = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['ttH_H0Mf05_ToWWTo2L2Nu']               = ['xsec=1',             'kfact=1.000',  'ref=X']        

xs_db['SSWW']                                 = ['xsec=1',             'kfact=1.000',  'ref=W']

xs_db['VBS_SSWW_cW_INT']                      = ['xsec=1',             'kfact=1.000',  'ref=W']
xs_db['VBS_SSWW_cW_BSM']                      = ['xsec=1',             'kfact=1.000',  'ref=W']
xs_db['VBS_SSWW_cHW_INT']                     = ['xsec=1',             'kfact=1.000',  'ref=W']
xs_db['VBS_SSWW_cHW_BSM']                     = ['xsec=1',             'kfact=1.000',  'ref=W']
xs_db['VBS_SSWW_cW_cHW']                      = ['xsec=1',             'kfact=1.000',  'ref=W']

xs_db['WpWmJJ_EWK_noTop_pol_LL']              = ['xsec=0.01132',             'kfact=1.000',  'ref=I']
xs_db['WpWmJJ_EWK_noTop_pol_LT']              = ['xsec=0.01446',             'kfact=1.000',  'ref=I']
xs_db['WpWmJJ_EWK_noTop_pol_TL']              = ['xsec=0.01512',             'kfact=1.000',  'ref=I']
xs_db['WpWmJJ_EWK_noTop_pol_TT']              = ['xsec=0.05026',             'kfact=1.000',  'ref=I']

xs_db['WpWmJJ_EWK_noTop_CMWW_pol_LL']         = ['xsec=0.01394',             'kfact=1.000',  'ref=I']
xs_db['WpWmJJ_EWK_noTop_CMWW_pol_LT']         = ['xsec=0.01318',             'kfact=1.000',  'ref=I']
xs_db['WpWmJJ_EWK_noTop_CMWW_pol_TL']         = ['xsec=0.01390',             'kfact=1.000',  'ref=I']
xs_db['WpWmJJ_EWK_noTop_CMWW_pol_TT']         = ['xsec=0.05004',             'kfact=1.000',  'ref=I']

xs_db['WpWmJJ_EWK_noTop']                     = ['xsec=0.09283',             'kfact=1.000',  'ref=I']
xs_db['WpWmJJ_QCD_noTop']                     = ['xsec=2.190',               'kfact=1.000',  'ref=I']
xs_db['WpWmJJ_EWK_QCD_noTop']                 = ['xsec=2.295',               'kfact=1.000',  'ref=I']

xs_db['AToZHToLLTTbar_MA-1000_MH-330'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1000_MH-350'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1000_MH-400'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1000_MH-450'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1000_MH-500'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1000_MH-550'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1000_MH-600'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1000_MH-650'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1000_MH-700'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1000_MH-750'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1000_MH-800'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1000_MH-850'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1000_MH-900'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1050_MH-330'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1050_MH-350'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1050_MH-400'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1050_MH-450'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1050_MH-500'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1050_MH-550'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1050_MH-600'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1050_MH-700'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1050_MH-750'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1050_MH-800'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1050_MH-850'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1050_MH-900'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1050_MH-950'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1100_MH-1000'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1100_MH-330'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1100_MH-350'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1100_MH-400'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1100_MH-450'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1100_MH-500'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1100_MH-550'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1100_MH-600'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1100_MH-650'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1100_MH-700'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1100_MH-750'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1100_MH-800'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1100_MH-850'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1100_MH-900'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1100_MH-950'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1150_MH-1050'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1150_MH-330'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1150_MH-350'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1150_MH-450'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1150_MH-550'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1150_MH-650'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1150_MH-750'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1150_MH-850'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1150_MH-950'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1200_MH-1000'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1200_MH-1100'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1200_MH-330'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1200_MH-350'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1200_MH-400'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1200_MH-500'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1200_MH-600'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1200_MH-700'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1200_MH-800'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1200_MH-850'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1200_MH-900'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1300_MH-1000'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1300_MH-1100'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1300_MH-1200'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1300_MH-350'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1300_MH-400'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1300_MH-500'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1300_MH-600'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1300_MH-700'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1300_MH-800'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1300_MH-900'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1400_MH-1000'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1400_MH-1100'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1400_MH-1200'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1400_MH-1300'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1400_MH-350'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1400_MH-400'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1400_MH-500'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1400_MH-600'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1400_MH-700'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1400_MH-800'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1400_MH-900'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1500_MH-1000'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1500_MH-1100'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1500_MH-1200'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1500_MH-1300'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1500_MH-1400'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1500_MH-350'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1500_MH-400'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1500_MH-500'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1500_MH-600'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1500_MH-700'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1500_MH-800'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1500_MH-900'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1600_MH-1000'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1600_MH-1100'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1600_MH-1200'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1600_MH-1300'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1600_MH-1400'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1600_MH-1500'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1600_MH-350'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1600_MH-400'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1600_MH-500'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1600_MH-600'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1600_MH-700'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1600_MH-800'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1600_MH-900'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1700_MH-1000'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1700_MH-1100'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1700_MH-1200'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1700_MH-1300'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1700_MH-1400'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1700_MH-1500'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1700_MH-1600'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1700_MH-350'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1700_MH-400'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1700_MH-500'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1700_MH-600'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1700_MH-700'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1700_MH-800'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1700_MH-900'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1800_MH-1000'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1800_MH-1100'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1800_MH-1200'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1800_MH-1300'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1800_MH-1400'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1800_MH-1500'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1800_MH-1600'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1800_MH-1700'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1800_MH-350'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1800_MH-400'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1800_MH-500'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1800_MH-600'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1800_MH-700'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1800_MH-800'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1800_MH-900'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1900_MH-1000'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1900_MH-1100'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1900_MH-1200'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1900_MH-1300'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1900_MH-1400'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1900_MH-1500'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1900_MH-1600'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1900_MH-1700'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1900_MH-1800'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1900_MH-350'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1900_MH-400'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1900_MH-500'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1900_MH-600'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1900_MH-700'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1900_MH-800'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-1900_MH-900'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2000_MH-1000'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2000_MH-1100'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2000_MH-1200'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2000_MH-1300'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2000_MH-1400'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2000_MH-1500'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2000_MH-1600'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2000_MH-1700'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2000_MH-1800'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2000_MH-1900'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2000_MH-350'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2000_MH-400'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2000_MH-500'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2000_MH-600'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2000_MH-700'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2000_MH-800'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2000_MH-900'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2100_MH-1000'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2100_MH-1100'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2100_MH-1200'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2100_MH-1300'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2100_MH-1400'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2100_MH-1500'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2100_MH-1600'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2100_MH-1700'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2100_MH-1800'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2100_MH-1900'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2100_MH-2000'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2100_MH-350'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2100_MH-400'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2100_MH-500'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2100_MH-600'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2100_MH-700'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2100_MH-800'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-2100_MH-900'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-430_MH-330'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-450_MH-330'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-450_MH-350'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-500_MH-330'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-500_MH-350'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-500_MH-370'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-500_MH-400'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-550_MH-330'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-550_MH-350'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-550_MH-400'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-550_MH-450'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-600_MH-330'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-600_MH-350'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-600_MH-400'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-600_MH-450'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-600_MH-500'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-650_MH-330'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-650_MH-350'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-650_MH-400'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-650_MH-450'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-650_MH-500'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-650_MH-550'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-700_MH-330'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-700_MH-350'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-700_MH-370'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-700_MH-400'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-700_MH-450'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-700_MH-500'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-700_MH-550'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-700_MH-600'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-750_MH-330'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-750_MH-350'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-750_MH-400'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-750_MH-450'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-750_MH-500'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-750_MH-550'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-750_MH-600'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-750_MH-650'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-800_MH-330'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-800_MH-350'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-800_MH-400'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-800_MH-450'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-800_MH-500'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-800_MH-550'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-800_MH-600'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-800_MH-650'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-800_MH-700'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-850_MH-330'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-850_MH-350'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-850_MH-400'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-850_MH-450'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-850_MH-500'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-850_MH-550'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-850_MH-600'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-850_MH-650'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-850_MH-700'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-850_MH-750'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-900_MH-330'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-900_MH-350'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-900_MH-370'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-900_MH-400'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-900_MH-450'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-900_MH-500'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-900_MH-550'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-900_MH-600'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-900_MH-650'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-900_MH-700'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-900_MH-750'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-900_MH-800'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-950_MH-330'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-950_MH-350'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-950_MH-400'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-950_MH-450'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-950_MH-500'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-950_MH-550'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-950_MH-600'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-950_MH-650'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-950_MH-700'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-950_MH-750'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-950_MH-800'] = ['xsec=1',             'kfact=1.000',  'ref=X']
xs_db['AToZHToLLTTbar_MA-950_MH-850'] = ['xsec=1',             'kfact=1.000',  'ref=X']

# WW aTGCs
xs_db['WWToLNuLNu_MWW-0To500']         = ['xsec=4.1880002',             'kfact=1.000',  'ref=X']
xs_db['WWToLNuLNu_MWW-500To750']         = ['xsec=0.2617599',             'kfact=1.000',  'ref=X']
xs_db['WWToLNuLNu_MWW-750To1000']         = ['xsec=0.0928599',             'kfact=1.000',  'ref=X']
xs_db['WWToLNuLNu_MWW-1000ToInf']         = ['xsec=0.1599200',             'kfact=1.000',  'ref=X']

# Added since NanoGardener?
xs_db["EWKZ2Jets_ZToLL_M-50_MJJ-120"]                 = ["xsec=1.723", "kfact=1.000", "ref=N"]
xs_db["EWKZ2Jets_ZToLL_M-50_MJJ-120_herwig7_angular"] = ["xsec=1.723", "kfact=1.000", "ref=N"]

