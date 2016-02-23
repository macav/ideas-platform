from api.models import Idea
from django.contrib import admin

class IdeaAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')

admin.site.register(Idea, IdeaAdmin)