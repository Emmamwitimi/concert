from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Band, Venue, Concert

# Connect to the database
engine = create_engine('sqlite:///concerts.db')

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Function to print all bands
def print_all_bands():
    bands = session.query(Band).all()
    for band in bands:
        print(band)

# Function to print all concerts
def print_all_concerts():
    concerts = session.query(Concert).all()
    for concert in concerts:
        print(f"Concert {concert.id}: {concert.band.name} at {concert.venue.title} on {concert.date}")

# Function to print all venues
def print_all_venues():
    venues = session.query(Venue).all()
    for venue in venues:
        print(venue)

# Add custom test cases below:
def run_custom_tests():
    # Find a band by name
    rolling_stones = session.query(Band).filter(Band.name == "The Rolling Stones").first()
    if rolling_stones:
        print(f"Found band: {rolling_stones}")
    
    # Find concerts in a specific venue
    wembley_concerts = session.query(Concert).filter(Concert.venue.has(title="Wembley Stadium")).all()
    print(f"Concerts at Wembley Stadium: {wembley_concerts}")

# Example usage:
if __name__ == "__main__":
    print("Testing database queries...")
    
    # Test functions
    print_all_bands()
    print_all_concerts()
    print_all_venues()

    # Run custom tests
    run_custom_tests()

    # Close the session
    session.close()
