ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = var_0_0.Battle.BattleFleetCardPuzzleCardManageComponent

var_0_0.Battle.BattleCardPuzzleWave = class("BattleCardPuzzleWave", var_0_0.Battle.BattleWaveInfo)
var_0_0.Battle.BattleCardPuzzleWave.__name = "BattleCardPuzzleWave"

local var_0_3 = var_0_0.Battle.BattleCardPuzzleWave

def var_0_3.Ctor(arg_1_0):
	var_0_3.super.Ctor(arg_1_0)

def var_0_3.SetWaveData(arg_2_0, arg_2_1):
	var_0_3.super.SetWaveData(arg_2_0, arg_2_1)

	arg_2_0._cardID = arg_2_0._param.card_id
	arg_2_0._moveTo = arg_2_0._param.move_to
	arg_2_0._moveOP = arg_2_0._param.move_op or var_0_2.FUNC_NAME_ADD
	arg_2_0._op = arg_2_0._param.shuffle or 1

def var_0_3.DoWave(arg_3_0):
	var_0_3.super.DoWave(arg_3_0)

	local var_3_0 = var_0_0.Battle.BattleDataProxy.GetInstance().GetFleetByIFF(var_0_1.FRIENDLY_CODE).GetCardPuzzleComponent()
	local var_3_1 = var_3_0.GenerateCard(arg_3_0._cardID)
	local var_3_2 = var_3_0.GetCardPileByIndex(arg_3_0._moveTo)

	var_3_2[arg_3_0._moveOP](var_3_2, var_3_1)

	if arg_3_0._op == 1:
		var_3_2.Shuffle()

	arg_3_0.doPass()
