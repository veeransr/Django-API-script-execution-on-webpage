from django.contrib import admin
from .models import Snippet, entervaluesCTS
# Register your models here.

# class SnippetAdmin(admin.ModelAdmin):
#     fileds = ['number1', 'number2', 'number3']
admin.site.register(Snippet) #SnippetAdmin
admin.site.register(entervaluesCTS)