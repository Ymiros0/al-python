local var_0_0 = class("MapEventStoryCellView", import("view.level.cell.StaticCellView"))

function var_0_0.Ctor(arg_1_0, arg_1_1)
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.attachTw = nil
end

function var_0_0.GetOrder(arg_2_0)
	return ChapterConst.CellPriorityAttachment
end

function var_0_0.Update(arg_3_0)
	local var_3_0 = arg_3_0.info

	if IsNil(arg_3_0.go) then
		local var_3_1 = var_3_0.row
		local var_3_2 = var_3_0.column
		local var_3_3 = var_3_0.data
		local var_3_4 = pg.map_event_template[var_3_0.attachmentId].icon
		local var_3_5 = "story_" .. var_3_1 .. "_" .. var_3_2 .. "_" .. var_3_0.attachmentId

		arg_3_0:PrepareBase(var_3_5)
		setAnchoredPosition(arg_3_0.tf, Vector2(0, 30))

		arg_3_0.attachTw = LeanTween.moveY(rtf(arg_3_0.go), 40, 1.5):setEase(LeanTweenType.easeInOutSine):setLoopPingPong()

		arg_3_0:GetLoader():GetPrefab("leveluiview/tpl_box", "tpl_box", function(arg_4_0)
			arg_4_0.name = var_3_4

			setParent(arg_4_0, arg_3_0.tf)
			setAnchoredPosition(arg_4_0, Vector2.zero)
			arg_3_0:GetLoader():GetPrefab("boxprefab/" .. var_3_4, var_3_4, function(arg_5_0)
				setParent(arg_5_0, tf(arg_4_0):Find("icon"))
			end)
		end)
	end

	local var_3_6 = var_3_0.flag == ChapterConst.CellFlagActive

	setActive(arg_3_0.tf, var_3_6)
end

function var_0_0.DestroyGO(arg_6_0)
	if arg_6_0.attachTw then
		LeanTween.cancel(arg_6_0.attachTw.uniqueId)

		arg_6_0.attachTw = nil
	end

	var_0_0.super.DestroyGO(arg_6_0)
end

return var_0_0
