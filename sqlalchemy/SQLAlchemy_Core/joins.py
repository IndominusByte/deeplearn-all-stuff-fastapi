from define_create_table import users, addresses
from create_query import conn
from sqlalchemy import select

print(users.join(addresses))
print()

"""
if we want to join on all users who use the same name in their email address as their username:
"""
print(users.join(addresses, addresses.c.email_address.like(users.c.name + '%')))
print()

"""
When we create a select() construct, SQLAlchemy looks around at the tables we’ve mentioned
and then places them in the FROM clause of the statement.
When we use JOINs however, we know what FROM clause we want,
so here we make use of the Select.select_from() method:
"""
s = select([users.c.name]).select_from(users.join(addresses, addresses.c.email_address.like(users.c.name + '%')))
print(s)
print(conn.execute(s).fetchall())
print()

"""
The FromClause.outerjoin() method creates LEFT OUTER JOIN constructs, and is used in the same way as FromClause.join():
"""
s = select([users.c.fullname]).select_from(users.outerjoin(addresses))
print(s)
