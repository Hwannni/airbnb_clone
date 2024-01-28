from django.contrib import admin
from .models import Review

# Register your models here.

class WordFilter(admin.SimpleListFilter):

    title = "Filter by words!"


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        "rating",
        # Foreign Key 관계로 필터 만들기
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
