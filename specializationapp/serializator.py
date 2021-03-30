from rest_framework import routers,serializers,viewsets
from .models import SubSection,Specialization

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
        model = SubSection
        fields = ['id', 'uid', 'name']