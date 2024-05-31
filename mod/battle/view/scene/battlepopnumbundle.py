ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleUnitEvent
local var_0_2 = var_0_0.Battle.BattleConst
local var_0_3 = var_0_0.Battle.BattlePopNumManager

var_0_0.Battle.BattlePopNumBundle = class("BattlePopNumBundle")
var_0_0.Battle.BattlePopNumBundle.__name = "BattlePopNumBundle"

local var_0_4 = var_0_0.Battle.BattlePopNumBundle

var_0_4.PRO = 0
var_0_4.SLIM = 1

def var_0_4.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.pool = arg_1_1
	arg_1_0._container = cloneTplTo(arg_1_2.containerTpl, arg_1_2.containerTpl.parent)
	arg_1_0._bundleType = arg_1_2.type
	arg_1_0._score = arg_1_2.score

	arg_1_0.init()

def var_0_4.InitPopScore(arg_2_0, arg_2_1):
	arg_2_0._allPool[var_0_3.POP_SCORE] = arg_2_0.generateTempPool(var_0_3.POP_SCORE, arg_2_0._container, arg_2_1, 1)

def var_0_4.GetContainer(arg_3_0):
	return arg_3_0._container

def var_0_4.init(arg_4_0):
	arg_4_0._allPool = {}

	local var_4_0 = var_0_3.GetInstance().GetPopSkin()

	if arg_4_0._score:
		arg_4_0._allPool[var_0_3.POP_SCORE] = arg_4_0.generateTempPool(var_0_3.POP_SCORE, arg_4_0._container, var_4_0, 1)
	else
		arg_4_0._allPool[var_0_3.POP_COMMON] = arg_4_0.generateTempPool(var_0_3.POP_COMMON, arg_4_0._container, var_4_0, 1)
		arg_4_0._allPool[var_0_3.POP_CT_EXPLO] = arg_4_0.generateTempPool(var_0_3.POP_CT_EXPLO, arg_4_0._container, var_4_0, 0)
		arg_4_0._allPool[var_0_3.POP_MISS] = arg_4_0.generateTempPool(var_0_3.POP_MISS, arg_4_0._container, var_4_0, 0)
		arg_4_0._allPool[var_0_3.POP_NORMAL] = arg_4_0.generateTempPool(var_0_3.POP_NORMAL, arg_4_0._container, var_4_0, 0)
		arg_4_0._allPool[var_0_3.POP_CT_NORMAL] = arg_4_0.generateTempPool(var_0_3.POP_CT_NORMAL, arg_4_0._container, var_4_0, 0)

		if arg_4_0._bundleType == var_0_4.PRO:
			arg_4_0._allPool[var_0_3.POP_UNBREAK] = arg_4_0.generateTempPool(var_0_3.POP_UNBREAK, arg_4_0._container, var_4_0, 1)
			arg_4_0._allPool[var_0_3.POP_HEAL] = arg_4_0.generateTempPool(var_0_3.POP_HEAL, arg_4_0._container, var_4_0, 1)
			arg_4_0._allPool[var_0_3.POP_EXPLO] = arg_4_0.generateTempPool(var_0_3.POP_EXPLO, arg_4_0._container, var_4_0, 0)
			arg_4_0._allPool[var_0_3.POP_PIERCE] = arg_4_0.generateTempPool(var_0_3.POP_PIERCE, arg_4_0._container, var_4_0, 0)
			arg_4_0._allPool[var_0_3.POP_CT_PIERCE] = arg_4_0.generateTempPool(var_0_3.POP_CT_PIERCE, arg_4_0._container, var_4_0, 0)

def var_0_4.Clear(arg_5_0):
	arg_5_0.pool.Recycle(arg_5_0)

def var_0_4.GetPop(arg_6_0, arg_6_1, arg_6_2, arg_6_3, arg_6_4, arg_6_5):
	local var_6_0, var_6_1 = var_0_3.getType(arg_6_1, arg_6_2, arg_6_3, arg_6_5)
	local var_6_2 = arg_6_0._allPool[var_6_0].GetObject()

	if var_6_0 != var_0_3.POP_MISS:
		var_6_2.SetText(arg_6_4)

	var_6_2.SetScale(var_6_1)

	return var_6_2

def var_0_4.GetScorePop(arg_7_0, arg_7_1):
	local var_7_0 = arg_7_0._allPool[var_0_3.POP_SCORE].GetObject()

	var_7_0.SetText(arg_7_1)

	return var_7_0

def var_0_4.generateTempPool(arg_8_0, arg_8_1, arg_8_2, arg_8_3, arg_8_4):
	return pg.LuaObPool.New(var_0_0.Battle.BattlePopNum, {
		template = arg_8_3.transform.Find(arg_8_1).gameObject,
		parentTF = arg_8_2,
		mgr = arg_8_0
	}, arg_8_4)

def var_0_4.Init(arg_9_0):
	return

def var_0_4.Recycle(arg_10_0):
	return

def var_0_4.IsScorePop(arg_11_0):
	return arg_11_0._score

def var_0_4.Dispose(arg_12_0):
	for iter_12_0, iter_12_1 in pairs(arg_12_0._allPool):
		iter_12_1.Dispose()

	arg_12_0._allPool = None

	Object.Destroy(arg_12_0._container.gameObject)

	arg_12_0._container = None
