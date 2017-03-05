from rest_framework import viewsets
from exps.models import Exp, Project, Contribution
from exps.serializers import ExpSerializer, ProjectSerializer, ContributionSerializer


class ExpViewSet(viewsets.ModelViewSet):
    queryset = Exp.objects.all()
    serializer_class = ExpSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ContributionViewSet(viewsets.ModelViewSet):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer
