local var_0_0 = class("CommanderHomeLevelCard")
local var_0_1 = "#9A9898"
local var_0_2 = "#a59897"
local var_0_3 = "#6a5a5a"

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._go = arg_1_1
	arg_1_0._tf = arg_1_1.transform
	arg_1_0.view = arg_1_2
	arg_1_0.mask = findTF(arg_1_0._tf, "mask").GetComponent(typeof(RectMask2D))
	arg_1_0.progress = findTF(arg_1_0._tf, "mask/progress/bar")
	arg_1_0.unlockTF = findTF(arg_1_0._tf, "unlock")
	arg_1_0.doingTF = findTF(arg_1_0._tf, "doing")
	arg_1_0.lockTF = findTF(arg_1_0._tf, "lock")
	arg_1_0.levelTxt = findTF(arg_1_0._tf, "level").GetComponent(typeof(Text))
	arg_1_0.descUnLockIcon = findTF(arg_1_0._tf, "desc/icon_pass")
	arg_1_0.descDoingIcon = findTF(arg_1_0._tf, "desc/icon_doing")
	arg_1_0.descTxt = findTF(arg_1_0._tf, "desc/Text").GetComponent(typeof(Text))
	arg_1_0.expTxt = findTF(arg_1_0._tf, "exp").GetComponent(typeof(Text))

def var_0_0.Update(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0.Clear()

	arg_2_0.home = arg_2_1
	arg_2_0.config = arg_2_2

	local var_2_0 = arg_2_2.level

	arg_2_0.mask.enabled = arg_2_2.tail == True

	setActive(arg_2_0.unlockTF, False)
	setActive(arg_2_0.doingTF, False)
	setActive(arg_2_0.lockTF, False)
	setActive(arg_2_0.descUnLockIcon, False)
	setActive(arg_2_0.descDoingIcon, False)

	local var_2_1

	if arg_2_1.level + 1 == arg_2_2.level:
		arg_2_0.UpdateDoingState()

		var_2_1 = var_0_3
	elif arg_2_1.level < arg_2_2.level:
		arg_2_0.UpdateLockState()

		var_2_1 = var_0_1
	elif arg_2_1.level >= arg_2_2.level:
		arg_2_0.UpdateUnlockState()

		var_2_1 = var_0_2

	arg_2_0.levelTxt.text = setColorStr("LV." .. arg_2_2.level, var_2_1)
	arg_2_0.descTxt.text = setColorStr(shortenString(arg_2_2.desc, 12), var_2_1)
	arg_2_0.expTxt.text = setColorStr(arg_2_2.totalExp, var_2_1)

def var_0_0.UpdateLockState(arg_3_0):
	setFillAmount(arg_3_0.progress, 0)
	setActive(arg_3_0.lockTF, True)
	onButton(None, arg_3_0.lockTF, function()
		arg_3_0.ShowDesc(), SFX_PANEL)

def var_0_0.UpdateDoingState(arg_5_0):
	local var_5_0 = pg.commander_home[arg_5_0.config.level - 1]
	local var_5_1 = 0

	if var_5_0:
		var_5_1 = var_5_0.home_exp

	setFillAmount(arg_5_0.progress, arg_5_0.home.exp / var_5_1)
	setActive(arg_5_0.doingTF, True)
	setActive(arg_5_0.descDoingIcon, True)
	onButton(None, arg_5_0.doingTF, function()
		arg_5_0.ShowDesc(), SFX_PANEL)

def var_0_0.UpdateUnlockState(arg_7_0):
	setFillAmount(arg_7_0.progress, 1)
	setActive(arg_7_0.unlockTF, True)
	setActive(arg_7_0.descUnLockIcon, True)
	onButton(None, arg_7_0.unlockTF, function()
		arg_7_0.ShowDesc(), SFX_PANEL)

def var_0_0.ShowDesc(arg_9_0):
	arg_9_0.view.ShowDescWindow(arg_9_0.config.desc, arg_9_0.config.level)

def var_0_0.Clear(arg_10_0):
	removeOnButton(arg_10_0.lockTF)
	removeOnButton(arg_10_0.doingTF)
	removeOnButton(arg_10_0.unlockTF)

def var_0_0.Dispose(arg_11_0):
	arg_11_0.Clear()

return var_0_0
