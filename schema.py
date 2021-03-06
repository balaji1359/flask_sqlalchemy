import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import Department, Employee, Role


class DepartmentNode(SQLAlchemyObjectType):
    class Meta:
        model = Department
        interfaces = (relay.Node,)


class DepartmentConnection(relay.Connection):
    class Meta:
        node = DepartmentNode


class EmployeeNode(SQLAlchemyObjectType):
    class Meta:
        model = Employee
        interfaces = (relay.Node,)


class EmployeeConnection(relay.Connection):
    class Meta:
        node = EmployeeNode

        
        
class Role(SQLAlchemyObjectType):
    class Meta:
        model = RoleModel
        interfaces = (relay.Node, )


class RoleConnection(relay.Connection):
    class Meta:
        node = Role


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_employees = SQLAlchemyConnectionField(EmployeeConnection)
    all_roles = SQLAlchemyConnectionField(RoleConnection)
    all_departments = SQLAlchemyConnectionField(DepartmentConnection, sort=None)


schema = graphene.Schema(query=Query)
