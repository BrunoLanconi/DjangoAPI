from django.contrib import admin
from freshot.models import Student


class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'ra')
    list_display_links = ('name', 'ra')
    search_fields = ('name',)


admin.site.register(Student, Students)
