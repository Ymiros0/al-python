ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleBuffDiva", var_0_0.Battle.BattleBuffEffect)

var_0_0.Battle.BattleBuffDiva = var_0_1
var_0_1.__name = "BattleBuffDiva"

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.super.Ctor(arg_1_0, arg_1_1)

def var_0_1.onInitGame(arg_2_0, arg_2_1, arg_2_2):
	local var_2_0 = var_0_0.Battle.BattleDataProxy.GetInstance().GetBGMList()
	local var_2_1 = var_2_0[math.random(#var_2_0)]

	pg.BgmMgr.GetInstance().Push(BattleScene.__cname, var_2_1)

def var_0_1.onTrigger(arg_3_0):
	local var_3_0 = var_0_0.Battle.BattleDataProxy.GetInstance().GetBGMList(True)
	local var_3_1 = var_3_0[math.random(#var_3_0)]

	pg.BgmMgr.GetInstance().Push(BattleScene.__cname, var_3_1)
