local var_0_0 = class("TransportCellView", import(".OniCellView"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.tfShadow = arg_1_0.tf.Find("shadow")
	arg_1_0.tfIcon = arg_1_0.tf.Find("ship/icon")
	arg_1_0.tfHp = arg_1_0.tf.Find("hp")
	arg_1_0.tfHpText = arg_1_0.tf.Find("hp/text")
	arg_1_0.tfFighting = arg_1_0.tf.Find("fighting")

def var_0_0.GetRotatePivot(arg_2_0):
	return arg_2_0.tfIcon

def var_0_0.GetOrder(arg_3_0):
	return ChapterConst.CellPriorityLittle

def var_0_0.SetActive(arg_4_0, arg_4_1):
	SetActive(arg_4_0.tf, arg_4_1)

def var_0_0.LoadIcon(arg_5_0, arg_5_1, arg_5_2):
	if arg_5_1 == "" or arg_5_0.lastPrefab == arg_5_1:
		existCall(arg_5_2)

		return

	arg_5_0.lastPrefab = arg_5_1

	arg_5_0.GetLoader().GetSpriteQuiet("enemies/" .. arg_5_1, arg_5_1, arg_5_0.tfIcon)
	existCall(arg_5_2)

return var_0_0
