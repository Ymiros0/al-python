local var_0_0 = class("ActivityBuff", import(".CommonBuff"))

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	var_0_0.super.Ctor(arg_1_0, {
		id = arg_1_2,
		timestamp = arg_1_3
	})

	arg_1_0.activityId = arg_1_1

def var_0_0.IsActiveType(arg_2_0):
	return True

local function var_0_1(arg_3_0, arg_3_1, arg_3_2)
	if arg_3_1 == "<=":
		return arg_3_0 <= arg_3_2
	elif arg_3_1 == "<":
		return arg_3_0 < arg_3_2
	elif arg_3_1 == "==":
		return arg_3_0 == arg_3_2
	elif arg_3_1 == ">=":
		return arg_3_2 <= arg_3_0
	elif arg_3_1 == ">":
		return arg_3_2 < arg_3_0

	return False

def var_0_0.isActivate(arg_4_0):
	local var_4_0 = False
	local var_4_1 = getProxy(ActivityProxy).getActivityById(arg_4_0.activityId)

	if var_4_1 and not var_4_1.isEnd():
		if var_4_1.getConfig("type") == ActivityConst.ACTIVITY_TYPE_BUFF:
			if arg_4_0.RookieBattleExpUsage():
				if getProxy(PlayerProxy).getRawData().level < arg_4_0.GetRookieBattleExpMaxLevel():
					var_4_0 = True
			elif arg_4_0.isAddedBuff():
				var_4_0 = True
		else
			var_4_0 = (function()
				local var_5_0 = arg_4_0.getConfig("benefit_condition")

				if var_5_0[1] == "lv":
					local var_5_1 = getProxy(PlayerProxy).getRawData()

					return var_0_1(var_5_1.level, var_5_0[2], var_5_0[3])
				elif var_5_0[1] == "activity":
					if var_5_0[3] == 0:
						return True

					if var_4_1.getConfig("type") == ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF or var_4_1.getConfig("type") == ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF_2:
						local var_5_2 = var_5_0[3][1]

						return (var_4_1.data1KeyValueList[2][var_5_2] or 1) == var_5_0[3][2]

				if var_5_0 == "":
					return True)() or False

	return var_4_0

def var_0_0.getLeftTime(arg_6_0):
	local var_6_0 = pg.TimeMgr.GetInstance().GetServerTime()

	return getProxy(ActivityProxy).getActivityById(arg_6_0.activityId).stopTime - var_6_0

def var_0_0.isAddedBuff(arg_7_0):
	local var_7_0 = True
	local var_7_1 = getProxy(ActivityProxy).getActivityById(arg_7_0.activityId)

	if var_7_1 and not var_7_1.isEnd():
		local var_7_2 = arg_7_0.getConfig("benefit_condition")

		if var_7_2[1] == "pt":
			local var_7_3 = var_7_2[2]
			local var_7_4 = var_7_2[3]
			local var_7_5 = var_7_2[4]
			local var_7_6 = pg.player_resource[var_7_3].name
			local var_7_7 = getProxy(PlayerProxy).getData()[var_7_6] or 0

			if not (var_7_4 <= var_7_7) or not (var_7_7 < var_7_5):
				var_7_0 = False

	return var_7_0

return var_0_0
