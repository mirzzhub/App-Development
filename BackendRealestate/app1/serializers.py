from rest_framework import serializers
from .models import Rental, User, Admins, Contact, Issues

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class AdminsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admins
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class IssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issues
        fields = '__all__'
