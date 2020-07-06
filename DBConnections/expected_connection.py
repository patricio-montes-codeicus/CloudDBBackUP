class ExpectedConnection:

	"""	def __init__(self, typehost, host, port, username, password, database):
		self.typehost = typehost
		self.host = host
		self.port = port
		self.username = username
		self.password = password
		self.database = database
	"""

	@property
	def typehost(self):
		return self._typehost

	@typehost.setter
	def typehost(self, value):
		self._typehost = value

	@typehost.deleter
	def typehost(self):
		del self._typehost

	@property
	def host(self):
		return self._host

	@host.setter
	def host(self, value):
		self._host = value

	@host.deleter
	def host(self):
		del self._host

	@property
	def port(self):
		return self._port

	@port.setter
	def port(self, value):
		self._port = value

	@port.deleter
	def port(self):
		del self._port

	@property
	def username(self):
		return self._username

	@username.setter
	def username(self, value):
		self._username = value

	@username.deleter
	def username(self):
		del self._username

	@property
	def password(self):
		return self._password

	@password.setter
	def password(self, value):
		self._password = value

	@password.deleter
	def password(self):
		del self._password

	@property
	def database(self):
		return self._database

	@database.setter
	def database(self, value):
		self._database = value

	@database.deleter
	def database(self):
		del self._database


	def get_db_type(self, id_type):
		if id_type == 1:
			return "SQL"
		if id_type == 2:
			return "ASE"




