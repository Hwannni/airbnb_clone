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


class ScoreFilter(admin.SimpleListFilter):
    title = "Filter by Score!"
    parameter_name = "score"

    def lookups(self, request, model_admin):
        return [
            ("bad", "Bad!"),
            ("good", "Good!"),
        ]

    def queryset(self, request, reviews):
        score = self.value()
        if score == "bad":
            # lt -> 해당 값보다 작은 값을 선택
            return reviews.filter(rating__lt=3)
        elif score == "good":
            # gte -> 해당 값보다 크거나 같은 값을 선택
            return reviews.filter(rating__gte=3)
        else:
            return reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        ScoreFilter,
        WordFilter,
        "rating",
        # Foreign Key 관계로 필터 만들기
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
