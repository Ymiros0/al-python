ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = var_0_0.Battle.BattleCardPuzzleEvent
local var_0_3 = var_0_0.Battle.BattleDataFunction

var_0_0.Battle.CardPuzzleGoalRemind = class("CardPuzzleGoalRemind")

local var_0_4 = var_0_0.Battle.CardPuzzleGoalRemind

var_0_4.__name = "CardPuzzleGoalRemind"

def var_0_4.Ctor(arg_1_0, arg_1_1):
	arg_1_0._go = arg_1_1

	arg_1_0.init()

def var_0_4.SetCardPuzzleComponent(arg_2_0, arg_2_1):
	local var_2_0 = arg_2_1.GetPuzzleDungeonID()

	arg_2_0._tmp = var_0_3.GetPuzzleDungeonTemplate(var_2_0)

	setText(arg_2_0._bg.Find("text"), arg_2_0._tmp.description)

def var_0_4.init(arg_3_0):
	pg.DelegateInfo.New(arg_3_0)

	arg_3_0._tf = arg_3_0._go.transform
	arg_3_0._bg = arg_3_0._tf.Find("bg")

	setText(arg_3_0._bg.Find("label_ch"), i18n("card_puzzel_goal_ch"))
	setText(arg_3_0._bg.Find("label_en"), i18n("card_puzzel_goal_en"))

	arg_3_0._arrow = arg_3_0._bg.Find("arrow")
	arg_3_0._openFlag = 1

	onButton(arg_3_0, arg_3_0._bg, function()
		local var_4_0 = rtf(arg_3_0._bg).rect
		local var_4_1 = var_4_0.height + arg_3_0._openFlag * 150

		rtf(arg_3_0._bg).sizeDelta = Vector2(var_4_0.width, var_4_1)
		arg_3_0._openFlag = arg_3_0._openFlag * -1
		arg_3_0._arrow.localScale = Vector3(1, arg_3_0._openFlag, 1))

def var_0_4.Dispose(arg_5_0):
	pg.DelegateInfo.Dispose(arg_5_0)

	arg_5_0._arrow = None
	arg_5_0._bg = None
	arg_5_0._tf = None
