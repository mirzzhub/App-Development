from django.contrib import admin
from .models import User,Rental,Contact,Admins,Issues
# Register your models here.
admin.site.register(User)
admin.site.register(Rental)
admin.site.register(Contact)
admin.site.register(Admins)
admin.site.register(Issues)