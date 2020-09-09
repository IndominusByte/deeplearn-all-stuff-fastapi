from define_create_table import addresses, users
from create_query import conn
from sqlalchemy import select

a1 = addresses.alias()
a2 = addresses.alias()

s = select([users]) \
    .where(
    ((users.c.id == a1.c.user_id) & (users.c.id == a2.c.user_id) &
    (a1.c.email_address == 'jack@msn.com') & (a2.c.email_address == 'jack@msn.com'))
)
print(s)
# print(conn.execute(s).fetchall())
print()

address_subq = s.alias()
s = select([users.c.name]).where(users.c.id == address_subq.c.id)
print(s)
print(conn.execute(s).fetchall())
