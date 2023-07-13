import pickle
import numpy as np

import warnings
warnings.filterwarnings('ignore')
import json

class Admission():

    def __init__ (self,GRE_Score,TOEFL_Score,University_Rating,Sop,LOR,CGPA,Research):
        self.GRE_Score=GRE_Score
        self.TOEFL_Score=TOEFL_Score
        self.University_Rating=University_Rating
        self.Sop=Sop
        self.LOR=LOR
        self.CGPA=CGPA
        self.Research=Research
        
    def Load_data(self):
        with open('model.pkl','rb')as f:
            self.model=pickle.load(f)

            
    def Admit_chance(self):
        self.Load_data()
        array = np.zeros([1,7])
        array[0,0]=self.GRE_Score
        array[0,1]=self.TOEFL_Score
        array[0,2]=self.University_Rating
     
        array[0,3]=self.Sop
        array[0,4]=self.LOR
        array[0,5]=self.CGPA
        array[0,6]=self.Research
        print(array)   
        
        Admit_chance= self.model.predict(array)
        AC = Admit_chance.round(2)[0]*100

        return AC
    

     




