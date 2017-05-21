from sqlalchemy import Column, Integer, DateTime, func
from abc import ABCMeta, abstractmethod
from app import db


class Base(db.Model):
    """
    Base model class from which other models will inherit from
    """
    __metaclass__ = ABCMeta
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    date_created = Column(DateTime, default=func.current_timestamp())
    date_modified = Column(DateTime, default=func.current_timestamp(),
                           onupdate=func.current_timestamp())

    @abstractmethod
    def __repr__(self):
        """
        :return: representation of this object as a Human readable string
        """
        pass

    @abstractmethod
    def to_json(self):
        """
        Converts Model to JSON
        :return: JSON representation of model
        """
        pass

    @abstractmethod
    def from_json(self):
        """
        Initializes this model from JSON received params
        :return: initialized model
        """
        pass
