import math
from Vector3  import Vector3
import BattleBulletUnit

class BattleScaleBulletUnit(BattleBulletUnit):
	__name = "BattleScaleBulletUnit"

	def __init__(arg_1_0, arg_1_1, arg_1_2):
		super().__init__(arg_1_0, arg_1_1, arg_1_2)

		arg_1_0._scaleX = 0

	def Update(arg_2_0, arg_2_1):
		var_2_0 = arg_2_0._tempData.cld_box

		if arg_2_0._scaleX + var_2_0[1] > arg_2_0._scaleLimit:
			arg_2_0.calcSpeed()
		else:
			arg_2_0.UpdateCLDBox()

		super().Update(arg_2_0, arg_2_1)

	def SetTemplateData(arg_3_0, arg_3_1):
		super().SetTemplateData(arg_3_0, arg_3_1)

		arg_3_0._scaleSpeed = arg_3_0._tempData.extra_param.scaleSpeed
		arg_3_0._scaleLimit = arg_3_0._tempData.extra_param.cldMax

	def InitSpeed(arg_4_0, arg_4_1):
		super().InitSpeed(arg_4_0, arg_4_1)
		arg_4_0.calcScaleSpeed()

	def calcScaleSpeed(arg_5_0):
		var_5_0 = arg_5_0._scaleSpeed * 0.5
		var_5_1 = math.deg2Rad * arg_5_0._yAngle

		arg_5_0._speed = Vector3(var_5_0 * math.cos(var_5_1), 0, var_5_0 * math.sin(var_5_1))

	def UpdateCLDBox(arg_6_0):
		var_6_0 = arg_6_0._tempData.cld_box

		arg_6_0._scaleX = arg_6_0._scaleX + arg_6_0._scaleSpeed

		arg_6_0._cldComponent.ResetSize(var_6_0[1] + arg_6_0._scaleX, var_6_0[2], var_6_0[3])

	def GetRadian(arg_7_0):
		var_7_0 = arg_7_0._radCache or arg_7_0.GetYAngle() * math.deg2Rad
		var_7_1 = arg_7_0._cosCache or math.cos(var_7_0)
		var_7_2 = arg_7_0._sinCache or math.sin(var_7_0)

		return var_7_0, var_7_1, var_7_2
