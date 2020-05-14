from django.contrib import admin
from . import models


@admin.register(models.Conversations)
class ConversationsAdmin(admin.ModelAdmin):

    """ Conversations Admin Definition """

    pass
