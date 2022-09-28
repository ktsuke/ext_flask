from ..extensions import db

class Func(db.Model):
    __tablename__ = "funcs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    func = db.Column(db.String(150))
    plug = db.Column(db.String(150))
    inp = db.Column(db.String(200))
    outp = db.Column(db.String(150))
    desc = db.Column(db.String(350))

    def __repr__(self):
        return "<funcs(func={}, plug={}, inp={}, outp={}, desc={})>".format(self.func, self.plug, self.inp, self.outp, self.desc)
