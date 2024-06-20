from luatable import table
from Vector3 import Vector3


from component import BattleColumnCldComponent
import BattleConst

import BattleAreaBulletUnit
class BattleColumnAreaBulletUnit(BattleAreaBulletUnit):

	__name = "BattleColumnAreaBulletUnit"
	AreaType = BattleConst.AreaType.COLUMN

	def InitCldComponent(arg_1_0):
		var_1_0 = arg_1_0.GetTemplate().cld_box
		var_1_1 = arg_1_0.GetTemplate().cld_offset

		arg_1_0._cldComponent = BattleColumnCldComponent(var_1_0[1], var_1_0[3])

		var_1_2 = table(
			type = BattleConst.CldType.AOE,
			UID = arg_1_0.GetUniqueID(),
			IFF = arg_1_0.GetIFF()
		)

		arg_1_0._cldComponent.SetCldData(var_1_2)

	def GetBoxSize(arg_2_0):
		var_2_0 = arg_2_0._cldComponent.GetCldBoxSize()

		return Vector3(var_2_0.range, var_2_0.range, var_2_0.tickness)
