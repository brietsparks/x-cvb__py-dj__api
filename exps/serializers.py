from rest_framework import serializers
from exps.models import Exp, Project, Contribution


class ExpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exp
        fields = ('id', 'parent_id', 'title', 'summary')


class ProjectSerializer(ExpSerializer):
    class Meta(ExpSerializer.Meta):
        model = Project