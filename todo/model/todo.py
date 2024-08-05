from todo import db


class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    complete = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Todo %s>' % self.title
