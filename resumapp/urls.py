from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

# third party
import rest_framework_jwt.views
import djoser.views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token;
from rest_framework_extensions.routers import ExtendedSimpleRouter
from django.conf.urls import include, url

# resumapp
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

    # auth
    url(r'^admin/', admin.site.urls),

    url(r'^auth/login', rest_framework_jwt.views.obtain_jwt_token),
    url(r'^auth/register', djoser.views.RegistrationView.as_view()),
    url(r'^auth/password/reset', djoser.views.PasswordResetView.as_view()),
    url(r'^auth/password/reset/confirm', djoser.views.PasswordResetConfirmView.as_view()),

    # api token
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),

    # api
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^exps/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^projects/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^contributions/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^skills/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^profiles', include('rest_framework.urls', namespace='rest_framework')),
]