local var_0_0 = class("CryptolaliaResDeleteWindow", import("view.base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "CryptolaliaResDeleteWindowui"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.closeBtn = arg_2_0.findTF("window/top/btnBack")
	arg_2_0.contentTxt = arg_2_0.findTF("window/content/Text").GetComponent(typeof(Text))
	arg_2_0.icon = arg_2_0.findTF("window/content/cover/icon").GetComponent(typeof(Image))
	arg_2_0.signature = arg_2_0.findTF("window/content/cover/signature").GetComponent(typeof(Image))
	arg_2_0.name = arg_2_0.findTF("window/content/cover/name").GetComponent(typeof(Text))
	arg_2_0.shipname = arg_2_0.findTF("window/content/cover/shipname").GetComponent(typeof(Text))
	arg_2_0.cancelBtn = arg_2_0.findTF("window/button_container/cancel")
	arg_2_0.confirmBtn = arg_2_0.findTF("window/button_container/confirm")

	setText(arg_2_0.findTF("window/top/title"), i18n("cryptolalia_delete_res_title"))
	setText(arg_2_0.cancelBtn.Find("Text"), i18n("text_cancel"))
	setText(arg_2_0.confirmBtn.Find("Text"), i18n("text_confirm"))

def var_0_0.OnInit(arg_3_0):
	onButton(arg_3_0, arg_3_0.cancelBtn, function()
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.closeBtn, function()
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0.Hide(), SFX_PANEL)

def var_0_0.Show(arg_7_0, arg_7_1, arg_7_2):
	var_0_0.super.Show(arg_7_0)
	pg.UIMgr.GetInstance().BlurPanel(arg_7_0._tf, False, {
		weight = LayerWeightConst.TOP_LAYER
	})

	arg_7_0.contentTxt.text = i18n("cryptolalia_delete_res_tip", arg_7_1.GetResSize(arg_7_2))
	arg_7_0.name.text = arg_7_1.GetName()
	arg_7_0.shipname.text = arg_7_1.GetShipName()

	local var_7_0 = arg_7_1.GetShipGroupId()

	LoadSpriteAtlasAsync("CryptolaliaShip/" .. var_7_0, "cd", function(arg_8_0)
		if arg_7_0.exited:
			return

		arg_7_0.icon.sprite = arg_8_0

		arg_7_0.icon.SetNativeSize())
	onButton(arg_7_0, arg_7_0.confirmBtn, function()
		if IsUnityEditor:
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_no_open"))

			return

		arg_7_0.Delete(arg_7_1, arg_7_2)
		arg_7_0.Hide(), SFX_PANEL)

def var_0_0.Delete(arg_10_0, arg_10_1, arg_10_2):
	if arg_10_1 and arg_10_1.IsPlayableState(arg_10_2):
		local var_10_0 = arg_10_1.GetCpkName(arg_10_2)
		local var_10_1 = Cryptolalia.BuildCpkPath(var_10_0)
		local var_10_2 = Cryptolalia.BuildSubtitlePath(var_10_0)

		pg.CipherGroupMgr.GetInstance().DelFile({
			var_10_1,
			var_10_2
		})
		arg_10_0.emit(CryptolaliaScene.ON_DELETE)

def var_0_0.Hide(arg_11_0):
	var_0_0.super.Hide(arg_11_0)
	pg.UIMgr.GetInstance().UnblurPanel(arg_11_0._tf, arg_11_0._parentTf)

def var_0_0.OnDestroy(arg_12_0):
	arg_12_0.exited = True

return var_0_0
