local var_0_0 = class("AttachmentBoxCell", import("view.level.cell.StaticCellView"))

function var_0_0.GetOrder(arg_1_0)
	return ChapterConst.CellPriorityAttachment
end

function var_0_0.Update(arg_2_0)
	local var_2_0 = arg_2_0.info

	if IsNil(arg_2_0.go) then
		local var_2_1 = pg.box_data_template[var_2_0.attachmentId]

		assert(var_2_1, "box_data_template not exist: " .. var_2_0.attachmentId)

		local var_2_2 = "box_" .. var_2_0.attachmentId

		arg_2_0:PrepareBase(var_2_2)

		local var_2_3
		local var_2_4

		parallelAsync({
			function(arg_3_0)
				arg_2_0:GetLoader():GetPrefab("boxprefab/" .. var_2_1.icon, var_2_1.icon, function(arg_4_0)
					var_2_4 = arg_4_0

					arg_3_0()
				end)
			end,
			function(arg_5_0)
				arg_2_0:GetLoader():GetPrefab("leveluiview/tpl_box", "tpl_box", function(arg_6_0)
					var_2_3 = arg_6_0

					setParent(tf(var_2_3), arg_2_0.tf)

					tf(var_2_3).anchoredPosition3D = Vector3(0, 30, 0)

					if var_2_1.type ~= ChapterConst.BoxTorpedo then
						local var_6_0 = LeanTween.move(tf(var_2_3), Vector3(0, 40, 0), 1.5):setEase(LeanTweenType.easeInOutSine):setLoopPingPong()

						arg_2_0.attachTw = var_6_0.uniqueId
					end

					arg_2_0.box = var_2_3

					arg_5_0()
				end)
			end
		}, function()
			setParent(var_2_4, tf(var_2_3):Find("icon"))
			arg_2_0:ResetCanvasOrder()
			arg_2_0:Update()
		end)
	end

	if arg_2_0.box and var_2_0.flag == ChapterConst.CellFlagActive then
		setActive(findTF(arg_2_0.box, "effect_found"), var_2_0.trait == ChapterConst.TraitVirgin)

		if var_2_0.trait == ChapterConst.TraitVirgin then
			pg.CriMgr.GetInstance():PlaySoundEffect_V3(SFX_UI_WEIGHANCHOR_ENEMY)
		end
	end

	setActive(arg_2_0.tf, var_2_0.flag == ChapterConst.CellFlagActive)
end

function var_0_0.RemoveTween(arg_8_0)
	if arg_8_0.attachTw then
		LeanTween.cancel(arg_8_0.attachTw)
	end

	arg_8_0.attachTw = nil
end

function var_0_0.Clear(arg_9_0)
	arg_9_0:RemoveTween()
	var_0_0.super.Clear(arg_9_0)
end

return var_0_0
