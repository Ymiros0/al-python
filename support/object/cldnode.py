from Vector3 import Vector3

class CldNode:
	def __init__(self, arg_1_1=None):
		self.cylinder = False

	def UpdateBox(self, arg_2_1, arg_2_2, arg_2_3):
		self.min = arg_2_1.Copy2(self.min)
		self.max = arg_2_2.Copy2(self.max)

		if arg_2_3:
			self.min.Add(arg_2_3)
			self.max.Add(arg_2_3)

		return self

	def UpdateStaticBox(self, arg_3_1, arg_3_2):
		self.min = arg_3_1
		self.max = arg_3_2

		return self

	def UpdateCylinder(self, arg_4_1, arg_4_2, arg_4_3):
		if arg_4_3 < 0:
			arg_4_3 = -arg_4_3

		self.center = arg_4_1.Copy2(self.center)
		self.range = arg_4_3

		var_4_0 = Vector3(arg_4_3, arg_4_2, arg_4_3)

		self.min = arg_4_1 - var_4_0
		self.max = arg_4_1 + var_4_0
		self.cylinder = True

		return self
