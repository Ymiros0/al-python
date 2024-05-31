ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleWeaponButton")

var_0_0.Battle.BattleWeaponButton = var_0_1
var_0_1.__name = "BattleWeaponButton"
var_0_1.ICON_BY_INDEX = {
	"cannon",
	"torpedo",
	"aircraft",
	"submarine",
	"dive",
	"rise",
	"boost",
	"switch",
	"special",
	"aamissile",
	"meteor"
}

def var_0_1.Ctor(arg_1_0):
	var_0_0.EventListener.AttachEventListener(arg_1_0)

	arg_1_0.eventTriggers = {}

def var_0_1.ConfigCallback(arg_2_0, arg_2_1, arg_2_2, arg_2_3, arg_2_4):
	arg_2_0._downFunc = arg_2_1
	arg_2_0._upFunc = arg_2_2
	arg_2_0._cancelFunc = arg_2_3
	arg_2_0._emptyFunc = arg_2_4

def var_0_1.SetActive(arg_3_0, arg_3_1):
	SetActive(arg_3_0._skin, arg_3_1)

def var_0_1.SetJam(arg_4_0, arg_4_1):
	SetActive(arg_4_0._jam, arg_4_1)
	SetActive(arg_4_0._icon, not arg_4_1)
	SetActive(arg_4_0._progress, not arg_4_1)

def var_0_1.SwitchIcon(arg_5_0, arg_5_1):
	arg_5_0._iconIndex = arg_5_1

	local var_5_0 = var_0_1.ICON_BY_INDEX[arg_5_1]

	setImageSprite(arg_5_0._unfill, LoadSprite("ui/CombatUI_atlas", "weapon_unfill_" .. var_5_0))
	setImageSprite(arg_5_0._filled, LoadSprite("ui/CombatUI_atlas", "filled_combined_" .. var_5_0))

def var_0_1.SwitchIconEffect(arg_6_0, arg_6_1):
	local var_6_0 = var_0_1.ICON_BY_INDEX[arg_6_1]

	setImageSprite(arg_6_0._filledEffect, LoadSprite("ui/CombatUI_atlas", "filled_effect_" .. var_6_0), True)
	setImageSprite(arg_6_0._jam, LoadSprite("ui/CombatUI_atlas", "skill_jam_" .. var_6_0), True)

def var_0_1.ConfigSkin(arg_7_0, arg_7_1):
	arg_7_0._skin = arg_7_1
	arg_7_0._btn = arg_7_1.Find("ActCtl")
	arg_7_0._block = arg_7_1.Find("ActCtl/block").gameObject
	arg_7_0._progress = arg_7_1.Find("ActCtl/skill_progress")
	arg_7_0._progressBar = arg_7_0._progress.GetComponent(typeof(Image))
	arg_7_0._icon = arg_7_1.Find("ActCtl/skill_icon")
	arg_7_0._filled = arg_7_0._icon.Find("filled")
	arg_7_0._unfill = arg_7_0._icon.Find("unfill")
	arg_7_0._count = arg_7_1.Find("ActCtl/Count")
	arg_7_0._text = arg_7_0._count.Find("CountText")
	arg_7_0._selected = arg_7_1.Find("ActCtl/selected")
	arg_7_0._unSelect = arg_7_1.Find("ActCtl/unselect")
	arg_7_0._filledEffect = arg_7_1.Find("ActCtl/filledEffect")
	arg_7_0._jam = arg_7_1.Find("ActCtl/jam")
	arg_7_0._countTxt = arg_7_0._text.GetComponent(typeof(Text))

	arg_7_1.gameObject.SetActive(True)
	arg_7_0._block.SetActive(False)
	arg_7_0._progress.gameObject.SetActive(True)

	local var_7_0 = arg_7_0._filledEffect.gameObject

	var_7_0.SetActive(False)
	var_7_0.GetComponent("DftAniEvent").SetEndEvent(function(arg_8_0)
		SetActive(arg_7_0._filledEffect, False))

