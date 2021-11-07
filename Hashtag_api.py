from flask import Flask, jsonify

import requests 
import json
import chardet

def get_lib():
    result = requests.get( 
              "https://raw.githubusercontent.com/Qypol342/Hashtag/main/hashtag_list.json", 
             
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
    #text = text.encode('ascii').decode('uft-8')
    lib = get_lib()
    for i, v in lib.items():
        if i in text:
            if text.index(i)>1 and text[text.index(i)-1] != '#':
                inn = text.index(i)
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

