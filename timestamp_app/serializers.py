from rest_framework import serializers
from .models import user_timestamp, document_timestamp ,organisation_timestamp
import os
import requests
import json , datetime
class Timestampserializer (serializers.ModelSerializer):
    owner = serializers.ReadOnlyField()
    created_date = serializers.ReadOnlyField()
    created_time = serializers.ReadOnlyField()
    user_id = serializers.ReadOnlyField()
    class Meta:
        model = user_timestamp
        fields = ('action', 'user_id', 'owner', 'created_date', 'created_time')
    
    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user.email
        validated_data['user_id'] = self.context['request'].user.id
        validated_data['created_date'] = datetime.datetime.now().date()
        validated_data['created_time'] = datetime.datetime.now().time()
        return super().create(validated_data)
    
    


class TimestampDocserializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField()
    created_date = serializers.ReadOnlyField()
    created_time = serializers.ReadOnlyField()
    user_id = serializers.ReadOnlyField()

    class Meta:
        model = document_timestamp
        fields = ('action', 'user_id', 'owner', 'document_id', 'created_time', 'created_date')
        
    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user.email
        validated_data['user_id'] = self.context['request'].user.id
        validated_data['created_date'] = datetime.datetime.now().date()
        validated_data['created_time'] = datetime.datetime.now().time()
        return super().create(validated_data)
    
    
    

class TimestampOrgserializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField()
    created_date = serializers.ReadOnlyField()
    created_time = serializers.ReadOnlyField()
    user_id = serializers.ReadOnlyField()

    class Meta:
        model = organisation_timestamp
        fields = ('action', 'user_id', 'owner', 'organisation', 'created_time', 'created_date')
    
    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user.email
        validated_data['user_id'] = self.context['request'].user.id
        validated_data['created_date'] = datetime.datetime.now().date()
        validated_data['created_time'] = datetime.datetime.now().time()
        return super().create(validated_data)
    
    
    