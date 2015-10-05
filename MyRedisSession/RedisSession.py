# -*- coding:utf-8 -*-
__author__ = 'Qian'

import hmac
import uuid
import hashlib
from MyDBUtils.yq_NoSQL import RedisDB



class SessionData(dict):
    def __init__(self, session_id, hmac_key):
        self.session_id = session_id
        self.hmac_key = hmac_key


class Session(SessionData):
    def __init__(self, session_manager, request_handler):
        self.session_manager = session_manager
        self.request_handler = request_handler
        try:
          # 正常是获取该 session 的所有数据，以 SessionData 的形式保存
          current_session = session_manager.get(request_handler)
        except InvalidSessionException:
          # 如果是第一次访问会抛出异常，异常的时候是获取了一个空的 SessionData 对象,里面没有数据，但包含新生成的
          # session_id 和 hmac_key
          current_session = session_manager.get()

        # 取出 current_session 中的数据，以键值对的形式迭代存下
        for key, data in current_session.iteritems():
          self[key] = data

        # 保存下 session_id
        self.session_id = current_session.session_id
        # 以及对应的 hmac_key
        self.hmac_key = current_session.hmac_key

  # 定义 save 方法，用于 session 修改后的保存，实际调用 session_manager 的 set 方法
    def save(self):
        self.session_manager.set(self.request_handler, self)

class SessionManager():
    def __init__(self, secret, session_timeout):
        self.secret = secret
        self.session_timeout = session_timeout

     # 生成 session_id
    def _generate_id(self):
        return ''.join(['SessionID:', uuid.uuid1().hex])

    # 生成 hmac_key
    def _generate_hmac(self, session_id):
        return hmac.new(session_id, self.secret, hashlib.sha256).hexdigest()

    # 该方法用 session_id 从 memcache 中取出数据
    def _fetch(self, session_id):
        try:
            # 连接 memcache 服务器
            # 获取数据
            r = RedisDB.RedisDBCache().get_alldata_HASH(session_id)

            session_data = raw_data = r['result']

            if r['error'] != None:
                return {}

            if raw_data != None:
              # 为了重新刷新 timeout
                #mc.replace(session_id, raw_data, self.session_timeout, 0)
              # 反序列化
                #session_data = pickle.loads(raw_data)
                RedisDB.RedisDBCache().set_data_expire(session_id, self.session_timeout)

            # 如果拿到的数据是字典形式，才进行返回
            if type(session_data) == type({}):
                return session_data
            else:
                return {}
        except IOError:
            return {}



    def get(self, request_handler = None):

        # 获取对应的 session_id 和 hmac_key
        if (request_handler == None):
            session_id = None
            hmac_key = None
        else:
            # session 的基础还是靠 cookie
            session_id = request_handler.get_secure_cookie("session_id")
            hmac_key = request_handler.get_secure_cookie("verification")

        # session_id 不存在的时候则生成一个新的 session_id 和 hmac_key
        if session_id == None:
            session_exists = False
            session_id = self._generate_id()
            hmac_key = self._generate_hmac(session_id)
        else:
            session_exists = True

        # 检查 hmac_key
        check_hmac = self._generate_hmac(session_id)
        # 不通过则抛出异常
        if hmac_key != check_hmac:
            raise InvalidSessionException()

        # 新建 SessionData 对象
        session = SessionData(session_id, hmac_key)

        if session_exists:
            # 通过 _fetch 方法获取 memcache 中该 session 的所有数据
            session_data = self._fetch(session_id)
            for key, data in session_data.iteritems():
              session[key] = data

        return session

    # 设置新的 session,需要设置 handler 的 cookie 和 memcache 客户端
    def set(self, request_handler, session):
        # 设置浏览器的 cookie
        request_handler.set_secure_cookie("session_id", session.session_id, expires_days=None)
        request_handler.set_secure_cookie("verification", session.hmac_key, expires_days=None)

        # 连接 memcache 服务器

        RedisDB.RedisDBCache().set_mdata_HASH(session.session_id, session)
        RedisDB.RedisDBCache().set_data_expire(session.session_id, self.session_timeout)

class InvalidSessionException(Exception):
    pass
