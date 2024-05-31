local var_0_0 = class("WorldBossConst")

var_0_0.WORLD_BOSS_ITEM_ID = 100000
var_0_0.WORLD_PAST_BOSS_ITEM_ID = 100002
var_0_0.ACHIEVE_STATE_NOSTART = 1
var_0_0.ACHIEVE_STATE_STARTING = 2
var_0_0.ACHIEVE_STATE_CLEAR = 3
var_0_0.BOSS_TYPE_CURR = 1
var_0_0.BOSS_TYPE_ARCHIVES = 2
var_0_0.STOP_AUTO_BATTLE_MANUAL = 1
var_0_0.STOP_AUTO_BATTLE_TIMEOVER = 2
var_0_0.AUTO_BATTLE_STATE_NORMAL = 0
var_0_0.AUTO_BATTLE_STATE_LOCK = 1
var_0_0.AUTO_BATTLE_STATE_STARTING = 2
var_0_0.AUTO_BATTLE_STATE_HIDE = 3

def var_0_0.__IsCurrBoss(arg_1_0):
	return var_0_0.GetCurrBossID() == arg_1_0

def var_0_0.IsAchieveBoss(arg_2_0):
	local var_2_0 = var_0_0.GetAchieveBossIdList()

	return table.contains(var_2_0, arg_2_0)

def var_0_0.IsCurrBoss(arg_3_0):
	return var_0_0.GetCurrBossGroup() == arg_3_0

def var_0_0._IsCurrBoss(arg_4_0):
	local var_4_0 = arg_4_0.config.id

	return var_0_0.GetCurrBossID() == var_4_0

def var_0_0.GetCurrBossGroup():
	local var_5_0 = pg.world_joint_boss_template

	for iter_5_0 = #var_5_0.all, 1, -1:
		local var_5_1 = var_5_0.all[iter_5_0]

		if type(var_5_0[var_5_1].state) == "table" and pg.TimeMgr.GetInstance().inTime(var_5_0[var_5_1].state):
			return var_5_0[var_5_1].meta_id

	return None

def var_0_0.GetCurrBossID():
	local var_6_0 = pg.world_joint_boss_template

	for iter_6_0 = #var_6_0.all, 1, -1:
		local var_6_1 = var_6_0.all[iter_6_0]

		if type(var_6_0[var_6_1].state) == "table" and pg.TimeMgr.GetInstance().inTime(var_6_0[var_6_1].state):
			return var_6_0[var_6_1].id

	return None

def var_0_0.GetCurrBossLeftDay():
	local var_7_0 = var_0_0.GetCurrBossID()
	local var_7_1 = pg.world_joint_boss_template[var_7_0]
	local var_7_2 = pg.TimeMgr.GetInstance().GetServerTime()
	local var_7_3 = pg.TimeMgr.GetInstance().parseTimeFromConfig(var_7_1.state[2])
	local var_7_4 = var_7_3 - var_7_2

	return pg.TimeMgr.GetInstance().DiffDay(var_7_2, var_7_3), var_7_4 % 86400

def var_0_0.GetCurrBossDayIndex():
	local var_8_0 = var_0_0.GetCurrBossID()
	local var_8_1 = pg.world_joint_boss_template[var_8_0]
	local var_8_2 = pg.TimeMgr.GetInstance().parseTimeFromConfig(var_8_1.state[1])
	local var_8_3 = pg.TimeMgr.GetInstance()
	local var_8_4 = var_8_3.GetServerTime()

	return var_8_3.DiffDay(var_8_2, var_8_4) + 1

def var_0_0.GetCurrBossStartTimeAndEndTime():
	local var_9_0 = var_0_0.GetCurrBossID()

	return pg.world_joint_boss_template[var_9_0].state

def var_0_0.GetCurrBossConsume():
	local var_10_0 = pg.gameset.curr_boss_ticket.description
	local var_10_1 = var_10_0[1]
	local var_10_2 = var_10_0[2]
	local var_10_3 = var_10_0[3]

	return var_10_1, var_10_2, var_10_3

def var_0_0.GetCurrBossItemProgress():
	return nowWorld().worldBossProxy.GetSummonPt()

def var_0_0.GetCurrBossItemAcc():
	return nowWorld().worldBossProxy.GetSummonPtDailyAcc()

def var_0_0.CanUnlockCurrBoss():
	return var_0_0.GetCurrBossItemProgress() >= var_0_0.GetCurrBossConsume()

