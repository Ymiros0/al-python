local var_0_0 = class("SettingsBattlePage", import("...base.BaseSubView"))
local var_0_1 = "joystick_anchorX"
local var_0_2 = "joystick_anchorY"
local var_0_3 = "skill_1_anchorX"
local var_0_4 = "skill_1_anchorY"
local var_0_5 = "skill_2_anchorX"
local var_0_6 = "skill_2_anchorY"
local var_0_7 = "skill_3_anchorX"
local var_0_8 = "skill_3_anchorY"
local var_0_9 = "skill_4_anchorX"
local var_0_10 = "skill_4_anchorY"

var_0_0.CLD_RED = Color.New(0.6, 0.05, 0.05, 0.5)
var_0_0.DEFAULT_GREY = Color.New(0.5, 0.5, 0.5, 0.5)

def var_0_0.getUIName(arg_1_0):
	return "SettingsBattlePage"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.editPanel = arg_2_0._tf.Find("editor")

	local var_2_0 = findTF(arg_2_0._tf, "editor/buttons")

	arg_2_0.normalBtns = findTF(var_2_0, "normal")
	arg_2_0.editBtns = findTF(var_2_0, "editing")
	arg_2_0.saveBtn = findTF(arg_2_0.editBtns, "save")
	arg_2_0.cancelBtn = findTF(arg_2_0.editBtns, "cancel")
	arg_2_0.editBtn = findTF(arg_2_0.normalBtns, "edit")
	arg_2_0.revertBtn = findTF(arg_2_0.normalBtns, "reset")
	arg_2_0.interface = findTF(arg_2_0._tf, "editor/editing_region")
	arg_2_0.stick = findTF(arg_2_0.interface, "Stick")
	arg_2_0.skillBtn1 = findTF(arg_2_0.interface, "Skill_1")
	arg_2_0.skillBtn2 = findTF(arg_2_0.interface, "Skill_2")
	arg_2_0.skillBtn3 = findTF(arg_2_0.interface, "Skill_3")
	arg_2_0.skillBtn4 = findTF(arg_2_0.interface, "Skill_4")
	arg_2_0.eventStick = arg_2_0.stick.GetComponent("EventTriggerListener")
	arg_2_0.eventSkillBtn1 = arg_2_0.skillBtn1.GetComponent("EventTriggerListener")
	arg_2_0.eventSkillBtn2 = arg_2_0.skillBtn2.GetComponent("EventTriggerListener")
	arg_2_0.eventSkillBtn3 = arg_2_0.skillBtn3.GetComponent("EventTriggerListener")
	arg_2_0.eventSkillBtn4 = arg_2_0.skillBtn4.GetComponent("EventTriggerListener")
	arg_2_0.mask = findTF(arg_2_0.interface, "mask")
	arg_2_0.topArea = findTF(arg_2_0.interface, "top")
	arg_2_0.cg = arg_2_0._tf.GetComponent(typeof(CanvasGroup))
	arg_2_0.topLayerCg = arg_2_0._parentTf.parent.Find("blur_panel").GetComponent(typeof(CanvasGroup))

	setActive(arg_2_0._tf, True)
	setText(arg_2_0._tf.Find("editor/editing_region/mask/middle/Text"), i18n("settings_battle_tip"))
	setText(arg_2_0._tf.Find("editor/buttons/normal/edit/Image"), i18n("settings_battle_Btn_edit"))
	setText(arg_2_0._tf.Find("editor/buttons/normal/reset/Image"), i18n("settings_battle_Btn_reset"))
	setText(arg_2_0._tf.Find("editor/title"), i18n("settings_battle_title"))
	setText(arg_2_0._tf.Find("editor/buttons/editing/save/Image"), i18n("settings_battle_Btn_save"))
	setText(arg_2_0._tf.Find("editor/buttons/editing/cancel/Image"), i18n("settings_battle_Btn_cancel"))

