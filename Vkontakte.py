import requests
import json
from firebase import firebase
import urllib.request
import os


#--params--#
countWalls = 0
users = [] #массив экхемпляров
#----------#

class user:
    id = 0
    images = []
    def __init__(self, idd, imagess):
        print(idd)
        self.id = idd
        self.images = imagess
    def toDataBase(self, url):
        names = []
        for q in range(len(self.images)):
            names.append("image"+str(q))
        im = {}
        for q in range(len(self.images)):
            im.update({names[q]:self.images[q]})
        base.post("/users/id"+self.id, {"id":self.id, "images":im})



def gett(access_token="951704270acfe3ff0c327c8e5976d570acdab3987609f75582284509cdc82b341cccbfb0877b5a36a3e42",
         offset=0,
         ownerid=210445124,
         count="100",
         filter="owner",
         version="5.68"):
    url = "https://api.vk.com/method/wall.get?"
    url_post = (url +
                "&access_token=" + access_token +
                "&count=" + count +
                "&offset=" + str(offset) +
                "&count=" + count +
                "&filter=" + filter +
                "&v=" + version +
                "&owner_id=" + ownerid)
    return requests.get(url_post)


def work_with(js, count):
    images = []
    for i in range(count):
        if "copy_history" in js["response"]["items"][i]:
            continue
        else:
            if not "attachments" in js["response"]["items"][i]:
                continue
            else:
                sizeOfAtt = len(js["response"]["items"][i]["attachments"])
                for r in range(sizeOfAtt):
                    if js["response"]["items"][i]["attachments"][r]["type"] != "photo":
                        continue
                    else:
                        for g in js["response"]["items"][i]["attachments"][r]["photo"]:
                            mx = 0
                            if g[:5] == "photo":
                                if int(g[6:]) > mx:
                                    mx = int(g[6:])
                                images.append(js["response"]["items"][i]["attachments"][r]["photo"]["photo_" + str(mx)])

    return images


ids = []
while(True):
    id = input('Вводите id пользователей. Введите 0, когда закончите')
    if(id == "0"):
        break
    ids.append(id)

if(len(ids) == 0):
    exit()

for z in ids:
    ownerID = z

    #print(url_post)
    wall = gett(ownerid=z)
    js = json.loads(wall.text)
    c = int(js["response"]["count"])
    offset = 0
    a = []
    print(str(c) + " записей найдено")

    if c >= 100:
        for i in range(int(c//100)+1):
            wall = gett(offset=offset, ownerid=z)
            js = json.loads(wall.text)
            count = len(js["response"]["items"])
            a.append(work_with(js,count))

    ar = []

    for k in a:
        for b in a:
            ar.append(b)

    try:
        arr = ar[0]
        users.append(user(z,arr))
    except:
        print("Картинки не найдены")
        continue


base = firebase.FirebaseApplication("https://vkimages-873b3.firebaseio.com/",None)
for i in users:
    i.toDataBase("https://vkimages-873b3.firebaseio.com/")

    countI = len(i.images)
    a = []
    for o in range(countI):
        a.append("image"+str(o))

    counter = 0

    for urlOfImage in i.images:
        if not os.path.exists("users"):
            os.makedirs("users")
        urllib.request.urlretrieve(urlOfImage,
                                    str(a[counter])+".png")





