local var_0_0 = class("CourtYardStoreyComposeChecker")

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0.storey = arg_1_1
	arg_1_0.config = pg.furniture_compose_template
	arg_1_0.list = {}
end

function var_0_0.Check(arg_2_0)
	for iter_2_0, iter_2_1 in ipairs(arg_2_0.config.all) do
		if arg_2_0:IsMatch(arg_2_0.config[iter_2_1].furniture_ids) then
			arg_2_0:Add(iter_2_1)
		else
			arg_2_0:Remove(iter_2_1)
		end
	end
end

function var_0_0.Add(arg_3_0, arg_3_1)
	if not table.contains(arg_3_0.list, arg_3_1) then
		table.insert(arg_3_0.list, arg_3_1)
		arg_3_0.storey:DispatchEvent(CourtYardEvent.ON_ADD_EFFECT, arg_3_0.config[arg_3_1].effect_name)
	end
end

function var_0_0.Remove(arg_4_0, arg_4_1)
	if table.contains(arg_4_0.list, arg_4_1) then
		table.removebyvalue(arg_4_0.list, arg_4_1)
		arg_4_0.storey:DispatchEvent(CourtYardEvent.ON_REMOVE_EFFECT, arg_4_0.config[arg_4_1].effect_name)
	end
end

function var_0_0.IsMatch(arg_5_0, arg_5_1)
	local function var_5_0(arg_6_0)
		return arg_5_0.storey.furnitures[arg_6_0] ~= nil or arg_5_0.storey.wallPaper and arg_5_0.storey.wallPaper.configId == arg_6_0 or arg_5_0.storey.floorPaper and arg_5_0.storey.floorPaper.configId == arg_6_0
	end

	return _.all(arg_5_1, var_5_0)
end

function var_0_0.Dispose(arg_7_0)
	arg_7_0.config = nil
	arg_7_0.list = nil
	arg_7_0.storey = nil
end

return var_0_0
