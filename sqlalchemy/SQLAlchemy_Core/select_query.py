from sqlalchemy.sql import select
from create_query import users, addresses, conn

s = select([users])
print(s)
"""
The result returned is again a ResultProxy object, which acts much like a DBAPI cursor,
including methods such as fetchone() and fetchall(). These methods return row objects,
which are provided via the RowProxy class.
The result object can be iterated directly in order to provide an iterator of RowProxy objects:
"""
results = conn.execute(s)
print(results)

"""
we see that printing each RowProxy produces a simple tuple-like result.
The RowProxy behaves like a hybrid between a Python mapping and tuple,
with several methods of retrieving the data in each column.
One common way is as a Python mapping of strings, using the string names of columns:
"""
data = [f"id: {row['id']}, name: {row['name']}" for row in results.fetchall()]
print(data)

"""
Another way is as a Python sequence, using integer indexes:
"""
results = conn.execute(s)
row = results.fetchone()
print("name:", row[1], "; fullname:", row[2])

"""
A more specialized method of column access is to use the SQL construct
that directly corresponds to a particular column as the mapping key; in this example,
it means we would use the Column objects selected in our SELECT directly as keys:
"""
print([row[users.c.name] for row in conn.execute(s)])

# Selecting Specific Columns
"""
If we’d like to more carefully control the columns which are placed in the COLUMNS clause of the select,
we reference individual Column objects from our Table.
These are available as named attributes off the c attribute of the Table object:
"""
s = select([users.c.name, users.c.fullname])
results = conn.execute(s)
print([row for row in results])

# SQL joins
s = select([users,addresses]).where(users.c.id == addresses.c.user_id)
results = conn.execute(s)
print([row for row in results])
