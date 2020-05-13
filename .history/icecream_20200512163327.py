import random

test = {
    "list": [
        {"id": "0", "name": "거북알", "img": "img1"},
        {"id": "1", "name": "거북이", "img": "img2"},
        {"id": "2", "name": "고드름", "img": "img3"},
        {"id": "3", "name": "구구바", "img": "img4"},
        {"id": "4", "name": "구구콘", "img": "img5"},
    ]
}

mlist = list(test.items())
random.shuffle(mlist)
d = dict(mlist)
print(d)
