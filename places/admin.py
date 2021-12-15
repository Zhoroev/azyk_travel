from django.contrib import admin
from .models import PlacePhoto, Place


class PlacePhotoInline(admin.StackedInline):
    model = PlacePhoto
    extra = 1


class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    inlines = [PlacePhotoInline]
    fieldsets = (
        (None, {'fields': ('type', 'name', 'body', )}),
    )


admin.site.register(Place, PlaceAdmin)
admin.site.register(PlacePhoto)