def var_0_1.GetSkin(arg_9_0):
	return arg_9_0._skin

def var_0_1.Enabled(arg_10_0, arg_10_1):
	local var_10_0 = GetComponent(arg_10_0._btn, "EventTriggerListener")
	local var_10_1 = GetComponent(arg_10_0._block, "EventTriggerListener")

	arg_10_0.eventTriggers[var_10_0] = True
	arg_10_0.eventTriggers[var_10_1] = True
	var_10_0.enabled = arg_10_1
	var_10_1.enabled = arg_10_1

def var_0_1.Disable(arg_11_0):
	if arg_11_0._cancelFunc:
		arg_11_0._cancelFunc()

	arg_11_0.OnUnSelect()

	local var_11_0 = GetComponent(arg_11_0._btn, "EventTriggerListener")
	local var_11_1 = GetComponent(arg_11_0._block, "EventTriggerListener")

	var_11_0.enabled = False
	var_11_1.enabled = False

def var_0_1.OnSelected(arg_12_0):
	SetActive(arg_12_0._unSelect, False)
	SetActive(arg_12_0._selected, True)

def var_0_1.OnUnSelect(arg_13_0):
	SetActive(arg_13_0._selected, False)
	SetActive(arg_13_0._unSelect, True)

def var_0_1.OnFilled(arg_14_0):
	SetActive(arg_14_0._filled, True)
	SetActive(arg_14_0._unfill, False)

def var_0_1.OnfilledEffect(arg_15_0):
	SetActive(arg_15_0._filledEffect, True)

def var_0_1.OnOverLoadChange(arg_16_0):
	if arg_16_0._progressInfo.IsOverLoad():
		arg_16_0._block.SetActive(True)
		arg_16_0.OnUnfill()
	else
		arg_16_0._block.SetActive(False)
		arg_16_0.OnFilled()

	if arg_16_0._progressInfo.GetTotal() > 0:
		arg_16_0.updateProgressBar()

def var_0_1.OnUnfill(arg_17_0):
	SetActive(arg_17_0._filled, False)
	SetActive(arg_17_0._unfill, True)

def var_0_1.SetProgressActive(arg_18_0, arg_18_1):
	arg_18_0._progress.gameObject.SetActive(arg_18_1)

def var_0_1.SetTextActive(arg_19_0, arg_19_1):
	SetActive(arg_19_0._count, arg_19_1)

def var_0_1.SetProgressInfo(arg_20_0, arg_20_1):
	arg_20_0._progressInfo = arg_20_1

	arg_20_0._progressInfo.RegisterEventListener(arg_20_0, var_0_0.Battle.BattleEvent.WEAPON_TOTAL_CHANGE, arg_20_0.OnTotalChange)
	arg_20_0._progressInfo.RegisterEventListener(arg_20_0, var_0_0.Battle.BattleEvent.WEAPON_COUNT_PLUS, arg_20_0.OnfilledEffect)
	arg_20_0._progressInfo.RegisterEventListener(arg_20_0, var_0_0.Battle.BattleEvent.OVER_LOAD_CHANGE, arg_20_0.OnOverLoadChange)
	arg_20_0._progressInfo.RegisterEventListener(arg_20_0, var_0_0.Battle.BattleEvent.COUNT_CHANGE, arg_20_0.OnCountChange)
	arg_20_0.OnTotalChange()
	arg_20_0.OnOverLoadChange()

def var_0_1.OnCountChange(arg_21_0):
	local var_21_0 = arg_21_0._progressInfo.GetCount()
	local var_21_1 = arg_21_0._progressInfo.GetTotal()

	arg_21_0._countTxt.text = string.format("%d/%d", var_21_0, var_21_1)

	local var_21_2 = arg_21_0._progressInfo.GetCurrentWeaponIconIndex()

	if var_21_2 != arg_21_0._iconIndex:
		arg_21_0.SwitchIcon(var_21_2)
		arg_21_0.SwitchIconEffect(var_21_2)

