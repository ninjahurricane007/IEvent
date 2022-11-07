from django.contrib import admin

# Register your models here.
from .models import Fests,Events

admin.site.register(Fests)
admin.site.register(Events)
