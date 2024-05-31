local var_0_0 = class("BattleScene", import("..base.BaseUI"))

var_0_0.IN_VIEW_FRIEND_SKILL_OFFSET = Vector3(-5, 0, 6)
var_0_0.IN_VIEW_FOE_SKILL_OFFSET = Vector3(-15, 0, 6)
var_0_0.FOE_SIDE_X_OFFSET = 250
var_0_0.SKILL_FLOAT_SCALE = Vector3(1.5, 1.5, 0)
var_0_0.SIDE_ALIGNMENT = {
	{
		-120,
		-7.5,
		-232.5
	},
	{
		105,
		217.5,
		330
	},
	{
		-345,
		-457.5,
		-570
	}
}

local var_0_1

function var_0_0.getUIName(arg_1_0)
	return "CombatUI"
end

function var_0_0.getBGM(arg_2_0)
	local var_2_0 = {}

	table.insert(var_2_0, arg_2_0.contextData.system == SYSTEM_WORLD and checkExist(pg.world_expedition_data[arg_2_0.contextData.stageId], {
		"bgm"
	}) or "")
	table.insert(var_2_0, pg.expedition_data_template[arg_2_0.contextData.stageId].bgm)

	for iter_2_0, iter_2_1 in ipairs(var_2_0) do
		if iter_2_1 ~= "" then
			return iter_2_1
		end
	end

	return var_0_0.super.getBGM(arg_2_0)
end

function var_0_0.init(arg_3_0)
	var_0_1 = ys.Battle.BattleVariable

	local var_3_0 = pg.UIMgr.GetInstance():GetMainCamera()
	local var_3_1 = GameObject.Find("UICamera")

	arg_3_0.uiCanvas = findTF(var_3_1, "Canvas/UIMain")
	arg_3_0.skillTips = arg_3_0:findTF("Skill_Activation")
	arg_3_0.skillRoot = arg_3_0:findTF("Skill_Activation/Root")
	arg_3_0.skillTpl = arg_3_0:findTF("Skill_Activation/mask").gameObject
	arg_3_0._skillFloatPool = pg.Pool.New(arg_3_0.skillRoot, arg_3_0.skillTpl, 15, 10, true, false):InitSize()
	arg_3_0.skillCMDRoot = arg_3_0:findTF("Skill_Activation/Root_cmd")
	arg_3_0.skillCMDTpl = arg_3_0:findTF("Skill_Activation/mask_cmd").gameObject
	arg_3_0._skillFloatCMDPool = pg.Pool.New(arg_3_0.skillCMDRoot, arg_3_0.skillCMDTpl, 2, 4, true, false):InitSize()
	arg_3_0.popupTpl = arg_3_0:getTpl("popup")

	SetActive(arg_3_0._go, false)

	arg_3_0._skillPaintings = {}
	arg_3_0._skillFloat = true
	arg_3_0._cacheSkill = {}
	arg_3_0._commanderSkillList = {}
	arg_3_0._sideSkillFloatStateList = {}
	arg_3_0._sideSkillFloatStateList[ys.Battle.BattleConfig.FRIENDLY_CODE] = {
		{},
		{},
		{}
	}
	arg_3_0._sideSkillFloatStateList[ys.Battle.BattleConfig.FOE_CODE] = {
		{},
		{},
		{}
	}

	arg_3_0:initPainting()

	arg_3_0._fxContainerUpper = arg_3_0._tf:Find("FXContainerUpper")
	arg_3_0._fxContainerBottom = arg_3_0._tf:Find("FXContainerBottom")

	local var_3_2 = arg_3_0._tf:GetComponentInParent(typeof(UnityEngine.Canvas))

	arg_3_0._canvasOrder = var_3_2 and var_3_2.sortingOrder or 0
	arg_3_0._ratioFitter = GetComponent(arg_3_0._tf, typeof(AspectRatioFitter))
end

