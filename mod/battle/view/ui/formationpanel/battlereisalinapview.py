ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleDataFunction
local var_0_2 = var_0_0.Battle.BattleConfig
local var_0_3 = class("BattleReisalinAPView")

var_0_0.Battle.BattleReisalinAPView = var_0_3
var_0_3.__name = "BattleReisalinAPView"

def var_0_3.Ctor(arg_1_0, arg_1_1):
	arg_1_0._tf = arg_1_1

	arg_1_0.init()

def var_0_3.init(arg_2_0):
	arg_2_0._apCap = var_0_2.FLEET_ATTR_CAP[arg_2_0.GetAttrName()]
	arg_2_0._count = findTF(arg_2_0._tf, "count")
	arg_2_0._glow = findTF(arg_2_0._tf, "glow_gizmos")
	arg_2_0._countText = arg_2_0._count.GetComponent(typeof(Text))

	SetActive(arg_2_0._tf, True)
	arg_2_0.UpdateAP(0)

def var_0_3.UpdateAP(arg_3_0, arg_3_1):
	arg_3_0._countText.text = arg_3_1

	if arg_3_1 >= arg_3_0._apCap:
		arg_3_0._countText.color = Color.ReisalinGold

		SetActive(arg_3_0._glow, True)
	else
		arg_3_0._countText.color = Color.white

		SetActive(arg_3_0._glow, False)

def var_0_3.GetAttrName(arg_4_0):
	return var_0_2.ALCHEMIST_AP_NAME

def var_0_3.Dispose(arg_5_0):
	arg_5_0._count = None
	arg_5_0._glow = None
	arg_5_0._countText = None
	arg_5_0._tf = None
