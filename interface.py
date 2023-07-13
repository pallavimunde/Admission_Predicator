from flask import Flask,jsonify,request, render_template
from utils import Admission
import config

app =Flask(__name__)

@app.route('/')
def home():
    #return jsonify({'hello':'home'})
    return render_template('index.html')

@app.route('/prediction', methods=['GET','POST'])
def Admit_chance():

    if request.method == 'POST':
        data = request.form
        print('DATA:',data)

        GRE_Score = data['GRE_Score']
        TOEFL_Score = data['TOEFL_Score']
        University_Rating = data['University_Rating']  
        Sop = data['Sop']
        LOR = data['LOR']
        CGPA = data['CGPA']
        Research = data['Research']

        obj = Admission(GRE_Score, TOEFL_Score, University_Rating,Sop, LOR,CGPA, Research)
        pred = obj.Admit_chance()

        return jsonify({'Your Chances Of Admission is ':f"{pred} %"})
    
    
    elif request.method == 'GET':
        data=request.args.get
        print('DATA:',data)

        GRE_Score = data('GRE_Score')

        TOEFL_Score = data('TOEFL_Score')
        University_Rating = data('University_Rating')
        
        Sop = data('Sop')
        LOR = data('LOR')
        CGPA = data('CGPA')
        Research = data('Research')

        obj = Admission(GRE_Score,TOEFL_Score,University_Rating,Sop,LOR,CGPA,Research)
        P = obj.Admit_chance()

        return render_template('index.html', result = P)
    
    return jsonify({'Neither':'POST & GET'})
    
if __name__=="__main__":              
    app.run(host="0.0.0.0",port=5003,debug=True)

    