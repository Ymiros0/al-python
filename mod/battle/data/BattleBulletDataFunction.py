from luatable import table

import ys
import pg

import BattleDataFunction
BattleConst = ys.Battle.BattleConst
var_0_2 = pg.bullet_template
var_0_3 = pg.barrage_template


var_0_5 = BattleConst.UnitDir.LEFT
var_0_6 = BattleConst.UnitDir.RIGHT


@staticmethod
def CreateBattleBulletData(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4):
	var_1_0 = BattleDataFunction.GetBulletTmpDataFromID(arg_1_1)
	var_1_1 = var_1_0.type
	var_1_2, var_1_3 = BattleDataFunction.generateBulletFuncs[var_1_1](arg_1_0, var_1_0, arg_1_2, arg_1_3, arg_1_4)

	var_1_2.SetTemplateData(var_1_0)
	var_1_2.SetAttr(arg_1_2._attr)
	var_1_2.SetBuffTrigger(arg_1_2)
	var_1_2.SetWeapon(arg_1_3)

	if arg_1_3 and arg_1_3.GetStandHost():
		var_1_4 = arg_1_3.GetStandHost().GetAttr()

		var_1_2.SetStandHostAttr(var_1_4)

	var_1_5 = var_1_2.IsIngoreCld()

	if var_1_5 != None:
		var_1_6 = not var_1_5

		var_1_2.SetIsCld(var_1_6)

		var_1_3 = var_1_6

	return var_1_2, var_1_3
BattleDataFunction.CreateBattleBulletData = CreateBattleBulletData


@staticmethod
def GetBulletTmpDataFromID(arg_2_0):
	assert var_0_2[arg_2_0] != None, "找不到子弹配置：id = " + arg_2_0

	return var_0_2[arg_2_0]
BattleDataFunction.GetBulletTmpDataFromID = GetBulletTmpDataFromID


@staticmethod
def GetBarrageTmpDataFromID(arg_3_0):
	assert var_0_3[arg_3_0] != None, "找不到弹幕配置：id = " + arg_3_0

	return var_0_3[arg_3_0]
BattleDataFunction.GetBarrageTmpDataFromID = GetBarrageTmpDataFromID


@staticmethod
def GetConvertedBarrageTableFromID(arg_4_0, arg_4_1):
	assert var_0_3[arg_4_0] != None, "获取转换弹幕数据失败，找不到弹幕原型配置：id = " + arg_4_0

	if BattleDataFunction.ConvertedBarrageTableList[arg_4_0] == None or BattleDataFunction.ConvertedBarrageTableList[arg_4_0][arg_4_1] == None:
		BattleDataFunction.ConvertSpecificBarrage(arg_4_0, arg_4_1)

	return BattleDataFunction.ConvertedBarrageTableList[arg_4_0]
BattleDataFunction.GetConvertedBarrageTableFromID = GetConvertedBarrageTableFromID


@staticmethod
def GenerateTransBarrage(arg_5_0, arg_5_1, arg_5_2):
	var_5_0 = table()
	var_5_1 = BattleDataFunction.GetBarrageTmpDataFromID(arg_5_0)

	while var_5_1.trans_ID != -1:
		var_5_2 = var_5_1.trans_ID

		var_5_1 = BattleDataFunction.GetBarrageTmpDataFromID(var_5_2)

		var_5_3 = table(
			transStartDelay = var_5_1.first_delay + var_5_1.delay * arg_5_2 + var_5_1.delta_delay * arg_5_2
		)

		if var_5_1.offset_prioritise:
			var_5_3.transAimPosX = var_5_1.offset_x + var_5_1.delta_offset_x * arg_5_2
			var_5_3.transAimPosZ = var_5_1.offset_z + var_5_1.delta_offset_z * arg_5_2
		else:
			var_5_3.transAimAngle = var_5_1.angle + var_5_1.delta_angle * arg_5_2

			if arg_5_1 == -1:
				var_5_3.transAimAngle = var_5_3.transAimAngle + 180

		var_5_0.append(var_5_3)

	return var_5_0
BattleDataFunction.GenerateTransBarrage = GenerateTransBarrage


@staticmethod
def _createCannonBullet(arg_6_0, arg_6_1, arg_6_2, arg_6_3, arg_6_4):
	var_6_0 = ys.Battle.BattleCannonBulletUnit.New(arg_6_0, arg_6_2.GetIFF())

	var_6_0.SetIsCld(True)

	return var_6_0, True
BattleDataFunction._createCannonBullet = _createCannonBullet


@staticmethod
def _createBombBullet(arg_7_0, arg_7_1, arg_7_2, arg_7_3, arg_7_4):
	var_7_0 = ys.Battle.BattleBombBulletUnit.New(arg_7_0, arg_7_2.GetIFF())

	var_7_0.SetAttr(arg_7_2._attr)
	var_7_0.SetTemplateData(arg_7_1)

	if arg_7_4.EqualZero():
		arg_7_4 = arg_7_2.GetPosition().Clone()

		var_7_1 = arg_7_3.GetTemplateData().range

		if arg_7_2.GetDirection() == BattleConst.UnitDir.RIGHT:
			arg_7_4.x = arg_7_4.x + var_7_1
		else:
			arg_7_4.x = arg_7_4.x - var_7_1

	var_7_0.SetExplodePosition(arg_7_4)
	var_7_0.SetIsCld(False)

	return var_7_0, False
