from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

# third party
import rest_framework_jwt.views
import djoser.views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token;
from rest_framework_extensions.routers import ExtendedSimpleRouter
from django.conf.urls import include, url
from graphene_django.views import GraphQLView

# resumapp
from exps.views import ProjectViewSet, ContributionViewSet #, ExpViewSet
from skills.views import SkillViewSet
from profiles.views import ProfileViewSet


router = ExtendedSimpleRouter()
# router.register(r'exps', ExpViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'contributions', ContributionViewSet)
router.register(r'skills', SkillViewSet)
(
    router.register(r'profiles', ProfileViewSet)
          .register(r'projects', ProjectViewSet, parents_query_lookups=['profile_id'], base_name='profiles-contributions')
)
(
    router.register(r'profiles', ProfileViewSet)
          .register(r'contributions', ContributionViewSet, parents_query_lookups=['profile_id'], base_name='profiles-projects')
)

# graphql token view
# http://stackoverflow.com/questions/39026831/how-to-use-graphene-graphql-framework-with-django-rest-framework-authentication

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from resumapp.schema import schema
def graphql_token_view():
    view = GraphQLView.as_view(schema=schema)
    view = permission_classes((IsAuthenticated,))(view)
    view = authentication_classes((JSONWebTokenAuthentication,))(view)
    view = api_view(['POST', 'GET'])(view)
    return view


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

    # rest api
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^exps/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^projects/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^contributions/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^skills/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^profiles', include('rest_framework.urls', namespace='rest_framework')),

    # graphql api
    url(r'^graphiql', GraphQLView.as_view(graphiql=True)),
    url(r'^graphql_token', graphql_token_view()),
]