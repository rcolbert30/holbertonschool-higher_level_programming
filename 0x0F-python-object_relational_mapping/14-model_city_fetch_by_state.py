#!/usr/bin/python3
""" prints a onj with multiple tables"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    Session = session()

    loc_data = Session.query(City, State).filter(State.id == City.state_id)\
        .order_by(City.id)
    for city, state in loc_data:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    Session.close()

