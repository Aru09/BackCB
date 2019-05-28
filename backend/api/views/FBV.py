from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.models import Company, Reviewer_metadata
from api.serializers import CompanySerializer, Reviewer_metadataSerializers


@api_view(['GET', 'POST'])
def CompanyList(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def ReviewerList(request):
    if request.method == 'GET':
        reviewers = Reviewer_metadata.objects.all()
        serializer = Reviewer_metadataSerializers(reviewers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Reviewer_metadataSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
