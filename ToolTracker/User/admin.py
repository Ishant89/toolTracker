from django.contrib import admin

# Register your models here.
from .models import *

from django.contrib.admin import TabularInline, StackedInline,site
from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin




class FieldsAdmin(admin.ModelAdmin):
    fields = ('name','description','type','env')





class FieldsInline(SuperInlineModelAdmin,TabularInline):
    model = Fields
    extra = 0

class ToolAdmin(SuperModelAdmin):
    fields = ('name','user','file','description','usage')
    inlines = [
        FieldsInline,
    ]

    list_display = ('name','created_at','file')

admin.site.register(Tool,ToolAdmin)
admin.site.register(Fields,FieldsAdmin)
