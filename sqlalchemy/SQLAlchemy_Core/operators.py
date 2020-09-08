from define_create_table import users, addresses

"""
Since we’ve stumbled upon SQLAlchemy’s operator paradigm, let’s go through some of its capabilities.
We’ve seen how to equate two columns to each other:
"""
print(users.c.id == addresses.c.user_id)

"""
If we use a literal value (a literal meaning, not a SQLAlchemy clause object), we get a bind parameter:
"""
print(users.c.id == 7)

# None converts to IS NULL
print(users.c.name == None)
