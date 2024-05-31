﻿local var_0_0 = class("ItemCard")

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0.go = arg_1_1
	arg_1_0.bg = findTF(arg_1_1, "bg")
	arg_1_0.countTF = findTF(arg_1_1, "bg/icon_bg/count"):GetComponent(typeof(Text))
	arg_1_0.nameTF = findTF(arg_1_1, "bg/name"):GetComponent(typeof(Text))
	arg_1_0.timeLimitTag = findTF(arg_1_1, "bg/timeline")

	ClearTweenItemAlphaAndWhite(arg_1_0.go)
end

function var_0_0.update(arg_2_0, arg_2_1)
	arg_2_0.itemVO = arg_2_1

	if not IsNil(arg_2_0.timeLimitTag) then
		setActive(arg_2_0.timeLimitTag, arg_2_1:getConfig("time_limit") == 1 or Item.InTimeLimitSkinAssigned(arg_2_1.id))
	end

	updateItem(rtf(arg_2_0.bg), arg_2_1)
	TweenItemAlphaAndWhite(arg_2_0.go)

	arg_2_0.countTF.text = arg_2_1.count > 0 and arg_2_1.count or ""
	arg_2_0.nameTF.text = arg_2_0:ShortenString(arg_2_1:getConfig("name"), 6)
end

function var_0_0.ShortenString(arg_3_0, arg_3_1, arg_3_2)
	local var_3_0 = 1
	local var_3_1 = 0
	local var_3_2 = 0
	local var_3_3 = #arg_3_1
	local var_3_4 = false

	while var_3_0 <= var_3_3 do
		local var_3_5 = string.byte(arg_3_1, var_3_0)
		local var_3_6, var_3_7 = GetPerceptualSize(var_3_5)

		var_3_0 = var_3_0 + var_3_6
		var_3_1 = var_3_1 + var_3_7

		local var_3_8 = math.ceil(var_3_1)

		if var_3_8 == arg_3_2 - 1 then
			var_3_2 = var_3_0
		elseif arg_3_2 < var_3_8 then
			var_3_4 = true

			break
		end
	end

	if var_3_2 == 0 or var_3_3 < var_3_2 or not var_3_4 then
		return arg_3_1
	end

	return string.sub(arg_3_1, 1, var_3_2 - 1) .. ".."
end

function var_0_0.clear(arg_4_0)
	ClearTweenItemAlphaAndWhite(arg_4_0.go)
end

function var_0_0.dispose(arg_5_0)
	return
end

return var_0_0
