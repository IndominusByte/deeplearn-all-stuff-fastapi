from sqlalchemy import String, func, asc
from sqlalchemy.sql import text, bindparam, select
from create_query import conn, addresses

s = text(
    "SELECT users.fullname || ', ' || addresses.email_address AS title "
    "FROM users, addresses "
    "WHERE users.id = addresses.user_id "
    "AND users.name BETWEEN :x AND :y "
    "AND (addresses.email_address LIKE :e1 "
    "OR addresses.email_address LIKE :e2)"
)

print([row for row in conn.execute(s,x='m', y='z', e1='%@aol.com', e2='%@msn.com')])

# Specifying Bound Parameter Behaviors
stmt = text("SELECT * FROM users where users.name BETWEEN :x AND :y")
# stmt = stmt.bindparams(x="m",y="z")

# The parameters can also be explicitly typed
stmt = stmt.bindparams(bindparam("x", type_=String), bindparam("y", type_=String))
result = conn.execute(stmt, {'x':'m','y':'z'})
print([row for row in result])

# Using text() fragments inside bigger statements
s = select([text("users.fullname || ', ' || addresses.email_address AS title")]) \
    .where(
    (text("users.id = addresses.user_id") &
    text("users.name BETWEEN 'm' AND 'z'") &
    text("(addresses.email_address LIKE :x OR addresses.email_address LIKE :y)"))
).select_from(text('users, addresses'))

result = conn.execute(s,x='%@aol.com', y='%@msn.com')
print([row for row in result])

# Ordering or Grouping by a Label
stmt = select([addresses.c.user_id,func.count(addresses.c.id).label('num_addresses')]) \
    .group_by("user_id").order_by("user_id","num_addresses")
print(stmt)
result = conn.execute(stmt)
print([row for row in result])

# We can use modifiers like asc() or desc() by passing the string name
stmt = select([addresses.c.user_id,func.count(addresses.c.id).label('num_addresses')]) \
    .group_by("user_id").order_by(asc('num_addresses'))
print(stmt)
result = conn.execute(stmt)
print([row for row in result])
