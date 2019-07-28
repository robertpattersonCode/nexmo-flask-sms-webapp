#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template, flash, Response


from werkzeug import secure_filename
import nexmo
import time
import json
import datetime
import os
import sys


# from .utils.after_this_response import AfterThisResponse



UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'csv', 'png', 'jpg', 'jpeg', 'gif'])

def sms(filename):

    print(" ()()()()()" + filename)

    numFile = "uploads/" + filename 
    
    with open(numFile) as input_file:
        lines=input_file.readlines()
        message =lines[0].rstrip()
        fromNum =lines[1].rstrip()




    print("   FILE : " + numFile)
    print("MESSAGE : " + message)
    print("""

    """)
    
    snt = 0
    now = datetime.datetime.now()
    client = nexmo.Client(key='84ed6852', secret='JibCuseSVvI0Hp1F')

    print("starting " + fromNum)
    print(message)
    client.send_message(
        {
                "from": fromNum,
                "to": "12124611779",
                "text": "starting : " + message + " from: " + fromNum + " at: " + now.strftime("%Y-%m-%d %H:%M")
        }
    )
    print("""

    """)
    print("sending Max " + message)
    time.sleep(2)

    client.send_message(
    {
                "from": fromNum,
                "to": "19176885123",
                "text": "starting : " + message + "\n      from: " + fromNum + "\n           at: " + now.strftime("%H:%M  %Y-%m-%d")
        }
    )
    print("sending 19176885123 " + message)
    time.sleep(2)

    client.send_message(
        {
                "from": fromNum,
            "to": "17166660179",
                "text": "starting : " + message + " from: " + fromNum + " at: " + now.strftime("%Y-%m-%d %H:%M")
        }
    )
    print("sending 17166660179 " + message)
    time.sleep(2)
    print("""

    """)


    f = open(numFile, "r")
   
    for x in f:
        time.sleep(1.1)
        snt = snt + 1
        # print( message + '    ' + x)
        if x != message:
           
            responseData = client.send_message(
                {
                    "from": fromNum,
                    "to": x,
                    "text": message

                }
            )
            try:
                resp = {}
                now = datetime.datetime.now()

                resp = responseData['messages'][0]['to']
                resp2 = responseData['messages'][0]['status']
                resp3 = responseData['messages'][0]['network']
                service =  str(snt) + "  " + fromNum + ' -->  ' + resp + ' -- ' + resp2 + ' -- ' + resp3
                print(service)
               
                frmNumber = fromNum
                f = open('dataFile' + frmNumber + now.strftime("%Y-%m-%d")+ '.txt', 'a+')
                f.write(frmNumber + ',' + resp + ',' + resp2 + ',' +
                        resp3 + ',' + now.strftime("%Y-%m-%d %H:%M \n"))

            except:
                print("An exception occurred \n" + x)



    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")

    client.send_message(
        {
                "from": fromNum,
                "to": "19176885123",
                "text": fromNum + " finshed at: " + now.strftime(" %H:%M  %Y-%m-%d")
        }
    )
    print("""

    """)
    print("sending finished : 19176885123  ")
    time.sleep(2)
    client.send_message(
        {
                "from": fromNum,
                "to": "12124611779",
                "text": fromNum + " finshed at : " + now.strftime(" %H:%M  %Y-%m-%d")
        }
    )

    print("sending finished : 12124611779  ")
    time.sleep(2)
    client.send_message(
        {
                "from": fromNum,
                "to": "17166660179",
                "text": fromNum + " finshed at : " + now.strftime(" %H:%M  %Y-%m-%d")
        }
    )
    print("sending finished : 17166660179  ")


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
# def test():
#     def generate():
#         app.logger.info('request started')
#         for i in range(5):
#             time.sleep(1)
#             yield 'cunt!!!'
#         app.logger.info('request finished')
#         yield ''
#     return Response(generate(), mimetype='text/plain')

def upload_file():
    if request.method == 'POST':
         file = request.files['file']
         filename = secure_filename(file.filename)
         print (os.path.join(app.config['UPLOAD_FOLDER'],filename))
         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
         sms(filename)
         return render_template('f.html')
           
            

    return render_template('app.html')



  

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == '__main__':
    app.run(debug=True)                    







