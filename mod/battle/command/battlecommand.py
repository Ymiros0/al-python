ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleCommand = class("BattleCommand", var_0_0.MVC.Command)
var_0_0.Battle.BattleCommand.__name = "BattleCommand"

def var_0_0.Battle.BattleCommand.Ctor(arg_1_0):
	var_0_0.Battle.BattleCommand.super.Ctor(arg_1_0)

def var_0_0.Battle.BattleCommand.Initialize(arg_2_0):
	var_0_0.Battle.BattleCommand.super.Initialize(arg_2_0)

	arg_2_0._dataProxy = arg_2_0._state.GetProxyByName(var_0_0.Battle.BattleDataProxy.__name)

	arg_2_0.InitProtocol()
	arg_2_0.InitBattleEvent()

def var_0_0.Battle.BattleCommand.StartBattle(arg_3_0):
	arg_3_0._state.Active()

def var_0_0.Battle.BattleCommand.InitProtocol(arg_4_0):
	return

def var_0_0.Battle.BattleCommand.InitBattleEvent(arg_5_0):
	return
