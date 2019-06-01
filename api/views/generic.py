from api import models
from api.models import Review, Company
from api import serializers
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
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
