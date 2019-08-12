#!/usr/bin/python3
""" deletes an obj form the database containing specific letter"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    Session = session()

    obj_delete = Session.query(State).filter(State.name.contains('a'))
    for states_with_a in obj_delete:
        Session.delete(states_with_a)
    Session.commit()

    Session.close()
