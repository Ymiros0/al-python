local var_0_0 = class("AttachmentLBAirport", import("view.level.cell.StaticCellView"))

var_0_0.StateOutControl = 1
var_0_0.StateUnderControl = 2

def var_0_0.GetOrder(arg_1_0):
	return ChapterConst.CellPriorityAttachment

def var_0_0.Update(arg_2_0):
	local var_2_0 = arg_2_0.extraFlagList

	if IsNil(arg_2_0.go):
		arg_2_0.PrepareBase("airport")

	if table.contains(var_2_0, ChapterConst.StatusAirportOutControl) and arg_2_0.state != var_0_0.StateOutControl:
		arg_2_0.state = var_0_0.StateOutControl

		arg_2_0.GetLoader().ClearRequest("Dead", AutoLoader.PartLoading)
		arg_2_0.GetLoader().GetPrefab("chapter/dexiv3_2x2_2", "dexiv3_2x2_2", function(arg_3_0)
			arg_2_0.GetLoader().ClearRequest("Dead")
			setParent(arg_3_0, arg_2_0.tf), "Enemy")
	elif table.contains(var_2_0, ChapterConst.StatusAirportUnderControl) and arg_2_0.state != var_0_0.StateUnderControl:
		arg_2_0.state = var_0_0.StateUnderControl

		arg_2_0.GetLoader().ClearRequest("Enemy", AutoLoader.PartLoading)
		arg_2_0.GetLoader().GetPrefab("chapter/dexiv3_2x2_1", "dexiv3_2x2_1", function(arg_4_0)
			arg_2_0.GetLoader().ClearRequest("Enemy")
			setParent(arg_4_0, arg_2_0.tf), "Dead")

return var_0_0
