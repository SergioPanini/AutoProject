from django.contrib import admin
from .models import Users, Numbers, Parks, SecretTokens
# Register your models here.

admin.site.register(Users)
admin.site.register(Numbers)
admin.site.register(Parks)
admin.site.register(SecretTokens)
 