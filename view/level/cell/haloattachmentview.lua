local var_0_0 = class("HaloAttachmentView", import(".StaticCellView"))

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3)
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.line = {
		row = arg_1_2,
		column = arg_1_3
	}
end

function var_0_0.GetOrder(arg_2_0)
	return ChapterConst.CellPriorityUpperEffect
end

function var_0_0.Update(arg_3_0)
	local var_3_0 = arg_3_0.info
	local var_3_1 = var_3_0.flag == ChapterConst.CellFlagTriggerActive and var_3_0.trait ~= ChapterConst.TraitLurk

	if IsNil(arg_3_0.go) then
		local var_3_2 = arg_3_0.line.row
		local var_3_3 = arg_3_0.line.column
		local var_3_4 = "story_" .. var_3_2 .. "_" .. var_3_3 .. "_" .. var_3_0.attachmentId .. "_upper"

		arg_3_0:PrepareBase(var_3_4)

		local var_3_5 = pg.map_event_template[var_3_0.attachmentId].icon

		if var_3_5 and #var_3_5 > 0 then
			local var_3_6 = var_3_5 .. "_1shangceng"
			local var_3_7 = "ui/" .. var_3_6
			local var_3_8 = var_3_6

			arg_3_0:GetLoader():GetPrefab(var_3_7, var_3_8, function(arg_4_0)
				tf(arg_4_0):SetParent(arg_3_0.tf, false)
				arg_3_0:ResetCanvasOrder()
			end)
		end
	end

	setActive(arg_3_0.tf, var_3_1)
end

return var_0_0
