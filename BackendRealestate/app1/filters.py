from django_filters import rest_framework as filters
from .models import Rental, User, Admins, Contact, Issues

class RentalFilter(filters.FilterSet):
    class Meta:
        model = Rental
        fields = {
            'houseName': ['exact', 'icontains'],
            'area': ['exact', 'icontains'],
            'streetName': ['exact', 'icontains'],
            'city': ['exact', 'icontains'],
            'state': ['exact', 'icontains'],
            'address': ['exact', 'icontains'],
            'location': ['exact', 'icontains'],
            'ownerName': ['exact', 'icontains'],
            'ownerEmail': ['exact', 'icontains'],
            'rent': ['exact', 'gte', 'lte'],

        }

class UserFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'name': ['exact', 'icontains'],
            'password': ['exact', 'icontains'],
            'email': ['exact', 'icontains'],
        }

class AdminsFilter(filters.FilterSet):
    class Meta:
        model = Admins
        fields = {
            'name': ['exact', 'icontains'],
            'password': ['exact', 'icontains'],
            'email': ['exact', 'icontains'],
            'ownerCode': ['exact', 'gte', 'lte'],
        }

class ContactFilter(filters.FilterSet):
    class Meta:
        model = Contact
        fields = {
            'name': ['exact', 'icontains'],
            'message': ['exact', 'icontains'],
            'email': ['exact', 'icontains'],
        }

class IssuesFilter(filters.FilterSet):
    class Meta:
        model = Issues
        fields = {
            'user': ['exact'],
            'address': ['exact', 'icontains'],
            'issue': ['exact', 'icontains'],

        }
