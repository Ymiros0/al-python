local var_0_0 = class("EducateResPanel", import("...base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "EducateResPanel"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.moneyBtn = findTF(arg_2_0._go, "res/money")
	arg_2_0.moneyValue = findTF(arg_2_0._go, "res/money/value").GetComponent(typeof(Text))
	arg_2_0.moodBtn = findTF(arg_2_0._go, "res/mood")
	arg_2_0.moodValue = findTF(arg_2_0._go, "res/mood/value").GetComponent(typeof(Text))
	arg_2_0.moodMaxValue = pg.child_resource[EducateChar.RES_MOOD_ID].max_value
	arg_2_0.siteBtn = findTF(arg_2_0._go, "res/site")
	arg_2_0.siteValue = findTF(arg_2_0._go, "res/site/value").GetComponent(typeof(Text))
	arg_2_0.siteMaxValue = pg.child_resource[EducateChar.RES_SITE_ID].max_value

	local var_2_0 = findTF(arg_2_0._go, "res").GetComponent(typeof(Image))

	if arg_2_0.contextData and arg_2_0.contextData.showBg:
		var_2_0.enabled = True

		pg.UIMgr.GetInstance().OverlayPanelPB(arg_2_0._tf, {
			pbList = {
				findTF(arg_2_0._go, "res")
			},
			groupName = LayerWeightConst.GROUP_EDUCATE
		})
	else
		var_2_0.enabled = False

	arg_2_0.addListener()
	arg_2_0.Flush()

def var_0_0.addListener(arg_3_0):
	onButton(arg_3_0, arg_3_0.moneyBtn, function()
		arg_3_0.ShowResBox(EducateChar.RES_MONEY_ID), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.moodBtn, function()
		arg_3_0.ShowResBox(EducateChar.RES_MOOD_ID), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.siteBtn, function()
		arg_3_0.ShowResBox(EducateChar.RES_SITE_ID), SFX_PANEL)

def var_0_0.ShowResBox(arg_7_0, arg_7_1):
	arg_7_0.emit(EducateBaseUI.EDUCATE_ON_ITEM, {
		drop = {
			number = 1,
			type = EducateConst.DROP_TYPE_RES,
			id = arg_7_1
		}
	})

def var_0_0.Flush(arg_8_0):
	if not arg_8_0.GetLoaded():
		return

	arg_8_0.char = getProxy(EducateProxy).GetCharData()
	arg_8_0.siteMaxValue = arg_8_0.char.GetSiteCnt()
	arg_8_0.moneyValue.text = arg_8_0.char.money
	arg_8_0.moodValue.text = arg_8_0.char.mood .. "/" .. arg_8_0.moodMaxValue
	arg_8_0.siteValue.text = arg_8_0.char.site .. "/" .. arg_8_0.siteMaxValue

def var_0_0.FlushAddValue(arg_9_0, arg_9_1, arg_9_2):
	if not arg_9_0.GetLoaded():
		return

	arg_9_0.moodValue.text = arg_9_0.char.mood .. arg_9_1
	arg_9_0.moneyValue.text = arg_9_0.char.money .. arg_9_2

def var_0_0.OnDestroy(arg_10_0):
	if arg_10_0.contextData and arg_10_0.contextData.showBg:
		pg.UIMgr.GetInstance().UnOverlayPanel(arg_10_0._tf)

return var_0_0
