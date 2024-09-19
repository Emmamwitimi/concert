# Concerts Database

## Overview

This project models a Concerts database using SQLAlchemy, which includes three main entities: Bands, Venues, and Concerts. Bands and Venues have a many-to-many relationship through Concerts, as a Band can perform multiple Concerts at various Venues. The Concerts table links Bands and Venues, recording each concert's date and additional information.

## Setup Instructions

### Prerequisites
- Python 3.x
- SQLAlchemy
- SQLite

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/concerts-db.git
