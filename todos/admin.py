from django.contrib import admin
from todos.models import Todo, TodoImage

class TodoImageInline(admin.TabularInline):
    model=TodoImage
    fields = ("image",)


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'completed')
    inlines = [TodoImageInline]


@admin.register(TodoImage)
class TodoImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image")

