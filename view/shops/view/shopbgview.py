local var_0_0 = class("ShopBgView")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0._bg = arg_1_1
	arg_1_0.img = arg_1_0._bg.GetComponent(typeof(Image))

	setActive(arg_1_1, False)

	arg_1_0.bgs = {}

def var_0_0.Init(arg_2_0, arg_2_1):
	setActive(arg_2_0._bg, arg_2_1 != None)

	if arg_2_1:
		local var_2_0

		if arg_2_0.bgs[arg_2_1]:
			var_2_0 = arg_2_0.bgs[arg_2_1]
		else
			var_2_0 = GetSpriteFromAtlas(arg_2_1, "")

		arg_2_0.img.sprite = var_2_0

def var_0_0.Dispose(arg_3_0):
	UIUtil.ClearImageSprite(arg_3_0._bg.gameObject)

	arg_3_0.bgs = None

return var_0_0
