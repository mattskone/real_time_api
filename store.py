from motor.motor_tornado import MotorClient
from tornado import gen

import settings


class StoreClient(object):

    def __init__(self):
        db = MotorClient(settings.mongodb).store
        self.collection = db.store_collection

    @gen.coroutine
    def get(self, key):
        result = yield self.collection.find_one({'key': key})
        return result['value'] if result else 'null'

    @gen.coroutine
    def set(self, key, value):
        result = yield self.collection.insert({'key': key, 'value': value})
        return 'ok'

