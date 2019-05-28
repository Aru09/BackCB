from rest_framework import serializers
from django.utils import timezone
from .models import Company, Reviewer_metadata, Review
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username')

class CompanySerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=50)

    class Meta:
        model = Company
        fields = ('id', 'name')

class Reviewer_metadataSerializers(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    email = serializers.EmailField(max_length=50)
    phone = serializers.IntegerField()

    class Meta:
        model = Reviewer_metadata
        fields = ('id', 'user', 'email', 'phone')

class ReviewSerializers(serializers.ModelSerializer):
    rating = serializers.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    title = serializers.CharField(max_length=64)
    summary = serializers.CharField(max_length=10000)
    ip_address = serializers.CharField(max_length=100)
    submission_date = serializers.DateTimeField(default=timezone.now)
    company_id = CompanySerializer(read_only=True)
    #reviewer_id = Reviewer_metadataSerializers(read_only=True)
    created_by=Reviewer_metadataSerializers(read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'rating', 'title', 'summary', 'ip_address', 'submission_date', 'company_id','created_by')

