from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin
from exps.models import Exp, Project, Contribution
from exps.serializers import ExpSerializer, ProjectSerializer, ContributionSerializer


# class ExpViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
#     queryset = Exp.objects.all()
#     serializer_class = ExpSerializer


class ProjectViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ContributionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer
