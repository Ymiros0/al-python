local var_0_0 = class("ActivityBuff", import(".CommonBuff"))

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3)
	var_0_0.super.Ctor(arg_1_0, {
		id = arg_1_2,
		timestamp = arg_1_3
	})

	arg_1_0.activityId = arg_1_1
end

function var_0_0.IsActiveType(arg_2_0)
	return true
end

local function var_0_1(arg_3_0, arg_3_1, arg_3_2)
	if arg_3_1 == "<=" then
		return arg_3_0 <= arg_3_2
	elseif arg_3_1 == "<" then
		return arg_3_0 < arg_3_2
	elseif arg_3_1 == "==" then
		return arg_3_0 == arg_3_2
	elseif arg_3_1 == ">=" then
		return arg_3_2 <= arg_3_0
	elseif arg_3_1 == ">" then
		return arg_3_2 < arg_3_0
	end

	return false
end

function var_0_0.isActivate(arg_4_0)
	local var_4_0 = false
	local var_4_1 = getProxy(ActivityProxy):getActivityById(arg_4_0.activityId)

	if var_4_1 and not var_4_1:isEnd() then
		if var_4_1:getConfig("type") == ActivityConst.ACTIVITY_TYPE_BUFF then
			if arg_4_0:RookieBattleExpUsage() then
				if getProxy(PlayerProxy):getRawData().level < arg_4_0:GetRookieBattleExpMaxLevel() then
					var_4_0 = true
				end
			elseif arg_4_0:isAddedBuff() then
				var_4_0 = true
			end
		else
			var_4_0 = (function()
				local var_5_0 = arg_4_0:getConfig("benefit_condition")

				if var_5_0[1] == "lv" then
					local var_5_1 = getProxy(PlayerProxy):getRawData()

					return var_0_1(var_5_1.level, var_5_0[2], var_5_0[3])
				elseif var_5_0[1] == "activity" then
					if var_5_0[3] == 0 then
						return true
					end

					if var_4_1:getConfig("type") == ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF or var_4_1:getConfig("type") == ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF_2 then
						local var_5_2 = var_5_0[3][1]

						return (var_4_1.data1KeyValueList[2][var_5_2] or 1) == var_5_0[3][2]
					end
				end

				if var_5_0 == "" then
					return true
				end
			end)() or false
		end
	end

	return var_4_0
end

function var_0_0.getLeftTime(arg_6_0)
	local var_6_0 = pg.TimeMgr.GetInstance():GetServerTime()

	return getProxy(ActivityProxy):getActivityById(arg_6_0.activityId).stopTime - var_6_0
end

function var_0_0.isAddedBuff(arg_7_0)
	local var_7_0 = true
	local var_7_1 = getProxy(ActivityProxy):getActivityById(arg_7_0.activityId)

	if var_7_1 and not var_7_1:isEnd() then
		local var_7_2 = arg_7_0:getConfig("benefit_condition")

		if var_7_2[1] == "pt" then
			local var_7_3 = var_7_2[2]
			local var_7_4 = var_7_2[3]
			local var_7_5 = var_7_2[4]
			local var_7_6 = pg.player_resource[var_7_3].name
			local var_7_7 = getProxy(PlayerProxy):getData()[var_7_6] or 0

			if not (var_7_4 <= var_7_7) or not (var_7_7 < var_7_5) then
				var_7_0 = false
			end
		end
	end

	return var_7_0
end

return var_0_0
