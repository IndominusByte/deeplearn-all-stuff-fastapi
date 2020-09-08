from sqlalchemy import MetaData, Table, Column, String, Integer, ForeignKey
from connecting import engine

metadata = MetaData()

users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(10)),
    Column('fullname', String(50))
)

addresses = Table('addresses', metadata,
    Column('id', Integer, primary_key=True),
    Column('email_address', String(100), nullable=False),
    Column('user_id', Integer, ForeignKey('users.id'), nullable=False)
)

"""
to tell the MetaData we’d actually like to create our selection of tables for real inside the SQLite database,
we use create_all(), passing it the engine instance which points to our database.
This will check for the presence of each table first before creating, so it’s safe to call multiple times:
"""
metadata.create_all(engine)
print()
