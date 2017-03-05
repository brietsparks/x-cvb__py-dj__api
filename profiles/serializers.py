from rest_framework import serializers
from profiles.models import Profile
# from exps.serializers import ProjectSerializer, ContributionSerializer


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id',)
