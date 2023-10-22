from db import db


class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(80), unique=True, nullable=False)

    # lazy means items will not be prefetched
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic")