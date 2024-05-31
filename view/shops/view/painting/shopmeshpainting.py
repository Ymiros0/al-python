local var_0_0 = class("ShopMeshPainting")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0._painting = arg_1_1

def var_0_0.Load(arg_2_0, arg_2_1, arg_2_2, arg_2_3):
	setShopPaintingPrefab(arg_2_0._painting, arg_2_1, arg_2_2 or "chuanwu")
	arg_2_3()

def var_0_0.Action(arg_3_0, arg_3_1):
	return

def var_0_0.UnLoad(arg_4_0, arg_4_1):
	retShopPaintingPrefab(arg_4_0._painting, arg_4_1)

return var_0_0
