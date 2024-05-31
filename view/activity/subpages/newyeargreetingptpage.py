local var_0_0 = class("NewYearGreetingPtPage", import(".TemplatePage.PtTemplatePage"))

def var_0_0.OnInit(arg_1_0):
	var_0_0.super.OnInit(arg_1_0)

	arg_1_0.awardGotTag = arg_1_0.findTF("award_got", arg_1_0.bg)

def var_0_0.OnFirstFlush(arg_2_0):
	var_0_0.super.OnFirstFlush(arg_2_0)
	onButton(arg_2_0, arg_2_0.battleBtn, function()
		arg_2_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.TASK, {
			page = "activity"
		}), SFX_PANEL)

def var_0_0.OnUpdateFlush(arg_4_0):
	var_0_0.super.OnUpdateFlush(arg_4_0)
	setActive(arg_4_0.awardGotTag, not arg_4_0.ptData.CanGetNextAward())

return var_0_0
