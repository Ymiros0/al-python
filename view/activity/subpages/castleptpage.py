local var_0_0 = class("CastlePtPage", import(".TemplatePage.PtTemplatePage"))

var_0_0.MAIN_ID = ActivityConst.CASTLE_ACT_ID

def var_0_0.OnFirstFlush(arg_1_0):
	var_0_0.super.OnFirstFlush(arg_1_0)
	onButton(arg_1_0, arg_1_0.findTF("main_btn", arg_1_0.bg), function()
		arg_1_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.CASTLE_MAIN), SFX_PANEL)

def var_0_0.OnUpdateFlush(arg_3_0):
	var_0_0.super.OnUpdateFlush(arg_3_0)

	arg_3_0.mainAct = getProxy(ActivityProxy).getActivityById(var_0_0.MAIN_ID)

	local var_3_0 = arg_3_0.mainAct.data2
	local var_3_1 = arg_3_0.mainAct.data1

	if table.contains({
		4565,
		4568,
		4571,
		4574,
		4577,
		4580,
		4583,
		4586
	}, var_3_1) and not pg.NewStoryMgr.GetInstance().IsPlayed(pg.NewStoryMgr.GetInstance().StoryId2StoryName(var_3_1)):
		var_3_0 = var_3_0 - 1

	setText(arg_3_0.findTF("main_btn/Text", arg_3_0.bg), i18n("roll_times_left", var_3_0))
	setText(arg_3_0.findTF("description", arg_3_0.bg), i18n("activity_kill"))

return var_0_0
