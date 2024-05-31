ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = var_0_0.Battle.BattleDataFunction

var_0_0.Battle.CardPuzzleCardDetailAffix = class("CardPuzzleCardDetailAffix")

local var_0_3 = var_0_0.Battle.CardPuzzleCardDetailAffix

var_0_3.__name = "CardPuzzleCardDetailAffix"

def var_0_3.Ctor(arg_1_0, arg_1_1):
	arg_1_0._go = arg_1_1
	arg_1_0._tf = arg_1_0._go.transform
	arg_1_0._nameLabel = arg_1_0._tf.Find("name/labelCN")
	arg_1_0._nameLabelEN = arg_1_0._tf.Find("name/labelEN")
	arg_1_0._desc = arg_1_0._tf.Find("Desc")

def var_0_3.SetActive(arg_2_0, arg_2_1):
	setActive(arg_2_0._go, arg_2_1)

def var_0_3.SetAffixID(arg_3_0, arg_3_1):
	local var_3_0 = var_0_2.GetPuzzleCardAffixDataTemplate(arg_3_1)

	setText(arg_3_0._nameLabel, var_3_0.name)
	setText(arg_3_0._nameLabelEN, var_3_0.name_EN)
	setText(arg_3_0._desc, var_3_0.discript)

def var_0_3.Dispose(arg_4_0):
	arg_4_0._nameLabel = None
	arg_4_0._nameLabelEN = None
	arg_4_0._desc = None
	arg_4_0._tf = None
	arg_4_0._go = None
