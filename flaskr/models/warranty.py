from . import db


class Warranty(db.Model):
    __tablename__ = 'warranty'

    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return 'Warranty from {} to {}'.format(
            self.start_date, self.end_date
        )
