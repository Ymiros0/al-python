local var_0_0 = class("MonopolyPtPage", import("...base.BaseActivityPage"))

def var_0_0.OnInit(arg_1_0):
	onToggle(arg_1_0, findTF(arg_1_0._tf, "AD/toggle/1"), function()
		arg_1_0.changeToggle(1), SFX_CONFIRM)
	onToggle(arg_1_0, findTF(arg_1_0._tf, "AD/toggle/2"), function()
		arg_1_0.changeToggle(2), SFX_CONFIRM)
	onToggle(arg_1_0, findTF(arg_1_0._tf, "AD/toggle/3"), function()
		arg_1_0.changeToggle(3), SFX_CONFIRM)
	triggerToggle(findTF(arg_1_0._tf, "AD/toggle/1"), True)
	onButton(arg_1_0, findTF(arg_1_0._tf, "AD/btnShop"), function()
		arg_1_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.SHOP), SFX_CONFIRM)
	onButton(arg_1_0, findTF(arg_1_0._tf, "AD/btnGo"), function()
		arg_1_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.MONOPOLY_PT, {
			config_id = arg_1_0.activity.id
		}), SFX_CONFIRM)

def var_0_0.changeToggle(arg_7_0, arg_7_1):
	for iter_7_0 = 1, 3:
		setActive(findTF(arg_7_0._tf, "AD/toggle/" .. iter_7_0 .. "/on/desc"), iter_7_0 == arg_7_1)

def var_0_0.OnFirstFlush(arg_8_0):
	if arg_8_0.ptData:
		arg_8_0.ptData.Update(arg_8_0.activity)
	else
		arg_8_0.ptData = ActivityPtData.New(arg_8_0.activity)

def var_0_0.OnUpdateFlush(arg_9_0):
	if arg_9_0.ptData:
		arg_9_0.ptData.Update(arg_9_0.activity)
	else
		arg_9_0.ptData = ActivityPtData.New(arg_9_0.activity)

	local var_9_0, var_9_1, var_9_2 = arg_9_0.ptData.GetLevelProgress()
	local var_9_3, var_9_4, var_9_5 = arg_9_0.ptData.GetResProgress()
	local var_9_6 = arg_9_0.ptData.GetLevel()
	local var_9_7 = 20 - var_9_6
	local var_9_8 = math.floor(var_9_3 / 500) - var_9_6

	if var_9_7 < var_9_8:
		var_9_8 = var_9_7

	if var_9_7 == 0:
		setActive(findTF(arg_9_0._tf, "AD/clear"), True)
	else
		setActive(findTF(arg_9_0._tf, "AD/clear"), False)

	setActive(findTF(arg_9_0._tf, "AD/count"), var_9_8 > 0)
	setText(findTF(arg_9_0._tf, "AD/count/txt"), var_9_8)

return var_0_0
