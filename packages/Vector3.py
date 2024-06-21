import numpy as np
import quaternion
import math

class Vector3:
	quat = np.quaternion
	def __init__(self, x, y, z):
		self.x, self.y, self.z = x, y, z

	def __array__(self, dtype=None):
		if dtype:
			return np.array([self.x, self.y, self.z], dtype=dtype)
		else:
			return np.array([self.x, self.y, self.z])
	
	def __add__(self,other):
		return Vector3(*np.add(self,other))
	
	def __mul__(self,other):
		if type(other) == Vector3:
			return np.inner(self,other)
		elif type(other) == self.quat:
			return self.MulQuat(other)
		else:
			return Vector3(*self.__array__() * other)
		
	def __rmul__(self, other):
		return self.__mul__(other)
	
	def __eq__(self,other):
		return (self-other).EqualZero()
	
	def __neg__(self):
		return Vector3(-self.x, -self.y, -self.z)
	
	def __sub__(self,other):
		return self + -other
	
	def __str__(self):
		return f"Vector3({self.x}, {self.y}, {self.z})"
	
	def __repr__(self):
		return self.__str__()
	
	def __truediv__(self,other):
		return Vector3(*self.__array__() / other)
	
	def Cross(self,other):
		return Vector3(*np.cross(self,other))
	
	def Distance(self, other):
		return self.SqrDistance(other)**0.5
	
	def BattleDistance(self,other):
		return ((self.x-other.x)**2+(self.z-other.z)**2)**0.5
	
	def SqrDistance(self,other):
		return (self.x-other.x)**2+(self.y-other.y)**2+(self.z-other.z)**2
	
	def Lerp(self, other, factor):
		factor = 0 if factor < 0 else 1 if factor > 1 else factor
		return self+(other-self)*factor
	
	def Magnitude(self):
		return (self*self)**0.5
	
	def Normalize(self):
		mag = self.Magnitude()
		return self/mag if mag > 1e-5 else Vector3(0,0,0)
	
	def SetNormalize(self):
		self = self.Normalize()
	
	def Copy(self):
		return Vector3(self.x, self.y, self.z)
	
	def Angle(self, other):
		return math.acos(self.Normalize()*other.Normalize())
	
	def ClampMagnitude(self,length):
		if self*self > length*length:
			self = self.SetNormalize()*length
		return self
	
	def OrthoNormalize(self,other,what=None):
		self.SetNormalize()
		other -= other.Project(self)
		other.SetNormalize()

		if what is None:
			return self, other
		
		what -= what.Project(self)
		what -= what.Project(other)
		what.SetNormalize()

		return self, other, what

	def MoveTowards(self, target, maxDistanceDelta):
		direction = target-self

		sqrMagnitude = direction.sqrMagnitude()

		if sqrMagnitude > maxDistanceDelta**2:
			magnitude = sqrt(sqrMagnitude)

			if magnitude > 1e-06:
				direction *= (maxDistanceDelta / magnitude)
				direction += self
				return direction
			else:
				return self.clone()

		return target.clone()
	
	def ClampedMove(current, target, max_distance_delta): #Does this even work ingame?
		direction = target - current

		if direction > 0:
			return current + direction.ClampMagnitude(max_distance_delta)
		else:
			return current - -direction.ClampMagnitude(max_distance_delta)
		
	#slot21????
		
	def RotateTowards(self,a,b,c):
		pass

	def EqualZero(self):
		return self*self < 1e-10
	
	def MulQuat(self,quater):
		slot2 = quater.x * 2
		slot3 = quater.y * 2
		slot4 = quater.z * 2
		slot5 = quater.x * slot2
		slot6 = quater.y * slot3
		slot7 = quater.z * slot4
		slot8 = quater.x * slot3
		slot9 = quater.x * slot4
		slot10 = quater.y * slot4
		slot11 = quater.w * slot2
		slot12 = quater.w * slot3
		slot13 = quater.w * slot4

		ret = Vector3(
				(1 - (slot6 + slot7)) * self.x + (slot8 - slot13) * self.y + (slot9 + slot12) * self.z,
				(slot8 + slot13) * self.x + (1 - (slot5 + slot7)) * self.y + (slot10 - slot11) * self.z,
				(slot9 - slot12) * self.x + (slot10 + slot11) * self.y + (1 - (slot5 + slot6)) * self.z
			)

		return ret

Vector3.right = Vector3(1,0,0)
Vector3.forward = Vector3(0,0,1)
Vector3.up = Vector3(0,1,0)

class Vector2:
	def __init__(self, x, y):
		self.x, self.y = x, y

	def __array__(self, dtype=None):
		if dtype:
			return np.array([self.x, self.y], dtype=dtype)
		else:
			return np.array([self.x, self.y])
	
	def __add__(self,other):
		return Vector2(*np.add(self,other))
	
	def __mul__(self,other):
		if type(other) == Vector2:
			return np.inner(self,other)
		else:
			return Vector2(*self.__array__() * other)
		
	def __rmul__(self, other):
		return self.__mul__(other)
	
	def __eq__(self,other):
		return (self-other).EqualZero()
	
	def __neg__(self):
		return Vector2(-self.x, -self.y)
	
	def __sub__(self,other):
		return self + -other
	
	def __str__(self):
		return f"Vector2({self.x}, {self.y})"
	
	def __repr__(self):
		return self.__str__()
	
	def __truediv__(self,other):
		return Vector2(*self.__array__() / other)
	
	def Distance(self, other):
		return self.SqrDistance(other)**0.5
	
	def SqrDistance(self,other):
		return (self.x-other.x)**2+(self.y-other.y)**2
	
	def Lerp(self, other, factor):
		factor = 0 if factor < 0 else 1 if factor > 1 else factor
		return self+(other-self)*factor
	
	def Magnitude(self):
		return (self*self)**0.5
	
	def Normalize(self):
		mag = self.Magnitude()
		return self/mag if mag > 1e-5 else Vector2(0,0)
	
	def SetNormalize(self):
		self = self.Normalize()
	
	def Copy(self):
		return Vector2(self.x, self.y)
	
	def Angle(self, other):
		return math.acos(self.Normalize()*other.Normalize())
	
	def ClampMagnitude(self,length):
		if self*self > length*length:
			self = self.Normalize()*length
		return self
	
	def OrthoNormalize(self,other,what=None):
		self.SetNormalize()
		other -= other.Project(self)
		other.SetNormalize()

		if what is None:
			return self, other
		
		what -= what.Project(self)
		what -= what.Project(other)
		what.SetNormalize()

		return self, other, what

	def MoveTowards(self, target, maxDistanceDelta):
		direction = target-self

		sqrMagnitude = direction.sqrMagnitude()

		if sqrMagnitude > maxDistanceDelta**2:
			magnitude = sqrt(sqrMagnitude)

			if magnitude > 1e-06:
				direction *= (maxDistanceDelta / magnitude)
				direction += self
				return direction
			else:
				return self.clone()

		return target.clone()
	
	def ClampedMove(current, target, max_distance_delta): #Does this even work ingame?
		direction = target - current

		if direction > 0:
			return current + direction.ClampMagnitude(max_distance_delta)
		else:
			return current - -direction.ClampMagnitude(max_distance_delta)
		
	#slot21????
		
	def RotateTowards(self,a,b,c):
		pass

	def EqualZero(self):
		return self*self < 1e-10