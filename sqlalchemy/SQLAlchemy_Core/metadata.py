from sqlalchemy import MetaData, Table, Column, String, Integer, ForeignKey, create_engine
from sqlalchemy.sql import select

engine = create_engine('sqlite:///:memory:', echo=False)

metadata = MetaData()

users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(100), nullable=False),
    Column('fullname', String(50), nullable=False)
)

addresses = Table('addresses', metadata,
    Column('id', Integer, primary_key=True),
    Column('email_address', String(100), nullable=False),
    Column('user_id', Integer, ForeignKey('users.id'), nullable=False)
)

metadata.create_all(engine)

conn = engine.connect()

conn.execute(users.insert().values(name='jack',fullname='nyoman pradipta'))
conn.execute(addresses.insert(), [
    {'user_id': 1, 'email_address': 'jack@yahoo.com'},
    {'user_id': 1, 'email_address': 'jack@msn.com'},
])

"""
The MetaData object contains all of the schema constructs we’ve associated with it.
It supports a few methods of accessing these table objects,
such as the sorted_tables accessor which returns a list of each Table object
in order of foreign key dependency (that is, each table is preceded by all tables which it references):
"""
print([x.name for x in metadata.sorted_tables])

# access the column "ID":
print(users.columns.id)
# or just
print(users.c.id)
# via string
print(users.c['id'])
# iterate through all columns
print([x for x in users.c])
# get the table's primary key columns
print([x for x in users.primary_key])
# get the table's foreign key objects:
print([x for x in addresses.foreign_keys])
# get the table related by a foreign key
print(list(addresses.c.user_id.foreign_keys)[0].column.table.c.name)

s = select([addresses,users]).where(addresses.c.email_address == 'jack@yahoo.com').select_from(addresses.join(users))
print(s)
print(conn.execute(s).fetchone().name)
