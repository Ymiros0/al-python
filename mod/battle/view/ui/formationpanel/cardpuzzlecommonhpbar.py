ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig

var_0_0.Battle.CardPuzzleCommonHPBar = class("CardPuzzleCommonHPBar")

local var_0_2 = var_0_0.Battle.CardPuzzleCommonHPBar

var_0_2.__name = "CardPuzzleCommonHPBar"

def var_0_2.Ctor(arg_1_0, arg_1_1):
	arg_1_0._go = arg_1_1
	arg_1_0._tf = arg_1_0._go.transform
	arg_1_0._hpTF = arg_1_0._tf.Find("fleetBlood/blood")
	arg_1_0._hpProgress = arg_1_0._hpTF.GetComponent(typeof(Image))

def var_0_2.SetCardPuzzleComponent(arg_2_0, arg_2_1):
	arg_2_0._info = arg_2_1

def var_0_2.Update(arg_3_0):
	arg_3_0.updateHPBar()

def var_0_2.updateHPBar(arg_4_0):
	local var_4_0 = arg_4_0._info.GetCurrentCommonHP() / arg_4_0._info.GetTotalCommonHP()

	arg_4_0._hpProgress.fillAmount = var_4_0

def var_0_2.Dispose(arg_5_0):
	arg_5_0._hpProgress = None
	arg_5_0._hpTF = None
	arg_5_0._tf = None
	arg_5_0._go = None

def var_0_2.updateResource(arg_6_0):
	return
