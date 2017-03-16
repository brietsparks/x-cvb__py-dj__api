from graphene import relay, ObjectType, resolve_only_args, Schema, List
from graphene_django import DjangoConnectionField, DjangoObjectType

from .models import Exp as ExpModel
from .models import Project as ProjectModel 
from .models import Contribution as ContributionModel


class Exp(DjangoObjectType):
    class Meta:
        model = ExpModel
        interfaces = (relay.Node,)


class Project(DjangoObjectType):
    class Meta:
        model = ProjectModel
        

class Contribution(Exp):
    class Meta:
        model = ContributionModel


class Query(ObjectType):
    projects = List(Project)
    contributions = List(Contribution)

    @resolve_only_args
    def resolve_projects(self):
        return ProjectModel.objects.all()

    @resolve_only_args
    def resolve_contributions(self):
        return ContributionModel.objects.all()


schema = Schema(query=Query, types=[Project, Contribution])