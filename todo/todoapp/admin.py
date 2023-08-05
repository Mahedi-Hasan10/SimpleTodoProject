from django.contrib import admin
from todoapp.models import todoModel
# Register your models here.
class adminTodo(admin.ModelAdmin):
    list_display = ('id','todo_title')
admin.site.register(todoModel,adminTodo)