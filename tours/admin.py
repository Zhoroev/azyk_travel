from django.contrib import admin
from .models import Tour, Category, TourPhoto, Program, Accommodation, DatePrice, Question
from reviews.models import Review
from django.utils.html import format_html


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


class DatePriceInline(admin.StackedInline):
    model = DatePrice
    extra = 1


class AccommodationInline(admin.StackedInline):
    model = Accommodation
    extra = 1


class TourPhotoInline(admin.StackedInline):
    model = TourPhoto
    extra = 1

    def get_image(self, obj):
        try:
            return format_html(f'<img src="{obj.image.url}" />')
        except:
            return "Нет изображения"

    get_image.short_description = "Изображение"
    readonly_fields = ['get_image',]



class ProgramInline(admin.StackedInline):
    model = Program
    extra = 1


class ReviewInline(admin.StackedInline):
    model = Review
    extra = 1
    readonly_fields = ('author', 'tour', )


class TourAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'day', 'count_review', 'draft', 'is_top', ]
    list_filter = ['category', 'draft', 'is_top',]
    # search_fields = ['name', ]
    list_editable = ('draft',)
    inlines = [TourPhotoInline, ProgramInline, ReviewInline, AccommodationInline, DatePriceInline, QuestionInline]
    fieldsets = (
        (None, {'fields': ('name', 'category', 'body', 'body_list', 'included', 'excluded',
                           'draft', 'is_top', 'image', 'day', 'count_review', )}),
    )
    readonly_fields = ['day', 'count_review']


admin.site.register(Tour, TourAdmin)
admin.site.register(Accommodation)
admin.site.register(Category)
admin.site.register(TourPhoto)
admin.site.register(Program)
admin.site.register(DatePrice)
admin.site.register(Question)