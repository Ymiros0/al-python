local var_0_0 = class("MonthSignReSignUI", import("...base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "MonthSignReSignUI"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.InitUI()
	setActive(arg_2_0._tf, True)
	pg.UIMgr.GetInstance().BlurPanel(arg_2_0._tf)

def var_0_0.InitUI(arg_3_0):
	arg_3_0.destroyBonusList = arg_3_0._tf.Find("frame/bg/scrollview/list")
	arg_3_0.itemTpl = arg_3_0.destroyBonusList.Find("item_tpl")

	setText(arg_3_0.findTF("frame/title_text/Text"), i18n("month_sign_resign"))
	onButton(arg_3_0, arg_3_0.findTF("frame/top/btnBack"), function()
		arg_3_0.Destroy(), SFX_CANCEL)
	onButton(arg_3_0, arg_3_0.findTF("frame/actions/confirm_btn"), function()
		arg_3_0.Destroy(), SFX_UI_EQUIPMENT_RESOLVE)

def var_0_0.setAwardShow(arg_6_0, arg_6_1, arg_6_2):
	arg_6_0.awards = arg_6_1
	arg_6_0.callback = arg_6_2

	arg_6_0.displayAwards()

def var_0_0.OnDestroy(arg_7_0):
	arg_7_0.selectedIds = None

	if arg_7_0.callback:
		arg_7_0.callback()

		arg_7_0.callback = None

	arg_7_0.awards = None

	pg.UIMgr.GetInstance().UnblurPanel(arg_7_0._tf, arg_7_0._parentTf)

def var_0_0.displayAwards(arg_8_0):
	assert(#arg_8_0.awards != 0, "items数量不能为0")
	removeAllChildren(arg_8_0.destroyBonusList)

	for iter_8_0 = 1, #arg_8_0.awards:
		local var_8_0 = cloneTplTo(arg_8_0.itemTpl, arg_8_0.destroyBonusList).Find("bg")
		local var_8_1 = arg_8_0.awards[iter_8_0]

		updateDrop(tf(var_8_0), var_8_1, {
			fromAwardLayer = True
		})
		setActive(findTF(var_8_0, "bonus"), var_8_1.riraty)

		local var_8_2 = findTF(var_8_0, "name")
		local var_8_3 = findTF(var_8_0, "name_mask")

		setActive(var_8_2, False)
		setActive(var_8_3, True)

		local var_8_4 = var_8_1.name or getText(var_8_2)

		setScrollText(findTF(var_8_0, "name_mask/name"), var_8_4)
		onButton(arg_8_0, var_8_0, function()
			if arg_8_0.inAniming:
				return

			arg_8_0.emit(BaseUI.ON_DROP, var_8_1), SFX_PANEL)

return var_0_0
