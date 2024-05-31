ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig

var_0_0.Battle.BattleSkillView = class("BattleSkillView")

local var_0_2 = var_0_0.Battle.BattleSkillView

var_0_2.__name = "BattleSkillView"

def var_0_2.Ctor(arg_1_0, arg_1_1):
	var_0_0.EventListener.AttachEventListener(arg_1_0)

	arg_1_0._mediator = arg_1_1
	arg_1_0._ui = arg_1_1._ui

	arg_1_0.InitBtns()
	arg_1_0.EnableWeaponButton(False)

def var_0_2.EnableWeaponButton(arg_2_0, arg_2_1):
	for iter_2_0, iter_2_1 in ipairs(arg_2_0._skillBtnList):
		iter_2_1.Enabled(arg_2_1)

def var_0_2.DisableWeapnButton(arg_3_0):
	for iter_3_0, iter_3_1 in ipairs(arg_3_0._skillBtnList):
		iter_3_1.Disable()

def var_0_2.JamSkillButton(arg_4_0, arg_4_1):
	for iter_4_0, iter_4_1 in ipairs(arg_4_0._skillBtnList):
		iter_4_1.SetJam(arg_4_1)

def var_0_2.ShiftSubmarineManualButton(arg_5_0, arg_5_1):
	if arg_5_1 == var_0_0.Battle.OxyState.STATE_FREE_FLOAT:
		arg_5_0._diveBtn.SetActive(True)
		arg_5_0._floatBtn.SetActive(False)
	elif arg_5_1 == var_0_0.Battle.OxyState.STATE_FREE_DIVE:
		arg_5_0._diveBtn.SetActive(False)
		arg_5_0._floatBtn.SetActive(True)

