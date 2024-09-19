from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#SQLite engine and the base class for models
engine = create_engine('sqlite:///concerts.db')
Base = declarative_base()

# Band model
class Band(Base):
    __tablename__ = "bands"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    hometown = Column(String)

    # One-to-many relationship with Concert
    concerts = relationship('Concert', back_populates='band')

    def __repr__(self):
        return f"Band {self.id}: {self.name}, hometown {self.hometown}"

    def concerts(self):
        return self.concerts
    
    def venues(self):
        return set(concert.venue for concert in self.concerts)


#  Venue model
class Venue(Base):
    __tablename__ = "venues"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    city = Column(String)

    # One-to-many relationship with Concert
    concerts = relationship('Concert', back_populates='venue')

    def __repr__(self):
        return f"Venue {self.id}: {self.title}, city {self.city}"

    def concerts(self):
        return self.concerts
    
    def bands(self):
        return set(concert.band for concert in self.concerts)


# Concert model
class Concert(Base):
    __tablename__ = "concerts"
    
    id = Column(Integer, primary_key=True)
    date = Column(String)  # Corrected from `string` to `String`
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))

    # Many-to-one relationships with Band and Venue
    band = relationship('Band', back_populates='concerts')
    venue = relationship('Venue', back_populates='concerts')

    def __repr__(self):
        return f"Concert {self.id}: Band {self.band_id}, Venue {self.venue_id}"

    def band(self):
        return self.band
    def venue(self):
        return self.venue


# Create the tables in the database
Base.metadata.create_all(engine)
