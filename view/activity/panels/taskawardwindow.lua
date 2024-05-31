﻿local var_0_0 = class("TaskAwardWindow", import(".PtAwardWindow"))

local function var_0_1(arg_1_0)
	local var_1_0 = _.flatten(arg_1_0.tasklist)

	local function var_1_1(arg_2_0)
		for iter_2_0, iter_2_1 in ipairs(arg_1_0.tasklist) do
			if type(iter_2_1) == "table" then
				for iter_2_2, iter_2_3 in ipairs(iter_2_1) do
					if iter_2_3 == arg_2_0 then
						return iter_2_0
					end
				end
			elseif arg_2_0 == iter_2_1 then
				return iter_2_0
			end
		end
	end

	local var_1_2 = getProxy(TaskProxy)
	local var_1_3

	for iter_1_0 = #var_1_0, 1, -1 do
		local var_1_4 = var_1_0[iter_1_0]
		local var_1_5 = var_1_2:getFinishTaskById(var_1_4)

		if var_1_5 and var_1_5:isReceive() then
			var_1_3 = var_1_4
		end
	end

	var_1_3 = var_1_3 or var_1_0[(arg_1_0.index - 1) * 2 + 1]

	arg_1_0.UIlist:make(function(arg_3_0, arg_3_1, arg_3_2)
		if arg_3_0 == UIItemList.EventUpdate then
			local var_3_0 = var_1_0[arg_3_1 + 1]
			local var_3_1 = var_1_2:getTaskById(var_3_0) or var_1_2:getFinishTaskById(var_3_0) or Task.New({
				id = var_3_0
			})
			local var_3_2 = GetPerceptualSize(var_3_1:getConfig("name"))

			setText(arg_3_2:Find("title/Text"), "PHASE " .. var_1_1(var_3_0))
			setText(arg_3_2:Find("target/title"), var_3_1:getConfig("name"))
			setText(arg_3_2:Find("target/Text"), "")

			if arg_3_2:Find("target/icon") then
				if arg_1_0.resIcon == "" then
					arg_1_0.resIcon = nil
				end

				if arg_1_0.resIcon then
					LoadImageSpriteAsync(arg_1_0.resIcon, arg_3_2:Find("target/icon"), false)
				end

				setActive(arg_3_2:Find("target/icon"), arg_1_0.resIcon)
				setActive(arg_3_2:Find("target/mark"), arg_1_0.resIcon)
			end

			local var_3_3 = var_3_1:getConfig("award_display")[1]
			local var_3_4 = {
				type = var_3_3[1],
				id = var_3_3[2],
				count = var_3_3[3]
			}

			updateDrop(arg_3_2:Find("award"), var_3_4)
			onButton(arg_1_0.binder, arg_3_2:Find("award"), function()
				arg_1_0.binder:emit(BaseUI.ON_DROP, var_3_4)
			end, SFX_PANEL)

			local var_3_5 = var_1_3 and var_3_0 < var_1_3

			setActive(arg_3_2:Find("award/mask"), var_3_1:isReceive() or var_3_5)
		end
	end)
	arg_1_0.UIlist:align(#var_1_0)
end

function var_0_0.Show(arg_5_0, arg_5_1)
	arg_5_0.tasklist = arg_5_1.tasklist
	arg_5_0.ptId = arg_5_1.ptId
	arg_5_0.totalPt = arg_5_1.totalPt
	arg_5_0.index = arg_5_1.index or 1

	arg_5_0:updateResIcon(arg_5_1.resId, arg_5_1.resIcon, arg_5_1.type)
	var_0_1(arg_5_0)

	arg_5_0.totalTxt.text = arg_5_0.totalPt
	arg_5_0.totalTitleTxt.text = i18n("award_window_pt_title")

	setActive(arg_5_0._tf, true)
end

return var_0_0
