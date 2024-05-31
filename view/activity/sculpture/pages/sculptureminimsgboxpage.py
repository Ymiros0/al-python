local var_0_0 = class("SculptureMiniMsgBoxPage", import("view.base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "SculptureMiniMsgBoxUI"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.contentTxt = arg_2_0.findTF("frame/Text").GetComponent(typeof(Text))
	arg_2_0.confirmBtn = arg_2_0.findTF("frame/btns/btn_confrim")
	arg_2_0.btnImg = arg_2_0.confirmBtn.GetComponent(typeof(Image))
	arg_2_0.cancelBtn = arg_2_0.findTF("frame/btns/btn_cancel")

def var_0_0.OnInit(arg_3_0):
	onButton(arg_3_0, arg_3_0.confirmBtn, function()
		arg_3_0.Hide()

		if arg_3_0.settings.onYes:
			arg_3_0.settings.onYes(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0._tf, function()
		if arg_3_0.settings.model:
			return

		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.cancelBtn, function()
		if arg_3_0.settings.model:
			return

		arg_3_0.Hide(), SFX_PANEL)

def var_0_0.Show(arg_7_0, arg_7_1):
	var_0_0.super.Show(arg_7_0)

	arg_7_0.settings = arg_7_1
	arg_7_0.contentTxt.text = HXSet.hxLan(arg_7_1.content)

	SetParent(arg_7_0._tf, pg.UIMgr.GetInstance().OverlayMain)

	local var_7_0 = arg_7_1.yes_text or "btn_confrim"
	local var_7_1 = GetSpriteFromAtlas("ui/SculptureUI_atlas", var_7_0)

	arg_7_0.btnImg.sprite = var_7_1

	if arg_7_1.effect:
		arg_7_0.LoadEffect()

	setActive(arg_7_0.cancelBtn, arg_7_1.showNo)

def var_0_0.Hide(arg_8_0):
	var_0_0.super.Hide(arg_8_0)

	if arg_8_0.effectGo:
		Object.Destroy(arg_8_0.effectGo)

		arg_8_0.effectGo = None

def var_0_0.LoadEffect(arg_9_0):
	local var_9_0 = "liwucaijian_caidai"

	if not arg_9_0.effectGo:
		ResourceMgr.Inst.getAssetAsync("ui/" .. var_9_0, "", UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_10_0)
			if arg_9_0.exited:
				return

			arg_9_0.effectGo = Object.Instantiate(arg_10_0, arg_9_0._tf)
			arg_9_0.effectGo.name = var_9_0), True, True)
	else
		setActive(arg_9_0.effectGo, False)
		setActive(arg_9_0.effectGo, True)

def var_0_0.OnDestroy(arg_11_0):
	if arg_11_0.isShowing():
		arg_11_0.Hide()

return var_0_0
