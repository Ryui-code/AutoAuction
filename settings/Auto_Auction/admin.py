from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = [
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'password', 'role', 'data_registered', 'token'
            ),
        }),
    ]
    read_only_fields = ['data_registered', 'token']

admin.site.register(Car)
admin.site.register(Auction)
admin.site.register(Bid)
admin.site.register(Feedback)