def var_0_0.GetCurrBossItemCapacity():
	local var_14_0 = var_0_0.GetCurrBossItemProgress()
	local var_14_1 = var_0_0.GetCurrBossItemAcc()
	local var_14_2, var_14_3, var_14_4 = var_0_0.GetCurrBossConsume()

	return var_14_0, var_14_1, var_14_3, var_14_4

def var_0_0.GetAchieveBossConsume():
	local var_15_0 = pg.gameset.past_joint_boss_ticket.description
	local var_15_1 = var_15_0[1]
	local var_15_2 = var_15_0[2]
	local var_15_3 = var_15_0[3]

	return var_15_1, var_15_2, var_15_3

def var_0_0.GetAchieveBossItemProgress():
	return nowWorld().worldBossProxy.GetSummonPtOld()

def var_0_0.GetSummonPtOldAcc():
	return nowWorld().worldBossProxy.GetSummonPtOldAcc()

def var_0_0.CanUnlockArchivesBoss():
	return var_0_0.GetAchieveBossItemProgress() >= var_0_0.GetAchieveBossConsume()

def var_0_0.GetAchieveBossItemCapacity():
	local var_19_0 = var_0_0.GetAchieveBossItemProgress()
	local var_19_1 = var_0_0.GetSummonPtOldAcc()
	local var_19_2, var_19_3, var_19_4 = var_0_0.GetAchieveBossConsume()

	return var_19_0, var_19_1, var_19_3, var_19_4

def var_0_0.GetAchieveBossIdList():
	local var_20_0 = {}
	local var_20_1 = pg.world_joint_boss_template

	for iter_20_0 = 1, #var_20_1.all:
		local var_20_2 = var_20_1.all[iter_20_0]

		if var_20_1[var_20_2].state == "always":
			table.insert(var_20_0, var_20_1[var_20_2].meta_id)

	return var_20_0

def var_0_0.GetAchieveBossList():
	local var_21_0 = {}
	local var_21_1 = pg.world_joint_boss_template

	for iter_21_0 = 1, #var_21_1.all:
		local var_21_2 = var_21_1.all[iter_21_0]

		if var_21_1[var_21_2].state == "always":
			table.insert(var_21_0, var_21_1[var_21_2])

	return var_21_0

def var_0_0.GetCurrBossItemInfo():
	local var_22_0, var_22_1, var_22_2, var_22_3 = WorldBossConst.GetCurrBossItemCapacity()
	local var_22_4 = i18n("world_boss_item_info")
	local var_22_5 = string.split(var_22_4, "|")
	local var_22_6 = var_22_5[2]

	for iter_22_0, iter_22_1 in ipairs({
		var_22_1,
		var_22_2,
		var_22_0,
		var_22_3
	}):
		var_22_6 = string.gsub(var_22_6, "$" .. iter_22_0, iter_22_1)

	return {
		rarity = 4,
		name = var_22_5[1],
		display = var_22_6,
		icon = {
			"Props/world_boss_record"
		}
	}

def var_0_0.GetAchieveBossItemInfo():
	local var_23_0, var_23_1, var_23_2, var_23_3 = WorldBossConst.GetAchieveBossItemCapacity()
	local var_23_4 = i18n("world_past_boss_item_info")
	local var_23_5 = string.split(var_23_4, "|")
	local var_23_6 = var_23_5[2]

	for iter_23_0, iter_23_1 in ipairs({
		var_23_1,
		var_23_2,
		var_23_0,
		var_23_3
	}):
		var_23_6 = string.gsub(var_23_6, "$" .. iter_23_0, iter_23_1)

	return {
		rarity = 4,
		name = var_23_5[1],
		display = var_23_6,
		icon = {
			"Props/world_past_boss_record"
		}
	}

def var_0_0.IsClearAllAchieveBoss():
	local var_24_0 = var_0_0.GetAchieveBossIdList()

	return _.all(var_24_0, function(arg_25_0)
		return not getProxy(MetaCharacterProxy).getMetaProgressVOByID(arg_25_0).metaPtData.CanGetNextAward())

def var_0_0.GetArchivesId():
	return nowWorld().GetBossProxy().GetArchivesId()

def var_0_0.GetAchieveState():
	local var_27_0 = var_0_0.GetArchivesId()

	if var_27_0 == 0:
		return var_0_0.ACHIEVE_STATE_NOSTART

	if #var_0_0.GetAchieveBossIdList() == 0:
		return var_0_0.ACHIEVE_STATE_NOSTART
	elif var_0_0.IsClearAllAchieveBoss():
		return var_0_0.ACHIEVE_STATE_CLEAR
	else
		local var_27_1 = pg.world_joint_boss_template[var_27_0].meta_id
		local var_27_2 = getProxy(MetaCharacterProxy).getMetaProgressVOByID(var_27_1)

		if not var_27_2.metaPtData.CanGetNextAward() or var_27_2.metaPtData.IsMaxPt():
			return var_0_0.ACHIEVE_STATE_NOSTART
		else
			return var_0_0.ACHIEVE_STATE_STARTING

