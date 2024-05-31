local var_0_0 = class("MainLiveAreaOldPage", import("view.base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "MainLiveAreaOldUI"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0._academyBtn = arg_2_0.findTF("school_btn")
	arg_2_0._haremBtn = arg_2_0.findTF("backyard_btn")
	arg_2_0._commanderBtn = arg_2_0.findTF("commander_btn")

	pg.redDotHelper.AddNode(RedDotNode.New(arg_2_0._haremBtn.Find("tip"), {
		pg.RedDotMgr.TYPES.COURTYARD
	}))
	pg.redDotHelper.AddNode(SelfRefreshRedDotNode.New(arg_2_0._academyBtn.Find("tip"), {
		pg.RedDotMgr.TYPES.SCHOOL
	}))
	pg.redDotHelper.AddNode(SelfRefreshRedDotNode.New(arg_2_0._commanderBtn.Find("tip"), {
		pg.RedDotMgr.TYPES.COMMANDER
	}))

def var_0_0.OnInit(arg_3_0):
	onButton(arg_3_0, arg_3_0._commanderBtn, function()
		arg_3_0.emit(NewMainMediator.GO_SCENE, SCENE.COMMANDERCAT, {
			fromMain = True,
			fleetType = CommanderCatScene.FLEET_TYPE_COMMON
		})
		arg_3_0.Hide(), SFX_MAIN)
	onButton(arg_3_0, arg_3_0._haremBtn, function()
		arg_3_0.emit(NewMainMediator.GO_SCENE, SCENE.COURTYARD)
		arg_3_0.Hide(), SFX_MAIN)
	onButton(arg_3_0, arg_3_0._academyBtn, function()
		arg_3_0.emit(NewMainMediator.GO_SCENE, SCENE.NAVALACADEMYSCENE)
		arg_3_0.Hide(), SFX_MAIN)
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0.Hide(), SFX_PANEL)

def var_0_0.Show(arg_8_0):
	var_0_0.super.Show(arg_8_0)
	pg.UIMgr.GetInstance().BlurPanel(arg_8_0._tf, True, {
		weight = LayerWeightConst.SECOND_LAYER
	})

	local var_8_0 = getProxy(PlayerProxy).getRawData()

	if not pg.SystemOpenMgr.GetInstance().isOpenSystem(var_8_0.level, "CommanderCatMediator"):
		arg_8_0._commanderBtn.GetComponent(typeof(Image)).color = Color(0.3, 0.3, 0.3, 1)
	else
		arg_8_0._commanderBtn.GetComponent(typeof(Image)).color = Color(1, 1, 1, 1)

	if not pg.SystemOpenMgr.GetInstance().isOpenSystem(var_8_0.level, "CourtYardMediator"):
		arg_8_0._haremBtn.GetComponent(typeof(Image)).color = Color(0.3, 0.3, 0.3, 1)
	else
		arg_8_0._haremBtn.GetComponent(typeof(Image)).color = Color(1, 1, 1, 1)

def var_0_0.Hide(arg_9_0):
	if arg_9_0.isShowing():
		var_0_0.super.Hide(arg_9_0)
		pg.UIMgr.GetInstance().UnblurPanel(arg_9_0._tf, arg_9_0._parentTf)

def var_0_0.OnDestroy(arg_10_0):
	arg_10_0.Hide()

return var_0_0
