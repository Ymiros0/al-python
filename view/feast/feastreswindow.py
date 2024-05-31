local var_0_0 = class("FeastResWindow", import("view.base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "FeastResWindow"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.icon = arg_2_0.findTF("frame/item/icon").GetComponent(typeof(Image))
	arg_2_0.name = arg_2_0.findTF("frame/name/Text").GetComponent(typeof(Text))
	arg_2_0.desc = arg_2_0.findTF("frame/Text").GetComponent(typeof(Text))
	arg_2_0.outPut = arg_2_0.findTF("frame/output/Text").GetComponent(typeof(Text))
	arg_2_0.goBtn = arg_2_0.findTF("frame/go")

	setText(arg_2_0.goBtn.Find("Text"), i18n("feast_res_window_go_label"))
	setText(arg_2_0.findTF("frame/title"), i18n("feast_res_window_title"))

def var_0_0.OnInit(arg_3_0):
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0.Hide(), SFX_PANEL)

def var_0_0.Show(arg_5_0, arg_5_1):
	var_0_0.super.Show(arg_5_0)

	arg_5_0.id = arg_5_1

	arg_5_0.UpdateView()

def var_0_0.UpdateView(arg_6_0):
	local var_6_0 = pg.activity_workbench_item[arg_6_0.id]

	arg_6_0.icon.sprite = LoadSprite("props/" .. var_6_0.icon)

	arg_6_0.icon.SetNativeSize()

	arg_6_0.name.text = var_6_0.name
	arg_6_0.desc.text = var_6_0.display
	arg_6_0.outPut.text = var_6_0.get_access[1]

	onButton(arg_6_0, arg_6_0.goBtn, function()
		pg.m02.sendNotification(GAME.WORKBENCH_ITEM_GO, arg_6_0.id), SFX_PANEL)

def var_0_0.OnDestroy(arg_8_0):
	return

return var_0_0
