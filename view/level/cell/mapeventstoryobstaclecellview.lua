local var_0_0 = class("MapEventStoryObstacleCellView", import("view.level.cell.StaticCellView"))

function var_0_0.GetOrder(arg_1_0)
	return ChapterConst.CellPriorityAttachment
end

function var_0_0.Update(arg_2_0)
	local var_2_0 = arg_2_0.info

	if IsNil(arg_2_0.go) then
		local var_2_1 = var_2_0.row
		local var_2_2 = var_2_0.column
		local var_2_3 = "story_" .. var_2_1 .. "_" .. var_2_2 .. "_" .. var_2_0.attachmentId

		arg_2_0:PrepareBase(var_2_3)
	end

	local var_2_4 = pg.map_event_template[var_2_0.attachmentId].icon
	local var_2_5

	var_2_5 = var_2_4 and #var_2_4 > 0 and var_2_4 .. "_2" or nil

	local var_2_6 = ItemCell.TransformItemAsset(arg_2_0.chapter, var_2_5)

	if arg_2_0.assetName ~= var_2_6 then
		if var_2_6 == nil then
			arg_2_0:GetLoader():ClearRequest("ItemAsset")

			arg_2_0.assetName = var_2_6
		else
			arg_2_0:GetLoader():GetPrefab("ui/" .. var_2_6, var_2_6, function(arg_3_0)
				setParent(arg_3_0, arg_2_0.tf)
				arg_2_0:ResetCanvasOrder()

				arg_2_0.assetName = var_2_6
			end, "ItemAsset")
		end
	end

	local var_2_7 = var_2_0.flag == ChapterConst.CellFlagTriggerActive
	local var_2_8 = pg.map_event_template[var_2_0.attachmentId]

	if not var_2_7 and var_2_8 and var_2_8.animation and not arg_2_0.disappearAnim then
		local var_2_9 = var_2_8.animation

		if var_2_9 and #var_2_9 > 0 then
			arg_2_0:GetLoader():GetPrefab("ui/" .. var_2_9, var_2_9, function(arg_4_0)
				setParent(arg_4_0.transform, arg_2_0.tf, false)
				arg_2_0:ResetCanvasOrder()

				local var_4_0 = arg_4_0:GetComponent(typeof(ParticleSystemEvent))

				if not IsNil(var_4_0) then
					var_4_0:SetEndEvent(function()
						arg_2_0:GetLoader():ClearRequest("DisapperAnim")

						arg_2_0.playingAnim = false

						arg_2_0:Update()
					end)
				end
			end, "DisapperAnim")

			arg_2_0.disappearAnim = true
			arg_2_0.playingAnim = true
		end
	end

	setActive(arg_2_0.tf, var_2_7 or arg_2_0.playingAnim)
end

return var_0_0
