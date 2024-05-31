local var_0_0 = class("AttachmentLBDockCell", import("view.level.cell.StaticCellView"))

def var_0_0.GetOrder(arg_1_0):
	return ChapterConst.CellPriorityAttachment

def var_0_0.Update(arg_2_0):
	local var_2_0 = arg_2_0.info

	if IsNil(arg_2_0.go):
		arg_2_0.PrepareBase("dock")
		arg_2_0.GetLoader().GetPrefab("leveluiview/Tpl_Dockyard", "Tpl_Dockyard", function(arg_3_0)
			setParent(arg_3_0, arg_2_0.tf)

			tf(arg_3_0).anchoredPosition3D = Vector3(0, 10, 0)
			arg_2_0.dock = tf(arg_3_0)

			arg_2_0.Update())

	if arg_2_0.dock:
		local var_2_1 = pg.land_based_template[var_2_0.attachmentId]

		assert(var_2_1, "land_based_template not exist. " .. var_2_0.attachmentId)

		local var_2_2 = arg_2_0.chapter.getRoundNum()
		local var_2_3 = arg_2_0.dock.Find("text")
		local var_2_4 = math.ceil(var_2_0.data / 2)

		setActive(var_2_3, var_2_2 < var_2_4)

		local var_2_5 = arg_2_0.dock.Find("Slider").GetComponent(typeof(Slider))
		local var_2_6 = var_2_1.function_args[2]

		var_2_5.value = math.max(var_2_2 - var_2_4 + var_2_6, 0) / var_2_6

	setActive(arg_2_0.tf, var_2_0.flag == ChapterConst.CellFlagActive)

return var_0_0
