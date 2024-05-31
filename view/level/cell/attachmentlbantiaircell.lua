local var_0_0 = class("AttachmentLBAntiAirCell", import("view.level.cell.StaticCellView"))

function var_0_0.GetOrder(arg_1_0)
	return ChapterConst.CellPriorityAttachment
end

function var_0_0.Update(arg_2_0)
	local var_2_0 = arg_2_0.info

	if IsNil(arg_2_0.go) then
		arg_2_0:PrepareBase("antiAir")

		local var_2_1 = pg.land_based_template[var_2_0.attachmentId]

		assert(var_2_1, "land_based_template not exist: " .. var_2_0.attachmentId)
		arg_2_0:GetLoader():GetPrefab("leveluiview/Tpl_AntiAirGun", "Tpl_AntiAirGun", function(arg_3_0)
			setParent(arg_3_0, arg_2_0.tf)

			tf(arg_3_0).anchoredPosition3D = Vector3(0, 10, 0)
			arg_2_0.antiAirGun = arg_3_0

			arg_2_0:Update()
		end)
		arg_2_0:GetLoader():GetPrefab("leveluiview/Tpl_AntiAirGunArea", "Tpl_AntiAirGunArea", function(arg_4_0)
			setParent(arg_4_0, arg_2_0.grid.restrictMap)

			arg_4_0.name = "chapter_cell_mark_" .. var_2_0.row .. "_" .. var_2_0.column .. "#AntiAirGunArea"

			local var_4_0 = arg_2_0.chapter.theme
			local var_4_1 = var_4_0:GetLinePosition(arg_2_0.line.row, arg_2_0.line.column)
			local var_4_2 = arg_2_0.grid.restrictMap.anchoredPosition

			tf(arg_4_0).anchoredPosition = Vector2(var_4_1.x - var_4_2.x, var_4_1.y - var_4_2.y)

			local var_4_3 = var_2_1.function_args[1]
			local var_4_4 = (var_4_3 * 2 + 1) * var_4_0.cellSize.x + var_4_3 * 2 * var_4_0.cellSpace.x
			local var_4_5 = (var_4_3 * 2 + 1) * var_4_0.cellSize.y + var_4_3 * 2 * var_4_0.cellSpace.y

			tf(arg_4_0).sizeDelta = Vector2(var_4_4, var_4_5)
		end)
	end

	if arg_2_0.antiAirGun and var_2_0.flag ~= ChapterConst.CellFlagDisabled then
		local var_2_2 = math.ceil(var_2_0.data / 2)
		local var_2_3 = pg.land_based_template[var_2_0.attachmentId]

		assert(var_2_3, "land_based_template not exist: " .. var_2_0.attachmentId)

		local var_2_4 = var_2_3.function_args[2]
		local var_2_5 = arg_2_0.chapter:getRoundNum()
		local var_2_6 = tf(arg_2_0.antiAirGun):Find("text")

		setActive(var_2_6, var_2_5 < var_2_2)

		tf(arg_2_0.antiAirGun):Find("Slider"):GetComponent(typeof(Slider)).value = math.max(var_2_5 - var_2_2 + var_2_4, 0) / var_2_4
	end

	setActive(arg_2_0.tf, var_2_0.flag ~= ChapterConst.CellFlagDisabled)
end

return var_0_0
