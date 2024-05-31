local var_0_0 = class("BattleMediator", import("..base.ContextMediator"))

var_0_0.ON_BATTLE_RESULT = "BattleMediator:ON_BATTLE_RESULT"
var_0_0.ON_PAUSE = "BattleMediator:ON_PAUSE"
var_0_0.ENTER = "BattleMediator:ENTER"
var_0_0.ON_BACK_PRE_SCENE = "BattleMediator:ON_BACK_PRE_SCENE"
var_0_0.ON_LEAVE = "BattleMediator:ON_LEAVE"
var_0_0.ON_QUIT_BATTLE_MANUALLY = "BattleMediator:ON_QUIT_BATTLE_MANUALLY"
var_0_0.HIDE_ALL_BUTTONS = "BattleMediator:HIDE_ALL_BUTTONS"
var_0_0.ON_CHAT = "BattleMediator:ON_CHAT"
var_0_0.CLOSE_CHAT = "BattleMediator:CLOSE_CHAT"
var_0_0.ON_AUTO = "BattleMediator:ON_AUTO"
var_0_0.ON_PUZZLE_RELIC = "BattleMediator.ON_PUZZLE_RELIC"
var_0_0.ON_PUZZLE_CARD = "BattleMediator.ON_PUZZLE_CARD"

function var_0_0.register(arg_1_0)
	pg.BrightnessMgr.GetInstance():SetScreenNeverSleep(true)
	arg_1_0:GenBattleData()

	arg_1_0.contextData.battleData = arg_1_0._battleData

	local var_1_0 = ys.Battle.BattleState.GetInstance()
	local var_1_1 = arg_1_0.contextData.system

	arg_1_0:bind(var_0_0.ON_BATTLE_RESULT, function(arg_2_0, arg_2_1)
		arg_1_0:sendNotification(GAME.FINISH_STAGE, {
			token = arg_1_0.contextData.token,
			mainFleetId = arg_1_0.contextData.mainFleetId,
			stageId = arg_1_0.contextData.stageId,
			rivalId = arg_1_0.contextData.rivalId,
			memory = arg_1_0.contextData.memory,
			bossId = arg_1_0.contextData.bossId,
			exitCallback = arg_1_0.contextData.exitCallback,
			system = var_1_1,
			statistics = arg_2_1,
			actId = arg_1_0.contextData.actId,
			mode = arg_1_0.contextData.mode,
			puzzleCombatID = arg_1_0.contextData.puzzleCombatID
		})
	end)
	arg_1_0:bind(var_0_0.ON_AUTO, function(arg_3_0, arg_3_1)
		arg_1_0:onAutoBtn(arg_3_1)
	end)
	arg_1_0:bind(var_0_0.ON_PAUSE, function(arg_4_0)
		arg_1_0:onPauseBtn()
	end)
	arg_1_0:bind(var_0_0.ON_LEAVE, function(arg_5_0)
		arg_1_0:warnFunc()
	end)
	arg_1_0:bind(var_0_0.ON_CHAT, function(arg_6_0, arg_6_1)
		arg_1_0:addSubLayers(Context.New({
			mediator = NotificationMediator,
			viewComponent = NotificationLayer,
			data = {
				form = NotificationLayer.FORM_BATTLE,
				chatViewParent = arg_6_1
			}
		}))
	end)
	arg_1_0:bind(var_0_0.ENTER, function(arg_7_0)
		var_1_0:EnterBattle(arg_1_0._battleData, arg_1_0.contextData.prePause)
	end)
	arg_1_0:bind(var_0_0.ON_BACK_PRE_SCENE, function()
		local var_8_0 = getProxy(ContextProxy)
		local var_8_1 = var_8_0:getContextByMediator(DailyLevelMediator)
		local var_8_2 = var_8_0:getContextByMediator(LevelMediator2)
		local var_8_3 = var_8_0:getContextByMediator(ChallengeMainMediator)
		local var_8_4 = var_8_0:getContextByMediator(ActivityBossMediatorTemplate)
		local var_8_5 = var_8_0:getContextByMediator(WorldMediator)
		local var_8_6 = var_8_0:getContextByMediator(WorldBossMediator)

		if var_8_6 and arg_1_0.contextData.bossId then
			arg_1_0:sendNotification(GAME.WORLD_BOSS_BATTLE_QUIT, {
				id = arg_1_0.contextData.bossId
			})

			local var_8_7 = var_8_6:getContextByMediator(WorldBossFormationMediator)

			if var_8_7 then
				var_8_6:removeChild(var_8_7)
			end
		elseif var_8_5 then
			local var_8_8 = var_8_5:getContextByMediator(WorldPreCombatMediator) or var_8_5:getContextByMediator(WorldBossInformationMediator)

			if var_8_8 then
				var_8_5:removeChild(var_8_8)
			end
		elseif var_8_1 then
			local var_8_9 = var_8_1:getContextByMediator(PreCombatMediator)

			var_8_1:removeChild(var_8_9)
		elseif var_8_3 then
			arg_1_0:sendNotification(GAME.CHALLENGE2_RESET, {
				mode = arg_1_0.contextData.mode
			})

			local var_8_10 = var_8_3:getContextByMediator(ChallengePreCombatMediator)

			var_8_3:removeChild(var_8_10)
		elseif var_8_2 then
			if var_1_1 == SYSTEM_DUEL then
				-- block empty
			elseif var_1_1 == SYSTEM_SCENARIO then
				local var_8_11 = var_8_2:getContextByMediator(ChapterPreCombatMediator)

				if var_8_11 then
					var_8_2:removeChild(var_8_11)
				end
			elseif var_1_1 ~= SYSTEM_PERFORM and var_1_1 ~= SYSTEM_SIMULATION then
				local var_8_12 = var_8_2:getContextByMediator(PreCombatMediator)

				if var_8_12 then
					var_8_2:removeChild(var_8_12)
				end
			end
		elseif var_8_4 then
			local var_8_13 = var_8_4:getContextByMediator(PreCombatMediator)

			if var_8_13 then
				var_8_4:removeChild(var_8_13)
			end
		end

		arg_1_0:sendNotification(GAME.GO_BACK)
	end)
	arg_1_0:bind(var_0_0.ON_QUIT_BATTLE_MANUALLY, function(arg_9_0)
		if var_1_1 == SYSTEM_SCENARIO then
			getProxy(ChapterProxy):StopAutoFight(ChapterConst.AUTOFIGHT_STOP_REASON.MANUAL)
		elseif var_1_1 == SYSTEM_WORLD then
			nowWorld():TriggerAutoFight(false)
		elseif var_1_1 == SYSTEM_ACT_BOSS then
			if getProxy(ContextProxy):getCurrentContext():getContextByMediator(ContinuousOperationMediator) then
				getProxy(ContextProxy):GetPrevContext(1):addChild(Context.New({
					mediator = ActivityBossTotalRewardPanelMediator,
					viewComponent = ActivityBossTotalRewardPanel,
					data = {
						isAutoFight = false,
						isLayer = true,
						rewards = getProxy(ChapterProxy):PopActBossRewards(),
						continuousBattleTimes = arg_1_0.contextData.continuousBattleTimes,
						totalBattleTimes = arg_1_0.contextData.totalBattleTimes
					}
				}))
			end
		elseif var_1_1 == SYSTEM_BOSS_RUSH then
			if getProxy(ContextProxy):getCurrentContext():getContextByMediator(ContinuousOperationMediator) then
				local var_9_0 = getProxy(ActivityProxy):PopBossRushAwards()

				getProxy(ContextProxy):GetPrevContext(1):addChild(Context.New({
					mediator = BossRushTotalRewardPanelMediator,
					viewComponent = BossRushTotalRewardPanel,
					data = {
						isLayer = true,
						rewards = var_9_0
					}
				}))
			end
		elseif var_1_1 == SYSTEM_BOSS_SINGLE and getProxy(ContextProxy):getCurrentContext():getContextByMediator(BossSingleContinuousOperationMediator) then
			getProxy(ContextProxy):GetPrevContext(1):addChild(Context.New({
				mediator = BossSingleTotalRewardPanelMediator,
				viewComponent = BossSingleTotalRewardPanel,
				data = {
					isAutoFight = false,
					isLayer = true,
					rewards = getProxy(ChapterProxy):PopBossSingleRewards(),
					continuousBattleTimes = arg_1_0.contextData.continuousBattleTimes,
					totalBattleTimes = arg_1_0.contextData.totalBattleTimes
				}
			}))
		end
	end)
	arg_1_0:bind(var_0_0.ON_PUZZLE_RELIC, function(arg_10_0, arg_10_1)
		arg_1_0:addSubLayers(Context.New({
			mediator = CardPuzzleRelicDeckMediator,
			viewComponent = CardPuzzleRelicDeckLayerCombat,
			data = arg_10_1
		}))
		var_1_0:Pause()
	end)
	arg_1_0:bind(var_0_0.ON_PUZZLE_CARD, function(arg_11_0, arg_11_1)
		arg_1_0:addSubLayers(Context.New({
			mediator = CardPuzzleCardDeckMediator,
			viewComponent = CardPuzzleCardDeckLayerCombat,
			data = arg_11_1
		}))
		var_1_0:Pause()
	end)

	if arg_1_0.contextData.continuousBattleTimes and arg_1_0.contextData.continuousBattleTimes > 0 then
		if var_1_1 == SYSTEM_BOSS_SINGLE then
			if not getProxy(ContextProxy):getCurrentContext():getContextByMediator(BossSingleContinuousOperationMediator) then
				local var_1_2 = CreateShell(arg_1_0.contextData)

				var_1_2.LayerWeightMgr_weight = LayerWeightConst.BASE_LAYER

				arg_1_0:addSubLayers(Context.New({
					mediator = BossSingleContinuousOperationMediator,
					viewComponent = BossSingleContinuousOperationPanel,
					data = var_1_2
				}))
			end
		elseif not getProxy(ContextProxy):getCurrentContext():getContextByMediator(ContinuousOperationMediator) then
			local var_1_3 = CreateShell(arg_1_0.contextData)

			var_1_3.LayerWeightMgr_weight = LayerWeightConst.BASE_LAYER

			arg_1_0:addSubLayers(Context.New({
				mediator = ContinuousOperationMediator,
				viewComponent = ContinuousOperationPanel,
				data = var_1_3
			}))
		end

		arg_1_0.contextData.battleData.hideAllButtons = true
	end

	local var_1_4 = getProxy(PlayerProxy)

	if var_1_4 then
		arg_1_0.player = var_1_4:getData()

		var_1_4:setFlag("battle", true)
	end
