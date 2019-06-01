from django.contrib import admin
from .models import Review, ReviewerMetadata , Company

admin.site.register(ReviewerMetadata)
admin.site.register(Company)
admin.site.register(Review)

# Register your models here.
