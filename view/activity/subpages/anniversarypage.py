local var_0_0 = class("AnniversaryPage", import("...base.BaseActivityPage"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.btnShop = arg_1_0.findTF("BtnShop")
	arg_1_0.charListTF = arg_1_0.findTF("list")
	arg_1_0.charTF = arg_1_0.findTF("Image", arg_1_0.charListTF)

	arg_1_0.scrollAnim()

def var_0_0.OnFirstFlush(arg_2_0):
	onButton(arg_2_0, arg_2_0.btnShop, function()
		arg_2_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.SKINSHOP), SFX_PANEL)

def var_0_0.scrollAnim(arg_4_0):
	arg_4_0._tf.GetComponent(typeof(DftAniEvent)).SetTriggerEvent(function(arg_5_0)
		arg_4_0.charListTF.GetChild(0).SetAsLastSibling()

		local var_5_0 = 0

		eachChild(arg_4_0.charListTF, function(arg_6_0)
			setActive(arg_4_0.charListTF.GetChild(var_5_0), var_5_0 != 6)

			var_5_0 = var_5_0 + 1)
		arg_4_0.charTF.SetSiblingIndex(6))

def var_0_0.OnDestroy(arg_7_0):
	return

return var_0_0
