from django.contrib import admin
from .models import Contact
from django.contrib.auth.models import Group

class ContacAdmin(admin.ModelAdmin):
    list_display = ('id','name','gender','email', 'info','phone')
    list_display_links = ('id', 'name')
    list_editable = ('info',)
    list_per_page = 8
    search_fields = ('name','gender','email', 'info','phone')
    list_filter = ('gender','date_added')

# Register your models here.
admin.site.register(Contact, ContacAdmin)
admin.site.unregister(Group)