__author__ = 'mishindanila'

import os
from bottle import post, run, request, route
from getMis import Prog

htmlStart = '''
<html>
    <head>
        <style type="text/css">
            body {
              background-color: #FFCC00;
            }
            .center-img {
                display: block;
                margin: 100 auto;
                vertical-align: middle;
                width: 85%;
                text-align:center;
            }
        
        </style>
    </head>
    <body>
    
'''

htmlEnd = '''

    </body>
</html>
'''

divStart = '''
<div class = "center-img">
'''
divEnd = '''
</div>'''

@route("/gett")
def hi():
    getter = request.query
    q = getter["id"]
    try:
        q = int(q)
    except:
        pass
    print("ID пользователя:" + str(q))
    if isinstance(q, int):
        print("Это id!")
        Prog.idk = q
        htmlMid = str(Prog.StartCheck(q, ""))
    else:
        Prog.nam = q
        print("Это текст!")
        htmlMid = str(Prog.StartCheck(0, q))

    return (htmlStart + divStart +
            htmlMid + divEnd +
            htmlEnd)

@post("/")
def pos():
    #print(request.json)
    return "0"

run(host="127.0.0.1", port=os.environ.get('PORT', 5000))