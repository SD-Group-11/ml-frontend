from django.test import TestCase
from .models import Dataset
from .views import  filterData,delete_dataset
import pandas as pd
from users.models import User
from LinearRegression.views import linearRegression,TrainingLinearRegression
from LinearRegression.models import TrainedModel
import json
import numpy as np
# Create your tests here.
class DatasetModelTests(TestCase):
    data = str(b'------WebKitFormBoundaryawv8nwBYkYVuljBX\r\nContent-Disposition: form-data; name="dataset"; filename="Train.csv"\r\nContent-Type: text/csv\r\n\r\nx,y\n24,21.54945196\n50,47.46446305\n15,17.21865634\n38,36.58639803\n87,87.28898389\n36,32.46387493\n12,10.78089683\n81,80.7633986\n25,24.61215147\n5,6.963319071\n16,11.23757338\n16,13.53290206\n24,24.60323899\n39,39.40049976\n54,48.43753838\n60,61.69900319\n26,26.92832418\n73,70.4052055\n29,29.34092408\n31,25.30895192\n68,69.02934339\n87,84.99484703\n58,57.04310305\n54,50.5921991\n84,83.02772202\n58,57.05752706\n49,47.95883341\n20,24.34226432\n90,94.68488281\n48,48.03970696\n4,7.08132338\n25,21.99239907\n42,42.33151664\n0,0.329089443\n60,61.92303698\n93,91.17716423\n39,39.45358014\n7,5.996069607\n21,22.59015942\n68,61.18044414\n84,85.02778957\n0,-1.28631089\n58,61.94273962\n19,21.96033347\n36,33.66194193\n19,17.60946242\n59,58.5630564\n51,52.82390762\n19,22.1363481\n33,35.07467353\n85,86.18822311\n44,42.63227697\n5,4.09817744\n59,61.2229864\n14,17.70677576\n9,11.85312574\n75,80.23051695\n69,62.64931741\n10,9.616859804\n17,20.02797699\n58,61.7510743\n74,71.61010303\n21,23.77154623\n51,51.90142035\n19,22.66073682\n50,50.02897927\n24,26.68794368\n0,0.376911899\n12,6.806419002\n75,77.33986001\n21,28.90260209\n64,66.7346608\n5,0.707510638\n58,57.07748383\n32,28.41453196\n41,44.46272123\n7,7.459605998\n4,2.316708112\n5,4.928546187\n49,52.50336074\n90,91.19109623\n3,8.489164326\n11,6.963371967\n32,31.97989959\n83,81.4281205\n25,22.62365422\n83,78.52505087\n26,25.80714057\n76,73.51081775\n95,91.775467\n53,49.21863516\n77,80.50445387\n42,50.05636123\n25,25.46292549\n54,55.32164264\n55,59.1244888\n0,1.100686692\n73,71.98020786\n35,30.13666408\n86,83.88427405\n90,89.91004752\n13,8.335654576\n46,47.88388961\n46,45.00397413\n32,31.15664574\n8,9.190375682\n71,74.83135003\n28,30.23177607\n24,24.21914027\n56,57.87219151\n49,50.61728392\n79,78.67470043\n90,86.236707\n89,89.10409255\n41,43.26595082\n27,26.68273277\n58,59.46383041\n26,28.90055826\n31,31.300416\n70,71.1433266\n71,68.4739206\n39,39.98238856\n7,4.075776144\n48,47.85817542\n56,51.20390217\n45,43.9367213\n41,38.13626679\n3,3.574661632\n37,36.4139958\n24,22.21908523\n68,63.5312572\n47,49.86702787\n27,21.53140009\n68,64.05710234\n74,70.77549842\n95,92.15749762\n79,81.22259156\n21,25.10114067\n95,94.08853397\n54,53.25166165\n56,59.16236621\n80,75.24148428\n26,28.22325833\n25,25.33323728\n8,6.364615703\n95,95.4609216\n94,88.64183756\n54,58.70318693\n7,6.815491279\n99,99.40394676\n36,32.77049249\n48,47.0586788\n65,60.53321778\n42,40.30929858\n93,89.42222685\n86,86.82132066\n26,26.11697543\n51,53.26657596\n100,96.62327888\n94,95.78441027\n6,6.047286687\n24,24.47387908\n75,75.96844763\n7,3.829381009\n53,52.51703683\n73,72.80457527\n16,14.10999096\n80,80.86087062\n77,77.01988215\n89,86.26972444\n80,77.13735466\n55,51.47649476\n19,17.34557531\n56,57.72853572\n47,44.15029394\n56,59.24362743\n2,-1.053275611\n82,86.79002254\n57,60.14031858\n44,44.04222058\n26,24.5227488\n52,52.95305521\n41,43.16133498\n44,45.67562576\n3,-2.830749501\n31,29.19693178\n97,96.49812401\n21,22.5453232\n17,20.10741433\n7,4.035430253\n61,61.14568518\n10,13.97163653\n52,55.34529893\n10,12.18441166\n65,64.00077658\n71,70.3188322\n4,-0.936895047\n24,18.91422276\n26,23.87590331\n51,47.5775361\n42,43.2736092\n62,66.48278755\n74,75.72605529\n77,80.59643338\n3,-2.235879852\n50,47.04654956\n24,21.59635575\n37,32.87558963\n58,57.95782956\n52,52.24760027\n27,24.58286902\n14,12.12573805\n100,100.0158026\n3530.15736917,\n72,74.04682658\n5,1.611947467\n71,70.36836307\n54,52.26831735\n84,83.1286166\n42,43.64765048\n54,49.44785426\n74,72.6356699\n54,52.78130641\n53,57.11195136\n78,79.1050629\n97,101.6228548\n49,53.5825402\n71,68.92139297\n48,46.9666961\n51,51.02642868\n89,85.52073551\n99,99.51685756\n93,94.63911256\n49,46.78357742\n18,21.21321959\n65,58.37266004\n83,87.22059677\n100,102.4967859\n41,43.88314335\n52,53.06655757\n29,26.33464785\n97,98.52008934\n7,9.400497579\n51,52.94026699\n58,53.83020877\n50,45.94511142\n67,65.0132736\n89,86.5069584\n76,75.63280796\n35,36.78035027\n99,100.5328916\n31,29.04466136\n52,51.70352433\n11,9.199954718\n66,71.70015848\n50,49.82634062\n39,37.49971096\n60,53.65084683\n35,33.92561965\n53,49.92639685\n14,8.148154262\n49,49.72359037\n16,16.16712757\n76,75.30033002\n13,9.577368568\n51,48.38088357\n70,72.95331671\n98,92.59573853\n86,88.85523586\n100,99.00361771\n46,45.09439571\n51,46.94362684\n50,48.33449605\n91,94.92329574\n48,47.78165248\n81,81.28960746\n38,37.83155021\n40,39.69185252\n79,76.92664854\n96,88.02990531\n60,56.99178872\n70,72.58929383\n44,44.98103442\n11,11.99017641\n6,1.919513328\n5,1.628826073\n72,66.27746655\n55,57.53887255\n95,94.70291077\n41,41.21469904\n25,25.04169243\n1,3.778209914\n55,50.50711779\n4,9.682408486\n48,48.88147608\n55,54.40348599\n75,71.70233156\n68,69.35848388\n100,99.98491591\n25,26.03323718\n75,75.48910307\n34,36.59623056\n38,40.95102191\n92,86.78316267\n21,15.50701184\n88,85.86077871\n75,79.20610113\n76,80.80643766\n44,48.59717283\n10,13.93415049\n21,27.3051179\n16,14.00226297\n32,33.67416\n13,13.11612884\n26,24.76649193\n70,73.68477876\n77,77.53149541\n77,76.24503196\n88,88.0578931\n35,35.02445799\n24,21.65857739\n17,17.33681562\n91,94.36778957\n32,33.43396307\n36,32.52179399\n89,90.57741298\n69,71.25634126\n30,31.23212856\n6,5.398840061\n22,18.56241391\n67,71.97121038\n9,5.225759566\n74,73.5964342\n50,49.76948983\n85,82.69087513\n3,1.652309089\n0,-3.836652144\n59,62.03811556\n62,61.26514581\n17,13.24991628\n90,88.61672694\n23,21.13655528\n19,23.85017475\n93,92.01203405\n14,10.26712261\n58,54.14681616\n87,87.00645713\n37,37.69447352\n20,19.62278654\n35,34.78561007\n63,62.03190983\n56,52.67003801\n62,58.09031476\n98,97.19448821\n90,90.50155298\n51,50.5123462\n93,94.45211871\n22,21.10794636\n38,37.36298431\n13,10.28574844\n98,96.04932416\n99,100.0953697\n31,30.6063167\n94,96.19000542\n73,71.30828034\n37,34.59311043\n23,19.02332876\n11,10.76669688\n88,90.5799868\n47,48.71787679\n79,78.74139764\n91,85.23492274\n71,71.65789964\n10,8.938990554\n39,39.89606046\n92,91.85091116\n99,99.11200375\n28,26.22196486\n32,33.21584226\n32,35.72392691\n75,76.88604495\n99,99.30874567\n27,25.77161074\n64,67.85169407\n98,98.50371084\n38,31.11331895\n46,45.51171028\n13,12.65537808\n96,95.56065366\n9,9.526431641\n34,36.10893209\n49,46.43628318\n1,-3.83998112\n50,48.97302037\n94,93.25305499\n27,23.47650968\n20,17.13551132\n12,14.55896144\n45,41.53992729\n91,91.64730552\n61,66.16652565\n10,9.230857489\n47,47.41377893\n33,34.76441561\n84,86.10796637\n24,21.81267954\n48,48.89963951\n48,46.78108638\n9,12.91328547\n93,94.55203143\n99,94.97068753\n8,2.379172481\n20,21.47982988\n38,35.79795462\n78,82.0763803\n81,78.87097714\n42,47.2492425\n95,96.18852325\n78,78.38491927\n44,42.94274064\n68,64.43231595\n87,84.21191485\n58,57.3069783\n52,52.52101436\n26,25.7440243\n75,75.42283401\n48,53.62523007\n71,75.14466308\n77,74.12151511\n34,36.24807243\n24,20.21665898\n70,66.94758118\n29,34.07278254\n76,73.13850045\n98,92.85929155\n28,28.36793808\n87,85.59308727\n9,10.68453755\n87,86.10708624\n33,33.22031418\n64,66.09563422\n17,19.30486546\n49,48.84542083\n95,93.73176312\n75,75.45758614\n89,91.24239226\n81,87.15690853\n25,25.53752833\n47,46.06629478\n50,49.65277661\n5,7.382244165\n68,71.11189935\n84,83.50570521\n8,8.791139893\n41,33.30638903\n26,26.40362524\n89,91.72960726\n78,82.53030719\n34,36.67762733\n92,86.98450355\n27,32.34784175\n12,16.78353974\n2,1.576584383\n22,17.4618141\n0,2.116113029\n26,24.34804332\n50,48.29491198\n84,85.52145453\n70,73.71434779\n66,63.15189497\n42,38.46213684\n19,19.47100788\n94,94.07428225\n71,67.92051286\n19,22.58096241\n16,16.01629889\n49,48.43307886\n29,29.6673599\n29,26.65566328\n86,86.28206739\n50,50.82304924\n86,88.57251713\n30,32.59980745\n23,21.02469368\n20,20.72894979\n16,20.38051187\n57,57.25180153\n8,6.967537054\n8,10.240085\n62,64.94841088\n55,55.35893915\n30,31.24365589\n86,90.72048818\n62,58.750127\n51,55.85003198\n61,60.19925869\n86,85.03295412\n61,60.38823085\n21,18.44679787\n81,82.18839247\n97,94.2963344\n5,7.682024586\n61,61.01858089\n47,53.60562216\n98,94.47728801\n30,27.9645947\n63,62.55662585\n0,1.406254414\n100,101.7003412\n18,13.84973988\n30,28.99769315\n98,99.04315693\n16,15.56135514\n22,24.63528393\n55,53.98393374\n43,42.91449728\n75,74.29662112\n91,91.17012883\n46,49.42440876\n85,82.47683519\n55,56.15303953\n36,37.17063131\n49,46.36928662\n94,97.02383456\n43,40.83182104\n22,24.08498313\n37,41.14386358\n24,21.97388066\n95,100.740897\n61,61.19971596\n75,74.39517002\n68,69.04377173\n58,56.68718792\n5,5.860391715\n53,55.72021356\n80,79.22021816\n83,86.30177517\n25,25.26971886\n34,36.33294447\n26,27.65574228\n90,94.79690531\n60,58.67366671\n49,56.15934471\n19,18.40919388\n92,86.26936988\n29,26.59436195\n8,8.452520159\n57,56.18131518\n29,27.65452669\n19,20.87391785\n81,77.83354439\n50,50.01787825\n15,9.290856256\n70,75.0284725\n39,38.3037698\n43,44.70786405\n21,22.51016575\n98,102.4959452\n86,86.76845244\n16,13.89748578\n25,24.81824269\n31,33.94224862\n93,92.26970059\n67,68.73365081\n49,47.38516883\n25,32.37576914\n88,87.67388681\n54,54.57648371\n21,18.06450222\n8,7.896539841\n32,35.00341078\n35,36.72823317\n67,65.84975426\n90,89.59295492\n59,61.69026202\n15,11.60499315\n67,71.0826803\n42,43.71901164\n44,41.57421008\n77,74.25552425\n68,66.28310437\n36,36.62438077\n11,10.32374866\n10,7.156457657\n65,67.88603132\n98,101.1097591\n98,98.6132033\n49,50.19083844\n31,27.83896261\n56,55.9249564\n70,76.47340872\n91,92.05756378\n25,27.35245439\n54,55.32083476\n39,41.39990349\n91,93.59057024\n3,5.297054029\n22,21.01429422\n2,2.267059451\n2,-0.121860502\n65,66.49546208\n71,73.83637687\n42,42.10140878\n76,77.35135732\n43,41.02251779\n8,14.75305272\n86,83.28199022\n87,89.93374342\n3,2.286571686\n58,55.61421297\n62,62.15313408\n89,89.55803528\n95,94.00291863\n28,26.78023848\n0,-0.764537626\n1,0.282866003\n49,44.26800515\n21,19.85174138\n46,47.15960005\n11,8.359366572\n89,92.08157084\n37,41.88734051\n29,30.5413129\n44,46.87654473\n96,96.35659485\n16,17.9170699\n74,71.67949917\n35,32.64997554\n42,39.34482965\n16,17.03401999\n56,52.87524074\n18,15.85414849\n100,108.8716183\n54,49.30477253\n92,89.4749477\n63,63.67348242\n81,83.78410946\n73,73.51136922\n48,46.80297244\n1,5.809946802\n85,85.23027975\n14,10.58213964\n25,21.37698317\n45,46.0537745\n98,95.2389253\n97,94.15149206\n58,54.54868046\n93,87.36260449\n88,88.47741598\n89,84.48045678\n47,48.79647071\n6,10.76675683\n34,30.48882921\n30,29.76846185\n16,13.51574749\n86,86.12955884\n40,43.30022747\n52,51.92110232\n15,16.49185287\n4,7.998073432\n95,97.66689567\n99,89.80545367\n35,38.07166567\n58,60.27852322\n10,6.709195759\n16,18.35488924\n53,56.37058203\n58,62.80064204\n42,41.25155632\n24,19.42637541\n84,82.88935804\n64,63.61364981\n12,11.29627199\n61,60.02274882\n75,72.60339326\n15,11.87964573\n100,100.7012737\n43,45.12420809\n13,14.81106804\n48,48.09368034\n45,42.29145672\n52,52.73389794\n34,36.72396986\n30,28.64535198\n65,62.16675273\n100,95.58459518\n67,66.04325304\n99,99.9566225\n45,46.14941984\n87,89.13754963\n73,69.71787806\n9,12.31736648\n81,78.20296268\n72,71.30995371\n81,81.45544709\n58,58.59500642\n93,94.62509374\n82,88.60376995\n66,63.64868529\n97,94.9752655\n\r\n------WebKitFormBoundaryawv8nwBYkYVuljBX\r\nContent-Disposition: form-data; name="id"\r\n\r\n1\r\n------WebKitFormBoundaryawv8nwBYkYVuljBX\r\nContent-Disposition: form-data; name="model"\r\n\r\nLinear Regression\r\n------WebKitFormBoundaryawv8nwBYkYVuljBX--\r\n')

    id,filename,dataset,nullValues,model = filterData(data)
    obj = None
    def test_datasets_model(self):
        FalseObject = ''
        try:
            FalseObject = Dataset.objects.get(UserId=2)
        except:
            FalseObject = "Dataset matching query does not exist."
        
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset,model = "Linear Regression")
        self.obj.save()
        o = Dataset.objects.get(UserId = self.id,filename=self.filename,model = "Linear Regression")
      
        ## Check for success 
        self.assertEquals(self.obj,o)
       
        ##Check if it fails 
       
        self.assertEquals("Dataset matching query does not exist.",FalseObject)
        
    
    def test_UserId(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset,model = "Linear Regression")
        self.obj.save()
        FromDb = Dataset.objects.get(UserId =self.id,filename=self.filename,model = "Linear Regression")
       
       ##Check UserId is correct
        self.assertEquals(self.id,FromDb.UserId)

        #Check incorrect id is false
        self.assertNotEquals(self.id,-1)
    
    def test_filename(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset,model = "Linear Regression")
        self.obj.save()
        FromDb = Dataset.objects.get(UserId =self.id,filename=self.filename,model = "Linear Regression")

        "Check filename is stored"
        self.assertEquals(self.obj.filename,FromDb.filename)
        "Only allows csv"
        self.assertNotEquals(self.filename,"train.odt")
    
    def test_data_is_stored_correct(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset,model = "Linear Regression")
        self.obj.save()
        FromDb = Dataset.objects.get(UserId =self.id,filename=self.filename,model = "Linear Regression")
        x = pd.read_json(self.dataset).to_numpy()
        y = pd.read_json(FromDb.data).to_numpy()
        ##Check data is stored the same in db as incoming data
        self.assertEquals(x.all(),y.all())
        ##check that values are not swapped
        self.assertNotEquals(x.all(),y.any())
    
    def test_type_of_UserId(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset,model = "Linear Regression")
        self.obj.save()

        #must be int
        self.assertEquals(type(self.id),int)
        #cant be string
        self.assertNotEquals(type(self.id),str)

    def test_type_of_filename(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset,model = "Linear Regression")
        self.obj.save()

        #must be string
        self.assertEquals(type(self.filename),str)
        #cant be anything else
        self.assertNotEquals(type(self.filename),dict)

    def test_type_of_dataset(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset,model = "Linear Regression")
        self.obj.save()

        #must be string
        self.assertEquals(type(self.obj.data),str)
        #cant be anything else
        self.assertNotEquals(type(self.data),dict)
    
    def test_type_of_nullvalues(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset,model = "Linear Regression")
        self.obj.save()

        #must be string
        self.assertEquals(type(self.nullValues),np.int64)
        #cant be anything else
        self.assertNotEquals(type(self.nullValues),str)

    def test_type_of_learningRate(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset,model = "Linear Regression")
        self.obj.save()
        self.obj.learningRate = "auto"

        #must be string
        self.assertEquals(type(self.obj.learningRate),str)
        #cant be anything else
        self.assertNotEquals(type(self.obj.learningRate),int)
    
    def test_type_of_tol(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset,model = "Linear Regression")
        self.obj.save()
        self.obj.tol = "auto"

        #must be string
        self.assertEquals(type(self.obj.tol),str)
        #cant be anything else
        self.assertNotEquals(type(self.obj.tol),int)

    def test_no_test_data(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset,model = "Linear Regression")
        self.obj.save()

        #must be float
        self.assertEquals(type(self.obj.testData),dict)
        #cant be int
        self.assertNotEquals(type(self.obj.learningRate),int)

    def test_nullValues(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset,nullValues=self.nullValues,model = "Linear Regression")
        self.obj.save()
        o = Dataset.objects.get(UserId = self.id)

        self.assertEquals(self.obj.nullValues,o.nullValues)

        self.assertNotEquals(self.obj.nullValues,0)
    
    def test_data_columns(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset,nullValues=self.nullValues,model = "Linear Regression")
        self.obj.save()
        o = Dataset.objects.get(UserId = self.id)

        self.assertEquals(list(pd.read_json(self.dataset).columns),list(pd.read_json(o.data).columns))

    def test_data_shape_columns(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset,nullValues=self.nullValues,model = "Linear Regression")
        self.obj.save()
        o = Dataset.objects.get(UserId = self.id)
        self.assertEquals(pd.read_json(self.dataset).shape[0],pd.read_json(o.data).shape[0])
        self.assertNotEquals(pd.read_json(self.dataset).shape[0],0)
    
    def test_data_shape_rows(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset,nullValues=self.nullValues,model = "Linear Regression")
        self.obj.save()
        o = Dataset.objects.get(UserId = self.id)
        self.assertEquals(pd.read_json(self.dataset).shape[1],pd.read_json(o.data).shape[1])
        self.assertNotEquals(pd.read_json(self.dataset).shape[1],0)

    def test_if_learningRate_can_be_empty(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset,nullValues=self.nullValues,model = "Linear Regression")
        self.obj.save()
        o = Dataset.objects.get(UserId = self.id)
        o.learningRate = json.dumps("auto")

        self.assertEquals(json.dumps("auto"),o.learningRate)
        self.assertNotEquals(json.dumps("empty"),o.learningRate)
    
    def test_if_tol_can_be_empty(self):
        self.obj = Dataset.objects.create(UserId = self.id, filename=self.filename,data=self.dataset,nullValues=self.nullValues,model = "Linear Regression")
        self.obj.save()
        o = Dataset.objects.get(UserId = self.id)
        o.tol = json.dumps("auto")

        self.assertEquals(json.dumps("auto"),o.tol)
        self.assertNotEquals(json.dumps("empty"),o.tol)
    
    results = []

    def test_do_linear_regression(self):
        id,filename,dataset,nullValues,model = filterData(self.data)
        
        obj = Dataset.objects.create(UserId = id, filename=filename,data=dataset,nullValues=nullValues,model = "Linear Regression")
        obj.save()
        o = Dataset.objects.get(UserId = id,filename=filename,model = "Linear Regression")
        o.tol = json.dumps("auto")
        o.learningRate = json.dumps("auto")

        self.results  = TrainingLinearRegression(o.UserId,o.filename,o.learningRate,o.tol,pd.read_json(o.data))
        
        ## check that the ml was performed and not empty
        self.assertEquals(len(self.results),7)
        

        ##Check for failures
        self.assertNotEquals(len(self.results),-1)
        
    
    def test_json_features(self):
        id,filename,dataset,nullValues,model = filterData(self.data)
        obj = Dataset.objects.create(UserId = id, filename=filename,data=dataset,nullValues=nullValues,model = "Linear Regression")
        obj.save()
        o = Dataset.objects.get(UserId = id,filename=filename,model = "Linear Regression")
        o.tol = json.dumps("auto")
        o.learningRate = json.dumps("auto")

        self.results  = TrainingLinearRegression(o.UserId,o.filename,o.learningRate,o.tol,pd.read_json(o.data))
        self.assertEquals(type(self.results[0]),dict)
        self.assertNotEquals(type(self.results[0]),str)
    
    def test_accuracy(self):
        id,filename,dataset,nullValues,model = filterData(self.data)
        obj = Dataset.objects.create(UserId = id, filename=filename,data=dataset,nullValues=nullValues,model = "Linear Regression")
        obj.save()
        o = Dataset.objects.get(UserId = id,filename=filename,model = "Linear Regression")
        o.tol = json.dumps("auto")
        o.learningRate = json.dumps("auto")

        self.results  = TrainingLinearRegression(o.UserId,o.filename,o.learningRate,o.tol,pd.read_json(o.data))
        self.assertAlmostEquals(round(self.results[5],2),0.99)
        self.assertNotEquals(round(self.results[5],2),0)
    
    def test_numFeatures(self):
        id,filename,dataset,nullValues,model = filterData(self.data)
        obj = Dataset.objects.create(UserId = id, filename=filename,data=dataset,nullValues=nullValues,model = "Linear Regression")
        obj.save()
        o = Dataset.objects.get(UserId = id,filename=filename,model = "Linear Regression")
        o.tol = json.dumps("auto")
        o.learningRate = json.dumps("auto")

        self.results  = TrainingLinearRegression(o.UserId,o.filename,o.learningRate,o.tol,pd.read_json(o.data))
        self.assertEquals(len(self.results[0]['0']),2)
        self.assertNotEquals(len(self.results[0]['0']),1)



    
    
