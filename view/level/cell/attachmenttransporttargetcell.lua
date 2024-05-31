local var_0_0 = class("AttachmentTransportTargetCell", import("view.level.cell.StaticCellView"))

function var_0_0.GetOrder(arg_1_0)
	return ChapterConst.CellPriorityAttachment
end

function var_0_0.Update(arg_2_0)
	local var_2_0 = arg_2_0.info

	if IsNil(arg_2_0.go) then
		arg_2_0:PrepareBase("transport_target")
		arg_2_0:GetLoader():GetPrefab("leveluiview/Tpl_TransportTarget", "Tpl_TransportTarget", function(arg_3_0)
			setParent(arg_3_0, arg_2_0.tf)

			tf(arg_3_0).anchoredPosition3D = Vector3.zero

			local var_3_0 = LeanTween.moveY(tf(arg_3_0), 10, 1.5):setEase(LeanTweenType.easeInOutSine):setLoopPingPong()

			arg_2_0.attachTw = var_3_0.uniqueId

			arg_2_0:ResetCanvasOrder()
			arg_2_0:Update()
		end)
	end
end

function var_0_0.RemoveTween(arg_4_0)
	if arg_4_0.attachTw then
		LeanTween.cancel(arg_4_0.attachTw)
	end

	arg_4_0.attachTw = nil
end

function var_0_0.Clear(arg_5_0)
	arg_5_0:RemoveTween()
	var_0_0.super.Clear(arg_5_0)
end

return var_0_0
