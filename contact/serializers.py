from rest_framework import serializers
from django.db import models
from .models import Message, Contact, SocialMedia, Phone

# TODO если пользователь зареган то поля уже заполнены
class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['id', 'first_name', 'last_name', 'email', 'body', 'creation_date', ]
        read_only_fields = ['creation_date', ]


class PhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phone
        fields = ['id', 'phone_number', ]
        read_only_fields = ['creation_date', ]


class ContactSerializer(serializers.ModelSerializer):
    phone_numbers = PhoneSerializer(many=True, read_only=True)

    class Meta:
        model = Contact
        fields = ['id', 'email', 'address', 'address_link', 'phone_numbers']


class SocialMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = SocialMedia
        fields = ['id', 'name', 'link', ]
