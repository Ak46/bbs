from flask_sqlalchemy import SQLAlchemy
import time


db = SQLAlchemy()


class ReprMixin(object):
    def __repr__(self):
        class_name = self.__class__.__name__
        properties = ('{0} = {1}'.format(k, v) for k, v in self.__dict__.items())
        return '<{0}: \n  {1}\n>'.format(class_name, '\n  '.join(properties))

    @classmethod
    def delete(cls, model_id):
        m = cls.query.get(model_id)
        m.remove()

    @classmethod
    def new(cls, form):
        m = cls(form)
        m.save()
        return m

    def save(self):
        db.session.add(self)
        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()


def utctime():
    utc = int(time.time())
    return utc

# %Y-%m-%d %H-%M-%S
def data_time():
    format = '%Y-%m-%d %H:%M'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    return dt

# a = data_time()
# print(a)
