local var_0_0 = class("DeXiQianShaoRePtPage", import(".TemplatePage.NewFrameTemplatePage"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.bg = arg_1_0.findTF("AD")
	arg_1_0.battleBtn = arg_1_0.findTF("battle_btn", arg_1_0.bg)
	arg_1_0.getBtn = arg_1_0.findTF("get_btn", arg_1_0.bg)
	arg_1_0.gotBtn = arg_1_0.findTF("got_btn", arg_1_0.bg)
	arg_1_0.switchBtn = arg_1_0.findTF("AD/switcher/switch_btn")
	arg_1_0.phases = {
		arg_1_0.findTF("AD/switcher/phase1"),
		arg_1_0.findTF("AD/switcher/phase2")
	}
	arg_1_0.bar = arg_1_0.findTF("AD/switcher/phase2/Image/bar")
	arg_1_0.cur = arg_1_0.findTF("AD/switcher/phase2/Image/step")
	arg_1_0.target = arg_1_0.findTF("AD/switcher/phase2/Image/progress")
	arg_1_0.gotTag = arg_1_0.findTF("AD/switcher/phase2/got")

def var_0_0.OnFirstFlush(arg_2_0):
	onButton(arg_2_0, arg_2_0.battleBtn, function()
		arg_2_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.TASK), SFX_PANEL)
	onButton(arg_2_0, arg_2_0.getBtn, function()
		arg_2_0.emit(ActivityMediator.EVENT_OPERATION, {
			cmd = 1,
			activity_id = arg_2_0.activity.id
		}), SFX_PANEL)
	onToggle(arg_2_0, arg_2_0.switchBtn, function(arg_5_0)
		if arg_2_0.isSwitching:
			return

		arg_2_0.Switch(arg_5_0), SFX_PANEL)

	arg_2_0.inPhase2 = arg_2_0.timeStamp and pg.TimeMgr.GetInstance().GetServerTime() - arg_2_0.timeStamp > 0

	triggerToggle(arg_2_0.switchBtn, arg_2_0.inPhase2)

	if not IsNil(arg_2_0.gotTag.Find("Text")):
		setText(arg_2_0.gotTag.Find("Text"), i18n("avatarframe_got"))

return var_0_0
