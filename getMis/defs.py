import requests
from firebase import firebase


id = 0;
nam = "";
# --params--#
countWalls = 0


# ----------#

def toDataBase(base, images):
    print("Загружаем картинки...")
    names = []
    for q in range(len(images)):
        names.append("image" + str(q))
    im = {}
    for q in range(len(images)):
        im.update({names[q]: images[q]})
    base.put(url="/users/id" + str(id), name="image", data=im)
    print("Все круто. Положили")

def gett(access_token="951704270acfe3ff0c327c8e5976d570acdab3987609f75582284509cdc82b341cccbfb0877b5a36a3e42",
         offset=0,
         ownerid=0,
         nam = "",
         count="100",
         filter="owner",
         version="5.68"):
    print("Получаем инфу о страничке")
    url = "https://api.vk.com/method/wall.get?"
    if(nam == ""):
        print("ЦЫФРЫ")
        url_post = (url +
                    "&access_token=" + access_token +
                    "&count=" + count +
                    "&offset=" + str(offset) +
                    "&count=" + count +
                    "&filter=" + filter +
                    "&v=" + version +
                    "&owner_id=" + str(ownerid))
        print(url_post)
    else:
        print("Да я понял, что это текст")
        url_post = (url +
                    "&access_token=" + access_token +
                    "&count=" + count +
                    "&offset=" + str(offset) +
                    "&count=" + count +
                    "&filter=" + filter +
                    "&v=" + version +
                    "&domain=" + str(nam))
        print(url_post)
    print("Получили, возращаем")
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
                        mx = 0
                        for g in js["response"]["items"][i]["attachments"][r]["photo"]:
                            if g[:5] == "photo":
                                if int(g[6:]) > mx:
                                    mx = int(g[6:])
                        images.append(
                            js["response"]["items"][i]["attachments"][r]["photo"]["photo_" + str(mx)])
                        #print("photo_" + str(mx))
    #print(images)

    return images