BattleDataFunction._createBombBullet = _createBombBullet


@staticmethod
def _createStrayBullet(arg_8_0, arg_8_1, arg_8_2, arg_8_3, arg_8_4):
	var_8_0 = ys.Battle.BattleStrayBulletUnit.New(arg_8_0, arg_8_2.GetIFF())

	var_8_0.SetIsCld(True)

	return var_8_0, True
BattleDataFunction._createStrayBullet = _createStrayBullet


@staticmethod
def _createTorpedoBullet(arg_9_0, arg_9_1, arg_9_2, arg_9_3, arg_9_4):
	var_9_0 = ys.Battle.BattleTorpedoBulletUnit.New(arg_9_0, arg_9_2.GetIFF())

	var_9_0.SetExplodePosition(arg_9_4)
	var_9_0.SetIsCld(True)

	return var_9_0, True
BattleDataFunction._createTorpedoBullet = _createTorpedoBullet


@staticmethod
def _createDirectBullet(arg_10_0, arg_10_1, arg_10_2, arg_10_3, arg_10_4):
	var_10_0 = ys.Battle.BattleAntiAirBulletUnit.New(arg_10_0, arg_10_2.GetIFF())

	var_10_0.SetIsCld(False)

	return var_10_0, False
BattleDataFunction._createDirectBullet = _createDirectBullet


@staticmethod
def _createAntiAirBullet(arg_11_0, arg_11_1, arg_11_2, arg_11_3, arg_11_4):
	var_11_0 = ys.Battle.BattleAntiAirBulletUnit.New(arg_11_0, arg_11_2.GetIFF())

	var_11_0.SetIsCld(False)

	return var_11_0, False
BattleDataFunction._createAntiAirBullet = _createAntiAirBullet


@staticmethod
def _createAntiSeaBullet(arg_12_0, arg_12_1, arg_12_2, arg_12_3, arg_12_4):
	var_12_0 = ys.Battle.BattleAntiSeaBulletUnit.New(arg_12_0, arg_12_2.GetIFF())

	var_12_0.SetIsCld(False)

	return var_12_0, False
BattleDataFunction._createAntiSeaBullet = _createAntiSeaBullet


@staticmethod
def _createSharpnelBullet(arg_13_0, arg_13_1, arg_13_2, arg_13_3, arg_13_4):
	var_13_0 = ys.Battle.BattleShrapnelBulletUnit.New(arg_13_0, arg_13_2.GetIFF())

	var_13_0.SetExplodePosition(arg_13_4)
	var_13_0.SetSrcHost(arg_13_2)
	var_13_0.SetIsCld(True)

	return var_13_0, True
BattleDataFunction._createSharpnelBullet = _createSharpnelBullet


@staticmethod
def _createEffectBullet(arg_14_0, arg_14_1, arg_14_2, arg_14_3, arg_14_4):
	var_14_0 = ys.Battle.BattleEffectBulletUnit.New(arg_14_0, arg_14_2.GetIFF())

	var_14_0.SetTemplateData(arg_14_1)
	var_14_0.SetIsCld(False)
	var_14_0.SetImmuneCLS(True)

	if arg_14_1.attach_buff[1].flare:
		var_14_0.spawnArea(True)

	return var_14_0, False
BattleDataFunction._createEffectBullet = _createEffectBullet


@staticmethod
def _createBeamBullet(arg_15_0, arg_15_1, arg_15_2, arg_15_3, arg_15_4):
	var_15_0 = ys.Battle.BattleAntiAirBulletUnit.New(arg_15_0, arg_15_2.GetIFF())

	var_15_0.SetIsCld(False)

	return var_15_0, False
BattleDataFunction._createBeamBullet = _createBeamBullet


@staticmethod
def _createGravitationBullet(arg_16_0, arg_16_1, arg_16_2, arg_16_3, arg_16_4):
	var_16_0 = ys.Battle.BattleGravitationBulletUnit.New(arg_16_0, arg_16_2.GetIFF())

	var_16_0.SetExplodePosition(arg_16_4)
	var_16_0.SetIsCld(True)
	var_16_0.SetImmuneCLS(True)

	return var_16_0, True
BattleDataFunction._createGravitationBullet = _createGravitationBullet


@staticmethod
def _createMissile(arg_17_0, arg_17_1, arg_17_2, arg_17_3, arg_17_4):
	var_17_0 = ys.Battle.BattleMissileUnit.New(arg_17_0, arg_17_2.GetIFF())

	var_17_0.SetAttr(arg_17_2._attr)
	var_17_0.SetTemplateData(arg_17_1)
	var_17_0.SetImmuneCLS(True)
	var_17_0.SetIsCld(False)

	return var_17_0, False
