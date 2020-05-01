from graphene import ObjectType, String, Schema
from .jobcall_schema import Query as QueryJobCall,Mutation as MutationJobCall
from .auth_schema import Mutation as AuthMutation

class Query(QueryJobCall):
    pass
class Mutation(MutationJobCall,AuthMutation):
    pass
ROOT_SCHEMA = Schema(query=Query,mutation=Mutation)