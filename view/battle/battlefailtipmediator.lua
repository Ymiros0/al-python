local var_0_0 = class("BattleFailTipMediator", import("..base.ContextMediator"))

var_0_0.CHAPTER_RETREAT = "BattleFailTipMediator:CHAPTER_RETREAT"
var_0_0.GO_NAVALTACTICS = "BattleFailTipMediator:GO_NAVALTACTICS"
var_0_0.GO_HIGEST_CHAPTER = "BattleFailTipMediator:GO_HIGEST_CHAPTER"
var_0_0.GO_DOCKYARD_EQUIP = "BattleFailTipMediator:GO_DOCKYARD_EQUIP"
var_0_0.GO_DOCKYARD_SHIP = "BattleFailTipMediator:GO_DOCKYARD_SHIP"

function var_0_0.register(arg_1_0)
	arg_1_0:initData()
	arg_1_0:bindEvent()
end

function var_0_0.initData(arg_2_0)
	arg_2_0.mainShips = arg_2_0.contextData.mainShips
	arg_2_0.battleSystem = arg_2_0.contextData.battleSystem
end

function var_0_0.bindEvent(arg_3_0)
	arg_3_0:bind(var_0_0.CHAPTER_RETREAT, function(arg_4_0, arg_4_1)
		local var_4_0 = getProxy(ChapterProxy):getActiveChapter()
		local var_4_1

		if var_4_0 then
			var_4_1 = var_4_0:getShips()
		else
			var_4_1 = arg_3_0.mainShips
		end

		local var_4_2 = {}

		for iter_4_0, iter_4_1 in ipairs(var_4_1) do
			var_4_2[#var_4_2 + 1] = iter_4_1.id
		end

		arg_3_0.tempShipIDList = var_4_2

		arg_3_0:sendNotification(GAME.CHAPTER_OP, {
			type = ChapterConst.OpRetreat
		})
	end)
	arg_3_0:bind(var_0_0.GO_HIGEST_CHAPTER, function(arg_5_0)
		arg_3_0:removeContextBeforeGO()

		local var_5_0, var_5_1 = getProxy(ChapterProxy):getHigestClearChapterAndMap()

		arg_3_0:sendNotification(GAME.CHANGE_SCENE, SCENE.LEVEL, {
			targetChapter = var_5_0,
			targetMap = var_5_1
		})
	end)
	arg_3_0:bind(var_0_0.GO_DOCKYARD_EQUIP, function(arg_6_0)
		arg_3_0:removeContextBeforeGO()

		if not arg_3_0.tempShipIDList then
			local var_6_0 = {}

			for iter_6_0, iter_6_1 in ipairs(arg_3_0.mainShips) do
				var_6_0[#var_6_0 + 1] = iter_6_1.id
			end

			arg_3_0.tempShipIDList = var_6_0
		end

		arg_3_0:sendNotification(GAME.CHANGE_SCENE, SCENE.DOCKYARD, {
			priorEquipUpShipIDList = arg_3_0.tempShipIDList,
			priorMode = DockyardScene.PRIOR_MODE_EQUIP_UP,
			mode = DockyardScene.MODE_OVERVIEW,
			onClick = function(arg_7_0, arg_7_1)
				pg.m02:sendNotification(GAME.GO_SCENE, SCENE.SHIPINFO, {
					openEquipUpgrade = true,
					shipId = arg_7_0.id,
					shipVOs = arg_7_1,
					page = ShipViewConst.PAGE.EQUIPMENT
				})
			end
		})
	end)
	arg_3_0:bind(var_0_0.GO_DOCKYARD_SHIP, function(arg_8_0)
		arg_3_0:removeContextBeforeGO()

		if not arg_3_0.tempShipIDList then
			local var_8_0 = {}

			for iter_8_0, iter_8_1 in ipairs(arg_3_0.mainShips) do
				var_8_0[#var_8_0 + 1] = iter_8_1.id
			end

			arg_3_0.tempShipIDList = var_8_0
		end

		arg_3_0:sendNotification(GAME.CHANGE_SCENE, SCENE.DOCKYARD, {
			priorEquipUpShipIDList = arg_3_0.tempShipIDList,
			priorMode = DockyardScene.PRIOR_MODE_SHIP_UP,
			mode = DockyardScene.MODE_OVERVIEW,
			onClick = function(arg_9_0, arg_9_1)
				pg.m02:sendNotification(GAME.GO_SCENE, SCENE.SHIPINFO, {
					shipId = arg_9_0.id,
					shipVOs = arg_9_1,
					page = ShipViewConst.PAGE.INTENSIFY
				})
			end
		})
	end)
	arg_3_0:bind(var_0_0.GO_NAVALTACTICS, function(arg_10_0)
		arg_3_0:removeContextBeforeGO()
		arg_3_0:sendNotification(GAME.CHANGE_SCENE, SCENE.NAVALTACTICS)
	end)
end

function var_0_0.listNotificationInterests(arg_11_0)
	return {
		GAME.CHAPTER_OP_DONE
	}
end

function var_0_0.handleNotification(arg_12_0, arg_12_1)
	local var_12_0 = arg_12_1:getName()
	local var_12_1 = arg_12_1:getBody()

	if var_12_0 == GAME.CHAPTER_OP_DONE then
		if arg_12_0.viewComponent.lastClickBtn == BattleFailTipLayer.PowerUpBtn.ShipLevelUp then
			local var_12_2 = getProxy(ContextProxy):getContextByMediator(LevelMediator2)

			if var_12_2 then
				local var_12_3 = var_12_2:getContextByMediator(ChapterPreCombatMediator)

				if var_12_3 then
					var_12_2:removeChild(var_12_3)
				end

				local var_12_4 = var_12_2:getContextByMediator(BattleResultMediator)

				if var_12_4 then
					var_12_2:removeChild(var_12_4)
				end
			end

			local var_12_5, var_12_6 = getProxy(ChapterProxy):getHigestClearChapterAndMap()

			arg_12_0:sendNotification(GAME.GO_BACK, {
				targetChapter = var_12_5,
				targetMap = var_12_6
			})
		elseif arg_12_0.viewComponent.lastClickBtn == BattleFailTipLayer.PowerUpBtn.EquipLevelUp then
			local var_12_7 = getProxy(ContextProxy):getContextByMediator(LevelMediator2)

			if var_12_7 then
				local var_12_8 = var_12_7:getContextByMediator(ChapterPreCombatMediator)

				if var_12_8 then
					var_12_7:removeChild(var_12_8)
				end

				local var_12_9 = var_12_7:getContextByMediator(BattleResultMediator)

				if var_12_9 then
					var_12_7:removeChild(var_12_9)
				end
			end

			arg_12_0:sendNotification(GAME.CHANGE_SCENE, SCENE.DOCKYARD, {
				priorEquipUpShipIDList = arg_12_0.tempShipIDList,
				priorMode = DockyardScene.PRIOR_MODE_EQUIP_UP,
				mode = DockyardScene.MODE_OVERVIEW,
				onClick = function(arg_13_0, arg_13_1)
					pg.m02:sendNotification(GAME.GO_SCENE, SCENE.SHIPINFO, {
						openEquipUpgrade = true,
						shipId = arg_13_0.id,
						shipVOs = arg_13_1,
						page = ShipViewConst.PAGE.EQUIPMENT
					})
				end
			})
		elseif arg_12_0.viewComponent.lastClickBtn == BattleFailTipLayer.PowerUpBtn.SkillLevelUp then
			local var_12_10 = getProxy(ContextProxy):getContextByMediator(LevelMediator2)

			if var_12_10 then
				local var_12_11 = var_12_10:getContextByMediator(ChapterPreCombatMediator)

				if var_12_11 then
					var_12_10:removeChild(var_12_11)
				end

				local var_12_12 = var_12_10:getContextByMediator(BattleResultMediator)

				if var_12_12 then
					var_12_10:removeChild(var_12_12)
				end
			end

			arg_12_0:sendNotification(GAME.CHANGE_SCENE, SCENE.NAVALTACTICS)
		elseif arg_12_0.viewComponent.lastClickBtn == BattleFailTipLayer.PowerUpBtn.ShipBreakUp then
			local var_12_13 = getProxy(ContextProxy):getContextByMediator(LevelMediator2)

			if var_12_13 then
				local var_12_14 = var_12_13:getContextByMediator(ChapterPreCombatMediator)

				if var_12_14 then
					var_12_13:removeChild(var_12_14)
				end

				local var_12_15 = var_12_13:getContextByMediator(BattleResultMediator)

				if var_12_15 then
					var_12_13:removeChild(var_12_15)
				end
			end

			arg_12_0:sendNotification(GAME.CHANGE_SCENE, SCENE.DOCKYARD, {
				priorEquipUpShipIDList = arg_12_0.tempShipIDList,
				priorMode = DockyardScene.PRIOR_MODE_SHIP_UP,
				mode = DockyardScene.MODE_OVERVIEW,
				onClick = function(arg_14_0, arg_14_1)
					pg.m02:sendNotification(GAME.GO_SCENE, SCENE.SHIPINFO, {
						shipId = arg_14_0.id,
						shipVOs = arg_14_1,
						page = ShipViewConst.PAGE.INTENSIFY
					})
				end
			})
		end

		arg_12_0.tempShipIDList = nil
	end
end

function var_0_0.removeContextBeforeGO(arg_15_0)
	local var_15_0 = getProxy(ContextProxy)
	local var_15_1 = arg_15_0.battleSystem

	if var_15_1 == SYSTEM_SCENARIO then
		local var_15_2 = var_15_0:getContextByMediator(LevelMediator2)

		if var_15_2 then
			local var_15_3 = var_15_2:getContextByMediator(ChapterPreCombatMediator)

			if var_15_3 then
				var_15_2:removeChild(var_15_3)
			end

			local var_15_4 = var_15_2:getContextByMediator(BattleResultMediator)

			if var_15_4 then
				var_15_2:removeChild(var_15_4)
			end
		end
	elseif var_15_1 == SYSTEM_ROUTINE or var_15_1 == SYSTEM_SUB_ROUTINE then
		local var_15_5 = var_15_0:getContextByMediator(DailyLevelMediator)

		if var_15_5 then
			local var_15_6 = var_15_5:getContextByMediator(PreCombatMediator)

			if var_15_6 then
				var_15_5:removeChild(var_15_6)
			end

			local var_15_7 = var_15_5:getContextByMediator(BattleResultMediator)

			if var_15_7 then
				var_15_5:removeChild(var_15_7)
			end
		end
	elseif var_15_1 == SYSTEM_DUEL then
		local var_15_8 = var_15_0:getContextByMediator(MilitaryExerciseMediator)

		if var_15_8 then
			local var_15_9 = var_15_8:getContextByMediator(ExercisePreCombatMediator)

			if var_15_9 then
				var_15_8:removeChild(var_15_9)
			end

			local var_15_10 = var_15_8:getContextByMediator(BattleResultMediator)

			if var_15_10 then
				var_15_8:removeChild(var_15_10)
			end
		end
	elseif var_15_1 == SYSTEM_HP_SHARE_ACT_BOSS then
		local var_15_11, var_15_12 = var_15_0:getContextByMediator(ActivityBossPreCombatMediator)

		if var_15_11 then
			var_15_12:removeChild(var_15_11)
		end
	end
end

return var_0_0