def var_0_0.OnInit(arg_3_0):
	onButton(arg_3_0, arg_3_0.editBtn, function()
		arg_3_0.EditModeEnabled(True), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.revertBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			hideNo = False,
			content = i18n("setting_interface_revert_check"),
			def onYes:()
				arg_3_0.RevertInterfaceSetting(True)
		}), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.cancelBtn, function()
		if arg_3_0._currentDrag:
			LuaHelper.triggerEndDrag(arg_3_0._currentDrag)

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			hideNo = False,
			content = i18n("setting_interface_cancel_check"),
			def onYes:()
				arg_3_0.EditModeEnabled(False)
				arg_3_0.RevertInterfaceSetting(False)
		}), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.saveBtn, function()
		if arg_3_0._currentDrag:
			LuaHelper.triggerEndDrag(arg_3_0._currentDrag)

		arg_3_0.EditModeEnabled(False)
		arg_3_0.SaveInterfaceSetting()
		pg.TipsMgr.GetInstance().ShowTips(i18n("setting_interface_save_success")), SFX_PANEL)
	arg_3_0.InitInterfaceComponents()

def var_0_0.InitInterfaceComponents(arg_10_0):
	local var_10_0 = ys.Battle.BattleConfig.JOY_STICK_DEFAULT_PREFERENCE

	arg_10_0.InitInterfaceComponent(arg_10_0.stick, arg_10_0.eventStick, var_0_1, var_0_2, var_10_0)

	local var_10_1 = ys.Battle.BattleConfig.SKILL_BUTTON_DEFAULT_PREFERENCE

	arg_10_0.InitInterfaceComponent(arg_10_0.skillBtn1, arg_10_0.eventSkillBtn1, var_0_3, var_0_4, var_10_1[1])
	arg_10_0.InitInterfaceComponent(arg_10_0.skillBtn2, arg_10_0.eventSkillBtn2, var_0_5, var_0_6, var_10_1[2])
	arg_10_0.InitInterfaceComponent(arg_10_0.skillBtn3, arg_10_0.eventSkillBtn3, var_0_7, var_0_8, var_10_1[3])
	arg_10_0.InitInterfaceComponent(arg_10_0.skillBtn4, arg_10_0.eventSkillBtn4, var_0_9, var_0_10, var_10_1[4])

	local var_10_2 = arg_10_0.GetScale()

	arg_10_0.components = {
		arg_10_0.topArea,
		arg_10_0.stick,
		arg_10_0.skillBtn1,
		arg_10_0.skillBtn2,
		arg_10_0.skillBtn3,
		arg_10_0.skillBtn4
	}

	for iter_10_0 = 2, #arg_10_0.components:
		setLocalScale(arg_10_0.components[iter_10_0], var_10_2)

	arg_10_0.EditModeEnabled(False)

def var_0_0.GetScale(arg_11_0):
	local var_11_0 = rtf(arg_11_0.interface).rect.width
	local var_11_1 = rtf(arg_11_0.interface).rect.height
	local var_11_2 = rtf(arg_11_0._parentTf).rect.width
	local var_11_3 = rtf(arg_11_0._parentTf).rect.height
	local var_11_4

	if var_11_0 / var_11_1 > var_11_2 / var_11_3:
		var_11_4 = var_11_1 / var_11_3
	else
		var_11_4 = var_11_0 / var_11_2

	return Vector3.New(var_11_4, var_11_4, 1)

