local var_0_0 = class("BackYardThemeTemplateCard", import("...Shop.cards.BackYardThemeCard"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0._go = arg_1_1
	arg_1_0._tf = arg_1_1.transform
	arg_1_0.content = arg_1_0._tf.Find("content")
	arg_1_0.mask = arg_1_0.content.Find("mask")
	arg_1_0.iconRaw = arg_1_0.content.Find("icon_mask/icon_raw").GetComponent(typeof(RawImage))
	arg_1_0.nameTxt = arg_1_0.content.Find("Text").GetComponent(typeof(Text))
	arg_1_0.pos = arg_1_0.content.Find("pos")
	arg_1_0.posTxt = arg_1_0.pos.Find("Text").GetComponent(typeof(Text))

def var_0_0.FlushData(arg_2_0, arg_2_1):
	arg_2_0.template = arg_2_1
	arg_2_0.themeVO = arg_2_1
	arg_2_0.nameTxt.text = arg_2_1.GetName()

def var_0_0.Update(arg_3_0, arg_3_1):
	if arg_3_0.template and arg_3_1.id == arg_3_0.template.id:
		arg_3_0.FlushData(arg_3_1)

		return
	else
		arg_3_0.FlushData(arg_3_1)
		setActive(arg_3_0.iconRaw.gameObject, False)

		local var_3_0 = arg_3_1.GetIconMd5()

		BackYardThemeTempalteUtil.GetTexture(arg_3_1.GetTextureIconName(), var_3_0, function(arg_4_0)
			if not IsNil(arg_3_0.iconRaw) and arg_4_0:
				setActive(arg_3_0.iconRaw.gameObject, True)

				arg_3_0.iconRaw.texture = arg_4_0)

		local var_3_1 = arg_3_1.IsSelfUsage()

		setActive(arg_3_0.mask, arg_3_1.IsPushed() and var_3_1)
		setActive(arg_3_0.pos, var_3_1)

		if var_3_1:
			local var_3_2 = arg_3_1.pos

			if arg_3_1.pos <= 9:
				var_3_2 = "0" .. arg_3_1.pos

			arg_3_0.posTxt.text = var_3_2

def var_0_0.Dispose(arg_5_0):
	var_0_0.super.Dispose(arg_5_0)

	if not IsNil(arg_5_0.iconRaw.texture):
		Object.Destroy(arg_5_0.iconRaw.texture)

		arg_5_0.iconRaw.texture = None

return var_0_0
