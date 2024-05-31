local var_0_0 = class("MailTipsLayer", import("view.base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "MailTipLayersMsgBoxUI"

def var_0_0.init(arg_2_0):
	arg_2_0.btnBack = arg_2_0._tf.Find("adapt/window/top/btnBack")
	arg_2_0.goBtn = arg_2_0._tf.Find("adapt/window/button_container/btn_ok")
	arg_2_0.title = arg_2_0._tf.Find("adapt/window/top/bg/infomation/title")
	arg_2_0.bgBack = arg_2_0._tf.Find("bg")
	arg_2_0.context = arg_2_0._tf.Find("adapt/window/msg_panel/content").GetComponent("RichText")

def var_0_0.didEnter(arg_3_0):
	pg.UIMgr.GetInstance().BlurPanel(arg_3_0._tf, False, {
		weight = LayerWeightConst.TOP_LAYER
	})
	onButton(arg_3_0, arg_3_0.btnBack, function()
		arg_3_0.closeView(), SFX_CANCEL)
	onButton(arg_3_0, arg_3_0.bgBack, function()
		arg_3_0.closeView(), SFX_CANCEL)
	onButton(arg_3_0, arg_3_0.goBtn, function()
		arg_3_0.contextData.onYes()
		arg_3_0.closeView(), SFX_CANCEL)

	arg_3_0.context.text = arg_3_0.contextData.content

	setText(arg_3_0.title, i18n("mail_boxtitle_information"))
	setText(arg_3_0.goBtn.Find("Text"), i18n("mail_box_confirm"))

	if not pg.NewStoryMgr.GetInstance().IsPlayed("NEW_MAIL_GUIDE"):
		pg.NewGuideMgr.GetInstance().Play("NEW_MAIL_GUIDE")
		pg.m02.sendNotification(GAME.STORY_UPDATE, {
			storyId = "NEW_MAIL_GUIDE"
		})

def var_0_0.willExit(arg_7_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_7_0._tf)

return var_0_0
