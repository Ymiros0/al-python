local var_0_0 = class("GuildEventBaseCommand", pm.SimpleCommand)

def var_0_0.ExistGuild(arg_1_0):
	if not getProxy(GuildProxy).getRawData():
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_not_exist"))

		return False

	return True

def var_0_0.ExistEvent(arg_2_0, arg_2_1):
	if not getProxy(GuildProxy).getRawData().GetEventById(arg_2_1):
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_not_exist_battle"))

		return False

	return True

def var_0_0.ExistActiveEvent(arg_3_0):
	if not arg_3_0.ExistGuild():
		return False

	local var_3_0 = getProxy(GuildProxy).getRawData().GetActiveEvent()

	if not var_3_0 or var_3_0 and var_3_0.IsExpired():
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_battle_is_end"))

		return False

	return True

def var_0_0.NotExistActiveEvent(arg_4_0):
	if getProxy(GuildProxy).getRawData().GetActiveEvent():
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_battle_is_exist"))

		return False

	return True

def var_0_0.ExistMission(arg_5_0, arg_5_1):
	if not arg_5_0.ExistActiveEvent():
		return False

	local var_5_0 = getProxy(GuildProxy).getRawData().GetActiveEvent()

	if arg_5_1 and var_5_0.GetMissionById(arg_5_1) == None:
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_event_not_exist"))

		return False

	return True

def var_0_0.GetMissionById(arg_6_0, arg_6_1):
	if arg_6_0.ExistMission(arg_6_1):
		return getProxy(GuildProxy).getRawData().GetActiveEvent().GetMissionById(arg_6_1)

def var_0_0.CanFormationMission(arg_7_0, arg_7_1):
	if not arg_7_0.ExistMission(arg_7_1):
		return False

	if getProxy(GuildProxy).getRawData().GetActiveEvent().GetMissionById(arg_7_1).GetCanFormationIndex() == -1:
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_fleet_can_not_edit"))

		return False

	return True

def var_0_0.ExistBoss(arg_8_0):
	if not arg_8_0.ExistActiveEvent():
		return False

	local var_8_0 = getProxy(GuildProxy).getRawData().GetActiveEvent().GetBossMission()

	if not var_8_0 or not var_8_0.IsActive():
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_not_exist_boss"))

		return False

	return True

def var_0_0.IsAnim(arg_9_0):
	local var_9_0 = getProxy(GuildProxy).getRawData()

	if not GuildMember.IsAdministrator(var_9_0.getSelfDuty()):
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_commander_and_sub_op"))

		return False

	return True

def var_0_0.CheckCapital(arg_10_0, arg_10_1, arg_10_2):
	if getProxy(GuildProxy).getRawData().getCapital() < arg_10_1.GetConsume():
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_guildgold_no_enough_for_battle"))

		return False

	return True

return var_0_0
