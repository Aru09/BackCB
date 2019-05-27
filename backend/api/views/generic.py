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


class CompanyList(generics.ListCreateAPIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

