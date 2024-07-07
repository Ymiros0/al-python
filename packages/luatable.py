from collections import UserDict
from typing import Any
from collections.abc import ItemsView
from functools import cmp_to_key
NOTHING = object()
IMPLEMENTED = {
	'__index':'get',
	'__newindex':'__setitem__'
	}
class table(UserDict):
	@staticmethod
	def _metatable(tab,method,*args):
		if not (meta := tab._meta):
			return
		if not (fallback := meta.get(method)):
			return
		if callable(fallback): return fallback(tab, *args)
		return getattr(fallback,IMPLEMENTED[method])(*args)
	
	def _sequential(self):
		return all(x == y for x, y in zip(self.keys(), range(len(self))))

	def __init__(self, *args, **kwargs):
		try: super().__init__(*args, **kwargs)
		except: super().__init__(enumerate(args))

	def __getattr__(self, __name: str) -> Any:
		if __name in ('data', '_meta'):
			return
		return self[__name]
	
	def __setattr__(self, __name: str, __value: Any) -> None:
		if __name in ('data', '_meta'):
			super().__setattr__(__name, __value)
		else:
			self[__name] = __value
	
	def __getitem__(self, key: Any) -> Any:
		if isinstance(key,float) and int(key) == key:
			key = int(key)
		if (ret := self.data.get(key)) is not None:
			return ret
		if type(key) == int and key < 0 and self._sequential():
			return self[len(self)+key]
		return self._metatable(self,'__index',key)
	
	def __setitem__(self, key: Any, item: Any) -> None:
		if key not in self and self._meta and '__newindex' in self._meta:
			self._metatable(self,'__newindex', key, item)
			return
		if item is None:
			self.data.pop(key, None)
			return
		if isinstance(key,float) and int(key) == key:
			key = int(key)
		self.data[key] = item
	
	def rawget(self, key):
		return self.data.get(key)
	
	def rawset(self, key, item):
		self.data[key] = item

	def update(self,other):
		try: return super().update(other)
		except TypeError:
			return self.extend(other)
		
	def ikeys(self) -> list:
		i = 0
		ret = []
		while i in self.data:
			ret.append(i)
			i += 1
		return ret
		
	def ivalues(self) -> list:
		i = 0
		ret = []
		while i in self.data:
			ret.append(self.data[i])
			i += 1
		return ret

	def iitems(self) -> list:
		i = 0
		ret = []
		while i in self.data:
			ret.append((i, self.data[i]))
			i += 1
		return ret
	
	def append(self,value):
		i = 0
		while i in self.data:
			i += 1
		self.data[i] = value
	
	def extend(self,liste:list):
		i = 0
		while i in self.data:
			i += 1
		self.update({k+i: v for k,v in enumerate(liste)})
	
	def pop(self, key=NOTHING, /, default=NOTHING):
		if key is not NOTHING:
			if default is NOTHING:
				return super().pop(key)
			return super().pop(key, default)
		last = self.ikeys()[-1]
		return self.pop(last)
	
	def contains(self, __value) -> bool:
		for v in self.values():
			if v == __value:
				return True
		return False
	
	def find(self, value):
		for k, v in self.items():
			if v == value:
				return k
		return None
	
	def removebyvalue(self,__value,all:bool=False):
		keys = []
		for k,v in self.items():
			if v == __value:
				if not all:
					self.remove(k)
					return 1
				keys.append(k)
		for k in keys:
			self.remove(k)
		return len(keys)

	def insert(self, v:Any, index:int = NOTHING):
		if index == NOTHING:
			self.append(v)
		else:
			self[index] = v
	
	def sort(self, func = lambda a, b: a - b):
		return sorted(self, key = lambda x: cmp_to_key(func)(self[x]))

	def concat(self, s:str) -> str:
		return s.join(str(v) for v in self.values())

def pairs(tab:table) -> ItemsView:
	return tab.items()

def ipairs(tab:table) -> list:
	return tab.iitems()

def Clone(tab:table) -> table:
	return table.copy()

def setmetatable(table,meta):
	table._meta = meta
	if x := [i for i in meta if i not in IMPLEMENTED]:
		print('Warning, these special funcs are not implemented:', x)
	return table

def getmetatable(table):
	return table._meta
