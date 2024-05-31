local var_0_0 = class("AttachmentBoxCell", import("view.level.cell.StaticCellView"))

def var_0_0.GetOrder(arg_1_0):
	return ChapterConst.CellPriorityAttachment

def var_0_0.Update(arg_2_0):
	local var_2_0 = arg_2_0.info

	if IsNil(arg_2_0.go):
		local var_2_1 = pg.box_data_template[var_2_0.attachmentId]

		assert(var_2_1, "box_data_template not exist. " .. var_2_0.attachmentId)

		local var_2_2 = "box_" .. var_2_0.attachmentId

		arg_2_0.PrepareBase(var_2_2)

		local var_2_3
		local var_2_4

		parallelAsync({
			function(arg_3_0)
				arg_2_0.GetLoader().GetPrefab("boxprefab/" .. var_2_1.icon, var_2_1.icon, function(arg_4_0)
					var_2_4 = arg_4_0

					arg_3_0()),
			function(arg_5_0)
				arg_2_0.GetLoader().GetPrefab("leveluiview/tpl_box", "tpl_box", function(arg_6_0)
					var_2_3 = arg_6_0

					setParent(tf(var_2_3), arg_2_0.tf)

					tf(var_2_3).anchoredPosition3D = Vector3(0, 30, 0)

					if var_2_1.type != ChapterConst.BoxTorpedo:
						local var_6_0 = LeanTween.move(tf(var_2_3), Vector3(0, 40, 0), 1.5).setEase(LeanTweenType.easeInOutSine).setLoopPingPong()

						arg_2_0.attachTw = var_6_0.uniqueId

					arg_2_0.box = var_2_3

					arg_5_0())
		}, function()
			setParent(var_2_4, tf(var_2_3).Find("icon"))
			arg_2_0.ResetCanvasOrder()
			arg_2_0.Update())

	if arg_2_0.box and var_2_0.flag == ChapterConst.CellFlagActive:
		setActive(findTF(arg_2_0.box, "effect_found"), var_2_0.trait == ChapterConst.TraitVirgin)

		if var_2_0.trait == ChapterConst.TraitVirgin:
			pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_UI_WEIGHANCHOR_ENEMY)

	setActive(arg_2_0.tf, var_2_0.flag == ChapterConst.CellFlagActive)

def var_0_0.RemoveTween(arg_8_0):
	if arg_8_0.attachTw:
		LeanTween.cancel(arg_8_0.attachTw)

	arg_8_0.attachTw = None

def var_0_0.Clear(arg_9_0):
	arg_9_0.RemoveTween()
	var_0_0.super.Clear(arg_9_0)

return var_0_0