function var_0_0.initPainting(arg_4_0)
	local var_4_0 = ys.Battle.BattleResourceManager.GetInstance():InstSkillPaintingUI()

	setParent(var_4_0, arg_4_0.uiCanvas, false)

	arg_4_0._paintingUI = var_4_0
	arg_4_0._paintingAnimator = var_4_0:GetComponent(typeof(Animator))
	arg_4_0._paintingAnimator.enabled = false
	arg_4_0._paintingParticleContainer = findTF(var_4_0, "particleContainer")
	arg_4_0._paintingParticles = findTF(arg_4_0._paintingParticleContainer, "effect")
	arg_4_0._paintingParticleSystem = arg_4_0._paintingParticles:GetComponent(typeof(ParticleSystem))

	arg_4_0._paintingParticleSystem:Stop(true)

	arg_4_0._paintingFitter = findTF(var_4_0, "hero/fitter")

	removeAllChildren(arg_4_0._paintingFitter)

	local var_4_1 = GetOrAddComponent(arg_4_0._paintingFitter, "PaintingScaler")

	var_4_1.FrameName = "lihuisha"
	var_4_1.Tween = 1

	var_4_0:GetComponent(typeof(DftAniEvent)):SetEndEvent(function(arg_5_0)
		if arg_4_0._currentPainting then
			setActive(arg_4_0._currentPainting, false)

			arg_4_0._currentPainting = nil
		end
	end)
end

function var_0_0.EnableSkillFloat(arg_6_0, arg_6_1)
	if arg_6_1 == arg_6_0._skillFloat then
		return
	end

	arg_6_0._skillFloat = arg_6_1

	if arg_6_0._skillFloat then
		for iter_6_0, iter_6_1 in ipairs(arg_6_0._cacheSkill) do
			arg_6_0:SkillHrzPop(iter_6_1.skillName, iter_6_1.caster, iter_6_1.commander, iter_6_1.hrzIcon)
		end

		arg_6_0._cacheSkill = {}
	else
		arg_6_0._skillFloatPool:AllRecycle()
		arg_6_0._skillFloatCMDPool:AllRecycle()

		arg_6_0._preCommanderSkillTF = nil
		arg_6_0._preSkillTF = nil
	end

	SetActive(arg_6_0.skillTips, arg_6_1)
end

