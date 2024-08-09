from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Rental, User, Admins, Contact, Issues
from .serializers import RentalSerializer, UserSerializer, AdminsSerializer, ContactSerializer, IssuesSerializer
from .filters import RentalFilter, UserFilter, AdminsFilter, ContactFilter, IssuesFilter

class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.all()
    serializer_class = RentalSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RentalFilter

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter

class AdminsViewSet(viewsets.ModelViewSet):
    queryset = Admins.objects.all()
    serializer_class = AdminsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdminsFilter

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ContactFilter

class IssuesViewSet(viewsets.ModelViewSet):
    queryset = Issues.objects.all()
    serializer_class = IssuesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = IssuesFilter
