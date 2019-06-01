from api import models
from api.models import Review, ReviewerMetadata, Company
from api import serializers
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from api.serializers import CompanySerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


class ReviewViewSet(viewsets.ModelViewSet):
    # queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Review.objects.for_user(self.request.user)

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.CompanySerializer


    # def list(self, request):
    #     queryset = Review.objects.all()
    #     serializer = ReviewSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, pk=None):
    #     queryset = Review.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = ReviewSerializer(user)
    #     return Response(serializer.data)


'''class ReviewList(generics.ListCreateAPIView):
    permission_classes = IsAuthenticated
    serializer_class =ReviewSerializers

    def get_queryset(self):
        return Review.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)'''


'''class ReviewerViewSet(viewsets.ModelViewSet):
    permission_classes = IsAuthenticated
    # queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def list(self, request):
        queryset = ReviewerMetadata.objects.all()
        serializer = ReviewerMetadataSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = ReviewerMetadata.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ReviewerMetadataSerializer(user)
        return Response(serializer.data)'''
