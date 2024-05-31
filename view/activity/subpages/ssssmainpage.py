local var_0_0 = class("SSSSMainPage", import(".TemplatePage.PreviewTemplatePage"))
local var_0_1 = 0.45
local var_0_2 = 0.2
local var_0_3 = 1.2
local var_0_4 = "event./ui/kaiji"

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
			pg.m02.sendNotification(GAME.GO_SCENE, SCENE.SSSS_ACADEMY)), SFX_PANEL)

	arg_2_0.buildBtn = arg_2_0.findTF("build", arg_2_0.btnList)

	onButton(arg_2_0, arg_2_0.buildBtn, function()
		arg_2_0.PlayClickEffect(arg_2_0.buildBtn, function()
			arg_2_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.GETBOAT, {
				projectName = BuildShipScene.PROJECTS.ACTIVITY
			})), SFX_PANEL)

	arg_2_0.shopBtn = arg_2_0.findTF("shop", arg_2_0.btnList)

	onButton(arg_2_0, arg_2_0.shopBtn, function()
		arg_2_0.PlayClickEffect(arg_2_0.shopBtn, function()
			local var_10_0 = _.detect(getProxy(ActivityProxy).getActivitiesByType(ActivityConst.ACTIVITY_TYPE_SHOP), function(arg_11_0)
				return arg_11_0.getConfig("config_client").pt_id == pg.gameset.activity_res_id.key_value)

			arg_2_0.emit(ActivityMediator.GO_SHOPS_LAYER, {
				warp = NewShopsScene.TYPE_ACTIVITY,
				actId = var_10_0 and var_10_0.id
			})), SFX_PANEL)

	arg_2_0.fightBtn = arg_2_0.findTF("fight", arg_2_0.btnList)

	onButton(arg_2_0, arg_2_0.fightBtn, function()
		arg_2_0.PlayClickEffect(arg_2_0.fightBtn, function()
			arg_2_0.emit(ActivityMediator.BATTLE_OPERA)), SFX_PANEL)
	arg_2_0.PlayOpenEffect()

def var_0_0.PlayOpenEffect(arg_14_0):
	setActive(arg_14_0.effectBlankScreen, True)
	setActive(arg_14_0.effectOpen, False)
	arg_14_0.managedTween(LeanTween.delayedCall, function()
		setActive(arg_14_0.effectOpen, True)
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_4), var_0_2, None)
	arg_14_0.managedTween(LeanTween.delayedCall, function()
		setActive(arg_14_0.effectBlankScreen, False), var_0_1, None)
	arg_14_0.managedTween(LeanTween.delayedCall, function()
		setActive(arg_14_0.effectOpen, False)
		setActive(arg_14_0.effectBlink, True), var_0_2 + var_0_3, None)

def var_0_0.PlayClickEffect(arg_18_0, arg_18_1, arg_18_2):
	local var_18_0 = pg.UIMgr.GetInstance().OverlayEffect.GetChild(0)
	local var_18_1 = Vector3(192, 60, 0)
	local var_18_2 = var_18_0 and var_18_0.localPosition.Sub(var_18_1) or arg_18_1.localPosition

	setLocalPosition(arg_18_0.effectClick, var_18_2)
	setActive(arg_18_0.effectClick, True)
	arg_18_0.managedTween(LeanTween.delayedCall, function()
		setActive(arg_18_0.effectClick, False)

		if arg_18_2:
			arg_18_2(), 0.3, None)

def var_0_0.OnDestroy(arg_20_0):
	arg_20_0.cleanManagedTween()

return var_0_0