def var_0_2.InitBtns(arg_6_0):
	arg_6_0._skillBtnList = {}
	arg_6_0._activeBtnList = {}
	arg_6_0._delayAnimaList = {}
	arg_6_0._fleetVO = arg_6_0._mediator._dataProxy.GetFleetByIFF(var_0_0.Battle.BattleConfig.FRIENDLY_CODE)
	arg_6_0._buttonContainer = arg_6_0._ui.findTF("Weapon_button_container")
	arg_6_0._buttonRes = arg_6_0._ui.findTF("Weapon_button_Resource")

	local function var_6_0()
		pg.TipsMgr.GetInstance().ShowTips(i18n("battle_emptyBlock"))

	local function var_6_1()
		return

	local function var_6_2()
		if arg_6_0._main_cannon_sound:
			arg_6_0._main_cannon_sound.Stop(True)

		arg_6_0._main_cannon_sound = pg.CriMgr.GetInstance().PlaySE_V3("battle-cannon-main-prepared")

		arg_6_0._fleetVO.CastChargeWeapon()

	local function var_6_3()
		arg_6_0._fleetVO.UnleashChrageWeapon()

	local function var_6_4()
		if arg_6_0._main_cannon_sound:
			arg_6_0._main_cannon_sound.Stop(True)

		arg_6_0._fleetVO.CancelChargeWeapon()

	arg_6_0._chargeBtn = arg_6_0.generateCommonButton(1)

	arg_6_0._chargeBtn.ConfigCallback(var_6_2, var_6_3, var_6_4, var_6_0)

	local var_6_5 = arg_6_0._fleetVO.GetChargeWeaponVO()

	arg_6_0._chargeBtn.SetProgressInfo(var_6_5)

	local function var_6_6()
		arg_6_0._fleetVO.CastTorpedo()

	local function var_6_7()
		arg_6_0._fleetVO.UnleashTorpedo()

	local function var_6_8()
		arg_6_0._fleetVO.CancelTorpedo()

	arg_6_0._torpedoBtn = arg_6_0.generateCommonButton(2)

	arg_6_0._torpedoBtn.ConfigCallback(var_6_6, var_6_7, var_6_8, var_6_0)

	local var_6_9 = arg_6_0._fleetVO.GetTorpedoWeaponVO()

	arg_6_0._torpedoBtn.SetProgressInfo(var_6_9)

	local function var_6_10()
		arg_6_0._fleetVO.UnleashAllInStrike(True)

	arg_6_0._airStrikeBtn = arg_6_0.generateCommonButton(3)

	arg_6_0._airStrikeBtn.ConfigCallback(var_6_1, var_6_10, var_6_1, var_6_0)

	local var_6_11 = arg_6_0._fleetVO.GetAirAssistVO()

	arg_6_0._airStrikeBtn.SetProgressInfo(var_6_11)

	local function var_6_12()
		arg_6_0._fleetVO.ChangeSubmarineState(var_0_0.Battle.OxyState.STATE_FREE_DIVE, True)

	arg_6_0._diveBtn = arg_6_0.generateSubmarineFuncButton(5)

	arg_6_0._diveBtn.ConfigCallback(var_6_1, var_6_12, var_6_1, var_6_0)

	local var_6_13 = arg_6_0._fleetVO.GetSubFreeDiveVO()

	arg_6_0._diveBtn.SetProgressInfo(var_6_13)
	arg_6_0._diveBtn.SetActive(False)

	local function var_6_14()
		arg_6_0._fleetVO.ChangeSubmarineState(var_0_0.Battle.OxyState.STATE_FREE_FLOAT, True)

	arg_6_0._floatBtn = arg_6_0.generateSubmarineFuncButton(6)

	arg_6_0._floatBtn.ConfigCallback(var_6_1, var_6_14, var_6_1, var_6_0)

	local var_6_15 = arg_6_0._fleetVO.GetSubFreeFloatVO()

	arg_6_0._floatBtn.SetProgressInfo(var_6_15)
	arg_6_0._floatBtn.SetActive(False)

	local function var_6_16()
		arg_6_0._fleetVO.SubmarinBoost()

	arg_6_0._boostBtn = arg_6_0.generateSubmarineFuncButton(7)

	arg_6_0._boostBtn.ConfigCallback(var_6_1, var_6_16, var_6_1, var_6_0)

	local var_6_17 = arg_6_0._fleetVO.GetSubBoostVO()

	arg_6_0._boostBtn.SetProgressInfo(var_6_17)

	local function var_6_18()
		arg_6_0._fleetVO.UnleashSubmarineSpecial()

	arg_6_0._specialBtn = arg_6_0.generateSubmarineButton(9)

	arg_6_0._specialBtn.ConfigCallback(var_6_1, var_6_18, var_6_1, var_6_0)

	local var_6_19 = arg_6_0._fleetVO.GetSubSpecialVO()

	arg_6_0._specialBtn.SetProgressInfo(var_6_19)

	local function var_6_20()
		arg_6_0._fleetVO.ShiftManualSub()

	arg_6_0._shiftBtn = arg_6_0.generateSubmarineFuncButton(8)

	arg_6_0._shiftBtn.ConfigCallback(var_6_1, var_6_20, var_6_1, var_6_0)

	local var_6_21 = arg_6_0._fleetVO.GetSubShiftVO()

	arg_6_0._shiftBtn.SetProgressInfo(var_6_21)

	local var_6_22 = arg_6_0._fleetVO._submarineVO

	if var_6_22.GetUseable() and var_6_22.GetCount() > 0:
		local function var_6_23()
			arg_6_0._mediator._dataProxy.SubmarineStrike(var_0_0.Battle.BattleConfig.FRIENDLY_CODE)

		arg_6_0._subStriveBtn = arg_6_0.generateSubmarineButton(4)

		local var_6_24 = arg_6_0._subStriveBtn.GetSkin()

		arg_6_0.setSkillButtonPreferences(var_6_24, 4)
		arg_6_0._subStriveBtn.ConfigCallback(var_6_1, var_6_23, var_6_1, var_6_0)
		arg_6_0._subStriveBtn.SetProgressInfo(var_6_22)
		table.insert(arg_6_0._activeBtnList, arg_6_0._subStriveBtn)

	local var_6_25 = var_0_0.Battle.BattleWeaponButton.New()
	local var_6_26 = cloneTplTo(arg_6_0._progressSkin, arg_6_0._buttonContainer)

	arg_6_0.setSkillButtonPreferences(var_6_26, 2)
	var_6_25.ConfigSkin(var_6_26)
	var_6_25.SwitchIcon(10)
	var_6_25.SwitchIconEffect(2)
	var_6_25.ConfigCallback(var_6_6, var_6_7, var_6_8, var_6_0)
	table.insert(arg_6_0._skillBtnList, var_6_25)
	var_6_25.SetProgressInfo(var_6_9)
	var_6_25.SetActive(False)
	arg_6_0._boostBtn.SetActive(False)
	arg_6_0._diveBtn.SetActive(False)
	arg_6_0._floatBtn.SetActive(False)
	arg_6_0._specialBtn.SetActive(False)
	arg_6_0._shiftBtn.SetActive(False)

def var_0_2.generateCommonButton(arg_22_0, arg_22_1):
	local var_22_0 = var_0_0.Battle.BattleWeaponButton.New()

	arg_22_0._progressSkin = arg_22_0._progressSkin or arg_22_0._ui.findTF("Weapon_button_progress")

	local var_22_1 = cloneTplTo(arg_22_0._progressSkin, arg_22_0._buttonContainer)

	var_22_1.name = "Skill_" .. arg_22_1

	arg_22_0.setSkillButtonPreferences(var_22_1, arg_22_1)
	var_22_0.ConfigSkin(var_22_1)
	var_22_0.SwitchIcon(arg_22_1)
	var_22_0.SwitchIconEffect(arg_22_1)
	var_22_0.SetTextActive(True)
	table.insert(arg_22_0._skillBtnList, var_22_0)

	return var_22_0

