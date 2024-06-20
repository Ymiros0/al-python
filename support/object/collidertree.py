from Vector3 import Vector3
from luatable import table, ipairs, pairs
from alsupport import math

from CldNode import CldNode

class CldArea:
	def __init__(self, arg_1_1, arg_1_2, arg_1_3):
		self.min = arg_1_1
		self.max = arg_1_2
		self.center = (arg_1_1 + arg_1_2).Mul(0.5)
		self.father = arg_1_3

		if arg_1_3:
			self.level = arg_1_3.level + 1
		else:
			self.level = 1

		self.isLeaf = True
		self.childs = {}
		self.nodes = {}

	def AddNode(self, arg_2_1):
		table.insert(self.nodes, arg_2_1)

		arg_2_1.area = self

	def InArea(self, arg_3_1, arg_3_2):
		if arg_3_1.x < self.min.x or arg_3_1.y < self.min.y:
			return False

		if arg_3_2.x > self.max.x or arg_3_2.y > self.max.y:
			return False

		return True

	def GetAreaIndex(self, arg_4_1, arg_4_2):
		var_4_0 = self.center
		var_4_1 = arg_4_1.x >= var_4_0.x and 0 or 2
		var_4_2 = arg_4_2.x >= var_4_0.x and 0 or 2

		if var_4_1 != var_4_2:
			return 0

		var_4_3 = var_4_1 + (arg_4_1.z >= var_4_0.z and 1 or 2)

		return var_4_3 == var_4_2 + (arg_4_2.z >= var_4_0.z and 1 or 2) and var_4_3 or 0

