from .serializers import MessageSerializer, ContactSerializer, SocialMediaSerializer
from .models import Message, Contact, SocialMedia
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class SocialMediaViewSet(ModelViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