end

function var_0_0.onAutoBtn(arg_12_0, arg_12_1)
	local var_12_0 = arg_12_1.isOn
	local var_12_1 = arg_12_1.toggle
	local var_12_2 = arg_12_1.system

	arg_12_0:sendNotification(GAME.AUTO_BOT, {
		isActiveBot = var_12_0,
		toggle = var_12_1,
		system = var_12_2
	})
end

function var_0_0.onPauseBtn(arg_13_0)
	local var_13_0 = ys.Battle.BattleState.GetInstance()

	if arg_13_0.contextData.system == SYSTEM_PROLOGUE or arg_13_0.contextData.system == SYSTEM_PERFORM then
		local var_13_1 = {}

		if EPILOGUE_SKIPPABLE then
			local var_13_2 = {
				text = "关爱胡德",
				btnType = pg.MsgboxMgr.BUTTON_RED,
				onCallback = function()
					var_13_0:Deactive()
					arg_13_0:sendNotification(GAME.CHANGE_SCENE, SCENE.CREATE_PLAYER)
				end
			}

			table.insert(var_13_1, 1, var_13_2)
		end

		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = i18n("help_battle_rule"),
			onClose = function()
				ys.Battle.BattleState.GetInstance():Resume()
			end,
			onNo = function()
				ys.Battle.BattleState.GetInstance():Resume()
			end,
			custom = var_13_1
		})
		var_13_0:Pause()
	elseif arg_13_0.contextData.system == SYSTEM_DODGEM then
		local var_13_3 = {
			text = "text_cancel_fight",
			btnType = pg.MsgboxMgr.BUTTON_RED,
			onCallback = function()
				arg_13_0:warnFunc(function()
					ys.Battle.BattleState.GetInstance():Resume()
				end)
			end
		}

		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = i18n("help_battle_warspite"),
			onClose = function()
				ys.Battle.BattleState.GetInstance():Resume()
			end,
			onNo = function()
				ys.Battle.BattleState.GetInstance():Resume()
			end,
			custom = {
				var_13_3
			}
		})
		var_13_0:Pause()
	elseif arg_13_0.contextData.system == SYSTEM_SIMULATION then
		local var_13_4 = {
			text = "text_cancel_fight",
			btnType = pg.MsgboxMgr.BUTTON_RED,
			onCallback = function()
				arg_13_0:warnFunc(function()
					ys.Battle.BattleState.GetInstance():Resume()
				end)
			end
		}

		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = i18n("help_battle_rule"),
			onClose = function()
				ys.Battle.BattleState.GetInstance():Resume()
			end,
			onNo = function()
				ys.Battle.BattleState.GetInstance():Resume()
			end,
			custom = {
				var_13_4
			}
		})
		var_13_0:Pause()
	elseif arg_13_0.contextData.system == SYSTEM_SUBMARINE_RUN or arg_13_0.contextData.system == SYSTEM_SUB_ROUTINE or arg_13_0.contextData.system == SYSTEM_REWARD_PERFORM or arg_13_0.contextData.system == SYSTEM_AIRFIGHT then
		var_13_0:Pause()
		arg_13_0:warnFunc(function()
			ys.Battle.BattleState.GetInstance():Resume()
		end)
	elseif arg_13_0.contextData.system == SYSTEM_CARDPUZZLE then
		arg_13_0:addSubLayers(Context.New({
			mediator = CardPuzzleCombatPauseMediator,
			viewComponent = CardPuzzleCombatPauseLayer
		}))
		var_13_0:Pause()
	else
		arg_13_0.viewComponent:updatePauseWindow()
		var_13_0:Pause()
	end
end

function var_0_0.warnFunc(arg_26_0, arg_26_1)
	local var_26_0 = ys.Battle.BattleState.GetInstance()
	local var_26_1 = arg_26_0.contextData.system
	local var_26_2
	local var_26_3

	local function var_26_4()
		var_26_0:Stop()
	end

	local var_26_5 = arg_26_0.contextData.warnMsg

	if var_26_5 and #var_26_5 > 0 then
		var_26_3 = i18n(var_26_5)
	elseif var_26_1 == SYSTEM_CHALLENGE then
		var_26_3 = i18n("battle_battleMediator_clear_warning")
	elseif var_26_1 == SYSTEM_SIMULATION then
		var_26_3 = i18n("tech_simulate_quit")
	else
		var_26_3 = i18n("battle_battleMediator_quest_exist")
	end

	pg.MsgboxMgr.GetInstance():ShowMsgBox({
		modal = true,
		hideNo = true,
		hideYes = true,
		content = var_26_3,
		onClose = arg_26_1,
		custom = {
			{
				text = "text_cancel",
				onCallback = arg_26_1,
				sound = SFX_CANCEL
			},
			{
				text = "text_exit",
				btnType = pg.MsgboxMgr.BUTTON_RED,
				onCallback = var_26_4,
				sound = SFX_CONFIRM
			}
		}
	})
end

function var_0_0.guideDispatch(arg_28_0)
	return
end

local function var_0_1(arg_29_0, arg_29_1, arg_29_2, arg_29_3)
	local var_29_0 = {}

	for iter_29_0, iter_29_1 in ipairs(arg_29_1:getActiveEquipments()) do
		if iter_29_1 then
			var_29_0[#var_29_0 + 1] = {
				id = iter_29_1.configId,
				skin = iter_29_1.skinId,
				equipmentInfo = iter_29_1
			}
		else
			var_29_0[#var_29_0 + 1] = {
				skin = 0,
				id = iter_29_1,
				equipmentInfo = iter_29_1
			}
		end
	end

	local var_29_1 = {}

	local function var_29_2(arg_30_0)
		local var_30_0 = {
			level = arg_30_0.level
		}
		local var_30_1 = arg_30_0.id
		local var_30_2 = arg_29_1:RemapSkillId(var_30_1)

		var_30_0.id = ys.Battle.BattleDataFunction.SkillTranform(arg_29_0, var_30_2)

		return var_30_0
	end

	local var_29_3 = ys.Battle.BattleDataFunction.GenerateHiddenBuff(arg_29_1.configId)

	for iter_29_2, iter_29_3 in pairs(var_29_3) do
		local var_29_4 = var_29_2(iter_29_3)

		var_29_1[var_29_4.id] = var_29_4
	end

	for iter_29_4, iter_29_5 in pairs(arg_29_1.skills) do
		if iter_29_5 and iter_29_5.id == 14900 and not arg_29_1.transforms[16412] then
			-- block empty
		else
			local var_29_5 = var_29_2(iter_29_5)

			var_29_1[var_29_5.id] = var_29_5
		end
	end

	local var_29_6 = ys.Battle.BattleDataFunction.GetEquipSkill(var_29_0)

	for iter_29_6, iter_29_7 in ipairs(var_29_6) do
		local var_29_7 = {}

		var_29_7.level = 1
		var_29_7.id = ys.Battle.BattleDataFunction.SkillTranform(arg_29_0, iter_29_7)
		var_29_1[var_29_7.id] = var_29_7
	end

	local var_29_8

	;(function()
		var_29_8 = arg_29_1:GetSpWeapon()

		if not var_29_8 then
			return
		end

		local var_31_0 = var_29_8:GetEffect()

		if var_31_0 == 0 then
			return
		end

		local var_31_1 = {}

		var_31_1.level = 1
		var_31_1.id = ys.Battle.BattleDataFunction.SkillTranform(arg_29_0, var_31_0)
		var_29_1[var_31_1.id] = var_31_1
	end)()

	for iter_29_8, iter_29_9 in pairs(arg_29_1:getTriggerSkills()) do
		local var_29_9 = {
			level = iter_29_9.level,
			id = ys.Battle.BattleDataFunction.SkillTranform(arg_29_0, iter_29_9.id)
		}

		var_29_1[var_29_9.id] = var_29_9
	end

	local var_29_10 = arg_29_0 == SYSTEM_WORLD
	local var_29_11 = false

	if var_29_10 then
		local var_29_12 = WorldConst.FetchWorldShip(arg_29_1.id)

		if var_29_12 then
			var_29_11 = var_29_12:IsBroken()
		end
	end

	if var_29_11 then
		for iter_29_10, iter_29_11 in pairs(var_29_1) do
			local var_29_13 = pg.skill_data_template[iter_29_10].world_death_mark[1]

			if var_29_13 == ys.Battle.BattleConst.DEATH_MARK_SKILL.DEACTIVE then
				var_29_1[iter_29_10] = nil
			elseif var_29_13 == ys.Battle.BattleConst.DEATH_MARK_SKILL.IGNORE then
				-- block empty
			end
		end
	end

	return {
		id = arg_29_1.id,
		tmpID = arg_29_1.configId,
		skinId = arg_29_1.skinId,
		level = arg_29_1.level,
		equipment = var_29_0,
		properties = arg_29_1:getProperties(arg_29_2, arg_29_3, var_29_10),
		baseProperties = arg_29_1:getShipProperties(),
		proficiency = arg_29_1:getEquipProficiencyList(),
		rarity = arg_29_1:getRarity(),
		intimacy = arg_29_1:getCVIntimacy(),
		shipGS = arg_29_1:getShipCombatPower(),
		skills = var_29_1,
		baseList = arg_29_1:getBaseList(),
		preloasList = arg_29_1:getPreLoadCount(),
		name = arg_29_1:getName(),
		deathMark = var_29_11,
		spWeapon = var_29_8
	}
