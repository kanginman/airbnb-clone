import random
import os


path = "C:\Users\kangi\OneDrive\바탕 화면\아이스크림 이미지"
file_list = os.listdir(path)
print ("file_list: {}".format(file_list))

'''
test = {
    "list": [
        {"id": "0", "name": "거북알", "img": "img1"},
        {"id": "1", "name": "거북이", "img": "img2"},
        {"id": "2", "name": "고드름", "img": "img3"},
        {"id": "3", "name": "구구바", "img": "img4"},
        {"id": "4", "name": "구구콘", "img": "img5"},
    ]
}

mlist = test.get("list")
random.shuffle(mlist)

test["list"] = mlist
print(test)
'''