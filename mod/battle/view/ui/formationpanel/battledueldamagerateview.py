ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleEvent
local var_0_2 = var_0_0.Battle.BattleConfig
local var_0_3 = class("BattleDuelDamageRateView")

var_0_0.Battle.BattleDuelDamageRateView = var_0_3
var_0_3.__name = "BattleDuelDamageRateView"

def var_0_3.Ctor(arg_1_0, arg_1_1):
	var_0_0.EventListener.AttachEventListener(arg_1_0)

	arg_1_0._go = arg_1_1
	arg_1_0._tf = arg_1_1.transform
	arg_1_0._progressList = {}
	arg_1_0._rateBarList = {}
	arg_1_0._fleetList = {}
	arg_1_0._rateBarList[var_0_2.FRIENDLY_CODE] = arg_1_0._tf.Find("leftDamageBar")
	arg_1_0._rateBarList[var_0_2.FOE_CODE] = arg_1_0._tf.Find("rightDamageBar")

def var_0_3.SetActive(arg_2_0, arg_2_1):
	setActive(arg_2_0._go, arg_2_1)

def var_0_3.SetFleetVO(arg_3_0, arg_3_1, arg_3_2):
	arg_3_0._fleetList[arg_3_1] = True

	local var_3_0 = arg_3_0._rateBarList[arg_3_1.GetIFF()]

	var_3_0.Find("nameText").GetComponent(typeof(Text)).text = arg_3_2.name
	var_3_0.Find("LVText").GetComponent(typeof(Text)).text = "Lv." .. arg_3_2.level

	local var_3_1 = var_3_0.Find("bar/progress").GetComponent(typeof(Image))

	arg_3_0._progressList[arg_3_1.GetIFF()] = var_3_1

	arg_3_1.RegisterEventListener(arg_3_0, var_0_1.FLEET_DMG_CHANGE, arg_3_0.onDMGChange)

def var_0_3.onDMGChange(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_1.Dispatcher
	local var_4_1 = var_4_0.GetIFF()

	arg_4_0._progressList[var_4_1].fillAmount = var_4_0.GetDamageRatio()

def var_0_3.Dispose(arg_5_0):
	for iter_5_0, iter_5_1 in pairs(arg_5_0._fleetList):
		iter_5_0.UnregisterEventListener(arg_5_0, var_0_1.FLEET_DMG_CHANGE)

	arg_5_0._rateBarList = None
	arg_5_0._progressList = None
