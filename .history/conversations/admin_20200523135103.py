from django.contrib import admin
from . import models


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    """ Message Admin Definition """

    list_display = ("__str__", "created")


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):

    """ Conversation Admin Definition """

    list_display = ("__str__", "count_messages", "count_participants")


[
    {"id": "0", "name": "고든세터", "img": "img0"},
    {"id": "0", "name": "골든리트리버", "img": "img1"},
    {"id": "0", "name": "그레이트피레니즈", "img": "img2"},
    {"id": "0", "name": "그레이하운드", "img": "img3"},
    {"id": "0", "name": "뉴펀들랜드", "img": "img4"},
    {"id": "0", "name": "닥스훈트", "img": "img5"},
    {"id": "0", "name": "달마시안", "img": "img6"},
    {"id": "0", "name": "도베르만핀셔", "img": "img7"},
    {"id": "0", "name": "도사견", "img": "img8"},
    {"id": "0", "name": "래브라도리트리버", "img": "img9"},
    {"id": "0", "name": "로디지안리지백", "img": "img10"},
    {"id": "0", "name": "로트와일러", "img": "img11"},
    {"id": "0", "name": "르웰린", "img": "img12"},
    {"id": "0", "name": "말리노이즈", "img": "img13"},
    {"id": "0", "name": "말티즈", "img": "img14"},
    {"id": "0", "name": "말티즈", "img": "img15"},
    {"id": "0", "name": "멕시칸헤어리스-도그", "img": "img16"},
    {"id": "0", "name": "무디", "img": "img17"},
    {"id": "0", "name": "미니핀", "img": "img18"},
    {"id": "0", "name": "바셋하운드", "img": "img19"},
    {"id": "0", "name": "베들링턴테리어", "img": "img20"},
    {"id": "0", "name": "벨기에테뷰런", "img": "img21"},
    {"id": "0", "name": "벨지안셰퍼드그로넨달", "img": "img22"},
    {"id": "0", "name": "보르조이", "img": "img23"},
    {"id": "0", "name": "복서", "img": "img24"},
    {"id": "0", "name": "불독", "img": "img25"},
    {"id": "0", "name": "불테리어", "img": "img26"},
    {"id": "0", "name": "블러드하운드", "img": "img27"},
    {"id": "0", "name": "비숑프리제", "img": "img28"},
    {"id": "0", "name": "비즐라", "img": "img29"},
    {"id": "0", "name": "빠삐용", "img": "img30"},
    {"id": "0", "name": "사모예드견", "img": "img31"},
    {"id": "0", "name": "살루키", "img": "img32"},
    {"id": "0", "name": "삽살개", "img": "img33"},
    {"id": "0", "name": "샤페이", "img": "img34"},
    {"id": "0", "name": "서식스스패니얼", "img": "img35"},
    {"id": "0", "name": "세인트버나드", "img": "img36"},
    {"id": "0", "name": "슈나우저", "img": "img37"},
    {"id": "0", "name": "스무스폭스테리어", "img": "img38"},
    {"id": "0", "name": "스태퍼드셔불테리어", "img": "img39"},
    {"id": "0", "name": "스테비훈", "img": "img40"},
    {"id": "0", "name": "스페니쉬마스티프", "img": "img41"},
    {"id": "0", "name": "스피노네이탈리아노", "img": "img42"},
    {"id": "0", "name": "슬루기", "img": "img43"},
    {"id": "0", "name": "시르네코델레트나", "img": "img44"},
    {"id": "0", "name": "시베리안허스키", "img": "img45"},
    {"id": "0", "name": "시츄", "img": "img46"},
    {"id": "0", "name": "아메리칸스태퍼드셔테리어", "img": "img47"},
    {"id": "0", "name": "아메리칸코커스파니엘", "img": "img48"},
    {"id": "0", "name": "아이리시세터", "img": "img49"},
    {"id": "0", "name": "아이리시워터스패니얼", "img": "img50"},
    {"id": "0", "name": "아자와크", "img": "img51"},
    {"id": "0", "name": "아키타", "img": "img52"},
    {"id": "0", "name": "아펜핀셔", "img": "img53"},
    {"id": "0", "name": "아프간하운드", "img": "img54"},
    {"id": "0", "name": "알래스칸맬러뮤트", "img": "img55"},
    {"id": "0", "name": "에어데일테리어", "img": "img56"},
    {"id": "0", "name": "에이디", "img": "img57"},
    {"id": "0", "name": "오스트레일리언셰퍼드", "img": "img58"},
    {"id": "0", "name": "올드잉글리시쉽독", "img": "img59"},
    {"id": "0", "name": "와이머라너", "img": "img60"},
    {"id": "0", "name": "요크셔테리어", "img": "img61"},
    {"id": "0", "name": "웰시코기", "img": "img62"},
    {"id": "0", "name": "유라시아", "img": "img63"},
    {"id": "0", "name": "잉글리시폭스하운드", "img": "img64"},
    {"id": "0", "name": "자이언트슈나우저", "img": "img65"},
    {"id": "0", "name": "저먼셰퍼드", "img": "img66"},
    {"id": "0", "name": "저먼쇼트헤어드포인터", "img": "img67"},
    {"id": "0", "name": "저먼와이어헤어드포인터", "img": "img68"},
    {"id": "0", "name": "진돗개", "img": "img69"},
    {"id": "0", "name": "차우차우", "img": "img70"},
    {"id": "0", "name": "차이니스크레스티드", "img": "img71"},
    {"id": "0", "name": "체서피크베이리트리버", "img": "img72"},
    {"id": "0", "name": "체코슬로바키아늑대개", "img": "img73"},
    {"id": "0", "name": "치와와", "img": "img74"},
    {"id": "0", "name": "카이켄", "img": "img75"},
    {"id": "0", "name": "컬리코티드리트리버", "img": "img76"},
    {"id": "0", "name": "코몬돌", "img": "img77"},
    {"id": "0", "name": "코카스파니엘", "img": "img78"},
    {"id": "0", "name": "콜리", "img": "img79"},
    {"id": "0", "name": "토른쟈크", "img": "img80"},
    {"id": "0", "name": "티베탄테리어", "img": "img81"},
    {"id": "0", "name": "퍼그", "img": "img82"},
    {"id": "0", "name": "페키니즈", "img": "img83"},
    {"id": "0", "name": "포메라니안", "img": "img84"},
    {"id": "0", "name": "풍산개", "img": "img85"},
    {"id": "0", "name": "프렌치불독", "img": "img86"},
    {"id": "0", "name": "핀란드사미개", "img": "img87"},
    {"id": "0", "name": "화이트테리어", "img": "img88"},
    {"id": "0", "name": "휘핏", "img": "img89"},
]

