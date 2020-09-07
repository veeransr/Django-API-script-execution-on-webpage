from django.contrib import admin
from .models import Snippet, entervaluesAOFT1
# Register your models here.

# class SnippetAdmin(admin.ModelAdmin):
#     fileds = ['number1', 'number2', 'number3']
admin.site.register(Snippet)
admin.site.register(entervaluesAOFT1)#SnippetAdmin