ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffAddAircraftTag = class("BattleBuffAddAircraftTag", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffAddAircraftTag.__name = "BattleBuffAddAircraftTag"

local var_0_1 = var_0_0.Battle.BattleBuffAddAircraftTag

function var_0_1.Ctor(arg_1_0, arg_1_1)
	var_0_1.super.Ctor(arg_1_0, arg_1_1)
end

function var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0._labelTag = arg_2_0._tempData.arg_list.tag_list
end

function var_0_1.onAircraftCreate(arg_3_0, arg_3_1, arg_3_2, arg_3_3)
	if not arg_3_0:equipIndexRequire(arg_3_3.equipIndex) then
		return
	end

	local var_3_0 = arg_3_3.aircraft

	for iter_3_0, iter_3_1 in ipairs(arg_3_0._labelTag) do
		if string.find(iter_3_1, "^[NT]_%d+$") then
			pg.TipsMgr.GetInstance():ShowTips(">>BattleBuffAddAircraftTag<<不允许使用'N_'或'T_'标签")
		else
			var_3_0:AddLabelTag(iter_3_1)
		end
	end
end
