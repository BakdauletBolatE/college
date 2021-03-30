from rest_framework import serializers
from .models import SubSection,Specialization,Qualification

class SubSectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubSection
        fields = ['id', 'uid', 'name']

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ['id', 'uid', 'name']

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = ['id', 'uid', 'name']