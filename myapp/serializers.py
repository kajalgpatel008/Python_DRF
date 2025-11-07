from rest_framework import serializers
from . models import Speaker, Event

class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Speaker
        fields=('name','description','photo')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=('title','desc','event_date')
