from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.contrib.auth.models import User


class ReviewListManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)


class Company(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ReviewerMetadata(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()

    def __str__(self):
        return self.user.username


class Review(models.Model):
    rating=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    title=models.CharField(max_length=64)
    summary=models.CharField(max_length=10000)
    ip_address=models.CharField(max_length=100)
    submission_date=models.DateTimeField(default=timezone.now)
    company_id=models.ForeignKey(Company, on_delete=models.CASCADE)
    #reviewer_id=models.ForeignKey(Reviewer_metadata,on_delete=models.CASCADE)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE,default=1)

    objects = ReviewListManager()

    def __str__(self):
        return self.title








