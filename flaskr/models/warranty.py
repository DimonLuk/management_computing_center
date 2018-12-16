from . import Base
from sqlalchemy import Column, Integer, Date


class Warranty(Base):
    __tablename__ = 'warranty'

    id = Column(Integer, primary_key=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    def __repr__(self):
        return 'Warranty from {} to {}'.format(
            self.start_date, self.end_date
        )
