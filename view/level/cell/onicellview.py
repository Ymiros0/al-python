local var_0_0 = import(".DynamicCellView")
local var_0_1 = class("OniCellView", var_0_0)

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.tfShadow = arg_1_0.tf.Find("shadow")
	arg_1_0.tfIcon = arg_1_0.tf.Find("ship/icon")

def var_0_1.GetOrder(arg_2_0):
	return ChapterConst.CellPriorityLittle

def var_0_1.SetActive(arg_3_0, arg_3_1):
	SetActive(arg_3_0.tf, arg_3_1)

def var_0_1.UpdateChampionCell(arg_4_0, arg_4_1, arg_4_2, arg_4_3):
	local var_4_0 = arg_4_2.trait != ChapterConst.TraitLurk and arg_4_1.getChampionVisibility(arg_4_2) and not arg_4_1.existFleet(FleetType.Transport, arg_4_2.row, arg_4_2.column)
	local var_4_1 = 1

	_.each(arg_4_1.fleets, function(arg_5_0)
		if arg_4_2.inAlertRange(arg_5_0.line.row, arg_5_0.line.column):
			var_4_1 = var_4_1 + 1)
	GetImageSpriteFromAtlasAsync("enemies/sp_" .. var_4_1, "", arg_4_0.tfIcon, True)

	arg_4_0.tfShadow.localEulerAngles = Vector3(arg_4_1.theme.angle, 0, 0)

	arg_4_0.RefreshLinePosition(arg_4_1, arg_4_2)
	arg_4_0.SetActive(var_4_0)
	existCall(arg_4_3)

return var_0_1