function var_0_0.SkillHrzPop(arg_7_0, arg_7_1, arg_7_2, arg_7_3, arg_7_4)
	if not arg_7_0._skillFloat then
		table.insert(arg_7_0._cacheSkill, {
			skillName = arg_7_1,
			caster = arg_7_2,
			commander = arg_7_3,
			hrzIcon = arg_7_4
		})

		return
	end

	local var_7_0 = ys.Battle.BattleResourceManager.GetInstance()
	local var_7_1
	local var_7_2

	if arg_7_3 then
		if arg_7_0._commanderSkillList[arg_7_3] and arg_7_0._commanderSkillList[arg_7_3][arg_7_1] then
			return
		end

		var_7_1 = arg_7_0._skillFloatCMDPool
		var_7_2 = var_7_0:GetCommanderHrzIcon(arg_7_3)
	else
		var_7_1 = arg_7_0._skillFloatPool

		if arg_7_2:GetUnitType() == ys.Battle.BattleConst.UnitType.PLAYER_UNIT then
			local var_7_3 = arg_7_4 or arg_7_2:GetTemplate().painting

			var_7_2 = var_7_0:GetCharacterIcon(var_7_3)
		else
			var_7_2 = var_7_0:GetCharacterIcon(pg.enemy_data_statistics[arg_7_2:GetTemplateID()].icon)
		end
	end

	local var_7_4 = var_7_1:GetObject()
	local var_7_5 = var_7_4.transform

	var_7_5.localScale = var_0_0.SKILL_FLOAT_SCALE

	setText(findTF(var_7_5, "skill/skill_name/Text"), HXSet.hxLan(arg_7_1))

	local var_7_6 = findTF(var_7_5, "skill/icon")
	local var_7_7 = findTF(var_7_5, "skill/skill_name")

	var_7_6:GetComponent(typeof(Image)).sprite = var_7_2

	local var_7_8, var_7_9 = arg_7_2:GetIFF()

	if arg_7_2:GetIFF() == ys.Battle.BattleConfig.FRIENDLY_CODE then
		var_7_9 = Color.New(1, 1, 1, 1)
	else
		var_7_9 = Color.New(1, 0.33, 0.33, 1)
	end

	var_7_7:GetComponent(typeof(Image)).color = var_7_9
	findTF(var_7_5, "skill"):GetComponent(typeof(Image)).color = var_7_9

	if arg_7_3 then
		arg_7_0:commanderSkillFloat(arg_7_3, arg_7_1, var_7_4)
	else
		local var_7_10 = var_0_1.CameraPosToUICamera(arg_7_2:GetPosition():Clone())
		local var_7_11 = ys.Battle.BattleCameraUtil.GetInstance():GetCharacterArrowBarPosition(var_7_10)
		local var_7_12 = table.contains(TeamType.SubShipType, arg_7_2:GetTemplate().type)
		local var_7_13 = arg_7_2:GetMainUnitIndex()

		if var_7_11 == nil or var_7_11 == nil and var_7_12 and not arg_7_2:IsMainFleetUnit() then
			if var_7_8 == ys.Battle.BattleConfig.FRIENDLY_CODE then
				var_7_10 = var_0_1.CameraPosToUICamera(arg_7_2:GetPosition():Clone():Add(var_0_0.IN_VIEW_FRIEND_SKILL_OFFSET))
			else
				var_7_10 = var_0_1.CameraPosToUICamera(arg_7_2:GetPosition():Clone():Add(var_0_0.IN_VIEW_FOE_SKILL_OFFSET))
			end

			var_7_5.position = Vector3(var_7_10.x, var_7_10.y, -2)

			local var_7_14 = rtf(var_7_5).rect.width * 0.5
			local var_7_15 = var_7_5.anchoredPosition
			local var_7_16 = var_7_15.x

			if Screen.width * 0.5 < var_7_14 + var_7_16 then
				var_7_15.x = var_7_16 - rtf(var_7_5).rect.width
				var_7_5.anchoredPosition = var_7_15
			end

			if arg_7_0._preSkillTF then
				arg_7_0.handleSkillFloatCld(arg_7_0._preSkillTF, var_7_5)
			end

			arg_7_0._preSkillTF = var_7_5

			var_7_5:GetComponent(typeof(DftAniEvent)):SetEndEvent(function(arg_8_0)
				arg_7_0._preSkillTF = nil

				var_7_1:Recycle(var_7_4)
			end)
		else
			local var_7_17
			local var_7_18 = var_0_0.SIDE_ALIGNMENT[var_7_13]
			local var_7_19 = arg_7_0._sideSkillFloatStateList[var_7_8][var_7_13]

			for iter_7_0 = 1, #var_7_19 do
				if var_7_19[iter_7_0] then
					var_7_17 = iter_7_0

					break
				end
			end

			if var_7_17 == nil then
				var_7_17 = #var_7_19 + 1
			end

			var_7_19[var_7_17] = false
			var_7_5.position = var_7_11

			local var_7_20 = var_7_5.anchoredPosition

			var_7_20.y = var_7_18[var_7_17]

			if var_7_8 == ys.Battle.BattleConfig.FOE_CODE then
				var_7_20.x = var_0_0.FOE_SIDE_X_OFFSET
			end

			var_7_5.anchoredPosition = var_7_20

			var_7_5:GetComponent(typeof(DftAniEvent)):SetEndEvent(function(arg_9_0)
				var_7_19[var_7_17] = true

				var_7_1:Recycle(var_7_4)
			end)
		end
	end
end

function var_0_0.SkillHrzPopCover(arg_10_0, arg_10_1, arg_10_2, arg_10_3)
	arg_10_0:SkillHrzPop(arg_10_1, arg_10_2, nil, arg_10_3)
end

function var_0_0.handleSkillFloatCld(arg_11_0, arg_11_1)
	local var_11_0 = arg_11_1.anchoredPosition
	local var_11_1 = arg_11_0.anchoredPosition.y

	if math.floor(math.abs(var_11_0.y - var_11_1)) <= 112.5 then
		var_11_0.y = var_11_1 + 112.5
		arg_11_1.anchoredPosition = var_11_0
	end