def var_0_0.InitInterfaceComponent(arg_12_0, arg_12_1, arg_12_2, arg_12_3, arg_12_4, arg_12_5):
	local var_12_0 = rtf(arg_12_0._parentTf).rect.width
	local var_12_1 = rtf(arg_12_0._parentTf).rect.height
	local var_12_2 = var_12_0 * 0.5 + arg_12_0.interface.localPosition.x + arg_12_0.interface.parent.localPosition.x + arg_12_0.interface.parent.parent.localPosition.x
	local var_12_3 = var_12_1 * 0.5 + arg_12_0.interface.localPosition.y + arg_12_0.interface.parent.localPosition.y + arg_12_0.interface.parent.parent.localPosition.y
	local var_12_4
	local var_12_5
	local var_12_6
	local var_12_7

	arg_12_2.AddBeginDragFunc(function(arg_13_0, arg_13_1)
		arg_12_0._currentDrag = arg_12_2
		var_12_6 = var_12_0 / UnityEngine.Screen.width
		var_12_7 = var_12_1 / UnityEngine.Screen.height
		var_12_4 = arg_12_1.localPosition.x
		var_12_5 = arg_12_1.localPosition.y)
	arg_12_2.AddDragFunc(function(arg_14_0, arg_14_1)
		arg_12_1.localPosition = Vector3(arg_14_1.position.x * var_12_6 - var_12_2, arg_14_1.position.y * var_12_7 - var_12_3, 0)

		arg_12_0.CheckInterfaceIntersect())
	arg_12_2.AddDragEndFunc(function(arg_15_0, arg_15_1)
		arg_12_0._currentDrag = None

		if arg_12_0.CheckInterfaceIntersect():
			arg_12_1.localPosition = Vector3(var_12_4, var_12_5, 0)

		arg_12_0.CheckInterfaceIntersect())
	arg_12_0.SetInterfaceAnchor(arg_12_1, arg_12_3, arg_12_4, arg_12_5)

def var_0_0.EditModeEnabled(arg_16_0, arg_16_1):
	setActive(arg_16_0.normalBtns, not arg_16_1)
	setActive(arg_16_0.mask, not arg_16_1)
	setActive(arg_16_0.editBtns, arg_16_1)

	for iter_16_0, iter_16_1 in ipairs(arg_16_0.components):
		setActive(findTF(iter_16_1, "rect"), arg_16_1)

		if iter_16_0 > 1:
			GetOrAddComponent(iter_16_1, "EventTriggerListener").enabled = arg_16_1

	Input.multiTouchEnabled = not arg_16_1
	arg_16_0.topLayerCg.blocksRaycasts = not arg_16_1

def var_0_0.SetInterfaceAnchor(arg_17_0, arg_17_1, arg_17_2, arg_17_3, arg_17_4, arg_17_5):
	local var_17_0
	local var_17_1

	if arg_17_5:
		var_17_0 = arg_17_4.x
		var_17_1 = arg_17_4.y
	else
		var_17_0 = PlayerPrefs.GetFloat(arg_17_2, arg_17_4.x)
		var_17_1 = PlayerPrefs.GetFloat(arg_17_3, arg_17_4.y)

	local var_17_2 = rtf(arg_17_0.interface).rect.width
	local var_17_3 = rtf(arg_17_0.interface).rect.height
	local var_17_4 = (var_17_0 - 0.5) * var_17_2
	local var_17_5 = (var_17_1 - 0.5) * var_17_3

	arg_17_1.localPosition = Vector3(var_17_4, var_17_5, 0)

local function var_0_11(arg_18_0)
	local var_18_0 = rtf(arg_18_0)
	local var_18_1 = var_18_0.rect
	local var_18_2 = var_18_1.width * var_18_0.lossyScale.x
	local var_18_3 = var_18_1.height * var_18_0.lossyScale.y
	local var_18_4 = var_18_0.position

	return UnityEngine.Rect.New(var_18_4.x - var_18_2 / 2, var_18_4.y - var_18_3 / 2, var_18_2, var_18_3)

