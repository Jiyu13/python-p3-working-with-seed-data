#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game

fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///seed_db.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # # 1. ============create rows and add rows to existing rows======================
    # Create new instances of Game and add them as new rows to the database
    btow = Game(title="Breath of the Wild", platform="Switch", genre="Adventure", price=60)
    ffvii = Game(title="Final Fantasy VII", platform="Playstation", genre="RPG", price=30)
    mk8 = Game(title="Mario Kart 8", platform="Switch", genre="Racing", price=50)

    # add new row
    ccs = Game(title="Candy Crush Saga", platform="Mobile", genre="Puzzle", price=0)

    # create old rows before the creation of any new records
    session.query(Game).delete()
    session.commit()

    # session.bulk_save_objects([btow, ffvii, mk8, ccs])
    # # commit changes to pesist in the db
    # session.commit()
    # # install faker if needed: pip install faker
    # # then run this file => python seed.py
    # # returns nothing if it executes without errors
    # # then run debug.py again
    # # =============================================================================

    # 2. ===============using Fake library to generate randomised data=================
    print("Seeding games...")
    games = [
        Game(
            title=fake.name(),
            genre=fake.word(),
            platform=fake.word(),
            price=random.randint(0, 60)
        )
        for i in range(50)
    ]

    session.bulk_save_objects(games)
    session.commit()
    # # ===============================================================================