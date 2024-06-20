local var_0_0 = class("AttachmentSupplyCell", import("view.level.cell.StaticCellView"))

def var_0_0.GetOrder(arg_1_0):
	return ChapterConst.CellPriorityAttachment

def var_0_0.Update(arg_2_0):
	local var_2_0 = arg_2_0.info

	if IsNil(arg_2_0.go):
		arg_2_0.PrepareBase("supply")
		arg_2_0.GetLoader().GetPrefab("leveluiview/tpl_supply", "Tpl_Supply", function(arg_3_0)
			setParent(arg_3_0, arg_2_0.tf)

			tf(arg_3_0).anchoredPosition3D = Vector3(0, 30, 0)

			local var_3_0 = LeanTween.moveY(tf(arg_3_0), 40, 1.5).setEase(LeanTweenType.easeInOutSine).setLoopPingPong()

			arg_2_0.attachTw = var_3_0.uniqueId
			arg_2_0.supply = arg_3_0

			arg_2_0.Update())

	if arg_2_0.supply:
		setActive(findTF(arg_2_0.supply, "normal"), var_2_0.attachmentId > 0)
		setActive(findTF(arg_2_0.supply, "empty"), False)

	setActive(arg_2_0.tf, var_2_0.flag == ChapterConst.CellFlagActive)

def var_0_0.RemoveTween(arg_4_0):
	if arg_4_0.attachTw:
		LeanTween.cancel(arg_4_0.attachTw)

	arg_4_0.attachTw = None

def var_0_0.Clear(arg_5_0):
	arg_5_0.RemoveTween()
	var_0_0.super.Clear(arg_5_0)

return var_0_0