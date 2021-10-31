from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import request, status
from api.serializers import advisorListSerializer, bookingSerializer
from api.models import advisor, booking
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsOwner

# Created views here:-


class testapi(APIView):

    def get(self, request, format=None):
        return Response({"name": "Raj"})


class advisorAPIView(APIView):
    serializer_class = advisorListSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get(self, request, format=None):
        data = advisor.objects.filter(user=request.user)
        serializer = self.serializer_class(data, many=True)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        # print(request.data)
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class advisorsAPIView(APIView):
    serializer_class = advisorListSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_object(self, pk):
        try:
            obj = advisor.objects.get(pk=pk)
            self.check_object_permissions(self.request, obj)
            return obj
        except advisor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        serializer = self.serializer_class(self.get_object(pk))
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)


class bookingAPIView(APIView):
    serializer_class = bookingSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def post(self, request, format=None):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_200_OK)


class bookedAPIView(APIView):
    serializer_class = bookingSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_object(self, pk):
        try:
            obj = booking.objects.get(pk=pk)
            self.check_object_permissions(self.request, obj)
            return obj
        except booking.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        booking = self.get_object(pk)
        serializer = self.serializer_class(booking)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)
