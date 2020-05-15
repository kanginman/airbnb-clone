from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):

    """ Conversation Model Definition """

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        return str(self.created)


class Message(core_models.TimeStampedModel):

    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    conversation = models.ForeignKey("conversation", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} says: {self.message}"

test = {
    "list": [
"Dr구",
"강아율", 
"강우빈", 
"고나래", 
"곽재형", 
"곽준형", 
"구지용", 
"규자욱", 
"김건우", 
"김준호", 
"나르샤그린필드", 
"남동진", 
"남선지", 
"마용규", 
"맥스", 
"박찬영", 
"백설현", 
"송현우", 
"신가희", 
"아람", 
"양양궁", 
"양인희", 
"엠제이", 
"우연", 
"유루미.jpg", 
"윤세아", 
"윤슬", 
"이세빈", 
"이유리", 
"임현지", 
"정동석", 
"정예슬", 
"정태현", 
"조연빈", 
"조예지", 
"주희원", 
"케빈", 
"편준범", 
"표이현", 
"하린", 
"홍산하"
]