from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Band, Venue, Concert, Base  # Import the models from your main file (assuming models.py)

# Connect to the SQLite database
engine = create_engine('sqlite:///concerts.db')

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Drop all tables and recreate them (for clean seeding)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Sample bands
band1 = Band(name="The Rolling Stones", hometown="London")
band2 = Band(name="The Beatles", hometown="Liverpool")
band3 = Band(name="Queen", hometown="London")

# Sample venues
venue1 = Venue(title="Wembley Stadium", city="London")
venue2 = Venue(title="Madison Square Garden", city="New York")
venue3 = Venue(title="Hollywood Bowl", city="Los Angeles")

# Sample concerts
concert1 = Concert(date="2023-05-15", band=band1, venue=venue1)
concert2 = Concert(date="2023-06-20", band=band2, venue=venue2)
concert3 = Concert(date="2023-07-25", band=band3, venue=venue3)
concert4 = Concert(date="2023-08-15", band=band1, venue=venue2)
concert5 = Concert(date="2023-09-10", band=band3, venue=venue1)

# Add the instances to the session
session.add_all([band1, band2, band3])
session.add_all([venue1, venue2, venue3])
session.add_all([concert1, concert2, concert3, concert4, concert5])

# Commit the session to save the data to the database
session.commit()

# Close the session
session.close()

print("Database seeded successfully!")