end

local function var_0_2(arg_32_0, arg_32_1)
	local var_32_0 = arg_32_0:getProperties(arg_32_1)
	local var_32_1 = arg_32_0:getConfig("id")

	return {
		deathMark = false,
		shipGS = 100,
		rarity = 1,
		intimacy = 100,
		id = var_32_1,
		tmpID = var_32_1,
		skinId = arg_32_0:getConfig("skin_id"),
		level = arg_32_0:getConfig("level"),
		equipment = arg_32_0:getConfig("default_equip"),
		properties = var_32_0,
		baseProperties = var_32_0,
		proficiency = {
			1,
			1,
			1
		},
		skills = {},
		baseList = {
			1,
			1,
			1
		},
		preloasList = {
			0,
			0,
			0
		},
		name = var_32_1,
		fleetIndex = arg_32_0:getConfig("location")
	}
end

function var_0_0.GenBattleData(arg_33_0)
	local var_33_0 = {}
	local var_33_1 = arg_33_0.contextData.system

	arg_33_0._battleData = var_33_0
	var_33_0.battleType = arg_33_0.contextData.system
	var_33_0.StageTmpId = arg_33_0.contextData.stageId
	var_33_0.CMDArgs = arg_33_0.contextData.cmdArgs
	var_33_0.MainUnitList = {}
	var_33_0.VanguardUnitList = {}
	var_33_0.SubUnitList = {}
	var_33_0.AidUnitList = {}
	var_33_0.SupportUnitList = {}
	var_33_0.SubFlag = -1
	var_33_0.ActID = arg_33_0.contextData.actId
	var_33_0.bossLevel = arg_33_0.contextData.bossLevel
	var_33_0.bossConfigId = arg_33_0.contextData.bossConfigId

	if pg.battle_cost_template[var_33_1].global_buff_effected > 0 then
		local var_33_2 = BuffHelper.GetBattleBuffs(var_33_1)

		var_33_0.GlobalBuffIDs = _.map(var_33_2, function(arg_34_0)
			return arg_34_0:getConfig("benefit_effect")
		end) or {}
	end

	local var_33_3 = pg.battle_cost_template[var_33_1]
	local var_33_4 = getProxy(BayProxy)
	local var_33_5 = {}

	if var_33_1 == SYSTEM_SCENARIO then
		local var_33_6 = getProxy(ChapterProxy)
		local var_33_7 = var_33_6:getActiveChapter()

		var_33_0.RepressInfo = var_33_7:getRepressInfo()

		arg_33_0.viewComponent:setChapter(var_33_7)

		local var_33_8 = var_33_7.fleet

		var_33_0.KizunaJamming = var_33_7.extraFlagList
		var_33_0.DefeatCount = var_33_8:getDefeatCount()
		var_33_0.ChapterBuffIDs, var_33_0.CommanderList = var_33_7:getFleetBattleBuffs(var_33_8)
		var_33_0.StageWaveFlags = var_33_7:GetStageFlags()
		var_33_0.ChapterWeatherIDS = var_33_7:GetWeather(var_33_8.line.row, var_33_8.line.column)
		var_33_0.MapAuraSkills = var_33_6.GetChapterAuraBuffs(var_33_7)
		var_33_0.MapAidSkills = {}

		local var_33_9 = var_33_6.GetChapterAidBuffs(var_33_7)

		for iter_33_0, iter_33_1 in pairs(var_33_9) do
			local var_33_10 = var_33_7:getFleetByShipVO(iter_33_0)
			local var_33_11 = _.values(var_33_10:getCommanders())
			local var_33_12 = var_0_1(var_33_1, iter_33_0, var_33_11)

			table.insert(var_33_0.AidUnitList, var_33_12)

			for iter_33_2, iter_33_3 in ipairs(iter_33_1) do
				table.insert(var_33_0.MapAidSkills, iter_33_3)
			end
		end

		local var_33_13 = var_33_8:getShipsByTeam(TeamType.Main, false)
		local var_33_14 = var_33_8:getShipsByTeam(TeamType.Vanguard, false)
		local var_33_15 = {}
		local var_33_16 = _.values(var_33_8:getCommanders())
		local var_33_17 = {}
		local var_33_18, var_33_19 = var_33_6.getSubAidFlag(var_33_7, arg_33_0.contextData.stageId)

		if var_33_18 == true or var_33_18 > 0 then
			var_33_0.SubFlag = 1
			var_33_0.TotalSubAmmo = 1
			var_33_15 = var_33_19:getShipsByTeam(TeamType.Submarine, false)
			var_33_17 = _.values(var_33_19:getCommanders())

			local var_33_20, var_33_21 = var_33_7:getFleetBattleBuffs(var_33_19)

			var_33_0.SubCommanderList = var_33_21
		else
			var_33_0.SubFlag = var_33_18

			if var_33_18 ~= ys.Battle.BattleConst.SubAidFlag.AID_EMPTY then
				var_33_0.TotalSubAmmo = 0
			end
		end

		arg_33_0.mainShips = {}

		local function var_33_22(arg_35_0, arg_35_1, arg_35_2)
			local var_35_0 = arg_35_0.id
			local var_35_1 = arg_35_0.hpRant * 0.0001

			if table.contains(var_33_5, var_35_0) then
				BattleVertify.cloneShipVertiry = true
			end

			var_33_5[#var_33_5 + 1] = var_35_0

			local var_35_2 = var_0_1(var_33_1, arg_35_0, arg_35_1)

			var_35_2.initHPRate = var_35_1

			table.insert(arg_33_0.mainShips, arg_35_0)
			table.insert(arg_35_2, var_35_2)
		end

		for iter_33_4, iter_33_5 in ipairs(var_33_13) do
			var_33_22(iter_33_5, var_33_16, var_33_0.MainUnitList)
		end

		for iter_33_6, iter_33_7 in ipairs(var_33_14) do
			var_33_22(iter_33_7, var_33_16, var_33_0.VanguardUnitList)
		end

		for iter_33_8, iter_33_9 in ipairs(var_33_15) do
			var_33_22(iter_33_9, var_33_17, var_33_0.SubUnitList)
		end

		local var_33_23 = var_33_7:getChapterSupportFleet()

		if var_33_23 then
			local var_33_24 = var_33_23:getShips()

			for iter_33_10, iter_33_11 in pairs(var_33_24) do
				var_33_22(iter_33_11, {}, var_33_0.SupportUnitList)
			end
		end

		arg_33_0.viewComponent:setFleet(var_33_13, var_33_14, var_33_15)
	elseif var_33_1 == SYSTEM_CHALLENGE then
		local var_33_25 = arg_33_0.contextData.mode
		local var_33_26 = getProxy(ChallengeProxy):getUserChallengeInfo(var_33_25)

		var_33_0.ChallengeInfo = var_33_26

		arg_33_0.viewComponent:setChapter(var_33_26)

		local var_33_27 = var_33_26:getRegularFleet()

		var_33_0.CommanderList = var_33_27:buildBattleBuffList()

		local var_33_28 = _.values(var_33_27:getCommanders())
		local var_33_29 = {}
		local var_33_30 = var_33_27:getShipsByTeam(TeamType.Main, false)
		local var_33_31 = var_33_27:getShipsByTeam(TeamType.Vanguard, false)
		local var_33_32 = {}
		local var_33_33 = var_33_26:getSubmarineFleet()
		local var_33_34 = var_33_33:getShipsByTeam(TeamType.Submarine, false)

		if #var_33_34 > 0 then
			var_33_0.SubFlag = 1
			var_33_0.TotalSubAmmo = 1
			var_33_29 = _.values(var_33_33:getCommanders())
			var_33_0.SubCommanderList = var_33_33:buildBattleBuffList()
		else
			var_33_0.SubFlag = 0
			var_33_0.TotalSubAmmo = 0
		end

		arg_33_0.mainShips = {}

		local function var_33_35(arg_36_0, arg_36_1, arg_36_2)
			local var_36_0 = arg_36_0.id
			local var_36_1 = arg_36_0.hpRant * 0.0001

			if table.contains(var_33_5, var_36_0) then
				BattleVertify.cloneShipVertiry = true
			end

			var_33_5[#var_33_5 + 1] = var_36_0

			local var_36_2 = var_0_1(var_33_1, arg_36_0, arg_36_1)

			var_36_2.initHPRate = var_36_1

			table.insert(arg_33_0.mainShips, arg_36_0)
			table.insert(arg_36_2, var_36_2)
		end

		for iter_33_12, iter_33_13 in ipairs(var_33_30) do
			var_33_35(iter_33_13, var_33_28, var_33_0.MainUnitList)
		end

		for iter_33_14, iter_33_15 in ipairs(var_33_31) do
			var_33_35(iter_33_15, var_33_28, var_33_0.VanguardUnitList)
		end

		for iter_33_16, iter_33_17 in ipairs(var_33_34) do
			var_33_35(iter_33_17, var_33_29, var_33_0.SubUnitList)
		end

		arg_33_0.viewComponent:setFleet(var_33_30, var_33_31, var_33_34)
	elseif var_33_1 == SYSTEM_WORLD then
		local var_33_36 = nowWorld()
		local var_33_37 = var_33_36:GetActiveMap()
		local var_33_38 = var_33_37:GetFleet()
		local var_33_39 = var_33_37:GetCell(var_33_38.row, var_33_38.column):GetStageEnemy()
		local var_33_40 = var_33_39:GetHP()

		if var_33_40 then
			var_33_0.RepressInfo = {
				repressEnemyHpRant = var_33_40 / var_33_39:GetMaxHP()
			}
		end

		var_33_0.AffixBuffList = table.mergeArray(var_33_39:GetBattleLuaBuffs(), var_33_37:GetBattleLuaBuffs(WorldMap.FactionEnemy, var_33_39))

		local function var_33_41(arg_37_0)
			local var_37_0 = {}

			for iter_37_0, iter_37_1 in ipairs(arg_37_0) do
				local var_37_1 = {
					id = ys.Battle.BattleDataFunction.SkillTranform(var_33_1, iter_37_1.id),
					level = iter_37_1.level
				}

				table.insert(var_37_0, var_37_1)
			end

			return var_37_0
		end

		var_33_0.DefeatCount = var_33_38:getDefeatCount()
		var_33_0.ChapterBuffIDs, var_33_0.CommanderList = var_33_37:getFleetBattleBuffs(var_33_38, true)
		var_33_0.MapAuraSkills = var_33_37:GetChapterAuraBuffs()
		var_33_0.MapAuraSkills = var_33_41(var_33_0.MapAuraSkills)
		var_33_0.MapAidSkills = {}

		local var_33_42 = var_33_37:GetChapterAidBuffs()

		for iter_33_18, iter_33_19 in pairs(var_33_42) do
			local var_33_43 = var_33_37:GetFleet(iter_33_18.fleetId)
			local var_33_44 = _.values(var_33_43:getCommanders(true))
			local var_33_45 = var_0_1(var_33_1, WorldConst.FetchShipVO(iter_33_18.id), var_33_44)

			table.insert(var_33_0.AidUnitList, var_33_45)

			var_33_0.MapAidSkills = table.mergeArray(var_33_0.MapAidSkills, var_33_41(iter_33_19))
		end

		local var_33_46 = var_33_38:GetTeamShipVOs(TeamType.Main, false)
		local var_33_47 = var_33_38:GetTeamShipVOs(TeamType.Vanguard, false)
		local var_33_48 = {}
		local var_33_49 = _.values(var_33_38:getCommanders(true))
		local var_33_50 = {}
		local var_33_51 = var_33_36:GetSubAidFlag()

		if var_33_51 == true then
			local var_33_52 = var_33_37:GetSubmarineFleet()

			var_33_0.SubFlag = 1
			var_33_0.TotalSubAmmo = 1
			var_33_48 = var_33_52:GetTeamShipVOs(TeamType.Submarine, false)
			var_33_50 = _.values(var_33_52:getCommanders(true))

			local var_33_53, var_33_54 = var_33_37:getFleetBattleBuffs(var_33_52, true)

			var_33_0.SubCommanderList = var_33_54
		else
			var_33_0.SubFlag = 0

			if var_33_51 ~= ys.Battle.BattleConst.SubAidFlag.AID_EMPTY then
				var_33_0.TotalSubAmmo = 0
			end
		end

		arg_33_0.mainShips = {}

		for iter_33_20, iter_33_21 in ipairs(var_33_46) do
			local var_33_55 = iter_33_21.id
			local var_33_56 = WorldConst.FetchWorldShip(iter_33_21.id).hpRant * 0.0001

			if table.contains(var_33_5, var_33_55) then
				BattleVertify.cloneShipVertiry = true
			end

			var_33_5[#var_33_5 + 1] = var_33_55

			local var_33_57 = var_0_1(var_33_1, iter_33_21, var_33_49)

			var_33_57.initHPRate = var_33_56

			table.insert(arg_33_0.mainShips, iter_33_21)
			table.insert(var_33_0.MainUnitList, var_33_57)
		end

		for iter_33_22, iter_33_23 in ipairs(var_33_47) do
			local var_33_58 = iter_33_23.id
			local var_33_59 = WorldConst.FetchWorldShip(iter_33_23.id).hpRant * 0.0001

			if table.contains(var_33_5, var_33_58) then
				BattleVertify.cloneShipVertiry = true
			end

			var_33_5[#var_33_5 + 1] = var_33_58

			local var_33_60 = var_0_1(var_33_1, iter_33_23, var_33_49)

			var_33_60.initHPRate = var_33_59

			table.insert(arg_33_0.mainShips, iter_33_23)
			table.insert(var_33_0.VanguardUnitList, var_33_60)
		end

		for iter_33_24, iter_33_25 in ipairs(var_33_48) do
			local var_33_61 = iter_33_25.id
			local var_33_62 = WorldConst.FetchWorldShip(iter_33_25.id).hpRant * 0.0001

			if table.contains(var_33_5, var_33_61) then
				BattleVertify.cloneShipVertiry = true
			end

			var_33_5[#var_33_5 + 1] = var_33_61

			local var_33_63 = var_0_1(var_33_1, iter_33_25, var_33_50)

			var_33_63.initHPRate = var_33_62

			table.insert(arg_33_0.mainShips, iter_33_25)
			table.insert(var_33_0.SubUnitList, var_33_63)
		end

		arg_33_0.viewComponent:setFleet(var_33_46, var_33_47, var_33_48)

		local var_33_64 = pg.expedition_data_template[arg_33_0.contextData.stageId]

		if var_33_64.difficulty == ys.Battle.BattleConst.Difficulty.WORLD then
			var_33_0.WorldMapId = var_33_37.config.expedition_map_id
			var_33_0.WorldLevel = WorldConst.WorldLevelCorrect(var_33_37.config.expedition_level, var_33_64.type)
		end
	elseif var_33_1 == SYSTEM_WORLD_BOSS then
		local var_33_65 = nowWorld():GetBossProxy()
		local var_33_66 = arg_33_0.contextData.bossId
		local var_33_67 = var_33_65:GetFleet(var_33_66)
		local var_33_68 = var_33_65:GetBossById(var_33_66)

		assert(var_33_68, var_33_66)

		local var_33_69 = var_33_68:GetHP()

		if var_33_69 then
			if var_33_68:IsSelf() then
				var_33_0.RepressInfo = {
					repressEnemyHpRant = var_33_69 / var_33_68:GetMaxHp()
				}
			else
				var_33_0.RepressInfo = {
					repressEnemyHpRant = 1
				}
			end
		end

		local var_33_70 = _.values(var_33_67:getCommanders())

		var_33_0.CommanderList = var_33_67:buildBattleBuffList()
		arg_33_0.mainShips = var_33_4:getShipsByFleet(var_33_67)

		local var_33_71 = {}
		local var_33_72 = {}
		local var_33_73 = {}
		local var_33_74 = var_33_67:getTeamByName(TeamType.Main)

		for iter_33_26, iter_33_27 in ipairs(var_33_74) do
			if table.contains(var_33_5, iter_33_27) then
				BattleVertify.cloneShipVertiry = true
			end

			var_33_5[#var_33_5 + 1] = iter_33_27

			local var_33_75 = var_33_4:getShipById(iter_33_27)
			local var_33_76 = var_0_1(var_33_1, var_33_75, var_33_70)

			table.insert(var_33_71, var_33_75)
			table.insert(var_33_0.MainUnitList, var_33_76)
		end

		local var_33_77 = var_33_67:getTeamByName(TeamType.Vanguard)

		for iter_33_28, iter_33_29 in ipairs(var_33_77) do
			if table.contains(var_33_5, iter_33_29) then
				BattleVertify.cloneShipVertiry = true
			end

			var_33_5[#var_33_5 + 1] = iter_33_29

			local var_33_78 = var_33_4:getShipById(iter_33_29)
			local var_33_79 = var_0_1(var_33_1, var_33_78, var_33_70)

			table.insert(var_33_72, var_33_78)
			table.insert(var_33_0.VanguardUnitList, var_33_79)
		end

		arg_33_0.viewComponent:setFleet(var_33_71, var_33_72, var_33_73)

		var_33_0.MapAidSkills = {}

		if var_33_68:IsSelf() then
			local var_33_80, var_33_81, var_33_82 = var_33_65.GetSupportValue()

			if var_33_80 then
				table.insert(var_33_0.MapAidSkills, {
					level = 1,
					id = var_33_82
				})
			end
		end
	elseif var_33_1 == SYSTEM_HP_SHARE_ACT_BOSS or var_33_1 == SYSTEM_ACT_BOSS or var_33_1 == SYSTEM_ACT_BOSS_SP or var_33_1 == SYSTEM_BOSS_EXPERIMENT then
		if arg_33_0.contextData.mainFleetId then
			local var_33_83 = getProxy(FleetProxy):getActivityFleets()[arg_33_0.contextData.actId]
			local var_33_84 = var_33_83[arg_33_0.contextData.mainFleetId]
			local var_33_85 = _.values(var_33_84:getCommanders())

			var_33_0.CommanderList = var_33_84:buildBattleBuffList()
			arg_33_0.mainShips = {}

			local var_33_86 = {}
			local var_33_87 = {}
			local var_33_88 = {}

			local function var_33_89(arg_38_0, arg_38_1, arg_38_2, arg_38_3)
				if table.contains(var_33_5, arg_38_0) then
					BattleVertify.cloneShipVertiry = true
				end

				var_33_5[#var_33_5 + 1] = arg_38_0

				local var_38_0 = var_33_4:getShipById(arg_38_0)
				local var_38_1 = var_0_1(var_33_1, var_38_0, arg_38_1)

				table.insert(arg_33_0.mainShips, var_38_0)
				table.insert(arg_38_3, var_38_0)
				table.insert(arg_38_2, var_38_1)
			end

			local var_33_90 = var_33_84:getTeamByName(TeamType.Main)
			local var_33_91 = var_33_84:getTeamByName(TeamType.Vanguard)

			for iter_33_30, iter_33_31 in ipairs(var_33_90) do
				var_33_89(iter_33_31, var_33_85, var_33_0.MainUnitList, var_33_86)
			end

			for iter_33_32, iter_33_33 in ipairs(var_33_91) do
				var_33_89(iter_33_33, var_33_85, var_33_0.VanguardUnitList, var_33_87)
			end

			local var_33_92 = var_33_83[arg_33_0.contextData.mainFleetId + 10]
			local var_33_93 = _.values(var_33_92:getCommanders())
			local var_33_94 = var_33_92:getTeamByName(TeamType.Submarine)

			for iter_33_34, iter_33_35 in ipairs(var_33_94) do
				var_33_89(iter_33_35, var_33_93, var_33_0.SubUnitList, var_33_88)
			end

			local var_33_95 = getProxy(PlayerProxy):getRawData()
			local var_33_96 = getProxy(ActivityProxy):getActivityById(arg_33_0.contextData.actId)
			local var_33_97 = var_33_96:getConfig("config_id")
			local var_33_98 = pg.activity_event_worldboss[var_33_97].use_oil_limit[arg_33_0.contextData.mainFleetId]
			local var_33_99 = var_33_96:IsOilLimit(arg_33_0.contextData.stageId)
			local var_33_100 = 0
			local var_33_101 = var_33_3.oil_cost > 0

			local function var_33_102(arg_39_0, arg_39_1)
				if var_33_101 then
					local var_39_0 = arg_39_0:getEndCost().oil

					if arg_39_1 > 0 then
						local var_39_1 = arg_39_0:getStartCost().oil

						cost = math.clamp(arg_39_1 - var_39_1, 0, var_39_0)
					end

					var_33_100 = var_33_100 + var_39_0
				end
			end

			if var_33_1 == SYSTEM_ACT_BOSS_SP then
				local var_33_103 = getProxy(ActivityProxy):GetActivityBossRuntime(arg_33_0.contextData.actId).buffIds
				local var_33_104 = _.map(var_33_103, function(arg_40_0)
					return ActivityBossBuff.New({
						configId = arg_40_0
					})
				end)

				var_33_0.ExtraBuffList = _.map(_.select(var_33_104, function(arg_41_0)
					return arg_41_0:CastOnEnemy()
				end), function(arg_42_0)
					return arg_42_0:GetBuffID()
				end)
				var_33_0.ChapterBuffIDs = _.map(_.select(var_33_104, function(arg_43_0)
					return not arg_43_0:CastOnEnemy()
				end), function(arg_44_0)
					return arg_44_0:GetBuffID()
				end)
			else
				var_33_102(var_33_84, var_33_99 and var_33_98[1] or 0)
				var_33_102(var_33_92, var_33_99 and var_33_98[2] or 0)
			end

			if var_33_92:isLegalToFight() == true and (var_33_1 == SYSTEM_BOSS_EXPERIMENT or var_33_100 <= var_33_95.oil) then
				var_33_0.SubFlag = 1
				var_33_0.TotalSubAmmo = 1
			end

			var_33_0.SubCommanderList = var_33_92:buildBattleBuffList()

			arg_33_0.viewComponent:setFleet(var_33_86, var_33_87, var_33_88)
		end
	elseif var_33_1 == SYSTEM_GUILD then
		local var_33_105 = getProxy(GuildProxy):getRawData():GetActiveEvent():GetBossMission()
		local var_33_106 = var_33_105:GetMainFleet()
		local var_33_107 = _.values(var_33_106:getCommanders())

		var_33_0.CommanderList = var_33_106:BuildBattleBuffList()
		arg_33_0.mainShips = {}

		local var_33_108 = {}
		local var_33_109 = {}
		local var_33_110 = {}

		local function var_33_111(arg_45_0, arg_45_1, arg_45_2, arg_45_3)
			local var_45_0 = var_0_1(var_33_1, arg_45_0, arg_45_1)

			table.insert(arg_33_0.mainShips, arg_45_0)
			table.insert(arg_45_3, arg_45_0)
			table.insert(arg_45_2, var_45_0)
		end

		local var_33_112 = {}
		local var_33_113 = {}
		local var_33_114 = var_33_106:GetShips()

		for iter_33_36, iter_33_37 in pairs(var_33_114) do
			local var_33_115 = iter_33_37.ship

			if var_33_115:getTeamType() == TeamType.Main then
				table.insert(var_33_112, var_33_115)
			elseif var_33_115:getTeamType() == TeamType.Vanguard then
				table.insert(var_33_113, var_33_115)
			end
		end

		for iter_33_38, iter_33_39 in ipairs(var_33_112) do
			var_33_111(iter_33_39, var_33_107, var_33_0.MainUnitList, var_33_108)
		end

		for iter_33_40, iter_33_41 in ipairs(var_33_113) do
			var_33_111(iter_33_41, var_33_107, var_33_0.VanguardUnitList, var_33_109)
		end

		local var_33_116 = var_33_105:GetSubFleet()
		local var_33_117 = _.values(var_33_116:getCommanders())
		local var_33_118 = {}
		local var_33_119 = var_33_116:GetShips()

		for iter_33_42, iter_33_43 in pairs(var_33_119) do
			local var_33_120 = iter_33_43.ship

			if var_33_120:getTeamType() == TeamType.Submarine then
				table.insert(var_33_118, var_33_120)
			end
		end

		for iter_33_44, iter_33_45 in ipairs(var_33_118) do
			var_33_111(iter_33_45, var_33_117, var_33_0.SubUnitList, var_33_110)
		end

		if #var_33_110 > 0 then
			var_33_0.SubFlag = 1
			var_33_0.TotalSubAmmo = 1
		end

		var_33_0.SubCommanderList = var_33_116:BuildBattleBuffList()

		arg_33_0.viewComponent:setFleet(var_33_108, var_33_109, var_33_110)
	elseif var_33_1 == SYSTEM_BOSS_RUSH or var_33_1 == SYSTEM_BOSS_RUSH_EX then
		local var_33_121 = getProxy(ActivityProxy):getActivityById(arg_33_0.contextData.actId):GetSeriesData()

		assert(var_33_121)

		local var_33_122 = var_33_121:GetStaegLevel() + 1
		local var_33_123 = var_33_121:GetFleetIds()
		local var_33_124 = var_33_123[var_33_122]
		local var_33_125 = var_33_123[#var_33_123]

		if var_33_121:GetMode() == BossRushSeriesData.MODE.SINGLE then
			var_33_124 = var_33_123[1]
		end

		local var_33_126 = getProxy(FleetProxy):getActivityFleets()[arg_33_0.contextData.actId]

		arg_33_0.mainShips = {}

		local var_33_127 = {}
		local var_33_128 = {}
		local var_33_129 = {}

		local function var_33_130(arg_46_0, arg_46_1, arg_46_2, arg_46_3)
			if table.contains(var_33_5, arg_46_0) then
				BattleVertify.cloneShipVertiry = true
			end

			var_33_5[#var_33_5 + 1] = arg_46_0

			local var_46_0 = var_33_4:getShipById(arg_46_0)
			local var_46_1 = var_0_1(var_33_1, var_46_0, arg_46_1)

			table.insert(arg_33_0.mainShips, var_46_0)
			table.insert(arg_46_3, var_46_0)
			table.insert(arg_46_2, var_46_1)
		end

		local var_33_131 = var_33_126[var_33_124]
		local var_33_132 = _.values(var_33_131:getCommanders())

		var_33_0.CommanderList = var_33_131:buildBattleBuffList()

		local var_33_133 = var_33_131:getTeamByName(TeamType.Main)
		local var_33_134 = var_33_131:getTeamByName(TeamType.Vanguard)

		for iter_33_46, iter_33_47 in ipairs(var_33_133) do
			var_33_130(iter_33_47, var_33_132, var_33_0.MainUnitList, var_33_127)
		end

		for iter_33_48, iter_33_49 in ipairs(var_33_134) do
			var_33_130(iter_33_49, var_33_132, var_33_0.VanguardUnitList, var_33_128)
		end

		local var_33_135 = var_33_126[var_33_125]
		local var_33_136 = _.values(var_33_135:getCommanders())

		var_33_0.SubCommanderList = var_33_135:buildBattleBuffList()

		local var_33_137 = var_33_135:getTeamByName(TeamType.Submarine)

		for iter_33_50, iter_33_51 in ipairs(var_33_137) do
			var_33_130(iter_33_51, var_33_136, var_33_0.SubUnitList, var_33_129)
		end

		local var_33_138 = getProxy(PlayerProxy):getRawData()
		local var_33_139 = 0
		local var_33_140 = var_33_121:GetOilLimit()
		local var_33_141 = var_33_3.oil_cost > 0

		local function var_33_142(arg_47_0, arg_47_1)
			local var_47_0 = 0

			if var_33_141 then
				local var_47_1 = arg_47_0:getStartCost().oil
				local var_47_2 = arg_47_0:getEndCost().oil

				var_47_0 = var_47_2

				if arg_47_1 > 0 then
					var_47_0 = math.clamp(arg_47_1 - var_47_1, 0, var_47_2)
				end
			end

			return var_47_0
		end

		local var_33_143 = var_33_139 + var_33_142(var_33_131, var_33_140[1]) + var_33_142(var_33_135, var_33_140[2])

		if var_33_135:isLegalToFight() == true and var_33_143 <= var_33_138.oil then
			var_33_0.SubFlag = 1
			var_33_0.TotalSubAmmo = 1
		end

		arg_33_0.viewComponent:setFleet(var_33_127, var_33_128, var_33_129)
	elseif var_33_1 == SYSTEM_LIMIT_CHALLENGE then
		local var_33_144 = LimitChallengeConst.GetChallengeIDByStageID(arg_33_0.contextData.stageId)

		var_33_0.ExtraBuffList = AcessWithinNull(pg.expedition_constellation_challenge_template[var_33_144], "buff_id")

		local var_33_145 = FleetProxy.CHALLENGE_FLEET_ID
		local var_33_146 = FleetProxy.CHALLENGE_SUB_FLEET_ID
		local var_33_147 = getProxy(FleetProxy)
		local var_33_148 = var_33_147:getFleetById(var_33_145)
		local var_33_149 = var_33_147:getFleetById(var_33_146)

		arg_33_0.mainShips = {}

		local var_33_150 = {}
		local var_33_151 = {}
		local var_33_152 = {}

		local function var_33_153(arg_48_0, arg_48_1, arg_48_2, arg_48_3)
			if table.contains(var_33_5, arg_48_0) then
				BattleVertify.cloneShipVertiry = true
			end

			var_33_5[#var_33_5 + 1] = arg_48_0

			local var_48_0 = var_33_4:getShipById(arg_48_0)
			local var_48_1 = var_0_1(var_33_1, var_48_0, arg_48_1)

			table.insert(arg_33_0.mainShips, var_48_0)
			table.insert(arg_48_3, var_48_0)
			table.insert(arg_48_2, var_48_1)
		end

		local var_33_154 = _.values(var_33_148:getCommanders())

		var_33_0.CommanderList = var_33_148:buildBattleBuffList()

		local var_33_155 = var_33_148:getTeamByName(TeamType.Main)
		local var_33_156 = var_33_148:getTeamByName(TeamType.Vanguard)

		for iter_33_52, iter_33_53 in ipairs(var_33_155) do
			var_33_153(iter_33_53, var_33_154, var_33_0.MainUnitList, var_33_150)
		end

		for iter_33_54, iter_33_55 in ipairs(var_33_156) do
			var_33_153(iter_33_55, var_33_154, var_33_0.VanguardUnitList, var_33_151)
		end

		local var_33_157 = _.values(var_33_149:getCommanders())

		var_33_0.SubCommanderList = var_33_149:buildBattleBuffList()

		local var_33_158 = var_33_149:getTeamByName(TeamType.Submarine)

		for iter_33_56, iter_33_57 in ipairs(var_33_158) do
			var_33_153(iter_33_57, var_33_157, var_33_0.SubUnitList, var_33_152)
		end

		local var_33_159 = getProxy(PlayerProxy):getRawData()
		local var_33_160 = 0
		local var_33_161 = var_33_3.oil_cost > 0

		local function var_33_162(arg_49_0, arg_49_1)
			local var_49_0 = 0

			if var_33_161 then
				local var_49_1 = arg_49_0:getStartCost().oil
				local var_49_2 = arg_49_0:getEndCost().oil

				var_49_0 = var_49_2

				if arg_49_1 > 0 then
					var_49_0 = math.clamp(arg_49_1 - var_49_1, 0, var_49_2)
				end
			end

			return var_49_0
		end

		local var_33_163 = var_33_160 + var_33_162(var_33_148, 0) + var_33_162(var_33_149, 0)

		if var_33_149:isLegalToFight() == true and var_33_163 <= var_33_159.oil then
			var_33_0.SubFlag = 1
			var_33_0.TotalSubAmmo = 1
		end

		arg_33_0.viewComponent:setFleet(var_33_150, var_33_151, var_33_152)
	elseif var_33_1 == SYSTEM_CARDPUZZLE then
		local var_33_164 = {}
		local var_33_165 = {}
		local var_33_166 = arg_33_0.contextData.relics

		for iter_33_58, iter_33_59 in ipairs(arg_33_0.contextData.cardPuzzleFleet) do
			local var_33_167 = var_0_2(iter_33_59, var_33_166)
			local var_33_168 = var_33_167.fleetIndex

			if var_33_168 == 1 then
				table.insert(var_33_165, var_33_167)
				table.insert(var_33_0.VanguardUnitList, var_33_167)
			elseif var_33_168 == 2 then
				table.insert(var_33_164, var_33_167)
				table.insert(var_33_0.MainUnitList, var_33_167)
			end
		end

		var_33_0.CardPuzzleCardIDList = arg_33_0.contextData.cards
		var_33_0.CardPuzzleCommonHPValue = arg_33_0.contextData.hp
		var_33_0.CardPuzzleRelicList = var_33_166
		var_33_0.CardPuzzleCombatID = arg_33_0.contextData.puzzleCombatID
	elseif var_33_1 == SYSTEM_BOSS_SINGLE then
		if arg_33_0.contextData.mainFleetId then
			local var_33_169 = getProxy(FleetProxy):getActivityFleets()[arg_33_0.contextData.actId]
			local var_33_170 = var_33_169[arg_33_0.contextData.mainFleetId]
			local var_33_171 = _.values(var_33_170:getCommanders())

			var_33_0.CommanderList = var_33_170:buildBattleBuffList()
			arg_33_0.mainShips = {}

			local var_33_172 = {}
			local var_33_173 = {}
			local var_33_174 = {}

			local function var_33_175(arg_50_0, arg_50_1, arg_50_2, arg_50_3)
				if table.contains(var_33_5, arg_50_0) then
					BattleVertify.cloneShipVertiry = true
				end

				var_33_5[#var_33_5 + 1] = arg_50_0

				local var_50_0 = var_33_4:getShipById(arg_50_0)
				local var_50_1 = var_0_1(var_33_1, var_50_0, arg_50_1)

				table.insert(arg_33_0.mainShips, var_50_0)
				table.insert(arg_50_3, var_50_0)
				table.insert(arg_50_2, var_50_1)
			end

			local var_33_176 = var_33_170:getTeamByName(TeamType.Main)
			local var_33_177 = var_33_170:getTeamByName(TeamType.Vanguard)

			for iter_33_60, iter_33_61 in ipairs(var_33_176) do
				var_33_175(iter_33_61, var_33_171, var_33_0.MainUnitList, var_33_172)
			end

			for iter_33_62, iter_33_63 in ipairs(var_33_177) do
				var_33_175(iter_33_63, var_33_171, var_33_0.VanguardUnitList, var_33_173)
			end

			local var_33_178 = var_33_169[arg_33_0.contextData.mainFleetId + 10]
			local var_33_179 = _.values(var_33_178:getCommanders())
			local var_33_180 = var_33_178:getTeamByName(TeamType.Submarine)

			for iter_33_64, iter_33_65 in ipairs(var_33_180) do
				var_33_175(iter_33_65, var_33_179, var_33_0.SubUnitList, var_33_174)
			end

			local var_33_181 = getProxy(PlayerProxy):getRawData()
			local var_33_182 = getProxy(ActivityProxy):getActivityById(arg_33_0.contextData.actId)

			var_33_0.ChapterBuffIDs = var_33_182:GetBuffIdsByStageId(arg_33_0.contextData.stageId)

			local var_33_183 = var_33_182:GetEnemyDataByStageId(arg_33_0.contextData.stageId):GetOilLimit()
			local var_33_184 = 0
			local var_33_185 = var_33_3.oil_cost > 0

			local function var_33_186(arg_51_0, arg_51_1)
				if var_33_185 then
					local var_51_0 = arg_51_0:getEndCost().oil

					if arg_51_1 > 0 then
						local var_51_1 = arg_51_0:getStartCost().oil

						cost = math.clamp(arg_51_1 - var_51_1, 0, var_51_0)
					end

					var_33_184 = var_33_184 + var_51_0
				end
			end

			var_33_186(var_33_170, var_33_183[1] or 0)
			var_33_186(var_33_178, var_33_183[2] or 0)

			if var_33_178:isLegalToFight() == true and var_33_184 <= var_33_181.oil then
				var_33_0.SubFlag = 1
				var_33_0.TotalSubAmmo = 1
			end

			var_33_0.SubCommanderList = var_33_178:buildBattleBuffList()

			arg_33_0.viewComponent:setFleet(var_33_172, var_33_173, var_33_174)
		end
	elseif arg_33_0.contextData.mainFleetId then
		local var_33_187 = var_33_1 == SYSTEM_DUEL
		local var_33_188 = getProxy(FleetProxy)
		local var_33_189
		local var_33_190
		local var_33_191 = var_33_188:getFleetById(arg_33_0.contextData.mainFleetId)

		arg_33_0.mainShips = var_33_4:getShipsByFleet(var_33_191)

		local var_33_192 = {}
		local var_33_193 = {}
		local var_33_194 = {}

		local function var_33_195(arg_52_0, arg_52_1, arg_52_2)
			for iter_52_0, iter_52_1 in ipairs(arg_52_0) do
				if table.contains(var_33_5, iter_52_1) then
					BattleVertify.cloneShipVertiry = true
				end

				var_33_5[#var_33_5 + 1] = iter_52_1

				local var_52_0 = var_33_4:getShipById(iter_52_1)
				local var_52_1 = var_0_1(var_33_1, var_52_0, nil, var_33_187)

				table.insert(arg_52_1, var_52_0)
				table.insert(arg_52_2, var_52_1)
			end
		end

		local var_33_196 = var_33_191:getTeamByName(TeamType.Main)
		local var_33_197 = var_33_191:getTeamByName(TeamType.Vanguard)
		local var_33_198 = var_33_191:getTeamByName(TeamType.Submarine)

		var_33_195(var_33_196, var_33_192, var_33_0.MainUnitList)
		var_33_195(var_33_197, var_33_193, var_33_0.VanguardUnitList)
		var_33_195(var_33_198, var_33_194, var_33_0.SubUnitList)
		arg_33_0.viewComponent:setFleet(var_33_192, var_33_193, var_33_194)

		if BATTLE_DEBUG and BATTLE_FREE_SUBMARINE then
			local var_33_199 = var_33_188:getFleetById(11)
			local var_33_200 = var_33_199:getTeamByName(TeamType.Submarine)

			if #var_33_200 > 0 then
				var_33_0.SubFlag = 1
				var_33_0.TotalSubAmmo = 1

				local var_33_201 = _.values(var_33_199:getCommanders())

				var_33_0.SubCommanderList = var_33_199:buildBattleBuffList()

				for iter_33_66, iter_33_67 in ipairs(var_33_200) do
					local var_33_202 = var_33_4:getShipById(iter_33_67)
					local var_33_203 = var_0_1(var_33_1, var_33_202, var_33_201, var_33_187)

					table.insert(var_33_194, var_33_202)
					table.insert(var_33_0.SubUnitList, var_33_203)
				end
			end
		end
	end

	if var_33_1 == SYSTEM_WORLD then
		local var_33_204 = nowWorld()
		local var_33_205 = var_33_204:GetActiveMap()
		local var_33_206 = var_33_205:GetFleet()
		local var_33_207 = var_33_205:GetCell(var_33_206.row, var_33_206.column):GetStageEnemy()
		local var_33_208 = pg.world_expedition_data[arg_33_0.contextData.stageId]
		local var_33_209 = var_33_204:GetWorldMapDifficultyBuffLevel()

		var_33_0.EnemyMapRewards = {
			var_33_209[1] * (1 + var_33_208.expedition_sairenvalueA / 10000),
			var_33_209[2] * (1 + var_33_208.expedition_sairenvalueB / 10000),
			var_33_209[3] * (1 + var_33_208.expedition_sairenvalueC / 10000)
		}
		var_33_0.FleetMapRewards = var_33_204:GetWorldMapBuffLevel()
	end

	var_33_0.RivalMainUnitList, var_33_0.RivalVanguardUnitList = {}, {}

	local var_33_210

	if var_33_1 == SYSTEM_DUEL and arg_33_0.contextData.rivalId then
		local var_33_211 = getProxy(MilitaryExerciseProxy)

		var_33_210 = var_33_211:getRivalById(arg_33_0.contextData.rivalId)
		arg_33_0.oldRank = var_33_211:getSeasonInfo()
	end

	if var_33_210 then
		var_33_0.RivalVO = var_33_210

		local var_33_212 = 0

		for iter_33_68, iter_33_69 in ipairs(var_33_210.mainShips) do
			var_33_212 = var_33_212 + iter_33_69.level
		end

		for iter_33_70, iter_33_71 in ipairs(var_33_210.vanguardShips) do
			var_33_212 = var_33_212 + iter_33_71.level
		end

		BattleVertify = BattleVertify or {}
		BattleVertify.rivalLevel = var_33_212

		for iter_33_72, iter_33_73 in ipairs(var_33_210.mainShips) do
			if not iter_33_73.hpRant or iter_33_73.hpRant > 0 then
				local var_33_213 = var_0_1(var_33_1, iter_33_73, nil, true)

				if iter_33_73.hpRant then
					var_33_213.initHPRate = iter_33_73.hpRant * 0.0001
				end

				table.insert(var_33_0.RivalMainUnitList, var_33_213)
			end
		end

		for iter_33_74, iter_33_75 in ipairs(var_33_210.vanguardShips) do
			if not iter_33_75.hpRant or iter_33_75.hpRant > 0 then
				local var_33_214 = var_0_1(var_33_1, iter_33_75, nil, true)

				if iter_33_75.hpRant then
					var_33_214.initHPRate = iter_33_75.hpRant * 0.0001
				end

				table.insert(var_33_0.RivalVanguardUnitList, var_33_214)
			end
		end
	end

	local var_33_215 = arg_33_0.contextData.prefabFleet.main_unitList
	local var_33_216 = arg_33_0.contextData.prefabFleet.vanguard_unitList
	local var_33_217 = arg_33_0.contextData.prefabFleet.submarine_unitList

	if var_33_215 then
		for iter_33_76, iter_33_77 in ipairs(var_33_215) do
			local var_33_218 = {}

			for iter_33_78, iter_33_79 in ipairs(iter_33_77.equipment) do
				var_33_218[#var_33_218 + 1] = {
					skin = 0,
					id = iter_33_79
				}
			end

			local var_33_219 = {
				id = iter_33_77.id,
				tmpID = iter_33_77.configId,
				skinId = iter_33_77.skinId,
				level = iter_33_77.level,
				equipment = var_33_218,
				properties = iter_33_77.properties,
				baseProperties = iter_33_77.properties,
				proficiency = {
					1,
					1,
					1
				},
				skills = iter_33_77.skills
			}

			table.insert(var_33_0.MainUnitList, var_33_219)
		end
	end

	if var_33_216 then
		for iter_33_80, iter_33_81 in ipairs(var_33_216) do
			local var_33_220 = {}

			for iter_33_82, iter_33_83 in ipairs(iter_33_81.equipment) do
				var_33_220[#var_33_220 + 1] = {
					skin = 0,
					id = iter_33_83
				}
			end

			local var_33_221 = {
				id = iter_33_81.id,
				tmpID = iter_33_81.configId,
				skinId = iter_33_81.skinId,
				level = iter_33_81.level,
				equipment = var_33_220,
				properties = iter_33_81.properties,
				baseProperties = iter_33_81.properties,
				proficiency = {
					1,
					1,
					1
				},
				skills = iter_33_81.skills
			}

			table.insert(var_33_0.VanguardUnitList, var_33_221)
		end
	end

	if var_33_217 then
		for iter_33_84, iter_33_85 in ipairs(var_33_217) do
			local var_33_222 = {}

			for iter_33_86, iter_33_87 in ipairs(iter_33_85.equipment) do
				var_33_222[#var_33_222 + 1] = {
					skin = 0,
					id = iter_33_87
				}
			end

			local var_33_223 = {
				id = iter_33_85.id,
				tmpID = iter_33_85.configId,
				skinId = iter_33_85.skinId,
				level = iter_33_85.level,
				equipment = var_33_222,
				properties = iter_33_85.properties,
				baseProperties = iter_33_85.properties,
				proficiency = {
					1,
					1,
					1
				},
				skills = iter_33_85.skills
			}

			table.insert(var_33_0.SubUnitList, var_33_223)

			if var_33_1 == SYSTEM_SIMULATION and #var_33_0.SubUnitList > 0 then
				var_33_0.SubFlag = 1
				var_33_0.TotalSubAmmo = 1
			end
		end
	end
end

function var_0_0.listNotificationInterests(arg_53_0)
	return {
		GAME.FINISH_STAGE_DONE,
		GAME.FINISH_STAGE_ERROR,
		GAME.STORY_BEGIN,
		GAME.STORY_END,
		GAME.END_GUIDE,
		GAME.START_GUIDE,
		GAME.PAUSE_BATTLE,
		GAME.RESUME_BATTLE,
		var_0_0.CLOSE_CHAT,
		GAME.QUIT_BATTLE,
		var_0_0.HIDE_ALL_BUTTONS
	}
end

function var_0_0.handleNotification(arg_54_0, arg_54_1)
	local var_54_0 = arg_54_1:getName()
	local var_54_1 = arg_54_1:getBody()
	local var_54_2 = ys.Battle.BattleState.GetInstance()
	local var_54_3 = arg_54_0.contextData.system

	if var_54_0 == GAME.FINISH_STAGE_DONE then
		pg.MsgboxMgr.GetInstance():hide()

		local var_54_4 = var_54_1.system

		if var_54_4 == SYSTEM_PROLOGUE then
			ys.Battle.BattleState.GetInstance():Deactive()
			arg_54_0:sendNotification(GAME.CHANGE_SCENE, SCENE.CREATE_PLAYER)
		elseif var_54_4 == SYSTEM_PERFORM or var_54_4 == SYSTEM_SIMULATION then
			ys.Battle.BattleState.GetInstance():Deactive()
			arg_54_0.viewComponent:exitBattle()

			if var_54_1.exitCallback then
				var_54_1.exitCallback()
			end
		else
			local var_54_5 = BattleResultMediator.GetResultView(var_54_4)
			local var_54_6 = {}

			if var_54_4 == SYSTEM_SCENARIO then
				var_54_6 = getProxy(ChapterProxy):getActiveChapter().operationBuffList
			end

			arg_54_0:addSubLayers(Context.New({
				mediator = NewBattleResultMediator,
				viewComponent = NewBattleResultScene,
				data = {
					system = var_54_4,
					rivalId = arg_54_0.contextData.rivalId,
					mainFleetId = arg_54_0.contextData.mainFleetId,
					stageId = arg_54_0.contextData.stageId,
					oldMainShips = arg_54_0.mainShips or {},
					oldPlayer = arg_54_0.player,
					oldRank = arg_54_0.oldRank,
					statistics = var_54_1.statistics,
					score = var_54_1.score,
					drops = var_54_1.drops,
					bossId = var_54_1.bossId,
					name = var_54_1.name,
					prefabFleet = var_54_1.prefabFleet,
					commanderExps = var_54_1.commanderExps,
					actId = arg_54_0.contextData.actId,
					result = var_54_1.result,
					extraDrops = var_54_1.extraDrops,
					extraBuffList = var_54_6,
					isLastBonus = var_54_1.isLastBonus,
					continuousBattleTimes = arg_54_0.contextData.continuousBattleTimes,
					totalBattleTimes = arg_54_0.contextData.totalBattleTimes,
					mode = arg_54_0.contextData.mode,
					cmdArgs = arg_54_0.contextData.cmdArgs
				}
			}))
		end
	elseif var_54_0 == GAME.STORY_BEGIN then
		var_54_2:Pause()
	elseif var_54_0 == GAME.STORY_END then
		var_54_2:Resume()
	elseif var_54_0 == GAME.START_GUIDE then
		var_54_2:Pause()
	elseif var_54_0 == GAME.END_GUIDE then
		var_54_2:Resume()
	elseif var_54_0 == GAME.PAUSE_BATTLE then
		if not var_54_2:IsPause() then
			arg_54_0:onPauseBtn()
		end
	elseif var_54_0 == GAME.RESUME_BATTLE then
		var_54_2:Resume()
	elseif var_54_0 == GAME.FINISH_STAGE_ERROR then
		gcAll(true)

		local var_54_7 = getProxy(ContextProxy)
		local var_54_8 = var_54_7:getContextByMediator(DailyLevelMediator)
		local var_54_9 = var_54_7:getContextByMediator(LevelMediator2)
		local var_54_10 = var_54_7:getContextByMediator(ChallengeMainMediator)
		local var_54_11 = var_54_7:getContextByMediator(ActivityBossMediatorTemplate)

		if var_54_8 then
			local var_54_12 = var_54_8:getContextByMediator(PreCombatMediator)

			var_54_8:removeChild(var_54_12)
		elseif var_54_10 then
			local var_54_13 = var_54_10:getContextByMediator(ChallengePreCombatMediator)

			var_54_10:removeChild(var_54_13)
		elseif var_54_9 then
			if var_54_3 == SYSTEM_DUEL then
				-- block empty
			elseif var_54_3 == SYSTEM_SCENARIO then
				local var_54_14 = var_54_9:getContextByMediator(ChapterPreCombatMediator)

				var_54_9:removeChild(var_54_14)
			elseif var_54_3 ~= SYSTEM_PERFORM and var_54_3 ~= SYSTEM_SIMULATION then
				local var_54_15 = var_54_9:getContextByMediator(PreCombatMediator)

				if var_54_15 then
					var_54_9:removeChild(var_54_15)
				end
			end
		elseif var_54_11 then
			local var_54_16 = var_54_11:getContextByMediator(PreCombatMediator)

			if var_54_16 then
				var_54_11:removeChild(var_54_16)
			end
		end

		arg_54_0:sendNotification(GAME.GO_BACK)
	elseif var_54_0 == var_0_0.CLOSE_CHAT then
		arg_54_0.viewComponent:OnCloseChat()
	elseif var_54_0 == var_0_0.HIDE_ALL_BUTTONS then
		ys.Battle.BattleState.GetInstance():GetProxyByName(ys.Battle.BattleDataProxy.__name):DispatchEvent(ys.Event.New(ys.Battle.BattleEvent.HIDE_INTERACTABLE_BUTTONS, {
			isActive = var_54_1
		}))
	elseif var_54_0 == GAME.QUIT_BATTLE then
		var_54_2:Stop()
	end
end

function var_0_0.remove(arg_55_0)
	pg.BrightnessMgr.GetInstance():SetScreenNeverSleep(false)
end

return var_0_0
