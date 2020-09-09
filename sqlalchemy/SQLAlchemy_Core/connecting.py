from sqlalchemy import create_engine

"""
The echo flag is a shortcut to setting up SQLAlchemy logging, which is accomplished via Python’s
standard logging module. With it enabled, we’ll see all the generated SQL produced.
If you are working through this tutorial and want less output generated, set it to False
"""
engine = create_engine('sqlite:///:memory:', echo=False)