def var_0_2.generateSubmarineFuncButton(arg_23_0, arg_23_1):
	local var_23_0 = var_0_0.Battle.BattleSubmarineFuncButton.New()

	arg_23_0._progressSkin = arg_23_0._progressSkin or arg_23_0._ui.findTF("Weapon_button_progress")

	local var_23_1 = cloneTplTo(arg_23_0._progressSkin, arg_23_0._buttonContainer)

	var_23_0.ConfigSkin(var_23_1)
	var_23_0.SwitchIcon(arg_23_1)
	var_23_0.SetTextActive(False)
	table.insert(arg_23_0._skillBtnList, var_23_0)

	return var_23_0

def var_0_2.generateSubmarineButton(arg_24_0, arg_24_1):
	local var_24_0 = var_0_0.Battle.BattleSubmarineButton.New()

	arg_24_0._disposableSkin = arg_24_0._disposableSkin or arg_24_0._ui.findTF("Weapon_button")

	local var_24_1 = cloneTplTo(arg_24_0._disposableSkin, arg_24_0._buttonContainer)

	var_24_0.ConfigSkin(var_24_1)
	var_24_0.SwitchIcon(arg_24_1)
	table.insert(arg_24_0._skillBtnList, var_24_0)

	return var_24_0

def var_0_2.CustomButton(arg_25_0, arg_25_1):
	for iter_25_0, iter_25_1 in ipairs(arg_25_1):
		arg_25_0._skillBtnList[iter_25_1].SetActive(False)

def var_0_2.NormalButton(arg_26_0):
	arg_26_0._chargeBtn.SetActive(True)
	arg_26_0._torpedoBtn.SetActive(True)
	arg_26_0._airStrikeBtn.SetActive(True)
	arg_26_0._boostBtn.SetActive(False)
	arg_26_0._diveBtn.SetActive(False)
	arg_26_0._floatBtn.SetActive(False)
	arg_26_0._specialBtn.SetActive(False)
	arg_26_0._shiftBtn.SetActive(False)
	table.insert(arg_26_0._activeBtnList, arg_26_0._chargeBtn)
	table.insert(arg_26_0._activeBtnList, arg_26_0._torpedoBtn)
	table.insert(arg_26_0._activeBtnList, arg_26_0._airStrikeBtn)
	table.insert(arg_26_0._delayAnimaList, arg_26_0._chargeBtn)
	table.insert(arg_26_0._delayAnimaList, arg_26_0._torpedoBtn)
	table.insert(arg_26_0._delayAnimaList, arg_26_0._airStrikeBtn)

	if arg_26_0._subStriveBtn:
		table.insert(arg_26_0._delayAnimaList, arg_26_0._subStriveBtn)

def var_0_2.SubmarineButton(arg_27_0):
	arg_27_0._chargeBtn.SetActive(False)
	arg_27_0._torpedoBtn.SetActive(True)
	arg_27_0._airStrikeBtn.SetActive(False)
	arg_27_0._boostBtn.SetActive(True)
	arg_27_0._diveBtn.SetActive(True)
	arg_27_0._floatBtn.SetActive(True)
	table.insert(arg_27_0._activeBtnList, arg_27_0._diveBtn)
	table.insert(arg_27_0._activeBtnList, arg_27_0._torpedoBtn)
	table.insert(arg_27_0._activeBtnList, arg_27_0._boostBtn)
	table.insert(arg_27_0._activeBtnList, arg_27_0._floatBtn)
	table.insert(arg_27_0._delayAnimaList, arg_27_0._floatBtn)
	table.insert(arg_27_0._delayAnimaList, arg_27_0._torpedoBtn)
	table.insert(arg_27_0._delayAnimaList, arg_27_0._boostBtn)

	local var_27_0 = arg_27_0._torpedoBtn.GetSkin().transform
	local var_27_1 = var_0_1.SKILL_BUTTON_DEFAULT_PREFERENCE[2]

	var_27_0.anchorMin = Vector2(var_27_1.x, var_27_1.y)
	var_27_0.anchorMax = Vector2(var_27_1.x, var_27_1.y)

