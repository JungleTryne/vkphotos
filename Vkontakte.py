__author__ = 'mishindanila'

import os
from bottle import post, run, request, route
from getMis import Prog

htmlStart = '''
<html>
    <head>
    </head>
    <body>
'''

htmlEnd = '''

    </body>
</html>
'''

@route("/gett")
def hi():
    getter = request.query
    q = getter["id"]
    print("ID пользователя:" + q)
    if isinstance(q, int):
        int(q)
        print("Это id!")
        Prog.idk = q
        htmlMid = str(Prog.StartCheck(q, ""))
    else:
        Prog.nam = q
        print("Это текст!")
        htmlMid = str(Prog.StartCheck(0, q))

    return (htmlStart +
            htmlMid +
            htmlEnd)

@post("/")
def pos():
    #print(request.json)
    return "0"

run(host="0.0.0.0", port=os.environ.get('PORT', 5000))