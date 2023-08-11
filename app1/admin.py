# from .models import User
from .models import Person
from django.contrib import admin

# # @admin.register(User)
# class Users(admin.ModelAdmin):
#     pass
@admin.register(Person)
class Person(admin.ModelAdmin):
    pass


