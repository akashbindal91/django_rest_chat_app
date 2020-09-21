from django.contrib import admin
from chats.models import Message
# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = ['message', 'sender' , 'receiver', 'timestamp', 'is_read']
    list_editable = ('is_read'),

    def created_on(self , request ):
        return request.timestamp

admin.site.register(Message, MessageAdmin)