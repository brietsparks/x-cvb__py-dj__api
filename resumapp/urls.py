"""resumapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from items.models import Item
from rest_framework import routers, serializers, viewsets
from rest_framework_jwt.views import obtain_jwt_token

from exps import views as exp_views
from skills import views as skill_views
from profiles import views as profile_views


router = routers.DefaultRouter()
router.register(r'exps', exp_views.ExpViewSet)
router.register(r'projects', exp_views.ProjectViewSet)
router.register(r'contributions', exp_views.ContributionViewSet)
router.register(r'skills', skill_views.SkillViewSet)
router.register(r'profiles', profile_views.ProfileViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),

    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^api-token-auth/', obtain_jwt_token),

    url(r'^exps/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^projects/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^contributions/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^skills/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^profiles', include('rest_framework.urls', namespace='rest_framework')),
]