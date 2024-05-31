local var_0_0 = class("WorldMediator", import("..base.ContextMediator"))

var_0_0.OnMapOp = "WorldMediator.OnMapOp"
var_0_0.OnMapReq = "WorldMediator.OnMapReq"
var_0_0.OnOpenLayer = "WorldMediator.OnOpenLayer"
var_0_0.OnOpenScene = "WorldMediator.OnOpenScene"
var_0_0.OnChangeScene = "WorldMediator.OnChangeScene"
var_0_0.OnOpenMarkMap = "WorldMediator.OnOpenMarkMap"
var_0_0.OnTriggerTaskGo = "WorldMediator.OnTriggerTaskGo"
var_0_0.OnAutoSubmitTask = "WorldMediator.OnAutoSubmitTask"
var_0_0.OnNotificationOpenLayer = "WorldMediator.OnNotificationOpenLayer"
var_0_0.OnStart = "WorldMediator.OnStart"
var_0_0.OnStartPerform = "WorldMediator.OnStartPerform"
var_0_0.OnStartAutoSwitch = "WorldMediator.OnStartAutoSwitch"
var_0_0.OnMoveAndOpenLayer = "WorldMediator.OnMoveAndOpenLayer"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.OnMapOp, function(arg_2_0, arg_2_1)
		arg_1_0.sendNotification(GAME.WORLD_MAP_OP, arg_2_1))
	arg_1_0.bind(var_0_0.OnMapReq, function(arg_3_0, arg_3_1, arg_3_2)
		assert(arg_1_0.fetchCallback == None)

		arg_1_0.fetchCallback = arg_3_2

		arg_1_0.sendNotification(GAME.WORLD_MAP_REQ, {
			mapId = arg_3_1
		}))
	arg_1_0.bind(var_0_0.OnOpenLayer, function(arg_4_0, arg_4_1, arg_4_2)
		arg_1_0.addSubLayers(arg_4_1, False, arg_4_2))
	arg_1_0.bind(var_0_0.OnOpenScene, function(arg_5_0, arg_5_1, ...)
		local var_5_0 = {}

		if arg_1_0.viewComponent.GetInMap():
			table.insert(var_5_0, function(arg_6_0)
				arg_1_0.viewComponent.EaseOutMapUI(arg_6_0))
		else
			table.insert(var_5_0, function(arg_7_0)
				arg_1_0.viewComponent.EaseOutAtlasUI(arg_7_0))

		local var_5_1 = packEx(...)

		pg.UIMgr.GetInstance().LoadingOn()
		seriesAsync(var_5_0, function()
			pg.UIMgr.GetInstance().LoadingOff()
			arg_1_0.sendNotification(GAME.GO_SCENE, arg_5_1, unpack(var_5_1, 1, var_5_1.len))))
	arg_1_0.bind(var_0_0.OnChangeScene, function(arg_9_0, arg_9_1, ...)
		local var_9_0 = {}

		if arg_1_0.viewComponent.GetInMap():
			table.insert(var_9_0, function(arg_10_0)
				arg_1_0.viewComponent.EaseOutMapUI(arg_10_0))
		else
			table.insert(var_9_0, function(arg_11_0)
				arg_1_0.viewComponent.EaseOutAtlasUI(arg_11_0))

		local var_9_1 = packEx(...)

		pg.UIMgr.GetInstance().LoadingOn()
		seriesAsync(var_9_0, function()
			pg.UIMgr.GetInstance().LoadingOff()
			arg_1_0.sendNotification(GAME.CHANGE_SCENE, arg_9_1, unpack(var_9_1, 1, var_9_1.len))))
	arg_1_0.bind(var_0_0.OnStart, function(arg_13_0, arg_13_1, arg_13_2, arg_13_3)
		if arg_13_2.damageLevel > arg_13_3.GetLimitDamageLevel():
			nowWorld().TriggerAutoFight(False)
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				hideYes = True,
				content = i18n("world_low_morale")
			})
		else
			arg_1_0.sendNotification(GAME.BEGIN_STAGE, {
				system = SYSTEM_WORLD,
				stageId = arg_13_1
			}))
	arg_1_0.bind(var_0_0.OnStartPerform, function(arg_14_0, arg_14_1, arg_14_2)
		arg_1_0.sendNotification(GAME.BEGIN_STAGE, {
			system = SYSTEM_PERFORM,
			stageId = arg_14_1,
			exitCallback = arg_14_2
		}))
	arg_1_0.bind(var_0_0.OnAutoSubmitTask, function(arg_15_0, arg_15_1)
		arg_1_0.sendNotification(GAME.WORLD_AUTO_SUMBMIT_TASK, {
			taskId = arg_15_1.id
		}))
	arg_1_0.viewComponent.SetPlayer(getProxy(PlayerProxy).getRawData())

