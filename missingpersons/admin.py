from django.contrib import admin
from .models import Missingperson, Comment
class CommentInLine(admin.TabularInline):
    model = Comment
class MissingAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]
    list_display = ('Name','Sex','description','lastseenat')
admin.site.register(Missingperson, MissingAdmin)

