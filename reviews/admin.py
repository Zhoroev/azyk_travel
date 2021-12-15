from django.contrib import admin
from .models import Review


# class ReviewAdmin(admin.ModelAdmin):
#     fieldsets = (
#         (None, {'fields': ('body', 'author', )}),
#     )
#     readonly_fields = ('author',)
#
#
admin.site.register(Review)