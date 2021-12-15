from django.contrib import admin
from .models import Message, Contact, SocialMedia, Phone


class PhoneInline(admin.StackedInline):
    model = Phone
    extra = 1


class ContactAdmin(admin.ModelAdmin):
    list_display = ['address', ]
    inlines = [PhoneInline]
    fieldsets = (
        (None, {'fields': ('email', 'address', 'address_link', )}),
    )


admin.site.register(Message)
admin.site.register(Contact, ContactAdmin)
admin.site.register(SocialMedia)
admin.site.register(Phone)
