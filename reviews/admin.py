from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Review

# Register your models here.


class WordFilter(admin.SimpleListFilter):
    title = "Filter by words!"
    parameter_name = "word"

    # lookups는 항상 튜플 리스트를 반환해야 한다.
    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        WordFilter,
        "rating",
        # Foreign Key 관계로 필터 만들기
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
