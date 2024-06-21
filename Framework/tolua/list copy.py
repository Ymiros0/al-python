from luatable import table, setmetatable

class allist:
	def __init__(self):
		node = table(
			_next = 0,
			length = 0,
			_prev = 0
		)

		node._prev = node
		node._next = node

		return setmetatable(node, self)

	def clear(self):
		self._next = self
		self._prev = self
		self.length = 0

	def push(self, elem):
		node = table(
			_prev = 0,
			_next = 0,
			removed = False,
			value = elem
		)

		self._prev._next = node
		node._next = self
		node._prev = self._prev
		self._prev = node
		self.length += 1

		return node

	def pushnode(self, node):
		if not node.removed:
			return

		self._prev._next = node
		node._next = self
		node._prev = self._prev
		self._prev = node
		node.removed = False
		self.length += 1

	def pop(self):
		node = self._prev

		self.remove(node)

		return node.value

	def unshift(self, value):
		node = table(
			_prev = 0,
			_next = 0,
			removed = False,
			value = value
		)

		self._next._prev = node
		node._prev = self
		node._next = self._next
		self._next = node
		self.length += 1

		return node

	def shift(self):
		node = self._next

		self.remove(node)

		return node.value

	def remove(self, node):
		if node.removed:
			return

		prev = node._prev
		next = node._next

		next._prev = prev
		prev._next = next
		self.length = max(0, self.length - 1)
		node.removed = True

	def find(self, value, start=None):
		start = start or self

		while True:
			if value == start.value:
				return start
			start = start._next
			if start == self:
				return None

	def findlast(self, value, start):
		start = start or self

		while True:
			if value == start.value:
				return start

			start = start._prev
			if start == self:
				return None

	def next(self, arg_11_1):
		var_11_0 = arg_11_1._next

		if var_11_0 != self:
			return var_11_0, var_11_0.value

		return None

	def prev(self, arg_12_1):
		var_12_0 = arg_12_1._prev

		if var_12_0 != self:
			return var_12_0, var_12_0.value

		return None

	def erase(arg_13_0, arg_13_1):
		var_13_0 = arg_13_0.find(arg_13_1)

		if var_13_0:
			arg_13_0.remove(var_13_0)

	def insert(self, arg_14_1, arg_14_2):
		if not arg_14_2:
			return self.push(arg_14_1)

		var_14_0 = table(
			_prev = 0,
			_next = 0,
			removed = False,
			value = arg_14_1
		)

		if arg_14_2._next:
			arg_14_2._next._prev = var_14_0
			var_14_0._next = arg_14_2._next
		else:
			self.last = var_14_0

		var_14_0._prev = arg_14_2
		arg_14_2._next = var_14_0
		self.length += 1

		return var_14_0

	def head(self):
		return self._next.value

	def tail(self):
		return self._prev.value

	def clone(self):
		copy = allist()

		for iter_17_0, iter_17_1 in allist.next, self, self:
			copy.push(iter_17_1)

		return copy

def ilist(arg_18_0):
	return allist.next, arg_18_0, arg_18_0

def rilist(arg_19_0):
	return allist.prev, arg_19_0, arg_19_0




