local var_0_0 = class("GuildEventTimerView")

def var_0_0.Flush(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.text = arg_1_1

	arg_1_0.RemoveEndEventTimer()

	local var_1_0 = arg_1_2.GetLeftTime()

	if var_1_0 < 86400:
		arg_1_0.timer = Timer.New(function()
			local var_2_0 = arg_1_2.GetLeftTime()

			arg_1_0.UpdateText("<size=31><color=#FF3838>" .. pg.TimeMgr.GetInstance().DescCDTime(var_2_0) .. "</color></size>")

			if var_2_0 <= 0:
				arg_1_0.OnOver(), 1, -1)

		arg_1_0.timer.func()
	else
		local var_1_1, var_1_2, var_1_3, var_1_4 = pg.TimeMgr.GetInstance().parseTimeFrom(var_1_0)

		assert(var_1_1 > 0)

		if var_1_2 <= 0 and (var_1_3 > 0 or var_1_4 > 0):
			var_1_2 = var_1_2 + 1

		local var_1_5 = string.format("%s" .. i18n("word_date") .. "%s" .. i18n("word_hour"), var_1_1, var_1_2)

		if var_1_1 < 7:
			var_1_5 = "<size=31><color=#FF3838>" .. var_1_5 .. "</color></size>"

		arg_1_0.UpdateText(var_1_5)

		local var_1_6 = var_1_3 * 60 + var_1_4

		if var_1_6 <= 0:
			var_1_6 = 3600

		local var_1_7 = math.min(var_1_0 - 86400, var_1_6)

		arg_1_0.timer = Timer.New(function()
			arg_1_0.Flush(arg_1_1, arg_1_2), var_1_7 + 2, 1)

	arg_1_0.timer.Start()

def var_0_0.UpdateText(arg_4_0, arg_4_1):
	arg_4_0.text.text = arg_4_1

def var_0_0.RemoveEndEventTimer(arg_5_0):
	if arg_5_0.timer:
		arg_5_0.timer.Stop()

		arg_5_0.timer = None

def var_0_0.OnOver(arg_6_0):
	arg_6_0.RemoveEndEventTimer()
	pg.m02.sendNotification(GAME.GUILD_GET_ACTIVATION_EVENT, {
		force = True
	})

def var_0_0.Dispose(arg_7_0):
	arg_7_0.RemoveEndEventTimer()

return var_0_0
