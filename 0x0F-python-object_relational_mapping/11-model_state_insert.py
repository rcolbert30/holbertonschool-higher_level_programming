#!/usr/bin/python3
'''inserts obj into database then prints the id'''
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

    new_state = State(name="Louisiana")
    Session.add(new_state)
    Session.commit()

    print('{}'.format(new_state.id))

    Session.close()
