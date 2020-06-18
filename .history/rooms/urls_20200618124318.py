from django.urls import path
from . import views


urlpatterns = [path("/1", views.room_detail, name="detail")]