end

function var_0_0.handleSkillSinkCld(arg_12_0, arg_12_1)
	return
end

function var_0_0.commanderSkillFloat(arg_13_0, arg_13_1, arg_13_2, arg_13_3)
	arg_13_0._commanderSkillList[arg_13_1] = arg_13_0._commanderSkillList[arg_13_1] or {}
	arg_13_0._commanderSkillList[arg_13_1][arg_13_2] = true

	local var_13_0 = arg_13_3.transform
	local var_13_1 = var_13_0.anchoredPosition

	var_13_1.x = 0
	var_13_1.y = 0
	var_13_0.anchoredPosition = var_13_1

	if arg_13_0._preCommanderSkillTF then
		local var_13_2 = arg_13_0._preCommanderSkillTF.anchoredPosition.y

		if math.floor(math.abs(var_13_1.y - var_13_2)) <= 97.5 then
			var_13_1.y = var_13_2 - 97.5
		end
	end

	var_13_0.anchoredPosition = var_13_1
	arg_13_0._preCommanderSkillTF = var_13_0

	var_13_0:GetComponent(typeof(DftAniEvent)):SetEndEvent(function(arg_14_0)
		arg_13_0._commanderSkillList[arg_13_1][arg_13_2] = nil
		arg_13_0._preCommanderSkillTF = nil

		arg_13_0._skillFloatCMDPool:Recycle(arg_13_3)
	end)
end

function var_0_0.CutInPainting(arg_15_0, arg_15_1, arg_15_2, arg_15_3, arg_15_4)
	if arg_15_0._currentPainting then
		arg_15_0._paintingAnimator.enabled = false

		setActive(arg_15_0._currentPainting, false)
	end

	local var_15_0 = arg_15_4 or arg_15_1.painting or arg_15_1.prefab

	if arg_15_0._skillPaintings[var_15_0] == nil then
		local var_15_1 = ys.Battle.BattleResourceManager.GetInstance():InstPainting(var_15_0)

		arg_15_0._skillPaintings[var_15_0] = var_15_1

		setParent(var_15_1, arg_15_0._paintingFitter, false)
	end

	arg_15_0._currentPainting = arg_15_0._skillPaintings[var_15_0]

	setActive(arg_15_0._currentPainting, true)
	LuaHelper.SetParticleSpeed(arg_15_0._paintingUI, arg_15_2)

	local var_15_2 = Vector3(arg_15_3, 1, 1)

	arg_15_0._paintingUI.transform.localScale = var_15_2
	arg_15_0._paintingParticleContainer.transform.localScale = var_15_2
	arg_15_0._paintingParticles.transform.localEulerAngles = Vector3(0, 90 * arg_15_3, 0)

	arg_15_0._paintingParticleSystem:Play(true)

	arg_15_0._paintingAnimator.speed = arg_15_2
	arg_15_0._paintingAnimator.enabled = true

	arg_15_0._paintingAnimator:Play("skill_painting", -1, 0)
end

