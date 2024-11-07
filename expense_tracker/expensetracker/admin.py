from django.contrib import admin
from .models import User, Admin, Transaction, Log

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone']

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'amount', 'user']

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ['date', 'content_object']