BattleDataFunction._createMissile = _createMissile


@staticmethod
def _createSpaceLaser(arg_18_0, arg_18_1, arg_18_2, arg_18_3, arg_18_4):
	var_18_0 = ys.Battle.BattleSpaceLaserUnit.New(arg_18_0, arg_18_2.GetIFF())

	var_18_0.SetIsCld(True)
	var_18_0.SetImmuneCLS(True)

	return var_18_0, True
BattleDataFunction._createSpaceLaser = _createSpaceLaser


@staticmethod
def _createScaleBullet(arg_19_0, arg_19_1, arg_19_2, arg_19_3, arg_19_4):
	var_19_0 = ys.Battle.BattleScaleBulletUnit.New(arg_19_0, arg_19_2.GetIFF())

	var_19_0.SetIsCld(True)

	return var_19_0, True
BattleDataFunction._createScaleBullet = _createScaleBullet


@staticmethod
def _createAAMissile(arg_20_0, arg_20_1, arg_20_2, arg_20_3, arg_20_4):
	var_20_0 = ys.Battle.BattleTrackingAAMissileUnit.New(arg_20_0, arg_20_2.GetIFF())

	var_20_0.SetIsCld(True)

	return var_20_0, True
BattleDataFunction._createAAMissile = _createAAMissile

generateBulletFuncs = table()
generateBulletFuncs[BattleConst.BulletType.CANNON] = _createCannonBullet
generateBulletFuncs[BattleConst.BulletType.BOMB] = _createBombBullet
generateBulletFuncs[BattleConst.BulletType.TORPEDO] = _createTorpedoBullet
generateBulletFuncs[BattleConst.BulletType.DIRECT] = _createDirectBullet
generateBulletFuncs[BattleConst.BulletType.ANTI_AIR] = _createAntiAirBullet
generateBulletFuncs[BattleConst.BulletType.ANTI_SEA] = _createAntiSeaBullet
generateBulletFuncs[BattleConst.BulletType.SHRAPNEL] = _createSharpnelBullet
generateBulletFuncs[BattleConst.BulletType.STRAY] = _createStrayBullet
generateBulletFuncs[BattleConst.BulletType.EFFECT] = _createEffectBullet
generateBulletFuncs[BattleConst.BulletType.BEAM] = _createBeamBullet
generateBulletFuncs[BattleConst.BulletType.G_BULLET] = _createGravitationBullet
generateBulletFuncs[BattleConst.BulletType.ELECTRIC_ARC] = _createDirectBullet
generateBulletFuncs[BattleConst.BulletType.MISSILE] = _createMissile
generateBulletFuncs[BattleConst.BulletType.SPACE_LASER] = _createSpaceLaser
generateBulletFuncs[BattleConst.BulletType.SCALE] = _createScaleBullet
generateBulletFuncs[BattleConst.BulletType.TRIGGER_BOMB] = _createBombBullet
generateBulletFuncs[BattleConst.BulletType.AAMissile] = _createAAMissile



@staticmethod
def ConvertSpecificBarrage(arg_21_0, arg_21_1):
	var_21_0

	var_21_0[arg_21_1], var_21_0 = BattleDataFunction.barrageInteration(pg.barrage_template[arg_21_0], arg_21_1), BattleDataFunction.ConvertedBarrageTableList[arg_21_0] or table()
	BattleDataFunction.ConvertedBarrageTableList[arg_21_0] = var_21_0
BattleDataFunction.ConvertSpecificBarrage = ConvertSpecificBarrage


@staticmethod
def ClearConvertedBarrage():
	BattleDataFunction.ConvertedBarrageTableList = table()
BattleDataFunction.ClearConvertedBarrage = ClearConvertedBarrage


@staticmethod
def barrageInteration(arg_23_0, arg_23_1):
	var_23_0 = 1
	var_23_1 = arg_23_0.primal_repeat
	var_23_2 = table()
	var_23_3 = arg_23_0.offset_x
	var_23_4 = arg_23_0.offset_z
	var_23_5 = arg_23_0.angle
	var_23_6 = arg_23_0.delay
	var_23_7 = arg_23_0.delta_offset_x
	var_23_8 = arg_23_0.delta_offset_z
	var_23_9 = arg_23_0.delta_angle
	var_23_10 = arg_23_0.delta_delay

	for _ in range(var_23_1):
		var_23_11 = table(
			OffsetX = var_23_3 * arg_23_1,
			OffsetZ = var_23_4,
			Angle = var_23_5,
			Delay = var_23_6
		)

		table.insert(var_23_2, var_23_11)

		var_23_3 = var_23_3 + var_23_7
		var_23_4 = var_23_4 + var_23_8
		var_23_5 = var_23_5 + var_23_9
		var_23_6 = var_23_6 + var_23_10

	return var_23_2
BattleDataFunction.barrageInteration = barrageInteration

BattleDataFunction.ClearConvertedBarrage()