function var_0_0.didEnter(arg_16_0)
	setActive(arg_16_0._tf, false)

	arg_16_0._ratioFitter.enabled = true
	arg_16_0._ratioFitter.aspectRatio = pg.CameraFixMgr.GetInstance():GetBattleUIRatio()
	arg_16_0.camEventId = pg.CameraFixMgr.GetInstance():bind(pg.CameraFixMgr.ASPECT_RATIO_UPDATE, function(arg_17_0, arg_17_1)
		arg_16_0._ratioFitter.aspectRatio = pg.CameraFixMgr.GetInstance():GetBattleUIRatio()
	end)

	local var_16_0 = ys.Battle.BattleState.GetInstance()

	var_16_0:SetBattleUI(arg_16_0)
	onButton(arg_16_0, arg_16_0:findTF("PauseBtn"), function()
		arg_16_0:emit(BattleMediator.ON_PAUSE)
	end, SFX_CONFIRM)

	local var_16_1 = arg_16_0:findTF("chatBtn")

	onButton(arg_16_0, var_16_1, function()
		arg_16_0:emit(BattleMediator.ON_CHAT, arg_16_0:findTF("chatContainer"))
		setActive(var_16_1, false)
	end)
	onToggle(arg_16_0, arg_16_0:findTF("AutoBtn"), function(arg_20_0)
		local var_20_0 = var_16_0:GetBattleType()

		arg_16_0:emit(BattleMediator.ON_AUTO, {
			isOn = not arg_20_0,
			toggle = arg_16_0:findTF("AutoBtn"),
			system = var_20_0
		})
		var_16_0:ActiveBot(ys.Battle.BattleState.IsAutoBotActive(var_20_0))
		setActive(var_16_1, var_16_0:ChatUseable())
	end, SFX_PANEL, SFX_PANEL)
	onButton(arg_16_0, arg_16_0:findTF("CardPuzzleConsole/relic/bg"), function()
		local var_21_0 = var_16_0:GetProxyByName(ys.Battle.BattleDataProxy.__name):GetFleetByIFF(ys.Battle.BattleConfig.FRIENDLY_CODE):GetCardPuzzleComponent():GetRelicList()

		arg_16_0:emit(BattleMediator.ON_PUZZLE_RELIC, {
			relicList = var_21_0
		})
	end, SFX_CONFIRM)
	onButton(arg_16_0, arg_16_0:findTF("CardPuzzleConsole/deck/bg"), function()
		local var_22_0 = var_16_0:GetProxyByName(ys.Battle.BattleDataProxy.__name):GetFleetByIFF(ys.Battle.BattleConfig.FRIENDLY_CODE):GetCardPuzzleComponent()
		local var_22_1 = var_22_0:GetDeck():GetCardList()
		local var_22_2 = var_22_0:GetHand():GetCardList()

		arg_16_0:emit(BattleMediator.ON_PUZZLE_CARD, {
			card = var_22_1,
			hand = var_22_2
		})
	end, SFX_CONFIRM)
	var_16_0:ConfigBattleEndFunc(function(arg_23_0)
		arg_16_0:clear()
		arg_16_0:emit(BattleMediator.ON_BATTLE_RESULT, arg_23_0)
	end)

	local var_16_2 = ys.Battle.BattleConst.BuffEffectType
	local var_16_3 = {
		var_16_2.ON_START_GAME,
		var_16_2.ON_FLAG_SHIP,
		var_16_2.ON_CONSORT,
		var_16_2.ON_LEADER,
		var_16_2.ON_REAR,
		var_16_2.ON_SUB_LEADER,
		var_16_2.ON_SUB_CONSORT
	}
	local var_16_4 = 0

	local function var_16_5(arg_24_0)
		local var_24_0 = 0

		for iter_24_0, iter_24_1 in ipairs(arg_24_0) do
			var_24_0 = var_24_0 + ys.Battle.BattleDataFunction.GetShipSkillTriggerCount(iter_24_1, var_16_3)
		end

		return var_24_0
	end

	local var_16_6 = var_16_4 + var_16_5(arg_16_0.contextData.battleData.MainUnitList) + var_16_5(arg_16_0.contextData.battleData.VanguardUnitList) + var_16_5(arg_16_0.contextData.battleData.SubUnitList) + 4

	arg_16_0._skillFloatPool = pg.Pool.New(arg_16_0.skillRoot, arg_16_0.skillTpl, var_16_6, 10, true, false):InitSize()

	arg_16_0:emit(BattleMediator.ENTER)
	arg_16_0:initPauseWindow()

	if arg_16_0.contextData.prePause then
		triggerButton(arg_16_0:findTF("PauseBtn"))
	end

	setActive(var_16_1, var_16_0:ChatUseable())
end

function var_0_0.onBackPressed(arg_25_0)
	if isActive(arg_25_0.pauseWindow) then
		pg.CriMgr.GetInstance():PlaySoundEffect_V3(SFX_CANCEL)
		triggerButton(arg_25_0.continueBtn)
	end
end

