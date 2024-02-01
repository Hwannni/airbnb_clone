from django.urls import path
from . import views

urlpatterns = [
    path("", views.see_all_rooms),
    # 변수를 받을 땐 <> 사용(타입, 파라미터)
    path("<int:room_pk>", views.see_one_room),
]
