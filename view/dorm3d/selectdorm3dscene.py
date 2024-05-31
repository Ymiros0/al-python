local var_0_0 = class("SelectDorm3DScene", import("view.base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "SelectDorm3DUI"

def var_0_0.init(arg_2_0):
	onButton(arg_2_0, arg_2_0._tf.Find("btn_back"), function()
		arg_2_0.closeView(), SFX_CANCEL)

	arg_2_0.ids = pg.dorm3d_dorm_template.all
	arg_2_0.blurPanel = arg_2_0._tf.Find("BlurPanel")

	local var_2_0 = arg_2_0.blurPanel.Find("window/container")

	arg_2_0.itemList = UIItemList.New(var_2_0, var_2_0.Find("tpl"))

	arg_2_0.itemList.make(function(arg_4_0, arg_4_1, arg_4_2)
		arg_4_1 = arg_4_1 + 1

		if arg_4_0 == UIItemList.EventUpdate:
			local var_4_0 = arg_2_0.ids[arg_4_1]

			setActive(arg_4_2.Find("base"), var_4_0)
			setActive(arg_4_2.Find("empty"), not var_4_0)

			if var_4_0:
				GetImageSpriteFromAtlasAsync(string.format("dorm3dselect/%d_head", var_4_0), "", arg_4_2.Find("base/Image"))
				GetImageSpriteFromAtlasAsync(string.format("dorm3dselect/%d_name", var_4_0), "", arg_4_2.Find("base/name"))

				local var_4_1 = getProxy(ApartmentProxy).getApartment(var_4_0)

				setText(arg_4_2.Find("base/favor_level/Text"), var_4_1 and var_4_1.level or "?")
				onToggle(arg_2_0, arg_4_2.Find("base"), function(arg_5_0)
					if arg_5_0 and arg_2_0.selectId != var_4_0:
						arg_2_0.SetPage(var_4_0), SFX_PANEL)
				triggerToggle(arg_4_2.Find("base"), arg_4_1 == 1)
			else
				setText(arg_4_2.Find("empty/Text"), i18n("dorm3d_waiting"))
				RemoveComponent(arg_4_2, typeof(Toggle)))
	setText(arg_2_0._tf.Find("BlurPanel/window/bottom/daily/Text"), i18n("dorm3d_daily_favor"))

	arg_2_0.textDic = {}
	arg_2_0.btnGo = arg_2_0._tf.Find("BlurPanel/window/bottom/btn_go")

	onButton(arg_2_0, arg_2_0.btnGo, function()
		if arg_2_0.selectId != 20220:
			return

		arg_2_0.emit(SelectDorm3DMediator.ON_DORM, arg_2_0.selectId), SFX_PANEL)
	pg.UIMgr.GetInstance().OverlayPanelPB(arg_2_0.blurPanel, {
		pbList = {
			arg_2_0.blurPanel.Find("window")
		}
	})

def var_0_0.didEnter(arg_7_0):
	local var_7_0 = (math.floor(#arg_7_0.ids / 3) + 1) * 3

	arg_7_0.itemList.align(var_7_0)

def var_0_0.SetPage(arg_8_0, arg_8_1):
	arg_8_0.selectId = arg_8_1

	local var_8_0 = arg_8_0._tf.Find("Main/painting")

	GetImageSpriteFromAtlasAsync(string.format("dorm3dselect/%d_painting", arg_8_1), "", var_8_0)

	local var_8_1 = getProxy(ApartmentProxy).getApartment(arg_8_1)
	local var_8_2 = var_8_1.getConfig("welcome_text")

	arg_8_0.textDic[arg_8_1] = arg_8_0.textDic[arg_8_1] or math.random(#var_8_2)

	setText(var_8_0.Find("talk/Text"), var_8_2[arg_8_0.textDic[arg_8_1]])
	setText(arg_8_0._tf.Find("BlurPanel/window/bottom/daily/count"), string.format("%d/%d", var_8_1.getDailyFavor()))

def var_0_0.willExit(arg_9_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_9_0.blurPanel, arg_9_0._tf)

return var_0_0