function var_0_0.activeBotHelp(arg_26_0, arg_26_1)
	local var_26_0 = getProxy(PlayerProxy)

	if not arg_26_1 then
		if arg_26_0.autoBotHelp then
			pg.MsgboxMgr.GetInstance():hide()
		end

		return
	end

	if var_26_0.botHelp then
		return
	end

	arg_26_0.autoBotHelp = true

	pg.MsgboxMgr.GetInstance():ShowMsgBox({
		type = MSGBOX_TYPE_HELP,
		helps = i18n("help_battle_auto"),
		custom = {
			{
				text = "text_iknow",
				sound = SFX_CANCEL
			}
		},
		onClose = function()
			arg_26_0.autoBotHelp = false
		end
	})

	var_26_0.botHelp = true
end

function var_0_0.exitBattle(arg_28_0, arg_28_1)
	if not arg_28_1 then
		arg_28_0:emit(BattleMediator.ON_QUIT_BATTLE_MANUALLY)
		arg_28_0:emit(BattleMediator.ON_BACK_PRE_SCENE)
	elseif arg_28_1 == "kick" then
		-- block empty
	end
end

function var_0_0.setChapter(arg_29_0, arg_29_1)
	arg_29_0._chapter = arg_29_1
end

function var_0_0.setFleet(arg_30_0, arg_30_1, arg_30_2)
	arg_30_0._mainShipVOs = arg_30_1
	arg_30_0._vanShipVOs = arg_30_2
end

