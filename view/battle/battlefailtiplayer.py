local var_0_0 = class("BattleFailTipLayer", import("..base.BaseUI"))

var_0_0.PowerUpBtn = {
	ShipBreakUp = 4,
	SkillLevelUp = 3,
	ShipLevelUp = 1,
	EquipLevelUp = 2
}

def var_0_0.getUIName(arg_1_0):
	return "BattleFailTipUI"

def var_0_0.init(arg_2_0):
	arg_2_0.initData()
	arg_2_0.findUI()
	arg_2_0.addListener()

def var_0_0.initData(arg_3_0):
	arg_3_0.battleSystem = arg_3_0.contextData.battleSystem

def var_0_0.findUI(arg_4_0):
	arg_4_0.powerUpTipPanel = arg_4_0.findTF("Main")
	arg_4_0.shipLevelUpBtn = arg_4_0.findTF("ShipLevelUpBtn", arg_4_0.powerUpTipPanel)
	arg_4_0.equipLevelUpBtn = arg_4_0.findTF("EquipLevelUpBtn", arg_4_0.powerUpTipPanel)
	arg_4_0.skillLevelUpBtn = arg_4_0.findTF("SkillLevelUpBtn", arg_4_0.powerUpTipPanel)
	arg_4_0.shipBreakUpBtn = arg_4_0.findTF("ShipBreakUpBtn", arg_4_0.powerUpTipPanel)
	arg_4_0.closeBtn = arg_4_0.findTF("CloseBtn", arg_4_0.powerUpTipPanel)

def var_0_0.addListener(arg_5_0):
	onButton(arg_5_0, arg_5_0.closeBtn, function()
		arg_5_0.closeView(), SFX_CANCEL)
	onButton(arg_5_0, arg_5_0.shipLevelUpBtn, function()
		if arg_5_0.battleSystem == SYSTEM_SCENARIO:
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("fightfail_up"),
				def onYes:()
					if arg_5_0.contextData.battleSystem == SYSTEM_SCENARIO:
						arg_5_0.lastClickBtn = var_0_0.PowerUpBtn.ShipLevelUp

						arg_5_0.emit(BattleFailTipMediator.CHAPTER_RETREAT)
					else
						arg_5_0.emit(BattleFailTipMediator.GO_HIGEST_CHAPTER)
			})
		else
			arg_5_0.emit(BattleFailTipMediator.GO_HIGEST_CHAPTER), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.equipLevelUpBtn, function()
		if arg_5_0.battleSystem == SYSTEM_SCENARIO:
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("fightfail_equip"),
				def onYes:()
					if arg_5_0.contextData.battleSystem == SYSTEM_SCENARIO:
						arg_5_0.lastClickBtn = var_0_0.PowerUpBtn.EquipLevelUp

						arg_5_0.emit(BattleFailTipMediator.CHAPTER_RETREAT)
					else
						arg_5_0.emit(BattleFailTipMediator.GO_DOCKYARD_EQUIP)
			})
		else
			arg_5_0.emit(BattleFailTipMediator.GO_DOCKYARD_EQUIP), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.skillLevelUpBtn, function()
		arg_5_0.emit(BattleFailTipMediator.GO_NAVALTACTICS), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.shipBreakUpBtn, function()
		if arg_5_0.battleSystem == SYSTEM_SCENARIO:
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("fight_strengthen"),
				def onYes:()
					if arg_5_0.contextData.battleSystem == SYSTEM_SCENARIO:
						arg_5_0.lastClickBtn = var_0_0.PowerUpBtn.ShipBreakUp

						arg_5_0.emit(BattleFailTipMediator.CHAPTER_RETREAT)
					else
						arg_5_0.emit(BattleFailTipMediator.GO_DOCKYARD_SHIP)
			})
		else
			arg_5_0.emit(BattleFailTipMediator.GO_DOCKYARD_SHIP), SFX_PANEL)

def var_0_0.didEnter(arg_14_0):
	pg.UIMgr.GetInstance().BlurPanel(arg_14_0._tf)
	arg_14_0.aniBeforeEnter()

def var_0_0.onBackPressed(arg_15_0):
	arg_15_0.closeView()

def var_0_0.willExit(arg_16_0):
	LeanTween.cancel(go(arg_16_0._tf))
	pg.UIMgr.GetInstance().UnblurPanel(arg_16_0._tf)

def var_0_0.aniBeforeEnter(arg_17_0):
	local var_17_0 = GetComponent(arg_17_0._tf, "CanvasGroup")

	LeanTween.value(go(arg_17_0._tf), 0, 1, 0.6).setOnUpdate(System.Action_float(function(arg_18_0)
		var_17_0.alpha = arg_18_0))

return var_0_0
