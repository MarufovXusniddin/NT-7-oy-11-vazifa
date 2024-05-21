from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Brand, Model, CustomUser, Comment


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    search_fields = ['name', ]


class ModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'name', 'get_photo', 'year', 'mileage', 'price')
    list_display_links = ('name',)
    search_fields = ['name', 'brand']
    list_filter = ('year', 'mileage', 'pub_date')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50px">')
        return '-'

    get_photo.short_description = 'Rasm'


admin.site.register(Brand, BrandAdmin)
admin.site.register(Model, ModelAdmin)
admin.site.register(CustomUser)
admin.site.register(Comment)