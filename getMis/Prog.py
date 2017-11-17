from getMis import defs
import json

from firebase import firebase


htmlMidStart = '''
    <img src="
'''

htmlMidStop = '''
    ">
'''


idk = 0
nam = ""

def StartCheck (idk, nam):
    print("Мы в ВК")
    print("Мы смотрим данные: " + str(idk) + str(nam))
    if (idk == 0) and (len(nam) == 0):
        exit()

    isName = False # Id or Name

    if (idk == 0):
        print("ТЕКСТ")
        com = nam
        isName = True
    else:
        com = idk
    # com - с чем работаем


    ownerID = com
    print("Все пока хорошо...")


    # Смотрим, сколько записей
    if (isName):
        wall = defs.gett(nam=ownerID)
    else:
        wall = defs.gett(ownerid=ownerID)
    print("Фигачим жсон")
    js = json.loads(wall.text)
    c = int(js["response"]["count"])
    offset = 0
    a = []
    print(str(c) + " записей найдено")


    if c >= 100: #Если стена большая, то больше фигвчим
        for i in range(int(c // 100) + 1):
            if (isName):
                wall = defs.gett(offset=offset, nam=ownerID)
            else:
                wall = defs.gett(offset=offset, ownerid=ownerID)
            js = json.loads(wall.text)
            count = len(js["response"]["items"])
            a.append(defs.work_with(js, count))
            offset = offset + 100
    else: #Просто фиачим, когда меньше 100 записей
        if (isName):
            wall = defs.gett(offset=offset, nam=ownerID)
        else:
            wall = defs.gett(offset=offset, ownerid=ownerID)
        js = json.loads(wall.text)
        count = len(js["response"]["items"])
        a.append(defs.work_with(js, count))
    ar = []
    if c >= 100:
        for i in a:
            for j in i:
                ar.append(j)

    print(ar) # Увидеть все ссылки


    heh = ""
    base = firebase.FirebaseApplication("https://vkimages-873b3.firebaseio.com/", None)

    defs.toDataBase(base, ar)
    print("-----------------")
    # print(ar)
    for i in ar:
        heh = heh + htmlMidStart + str(i) + htmlMidStop
    return heh

