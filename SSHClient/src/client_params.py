class ClientParams:

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
	def command(self):
		return self._command

	@command.setter
	def command(self, value):
		self._command = value

	@command.deleter
	def command(self):
		del self._command