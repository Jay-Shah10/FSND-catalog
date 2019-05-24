from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Genre, Movies, Base

engine = create_engine('sqlite:///moviegenre.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create a horror genre.
horror = Genre(name="Horror")
session.add(horror)
session.commit()

# Create action genre.
action = Genre(name="Action")
session.add(action)
session.commit()

# Create Thriller Genre.
thriller = Genre(name="Thriller")
session.add(thriller)
session.commit()


# Creating Classic Genre.
classic = Genre(name="Classic")
session.add(classic)
session.commit()

# Creating Comedy Genre.
comedy = Genre(name="Comedy")
session.add(comedy)
session.commit()

# Creating Drama Genre.
drama = Genre(name="Drama")
session.add(drama)
session.commit()

print engine
print "finished populating a database."

