from rest_framework import serializers
from exps.models import Exp, Project, Contribution
from skills.serializers import SkillSerializer


class ExpSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'parent_id', 'profile_id', 'title', 'summary')


class ProjectSerializer(ExpSerializer):
    class Meta(ExpSerializer.Meta):
        model = Project


class ContributionSerializer(ExpSerializer):
    skills = SkillSerializer(many=True)

    class Meta(ExpSerializer.Meta):
        model = Contribution
        fields = ExpSerializer.Meta.fields + ('skills',)
