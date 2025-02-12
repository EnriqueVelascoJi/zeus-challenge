import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.tasks import Base

POSTGRES_DB=os.getenv("POSTGRES_DB")
POSTGRES_USER=os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD")
POSTGRES_PORT=os.getenv("POSTGRES_PORT")

# url_connection = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db.vgmnnonyynccbvfwjrgf.supabase.co:{POSTGRES_PORT}/{POSTGRES_DB}'
url_connection = f'postgresql://postgres.vgmnnonyynccbvfwjrgf:{POSTGRES_PASSWORD}@aws-0-us-west-1.pooler.supabase.com:5432/postgres'
engine = create_engine(url_connection)
try:
    with engine.connect() as connection_str:
        print('Successfully connected to the PostgreSQL database')
        Session = sessionmaker(bind=engine)
        session = Session()

        Base.metadata.create_all(engine)

except Exception as ex:
    print(f'Sorry failed to connect: {ex}')



