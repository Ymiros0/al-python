from random import random, randint
import math
import re
from functools import singledispatch

from luatable import table, ipairs, pairs
from Vector3 import Vector3

def defaultValue(a,b):
	if a == None:
		return b
	return a

def randomb(a=None,b=None):
	if a is not None and b is not None:
		return randint(a,b)
	elif a is not None:
		return randint(1,a)
	else:
		return random()
math.random = randomb
math.min = min
math.max = max

def Random(a, b):
	return random() * (b-a) + a
math.Random = Random

def uuid():
	return re.sub("[xy]", 
			   lambda x: str(x.group() == "x" and math.random(0, 15) or math.random(8, 11)),
			   "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx")

def map(a,b,c,d,e):
	return (a-b) / (c-b) * (e-d) + d

def shuffle(a):
	for i in range(len(a), 1, -1):
		index = math.random(i) -1
		a[index], a[i] = a[i], a[index]

def sign(x):
	return (x>0)-(x<0)
math.sign = sign

def clamp(val, min, max):
	return min if val < min else max if val > max else val
math.clamp = clamp

def lerp(a,b,c):
	return a + (b-a) * clamp(c, 0, 1)
math.lerp = lerp

math.Repeat = lambda a, b: a - int(a/b) * b #This is just fucking modulo

math.LerpAngle = lambda a, b, c: a + (b-a-360) * clamp(c, 0, 1) if (b-a)%360 > 180 else a + (b-a) * clamp(c, 0, 1)

def MoveTowards(a, b, c):
	if abs(b-a) <= c:
		return b
	else:
		raise Exception("mathf unknown")
math.MoveTowards = MoveTowards

math.DeltaAngle = lambda a, b: b-a-360 if (b-a)%360 > 180 else b-a

math.MoveTowardsAngle = lambda a, b, c: MoveTowards(a, a + math.DeltaAngle(a, b), c)

math.Approximately = lambda a, b: abs(a-b) < max(1e-6*max(abs(a),abs(b)), 1.121039e-44)

def InverseLerp(a, b, c):
	if a < b:
		if c < a:
			return 0
		if b < c:
			return 1
		return (c-a)/(b-a)
	if a == b:
		return 0
	if c < b:
		return 1
	if a < c:
		return 0
	return 1 - (c-b)/(a-b)

math.PingPong = lambda a,b: b - abs(math.Repeat(a, b*2) - b)

def calcFloor(a):
	return int(a+1e-9)

def getCompareFuncByPunctuation(x):
	if not hasattr(math,'compareFuncList'):
		math.compareFuncList = table({
			"=": lambda a, b: a == b,
			"==": lambda a, b: a == b,
			">=": lambda a, b: a >= b,
			"<=": lambda a, b: a <= b,
			">": lambda a, b: a > b,
			"<": lambda a, b: a < b,
			"!=": lambda a, b: a != b,
			"~=": lambda a, b: a != b,
		})
	return math.compareFuncList[x]

def getArithmeticFuncByOperator(x):
	if not hasattr(math,'arithmeticFuncList'):
		math.arithmeticFuncList = table({
			"+": lambda a, b: a+b,
			"-": lambda a, b: a-b,
			"*": lambda a, b: a*b,
			"/": lambda a, b: a/b
		})
	return math.arithmeticFuncList[x]

Mathf = table()
def MultiRandom(slot0, slot1):
	slot2 = {}
	slot3 = {}

	for slot7, _ in ipairs(slot0):
		table.insert(slot3, slot7)

	slot1 = min(len(slot0), slot1)

	while slot1 > 0:
		table.insert(slot2, slot0[table.remove(slot3, math.random(len(slot3))-1)])

		slot1 = slot1 - 1

	return slot2
Mathf.MultiRandom = MultiRandom
Mathf.Deg2Rad = math.radians(1)

def _typeof(ct):
	return type(ct) #No clue, Creates a "ctype object for the given ct", guess this is to use C directly?
def _findtype(obj):
	return obj.__name__ #Weird cs lua interaction bs
typetable = table()
def typeof(obj):
	typ = 0
	if isinstance(obj, table):
		if obj not in typetable:
			ret = _typeof(obj)
	elif isinstance(obj, str):
		if obj not in typetable:
			ret = _findtype(obj)
	else:
		raise TypeError(f"Attempt to call typeof on object of type {type(obj)}")
	typetable[obj] = ret
	return ret


class GameObject:
	def Find():
		return GameObject()
	
	def GetComponent(self, comp):
		return comp

def intProperties(arg_22_0):
	for iter_22_0, iter_22_1 in pairs(arg_22_0):
		arg_22_0[iter_22_0] = calcFloor(iter_22_1)

	return arg_22_0	

def tonumber(obj):
	try:
		i = int(obj)
		f = float(obj)
		return i if i == f else f
	except:
		return None

@singledispatch
def tablify(ob):
	try: return table(tablify(i) for i in ob)
	except: return ob

@tablify.register
def _handle_dict(ob:dict):
	return table({k: tablify(v) for k,v in ob.items()})

@tablify.register
def _handle_string(ob:str):
	if function in ob:
		return ob
	if "Vector3(" in ob:
		nums = re.search(r'Vector3\(([^)])\)',ob).group(1).split(',')
		return Vector3(int(i) for i in nums)
	return ob


def time(timetable:table):
	import time
	timestring = f"{timetable.year} {timetable.month} {timetable.day} {timetable.hour or 12}:{timetable.minute or 0}:{timetable.second or 0}"
	timetuple = time.strptime(timestring, "%Y %m %d %H:%M:%S")
	return time.mktime(timetuple)

class string:

	def lower(s:str):
		return s.lower()
	
	def upper(s:str):
		return s.upper()

from functools import reduce
class bit:
	def lshift(b, num):
		return b << (num & 31)
	def rshift(b,num):
		return (b & 0xffffffff) >> num
	def arshift(b, num):
		return b >> (num & 31)
	def bor(*args):
		return reduce(lambda a,b: a | b, args)
	def band(*args):
		return reduce(lambda a,b: a & b, args)
	def bxor(*args):
		return reduce(lambda a,b: a ^ b, args)
	def bnot(b):
		return ~ b
	def ror(n,rotations):
		return 31&(n>>rotations|n<<(32-rotations))
	def rol(n,rotations):
		return 31&(n<<rotations|n>>(32-rotations))
	def tohex(b, n=8):
		return hex(b&(2**n-1))
	def bswap(b):
		int(f'{b:08b}'[::-1], 2)