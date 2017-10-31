from django.contrib import admin

from .models import SuggestionBox, Suggestion, Comment, Vote


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class VoteInline(admin.StackedInline):
    model = Vote
    extra = 0


class SuggestionBoxAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "date_created"]
    list_filter = ["date_created"]
    search_fields = ["name", "description"]


class SuggestionAdmin(admin.ModelAdmin):
    inlines = [CommentInline, VoteInline]
    list_display = ["name", "description", "date_created"]
    list_filter = ["date_created"]
    search_fields = ["name", "description"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ["text", "date_created"]
    list_filter = ["date_created"]
    search_fields = ["text"]


admin.site.register(SuggestionBox, SuggestionBoxAdmin)
admin.site.register(Suggestion, SuggestionAdmin)
admin.site.register(Comment, CommentAdmin)
