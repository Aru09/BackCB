from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Company, ReviewerMetadata, Review


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id',
                  'username')


class CompanySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)

    class Meta:
        model = Company
        fields = ('id',
                  'name')


class ReviewerMetadataSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReviewerMetadata
        fields = ('id',
                  'user',
                  'email',
                  'phone')


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id',
                  'rating',
                  'title',
                  'summary',
                  'ip_address',
                  'submission_date',
                  'company_id',
                  'created_by')

