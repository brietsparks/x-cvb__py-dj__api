from .models import Skill as SkillModel

from graphene_django import DjangoObjectType
import graphene


class Skill(DjangoObjectType):
    class Meta:
        model = SkillModel


class Query(graphene.AbstractType):
    skills = graphene.List(Skill)

    @graphene.resolve_only_args
    def resolve_skills(self):
        return SkillModel.objects.all()
