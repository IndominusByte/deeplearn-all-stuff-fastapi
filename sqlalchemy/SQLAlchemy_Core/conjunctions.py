from sqlalchemy.sql import and_, or_, select
from define_create_table import users, addresses
from create_query import conn

query = and_(
    users.c.name.like('%a%'), users.c.id == addresses.c.user_id,
    or_(addresses.c.email_address == 'email', addresses.c.email_address == 'email'),
    and_(users.c.id <= 'id')
)
print(query)
print()

"""
And you can also use the re-jiggered bitwise AND, OR and NOT operators,
although because of Python operator precedence you have to watch your parenthesis:
"""
query = (
    users.c.name.like('%a%') & (users.c.id == addresses.c.user_id) &
    ((addresses.c.email_address == 'email') | (addresses.c.email_address == 'email')) & (users.c.id <= 'id')
)
print(query)
print()

s = select([(users.c.name + ' ,' + addresses.c.email_address).label('title')]) \
    .where(
    (
        (users.c.id == addresses.c.user_id) & users.c.name.between('m','z') &
        (addresses.c.email_address.like('%@aol.com') | addresses.c.email_address.like('%gmail.com'))
    )
)

print([row for row in conn.execute(s)])