def var_0_0.GetBossOilConsume(arg_28_0):
	local var_28_0 = pg.gameset.joint_boss_oil_consume.description

	arg_28_0 = math.min(arg_28_0, #var_28_0)

	return var_28_0[arg_28_0]

def var_0_0.GetArchivesBossAutoBattleSecond():
	return pg.gameset.past_joint_boss_autofight_time.key_value

def var_0_0.GetArchivesBossAutoBattleMinute():
	local var_30_0 = var_0_0.GetArchivesBossAutoBattleSecond()

	return math.ceil(var_30_0 / 60)

def var_0_0.GetHighestDamage():
	local var_31_0 = nowWorld().GetBossProxy()

	return math.max(var_31_0.GetHighestDamage(), 1)

def var_0_0.GetAutoBattleCnt():
	local var_32_0 = nowWorld().GetBossProxy().GetSelfBoss()
	local var_32_1 = var_0_0.GetHighestDamage()

	return math.ceil(var_32_0.hp / var_32_1)

def var_0_0.GetAutoBattleOilConsume():
	local var_33_0 = var_0_0.GetAutoBattleCnt()
	local var_33_1 = nowWorld().GetBossProxy().GetSelfBoss()
	local var_33_2 = 0
	local var_33_3 = var_33_1.fightCount

	for iter_33_0 = var_33_3 + 1, var_33_3 + var_33_0:
		var_33_2 = var_33_2 + WorldBossConst.GetBossOilConsume(iter_33_0)

	return var_33_2

def var_0_0.InAutoBattle():
	return nowWorld().GetBossProxy().InAutoBattle()

def var_0_0.GetAutoBattleLeftTime():
	return nowWorld().GetBossProxy().GetAutoBattleFinishTime() - pg.TimeMgr.GetInstance().GetServerTime()

def var_0_0.GetAutoBattleState(arg_36_0):
	if not arg_36_0 or arg_36_0.isDeath():
		return var_0_0.AUTO_BATTLE_STATE_HIDE

	if WorldBossConst.InAutoBattle():
		return var_0_0.AUTO_BATTLE_STATE_STARTING
	elif arg_36_0.isDeath():
		return var_0_0.AUTO_BATTLE_STATE_HIDE
	elif arg_36_0.GetSelfFightCnt() <= 0 or nowWorld().GetBossProxy().GetHighestDamage() <= 0:
		return var_0_0.AUTO_BATTLE_STATE_LOCK
	else
		return var_0_0.AUTO_BATTLE_STATE_NORMAL

def var_0_0.BossId2MetaId(arg_37_0):
	return pg.world_joint_boss_template[arg_37_0].meta_id

def var_0_0.MetaId2BossId(arg_38_0):
	for iter_38_0, iter_38_1 in ipairs(pg.world_joint_boss_template.all):
		if var_0_0.BossId2MetaId(iter_38_1) == arg_38_0:
			return iter_38_1

def var_0_0.AnyArchivesBossCanGetAward():
	return _.any(var_0_0.GetAchieveBossIdList(), function(arg_40_0)
		return getProxy(MetaCharacterProxy).getMetaProgressVOByID(arg_40_0).metaPtData.CanGetAward())

def var_0_0.GetCommissionSceneMetaBossBtnState():
	local var_41_0 = nowWorld()

	if not var_41_0 or not var_41_0.IsActivate():
		return CommissionMetaBossBtn.STATE_LOCK

	local var_41_1 = var_41_0.GetBossProxy()

	if not var_41_1 or not var_41_1.isSetup or not var_41_1.IsOpen():
		return CommissionMetaBossBtn.STATE_LOCK

	local var_41_2 = var_41_1.GetSelfBoss()

	if var_41_2 and WorldBossConst.GetAutoBattleState(var_41_2) == WorldBossConst.AUTO_BATTLE_STATE_STARTING:
		if WorldBossConst.GetAutoBattleLeftTime() > 0:
			return CommissionMetaBossBtn.STATE_AUTO_BATTLE
		else
			return CommissionMetaBossBtn.STATE_FINSH_BATTLE

	if var_41_1.NeedTip() or WorldBossConst.AnyArchivesBossCanGetAward():
		return CommissionMetaBossBtn.STATE_GET_AWARDS

	return CommissionMetaBossBtn.STATE_NORMAL

return var_0_0