def var_0_1.OnTotalChange(arg_22_0, arg_22_1):
	if arg_22_0._progressInfo.GetTotal() <= 0:
		arg_22_0._block.SetActive(True)

		arg_22_0._progressBar.fillAmount = 0
		arg_22_0._text.GetComponent(typeof(Text)).text = "0/0"

		arg_22_0.SetControllerActive(False)
		arg_22_0.OnUnfill()
		arg_22_0.OnUnSelect()
	else
		arg_22_0.OnCountChange()
		arg_22_0.SetControllerActive(True)

		if arg_22_1:
			local var_22_0 = arg_22_1.Data.index

			if var_22_0 and var_22_0 == 1:
				arg_22_0.OnUnSelect()

def var_0_1.SetControllerActive(arg_23_0, arg_23_1):
	if arg_23_0._isActive == arg_23_1:
		return

	arg_23_0._isActive = arg_23_1

	local var_23_0 = GetComponent(arg_23_0._btn, "EventTriggerListener")
	local var_23_1 = GetComponent(arg_23_0._block, "EventTriggerListener")

	if arg_23_1:
		local var_23_2

		if arg_23_0._downFunc != None:
			var_23_0.AddPointDownFunc(function()
				var_23_2 = True

				arg_23_0._downFunc()
				arg_23_0.OnSelected())

		if arg_23_0._upFunc != None:
			var_23_0.AddPointUpFunc(function()
				if var_23_2:
					var_23_2 = False

					arg_23_0._upFunc()
					arg_23_0.OnUnSelect())

		if arg_23_0._cancelFunc != None:
			var_23_0.AddPointExitFunc(function()
				if var_23_2:
					var_23_2 = False

					arg_23_0._cancelFunc()
					arg_23_0.OnUnSelect())

		var_23_1.RemovePointDownFunc()
	else
		var_23_1.AddPointDownFunc(arg_23_0._emptyFunc)
		var_23_0.RemovePointDownFunc()
		var_23_0.RemovePointUpFunc()
		var_23_0.RemovePointExitFunc()

def var_0_1.InitialAnima(arg_27_0, arg_27_1):
	SetActive(arg_27_0._btn, False)

	arg_27_0._leanID = LeanTween.delayedCall(arg_27_1, System.Action(function()
		arg_27_0._skin.GetComponent("Animator").enabled = True
		arg_27_0._leanID = None))

def var_0_1.Update(arg_29_0):
	local var_29_0 = arg_29_0._progressInfo.GetCurrent()
	local var_29_1 = arg_29_0._progressInfo.GetMax()

	if arg_29_0._progressInfo.GetTotal() > 0 and var_29_0 < var_29_1:
		arg_29_0.updateProgressBar()

def var_0_1.updateProgressBar(arg_30_0):
	local var_30_0 = arg_30_0._progressInfo.GetCurrent() / arg_30_0._progressInfo.GetMax()

	arg_30_0._progressBar.fillAmount = var_30_0

def var_0_1.Dispose(arg_31_0):
	if arg_31_0.eventTriggers:
		for iter_31_0, iter_31_1 in pairs(arg_31_0.eventTriggers):
			ClearEventTrigger(iter_31_0)

		arg_31_0.eventTriggers = None

	arg_31_0._progress = None
	arg_31_0._progressBar = None

	arg_31_0._progressInfo.UnregisterEventListener(arg_31_0, var_0_0.Battle.BattleEvent.OVER_LOAD_CHANGE)
	arg_31_0._progressInfo.UnregisterEventListener(arg_31_0, var_0_0.Battle.BattleEvent.WEAPON_TOTAL_CHANGE)
	arg_31_0._progressInfo.UnregisterEventListener(arg_31_0, var_0_0.Battle.BattleEvent.WEAPON_COUNT_PLUS)
	arg_31_0._progressInfo.UnregisterEventListener(arg_31_0, var_0_0.Battle.BattleEvent.COUNT_CHANGE)
	var_0_0.EventListener.DetachEventListener(arg_31_0)
