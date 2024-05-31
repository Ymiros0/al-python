local var_0_0 = class("MainGuildSequence")

def var_0_0.Ctor(arg_1_0):
	arg_1_0.ignores = {}
	arg_1_0.refreshTime = pg.TimeMgr.GetInstance().GetServerTime()

def var_0_0.Execute(arg_2_0, arg_2_1):
	local var_2_0 = getProxy(GuildProxy).getRawData()

	if not var_2_0:
		arg_2_1()

		return

	local var_2_1 = var_2_0.GetActiveEvent()

	if not var_2_1 or not var_2_1.IsParticipant():
		arg_2_1()

		return

	local var_2_2, var_2_3 = var_2_1.AnyMissionFirstFleetCanFroamtion()

	if var_2_2 and var_2_3 and table.contains(arg_2_0.ignores, var_2_3.id):
		arg_2_1()

		return

	if var_2_2:
		arg_2_0.Notify(arg_2_1)
	elif pg.TimeMgr.GetInstance().GetServerTime() - arg_2_0.refreshTime > 900:
		arg_2_0.RefreshEvent(var_2_1, False, arg_2_1)
	else
		arg_2_0.Notify(arg_2_1)

def var_0_0.RefreshEvent(arg_3_0, arg_3_1, arg_3_2, arg_3_3):
	local var_3_0 = arg_3_1.GetUnlockMission()

	if var_3_0 and (not arg_3_2 or var_3_0.id != arg_3_2.id):
		pg.m02.sendNotification(GAME.GUILD_REFRESH_MISSION, {
			force = True,
			id = var_3_0.id,
			def callback:()
				arg_3_0.RefreshEvent(arg_3_1, var_3_0, arg_3_3)
		})

		arg_3_0.refreshTime = pg.TimeMgr.GetInstance().GetServerTime()
	else
		arg_3_0.Notify(arg_3_3)

def var_0_0.Notify(arg_5_0, arg_5_1):
	pg.GuildMsgBoxMgr.GetInstance().Notification({
		def condition:()
			local var_6_0, var_6_1 = getProxy(GuildProxy).getRawData().GetActiveEvent().AnyMissionFirstFleetCanFroamtion()

			if var_6_0 and not table.contains(arg_5_0.ignores, var_6_1.id):
				table.insert(arg_5_0.ignores, var_6_1.id)

				return True

			return False,
		content = i18n("guild_operation_event_occurrence"),
		def OnYes:()
			pg.m02.sendNotification(GAME.GO_SCENE, SCENE.GUILD, {
				page = "battle"
			}),
		OnNo = arg_5_1
	})

def var_0_0.Dispose(arg_8_0):
	arg_8_0.ignores = {}
	arg_8_0.refreshTime = None

return var_0_0
