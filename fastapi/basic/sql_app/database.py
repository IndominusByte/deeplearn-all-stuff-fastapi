from sqlalchemy import MetaData, create_engine
from databases import Database

db_url = 'sqlite:///./sql.db'

engine = create_engine(db_url, echo=True)
database = Database(db_url)

metadata = MetaData()
metadata.bind = engine
