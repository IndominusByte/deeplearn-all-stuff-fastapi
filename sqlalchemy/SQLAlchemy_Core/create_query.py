from define_create_table import users, addresses
from connecting import engine

print("=== INSERT EXPRESSIONS ===")
# Insert Expressions
ins = users.insert()
print(ins)
ins = users.insert().values(name='oman',fullname='nyoman pradipta')
print(ins)
print(ins.compile().params)
print("=" * 26 + '\n')

print("=== EXECUTING ===")
# EXECUTING
conn = engine.connect()
print(conn)
result = conn.execute(ins)
print(result.inserted_primary_key)
print("=" * 26 + '\n')

# Executing Multiple Statements
print("=== Executing Multiple Statements ===")
result = conn.execute(users.insert(), name='lol',fullname='ahsiap')
print(result.inserted_primary_key)
conn.execute(addresses.insert(), [
    {'user_id': 1, 'email_address': 'jack@yahoo.com'},
    {'user_id': 1, 'email_address': 'jack@msn.com'},
    {'user_id': 2, 'email_address': 'www@www.org'},
    {'user_id': 2, 'email_address': 'wendy@aol.com'},
])
conn.execute(addresses.insert(), {'user_id': 1, 'email_address': 'oman@gmail.com'})
print("=" * 26 + '\n')
