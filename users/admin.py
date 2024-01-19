from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

@admin.register(User) # 이 클래스가 user 모델을 관리한다
class CustomUserAdmin(UserAdmin):
    pass