function var_0_0.initPauseWindow(arg_31_0)
	arg_31_0.pauseWindow = arg_31_0:findTF("Msgbox")
	arg_31_0.LeftTimeContainer = arg_31_0:findTF("window/LeftTime", arg_31_0.pauseWindow)
	arg_31_0.LeftTime = arg_31_0:findTF("window/LeftTime/Text", arg_31_0.pauseWindow)
	arg_31_0.mainTFs = {}
	arg_31_0.vanTFs = {}

	local function var_31_0(arg_32_0, arg_32_1, arg_32_2)
		for iter_32_0 = 1, 3 do
			local var_32_0 = arg_32_1:Find("ship_" .. iter_32_0)

			setActive(var_32_0, arg_32_2 and iter_32_0 <= #arg_32_2)

			if arg_32_2 and iter_32_0 <= #arg_32_2 then
				updateShip(var_32_0, arg_32_2[iter_32_0])
			end

			table.insert(arg_32_0 and arg_31_0.mainTFs or arg_31_0.vanTFs, var_32_0)
		end

		if arg_32_2 then
			local var_32_1 = 0

			for iter_32_1, iter_32_2 in ipairs(arg_32_2) do
				var_32_1 = var_32_1 + iter_32_2:getShipCombatPower()
			end

			setText(arg_32_1:Find("power/value"), var_32_1)
		end
	end

	if arg_31_0._mainShipVOs then
		var_31_0(true, arg_31_0:findTF("window/main", arg_31_0.pauseWindow), arg_31_0._mainShipVOs)
		var_31_0(false, arg_31_0:findTF("window/van", arg_31_0.pauseWindow), arg_31_0._vanShipVOs)
	end

	local var_31_1 = ys.Battle.BattleState.GetInstance()
	local var_31_2 = findTF(arg_31_0.pauseWindow, "window/Chapter")
	local var_31_3 = findTF(arg_31_0.pauseWindow, "window/Chapter/Text")

	arg_31_0.continueBtn = arg_31_0:findTF("window/button_container/continue", arg_31_0.pauseWindow)
	arg_31_0.leaveBtn = arg_31_0:findTF("window/button_container/leave", arg_31_0.pauseWindow)

	local var_31_4 = var_31_1:GetBattleType()

	if var_31_4 == SYSTEM_SCENARIO then
		local var_31_5 = arg_31_0._chapter:getConfigTable()

		setText(var_31_2, var_31_5.chapter_name)
		setText(var_31_3, string.split(var_31_5.name, "|")[1])
	elseif var_31_4 == SYSTEM_ROUTINE or var_31_4 == SYSTEM_DUEL or var_31_4 == SYSTEM_HP_SHARE_ACT_BOSS or var_31_4 == SYSTEM_BOSS_EXPERIMENT or var_31_4 == SYSTEM_ACT_BOSS or var_31_4 == SYSTEM_ACT_BOSS_SP or var_31_4 == SYSTEM_BOSS_RUSH or var_31_4 == SYSTEM_BOSS_RUSH_EX or var_31_4 == SYSTEM_LIMIT_CHALLENGE or var_31_4 == SYSTEM_BOSS_SINGLE then
		setText(var_31_2, "SP")

		local var_31_6 = var_31_1:GetProxyByName(ys.Battle.BattleDataProxy.__name):GetInitData().StageTmpId
		local var_31_7 = pg.expedition_data_template[var_31_6]

		setText(var_31_3, var_31_7.name)
	elseif var_31_4 == SYSTEM_DEBUG then
		setText(var_31_2, "??")
		setText(var_31_3, "碧蓝梦境")
	elseif var_31_4 == SYSTEM_CHALLENGE then
		local var_31_8 = arg_31_0._chapter:getNextExpedition()

		setText(var_31_2, "SP")
		setText(var_31_3, var_31_8.chapter_name[2])
		setActive(arg_31_0.LeftTimeContainer, true)
	elseif var_31_4 == SYSTEM_WORLD_BOSS or var_31_4 == SYSTEM_WORLD then
		setText(var_31_2, i18n("world_battle_pause"))
		setText(var_31_3, i18n("world_battle_pause2"))

		if var_31_4 == SYSTEM_WORLD_BOSS then
			setActive(arg_31_0.leaveBtn, false)
		end
	elseif var_31_4 == SYSTEM_GUILD then
		local var_31_9 = var_31_1:GetProxyByName(ys.Battle.BattleDataProxy.__name):GetInitData().ActID
		local var_31_10 = pg.guild_boss_event[var_31_9]

		setText(var_31_2, "BOSS")
		setText(var_31_3, var_31_10 and var_31_10.name or "")
	elseif var_31_4 == SYSTEM_TEST or var_31_4 == SYSTEM_SUB_ROUTINE or var_31_4 == SYSTEM_PERFORM or var_31_4 == SYSTEM_PROLOGUE or var_31_4 == SYSTEM_DODGEM or var_31_4 == SYSTEM_SIMULATION or var_31_4 == SYSTEM_SUBMARINE_RUN or var_31_4 == SYSTEM_BOSS_EXPERIMENT or var_31_4 == SYSTEM_REWARD_PERFORM or var_31_4 == SYSTEM_AIRFIGHT then
		-- block empty
	elseif var_31_4 == SYSTEM_CARDPUZZLE then
		-- block empty
	else
		assert(false, "System not defined " .. (var_31_4 or "NIL"))
	end

	onButton(arg_31_0, arg_31_0.leaveBtn, function()
		arg_31_0:emit(BattleMediator.ON_LEAVE)
	end)
	onButton(arg_31_0, arg_31_0.continueBtn, function()
		setActive(arg_31_0.pauseWindow, false)
		pg.UIMgr.GetInstance():UnblurPanel(arg_31_0.pauseWindow, arg_31_0._tf)
		var_31_1:Resume()
	end)
	onButton(arg_31_0, arg_31_0:findTF("help", arg_31_0.pauseWindow), function()
		if BATTLE_DEBUG and PLATFORM == 7 then
			setActive(arg_31_0.pauseWindow, false)
			pg.UIMgr.GetInstance():UnblurPanel(arg_31_0.pauseWindow, arg_31_0._tf)
			var_31_1:Resume()
			var_31_1:OpenConsole()
		else
			pg.MsgboxMgr.GetInstance():ShowMsgBox({
				type = MSGBOX_TYPE_HELP,
				helps = i18n("help_battle_rule")
			})
		end
	end)
	onButton(arg_31_0, arg_31_0:findTF("window/top/btnBack", arg_31_0.pauseWindow), function()
		triggerButton(arg_31_0.continueBtn)
	end)
	onButton(arg_31_0, arg_31_0.pauseWindow, function()
		triggerButton(arg_31_0.continueBtn)
	end)
	setActive(arg_31_0.pauseWindow, false)
end

function var_0_0.updatePauseWindow(arg_38_0)
	if not arg_38_0.pauseWindow then
		return
	end

	setActive(arg_38_0.pauseWindow, true)
	pg.UIMgr.GetInstance():BlurPanel(arg_38_0.pauseWindow, nil, {
		weight = LayerWeightConst.SECOND_LAYER
	})

	local var_38_0 = ys.Battle.BattleState.GetInstance():GetProxyByName(ys.Battle.BattleDataProxy.__name)
	local var_38_1 = var_38_0:GetFleetByIFF(ys.Battle.BattleConfig.FRIENDLY_CODE)
	local var_38_2 = var_38_1:GetMainList()
	local var_38_3 = var_38_1:GetScoutList()

	local function var_38_4(arg_39_0, arg_39_1, arg_39_2)
		if not arg_39_0 then
			return
		end

		for iter_39_0 = 1, #arg_39_0 do
			local var_39_0 = arg_39_0[iter_39_0].id

			if var_38_1:GetFreezeShipByID(var_39_0) then
				local var_39_1 = var_38_1:GetFreezeShipByID(var_39_0)

				setSlider(arg_39_2[iter_39_0]:Find("blood"), 0, 1, var_39_1:GetHPRate())
				SetActive(arg_39_2[iter_39_0]:Find("mask"), false)
			elseif var_38_1:GetShipByID(var_39_0) then
				local var_39_2 = var_38_1:GetShipByID(var_39_0)

				setSlider(arg_39_2[iter_39_0]:Find("blood"), 0, 1, var_39_2:GetHPRate())
				SetActive(arg_39_2[iter_39_0]:Find("mask"), false)
			else
				setSlider(arg_39_2[iter_39_0]:Find("blood"), 0, 1, 0)
				SetActive(arg_39_2[iter_39_0]:Find("mask"), true)
			end
		end
	end

	var_38_4(arg_38_0._mainShipVOs, var_38_2, arg_38_0.mainTFs)
	var_38_4(arg_38_0._vanShipVOs, var_38_3, arg_38_0.vanTFs)
	setText(arg_38_0.LeftTime, ys.Battle.BattleTimerView.formatTime(math.floor(var_38_0:GetCountDown())))
end

function var_0_0.AddUIFX(arg_40_0, arg_40_1, arg_40_2)
	arg_40_2 = arg_40_2 or 1

	local var_40_0 = arg_40_2 > 0

	arg_40_1 = tf(arg_40_1)

	local var_40_1 = var_40_0 and arg_40_0._fxContainerUpper or arg_40_0._fxContainerBottom

	arg_40_1:SetParent(var_40_1)
	pg.ViewUtils.SetSortingOrder(arg_40_1, arg_40_0._canvasOrder + arg_40_2)
	pg.ViewUtils.SetLayer(arg_40_1, Layer.UI)

	return var_40_1.localScale
end

function var_0_0.OnCloseChat(arg_41_0)
	local var_41_0 = arg_41_0:findTF("chatBtn")

	setActive(var_41_0, ys.Battle.BattleState.GetInstance():IsBotActive())
end

function var_0_0.clear(arg_42_0)
	arg_42_0._preSkillTF = nil
	arg_42_0._preCommanderSkillTF = nil
	arg_42_0._commanderSkillList = nil
	arg_42_0._skillPaintings = nil
	arg_42_0._currentPainting = nil

	Destroy(arg_42_0._paintingUI)
end

function var_0_0.willExit(arg_43_0)
	arg_43_0._skillFloatPool:Dispose()
	arg_43_0._skillFloatCMDPool:Dispose()
	ys.Battle.BattleState.GetInstance():ExitBattle()
	pg.UIMgr.GetInstance():UnblurPanel(arg_43_0.pauseWindow, arg_43_0._tf)
	pg.CameraFixMgr.GetInstance():disconnect(arg_43_0.camEventId)
end

return var_0_0
