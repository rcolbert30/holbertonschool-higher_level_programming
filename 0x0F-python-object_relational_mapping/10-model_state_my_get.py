#!/usr/bin/python3
""" prints state with name passed in as argument """
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

    state_ids = Session.query(State).filter(State.name == sys.argv[4]).all()
    if state_ids:
        for state in state_ids:
            print("{}".format(state.id))
    else:
        print("Not found")

    Session.close()
