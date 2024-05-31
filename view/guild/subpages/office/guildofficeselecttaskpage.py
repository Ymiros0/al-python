local var_0_0 = class("GuildOfficeSelectTaskPage", import("...base.GuildBasePage"))

def var_0_0.getTargetUI(arg_1_0):
	return "GuildTaskSelectBluePage", "GuildTaskSelectRedPage"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.uilist = UIItemList.New(arg_2_0.findTF("frame/bg/scrollrect/content"), arg_2_0.findTF("frame/bg/scrollrect/content/tpl"))
	arg_2_0.closeBtn = arg_2_0._tf.Find("frame/title/close")

def var_0_0.OnInit(arg_3_0):
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0.Close(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.closeBtn, function()
		arg_3_0.Close(), SFX_PANEL)

def var_0_0.Show(arg_6_0, arg_6_1, arg_6_2):
	arg_6_0.guild = arg_6_1
	arg_6_0.isAdmin = arg_6_2

	setActive(arg_6_0._tf, True)
	pg.UIMgr.GetInstance().BlurPanel(arg_6_0._tf)
	arg_6_0._tf.SetAsLastSibling()
	arg_6_0.Update()

def var_0_0.Update(arg_7_0):
	local var_7_0 = arg_7_0.guild.getSelectableWeeklyTasks()

	arg_7_0.uilist.make(function(arg_8_0, arg_8_1, arg_8_2)
		if arg_8_0 == UIItemList.EventUpdate:
			local var_8_0 = GuildTaskCard.New(arg_8_2)
			local var_8_1 = var_7_0[arg_8_1 + 1]

			onButton(arg_7_0, var_8_0.acceptBtn, function()
				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					content = i18n("guild_task_selecte_tip", var_8_1.getConfig("name")),
					def onYes:()
						arg_7_0.emit(GuildOfficeMediator.ON_SELECT_TASK, var_8_0.task.id)
						arg_7_0.Close()
				}), SFX_PANEL)
			var_8_0.Update(var_8_1))
	arg_7_0.uilist.align(#var_7_0)

def var_0_0.Close(arg_11_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_11_0._tf, arg_11_0._parentTf)
	setActive(arg_11_0._tf, False)

def var_0_0.OnDestroy(arg_12_0):
	arg_12_0.Close()

return var_0_0
