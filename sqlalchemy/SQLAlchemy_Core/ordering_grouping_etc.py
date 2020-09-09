from define_create_table import users, addresses
from create_query import conn
from sqlalchemy.sql import select, func

stmt = select([users.c.name]).order_by(users.c.name)
print(conn.execute(stmt).fetchall())
print()

"""
Ascending or descending can be controlled using the ColumnElement.asc() and ColumnElement.desc() modifiers:
"""
stmt = select([users.c.name]).order_by(users.c.name.desc())
print(conn.execute(stmt).fetchall())
print()

"""
Grouping refers to the GROUP BY clause, and is usually used in conjunction
with aggregate functions to establish groups of rows to be aggregated.
This is provided via the SelectBase.group_by() method:
"""
stmt = select([users.c.name, func.count(addresses.c.user_id)]).select_from(users.join(addresses)).group_by(users.c.name)
print(conn.execute(stmt).fetchall())
print()

"""
HAVING can be used to filter results on an aggregate value, after GROUP BY has been applied.
It’s available here via the Select.having() method:
"""
stmt = select([users.c.name, func.count(addresses.c.user_id)]).select_from(users.join(addresses)) \
    .group_by(users.c.name).having(func.length(users.c.name) > 4)
print(conn.execute(stmt).fetchall())
print()

"""
The Select.limit() and Select.offset() methods provide an easy abstraction into the current backend’s methodology:
"""
stmt = select([users.c.name, addresses.c.email_address]).select_from(users.join(addresses)) \
    .limit(1).offset(1)
print(conn.execute(stmt).fetchall())
print()
