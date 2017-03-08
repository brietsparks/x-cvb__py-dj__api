from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

from rest_framework import routers, serializers, viewsets
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from rest_framework_extensions.routers import ExtendedSimpleRouter

from exps.views import ExpViewSet, ProjectViewSet, ContributionViewSet
from skills.views import SkillViewSet
from profiles.views import ProfileViewSet


router = ExtendedSimpleRouter()
router.register(r'exps', ExpViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'contributions', ContributionViewSet)
router.register(r'skills', SkillViewSet)
(
    router.register(r'profiles', ProfileViewSet)
          .register(r'exps', ExpViewSet, parents_query_lookups=['profile_id'], base_name='profiles-exps')
)

urlpatterns = [
    url(r'^', include(router.urls)),

    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),

    url(r'^exps/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^projects/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^contributions/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^skills/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^profiles', include('rest_framework.urls', namespace='rest_framework')),
]