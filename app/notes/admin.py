from django.contrib import admin

from .models import User_note, Message

admin.site.register(User_note)
class User_noteAdmin(admin.ModelAdmin):
    list_display = ('id', 'external_id', 'username')

admin.site.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'text', 'created_time')
