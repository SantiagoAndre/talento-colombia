from graphene import ObjectType, String, Schema
from .jobcall_schema import Query as QueryJobCall,Mutation as MutationJobCall

class Query(QueryJobCall):
    pass
class Mutation(MutationJobCall):
    pass
ROOT_SCHEMA = Schema(query=Query,mutation=Mutation)