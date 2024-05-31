local var_0_0 = class("OtherWorldMainPage", import(".TemplatePage.PreviewTemplatePage"))
local var_0_1 = 0.45
local var_0_2 = 0.2
local var_0_3 = 1.2

def var_0_0.OnInit(arg_1_0):
	var_0_0.super.OnInit(arg_1_0)

	arg_1_0.effectBlankScreen = arg_1_0.findTF("blank_screen_effect", arg_1_0.bg)
	arg_1_0.effectOpen = arg_1_0.findTF("open_effect", arg_1_0.bg)
	arg_1_0.effectBlink = arg_1_0.findTF("blink_effect", arg_1_0.bg)
	arg_1_0.effectClick = arg_1_0.findTF("click_effect", arg_1_0.bg)

def var_0_0.OnFirstFlush(arg_2_0):
	arg_2_0.skinshopBtn = arg_2_0.findTF("skinshop", arg_2_0.btnList)

	onButton(arg_2_0, arg_2_0.skinshopBtn, function()
		arg_2_0.PlayClickEffect(arg_2_0.skinshopBtn, function()
			pg.m02.sendNotification(GAME.GO_SCENE, SCENE.SKINSHOP)), SFX_PANEL)

	arg_2_0.mountainBtn = arg_2_0.findTF("mountain", arg_2_0.btnList)

	onButton(arg_2_0, arg_2_0.mountainBtn, function()
		arg_2_0.PlayClickEffect(arg_2_0.mountainBtn, function()
			pg.m02.sendNotification(GAME.GO_SCENE, SCENE.OTHERWORLD_BACKHILL)), SFX_PANEL)

	arg_2_0.buildBtn = arg_2_0.findTF("build", arg_2_0.btnList)

	onButton(arg_2_0, arg_2_0.buildBtn, function()
		arg_2_0.PlayClickEffect(arg_2_0.buildBtn, function()
			arg_2_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.GETBOAT, {
				projectName = BuildShipScene.PROJECTS.ACTIVITY
			})), SFX_PANEL)

	arg_2_0.fightBtn = arg_2_0.findTF("fight", arg_2_0.btnList)

	onButton(arg_2_0, arg_2_0.fightBtn, function()
		arg_2_0.PlayClickEffect(arg_2_0.fightBtn, function()
			pg.m02.sendNotification(GAME.GO_SCENE, SCENE.OTHERWORLD_MAP)), SFX_PANEL)
	arg_2_0.PlayOpenEffect()

def var_0_0.PlayOpenEffect(arg_11_0):
	setActive(arg_11_0.effectBlankScreen, True)
	setActive(arg_11_0.effectOpen, False)
	arg_11_0.managedTween(LeanTween.delayedCall, function()
		setActive(arg_11_0.effectOpen, True), var_0_2, None)
	arg_11_0.managedTween(LeanTween.delayedCall, function()
		setActive(arg_11_0.effectBlankScreen, False), var_0_1, None)
	arg_11_0.managedTween(LeanTween.delayedCall, function()
		setActive(arg_11_0.effectOpen, False)
		setActive(arg_11_0.effectBlink, True), var_0_2 + var_0_3, None)

def var_0_0.PlayClickEffect(arg_15_0, arg_15_1, arg_15_2):
	local var_15_0 = pg.UIMgr.GetInstance().OverlayEffect.GetChild(0)
	local var_15_1 = Vector3(192, 60, 0)
	local var_15_2 = var_15_0 and var_15_0.localPosition.Sub(var_15_1) or arg_15_1.localPosition

	setLocalPosition(arg_15_0.effectClick, var_15_2)
	setActive(arg_15_0.effectClick, True)
	arg_15_0.managedTween(LeanTween.delayedCall, function()
		setActive(arg_15_0.effectClick, False)

		if arg_15_2:
			arg_15_2(), 0.3, None)

def var_0_0.OnDestroy(arg_17_0):
	arg_17_0.cleanManagedTween()

return var_0_0