def var_0_0.CheckInterfaceIntersect(arg_19_0):
	local var_19_0 = {}
	local var_19_1 = False
	local var_19_2 = {}
	local var_19_3 = var_0_11(arg_19_0.interface)

	for iter_19_0, iter_19_1 in ipairs(arg_19_0.components):
		var_19_2[iter_19_1] = var_0_11(iter_19_1.Find("rect"))

	for iter_19_2, iter_19_3 in ipairs(arg_19_0.components):
		for iter_19_4, iter_19_5 in ipairs(arg_19_0.components):
			if iter_19_3 != iter_19_5 and var_19_2[iter_19_3].Overlaps(var_19_2[iter_19_5]):
				var_19_0[iter_19_5] = True

		if iter_19_2 > 1:
			local var_19_4 = Vector2.New(var_19_2[iter_19_3].xMin, var_19_2[iter_19_3].yMin)
			local var_19_5 = Vector2.New(var_19_2[iter_19_3].xMax, var_19_2[iter_19_3].yMax)

			if not var_19_3.Contains(var_19_4) or not var_19_3.Contains(var_19_5):
				var_19_0[iter_19_3] = True

	for iter_19_6, iter_19_7 in ipairs(arg_19_0.components):
		local var_19_6 = findTF(iter_19_7, "rect").GetComponent(typeof(Image))

		if var_19_0[iter_19_7]:
			var_19_6.color = var_0_0.CLD_RED
			var_19_1 = True
		else
			var_19_6.color = var_0_0.DEFAULT_GREY

	return var_19_1

def var_0_0.RevertInterfaceSetting(arg_20_0, arg_20_1):
	local var_20_0 = ys.Battle.BattleConfig.JOY_STICK_DEFAULT_PREFERENCE
	local var_20_1 = ys.Battle.BattleConfig.SKILL_BUTTON_DEFAULT_PREFERENCE

	arg_20_0.SetInterfaceAnchor(arg_20_0.stick, var_0_1, var_0_2, var_20_0, arg_20_1)
	arg_20_0.SetInterfaceAnchor(arg_20_0.skillBtn1, var_0_3, var_0_4, var_20_1[1], arg_20_1)
	arg_20_0.SetInterfaceAnchor(arg_20_0.skillBtn2, var_0_5, var_0_6, var_20_1[2], arg_20_1)
	arg_20_0.SetInterfaceAnchor(arg_20_0.skillBtn3, var_0_7, var_0_8, var_20_1[3], arg_20_1)
	arg_20_0.SetInterfaceAnchor(arg_20_0.skillBtn4, var_0_9, var_0_10, var_20_1[4], arg_20_1)
	arg_20_0.SaveInterfaceSetting()

def var_0_0.SaveInterfaceSetting(arg_21_0):
	arg_21_0.OverrideInterfaceSetting(arg_21_0.stick, var_0_1, var_0_2)
	arg_21_0.OverrideInterfaceSetting(arg_21_0.skillBtn1, var_0_3, var_0_4)
	arg_21_0.OverrideInterfaceSetting(arg_21_0.skillBtn2, var_0_5, var_0_6)
	arg_21_0.OverrideInterfaceSetting(arg_21_0.skillBtn3, var_0_7, var_0_8)
	arg_21_0.OverrideInterfaceSetting(arg_21_0.skillBtn4, var_0_9, var_0_10)

def var_0_0.OverrideInterfaceSetting(arg_22_0, arg_22_1, arg_22_2, arg_22_3):
	local var_22_0 = rtf(arg_22_0.interface).rect.width
	local var_22_1 = rtf(arg_22_0.interface).rect.height
	local var_22_2 = (arg_22_1.localPosition.x + var_22_0 * 0.5) / var_22_0
	local var_22_3 = (arg_22_1.localPosition.y + var_22_1 * 0.5) / var_22_1

	PlayerPrefs.SetFloat(arg_22_2, var_22_2)
	PlayerPrefs.SetFloat(arg_22_3, var_22_3)

def var_0_0.OnDestroy(arg_23_0):
	ClearEventTrigger(arg_23_0.eventStick)
	ClearEventTrigger(arg_23_0.eventSkillBtn1)
	ClearEventTrigger(arg_23_0.eventSkillBtn2)
	ClearEventTrigger(arg_23_0.eventSkillBtn3)
	ClearEventTrigger(arg_23_0.eventSkillBtn4)

	Input.multiTouchEnabled = True

def var_0_0.Show(arg_24_0):
	arg_24_0.cg.blocksRaycasts = True
	arg_24_0.cg.alpha = 1

def var_0_0.Hide(arg_25_0):
	arg_25_0.cg.blocksRaycasts = False
	arg_25_0.cg.alpha = 0

return var_0_0
