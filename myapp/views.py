from django.shortcuts import render

# Create your views here.
from . models import Speaker,Event
from . serializers import SpeakerSerializer,EventSerializer
from rest_framework import generics

class SpeakerList(generics.ListCreateAPIView):
    queryset=Speaker.objects.all()
    serializer_class=SpeakerSerializer

class EventList(generics.ListCreateAPIView):
    queryset=Speaker.objects.all()
    serializer_class=SpeakerSerializer

class SpeakerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Speaker.objects.all()
    serializer_class=SpeakerSerializer

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Event.objects.all()
    serializer_class=EventSerializer



