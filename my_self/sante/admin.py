from django.contrib import admin
from .models import Portfolio, Education, Experience, ContactMessage, Project

# Register your models here.
admin.site.register(Portfolio)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(ContactMessage)
admin.site.register(Project)