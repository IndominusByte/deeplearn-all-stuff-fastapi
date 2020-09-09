from sqlalchemy.sql import bindparam, select
from create_query import users, addresses, conn

"""
An UPDATE statement is emitted using the TableClause.update() construct.
This works much like an INSERT, except there is an additional WHERE clause that can be specified:
"""

user = users.update().where(users.c.name == 'jack').values(name='test')
conn.execute(user)
print(user)
print(conn.execute(select([users])).fetchall())
print()

"""
When using TableClause.update() in an “executemany” context,
we may wish to also use explicitly named bound parameters in the WHERE clause.
Again, bindparam() is the construct used to achieve this:
"""
stmt = users.update().where(users.c.name == bindparam('oldname')).values(name=bindparam('newname'))
conn.execute(stmt, [
    {'oldname':'test', 'newname':'ed'},
    {'oldname':'wendy', 'newname':'mary'},
    {'oldname':'jim', 'newname':'jake'},
])
print(stmt)
print(conn.execute(select([users])).fetchall())
print()

# Multiple Table Updates
"""
When using MySQL, columns from each table can be assigned to in the SET clause directly,
using the dictionary form passed to Update.values():
"""
# stmt = users.update() \
#     .values({
#         users.c.name: 'testing',
#         addresses.c.email_address: 'marryme@gmail.com'
#     }).where(users.c.id == addresses.c.user_id).where(addresses.c.email_address.startswith('ed%'))
# conn.execute(stmt)

"""
The PostgreSQL, Microsoft SQL Server, and MySQL backends all support UPDATE statements that refer to multiple tables
"""
# stmt = users.update() \
#     .values(name='ed wood') \
#     .where(users.c.id == addresses.c.id) \
#     .where(addresses.c.email_address.startswith('ed%'))
# conn.execute(stmt)

# Deletes
"""
This is accomplished easily enough using the TableClause.delete() construct:
"""
conn.execute(addresses.delete())

conn.execute(users.delete().where(users.c.name == 'ed'))

print(conn.execute(select([users])).fetchall())

# Multiple Table Deletes
"""
The PostgreSQL, Microsoft SQL Server, and MySQL backends all support DELETE statements
that refer to multiple tables within the WHERE criteria
"""
# stmt = users.delete() \
#     .where(users.c.id == addresses.c.id) \
#     .where(addresses.c.email_address.startswith('ed%'))
# conn.execute(stmt)
