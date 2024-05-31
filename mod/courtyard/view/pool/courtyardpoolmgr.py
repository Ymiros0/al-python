local var_0_0 = class("CourtYardPoolMgr")

def var_0_0.Init(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.pools = {}
	arg_1_0.root = arg_1_1

	local var_1_0 = arg_1_0.GenPool(arg_1_1)

	parallelAsync(var_1_0, arg_1_2)

def var_0_0.GenPool(arg_2_0, arg_2_1):
	local var_2_0 = {
		"CourtYardFurniture",
		"CourtYardGrid",
		"CourtYardShip",
		"CourtYardWallGrid"
	}
	local var_2_1 = {
		{
			10,
			15
		},
		{
			4,
			8
		},
		{
			1,
			3
		},
		{
			2,
			8
		}
	}
	local var_2_2 = {
		"Heart"
	}
	local var_2_3 = {}

	for iter_2_0, iter_2_1 in ipairs(var_2_0):
		table.insert(var_2_3, function(arg_3_0)
			ResourceMgr.Inst.getAssetAsync("ui/" .. iter_2_1, "", typeof(Object), UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_4_0)
				if arg_2_0.exited:
					return

				local var_4_0 = var_2_1[iter_2_0]

				arg_2_0.pools[iter_2_1] = CourtYardPool.New(arg_2_1, arg_4_0, unpack(var_4_0))

				arg_3_0()), True, True))

	for iter_2_2, iter_2_3 in ipairs(var_2_2):
		table.insert(var_2_3, function(arg_5_0)
			ResourceMgr.Inst.getAssetAsync("Effect/" .. iter_2_3, "", typeof(Object), UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_6_0)
				if arg_2_0.exited:
					return

				if arg_6_0:
					arg_2_0.pools[iter_2_3] = CourtYardEffectPool.New(arg_2_1, arg_6_0, 0, 3)

				arg_5_0()), True, True))

	return var_2_3

def var_0_0.LoadAsset(arg_7_0, arg_7_1, arg_7_2):
	return

def var_0_0.GetFurniturePool(arg_8_0):
	return arg_8_0.pools.CourtYardFurniture

def var_0_0.GetShipPool(arg_9_0):
	return arg_9_0.pools.CourtYardShip

def var_0_0.GetGridPool(arg_10_0):
	return arg_10_0.pools.CourtYardGrid

def var_0_0.GetWallGridPool(arg_11_0):
	return arg_11_0.pools.CourtYardWallGrid

def var_0_0.GetHeartPool(arg_12_0):
	return arg_12_0.pools.Heart

def var_0_0.GetAiXinPool(arg_13_0):
	return arg_13_0.pools.chengbao_aixin

def var_0_0.GetXinXinPool(arg_14_0):
	return arg_14_0.pools.chengbao_xinxin

def var_0_0.GetYinFuPool(arg_15_0):
	return arg_15_0.pools.chengbao_yinfu

def var_0_0.GetZzzPool(arg_16_0):
	return arg_16_0.pools.chengbao_ZZZ

def var_0_0.Dispose(arg_17_0):
	for iter_17_0, iter_17_1 in pairs(arg_17_0.pools or {}):
		iter_17_1.Dispose()

	arg_17_0.pools = None
	arg_17_0.exited = True

return var_0_0
