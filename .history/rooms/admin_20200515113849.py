from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin Definition """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition """

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About the Space",
            {"classes": ("collapse",), "fields": ("amenity", "facility", "houseRule"),},
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    fieldsets = (
        (
            "Baisc Info",
            {"fields": (("name", "description", "country", "address", "price"))},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About the Space",
            {"classes": ("wide",), "fields": ("amenity", "facility", "houseRule"),},
        ),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "roomType",
        "amenity",
        "facility",
        "houseRule",
        "city",
        "country",
    )

    search_fields = ("=city", "^host__username")
    filter_horizontal = (
        "amenity",
        "facility",
        "houseRule",
    )


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo Admin Definition """

    pass
