from django.test import TestCase
from .models import Dataset
from .views import  filterData
import pandas as pd
from LinearRegression.views import linearRegression
from LinearRegression.models import TrainedModel
import json
import numpy as np
# Create your tests here.
class DatasetModelTests(TestCase):
    data = str(b'------WebKitFormBoundaryBoSe6RfDBSBWTKSd\r\nContent-Disposition: form-data; name="dataset"; filename="train.csv"\r\nContent-Type: text/csv\r\n\r\nNo,x,y\n1,24,21.54945196\n2,50,47.46446305\n3,15,17.21865634\n4,38,36.58639803\n5,87,87.28898389\n6,36,32.46387493\n7,12,10.78089683\n8,81,80.7633986\n9,25,24.61215147\n10,5,6.963319071\n11,16,11.23757338\n12,16,13.53290206\n13,24,24.60323899\n14,39,39.40049976\n15,54,48.43753838\n16,60,61.69900319\n17,26,26.92832418\n18,73,70.4052055\n19,29,29.34092408\n20,31,25.30895192\n21,68,69.02934339\n22,87,84.99484703\n23,58,57.04310305\n24,54,50.5921991\n25,84,83.02772202\n26,58,57.05752706\n27,49,47.95883341\n28,20,24.34226432\n29,90,94.68488281\n30,48,48.03970696\n31,4,7.08132338\n32,25,21.99239907\n33,42,42.33151664\n34,0,0.329089443\n35,60,61.92303698\n36,93,91.17716423\n37,39,39.45358014\n38,7,5.996069607\n39,21,22.59015942\n40,68,61.18044414\n41,84,85.02778957\n42,0,-1.28631089\n43,58,61.94273962\n44,19,21.96033347\n45,36,33.66194193\n46,19,17.60946242\n47,59,58.5630564\n48,51,52.82390762\n49,19,22.1363481\n50,33,35.07467353\n51,85,86.18822311\n52,44,42.63227697\n53,5,4.09817744\n54,59,61.2229864\n55,14,17.70677576\n56,9,11.85312574\n57,75,80.23051695\n58,69,62.64931741\n59,10,9.616859804\n60,17,20.02797699\n61,58,61.7510743\n62,74,71.61010303\n63,21,23.77154623\n64,51,51.90142035\n65,19,22.66073682\n66,50,50.02897927\n67,24,26.68794368\n68,0,0.376911899\n69,12,6.806419002\n70,75,77.33986001\n71,21,28.90260209\n72,64,66.7346608\n73,5,0.707510638\n74,58,57.07748383\n75,32,28.41453196\n76,41,44.46272123\n77,7,7.459605998\n78,4,2.316708112\n79,5,4.928546187\n80,49,52.50336074\n81,90,91.19109623\n82,3,8.489164326\n83,11,6.963371967\n84,32,31.97989959\n85,83,81.4281205\n86,25,22.62365422\n87,83,78.52505087\n88,26,25.80714057\n89,76,73.51081775\n90,95,91.775467\n91,53,49.21863516\n92,77,80.50445387\n93,42,50.05636123\n94,25,25.46292549\n95,54,55.32164264\n96,55,59.1244888\n97,0,1.100686692\n98,73,71.98020786\n99,35,30.13666408\n100,86,83.88427405\n101,90,89.91004752\n102,13,8.335654576\n103,46,47.88388961\n104,46,45.00397413\n105,32,31.15664574\n106,8,9.190375682\n107,71,74.83135003\n108,28,30.23177607\n109,24,24.21914027\n110,56,57.87219151\n111,49,50.61728392\n112,79,78.67470043\n113,90,86.236707\n114,89,89.10409255\n115,41,43.26595082\n116,27,26.68273277\n117,58,59.46383041\n118,26,28.90055826\n119,31,31.300416\n120,70,71.1433266\n121,71,68.4739206\n122,39,39.98238856\n123,7,4.075776144\n124,48,47.85817542\n125,56,51.20390217\n126,45,43.9367213\n127,41,38.13626679\n128,3,3.574661632\n129,37,36.4139958\n130,24,22.21908523\n131,68,63.5312572\n132,47,49.86702787\n133,27,21.53140009\n134,68,64.05710234\n135,74,70.77549842\n136,95,92.15749762\n137,79,81.22259156\n138,21,25.10114067\n139,95,94.08853397\n140,54,53.25166165\n141,56,59.16236621\n142,80,75.24148428\n143,26,28.22325833\n144,25,25.33323728\n145,8,6.364615703\n146,95,95.4609216\n147,94,88.64183756\n148,54,58.70318693\n149,7,6.815491279\n150,99,99.40394676\n151,36,32.77049249\n152,48,47.0586788\n153,65,60.53321778\n154,42,40.30929858\n155,93,89.42222685\n156,86,86.82132066\n157,26,26.11697543\n158,51,53.26657596\n159,100,96.62327888\n160,94,95.78441027\n161,6,6.047286687\n162,24,24.47387908\n163,75,75.96844763\n164,7,3.829381009\n165,53,52.51703683\n166,73,72.80457527\n167,16,14.10999096\n168,80,80.86087062\n169,77,77.01988215\n170,89,86.26972444\n171,80,77.13735466\n172,55,51.47649476\n173,19,17.34557531\n174,56,57.72853572\n175,47,44.15029394\n176,56,59.24362743\n177,2,-1.053275611\n178,82,86.79002254\n179,57,60.14031858\n180,44,44.04222058\n181,26,24.5227488\n182,52,52.95305521\n183,41,43.16133498\n184,44,45.67562576\n185,3,-2.830749501\n186,31,29.19693178\n187,97,96.49812401\n188,21,22.5453232\n189,17,20.10741433\n190,7,4.035430253\n191,61,61.14568518\n192,10,13.97163653\n193,52,55.34529893\n194,10,12.18441166\n195,65,64.00077658\n196,71,70.3188322\n197,4,-0.936895047\n198,24,18.91422276\n199,26,23.87590331\n200,51,47.5775361\n201,42,43.2736092\n202,62,66.48278755\n203,74,75.72605529\n204,77,80.59643338\n205,3,-2.235879852\n206,50,47.04654956\n207,24,21.59635575\n208,37,32.87558963\n209,58,57.95782956\n210,52,52.24760027\n211,27,24.58286902\n212,14,12.12573805\n213,100,100.0158026\n214,3530.15736917,\n215,72,74.04682658\n216,5,1.611947467\n217,71,70.36836307\n218,54,52.26831735\n219,84,83.1286166\n220,42,43.64765048\n221,54,49.44785426\n222,74,72.6356699\n223,54,52.78130641\n224,53,57.11195136\n225,78,79.1050629\n226,97,101.6228548\n227,49,53.5825402\n228,71,68.92139297\n229,48,46.9666961\n230,51,51.02642868\n231,89,85.52073551\n232,99,99.51685756\n233,93,94.63911256\n234,49,46.78357742\n235,18,21.21321959\n236,65,58.37266004\n237,83,87.22059677\n238,100,102.4967859\n239,41,43.88314335\n240,52,53.06655757\n241,29,26.33464785\n242,97,98.52008934\n243,7,9.400497579\n244,51,52.94026699\n245,58,53.83020877\n246,50,45.94511142\n247,67,65.0132736\n248,89,86.5069584\n249,76,75.63280796\n250,35,36.78035027\n251,99,100.5328916\n252,31,29.04466136\n253,52,51.70352433\n254,11,9.199954718\n255,66,71.70015848\n256,50,49.82634062\n257,39,37.49971096\n258,60,53.65084683\n259,35,33.92561965\n260,53,49.92639685\n261,14,8.148154262\n262,49,49.72359037\n263,16,16.16712757\n264,76,75.30033002\n265,13,9.577368568\n266,51,48.38088357\n267,70,72.95331671\n268,98,92.59573853\n269,86,88.85523586\n270,100,99.00361771\n271,46,45.09439571\n272,51,46.94362684\n273,50,48.33449605\n274,91,94.92329574\n275,48,47.78165248\n276,81,81.28960746\n277,38,37.83155021\n278,40,39.69185252\n279,79,76.92664854\n280,96,88.02990531\n281,60,56.99178872\n282,70,72.58929383\n283,44,44.98103442\n284,11,11.99017641\n285,6,1.919513328\n286,5,1.628826073\n287,72,66.27746655\n288,55,57.53887255\n289,95,94.70291077\n290,41,41.21469904\n291,25,25.04169243\n292,1,3.778209914\n293,55,50.50711779\n294,4,9.682408486\n295,48,48.88147608\n296,55,54.40348599\n297,75,71.70233156\n298,68,69.35848388\n299,100,99.98491591\n300,25,26.03323718\n301,75,75.48910307\n302,34,36.59623056\n303,38,40.95102191\n304,92,86.78316267\n305,21,15.50701184\n306,88,85.86077871\n307,75,79.20610113\n308,76,80.80643766\n309,44,48.59717283\n310,10,13.93415049\n311,21,27.3051179\n312,16,14.00226297\n313,32,33.67416\n314,13,13.11612884\n315,26,24.76649193\n316,70,73.68477876\n317,77,77.53149541\n318,77,76.24503196\n319,88,88.0578931\n320,35,35.02445799\n321,24,21.65857739\n322,17,17.33681562\n323,91,94.36778957\n324,32,33.43396307\n325,36,32.52179399\n326,89,90.57741298\n327,69,71.25634126\n328,30,31.23212856\n329,6,5.398840061\n330,22,18.56241391\n331,67,71.97121038\n332,9,5.225759566\n333,74,73.5964342\n334,50,49.76948983\n335,85,82.69087513\n336,3,1.652309089\n337,0,-3.836652144\n338,59,62.03811556\n339,62,61.26514581\n340,17,13.24991628\n341,90,88.61672694\n342,23,21.13655528\n343,19,23.85017475\n344,93,92.01203405\n345,14,10.26712261\n346,58,54.14681616\n347,87,87.00645713\n348,37,37.69447352\n349,20,19.62278654\n350,35,34.78561007\n351,63,62.03190983\n352,56,52.67003801\n353,62,58.09031476\n354,98,97.19448821\n355,90,90.50155298\n356,51,50.5123462\n357,93,94.45211871\n358,22,21.10794636\n359,38,37.36298431\n360,13,10.28574844\n361,98,96.04932416\n362,99,100.0953697\n363,31,30.6063167\n364,94,96.19000542\n365,73,71.30828034\n366,37,34.59311043\n367,23,19.02332876\n368,11,10.76669688\n369,88,90.5799868\n370,47,48.71787679\n371,79,78.74139764\n372,91,85.23492274\n373,71,71.65789964\n374,10,8.938990554\n375,39,39.89606046\n376,92,91.85091116\n377,99,99.11200375\n378,28,26.22196486\n379,32,33.21584226\n380,32,35.72392691\n381,75,76.88604495\n382,99,99.30874567\n383,27,25.77161074\n384,64,67.85169407\n385,98,98.50371084\n386,38,31.11331895\n387,46,45.51171028\n388,13,12.65537808\n389,96,95.56065366\n390,9,9.526431641\n391,34,36.10893209\n392,49,46.43628318\n393,1,-3.83998112\n394,50,48.97302037\n395,94,93.25305499\n396,27,23.47650968\n397,20,17.13551132\n398,12,14.55896144\n399,45,41.53992729\n400,91,91.64730552\n401,61,66.16652565\n402,10,9.230857489\n403,47,47.41377893\n404,33,34.76441561\n405,84,86.10796637\n406,24,21.81267954\n407,48,48.89963951\n408,48,46.78108638\n409,9,12.91328547\n410,93,94.55203143\n411,99,94.97068753\n412,8,2.379172481\n413,20,21.47982988\n414,38,35.79795462\n415,78,82.0763803\n416,81,78.87097714\n417,42,47.2492425\n418,95,96.18852325\n419,78,78.38491927\n420,44,42.94274064\n421,68,64.43231595\n422,87,84.21191485\n423,58,57.3069783\n424,52,52.52101436\n425,26,25.7440243\n426,75,75.42283401\n427,48,53.62523007\n428,71,75.14466308\n429,77,74.12151511\n430,34,36.24807243\n431,24,20.21665898\n432,70,66.94758118\n433,29,34.07278254\n434,76,73.13850045\n435,98,92.85929155\n436,28,28.36793808\n437,87,85.59308727\n438,9,10.68453755\n439,87,86.10708624\n440,33,33.22031418\n441,64,66.09563422\n442,17,19.30486546\n443,49,48.84542083\n444,95,93.73176312\n445,75,75.45758614\n446,89,91.24239226\n447,81,87.15690853\n448,25,25.53752833\n449,47,46.06629478\n450,50,49.65277661\n451,5,7.382244165\n452,68,71.11189935\n453,84,83.50570521\n454,8,8.791139893\n455,41,33.30638903\n456,26,26.40362524\n457,89,91.72960726\n458,78,82.53030719\n459,34,36.67762733\n460,92,86.98450355\n461,27,32.34784175\n462,12,16.78353974\n463,2,1.576584383\n464,22,17.4618141\n465,0,2.116113029\n466,26,24.34804332\n467,50,48.29491198\n468,84,85.52145453\n469,70,73.71434779\n470,66,63.15189497\n471,42,38.46213684\n472,19,19.47100788\n473,94,94.07428225\n474,71,67.92051286\n475,19,22.58096241\n476,16,16.01629889\n477,49,48.43307886\n478,29,29.6673599\n479,29,26.65566328\n480,86,86.28206739\n481,50,50.82304924\n482,86,88.57251713\n483,30,32.59980745\n484,23,21.02469368\n485,20,20.72894979\n486,16,20.38051187\n487,57,57.25180153\n488,8,6.967537054\n489,8,10.240085\n490,62,64.94841088\n491,55,55.35893915\n492,30,31.24365589\n493,86,90.72048818\n494,62,58.750127\n495,51,55.85003198\n496,61,60.19925869\n497,86,85.03295412\n498,61,60.38823085\n499,21,18.44679787\n500,81,82.18839247\n501,97,94.2963344\n502,5,7.682024586\n503,61,61.01858089\n504,47,53.60562216\n505,98,94.47728801\n506,30,27.9645947\n507,63,62.55662585\n508,0,1.406254414\n509,100,101.7003412\n510,18,13.84973988\n511,30,28.99769315\n512,98,99.04315693\n513,16,15.56135514\n514,22,24.63528393\n515,55,53.98393374\n516,43,42.91449728\n517,75,74.29662112\n518,91,91.17012883\n519,46,49.42440876\n520,85,82.47683519\n521,55,56.15303953\n522,36,37.17063131\n523,49,46.36928662\n524,94,97.02383456\n525,43,40.83182104\n526,22,24.08498313\n527,37,41.14386358\n528,24,21.97388066\n529,95,100.740897\n530,61,61.19971596\n531,75,74.39517002\n532,68,69.04377173\n533,58,56.68718792\n534,5,5.860391715\n535,53,55.72021356\n536,80,79.22021816\n537,83,86.30177517\n538,25,25.26971886\n539,34,36.33294447\n540,26,27.65574228\n541,90,94.79690531\n542,60,58.67366671\n543,49,56.15934471\n544,19,18.40919388\n545,92,86.26936988\n546,29,26.59436195\n547,8,8.452520159\n548,57,56.18131518\n549,29,27.65452669\n550,19,20.87391785\n551,81,77.83354439\n552,50,50.01787825\n553,15,9.290856256\n554,70,75.0284725\n555,39,38.3037698\n556,43,44.70786405\n557,21,22.51016575\n558,98,102.4959452\n559,86,86.76845244\n560,16,13.89748578\n561,25,24.81824269\n562,31,33.94224862\n563,93,92.26970059\n564,67,68.73365081\n565,49,47.38516883\n566,25,32.37576914\n567,88,87.67388681\n568,54,54.57648371\n569,21,18.06450222\n570,8,7.896539841\n571,32,35.00341078\n572,35,36.72823317\n573,67,65.84975426\n574,90,89.59295492\n575,59,61.69026202\n576,15,11.60499315\n577,67,71.0826803\n578,42,43.71901164\n579,44,41.57421008\n580,77,74.25552425\n581,68,66.28310437\n582,36,36.62438077\n583,11,10.32374866\n584,10,7.156457657\n585,65,67.88603132\n586,98,101.1097591\n587,98,98.6132033\n588,49,50.19083844\n589,31,27.83896261\n590,56,55.9249564\n591,70,76.47340872\n592,91,92.05756378\n593,25,27.35245439\n594,54,55.32083476\n595,39,41.39990349\n596,91,93.59057024\n597,3,5.297054029\n598,22,21.01429422\n599,2,2.267059451\n600,2,-0.121860502\n601,65,66.49546208\n602,71,73.83637687\n603,42,42.10140878\n604,76,77.35135732\n605,43,41.02251779\n606,8,14.75305272\n607,86,83.28199022\n608,87,89.93374342\n609,3,2.286571686\n610,58,55.61421297\n611,62,62.15313408\n612,89,89.55803528\n613,95,94.00291863\n614,28,26.78023848\n615,0,-0.764537626\n616,1,0.282866003\n617,49,44.26800515\n618,21,19.85174138\n619,46,47.15960005\n620,11,8.359366572\n621,89,92.08157084\n622,37,41.88734051\n623,29,30.5413129\n624,44,46.87654473\n625,96,96.35659485\n626,16,17.9170699\n627,74,71.67949917\n628,35,32.64997554\n629,42,39.34482965\n630,16,17.03401999\n631,56,52.87524074\n632,18,15.85414849\n633,100,108.8716183\n634,54,49.30477253\n635,92,89.4749477\n636,63,63.67348242\n637,81,83.78410946\n638,73,73.51136922\n639,48,46.80297244\n640,1,5.809946802\n641,85,85.23027975\n642,14,10.58213964\n643,25,21.37698317\n644,45,46.0537745\n645,98,95.2389253\n646,97,94.15149206\n647,58,54.54868046\n648,93,87.36260449\n649,88,88.47741598\n650,89,84.48045678\n651,47,48.79647071\n652,6,10.76675683\n653,34,30.48882921\n654,30,29.76846185\n655,16,13.51574749\n656,86,86.12955884\n657,40,43.30022747\n658,52,51.92110232\n659,15,16.49185287\n660,4,7.998073432\n661,95,97.66689567\n662,99,89.80545367\n663,35,38.07166567\n664,58,60.27852322\n665,10,6.709195759\n666,16,18.35488924\n667,53,56.37058203\n668,58,62.80064204\n669,42,41.25155632\n670,24,19.42637541\n671,84,82.88935804\n672,64,63.61364981\n673,12,11.29627199\n674,61,60.02274882\n675,75,72.60339326\n676,15,11.87964573\n677,100,100.7012737\n678,43,45.12420809\n679,13,14.81106804\n680,48,48.09368034\n681,45,42.29145672\n682,52,52.73389794\n683,34,36.72396986\n684,30,28.64535198\n685,65,62.16675273\n686,100,95.58459518\n687,67,66.04325304\n688,99,99.9566225\n689,45,46.14941984\n690,87,89.13754963\n691,73,69.71787806\n692,9,12.31736648\n693,81,78.20296268\n694,72,71.30995371\n695,81,81.45544709\n696,58,58.59500642\n697,93,94.62509374\n698,82,88.60376995\n699,66,63.64868529\n700,97,94.9752655\n\r\n------WebKitFormBoundaryBoSe6RfDBSBWTKSd\r\nContent-Disposition: form-data; name="id"\r\n\r\n1\r\n------WebKitFormBoundaryBoSe6RfDBSBWTKSd--\r\n')

    id,filename,dataset,nullValues = filterData(data)
    obj = None
    def test_datasets_model(self):
        FalseObject = ''
        try:
            FalseObject = Dataset.objects.get(UserId=2)
        except:
            FalseObject = "Dataset matching query does not exist."
        
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset)
        self.obj.save()
        o = Dataset.objects.get(UserId = self.id,filename=self.filename)
      
        ## Check for success 
        self.assertEquals(self.obj,o)
       
        ##Check if it fails 
       
        self.assertEquals("Dataset matching query does not exist.",FalseObject)
        
    
    def test_UserId(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset)
        self.obj.save()
        FromDb = Dataset.objects.get(UserId =self.id,filename=self.filename)
       
       ##Check UserId is correct
        self.assertEquals(self.id,FromDb.UserId)

        #Check incorrect id is false
        self.assertNotEquals(self.id,-1)
    
    def test_filename(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset)
        self.obj.save()
        FromDb = Dataset.objects.get(UserId =self.id,filename=self.filename)

        "Check filename is stored"
        self.assertEquals(self.obj.filename,FromDb.filename)
        "Only allows csv"
        self.assertNotEquals(self.filename,"train.odt")
    
    def test_data_is_stored_correct(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset)
        self.obj.save()
        FromDb = Dataset.objects.get(UserId =self.id,filename=self.filename)
        x = pd.read_json(self.dataset).to_numpy()
        y = pd.read_json(FromDb.data).to_numpy()
        ##Check data is stored the same in db as incoming data
        self.assertEquals(x.all(),y.all())
        ##check that values are not swapped
        self.assertNotEquals(x.all(),y.any())
    
    def test_type_of_UserId(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset)
        self.obj.save()

        #must be int
        self.assertEquals(type(self.id),int)
        #cant be string
        self.assertNotEquals(type(self.id),str)

    def test_type_of_filename(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset)
        self.obj.save()

        #must be string
        self.assertEquals(type(self.filename),str)
        #cant be anything else
        self.assertNotEquals(type(self.filename),dict)

    def test_type_of_dataset(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset)
        self.obj.save()

        #must be string
        self.assertEquals(type(self.obj.data),str)
        #cant be anything else
        self.assertNotEquals(type(self.data),dict)
    
    def test_type_of_nullvalues(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset)
        self.obj.save()

        #must be string
        self.assertEquals(type(self.nullValues),np.int64)
        #cant be anything else
        self.assertNotEquals(type(self.nullValues),str)

    def test_type_of_learningRate(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset)
        self.obj.save()
        self.obj.learningRate = "auto"

        #must be string
        self.assertEquals(type(self.obj.learningRate),str)
        #cant be anything else
        self.assertNotEquals(type(self.obj.learningRate),int)
    
    def test_type_of_tol(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset)
        self.obj.save()
        self.obj.tol = "auto"

        #must be string
        self.assertEquals(type(self.obj.tol),str)
        #cant be anything else
        self.assertNotEquals(type(self.obj.tol),int)

    def test_type_of_split(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset)
        self.obj.save()
        self.obj.split = 0.8

        #must be float
        self.assertEquals(type(self.obj.split),float)
        #cant be int
        self.assertNotEquals(type(self.obj.learningRate),int)

    def test_nullValues(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset,nullValues=self.nullValues)
        self.obj.save()
        o = Dataset.objects.get(UserId = self.id)

        self.assertEquals(self.obj.nullValues,o.nullValues)

        self.assertNotEquals(self.obj.nullValues,0)
    
    def test_data_columns(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset,nullValues=self.nullValues)
        self.obj.save()
        o = Dataset.objects.get(UserId = self.id)

        self.assertEquals(list(pd.read_json(self.dataset).columns),list(pd.read_json(o.data).columns))

    def test_data_shape_columns(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset,nullValues=self.nullValues)
        self.obj.save()
        o = Dataset.objects.get(UserId = self.id)
        self.assertEquals(pd.read_json(self.dataset).shape[0],pd.read_json(o.data).shape[0])
        self.assertNotEquals(pd.read_json(self.dataset).shape[0],0)
    
    def test_data_shape_rows(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset,nullValues=self.nullValues)
        self.obj.save()
        o = Dataset.objects.get(UserId = self.id)
        self.assertEquals(pd.read_json(self.dataset).shape[1],pd.read_json(o.data).shape[1])
        self.assertNotEquals(pd.read_json(self.dataset).shape[1],0)

    def test_if_learningRate_can_be_empty(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset,nullValues=self.nullValues)
        self.obj.save()
        o = Dataset.objects.get(UserId = self.id)
        o.learningRate = json.dumps("auto")

        self.assertEquals(json.dumps("auto"),o.learningRate)
        self.assertNotEquals(json.dumps("empty"),o.learningRate)
    
    def test_if_tol_can_be_empty(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset,nullValues=self.nullValues)
        self.obj.save()
        o = Dataset.objects.get(UserId = self.id)
        o.tol = json.dumps("auto")

        self.assertEquals(json.dumps("auto"),o.tol)
        self.assertNotEquals(json.dumps("empty"),o.tol)
    
    results = []

    def test_do_linear_regression(self):
        id,filename,dataset,nullValues = filterData(self.data)
        
        obj = Dataset.objects.create(UserId = id, filename=filename,data=dataset,nullValues=nullValues)
        obj.save()
        o = Dataset.objects.get(UserId = id,filename=filename)
        o.tol = json.dumps("auto")
        o.learningRate = json.dumps("auto")
        o.split = 80

        self.results  = linearRegression(o.UserId,o.filename,o.learningRate,o.tol,pd.read_json(o.data),int(o.split)/100)
        
        ## check that the ml was performed and not empty
        self.assertEquals(len(self.results),12)
        

        ##Check for failures
        self.assertNotEquals(len(self.results),-1)
        
    
    def test_json_features(self):
        id,filename,dataset,nullValues = filterData(self.data)
        obj = Dataset.objects.create(UserId = id, filename=filename,data=dataset,nullValues=nullValues)
        obj.save()
        o = Dataset.objects.get(UserId = id,filename=filename)
        o.tol = json.dumps("auto")
        o.learningRate = json.dumps("auto")
        o.split = 80

        self.results  = linearRegression(o.UserId,o.filename,o.learningRate,o.tol,pd.read_json(o.data),int(o.split)/100)
        self.assertEquals(type(self.results[0]),dict)
        self.assertNotEquals(type(self.results[0]),str)
    
    def test_accuracy(self):
        id,filename,dataset,nullValues = filterData(self.data)
        obj = Dataset.objects.create(UserId = id, filename=filename,data=dataset,nullValues=nullValues)
        obj.save()
        o = Dataset.objects.get(UserId = id,filename=filename)
        o.tol = json.dumps("auto")
        o.learningRate = json.dumps("auto")
        o.split = 80

        self.results  = linearRegression(o.UserId,o.filename,o.learningRate,o.tol,pd.read_json(o.data),int(o.split)/100)
        self.assertAlmostEquals(round(self.results[8],2),0.99)
        self.assertNotEquals(round(self.results[8],2),0)
    
    def test_numFeatures(self):
        id,filename,dataset,nullValues = filterData(self.data)
        obj = Dataset.objects.create(UserId = id, filename=filename,data=dataset,nullValues=nullValues)
        obj.save()
        o = Dataset.objects.get(UserId = id,filename=filename)
        o.tol = json.dumps("auto")
        o.learningRate = json.dumps("auto")
        o.split = 80

        self.results  = linearRegression(o.UserId,o.filename,o.learningRate,o.tol,pd.read_json(o.data),int(o.split)/100)
        self.assertEquals(len(self.results[0]['0']),3)
        self.assertNotEquals(len(self.results[0]['0']),1)