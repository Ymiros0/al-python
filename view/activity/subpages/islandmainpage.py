local var_0_0 = class("IslandMainPage", import(".TemplatePage.PreviewTemplatePage"))

def var_0_0.initBtn(arg_1_0):
	var_0_0.super.initBtn(arg_1_0)

	function arg_1_0.btnFuncList.shop(arg_2_0)
		onButton(arg_1_0, arg_2_0, function()
			local var_3_0 = underscore.detect(getProxy(ActivityProxy).getActivitiesByType(ActivityConst.ACTIVITY_TYPE_SHOP), function(arg_4_0)
				return arg_4_0.getConfig("config_id") == 3)

			if not var_3_0 or var_3_0.isEnd():
				pg.TipsMgr.GetInstance().ShowTips(i18n("challenge_end_tip"))

				return

			local var_3_1 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_ISLAND)

			if var_3_1 and not var_3_1.isEnd():
				arg_1_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.ANNIVERSARY_ISLAND_SEA, {
					wraps = SixthAnniversaryIslandScene.SHOP
				})
			else
				arg_1_0.emit(ActivityMediator.OPEN_LAYER, Context.New({
					mediator = SixthAnniversaryIslandShopMediator,
					viewComponent = SixthAnniversaryIslandShopLayer
				})), SFX_PANEL)

	function arg_1_0.btnFuncList.activity(arg_5_0)
		onButton(arg_1_0, arg_5_0, function()
			local var_6_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_ISLAND)

			if not var_6_0 or var_6_0.isEnd():
				pg.TipsMgr.GetInstance().ShowTips(i18n("challenge_end_tip"))

				return

			arg_1_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.ANNIVERSARY_ISLAND_SEA), SFX_PANEL)

	function arg_1_0.btnFuncList.mountain(arg_7_0)
		onButton(arg_1_0, arg_7_0, function()
			local var_8_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF_2)

			if not var_8_0 or var_8_0.isEnd():
				pg.TipsMgr.GetInstance().ShowTips(i18n("challenge_end_tip"))

				return

			arg_1_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.ANNIVERSARY_ISLAND_BACKHILL_2023), SFX_PANEL)

def var_0_0.OnUpdateFlush(arg_9_0):
	local var_9_0 = {
		def shop:()
			return underscore.detect(getProxy(ActivityProxy).getActivitiesByType(ActivityConst.ACTIVITY_TYPE_SHOP), function(arg_11_0)
				return arg_11_0.getConfig("config_id") == 3),
		def activity:()
			return getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_ISLAND),
		def mountain:()
			return getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF_2)
	}

	for iter_9_0, iter_9_1 in pairs(var_9_0):
		local var_9_1 = iter_9_1()

		setButtonEnabled(arg_9_0.btnList.Find(iter_9_0), tobool(var_9_1 and not var_9_1.isEnd()))

return var_0_0
