import random

test = {
    "list": [
        {"id":"0", "name":"거북알", "img": "img2"}, 
        {"id":"0", "name":"거북이", "img": "img2"}, 
        {"id":"0", "name":"고드름", "img": "img2"}, 
        {"id":"0", "name":"구구바", "img": "img2"}, 
        {"id":"0", "name":"구구콘", "img": "img2"},
        {"id":"0", "name":"구구크러스터", "img": "img2"},
        {"id":"0", "name":"국화빵", "img": "img2"},
        {"id":"0", "name":"그릭요거트바", "img": "img2"},
        {"id":"0", "name":"까페오레", "img": "img2"},
        {"id":"0", "name":"끌레도르", "img": "img2"},
        {"id":"0", "name":"나뚜루", "img": "img2"},
        {"id":"0", "name":"녹차마루", "img": "img2"},
        {"id":"0", "name":"누가바", "img": "img2"}, 
        {"id":"0", "name":"대롱대롱", "img": "img2"}, 
        {"id":"0", "name":"더블비얀코", "img": "img2"}, 
        {"id":"0", "name":"더위사냥", "img": "img2"}, 
        {"id":"0", "name":"델몬트망고", "img": "img2"}, 
        {"id":"0", "name":"돼지바", "img": "img2"},
        {"id":"0", "name":"돼지콘", "img": "img2"}, 
        {"id":"0", "name":"디핀다트", "img": "img2"}, 
        {"id":"0", "name":"리틀텐", "img": "img2"}, 
        {"id":"0", "name":"메가톤바", "img": "img2"}, 
        {"id":"0", "name":"메로나", "img": "img2"}, 
        {"id":"0", "name":"모히또바", "img": "img2"}, 
        {"id":"0", "name":"미니멜츠", "img": "img2"}, 
        {"id":"0", "name":"민트초콜릿칩", "img": "img2"}, 
        {"id":"0", "name":"밀키스바", "img": "img2"}, 
        {"id":"0", "name":"바람과함께사라지다", "img": "img2"}, 
        {"id":"0", "name":"바밤바", "img": "img2"}, 
        {"id":"0", "name":"베리베리스트로베리", "img": "img2"}, 
        {"id":"0", "name":"별난바", "img": "img2"}, 
        {"id":"0", "name":"보석바", "img": "img2"}, 
        {"id":"0", "name":"부라보콘", "img": "img2"}, 
        {"id":"0", "name":"붕어싸만코", "img": "img2"}, 
        {"id":"0", "name":"블루소다", "img": "img2"}, 
        {"id":"0", "name":"비비빅", "img": "img2"}, 
        {"id":"0", "name":"빙빙바", "img": "img2"}, 
        {"id":"0", "name":"빠삐코바", "img": "img2"}, 
        {"id":"0", "name":"빵또아", "img": "img2"}, 
        {"id":"0", "name":"빵빠레", "img": "img2"}, 
        {"id":"0", "name":"뽕따", "img": "img2"}, 
        {"id":"0", "name":"사랑에빠진딸기", "img": "img2"}, 
        {"id":"0", "name":"생귤탱귤", "img": "img2"}, 
        {"id":"0", "name":"설레임", "img": "img2"}, 
        {"id":"0", "name":"수박맛바", "img": "img2"}, 
        {"id":"0", "name":"순수밀크", "img": "img2"}, 
        {"id":"0", "name":"슈팅스타", "img": "img2"},
        {"id":"0", "name":"슈퍼콘", "img": "img2"}, 
        {"id":"0", "name":"스크류바", "img": "img2"}, 
        {"id":"0", "name":"쌍쌍바", "img": "img2"}, 
        {"id":"0", "name":"아맛나", "img": "img2"}, 
        {"id":"0", "name":"아몬드봉봉", "img": "img2"}, 
        {"id":"0", "name":"아차차", "img": "img2"}, 
        {"id":"0", "name":"아포가토", "img": "img2"}, 
        {"id":"0", "name":"알껌바", "img": "img2"}, 
        {"id":"0", "name":"알초코바", "img": "img2"}, 
        {"id":"0", "name":"엄마는외계인", "img": "img2"}, 
        {"id":"0", "name":"엔초", "img": "img2"}, 
        {"id":"0", "name":"옥동자", "img": "img2"}, 
        {"id":"0", "name":"와삭바", "img": "img2"}, 
        {"id":"0", "name":"와일드바디", "img": "img2"}, 
        {"id":"0", "name":"요맘때", "img": "img2"}, 
        {"id":"0", "name":"월드콘", "img": "img2"}, 
        {"id":"0", "name":"위즐", "img": "img2"}, 
        {"id":"0", "name":"이상한나라의솜사탕", "img": "img2"}, 
        {"id":"0", "name":"젤루조아", "img": "img2"}, 
        {"id":"0", "name":"조안나", "img": "img2"}, 
        {"id":"0", "name":"죠스바", "img": "img2"}, 
        {"id":"0", "name":"주물러", "img": "img2"}, 
        {"id":"0", "name":"찰떡시모나", "img": "img2"}, 
        {"id":"0", "name":"찰떡아이스", "img": "img2"}, 
        {"id":"0", "name":"찰옥수수", "img": "img2"}, 
        {"id":"0", "name":"체리마루", "img": "img2"}, 
        {"id":"0", "name":"체리쥬빌레", "img": "img2"}, 
        {"id":"0", "name":"초코나무숲", "img": "img2"}, 
        {"id":"0", "name":"초코퍼지", "img": "img2"}, 
        {"id":"0", "name":"캔디바", "img": "img2"}, 
        {"id":"0", "name":"쿠앤크", "img": "img2"}, 
        {"id":"0", "name":"쿠키오", "img": "img2"}, 
        {"id":"0", "name":"키위아작", "img": "img2"}, 
        {"id":"0", "name":"탱크보이", "img": "img2"}, 
        {"id":"0", "name":"테트리스", "img": "img2"}, 
        {"id":"0", "name":"토마토마", "img": "img2"}, 
        {"id":"0", "name":"투게더", "img": "img2"} 
        {"id":"0", "name":"티라미수", "img": "img2"} 
        {"id":"0", "name":"판타스틱트롤", "img": "img2"} 
        {"id":"0", "name":"팥빙수", "img": "img2"} 
        {"id":"0", "name":"팽이팽이", "img": "img2"} 
        {"id":"0", "name":"폭신폭신솜사탕바", "img": "img2"} 
        {"id":"0", "name":"폴라포", "img": "img2"} 
        {"id":"0", "name":"호두마루", "img": "img2"}        
    ]
}

mlist = test.get("list")
random.shuffle(mlist)

test["list"] = mlist
print(test)

