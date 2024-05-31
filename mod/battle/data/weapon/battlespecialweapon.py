ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleSpecialWeapon", var_0_0.Battle.BattleWeaponUnit)

var_0_0.Battle.BattleSpecialWeapon = var_0_1
var_0_1.__name = "BattleSpecialWeapon"

def var_0_1.Ctor(arg_1_0):
	var_0_1.super.Ctor(arg_1_0)

def var_0_1.CheckPreCast(arg_2_0):
	local var_2_0 = arg_2_0._dataProxy.GetSeqCenter()
	local var_2_1 = arg_2_0._tmpData.bullet_ID[1]

	if not var_2_1:
		arg_2_0._castInfo = {
			weapon = arg_2_0
		}

		return True

	local var_2_2 = var_2_0.NewSeq("precast")
	local var_2_3 = var_0_0.Battle.NodeData.New(arg_2_0._host, {
		weapon = arg_2_0
	}, var_2_2)

	pg.NodeMgr.GetInstance().GenNode(var_2_3, pg.BattleNodesCfg[var_2_1], var_2_2)

	local var_2_4 = var_2_3.GetData()

	if var_2_4.targets[1] == None:
		return False

	arg_2_0._castInfo = var_2_4

	return True

def var_0_1.Fire(arg_3_0):
	assert(arg_3_0._castInfo != None, "需要指定施法信息，有特殊需求可默认指定为{ weapon = self }")

	local var_3_0 = arg_3_0._dataProxy.GetSeqCenter()
	local var_3_1 = arg_3_0._tmpData.bullet_ID[1]
	local var_3_2 = arg_3_0._castInfo
	local var_3_3 = var_3_0.NewSeq("cast")
	local var_3_4 = var_0_0.Battle.NodeData.New(arg_3_0._host, var_3_2, var_3_3)

	pg.NodeMgr.GetInstance().GenNode(var_3_4, pg.BattleNodesCfg[arg_3_0._tmpData.barrage_ID[1]], var_3_3)
	arg_3_0._host.SetCurNodeList(var_3_4.GetAllSeq())

	arg_3_0._currentState = arg_3_0.STATE_ATTACK
	arg_3_0._castInfo = None

	arg_3_0.CheckAndShake()
	var_3_3.Add(var_0_0.Battle.CallbackNode.New(function()
		arg_3_0.EnterCoolDown()))

	return True