def var_0_2.SubRoutineButton(arg_28_0):
	arg_28_0._chargeBtn.SetActive(False)
	arg_28_0._torpedoBtn.SetActive(True)
	arg_28_0._airStrikeBtn.SetActive(False)
	arg_28_0._boostBtn.SetActive(False)
	arg_28_0._diveBtn.SetActive(True)
	arg_28_0._floatBtn.SetActive(True)
	arg_28_0._specialBtn.SetActive(True)
	arg_28_0._shiftBtn.SetActive(True)
	table.insert(arg_28_0._activeBtnList, arg_28_0._diveBtn)
	table.insert(arg_28_0._activeBtnList, arg_28_0._torpedoBtn)
	table.insert(arg_28_0._activeBtnList, arg_28_0._specialBtn)
	table.insert(arg_28_0._activeBtnList, arg_28_0._floatBtn)
	table.insert(arg_28_0._activeBtnList, arg_28_0._shiftBtn)
	table.insert(arg_28_0._delayAnimaList, arg_28_0._floatBtn)
	table.insert(arg_28_0._delayAnimaList, arg_28_0._torpedoBtn)
	table.insert(arg_28_0._delayAnimaList, arg_28_0._shiftBtn)
	table.insert(arg_28_0._delayAnimaList, arg_28_0._specialBtn)
	arg_28_0.setSkillButtonPreferences(arg_28_0._diveBtn.GetSkin(), 1)
	arg_28_0.setSkillButtonPreferences(arg_28_0._floatBtn.GetSkin(), 1)
	arg_28_0.setSkillButtonPreferences(arg_28_0._torpedoBtn.GetSkin(), 2)
	arg_28_0.setSkillButtonPreferences(arg_28_0._shiftBtn.GetSkin(), 3)
	arg_28_0.setSkillButtonPreferences(arg_28_0._specialBtn.GetSkin(), 4)

def var_0_2.AirFightButton(arg_29_0):
	local var_29_0 = {
		9
	}

	for iter_29_0, iter_29_1 in ipairs(arg_29_0._skillBtnList):
		local var_29_1 = table.indexof(var_29_0, iter_29_0)

		iter_29_1.SetActive(var_29_1)

		if var_29_1:
			table.insert(arg_29_0._activeBtnList, iter_29_1)
			arg_29_0.setSkillButtonPreferences(iter_29_1.GetSkin(), var_29_1)

def var_0_2.ButtonInitialAnima(arg_30_0):
	for iter_30_0, iter_30_1 in ipairs(arg_30_0._delayAnimaList):
		iter_30_1.InitialAnima(iter_30_0 * 0.2)

def var_0_2.CardPuzzleButton(arg_31_0):
	arg_31_0._chargeBtn.SetActive(False)
	arg_31_0._torpedoBtn.SetActive(False)
	arg_31_0._airStrikeBtn.SetActive(False)
	arg_31_0._boostBtn.SetActive(False)
	arg_31_0._diveBtn.SetActive(False)
	arg_31_0._floatBtn.SetActive(False)
	arg_31_0._specialBtn.SetActive(False)
	arg_31_0._shiftBtn.SetActive(False)

def var_0_2.HideSkillButton(arg_32_0, arg_32_1):
	for iter_32_0, iter_32_1 in ipairs(arg_32_0._activeBtnList):
		iter_32_1.SetActive(not arg_32_1)

def var_0_2.OnSkillCd(arg_33_0, arg_33_1):
	local var_33_0 = arg_33_1.Data.skillID
	local var_33_1 = arg_33_1.Data.coolDownTime

	if var_33_1 < pg.TimeMgr.GetInstance().GetCombatTime():
		return

	arg_33_0._skillCd[var_33_0] = var_33_1

def var_0_2.Dispose(arg_34_0):
	arg_34_0._delayAnimaList = None
	arg_34_0._activeBtnList = None

	for iter_34_0, iter_34_1 in ipairs(arg_34_0._skillBtnList):
		iter_34_1.Dispose()

	arg_34_0._ui = None

	if arg_34_0._main_cannon_sound:
		arg_34_0._main_cannon_sound.Stop(True)

		arg_34_0._main_cannon_sound = None

	var_0_0.EventListener.DetachEventListener(arg_34_0)

def var_0_2.Update(arg_35_0):
	for iter_35_0, iter_35_1 in ipairs(arg_35_0._skillBtnList):
		iter_35_1.Update()

def var_0_2.setSkillButtonPreferences(arg_36_0, arg_36_1, arg_36_2):
	local var_36_0 = var_0_1.SKILL_BUTTON_DEFAULT_PREFERENCE[arg_36_2]
	local var_36_1 = PlayerPrefs.GetFloat("skill_" .. arg_36_2 .. "_scale", var_36_0.scale)
	local var_36_2 = PlayerPrefs.GetFloat("skill_" .. arg_36_2 .. "_anchorX", var_36_0.x)
	local var_36_3 = PlayerPrefs.GetFloat("skill_" .. arg_36_2 .. "_anchorY", var_36_0.y)
	local var_36_4 = arg_36_1.transform

	var_36_4.localScale = Vector3(var_36_1, var_36_1, 0)
	var_36_4.anchorMin = Vector2(var_36_2, var_36_3)
	var_36_4.anchorMax = Vector2(var_36_2, var_36_3)
