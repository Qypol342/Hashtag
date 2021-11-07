from flask import Flask, jsonify

import requests 
import json
import chardet
import unidecode

def get_lib():
    result = requests.get( 
              "https://raw.githubusercontent.com/Qypol342/Hashtag/e0f690fa08e330e526ffe29f8f8112c54207e8f4/hashtag_list.json",

             
    ) 
    rep  =result.text
   
    #rep = rep.encode('utf-8')
    


    rep2 = json.loads(rep)
    return rep2




#https://raw.githubusercontent.com/Qypol342/Hashtag/main/hashtag_list.json


app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route('/hashtag')
def hashtag_():
    
    res = {'error':'please add text exemple /hashtag/hello'}
    return jsonify(res)

@app.route('/hashtag/<text>')
def hashtag(text=''):
    

    allow = [',','.',' ','!','?',"'",'"',":",";"]
    #text = text.encode('ascii').decode('uft-8')
    try:   
        lib = get_lib()
    except Exception as e:
        print("could not reatch git:",e)
        f = open('hashtag_list.json')
        lib = json.load(f)
    
    for i, v in lib.items():
        text_low = unidecode.unidecode(text).lower()
        print(text_low,)
        
        if i in text_low :

            
            if text_low.index(i) == 0 or text[text_low.index(i)-1] != '#':
                
                if text_low.index(i)+len(i)+1< len(text):
                    
                    if text[text_low.index(i)+len(i)] in allow:
                        inn = text_low.index(i)
                        text = text[:inn] + lib[i] + text[inn + len(i):]


                else:
                    
                    inn = text_low.index(i)
                    
                    text = text[:inn] + lib[i] + text[inn + len(i):]
    print('here',type(text),text)
    
    
    test = bytes(text,'UTF-8')

    res = {'hashtaged':text}
  
    return jsonify(res)






if __name__ == '__main__':
 
    try:

        app.run()

    except Exception as e:
        print("SERIOUS API ERROR",e)

