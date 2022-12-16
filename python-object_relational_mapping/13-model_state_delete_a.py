#!/usr/bin/python3
"""13-model_state_delete_a"""


if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    st = session.query(State).filter(State.name.like('%a%')).all()
    if st:
        for stat in st:
            session.delete(stat)
        session.commit()
    session.close()
