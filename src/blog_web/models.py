from .extensions import db  

class Count(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<count {self.count}>"
