local var_0_0 = class("CourtYardEffectAgent", import(".CourtYardAgent"))

function var_0_0.Ctor(arg_1_0, arg_1_1)
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.effects = {}
	arg_1_0.counts = {}
end

function var_0_0.EnableEffect(arg_2_0, arg_2_1)
	if not arg_2_1 then
		return
	end

	if arg_2_0.effects[arg_2_1] then
		arg_2_0.counts[arg_2_1] = (arg_2_0.counts[arg_2_1] or 0) + 1

		return
	end

	pg.UIMgr.GetInstance():LoadingOn()
	PoolMgr.GetInstance():GetPrefab("ui/" .. arg_2_1, arg_2_1, true, function(arg_3_0)
		pg.UIMgr.GetInstance():LoadingOff()

		if not arg_2_0.effects or arg_2_0.effects[arg_2_1] then
			PoolMgr.GetInstance():ReturnPrefab("ui/" .. arg_2_1, arg_2_1, arg_3_0)

			return
		end

		arg_3_0.name = arg_2_1

		setParent(arg_3_0, arg_2_0.effectContainer)
		setActive(arg_3_0, true)

		arg_2_0.effects[arg_2_1] = arg_3_0
		arg_2_0.counts[arg_2_1] = (arg_2_0.counts[arg_2_1] or 0) + 1
	end)
end

function var_0_0.DisableEffect(arg_4_0, arg_4_1)
	if not arg_4_0.effects[arg_4_1] then
		return
	end

	arg_4_0.counts[arg_4_1] = (arg_4_0.counts[arg_4_1] or 0) - 1

	if arg_4_0.counts[arg_4_1] <= 0 then
		local var_4_0 = findTF(arg_4_0.effectContainer, arg_4_1)

		if var_4_0 then
			PoolMgr.GetInstance():ReturnPrefab("ui/" .. arg_4_1, arg_4_1, var_4_0.gameObject)

			arg_4_0.effects[arg_4_1] = nil
		end
	end
end

function var_0_0.Dispose(arg_5_0)
	for iter_5_0, iter_5_1 in pairs(arg_5_0.effects) do
		PoolMgr.GetInstance():ReturnPrefab("ui/" .. iter_5_0, iter_5_0, iter_5_1)
	end

	arg_5_0.effects = nil
	arg_5_0.counts = nil
end

return var_0_0
