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

#Horror movie one.
movie_description = """In 1970, paranormal investirgators and demonlogists Lorriance and Ed
                       Warren are summored to the home of Carolyn and Roger Perron. The Perrons
                       and their five daugthers have recently moved into a srcluded farmhouse, 
                       where a supernatural presence has made iteself known. Though the manifestation
                       are benign at first, they soon escalate in horrifying fashion."""
                       # description taken from google revie and description - search for The conjuring.
conjuring = Movies(name="The Conjuring",
                   description=movie_description,
                   year=2013,
                   genre=horror)
session.add(conjuring)
session.commit()

# Horror movie two.
# Description taken from google reviews and description - search for The nightmare on elm street 1984.
movie_description_2 = """In Wes Cravens's Classic Slasher film, several teenagers fall prey to Freddy Krueger,
                         a disfigured midnight mangler who preys on the teenagers in their dreams - which in turn,
                         kills them in reality. After investigating the phenomenon, Nancy begins to suspect that 
                         a dark secret kept by her and her friend's parents may be the key to solve the mystery. """
nightmare = Movies(name="The Nightmare on Elm Street",
                   description=movie_description_2,
                   year=1984,
                   genre=horror)
session.add(nightmare)
session.commit()

# Horror movie three.
# Description taken from google review and descriptions - search for "The Texas Chain Saw Massacre 2003." IMDB.
movie_description_3 = """After picking up a traumatized young hitchhiker, five friends find themselves stalked and hunted
                         by a deformed chainsaw-wielding loon and hist family of equally psychopathic killers."""
massacre = Movies(name="The Texas Chainsaw Massacre",
                  description=movie_description_3,
                  year=2003,
                  genre=horror)
session.add(massacre)
session.commit()

###########################################################
# Create action genre.
action = Genre(name="Action")
session.add(action)
session.commit()


# These are from: www.imdb.com/list/ls027328830
# Action Movie one:
action_description_1 = """In a future where mutants are nearly extinct, an elderly and weary
                          Logan leads a quite life. But when Laura, a mutant child pursued by 
                          scientists, comes to him for help, he must get her to safety."""
logan = Movies(name="Logan",
               description=action_description_1,
               year=2017,
               genre=action)
session.add(logan)
session.commit()

# Action movie 2: 
action_description_2 = """After the devastating events of Avengers: infinity war, the universe is in ruins.
                          with the help of remaning allies, the Avengers assemble once more in order to undo
                          Thanos' actions and restore order to the universe. """
endgame = Movies(name="Avengers: Endgame",
                 description=action_description_2,
                 year=2019,
                 genre=action)
session.add(endgame)
session.commit()

# Action movie 3:
action_description_3 = """An ex-hit-man comes out of retirement to track down
                          the gangsters that killed his dog and took everything
                          from him."""
wick = Movies(name="John Wick",
              description=action_description_3,
              year=2014,
              genre=action)
session.add(wick)
session.commit()


###########################################################
# Create Thriller Genre.
thriller = Genre(name="Thriller")
session.add(thriller)
session.commit()

# Movies from https://www.imdb.com/search/title?genres=thriller&groups=top_250&sort=user_rating,desc&ref_=adv_prv
# Thriller movie 1: 
thriller_description_1 = """When the Menace known as the Joker emerges from his mysterious past, he wreaks
                            havoc and chaos on the people of Gotham. The Dark Knight must accept one of the greates pyschological
                            and physical tests of this ability to fight injustice. """
dark_knight = Movies(name="The Dark Knight",
                     description=thriller_description_1,
                     year=2008,
                     genre=thriller)
session.add(dark_knight)
session.commit()

# Thriller movie 2: 
thriller_description_2 = """A thief steals corporate secrets through the use of dream-sharing technology
                            is given the invers task of planting an idea into a mind of a CEO."""
inception = Movies(name="Inception",
                   description=thriller_description_2,
                   year=2010,
                   genre=thriller)
session.add(inception)
session.commit()
 
# Thriller movie 3: 


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

