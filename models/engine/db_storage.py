from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound
from sqlalchemy.exc import OperationalError
from sqlalchemy import Column, Integer, String
from models.user import User
from models.state import State


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new DBStorage object"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                    .format(os.getenv('HBNB_MYSQL_USER'),
                                            os.getenv('HBNB_MYSQL_PWD'),
                                            os.getenv('HBNB_MYSQL_HOST'),
                                            os.getenv('HBNB_MYSQL_DB')),
                                    pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)



    def all(self, cls=None):
        objects = {}
        if cls is None:
            classes = [User, State]
        else:
            classes = [cls]

        for c in classes:
            objects.update({obj.id: obj for obj in self.__session.query(c).all()})

        return objects

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
