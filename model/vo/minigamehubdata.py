local var_0_0 = class("MiniGameHubData", import(".BaseVO"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.id = arg_1_1.id
	arg_1_0.configId = arg_1_1.id
	arg_1_0.count = arg_1_1.available_cnt or arg_1_0.getConfig("reborn_times")
	arg_1_0.usedtime = arg_1_1.used_cnt or 0
	arg_1_0.ultimate = arg_1_1.ultimate or 0
	arg_1_0.highScores = {}

	underscore.each(arg_1_1.maxscores or {}, function(arg_2_0)
		arg_1_0.highScores[arg_2_0.key] = {
			arg_2_0.value1,
			arg_2_0.value2
		})

def var_0_0.bindConfigTable(arg_3_0):
	return pg.mini_game_hub

def var_0_0.UpdateData(arg_4_0, arg_4_1):
	arg_4_0.count = arg_4_1.available_cnt or arg_4_0.count
	arg_4_0.usedtime = arg_4_1.used_cnt or arg_4_0.usedtime
	arg_4_0.ultimate = arg_4_1.ultimate or arg_4_0.ultimate

	local var_4_0 = arg_4_1.maxscores

	underscore.each(arg_4_1.maxscores or {}, function(arg_5_0)
		arg_4_0.highScores[arg_5_0.key] = {
			arg_5_0.value1,
			arg_5_0.value2
		})
	print("Hub 更新", "ID.", tostring(arg_4_0.id), "Count.", tostring(arg_4_0.count), "UsedTime.", tostring(arg_4_0.usedtime), "Ultimate.", tostring(arg_4_0.ultimate))

def var_0_0.CheckInTime(arg_6_0):
	local var_6_0 = arg_6_0.getConfig("act_id")

	if var_6_0 != None:
		local var_6_1 = pg.activity_template[var_6_0]

		if var_6_1:
			local var_6_2 = var_6_1.time

			return (pg.TimeMgr.GetInstance().inTime(var_6_2))
	else
		return True

return var_0_0
