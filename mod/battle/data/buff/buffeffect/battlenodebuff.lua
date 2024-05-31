ys = ys or {}

local var_0_0 = class("BattleNodeBuff", ys.Battle.BattleBuffEffect)

ys.Battle.BattleNodeBuff = var_0_0
var_0_0.__name = "BattleNodeBuff"

function var_0_0.Ctor(arg_1_0, arg_1_1)
	var_0_0.super.Ctor(arg_1_0, arg_1_1)
end

function var_0_0.SetArgs(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0._rate = arg_2_0._tempData.arg_list.rate
end

function var_0_0.onFire(arg_3_0, arg_3_1, arg_3_2)
	if not ys.Battle.BattleFormulas.IsHappen(arg_3_0._rate) then
		return
	end

	local var_3_0 = arg_3_0._tempData.arg_list
	local var_3_1 = var_3_0.node
	local var_3_2 = var_3_0.weapon
	local var_3_3 = ys.Battle.BattleDataProxy.GetInstance():GetSeqCenter()

	for iter_3_0, iter_3_1 in ipairs(arg_3_1:GetAutoWeapons()) do
		if iter_3_1:GetWeaponId() == var_3_2 then
			local var_3_4 = var_3_3:NewSeq("buff" .. arg_3_0._id)
			local var_3_5 = ys.Battle.NodeData.New(arg_3_1, {
				weapon = iter_3_1
			}, var_3_4)

			pg.NodeMgr.GetInstance():GenNode(var_3_5, pg.BattleNodesCfg[var_3_1], var_3_4)

			break
		end
	end
end
