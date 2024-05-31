local var_0_0 = class("WorldBossMediator", import("...base.ContextMediator"))

var_0_0.ON_BATTLE = "WorldBossMediator.ON_BATTLE"
var_0_0.ON_RANK_LIST = "WorldBossMediator.ON_RANK_LIST"
var_0_0.ON_FETCH_BOSS = "WorldBossMediator.ON_FETCH_BOSS"
var_0_0.ON_SURPPORT = "WorldBossMediator.ON_SURPPORT"
var_0_0.ON_SUBMIT_AWARD = "WorldBossMediator.ON_SUBMIT_AWARD"
var_0_0.ON_SELF_BOSS_OVERTIME = "WorldBossMediator.ON_SELF_BOSS_OVERTIME"
var_0_0.ON_ACTIVE_BOSS = "WorldBossMediator.ON_ACTIVE_BOSS"
var_0_0.GET_RANK_CNT = "WorldBossMediator.GET_RANK_CNT"
var_0_0.UPDATE_CACHE_BOSS_HP = "WorldBossMediator.UPDATE_CACHE_BOSS_HP"
var_0_0.GO_META = "WorldBossMediator.GO_META"
var_0_0.FETCH_RANK_FORMATION = "WorldBossMediator.FETCH_RANK_FORMATION"
var_0_0.ON_SWITCH_ARCHIVES = "WorldBossMediator.ON_SWITCH_ARCHIVES"
var_0_0.ON_ACTIVE_ARCHIVES_BOSS = "WorldBossMediator.ON_ACTIVE_ARCHIVES_BOSS"
var_0_0.ON_ARCHIVES_BOSS_AUTO_BATTLE = "WorldBossMediator.ON_ARCHIVES_BOSS_AUTO_BATTLE"
var_0_0.ON_ARCHIVES_BOSS_STOP_AUTO_BATTLE = "WorldBossMediator.ON_ARCHIVES_BOSS_STOP_AUTO_BATTLE"
var_0_0.ON_ARCHIVES_BOSS_AUTO_BATTLE_TIMEOVER = "WorldBossMediator.ON_ARCHIVES_BOSS_AUTO_BATTLE_TIMEOVER"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.ON_ARCHIVES_BOSS_STOP_AUTO_BATTLE, function(arg_2_0, arg_2_1)
		arg_1_0.sendNotification(GAME.WORLD_ARCHIVES_BOSS_STOP_AUTO_BATTLE, {
			id = arg_2_1,
			type = WorldBossConst.STOP_AUTO_BATTLE_MANUAL
		}))
	arg_1_0.bind(var_0_0.ON_ARCHIVES_BOSS_AUTO_BATTLE_TIMEOVER, function(arg_3_0, arg_3_1)
		arg_1_0.sendNotification(GAME.WORLD_ARCHIVES_BOSS_STOP_AUTO_BATTLE, {
			id = arg_3_1,
			type = WorldBossConst.STOP_AUTO_BATTLE_TIMEOVER
		}))
	arg_1_0.bind(var_0_0.ON_ARCHIVES_BOSS_AUTO_BATTLE, function(arg_4_0, arg_4_1)
		arg_1_0.sendNotification(GAME.WORLD_ARCHIVES_BOSS_AUTO_BATTLE, {
			id = arg_4_1
		}))
	arg_1_0.bind(var_0_0.ON_ACTIVE_ARCHIVES_BOSS, function(arg_5_0)
		local var_5_0 = nowWorld().GetBossProxy().GetArchivesId()

		arg_1_0.sendNotification(GAME.WORLD_ACTIVE_WORLD_BOSS, {
			id = var_5_0,
			type = WorldBossConst.BOSS_TYPE_ARCHIVES
		}))
	arg_1_0.bind(var_0_0.ON_ACTIVE_BOSS, function(arg_6_0, arg_6_1)
		arg_1_0.sendNotification(GAME.WORLD_ACTIVE_WORLD_BOSS, {
			id = arg_6_1,
			type = WorldBossConst.BOSS_TYPE_CURR
		}))
	arg_1_0.bind(var_0_0.ON_SWITCH_ARCHIVES, function(arg_7_0, arg_7_1)
		arg_1_0.sendNotification(GAME.SWITCH_WORLD_BOSS_ARCHIVES, {
			id = arg_7_1
		}))
	arg_1_0.bind(var_0_0.FETCH_RANK_FORMATION, function(arg_8_0, arg_8_1, arg_8_2)
		arg_1_0.sendNotification(GAME.WORLD_BOSS_GET_FORMATION, {
			bossId = arg_8_2,
			userId = arg_8_1
		}))
	arg_1_0.bind(var_0_0.GO_META, function(arg_9_0, arg_9_1)
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.METACHARACTER, {
			autoOpenSyn = True,
			autoOpenShipConfigID = arg_9_1 * 10 + 1
		}))
	arg_1_0.bind(var_0_0.ON_SELF_BOSS_OVERTIME, function(arg_10_0)
		arg_1_0.sendNotification(GAME.WORLD_SELF_BOSS_OVERTIME))
	arg_1_0.bind(var_0_0.ON_SUBMIT_AWARD, function(arg_11_0, arg_11_1)
		arg_1_0.sendNotification(GAME.WORLD_BOSS_SUBMIT_AWARD, {
			bossId = arg_11_1
		}))
	arg_1_0.bind(var_0_0.ON_SURPPORT, function(arg_12_0, arg_12_1)
		if arg_12_1[3] == True:
			arg_1_0.sendNotification(GAME.WORLD_BOSS_SUPPORT, {
				type = WorldBoss.SUPPORT_TYPE_WORLD
			})

		if arg_12_1[1] == True:
			arg_1_0.sendNotification(GAME.WORLD_BOSS_SUPPORT, {
				type = WorldBoss.SUPPORT_TYPE_FRIEND
			})

		if arg_12_1[2] == True:
			arg_1_0.sendNotification(GAME.WORLD_BOSS_SUPPORT, {
				type = WorldBoss.SUPPORT_TYPE_GUILD
			}))
	arg_1_0.bind(var_0_0.ON_FETCH_BOSS, function(arg_13_0)
		arg_1_0.updateBossProxy())
	arg_1_0.bind(var_0_0.ON_BATTLE, function(arg_14_0, arg_14_1, arg_14_2)
		arg_1_0.sendNotification(GAME.WORLD_BOSS_START_BATTLE, {
			bossId = arg_14_1,
			isOther = arg_14_2
		}))
	arg_1_0.bind(var_0_0.ON_RANK_LIST, function(arg_15_0, arg_15_1)
		arg_1_0.sendNotification(GAME.WORLD_GET_BOSS_RANK, {
			bossId = arg_15_1
		}))
	arg_1_0.bind(var_0_0.GET_RANK_CNT, function(arg_16_0, arg_16_1, arg_16_2)
		local var_16_0 = arg_1_0.viewComponent.bossProxy.GetRank(arg_16_1)

		if not var_16_0:
			arg_1_0.sendNotification(GAME.WORLD_GET_BOSS_RANK, {
				bossId = arg_16_1,
				callback = arg_16_2
			})
		else
			arg_16_2(#var_16_0))
	arg_1_0.bind(var_0_0.UPDATE_CACHE_BOSS_HP, function(arg_17_0, arg_17_1)
		arg_1_0.sendNotification(GAME.GET_CACHE_BOSS_HP, {
			callback = arg_17_1
		}))

def var_0_0.updateBossProxy(arg_18_0):
	local var_18_0 = nowWorld().GetBossProxy()
	local var_18_1 = getProxy(MetaCharacterProxy)

	arg_18_0.viewComponent.SetBossProxy(var_18_0, var_18_1)

	if not WorldBossScene.inOtherBossBattle and not arg_18_0.contextData.worldBossId and not var_18_0.ExistSelfBossAward():
		local var_18_2 = var_18_0.GetCanGetAwardBoss()

		if var_18_2:
			arg_18_0.contextData.worldBossId = var_18_2.id

	if WorldBossScene.inOtherBossBattle or arg_18_0.contextData.worldBossId:
		local var_18_3 = var_18_0.GetCacheBoss(arg_18_0.contextData.worldBossId)

		if var_18_3 and not WorldBossConst._IsCurrBoss(var_18_3):
			arg_18_0.viewComponent.SwitchPage(WorldBossScene.PAGE_ARCHIVES_CHALLENGE)
		else
			arg_18_0.viewComponent.SwitchPage(WorldBossScene.PAGE_CHALLENGE)
	else
		arg_18_0.viewComponent.SwitchPage(WorldBossScene.PAGE_ENTRANCE)

def var_0_0.listNotificationInterests(arg_19_0):
	return {
		GAME.WORLD_GET_BOSS_DONE,
		GAME.WORLD_BOSS_SUPPORT_DONE,
		GAME.WORLD_BOSS_SUBMIT_AWARD_DONE,
		GAME.REMOVE_LAYERS,
		GAME.WORLD_BOSS_GET_FORMATION_DONE,
		GAME.SWITCH_WORLD_BOSS_ARCHIVES_DONE,
		GAME.WORLD_ARCHIVES_BOSS_STOP_AUTO_BATTLE_DONE,
		GAME.WORLD_ARCHIVES_BOSS_AUTO_BATTLE_DONE,
		GAME.GET_META_PT_AWARD_DONE
	}

def var_0_0.handleNotification(arg_20_0, arg_20_1):
	local var_20_0 = arg_20_1.getName()
	local var_20_1 = arg_20_1.getBody()

	if var_20_0 == GAME.WORLD_GET_BOSS_DONE:
		arg_20_0.updateBossProxy()
	elif var_20_0 == GAME.WORLD_BOSS_SUPPORT_DONE:
		pg.TipsMgr.GetInstance().ShowTips(i18n("world_joint_call_support_success"))
	elif var_20_0 == GAME.WORLD_BOSS_SUBMIT_AWARD_DONE:
		arg_20_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_20_1.items)
		arg_20_0.viewComponent.getAwardDone()
	elif var_20_0 == GAME.REMOVE_LAYERS:
		if not var_20_1.onHome and var_20_1.context.mediator == WorldBossFormationMediator:
			arg_20_0.viewComponent.OnRemoveLayers()
	elif var_20_0 == GAME.WORLD_BOSS_GET_FORMATION_DONE:
		arg_20_0.viewComponent.OnShowFormationPreview(var_20_1.ships)
	elif var_20_0 == GAME.SWITCH_WORLD_BOSS_ARCHIVES_DONE:
		arg_20_0.viewComponent.OnSwitchArchives()
		pg.TipsMgr.GetInstance().ShowTips(i18n("world_boss_switch_archives_success"))
	elif var_20_0 == GAME.WORLD_ARCHIVES_BOSS_STOP_AUTO_BATTLE_DONE:
		arg_20_0.viewComponent.OnAutoBattleResult(var_20_1)
	elif var_20_0 == GAME.WORLD_ARCHIVES_BOSS_AUTO_BATTLE_DONE:
		arg_20_0.viewComponent.OnAutoBattleStart(var_20_1)
	elif var_20_0 == GAME.GET_META_PT_AWARD_DONE:
		arg_20_0.viewComponent.OnGetMetaAwards()
		arg_20_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_20_1.awards)

return var_0_0
