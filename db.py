#coding=utf-8

class _Engine(object):
	"""db engine for webapp"""
	def __init__(self, connect):
		self._connect = connect

	def connect(self):
		return self._connect

	def update(self,sql,*args):
		pass

	def select(self, sql, *args):
		pass

engine = None

class _DbCtx(threading.local):
	"""context for db connection"""
	def __init__(self):
		self.connection = None
		self.transaction = 0

	def is_init(self):
		return not self.connection is None

	def _LazyConnection():
		return None

	def init(self):
		self.connection = _LazyConnection()
		self.transaction = 0

	def cleanup(self):
		self.connection.cleanup()
		self.connection = None

	def cursor(self):
		return self.connection.cursor()



_db_ctx = _DbCtx()
		