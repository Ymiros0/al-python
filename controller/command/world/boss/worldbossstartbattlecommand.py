local var_0_0 = class("WorldBossStartBattleCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.bossId
	local var_1_2 = var_1_0.isOther
	local var_1_3 = nowWorld().GetBossProxy()
	local var_1_4 = var_1_3.GetBossById(var_1_1)

	if not var_1_4:
		pg.TipsMgr.GetInstance().ShowTips(i18n("world_joint_boss_not_found"))

		return

	if var_1_2 and var_1_3.GetPt() <= 0 and WorldBossConst._IsCurrBoss(var_1_4):
		pg.TipsMgr.GetInstance().ShowTips(i18n("world_joint_count_no_enough"))

		return

	local function var_1_5()
		local var_2_0 = var_1_4.GetStageID()
		local var_2_1 = getProxy(ContextProxy).getCurrentContext()

		pg.m02.retrieveMediator(var_2_1.mediator.__cname).addSubLayers(Context.New({
			mediator = WorldBossFormationMediator,
			viewComponent = WorldBossFormationLayer,
			data = {
				actID = 0,
				stageId = var_2_0,
				bossId = var_1_1,
				system = SYSTEM_WORLD_BOSS,
				isOther = var_1_2
			}
		}))

	local function var_1_6()
		var_1_3.RemoveCacheBoss(var_1_4.id)

	arg_1_0.sendNotification(GAME.CHECK_WORLD_BOSS_STATE, {
		bossId = var_1_1,
		time = var_1_4.lastTime,
		callback = var_1_5,
		failedCallback = var_1_6
	})

return var_0_0
