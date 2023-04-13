from django.contrib import admin
from home.models import Onedsa, Onedsb, OneDsaPortion, OneDsaTimeTable, OneDsaSit

# Register your models here.
admin.site.register(Onedsa)
admin.site.register(Onedsb)
admin.site.register(OneDsaPortion)
admin.site.register(OneDsaTimeTable)
admin.site.register(OneDsaSit)
