from luatable import table, ipairs
from Vector3 import Vector3
from alsupport import math

from support.object.ColliderTree import ColliderTree

import BattleConst

OXY_STATE = BattleConst.OXY_STATE
BulletType = BattleConst.BulletType
import BattleAttr
class BattleCldSystem:
	__name = "BattleCldSystem"

	def __init__(self, arg_1_1):
		self._proxy = arg_1_1

		self.InitCldTree()

		self._friendlyCode = arg_1_1.GetFriendlyCode()
		self._foeCode = arg_1_1.GetFoeCode()

	def Dispose(self):
		self._proxy = None
		self._shipTree = None
		self._foeShipTree = None
		self._aircraftTree = None
		self._surfaceBulletTree = None
		self._airBulletTree = None
		self._bulletTreeList = None
		self._foeSurafceBulletTree = None
		self._foeAirbulletTree = None
		self._foeBulleetTreeList = None
		self._surfaceAOETree = None
		self._airAOETree = None
		self._AOETreeList = None
		self._wallTree = None

	def InitCldTree(self):
		var_3_0, var_3_1, var_3_2, var_3_3 = self._proxy.GetTotalBounds()
		var_3_4 = Vector3(var_3_2, 0, var_3_1)
		var_3_5 = Vector3(var_3_3, 0, var_3_0)

		self._shipTree = ColliderTree("shipTree", var_3_4, var_3_5, 2)
		self._foeShipTree = ColliderTree("foeShipTree", var_3_4, var_3_5, 2)
		self._aircraftTree = ColliderTree("aircraftTree", var_3_4, var_3_5, 2)
		self._surfaceBulletTree = ColliderTree("surfaceBullets", var_3_4, var_3_5, 4)
		self._airBulletTree = ColliderTree("airBullets", var_3_4, var_3_5, 3)
		self._bulletTreeList = {}
		self._bulletTreeList[BattleConst.BulletField.SURFACE] = self._surfaceBulletTree
		self._bulletTreeList[BattleConst.BulletField.AIR] = self._airBulletTree
		self._foeSurafceBulletTree = ColliderTree("foeSurfaceBullets", var_3_4, var_3_5, 3)
		self._foeAirbulletTree = ColliderTree("foeAirBullets", var_3_4, var_3_5, 3)
		self._foeBulleetTreeList = {}
		self._foeBulleetTreeList[BattleConst.BulletField.SURFACE] = self._foeSurafceBulletTree
		self._foeBulleetTreeList[BattleConst.BulletField.AIR] = self._foeAirbulletTree
		self._surfaceAOETree = ColliderTree("surfaceAOE", var_3_4, var_3_5, 2)
		self._airAOETree = ColliderTree("airAOE", var_3_4, var_3_5, 2)
		self._bulletAOETree = ColliderTree("bulletAOE", var_3_4, var_3_5, 2)
		self._AOETreeList = {}
		self._AOETreeList[BattleConst.AOEField.SURFACE] = self._surfaceAOETree
		self._AOETreeList[BattleConst.AOEField.AIR] = self._airAOETree
		self._AOETreeList[BattleConst.AOEField.BULLET] = self._bulletAOETree
		self._wallTree = ColliderTree("wall", var_3_4, var_3_5, 2)

	def UpdateShipCldTree(self, arg_4_1):
		var_4_0 = arg_4_1.GetSpeed()
		var_4_1 = arg_4_1.GetCldBox()
		var_4_2
		var_4_3 = not BattleAttr.IsUnitCldImmune(arg_4_1)

		if arg_4_1.GetIFF() == self._foeCode:
			if var_4_3:
				if arg_4_1.GetCldData().FriendlyCld:
					var_4_4 = self._foeShipTree.GetCldList(var_4_1, var_4_0)

					arg_4_1.GetCldData().distList = {}

					if len(var_4_4) > 1:
						self.HandleEnemyShipCld(var_4_4, arg_4_1)

				var_4_5 = self._shipTree.GetCldList(var_4_1, var_4_0)
				var_4_6 = self.surfaceFilterCount(arg_4_1, var_4_5)

				self._proxy.HandleShipCrashDecelerate(arg_4_1, var_4_6)
				self.HandlePlayerShipCld(var_4_5, arg_4_1)

			var_4_2 = self._foeShipTree
		elif arg_4_1.GetIFF() == self._friendlyCode:
			if var_4_3:
				var_4_7 = self._foeShipTree.GetCldList(var_4_1, var_4_0)
				var_4_8 = self.surfaceFilterCount(arg_4_1, var_4_7)

				self._proxy.HandleShipCrashDecelerate(arg_4_1, var_4_8)

			var_4_2 = self._shipTree

		var_4_2.Update(var_4_1)

	def HandlePlayerShipCld(self, arg_5_1, arg_5_2):
		var_5_0 = arg_5_2.GetCldData()

		if var_5_0.Active == False or var_5_0.ImmuneCLD == True:
			return

		var_5_1 = len(arg_5_1)
		var_5_2 = {}

		for iter_5_0 in range(var_5_1):
			var_5_3 = arg_5_1[iter_5_0].data

			if var_5_3.Active == False or var_5_3.ImmuneCLD == True:
				pass #block empty
			elif var_5_3.UID == arg_5_2.GetUniqueID():
				pass #block empty
			elif var_5_0.IFF == var_5_3.IFF:
				pass #block empty
			elif var_5_0.Surface != var_5_3.Surface:
				pass #block empty
			else:
				var_5_2.append(var_5_3.UID)

		self._proxy.HandleShipCrashDamageList(arg_5_2, var_5_2)

	def HandleEnemyShipCld(self, arg_6_1, arg_6_2):
		var_6_0 = arg_6_2.GetCldData()

		if var_6_0.Active == False or var_6_0.ImmuneCLD == True:
			return

		var_6_1 = arg_6_2.GetPosition()
		var_6_2 = {}
		var_6_3 = len(arg_6_1)

		for iter_6_0 in range(var_6_3):
			var_6_4 = arg_6_1[iter_6_0].data

			if var_6_4.Active == False or var_6_4.ImmuneCLD == True:
				pass #block empty
			elif var_6_4.UID == arg_6_2.GetUniqueID():
				pass #block empty
			elif var_6_0.IFF != var_6_4.IFF:
				pass #block empty
			elif not var_6_4.FriendlyCld:
				pass #block empty
			elif var_6_0.Surface != var_6_4.Surface:
				pass #block empty
			else:
				var_6_5 = var_6_1 - self.GetShip(var_6_4.UID).GetPosition()

				var_6_2.append(var_6_5)

		var_6_0.distList = var_6_2

	def surfaceFilterCount(self, arg_7_1):
		var_7_0 = self.GetCldData()
		var_7_1 = 0
		var_7_2 = len(arg_7_1)

		for iter_7_0 in range(1, var_7_2):
			var_7_3 = arg_7_1[iter_7_0].data

			if var_7_3.Active == True and var_7_3.ImmuneCLD == False and var_7_3.UID != self.GetUniqueID() and var_7_0.IFF != var_7_3.IFF and var_7_0.Surface == var_7_3.Surface:
				var_7_1 = var_7_1 + 1

		return var_7_1

	def UpdateAircraftCld(self, arg_8_1):
		var_8_0 = arg_8_1.GetSpeed()
		var_8_1 = arg_8_1.GetCldBox()
		var_8_2

		if arg_8_1.GetIFF() == self._foeCode:
			var_8_2 = self.GetBulletTree(BattleConst.BulletField.AIR)
		elif arg_8_1.GetIFF() == self._friendlyCode:
			var_8_2 = self.GetFoeBulletTree(BattleConst.BulletField.AIR)

		var_8_3 = var_8_2.GetCldList(var_8_1, var_8_0)

		self.HandleBulletCldWithAircraft(var_8_3, arg_8_1)
		self._aircraftTree.Update(arg_8_1.GetCldBox())

	def HandleBulletCldWithAircraft(self, arg_9_1, arg_9_2):
		var_9_0 = len(arg_9_1)

		for iter_9_0 in range(1, var_9_0):
			var_9_1 = arg_9_1[iter_9_0].data

			if var_9_1.type == BattleConst.CldType.BULLET and var_9_1.Active == True and var_9_1.ImmuneCLD == False:
				var_9_2 = self.GetBullet(var_9_1.UID)

				self._proxy.HandleBulletHit(var_9_2, arg_9_2)

	def UpdateBulletCld(self, arg_10_1):
		var_10_0 = arg_10_1.GetEffectField()
		var_10_1 = arg_10_1.GetCldBox()
		var_10_2 = arg_10_1.GetCldData().IFF

		if var_10_0 == BattleConst.BulletField.SURFACE:
			var_10_5 = var_10_2 == self._foeCode and self._shipTree or self._foeShipTree
			var_10_6 = self.getBulletCldShipList(arg_10_1, var_10_5)

			if arg_10_1.IsIndiscriminate():
				var_10_7 = var_10_5 == self._shipTree and self._foeShipTree or self._shipTree
				var_10_8 = self.getBulletCldShipList(arg_10_1, var_10_7)

				for iter_10_0, iter_10_1 in ipairs(var_10_8):
					table.insert(var_10_6, iter_10_1)

			self.HandleBulletCldWithShip(var_10_6, arg_10_1)

		if var_10_2 == self._friendlyCode:
			var_10_3 = self.GetBulletTree(var_10_0)
		elif var_10_2 == self._foeCode:
			var_10_3 = self.GetFoeBulletTree(var_10_0)

		var_10_3.Update(var_10_1)

	def getBulletCldShipList(self, arg_11_1, arg_11_2):
		var_11_0 = arg_11_1.GetCldBox()
		var_11_1

		if arg_11_1.GetType() == BattleConst.BulletType.SCALE:
			var_11_2, var_11_3, var_11_4 = arg_11_1.GetRadian()

			if math.abs(var_11_3) != 1:
				if arg_11_1.GetIFF() == -1:
					var_11_2 = var_11_2 + math.pi

				var_11_5 = arg_11_1.GetBoxSize()
				var_11_6 = var_11_5.x * 2
				var_11_7 = var_11_5.z * 2
				var_11_8 = arg_11_1.GetPosition()
				var_11_9 = var_11_5.x
				var_11_10 = var_11_9 * var_11_3
				var_11_11 = var_11_9 * var_11_4
				var_11_12 = Vector3(var_11_8.x - var_11_10, 1, var_11_8.z - var_11_11)

				var_11_1 = arg_11_2.GetCldListGradient(var_11_2, var_11_7, var_11_6, var_11_12)
			else:
				var_11_1 = arg_11_2.GetCldList(var_11_0, Vector3.zero)
		else:
			var_11_1 = arg_11_2.GetCldList(var_11_0, Vector3.zero)

		return var_11_1

	def HandleBulletCldWithShip(self, arg_12_1, arg_12_2):
		var_12_0 = len(arg_12_1)
		var_12_1 = arg_12_2.GetType()

		for iter_12_0 in range(1, var_12_0):
			var_12_2 = arg_12_1[iter_12_0].data

			if var_12_2.type == BattleConst.CldType.SHIP and var_12_2.Active == True and var_12_2.ImmuneCLD == False:
				var_12_3 = self.GetShip(var_12_2.UID)
				var_12_4 = var_12_3.GetCurrentOxyState()
				var_12_5 = var_12_3.IsImmuneCommonBulletCLD()

				if var_12_4 == OXY_STATE.DIVE and arg_12_2.GetCldData().Surface != BattleConst.OXY_STATE.DIVE:
					pass #block empty
				elif var_12_5:
					pass #block empty
				elif self._proxy.HandleBulletHit(arg_12_2, var_12_3):
					break

	def UpdateAOECld(self, arg_13_1):
		var_13_0 = arg_13_1.GetCldBox()
		var_13_1 = arg_13_1.GetFieldType()
		var_13_2 = arg_13_1.OpponentAffected()
		var_13_3 = arg_13_1.GetCldData().IFF
		var_13_4 = var_13_2 and var_13_3 * -1 or var_13_3

		if var_13_1 == BattleConst.AOEField.SURFACE:
			var_13_6 = arg_13_1.GetCldData().IFF == self._foeCode
			var_13_7 = arg_13_1.OpponentAffected() == var_13_6 and self._shipTree or self._foeShipTree
			var_13_8 = self.getAreaCldShipList(arg_13_1, var_13_7)

			if arg_13_1.GetIndiscriminate():
				var_13_9 = var_13_7 == self._shipTree and self._foeShipTree or self._shipTree
				var_13_10 = self.getAreaCldShipList(arg_13_1, var_13_9)

				for iter_13_0, iter_13_1 in ipairs(var_13_10):
					table.insert(var_13_8, iter_13_1)

			self.HandleAreaCldWithVehicle(arg_13_1, var_13_8)
		elif var_13_1 == BattleConst.AOEField.BULLET:
			var_13_11

			if var_13_4 == self._foeCode:
				var_13_11 = self._foeSurafceBulletTree
			else:
				var_13_11 = self._surfaceBulletTree

			var_13_12 = var_13_11.GetCldList(var_13_0, Vector3.zero)

			arg_13_1.ClearCLDList()
			self.HandleAreaCldWithBullet(arg_13_1, var_13_12)
		else:
			var_13_13 = {}
			var_13_14 = self._aircraftTree.GetCldList(var_13_0, Vector3.zero)

			for iter_13_2, iter_13_3 in ipairs(var_13_14):
				if iter_13_3.data.IFF == var_13_4:
					table.insert(var_13_13, iter_13_3)

			self.HandleAreaCldWithAircraft(arg_13_1, var_13_13)

	def getAreaCldShipList(self, arg_14_1, arg_14_2):
		var_14_0

		if arg_14_1.GetAreaType() == BattleConst.AreaType.COLUMN or arg_14_1.GetAnchorPointAlignment() == Vector3.zero:
			var_14_1 = arg_14_1.GetCldBox()

			var_14_0 = arg_14_2.GetCldList(var_14_1, Vector3.zero)
		else:
			var_14_2 = arg_14_1.GetCldData().IFF == self._foeCode
			var_14_3 = arg_14_1.GetAngle() * math.deg2Rad

			if var_14_2:
				var_14_3 = var_14_3 + math.pi

			var_14_4 = arg_14_1.GetWidth()
			var_14_5 = arg_14_1.GetHeight()
			var_14_6 = arg_14_1.GetPosition()

			var_14_0 = arg_14_2.GetCldListGradient(var_14_3, var_14_5, var_14_4, var_14_6)

		return var_14_0

	def HandleAreaCldWithVehicle(self, arg_15_1, arg_15_2):
		arg_15_1.ClearCLDList()

		var_15_0 = arg_15_1.GetCldData()
		var_15_1 = arg_15_1.OpponentAffected()
		var_15_2 = len(arg_15_2)

		for iter_15_0 in range(1, var_15_2):
			var_15_3 = arg_15_2[iter_15_0].data

			if var_15_3.Active == True and var_15_3.ImmuneCLD == False:
				var_15_4 = arg_15_1.GetDiveFilter()
				var_15_5 = self.GetShip(var_15_3.UID)
				var_15_6 = True

				if var_15_4:
					var_15_7 = var_15_5.GetCurrentOxyState()

					if table.contains(var_15_4, var_15_7):
						var_15_6 = False

				if var_15_6 and not arg_15_1.IsOutOfAngle(var_15_5):
					arg_15_1.AppendCldObj(var_15_3)

	def HandleAreaCldWithAircraft(self, arg_16_1, arg_16_2):
		arg_16_1.ClearCLDList()

		var_16_0 = arg_16_1.GetCldData()
		var_16_1 = arg_16_1.OpponentAffected()
		var_16_2 = len(arg_16_2)

		for iter_16_0 in range(1, var_16_2):
			var_16_3 = arg_16_2[iter_16_0].data

			if var_16_1 == (var_16_3.IFF != var_16_0.IFF):
				arg_16_1.AppendCldObj(var_16_3)

	def HandleAreaCldWithBullet(self, arg_17_1, arg_17_2):
		var_17_0 = len(arg_17_2)

		for iter_17_0 in range(1, var_17_0):
			var_17_1 = arg_17_2[iter_17_0].data

			arg_17_1.AppendCldObj(var_17_1)

	def UpdateWallCld(self, arg_18_1):
		var_18_0 = arg_18_1.GetCldBox()
		var_18_1 = arg_18_1.GetCldObjType()

		if var_18_1 == arg_18_1.CLD_OBJ_TYPE_BULLET:
			var_18_2

			if arg_18_1.GetIFF() == self._friendlyCode:
				var_18_2 = self._foeSurafceBulletTree.GetCldList(var_18_0, Vector3.zero)
			else:
				var_18_2 = self._surfaceBulletTree.GetCldList(var_18_0, Vector3.zero)

			self.HandleWallCldWithBullet(arg_18_1, var_18_2)
		elif var_18_1 == arg_18_1.CLD_OBJ_TYPE_SHIP:
			var_18_3

			if arg_18_1.GetIFF() == self._friendlyCode:
				var_18_3 = self._foeShipTree.GetCldList(var_18_0, Vector3.zero)
			else:
				var_18_3 = self._shipTree.GetCldList(var_18_0, Vector3.zero)

			self.HandleWllCldWithShip(arg_18_1, var_18_3)

	def HandleWallCldWithBullet(self, arg_19_1, arg_19_2):
		var_19_0 = len(arg_19_2)

		for iter_19_0 in range(1, var_19_0):
			var_19_1 = arg_19_2[iter_19_0].data

			if var_19_1.type == BattleConst.CldType.BULLET and var_19_1.Active == True and var_19_1.ImmuneCLD == False:
				var_19_2 = self.GetBullet(var_19_1.UID)

				if not self._proxy.HandleWallHitByBullet(arg_19_1, var_19_2):
					return

	def HandleWllCldWithShip(self, arg_20_1, arg_20_2):
		var_20_0 = len(arg_20_2)
		var_20_1 = {}

		for iter_20_0 in range(1, var_20_0):
			var_20_2 = arg_20_2[iter_20_0].data

			if var_20_2.type == BattleConst.CldType.SHIP and var_20_2.Active == True and var_20_2.ImmuneCLD == False:
				var_20_3 = self.GetShip(var_20_2.UID)

				if var_20_3.GetCurrentOxyState() == OXY_STATE.DIVE:
					pass #block empty
				else:
					table.insert(var_20_1, var_20_3)

		self._proxy.HandleWallHitByShip(arg_20_1, var_20_1)

	def InsertToBulletCldTree(self, arg_21_1, arg_21_2):
		var_21_0
		var_21_1 = arg_21_2.GetCldData()

		if var_21_1.IFF == self._foeCode:
			var_21_0 = self.GetFoeBulletTree(arg_21_1)
		elif var_21_1.IFF == self._friendlyCode:
			var_21_0 = self.GetBulletTree(arg_21_1)

		var_21_2 = arg_21_2.GetCldBox()

		var_21_0.Insert(var_21_2)

	def InsertToAOECldTree(self, arg_22_1, arg_22_2):
		var_22_0 = self.GetAOETree(arg_22_1)
		var_22_1 = arg_22_2.GetCldBox()

		var_22_0.Insert(var_22_1)

	def InsertToWallCldTree(self, arg_23_1):
		var_23_0 = self.GetWallTree()
		var_23_1 = arg_23_1.GetCldBox()

		var_23_0.Insert(var_23_1)

	def InsertToShipCldTree(self, arg_24_1):
		var_24_0 = arg_24_1.GetCldData()
		var_24_1

		if var_24_0.IFF == self._foeCode:
			var_24_1 = self.GetFoeShipTree()
		elif var_24_0.IFF == self._friendlyCode:
			var_24_1 = self.GetShipTree()

		var_24_2 = arg_24_1.GetCldBox()

		var_24_1.Insert(var_24_2)

	def InsertToAircraftCldTree(self, arg_25_1):
		var_25_0 = arg_25_1.GetCldBox()

		self._aircraftTree.Insert(var_25_0)

	def GetBulletTree(self, arg_26_1):
		return self._bulletTreeList[arg_26_1]

	def GetFoeBulletTree(self, arg_27_1):
		return self._foeBulleetTreeList[arg_27_1]

	def GetAOETree(self, arg_28_1):
		return self._AOETreeList[arg_28_1]

	def GetWallTree(self, arg_29_1):
		return self._wallTree

	def GetShipTree(self):
		return self._shipTree

	def GetFoeShipTree(self):
		return self._foeShipTree

	def GetAircraftTree(self):
		return self._aircraftTree

	def DeleteShipLeaf(self, arg_33_1):
		var_33_0 = arg_33_1.GetCldData().IFF

		if var_33_0 == self._foeCode:
			self.DeleteCldLeaf(self.GetFoeShipTree(), arg_33_1)
		elif var_33_0 == self._friendlyCode:
			self.DeleteCldLeaf(self.GetShipTree(), arg_33_1)

	def DeleteBulletLeaf(self, arg_34_1):
		var_34_0 = arg_34_1.GetCldData().IFF

		if var_34_0 == self._foeCode:
			self.DeleteCldLeaf(self.GetFoeBulletTree(arg_34_1.GetEffectField()), arg_34_1)
		elif var_34_0 == self._friendlyCode:
			self.DeleteCldLeaf(self.GetBulletTree(arg_34_1.GetEffectField()), arg_34_1)

	def DeleteCldLeaf(self, arg_35_1):
		var_35_0 = arg_35_1.GetCldBox()

		self.Remove(var_35_0)

	def GetShip(self, arg_36_1):
		return self._proxy.GetUnitList()[arg_36_1]

	def GetAircraft(self, arg_37_1):
		return self._proxy.GetAircraftList()[arg_37_1]

	def GetBullet(self, arg_38_1):
		return self._proxy.GetBulletList()[arg_38_1]

	def GetAOE(self, arg_39_1):
		return self._proxy.GetAOEList()[arg_39_1]

	def InitShipCld(self, arg_40_1):
		self.InsertToShipCldTree(arg_40_1)

	def DeleteShipCld(self, arg_41_1):
		arg_41_1.DeactiveCldBox()
		self.DeleteShipLeaf(arg_41_1)

	def InitAircraftCld(self, arg_42_1):
		self.InsertToAircraftCldTree(arg_42_1)

	def DeleteAircraftCld(self, arg_43_1):
		arg_43_1.DeactiveCldBox()
		self.DeleteCldLeaf(self.GetAircraftTree(), arg_43_1)

	def InitBulletCld(self, arg_44_1):
		self.InsertToBulletCldTree(arg_44_1.GetEffectField(), arg_44_1)

	def DeleteBulletCld(self, arg_45_1):
		arg_45_1.DeactiveCldBox()
		self.DeleteBulletLeaf(arg_45_1)

	def ShiftBulletCld(self, arg_46_1):
		return

	def InitAOECld(self, arg_47_1):
		self.InsertToAOECldTree(arg_47_1.GetFieldType(), arg_47_1)

	def DeleteAOECld(self, arg_48_1):
		arg_48_1.DeactiveCldBox()
		self.DeleteCldLeaf(self.GetAOETree(arg_48_1.GetFieldType()), arg_48_1)

	def InitWallCld(self, arg_49_1):
		self.InsertToWallCldTree(arg_49_1)

	def DeleteWallCld(self, arg_50_1):
		arg_50_1.DeactiveCldBox()

		var_50_0 = self.GetWallTree()

		if var_50_0:
			self.DeleteCldLeaf(var_50_0, arg_50_1)
