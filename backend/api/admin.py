from django.contrib import admin
from .models import Review, Reviewer_metadata , Company

admin.site.register(Reviewer_metadata)
admin.site.register(Company)
admin.site.register(Review)

# Register your models here.