class ColliderTree:
	MaxLayer = 3

	def __init__(self, arg_5_1:str, arg_5_2:Vector3, arg_5_3:Vector3, arg_5_4:int):
		self.name = arg_5_1
		self.root = CldArea.New(arg_5_2, arg_5_3, None)
		self.MaxLayer = arg_5_4
		self.cldStack = {}

	def Insert(self, arg_6_1):
		var_6_0 = arg_6_1.area

		if var_6_0:
			table.removebyvalue(var_6_0.nodes, arg_6_1)

		self._insert(arg_6_1, self._findParent(arg_6_1, self.root))

	def _findParent(self, arg_7_1, arg_7_2):
		var_7_0 = arg_7_1.min
		var_7_1 = arg_7_1.max
		
		while not arg_7_2.isLeaf:
			var_7_3 = arg_7_2.GetAreaIndex(var_7_0, var_7_1)

			if var_7_3 < 1:
				break

			arg_7_2 = arg_7_2.childs[var_7_3]

		return arg_7_2

	def _insert(self, arg_8_1, arg_8_2):
		if not arg_8_2.isLeaf or len(arg_8_2.nodes) < 6 or arg_8_2.level >= self.MaxLayer:
			arg_8_2.AddNode(arg_8_1)

			return

		arg_8_2.isLeaf = False

		var_8_1 = arg_8_2.center
		var_8_2 = arg_8_2.max
		var_8_3 = arg_8_2.min

		arg_8_2.childs[1] = CldArea.New(var_8_1, var_8_2, arg_8_2)
		arg_8_2.childs[2] = CldArea.New(Vector3(var_8_1.x, 0, var_8_3.z), Vector3(var_8_2.x, 0, var_8_1.z), arg_8_2)
		arg_8_2.childs[3] = CldArea.New(Vector3(var_8_3.x, 0, var_8_1.z), Vector3(var_8_1.x, 0, var_8_2.z), arg_8_2)
		arg_8_2.childs[4] = CldArea.New(var_8_3, var_8_1, arg_8_2)

		for iter_8_0 in range(len(arg_8_2.nodes), 1, -1):
			var_8_4 = arg_8_2.nodes[iter_8_0]
			var_8_5 = arg_8_2.GetAreaIndex(var_8_4.min, var_8_4.max)

			if var_8_5 > 0:
				arg_8_2.childs[var_8_5].AddNode(var_8_4)
				table.remove(arg_8_2.nodes, iter_8_0)

		var_8_6 = arg_8_2.GetAreaIndex(arg_8_1.min, arg_8_1.max)

		if var_8_6 > 0:
			arg_8_2.childs[var_8_6].AddNode(arg_8_1)
		else:
			arg_8_2.AddNode(arg_8_1)

	def Update(self, arg_9_1):
		var_9_0 = arg_9_1.area

		if var_9_0 == None:
			return

		var_9_1 = arg_9_1.min
		var_9_2 = arg_9_1.max

		while var_9_0.father:
			if var_9_0.InArea(var_9_1, var_9_2):
				break

			var_9_0 = var_9_0.father

		var_9_3 = self._findParent(arg_9_1, var_9_0)

		if var_9_3 != arg_9_1.area:
			table.removebyvalue(arg_9_1.area.nodes, arg_9_1)
			self._insert(arg_9_1, var_9_3)

	def Remove(self, arg_10_1):
		var_10_0 = arg_10_1.area

		if not var_10_0:
			return

		table.removebyvalue(var_10_0.nodes, arg_10_1)

		arg_10_1.area = None

	def Intersect(self, arg_11_1, arg_11_2, arg_11_3):
		return self.x <= arg_11_3.x and arg_11_1.x >= arg_11_2.x and self.z <= arg_11_3.z and arg_11_1.z >= arg_11_2.z

	def CylinderCheck(self, arg_12_1):
		if not self.cylinder and not arg_12_1.cylinder:
			return True

		if self.cylinder and arg_12_1.cylinder:
			var_12_0 = self.center.x - arg_12_1.center.x
			var_12_1 = self.center.z - arg_12_1.center.z
			var_12_2 = self.range + arg_12_1.range

			return var_12_0 * var_12_0 + var_12_1 * var_12_1 <= var_12_2 * var_12_2

		var_12_3 = self.cylinder and self or arg_12_1
		var_12_4 = var_12_3.range
		var_12_5 = var_12_3.center.x
		var_12_6 = var_12_3.center.z
		var_12_7 = self.cylinder and arg_12_1 or self

		if var_12_5 >= var_12_7.min.x and var_12_5 <= var_12_7.max.x:
			return var_12_6 >= var_12_7.min.z - var_12_4 and var_12_6 <= var_12_7.max.z + var_12_4
		elif var_12_6 >= var_12_7.min.z and var_12_6 <= var_12_7.max.z:
			return var_12_5 >= var_12_7.min.x - var_12_4 and var_12_5 <= var_12_7.max.x + var_12_4
		else:
			var_12_8
			var_12_9

			if var_12_5 < var_12_7.min.x:
				var_12_8 = var_12_7.min.x - var_12_5
			else:
				var_12_8 = var_12_7.max.x - var_12_5

			if var_12_6 < var_12_7.min.z:
				var_12_9 = var_12_7.min.z - var_12_6
			else:
				var_12_9 = var_12_7.max.z - var_12_6

			return var_12_8 * var_12_8 + var_12_9 * var_12_9 < var_12_4 * var_12_4

	def getTime(self, arg_13_1, arg_13_2):
		var_13_0 = 0

		if arg_13_2.x != 0:
			var_13_0 = max(0, (max(self.min.x, arg_13_1.min.x) - min(self.max.x, arg_13_1.max.x)) / arg_13_2.x)

		if arg_13_2.z != 0:
			var_13_0 = max(var_13_0, (max(self.min.z, arg_13_1.min.z) - min(self.max.z, arg_13_1.max.z)) / arg_13_2.z)

		return var_13_0

	def GetCldList(self, arg_14_1, arg_14_2):
		var_14_0 = arg_14_1.min
		var_14_1 = arg_14_1.max
		var_14_3 = self.root
		var_14_4 = {}

		while not var_14_3.isLeaf:
			var_14_5 = var_14_3.GetAreaIndex(var_14_0, var_14_1)

			if var_14_5 < 1:
				break

			for iter_14_0, iter_14_1 in ipairs(var_14_3.nodes):
				if self.Intersect(iter_14_1.min, iter_14_1.max, var_14_0, var_14_1) and self.CylinderCheck(arg_14_1, iter_14_1):
					table.insert(var_14_4, iter_14_1)

			var_14_3 = var_14_3.childs[var_14_5]

		var_14_6 = self.cldStack

		table.insert(var_14_6, var_14_3)

		while var_14_6:
			var_14_7 = table.remove(var_14_6)

			for iter_14_2, iter_14_3 in ipairs(var_14_7.nodes):
				if self.Intersect(iter_14_3.min, iter_14_3.max, var_14_0, var_14_1) and self.CylinderCheck(arg_14_1, iter_14_3):
					table.insert(var_14_4, iter_14_3)

			for iter_14_4, iter_14_5 in pairs(var_14_7.childs):
				if iter_14_5 != None and self.Intersect(iter_14_5.min, iter_14_5.max, var_14_0, var_14_1):
					table.insert(var_14_6, iter_14_5)

		return var_14_4

	def GetCldListGradient(self, arg_15_1, arg_15_2, arg_15_3, arg_15_4):
		var_15_0 = Vector3(math.cos(arg_15_1), 0, math.sin(arg_15_1))
		var_15_1 = Vector3.Cross(var_15_0, Vector3.up)
		var_15_2 = table(
			arg_15_4 + var_15_1 * (arg_15_2 * -0.5),
			arg_15_4 + var_15_1 * (arg_15_2 * 0.5),
			3,
			4
		)
		var_15_3 = var_15_0 * arg_15_3

		var_15_2[3] = var_15_2[2] + var_15_3
		var_15_2[4] = var_15_2[1] + var_15_3

		var_15_4 = CldNode()
		var_15_5 = Vector3(min(var_15_2[1].x, var_15_2[2].x, var_15_2[3].x, var_15_2[4].x), 0, min(var_15_2[1].z, var_15_2[2].z, var_15_2[3].z, var_15_2[4].z))
		var_15_6 = Vector3(max(var_15_2[1].x, var_15_2[2].x, var_15_2[3].x, var_15_2[4].x), 0, max(var_15_2[1].z, var_15_2[2].z, var_15_2[3].z, var_15_2[4].z))

		var_15_4.UpdateStaticBox(var_15_5, var_15_6)

		var_15_7 = self.GetCldList(var_15_4, None)
		var_15_8 = var_15_0.x * var_15_0.z

		if var_15_8 == 0:
			return var_15_7

		var_15_9
		var_15_10
		var_15_11
		var_15_12

		for iter_15_0 in range(len(var_15_7), 1, -1):
			var_15_13 = var_15_7[iter_15_0]

			if var_15_8 > 0:
				var_15_9 = var_15_13.min
				var_15_10 = var_15_13.max
				var_15_11 = Vector3(var_15_9.x, 0, var_15_10.z)
				var_15_12 = Vector3(var_15_10.x, 0, var_15_9.z)
			else:
				var_15_11 = var_15_13.min
				var_15_12 = var_15_13.max
				var_15_9 = Vector3(var_15_11.x, 0, var_15_12.z)
				var_15_10 = Vector3(var_15_12.x, 0, var_15_11.z)

			var_15_14 = Vector3.Dot(var_15_0, var_15_9 - var_15_2[1])
			var_15_15 = Vector3.Dot(var_15_0, var_15_10 - var_15_2[1])

			if var_15_14 < 0 and var_15_15 < 0 or arg_15_3 < var_15_14 and arg_15_3 < var_15_15:
				table.remove(var_15_7, iter_15_0)
				break

			var_15_16 = Vector3.Dot(var_15_1, var_15_11 - var_15_2[1])
			var_15_17 = Vector3.Dot(var_15_1, var_15_12 - var_15_2[1])

			if var_15_16 < 0 and var_15_17 < 0 or arg_15_2 < var_15_16 and arg_15_2 < var_15_17:
				table.remove(var_15_7, iter_15_0)

		return var_15_7
