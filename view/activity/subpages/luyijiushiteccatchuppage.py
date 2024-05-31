local var_0_0 = class("LuyijiushiTecCatchupPage", import("...base.BaseActivityPage"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.bg = arg_1_0.findTF("AD")
	arg_1_0.itemTF = arg_1_0.findTF("Award", arg_1_0.bg)
	arg_1_0.sliderTF = arg_1_0.findTF("Slider", arg_1_0.bg)
	arg_1_0.progressText = arg_1_0.findTF("Progress", arg_1_0.bg)
	arg_1_0.goBtn = arg_1_0.findTF("GoBtn", arg_1_0.bg)
	arg_1_0.finishBtn = arg_1_0.findTF("FinishBtn", arg_1_0.bg)

def var_0_0.OnDataSetting(arg_2_0):
	arg_2_0.curCount = arg_2_0.activity.data1

	local var_2_0 = arg_2_0.activity.getConfig("config_id")

	arg_2_0.maxCount = pg.activity_event_blueprint_catchup[var_2_0].obtain_max
	arg_2_0.itemID = arg_2_0.activity.getConfig("config_client").itemid

def var_0_0.OnFirstFlush(arg_3_0):
	local var_3_0 = {
		count = 1,
		type = DROP_TYPE_ITEM,
		id = arg_3_0.itemID
	}

	updateDrop(arg_3_0.itemTF, var_3_0)
	onButton(arg_3_0, arg_3_0.itemTF, function()
		arg_3_0.emit(BaseUI.ON_DROP, var_3_0), SFX_PANEL)
	setSlider(arg_3_0.sliderTF, 0, arg_3_0.maxCount, arg_3_0.curCount)
	setText(arg_3_0.progressText, arg_3_0.curCount .. "/" .. arg_3_0.maxCount)
	onButton(arg_3_0, arg_3_0.goBtn, function()
		arg_3_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.TECHNOLOGY), SFX_PANEL)

def var_0_0.OnUpdateFlush(arg_6_0):
	local var_6_0 = arg_6_0.curCount >= arg_6_0.maxCount

	setActive(arg_6_0.goBtn, not var_6_0)
	setActive(arg_6_0.finishBtn, var_6_0)

def var_0_0.OnDestroy(arg_7_0):
	return

return var_0_0
