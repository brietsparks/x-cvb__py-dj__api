from .models import Profile as ProfileModel
from graphene_django import DjangoObjectType
import graphene


class Profile(DjangoObjectType):
    class Meta:
        model = ProfileModel


class Query(graphene.AbstractType):
    profile = graphene.Field(Profile, profile_id=graphene.Int())

    def resolve_profile(self, args, context, info):
        profile_id = args.get('profile_id')

        if id is not None:
            return ProfileModel.objects.get(pk=profile_id)

        return None
