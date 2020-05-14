from django.contrib import admin
from . import models


@admin.register(modes.Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """ Reservation Admin Definition """

    pass


# Register your models here.