def var_0_0.listNotificationInterests(arg_16_0):
	local var_16_0 = {
		PlayerProxy.UPDATED,
		GAME.WORLD_MAP_OP_DONE,
		GAME.BEGIN_STAGE_DONE,
		GAME.WORLD_STAMINA_EXCHANGE_DONE,
		WorldInventoryMediator.OnMap,
		WorldCollectionMediator.ON_MAP,
		var_0_0.OnOpenMarkMap,
		GAME.WORLD_TRIGGER_TASK_DONE,
		GAME.WORLD_SUMBMIT_TASK_DONE,
		GAME.WORLD_AUTO_SUMBMIT_TASK_DONE,
		GAME.WORLD_ITEM_USE_DONE,
		GAME.WORLD_RETREAT_FLEET,
		var_0_0.OnTriggerTaskGo,
		GAME.WORLD_MAP_REQ_DONE,
		var_0_0.OnNotificationOpenLayer,
		GAME.WORLD_TRIGGER_AUTO_FIGHT,
		GAME.WORLD_TRIGGER_AUTO_SWITCH,
		var_0_0.OnStartAutoSwitch,
		var_0_0.OnMoveAndOpenLayer
	}
	local var_16_1 = WorldGuider.GetInstance().GetWorldGuiderNotifies()

	_.each(var_16_1, function(arg_17_0)
		var_16_0[#var_16_0 + 1] = arg_17_0)

	return var_16_0

def var_0_0.handleNotification(arg_18_0, arg_18_1):
	local var_18_0 = arg_18_1.getName()
	local var_18_1 = arg_18_1.getBody()

	WorldGuider.GetInstance().WorldGuiderNotifyHandler(var_18_0, var_18_1, arg_18_0.viewComponent)

	local var_18_2 = nowWorld()

	switch(var_18_0, {
		[GAME.WORLD_MAP_OP_DONE] = function()
			local var_19_0 = var_18_1.mapOp
			local var_19_1 = arg_18_0.viewComponent.GetCommand(var_19_0.depth)

			if var_18_1.result != 0:
				var_19_1.OpDone()

				if var_18_1.result == 130:
					var_18_2.staminaMgr.Show()

				return

			local var_19_2 = {}
			local var_19_3

			arg_18_0.viewComponent.RegistMapOp(var_19_0)

			if #var_19_0.drops > 0:
				if var_19_0.op == WorldConst.OpReqCatSalvage:
					local var_19_4 = var_18_2.GetFleet(var_19_0.id).GetSalvageScoreRarity()

					if var_18_2.isAutoFight:
						var_18_2.AddAutoInfo("salvage", {
							drops = var_19_0.drops,
							rarity = var_19_4
						})
					else
						table.insert(var_19_2, function(arg_20_0)
							arg_18_0.viewComponent.DisplayAwards(var_19_0.drops, {
								title = "commander",
								titleExtra = tostring(var_19_4)
							}, arg_20_0))
				elif var_18_2.isAutoFight:
					var_18_2.AddAutoInfo("drops", var_19_0.drops)
				else
					table.insert(var_19_2, function(arg_21_0)
						arg_18_0.viewComponent.DisplayAwards(var_19_0.drops, {}, arg_21_0))

			if var_19_0.routine:
				function var_19_3()
					var_19_0.routine(var_19_0)
			else
				local var_19_5 = var_19_0.op

				var_18_0 = WorldConst.ReqName[var_19_5]

				assert(var_18_0, "invalid operation. " .. var_19_5)

				if var_19_5 == WorldConst.OpReqTask:
					-- block empty
				elif var_19_5 == WorldConst.OpReqPressingMap or var_19_5 == WorldConst.OpReqCatSalvage:
					local var_19_6 = var_19_2

					var_19_2 = {}

					function var_19_3()
						var_19_1.OpDone(var_18_0 .. "Done", var_19_0, var_19_6)
				else
					function var_19_3()
						var_19_1.OpDone(var_18_0 .. "Done", var_19_0)

			seriesAsync(var_19_2, var_19_3),
		[PlayerProxy.UPDATED] = function()
			arg_18_0.viewComponent.SetPlayer(getProxy(PlayerProxy).getRawData()),
		[GAME.BEGIN_STAGE_DONE] = function()
			arg_18_0.sendNotification(GAME.GO_SCENE, SCENE.COMBATLOAD, var_18_1),
		[GAME.WORLD_STAMINA_EXCHANGE_DONE] = function()
			if not arg_18_0.viewComponent.GetInMap():
				local var_27_0 = arg_18_0.viewComponent.svFloatPanel

				if var_27_0.isShowing():
					var_27_0.UpdateCost(),
		[WorldInventoryMediator.OnMap] = function()
			arg_18_0.viewComponent.Op("OpFocusTargetEntrance", var_18_1),
		[WorldCollectionMediator.ON_MAP] = function()
			arg_18_0.viewComponent.Op("OpFocusTargetEntrance", var_18_1),
		[var_0_0.OnOpenMarkMap] = function()
			arg_18_0.viewComponent.Op("OpShowMarkOverview", var_18_1),
		[GAME.WORLD_TRIGGER_TASK_DONE] = function()
			pg.WorldToastMgr.GetInstance().ShowToast(var_18_1.task, False),
		[GAME.WORLD_SUMBMIT_TASK_DONE] = function()
			local var_32_0 = {}
			local var_32_1 = var_18_1.task

			if #var_32_1.config.task_ed > 0:
				table.insert(var_32_0, function(arg_33_0)
					pg.NewStoryMgr.GetInstance().Play(var_32_1.config.task_ed, arg_33_0, True))

			if var_18_1.drops and #var_18_1.drops > 0:
				if var_18_2.isAutoFight:
					var_18_2.AddAutoInfo("drops", var_18_1.drops)
				else
					table.insert(var_32_0, function(arg_34_0)
						arg_18_0.viewComponent.DisplayAwards(var_18_1.drops, {}, arg_34_0))

			for iter_32_0, iter_32_1 in ipairs(var_18_1.expfleets):
				table.insert(var_32_0, function(arg_35_0)
					local var_35_0 = iter_32_1.oldships
					local var_35_1 = iter_32_1.newships

					arg_18_0.viewComponent.emit(BaseUI.ON_SHIP_EXP, {
						title = "without word",
						oldShips = var_35_0,
						newShips = var_35_1
					}, arg_35_0))

			seriesAsync(var_32_0, function()
				pg.WorldToastMgr.GetInstance().ShowToast(var_32_1, True)),
		[GAME.WORLD_AUTO_SUMBMIT_TASK_DONE] = function()
			local var_37_0 = {}
			local var_37_1 = var_18_1.task

			if #var_37_1.config.task_ed > 0:
				table.insert(var_37_0, function(arg_38_0)
					pg.NewStoryMgr.GetInstance().Play(var_37_1.config.task_ed, arg_38_0, True))

			if var_18_1.drops and #var_18_1.drops > 0:
				if var_18_2.isAutoFight:
					var_18_2.AddAutoInfo("drops", var_18_1.drops)
				else
					table.insert(var_37_0, function(arg_39_0)
						arg_18_0.viewComponent.DisplayAwards(var_18_1.drops, {}, arg_39_0))

			for iter_37_0, iter_37_1 in ipairs(var_18_1.expfleets):
				table.insert(var_37_0, function(arg_40_0)
					local var_40_0 = iter_37_1.oldships
					local var_40_1 = iter_37_1.newships

					arg_18_0.viewComponent.emit(BaseUI.ON_SHIP_EXP, {
						title = "without word",
						oldShips = var_40_0,
						newShips = var_40_1
					}, arg_40_0))

			seriesAsync(var_37_0, function()
				pg.WorldToastMgr.GetInstance().ShowToast(var_37_1, True)
				arg_18_0.viewComponent.GetCommand().OpDone("OpAutoSubmitTaskDone", var_37_1)),
		[GAME.WORLD_ITEM_USE_DONE] = function()
			local var_42_0 = var_18_1.item
			local var_42_1 = var_18_1.drops
			local var_42_2 = {}

			switch(var_42_0.getWorldItemType(), {
				[WorldItem.UsageWorldClean] = function()
					table.insert(var_42_2, function(arg_44_0)
						local var_44_0 = pg.gameset.world_story_recycle_item.description[1]

						pg.NewStoryMgr.GetInstance().Play(var_44_0, arg_44_0, True))
					table.insert(var_42_2, function(arg_45_0)
						arg_18_0.viewComponent.GetAllPessingAward(arg_45_0)),
				[WorldItem.UsageWorldFlag] = function()
					table.insert(var_42_2, function(arg_47_0)
						local var_47_0 = pg.gameset.world_story_treasure_item.description[1]

						pg.NewStoryMgr.GetInstance().Play(var_47_0, arg_47_0, True)),
				[WorldItem.UsageWorldBuff] = function()
					local var_48_0, var_48_1 = var_42_0.getItemWorldBuff()
					local var_48_2 = var_48_1 * var_42_0.count

					table.insert(var_42_2, function(arg_49_0)
						local var_49_0 = {
							id = var_48_0,
							floor = var_48_2,
							before = var_18_2.GetGlobalBuff(var_48_0).GetFloor()
						}

						arg_18_0.viewComponent.ShowSubView("GlobalBuff", {
							var_49_0,
							arg_49_0
						}))
					table.insert(var_42_2, function(arg_50_0)
						var_18_2.AddGlobalBuff(var_48_0, var_48_2)
						arg_50_0()),
				[WorldItem.UsageWorldFlag] = function()
					switch(var_42_0.getItemFlagKey(), {
						function()
							table.insert(var_42_2, function(arg_53_0)
								local var_53_0 = var_18_2.GetActiveMap()

								if not var_53_0.visionFlag and var_18_2.IsMapVisioned(var_53_0.id):
									var_53_0.UpdateVisionFlag(True)

								arg_53_0())
					})
			})

			if #var_42_1 > 0:
				if var_18_2.isAutoFight:
					var_18_2.AddAutoInfo("drops", var_42_1)
				else
					table.insert(var_42_2, function(arg_54_0)
						arg_18_0.viewComponent.DisplayAwards(var_42_1, {}, arg_54_0))

			seriesAsync(var_42_2, function()
				return),
		[GAME.WORLD_RETREAT_FLEET] = function()
			local var_56_0 = var_18_2.GetFleet()

			arg_18_0.viewComponent.Op("OpReqRetreat", var_56_0),
		[var_0_0.OnTriggerTaskGo] = function()
			arg_18_0.viewComponent.Op("OpTaskGoto", var_18_1.taskId),
		[GAME.WORLD_MAP_REQ_DONE] = function()
			assert(arg_18_0.fetchCallback)
			existCall(arg_18_0.fetchCallback)

			arg_18_0.fetchCallback = None,
		[var_0_0.OnNotificationOpenLayer] = function()
			arg_18_0.addSubLayers(var_18_1.context),
		[GAME.WORLD_TRIGGER_AUTO_FIGHT] = function()
			arg_18_0.viewComponent.UpdateAutoFightDisplay(),
		[GAME.WORLD_TRIGGER_AUTO_SWITCH] = function()
			arg_18_0.viewComponent.UpdateAutoSwitchDisplay(),
		[var_0_0.OnStartAutoSwitch] = function()
			arg_18_0.viewComponent.StartAutoSwitch(),
		[var_0_0.OnMoveAndOpenLayer] = function()
			arg_18_0.viewComponent.MoveAndOpenLayer(var_18_1)
	})

return var_0_0
