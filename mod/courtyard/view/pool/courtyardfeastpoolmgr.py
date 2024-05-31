local var_0_0 = class("CourtYardFeastPoolMgr", import(".CourtYardPoolMgr"))

def var_0_0.GenPool(arg_1_0, arg_1_1):
	local var_1_0 = var_0_0.super.GenPool(arg_1_0, arg_1_1)
	local var_1_1 = {
		"chengbao_aixin",
		"chengbao_xinxin",
		"chengbao_yinfu",
		"chengbao_ZZZ"
	}

	for iter_1_0, iter_1_1 in ipairs(var_1_1):
		table.insert(var_1_0, function(arg_2_0)
			ResourceMgr.Inst.getAssetAsync("Effect/" .. iter_1_1, "", typeof(Object), UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_3_0)
				if arg_1_0.exited:
					return

				if arg_3_0:
					arg_1_0.pools[iter_1_1] = CourtYardEffectPool.New(arg_1_1, arg_3_0, 0, 3, CourtYardConst.FEAST_EFFECT_TIME)

				arg_2_0()), True, True))

	return var_1_0

return var_0_0