{
    "list": [
        {"id": "0", "name": "알래스칸맬러뮤트", "img": "img55"},
        {"id": "0", "name": "바셋하운드", "img": "img19"},
        {"id": "0", "name": "스태퍼드셔불테리어", "img": "img39"},
        {"id": "0", "name": "차이니스크레스티드", "img": "img71"},
        {"id": "0", "name": "고든세터", "img": "img0"},
        {"id": "0", "name": "프렌치불독", "img": "img86"},
        {"id": "0", "name": "보르조이", "img": "img23"},
        {"id": "0", "name": "말티즈", "img": "img14"},
        {"id": "0", "name": "복서", "img": "img24"},
        {"id": "0", "name": "스무스폭스테리어", "img": "img38"},
        {"id": "0", "name": "비즐라", "img": "img29"},
        {"id": "0", "name": "닥스훈트", "img": "img5"},
        {"id": "0", "name": "빠삐용", "img": "img30"},
        {"id": "0", "name": "미니핀", "img": "img18"},
        {"id": "0", "name": "달마시안", "img": "img6"},
        {"id": "0", "name": "도베르만핀셔", "img": "img7"},
        {"id": "0", "name": "삽살개", "img": "img33"},
        {"id": "0", "name": "유라시아", "img": "img63"},
        {"id": "0", "name": "슈나우저", "img": "img37"},
        {"id": "0", "name": "올드잉글리시쉽독", "img": "img59"},
        {"id": "0", "name": "멕시칸헤어리스-도그", "img": "img16"},
        {"id": "0", "name": "골든리트리버", "img": "img1"},
        {"id": "0", "name": "슬루기", "img": "img43"},
        {"id": "0", "name": "와이머라너", "img": "img60"},
        {"id": "0", "name": "베들링턴테리어", "img": "img20"},
        {"id": "0", "name": "아자와크", "img": "img51"},
        {"id": "0", "name": "시츄", "img": "img46"},
        {"id": "0", "name": "잉글리시폭스하운드", "img": "img64"},
        {"id": "0", "name": "그레이하운드", "img": "img3"},
        {"id": "0", "name": "포메라니안", "img": "img84"},
        {"id": "0", "name": "저먼셰퍼드", "img": "img66"},
        {"id": "0", "name": "로디지안리지백", "img": "img10"},
        {"id": "0", "name": "서식스스패니얼", "img": "img35"},
        {"id": "0", "name": "콜리", "img": "img79"},
        {"id": "0", "name": "저먼와이어헤어드포인터", "img": "img68"},
        {"id": "0", "name": "시베리안허스키", "img": "img45"},
        {"id": "0", "name": "살루키", "img": "img32"},
        {"id": "0", "name": "샤페이", "img": "img34"},
        {"id": "0", "name": "아프간하운드", "img": "img54"},
        {"id": "0", "name": "스피노네이탈리아노", "img": "img42"},
        {"id": "0", "name": "벨지안셰퍼드그로넨달", "img": "img22"},
        {"id": "0", "name": "오스트레일리언셰퍼드", "img": "img58"},
        {"id": "0", "name": "블러드하운드", "img": "img27"},
        {"id": "0", "name": "에어데일테리어", "img": "img56"},
        {"id": "0", "name": "웰시코기", "img": "img62"},
        {"id": "0", "name": "불독", "img": "img25"},
        {"id": "0", "name": "뉴펀들랜드", "img": "img4"},
        {"id": "0", "name": "체코슬로바키아늑대개", "img": "img73"},
        {"id": "0", "name": "아이리시세터", "img": "img49"},
        {"id": "0", "name": "페키니즈", "img": "img83"},
        {"id": "0", "name": "차우차우", "img": "img70"},
        {"id": "0", "name": "치와와", "img": "img74"},
        {"id": "0", "name": "사모예드견", "img": "img31"},
        {"id": "0", "name": "아메리칸코커스파니엘", "img": "img48"},
        {"id": "0", "name": "세인트버나드", "img": "img36"},
        {"id": "0", "name": "자이언트슈나우저", "img": "img65"},
        {"id": "0", "name": "아펜핀셔", "img": "img53"},
        {"id": "0", "name": "요크셔테리어", "img": "img61"},
        {"id": "0", "name": "무디", "img": "img17"},
        {"id": "0", "name": "래브라도리트리버", "img": "img9"},
        {"id": "0", "name": "에이디", "img": "img57"},
        {"id": "0", "name": "코몬돌", "img": "img77"},
        {"id": "0", "name": "토른쟈크", "img": "img80"},
        {"id": "0", "name": "아키타", "img": "img52"},
        {"id": "0", "name": "로트와일러", "img": "img11"},
        {"id": "0", "name": "불테리어", "img": "img26"},
        {"id": "0", "name": "카이켄", "img": "img75"},
        {"id": "0", "name": "아이리시워터스패니얼", "img": "img50"},
        {"id": "0", "name": "진돗개", "img": "img69"},
        {"id": "0", "name": "화이트테리어", "img": "img88"},
        {"id": "0", "name": "퍼그", "img": "img82"},
        {"id": "0", "name": "휘핏", "img": "img89"},
        {"id": "0", "name": "풍산개", "img": "img85"},
        {"id": "0", "name": "체서피크베이리트리버", "img": "img72"},
        {"id": "0", "name": "도사견", "img": "img8"},
        {"id": "0", "name": "저먼쇼트헤어드포인터", "img": "img67"},
        {"id": "0", "name": "르웰린", "img": "img12"},
        {"id": "0", "name": "벨기에테뷰런", "img": "img21"},
        {"id": "0", "name": "컬리코티드리트리버", "img": "img76"},
        {"id": "0", "name": "말리노이즈", "img": "img13"},
        {"id": "0", "name": "코카스파니엘", "img": "img78"},
        {"id": "0", "name": "그레이트피레니즈", "img": "img2"},
        {"id": "0", "name": "말티즈", "img": "img15"},
        {"id": "0", "name": "핀란드사미개", "img": "img87"},
        {"id": "0", "name": "비숑프리제", "img": "img28"},
        {"id": "0", "name": "스테비훈", "img": "img40"},
        {"id": "0", "name": "시르네코델레트나", "img": "img44"},
        {"id": "0", "name": "스페니쉬마스티프", "img": "img41"},
        {"id": "0", "name": "아메리칸스태퍼드셔테리어", "img": "img47"},
        {"id": "0", "name": "티베탄테리어", "img": "img81"},
    ]
}

