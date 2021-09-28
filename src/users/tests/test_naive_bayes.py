from django.test import TestCase
import pandas as pd
# Create your tests here.
from NaiveBayes.models import NBTrainedModel
from NaiveBayes.views import TrainNaiveBayes,UploadTrainingResults
from datasets.views import filterData
from datasets.models import Dataset
import json
class NaiveBayesModel(TestCase):


    d = str(b'------WebKitFormBoundaryg3tgYREfNvps5Jct\r\nContent-Disposition: form-data; name="dataset"; filename="Social_Network_Ads.csv"\r\nContent-Type: text/csv\r\n\r\nUser ID,Gender,Age,EstimatedSalary,Purchased\n15624510,Male,19,19000,0\n15810944,Male,35,20000,0\n15668575,Female,26,43000,0\n15603246,Female,27,57000,0\n15804002,Male,19,76000,0\n15728773,Male,27,58000,0\n15598044,Female,27,84000,0\n15694829,Female,32,150000,1\n15600575,Male,25,33000,0\n15727311,Female,35,65000,0\n15570769,Female,26,80000,0\n15606274,Female,26,52000,0\n15746139,Male,20,86000,0\n15704987,Male,32,18000,0\n15628972,Male,18,82000,0\n15697686,Male,29,80000,0\n15733883,Male,47,25000,1\n15617482,Male,45,26000,1\n15704583,Male,46,28000,1\n15621083,Female,48,29000,1\n15649487,Male,45,22000,1\n15736760,Female,47,49000,1\n15714658,Male,48,41000,1\n15599081,Female,45,22000,1\n15705113,Male,46,23000,1\n15631159,Male,47,20000,1\n15792818,Male,49,28000,1\n15633531,Female,47,30000,1\n15744529,Male,29,43000,0\n15669656,Male,31,18000,0\n15581198,Male,31,74000,0\n15729054,Female,27,137000,1\n15573452,Female,21,16000,0\n15776733,Female,28,44000,0\n15724858,Male,27,90000,0\n15713144,Male,35,27000,0\n15690188,Female,33,28000,0\n15689425,Male,30,49000,0\n15671766,Female,26,72000,0\n15782806,Female,27,31000,0\n15764419,Female,27,17000,0\n15591915,Female,33,51000,0\n15772798,Male,35,108000,0\n15792008,Male,30,15000,0\n15715541,Female,28,84000,0\n15639277,Male,23,20000,0\n15798850,Male,25,79000,0\n15776348,Female,27,54000,0\n15727696,Male,30,135000,1\n15793813,Female,31,89000,0\n15694395,Female,24,32000,0\n15764195,Female,18,44000,0\n15744919,Female,29,83000,0\n15671655,Female,35,23000,0\n15654901,Female,27,58000,0\n15649136,Female,24,55000,0\n15775562,Female,23,48000,0\n15807481,Male,28,79000,0\n15642885,Male,22,18000,0\n15789109,Female,32,117000,0\n15814004,Male,27,20000,0\n15673619,Male,25,87000,0\n15595135,Female,23,66000,0\n15583681,Male,32,120000,1\n15605000,Female,59,83000,0\n15718071,Male,24,58000,0\n15679760,Male,24,19000,0\n15654574,Female,23,82000,0\n15577178,Female,22,63000,0\n15595324,Female,31,68000,0\n15756932,Male,25,80000,0\n15726358,Female,24,27000,0\n15595228,Female,20,23000,0\n15782530,Female,33,113000,0\n15592877,Male,32,18000,0\n15651983,Male,34,112000,1\n15746737,Male,18,52000,0\n15774179,Female,22,27000,0\n15667265,Female,28,87000,0\n15655123,Female,26,17000,0\n15595917,Male,30,80000,0\n15668385,Male,39,42000,0\n15709476,Male,20,49000,0\n15711218,Male,35,88000,0\n15798659,Female,30,62000,0\n15663939,Female,31,118000,1\n15694946,Male,24,55000,0\n15631912,Female,28,85000,0\n15768816,Male,26,81000,0\n15682268,Male,35,50000,0\n15684801,Male,22,81000,0\n15636428,Female,30,116000,0\n15809823,Male,26,15000,0\n15699284,Female,29,28000,0\n15786993,Female,29,83000,0\n15709441,Female,35,44000,0\n15710257,Female,35,25000,0\n15582492,Male,28,123000,1\n15575694,Male,35,73000,0\n15756820,Female,28,37000,0\n15766289,Male,27,88000,0\n15593014,Male,28,59000,0\n15584545,Female,32,86000,0\n15675949,Female,33,149000,1\n15672091,Female,19,21000,0\n15801658,Male,21,72000,0\n15706185,Female,26,35000,0\n15789863,Male,27,89000,0\n15720943,Male,26,86000,0\n15697997,Female,38,80000,0\n15665416,Female,39,71000,0\n15660200,Female,37,71000,0\n15619653,Male,38,61000,0\n15773447,Male,37,55000,0\n15739160,Male,42,80000,0\n15689237,Male,40,57000,0\n15679297,Male,35,75000,0\n15591433,Male,36,52000,0\n15642725,Male,40,59000,0\n15701962,Male,41,59000,0\n15811613,Female,36,75000,0\n15741049,Male,37,72000,0\n15724423,Female,40,75000,0\n15574305,Male,35,53000,0\n15678168,Female,41,51000,0\n15697020,Female,39,61000,0\n15610801,Male,42,65000,0\n15745232,Male,26,32000,0\n15722758,Male,30,17000,0\n15792102,Female,26,84000,0\n15675185,Male,31,58000,0\n15801247,Male,33,31000,0\n15725660,Male,30,87000,0\n15638963,Female,21,68000,0\n15800061,Female,28,55000,0\n15578006,Male,23,63000,0\n15668504,Female,20,82000,0\n15687491,Male,30,107000,1\n15610403,Female,28,59000,0\n15741094,Male,19,25000,0\n15807909,Male,19,85000,0\n15666141,Female,18,68000,0\n15617134,Male,35,59000,0\n15783029,Male,30,89000,0\n15622833,Female,34,25000,0\n15746422,Female,24,89000,0\n15750839,Female,27,96000,1\n15749130,Female,41,30000,0\n15779862,Male,29,61000,0\n15767871,Male,20,74000,0\n15679651,Female,26,15000,0\n15576219,Male,41,45000,0\n15699247,Male,31,76000,0\n15619087,Female,36,50000,0\n15605327,Male,40,47000,0\n15610140,Female,31,15000,0\n15791174,Male,46,59000,0\n15602373,Male,29,75000,0\n15762605,Male,26,30000,0\n15598840,Female,32,135000,1\n15744279,Male,32,100000,1\n15670619,Male,25,90000,0\n15599533,Female,37,33000,0\n15757837,Male,35,38000,0\n15697574,Female,33,69000,0\n15578738,Female,18,86000,0\n15762228,Female,22,55000,0\n15614827,Female,35,71000,0\n15789815,Male,29,148000,1\n15579781,Female,29,47000,0\n15587013,Male,21,88000,0\n15570932,Male,34,115000,0\n15794661,Female,26,118000,0\n15581654,Female,34,43000,0\n15644296,Female,34,72000,0\n15614420,Female,23,28000,0\n15609653,Female,35,47000,0\n15594577,Male,25,22000,0\n15584114,Male,24,23000,0\n15673367,Female,31,34000,0\n15685576,Male,26,16000,0\n15774727,Female,31,71000,0\n15694288,Female,32,117000,1\n15603319,Male,33,43000,0\n15759066,Female,33,60000,0\n15814816,Male,31,66000,0\n15724402,Female,20,82000,0\n15571059,Female,33,41000,0\n15674206,Male,35,72000,0\n15715160,Male,28,32000,0\n15730448,Male,24,84000,0\n15662067,Female,19,26000,0\n15779581,Male,29,43000,0\n15662901,Male,19,70000,0\n15689751,Male,28,89000,0\n15667742,Male,34,43000,0\n15738448,Female,30,79000,0\n15680243,Female,20,36000,0\n15745083,Male,26,80000,0\n15708228,Male,35,22000,0\n15628523,Male,35,39000,0\n15708196,Male,49,74000,0\n15735549,Female,39,134000,1\n15809347,Female,41,71000,0\n15660866,Female,58,101000,1\n15766609,Female,47,47000,0\n15654230,Female,55,130000,1\n15794566,Female,52,114000,0\n15800890,Female,40,142000,1\n15697424,Female,46,22000,0\n15724536,Female,48,96000,1\n15735878,Male,52,150000,1\n15707596,Female,59,42000,0\n15657163,Male,35,58000,0\n15622478,Male,47,43000,0\n15779529,Female,60,108000,1\n15636023,Male,49,65000,0\n15582066,Male,40,78000,0\n15666675,Female,46,96000,0\n15732987,Male,59,143000,1\n15789432,Female,41,80000,0\n15663161,Male,35,91000,1\n15694879,Male,37,144000,1\n15593715,Male,60,102000,1\n15575002,Female,35,60000,0\n15622171,Male,37,53000,0\n15795224,Female,36,126000,1\n15685346,Male,56,133000,1\n15691808,Female,40,72000,0\n15721007,Female,42,80000,1\n15794253,Female,35,147000,1\n15694453,Male,39,42000,0\n15813113,Male,40,107000,1\n15614187,Male,49,86000,1\n15619407,Female,38,112000,0\n15646227,Male,46,79000,1\n15660541,Male,40,57000,0\n15753874,Female,37,80000,0\n15617877,Female,46,82000,0\n15772073,Female,53,143000,1\n15701537,Male,42,149000,1\n15736228,Male,38,59000,0\n15780572,Female,50,88000,1\n15769596,Female,56,104000,1\n15586996,Female,41,72000,0\n15722061,Female,51,146000,1\n15638003,Female,35,50000,0\n15775590,Female,57,122000,1\n15730688,Male,41,52000,0\n15753102,Female,35,97000,1\n15810075,Female,44,39000,0\n15723373,Male,37,52000,0\n15795298,Female,48,134000,1\n15584320,Female,37,146000,1\n15724161,Female,50,44000,0\n15750056,Female,52,90000,1\n15609637,Female,41,72000,0\n15794493,Male,40,57000,0\n15569641,Female,58,95000,1\n15815236,Female,45,131000,1\n15811177,Female,35,77000,0\n15680587,Male,36,144000,1\n15672821,Female,55,125000,1\n15767681,Female,35,72000,0\n15600379,Male,48,90000,1\n15801336,Female,42,108000,1\n15721592,Male,40,75000,0\n15581282,Male,37,74000,0\n15746203,Female,47,144000,1\n15583137,Male,40,61000,0\n15680752,Female,43,133000,0\n15688172,Female,59,76000,1\n15791373,Male,60,42000,1\n15589449,Male,39,106000,1\n15692819,Female,57,26000,1\n15727467,Male,57,74000,1\n15734312,Male,38,71000,0\n15764604,Male,49,88000,1\n15613014,Female,52,38000,1\n15759684,Female,50,36000,1\n15609669,Female,59,88000,1\n15685536,Male,35,61000,0\n15750447,Male,37,70000,1\n15663249,Female,52,21000,1\n15638646,Male,48,141000,0\n15734161,Female,37,93000,1\n15631070,Female,37,62000,0\n15761950,Female,48,138000,1\n15649668,Male,41,79000,0\n15713912,Female,37,78000,1\n15586757,Male,39,134000,1\n15596522,Male,49,89000,1\n15625395,Male,55,39000,1\n15760570,Male,37,77000,0\n15566689,Female,35,57000,0\n15725794,Female,36,63000,0\n15673539,Male,42,73000,1\n15705298,Female,43,112000,1\n15675791,Male,45,79000,0\n15747043,Male,46,117000,1\n15736397,Female,58,38000,1\n15678201,Male,48,74000,1\n15720745,Female,37,137000,1\n15637593,Male,37,79000,1\n15598070,Female,40,60000,0\n15787550,Male,42,54000,0\n15603942,Female,51,134000,0\n15733973,Female,47,113000,1\n15596761,Male,36,125000,1\n15652400,Female,38,50000,0\n15717893,Female,42,70000,0\n15622585,Male,39,96000,1\n15733964,Female,38,50000,0\n15753861,Female,49,141000,1\n15747097,Female,39,79000,0\n15594762,Female,39,75000,1\n15667417,Female,54,104000,1\n15684861,Male,35,55000,0\n15742204,Male,45,32000,1\n15623502,Male,36,60000,0\n15774872,Female,52,138000,1\n15611191,Female,53,82000,1\n15674331,Male,41,52000,0\n15619465,Female,48,30000,1\n15575247,Female,48,131000,1\n15695679,Female,41,60000,0\n15713463,Male,41,72000,0\n15785170,Female,42,75000,0\n15796351,Male,36,118000,1\n15639576,Female,47,107000,1\n15693264,Male,38,51000,0\n15589715,Female,48,119000,1\n15769902,Male,42,65000,0\n15587177,Male,40,65000,0\n15814553,Male,57,60000,1\n15601550,Female,36,54000,0\n15664907,Male,58,144000,1\n15612465,Male,35,79000,0\n15810800,Female,38,55000,0\n15665760,Male,39,122000,1\n15588080,Female,53,104000,1\n15776844,Male,35,75000,0\n15717560,Female,38,65000,0\n15629739,Female,47,51000,1\n15729908,Male,47,105000,1\n15716781,Female,41,63000,0\n15646936,Male,53,72000,1\n15768151,Female,54,108000,1\n15579212,Male,39,77000,0\n15721835,Male,38,61000,0\n15800515,Female,38,113000,1\n15591279,Male,37,75000,0\n15587419,Female,42,90000,1\n15750335,Female,37,57000,0\n15699619,Male,36,99000,1\n15606472,Male,60,34000,1\n15778368,Male,54,70000,1\n15671387,Female,41,72000,0\n15573926,Male,40,71000,1\n15709183,Male,42,54000,0\n15577514,Male,43,129000,1\n15778830,Female,53,34000,1\n15768072,Female,47,50000,1\n15768293,Female,42,79000,0\n15654456,Male,42,104000,1\n15807525,Female,59,29000,1\n15574372,Female,58,47000,1\n15671249,Male,46,88000,1\n15779744,Male,38,71000,0\n15624755,Female,54,26000,1\n15611430,Female,60,46000,1\n15774744,Male,60,83000,1\n15629885,Female,39,73000,0\n15708791,Male,59,130000,1\n15793890,Female,37,80000,0\n15646091,Female,46,32000,1\n15596984,Female,46,74000,0\n15800215,Female,42,53000,0\n15577806,Male,41,87000,1\n15749381,Female,58,23000,1\n15683758,Male,42,64000,0\n15670615,Male,48,33000,1\n15715622,Female,44,139000,1\n15707634,Male,49,28000,1\n15806901,Female,57,33000,1\n15775335,Male,56,60000,1\n15724150,Female,49,39000,1\n15627220,Male,39,71000,0\n15672330,Male,47,34000,1\n15668521,Female,48,35000,1\n15807837,Male,48,33000,1\n15592570,Male,47,23000,1\n15748589,Female,45,45000,1\n15635893,Male,60,42000,1\n15757632,Female,39,59000,0\n15691863,Female,46,41000,1\n15706071,Male,51,23000,1\n15654296,Female,50,20000,1\n15755018,Male,36,33000,0\n15594041,Female,49,36000,1\n\r\n------WebKitFormBoundaryg3tgYREfNvps5Jct\r\nContent-Disposition: form-data; name="id"\r\n\r\n1\r\n------WebKitFormBoundaryg3tgYREfNvps5Jct\r\nContent-Disposition: form-data; name="model"\r\n\r\nNaive Bayes\r\n------WebKitFormBoundaryg3tgYREfNvps5Jct--\r\n')

    id,filename,dataset,nullValues,model = filterData(d)
    # obj = Dataset.objects.create(UserId =id,filename=filename,data=dataset,nullValues=nullValues,model =model)

    def test_correct_model_extracted(self):

        ## ensure that the dataset is a Naive Bayes one
        self.assertEquals(self.model,"Naive Bayes")

        ##negative test case
        self.assertNotEquals(self.model,"Linear Regression")

    def test_creating_file_wih_tag(self):

        obj = Dataset.objects.create(UserId =self.id,filename=self.filename,data=self.dataset,nullValues=self.nullValues,model = self.model)
        ## check if uploaded file has tag Naive Bayes
        queryset = Dataset.objects.get(UserId=self.id,filename=self.filename,model=self.model)

        ##test if tag works in the database
        self.assertEquals(queryset.model,self.model)

        ##negative case
        self.assertNotEquals(queryset.model,"Linear Regression")


    def test_composite_primary_key(self):
        obj1 = Dataset.objects.create(UserId =self.id,filename=self.filename,data=self.dataset,nullValues=self.nullValues,model = self.model)
        obj2 = Dataset.objects.create(UserId =self.id,filename=self.filename,data=self.dataset,nullValues=self.nullValues,model = "Linear Regression")

        NbData = Dataset.objects.get(UserId=self.id,filename=self.filename,model=self.model)
        LRData = Dataset.objects.get(UserId=self.id,filename=self.filename,model="Linear Regression")

        ##datasets are the same just have different tags
        self.assertEquals(NbData.data,LRData.data)

        ##model tags should be different
        self.assertNotEquals(NbData.model,LRData.model)

    def test_NaiveBayes_Training(self):
        results = []
        try:
            results = TrainNaiveBayes(pd.read_json(self.dataset),self.id,self.filename)

        except:
            pass

        ##if it works , results will be populated
        self.assertEquals(len(results),4)

        self.assertNotEquals(len(results),0)


    def test_confusion_matrix(self):

        results = TrainNaiveBayes(pd.read_json(self.dataset),self.id,self.filename)
        ##check that a confusion matrix is being returned
        self.assertEquals(len(results[0]),2)
        ##check that a list of values are returned to populate confusion matrix
        self.assertEquals(type(results[0]),list)

        ##confusion cant be zero
        self.assertNotEquals(len(results[0]),0)

    def test_f1_score(self):

        results = TrainNaiveBayes(pd.read_json(self.dataset),self.id,self.filename)

        f1 = results[1]

        ##check that it is not empty
        self.assertEquals(len(f1),2)

        self.assertNotEquals(len(f1),0)


    def test_f1_classes(self):
        results = TrainNaiveBayes(pd.read_json(self.dataset),self.id,self.filename)

        f1 = results[1]

        ##check that each class has a value
        self.assertEquals(f1[0]['class'],'Purchased = 0')
        self.assertEquals(f1[1]['class'],'Purchased = 1')

        self.assertNotEquals(f1[0]['class'],'')


    def test_f1_values(self):
        results = TrainNaiveBayes(pd.read_json(self.dataset),self.id,self.filename)

        f1 = results[1]

        ##check that each score has a value
        self.assertAlmostEquals(f1[0]['score'],0.9125475285171102)
        self.assertAlmostEquals(f1[1]['score'],0.8321167883211678)

        ##values cannot be negative
        self.assertNotEquals(f1[0]['score'],-1)
        self.assertNotEquals(f1[1]['score'],-1)


    def test_auc_is_returned(self):
        results = TrainNaiveBayes(pd.read_json(self.dataset),self.id,self.filename)

        auc = results[2]

         ##check that it is not empty
        self.assertEquals(len(auc),2)

        self.assertNotEquals(len(auc),0)


    def test_auc_classes(self):

        results = TrainNaiveBayes(pd.read_json(self.dataset),self.id,self.filename)

        auc = results[2]

        ##check that each class has a value
        self.assertEquals(auc[0]['class'],'Purchased = 0')
        self.assertEquals(auc[1]['class'],'Purchased = 1')

        self.assertNotEquals(auc[0]['class'],'')

    def test_auc_scores(self):
        results = TrainNaiveBayes(pd.read_json(self.dataset),self.id,self.filename)

        auc = results[2]
        ##check that each score has a value
        self.assertAlmostEquals(auc[0]['value'],0.9520285162308509)
        self.assertAlmostEquals(auc[1]['value'],0.9520285162308508)

        ##values cannot be negative
        self.assertNotEquals(auc[0]['value'],-1)
        self.assertNotEquals(auc[1]['value'],-1)


    def test_ROC(self):
        results = TrainNaiveBayes(pd.read_json(self.dataset),self.id,self.filename)

        roc = results[3]

        ##check that tpr and fpr are in the result
        self.assertEquals(len(roc),2)
        ##shouldn't be empty
        self.assertNotEquals(len(roc),0)


    def test_roc_values(self):
        results = TrainNaiveBayes(pd.read_json(self.dataset),self.id,self.filename)

        roc = results[3]

        ##check that correct number of items being returned
        self.assertEquals(len(roc[0]),3)
        ##shouldn't be empty
        self.assertNotEquals(len(roc[0]),0)


    def test_upload_to_db(self):

        results = TrainNaiveBayes(pd.read_json(self.dataset),self.id,self.filename)
        ac = 0.99
        result = False
        try:
            NBTrainedModel.objects.create(UserId=self.id,filename=self.filename,TrainingAccuracy=ac,f1score=results[1],AUCScore=results[2])
            result = True
        except:
            self.assertEquals(result, False)
            

        ## if it works then the result is changed
        self.assertEquals(result, True)
