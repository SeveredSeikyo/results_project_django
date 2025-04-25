from django.contrib import admin
from .models import Branch,Result
# Register your models here.

class ResultAdmin(admin.ModelAdmin):
    list_display=['roll_number','name','percentage','final_result']

admin.site.register(Result,ResultAdmin)
admin.site.register(Branch)