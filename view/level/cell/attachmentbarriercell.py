local var_0_0 = class("AttachmentBarrierCell", import("view.level.cell.StaticCellView"))

def var_0_0.GetOrder(arg_1_0):
	return ChapterConst.CellPriorityAttachment

def var_0_0.Update(arg_2_0):
	local var_2_0 = arg_2_0.info

	if IsNil(arg_2_0.go):
		arg_2_0.PrepareBase("zulanwangheng")
		arg_2_0.GetLoader().GetPrefab("chapter/zulanwangheng", "zulanwangheng", function(arg_3_0)
			setParent(arg_3_0, arg_2_0.tf)
			setActive(arg_3_0, True)

			arg_2_0.barrier = arg_3_0

			arg_2_0.Update())

	setActive(arg_2_0.tf, var_2_0.flag == ChapterConst.CellFlagActive)

return var_0_0
