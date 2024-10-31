from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    # Specify the fields to be displayed in the admin interface
    list_display = ('email', 'name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    ordering = ('email',)
    search_fields = ('email', 'name')

    # Define the fields to be used in the forms
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'phone_number', 'address', 'city', 'country', 'agreed_to_policy')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser')}
        ),
    )

    # Define which fields should be editable when creating a new user
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If creating a new user
            obj.set_password(form.cleaned_data['password'])  # Hash the password
        obj.save()

# Register the custom User model with the admin
admin.site.register(User, UserAdmin)
