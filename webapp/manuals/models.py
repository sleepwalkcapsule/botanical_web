from webapp.db import db

class Manuals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    text = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return '<Manuals {} {}>'.format(self.title, self.url)