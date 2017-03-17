from exps.schema import Query as ExpsQuery
from skills.schema import Query as SkillsQuery
from profiles.schema import Query as ProfileQuery
from graphene import relay, ObjectType, Schema


class Query(ExpsQuery, SkillsQuery, ProfileQuery, ObjectType):
    pass


schema = Schema(query=Query)
