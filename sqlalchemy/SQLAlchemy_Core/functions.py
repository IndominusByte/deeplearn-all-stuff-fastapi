from sqlalchemy import String
from sqlalchemy.sql import func, select
from create_query import conn, addresses

print(func.now())
print()

print(func.current_timestamp())
print()

"""
use the result function scalar() to just read the first column of the first row
and then close the result; the label, even though present, is not important in this case:
"""
s = select([func.max(addresses.c.email_address, type_=String).label('maxemail')])
print(conn.execute(s).scalar())
