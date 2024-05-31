local var_0_0 = class("EquipmentTransformInfoLayer", import("view.base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "EquipmentTransformInfoUI"

def var_0_0.init(arg_2_0):
	arg_2_0.loader = AutoLoader.New()

def var_0_0.didEnter(arg_3_0):
	assert(arg_3_0.contextData.equipVO, "Not Pass EquipVO")

	local var_3_0 = arg_3_0._tf.Find("Main").Find("item")
	local var_3_1 = {
		type = DROP_TYPE_EQUIP,
		id = arg_3_0.contextData.equipVO.id
	}

	updateDrop(var_3_0, var_3_1)
	onButton(arg_3_0, var_3_0, function()
		arg_3_0.emit(var_0_0.ON_DROP, var_3_1), SFX_PANEL)

	local var_3_2

	pg.UIMgr.GetInstance().BlurPanel(arg_3_0._tf)
	arg_3_0.loader.GetPrefab("ui/equipupgradeAni", "", function(arg_5_0)
		setParent(arg_5_0, arg_3_0._tf)
		setActive(arg_5_0, True)

		local var_5_0 = arg_5_0.GetComponent(typeof(DftAniEvent))

		var_5_0.SetTriggerEvent(function(arg_6_0)
			var_3_2 = True)
		var_5_0.SetEndEvent(function(arg_7_0)
			arg_3_0.closeView())

		function arg_3_0.unloadEffect()
			var_5_0.SetTriggerEvent(None)
			var_5_0.SetEndEvent(None))
	onButton(arg_3_0, arg_3_0._tf, function()
		if var_3_2:
			arg_3_0.closeView())

def var_0_0.willExit(arg_10_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_10_0._tf)

	if arg_10_0.unloadEffect:
		arg_10_0.unloadEffect()

	arg_10_0.loader.Clear()

return var_0_0
