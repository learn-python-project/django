from django.contrib import admin
from .models import Member, Functie

class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "phone", "joined_date", "function")

class FunctieAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

admin.site.register(Member, MemberAdmin)
admin.site.register(Functie, FunctieAdmin)
