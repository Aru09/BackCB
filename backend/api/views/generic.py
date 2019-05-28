from api.models import Review, Reviewer_metadata, Company
from api.serializers import CompanySerializer, Reviewer_metadataSerializers, ReviewSerializers
#from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


class ReviewList(generics.ListCreateAPIView):
    permission_classes = IsAuthenticated
    serializer_class =ReviewSerializers

    def get_queryset(self):
        return Review.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ReviewerList(generics.ListCreateAPIView):
    permission_classes = IsAuthenticated
    serializer_class = Reviewer_metadataSerializers

    def get_queryset(self):
        return Reviewer_metadata.objects.filter



