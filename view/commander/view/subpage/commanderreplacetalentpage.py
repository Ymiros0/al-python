local var_0_0 = class("CommanderReplaceTalentPage", import("view.base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "CommanderCatReplaceTalentUI"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.replaceList = UIItemList.New(arg_2_0.findTF("bg/frame/bg/talents/content"), arg_2_0.findTF("bg/frame/bg/talents/content/talent"))
	arg_2_0.replaceTargetTF = arg_2_0.findTF("bg/frame/bg/talent")
	arg_2_0.replaceTalent = arg_2_0.findTF("bg/frame/bg/replace")
	arg_2_0.replaceCloseBtn = arg_2_0.findTF("bg/frame/close_btn")
	arg_2_0.replaceCancelBtn = arg_2_0.findTF("bg/frame/cancel_btn")
	arg_2_0.confirmBtn = arg_2_0.findTF("bg/frame/confirm_btn")

	setActive(arg_2_0.findTF("bg/frame/consume"), False)
	setText(arg_2_0.findTF("bg/frame/bg/title/Text"), i18n("commander_choice_talent_3"))
	setText(arg_2_0.findTF("bg/frame/bg/talents/title/Text"), i18n("commander_choice_talent_2"))

def var_0_0.OnInit(arg_3_0):
	onButton(arg_3_0, arg_3_0.replaceCloseBtn, function()
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.replaceCancelBtn, function()
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0.Hide(), SFX_PANEL)

def var_0_0.Show(arg_7_0, arg_7_1, arg_7_2):
	var_0_0.super.Show(arg_7_0)
	arg_7_0._tf.SetAsLastSibling()

	arg_7_0.commander = arg_7_1

	arg_7_0.UpdateTalents(arg_7_2, None)
	arg_7_0.UpdateList(arg_7_2)

def var_0_0.UpdateList(arg_8_0, arg_8_1):
	local var_8_0 = arg_8_0.commander.getTalents()

	arg_8_0.replaceList.make(function(arg_9_0, arg_9_1, arg_9_2)
		if arg_9_0 == UIItemList.EventUpdate:
			local var_9_0 = var_8_0[arg_9_1 + 1]

			onButton(arg_8_0, arg_9_2, function()
				if arg_8_0.prevToggle != arg_9_2:
					arg_8_0.UpdateTalents(arg_8_1, var_9_0)

					if arg_8_0.prevToggle:
						setActive(arg_8_0.prevToggle.Find("mark"), False)

					arg_8_0.prevToggle = arg_9_2

					setActive(arg_9_2.Find("mark"), True), SFX_PANEL)
			GetImageSpriteFromAtlasAsync("CommanderTalentIcon/" .. var_9_0.getConfig("icon"), "", arg_9_2))
	arg_8_0.replaceList.align(#var_8_0)

def var_0_0.UpdateTalents(arg_11_0, arg_11_1, arg_11_2):
	local var_11_0 = arg_11_0.commander

	arg_11_0.UpdateTalentCard(arg_11_0.replaceTargetTF, arg_11_1)
	arg_11_0.UpdateTalentCard(arg_11_0.replaceTalent, arg_11_2)
	onButton(arg_11_0, arg_11_0.confirmBtn, function()
		if arg_11_2 and arg_11_1 and var_11_0:
			if arg_11_2.getConfig("worth") > 1:
				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					content = i18n("commander_ability_replace_warning"),
					def onYes:()
						arg_11_0.emit(CommanderCatMediator.LEARN_TALENT, var_11_0.id, arg_11_1.id, arg_11_2.id)
						arg_11_0.Hide()
				})
			else
				arg_11_0.emit(CommanderCatMediator.LEARN_TALENT, var_11_0.id, arg_11_1.id, arg_11_2.id)
				arg_11_0.Hide(), SFX_PANEL)

def var_0_0.UpdateTalentCard(arg_14_0, arg_14_1, arg_14_2):
	local var_14_0 = arg_14_1.Find("unlock")
	local var_14_1 = arg_14_1.Find("lock")

	if arg_14_2:
		GetImageSpriteFromAtlasAsync("CommanderTalentIcon/" .. arg_14_2.getConfig("icon"), "", var_14_0.Find("icon"))

		local var_14_2 = var_14_0.Find("tree_btn")

		if var_14_2:
			onButton(arg_14_0, var_14_2, function()
				arg_14_0.contextData.treePanel.ExecuteAction("Show", arg_14_2), SFX_PANEL)

		setText(var_14_0.Find("name_bg/Text"), arg_14_2.getConfig("name"))
		setScrollText(var_14_0.Find("desc/Text"), arg_14_2.getConfig("desc"))

	setActive(var_14_0, arg_14_2)

	if var_14_1:
		setActive(var_14_1, not arg_14_2)

def var_0_0.Hide(arg_16_0):
	var_0_0.super.Hide(arg_16_0)

	if arg_16_0.prevToggle:
		setActive(arg_16_0.prevToggle.Find("mark"), False)

		arg_16_0.prevToggle = None

def var_0_0.OnDestroy(arg_17_0):
	return

return var_0_0
