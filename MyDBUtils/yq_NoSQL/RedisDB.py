# -*- coding:utf-8 -*-
__author__ = 'Qian'

import redis

class RedisDBConfig:
    #HOST = '127.0.0.1'
    HOST = '115.159.90.211'
    PORT = 6379
    DBID = 6

def operator_status(func):
    '''get operatoration status
    '''
    def gen_status(*args, **kwargs):
        error, result = None, None
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            error = str(e)

        return {'result': result, 'error':  error}

    return gen_status

class RedisDBCache(object):
    def __init__(self):
        if not hasattr(RedisDBCache, 'pool'):
            RedisDBCache.create_pool()
        self._connection = redis.Redis(connection_pool = RedisDBCache.pool)

    @staticmethod
    def create_pool():
        RedisDBCache.pool = redis.ConnectionPool(
                host = RedisDBConfig.HOST,
                port = RedisDBConfig.PORT,
                db   = RedisDBConfig.DBID)

    # String操作
    @operator_status
    def set_data_STRING(self, key, value):
        '''set data with (key, value)
        '''
        return self._connection.set(key, value)

    @operator_status
    def get_data_STRING(self, key):
        '''get data by key
        '''
        return self._connection.get(key)

    @operator_status
    def del_data(self, key):
        '''delete cache by key
        '''
        return self._connection.delete(key)


    # Hash操作
    @operator_status
    def set_data_HASH(self, key, field, value):
        '''set data with hset( key, field, value)
        '''
        return self._connection.hset( key, field, value)

    @operator_status
    def set_mdata_HASH(self, key, mappings):
        '''set data with hset( key, field, value)
        '''
        return self._connection.hmset( key, mappings)

    @operator_status
    def get_data_HASH(self, key, field):
        '''get data by key
        '''
        return self._connection.hget( key, field)

    @operator_status
    def get_mdata_HASH(self, key, filedList):
        '''get data by key
        '''
        return self._connection.hmget( key, filedList)

    @operator_status
    def get_alldata_HASH(self, key):
        '''get data by key
        '''
        return self._connection.hgetall( key)

    @operator_status
    def del_data_HASH(self, key, filedList):
        '''delete cache by key
        '''
        return self._connection.hdel(key, filedList)

    # 设置生存期
    @operator_status
    def set_data_expire(self, key, lifeTime):
        '''delete cache by key
        unit:second
        '''
        return self._connection.expire( key, lifeTime)

    @operator_status
    def get_data_expire(self, key, lifeTime):
        '''delete cache by key
        '''
        return self._connection.ttl( key)



    def getRedisConnection(self):
        return self._connection











if __name__ == '__main__':
    import  uuid
    print RedisDBCache().set_mdata_HASH( 'yq', { '1': 'v1', '2': 'v2'})
    print RedisDBCache().set_mdata_HASH( ''.join(['SessionID:', uuid.uuid1().hex]), { '1': 'v1', '2': 'v2'})

    print RedisDBCache().set_data_expire('yq',60)
    r= RedisDBCache().get_alldata_HASH('yq')
    print r['result']
