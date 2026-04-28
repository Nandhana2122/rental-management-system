# from django.contrib import admin

# # Register your models here.
# from .models import *

# admin.site.register(Profile)

# from .models import Property




from django.contrib import admin
from .models import *
from django.utils.html import format_html
from .models import ChatMessage



# class PropertyAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'image_preview')

#     def image_preview(self, obj):
#         if obj.image:
#             return format_html('<img src="{}" width="60" />', obj.image.url)
#         return "No Image"

# admin.site.register(Property, PropertyAdmin)



@admin.register(EmailOTP)
class EmailOTPAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'otp', 'created_at')
    search_fields = ('user',)
    list_filter = ('user',)
    list_display_links = ('id', 'user')
    ordering = ('id',)

@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone', 'address', 'city', 'state', 'pincode', 'occupation', 'family_size', 'purpose', 'budget', 'preferred_type')
    search_fields = ('user__username', 'phone')
    list_filter = ('user',)
    list_display_links = ('id', 'user')
    ordering = ('id',)
    

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'property', 'amount','status', 'created_at')
    search_fields = ('user__username',)
    list_filter = ('user',)
    list_display_links = ('id', 'user')
    ordering = ('id',)


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'location', 'rent')
    search_fields = ('user__username', 'title')
    list_filter = ('user',)
    list_display_links = ('id', 'user')
    ordering = ('id',)



class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'message', 'timestamp')  


admin.site.register(ChatMessage, ChatMessageAdmin)      