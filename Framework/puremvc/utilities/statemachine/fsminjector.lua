local var_0_0 = import("...patterns.observer.Notifier")
local var_0_1 = class("FSMInjector", var_0_0)
local var_0_2 = import(".StateMachine")
local var_0_3 = import(".State")

function var_0_1.Ctor(arg_1_0, arg_1_1)
	var_0_1.super.Ctor(arg_1_0)

	arg_1_0.fsm = arg_1_1
end

function var_0_1.inject(arg_2_0)
	local var_2_0 = var_0_2.New()
	local var_2_1 = arg_2_0:getStates()

	for iter_2_0, iter_2_1 in ipairs(var_2_1) do
		var_2_0:registerState(iter_2_1, arg_2_0:isInitial(iter_2_1.name))
	end

	arg_2_0.facade:registerMediator(var_2_0)
end

function var_0_1.getStates(arg_3_0)
	if arg_3_0.stateList == nil then
		arg_3_0.stateList = {}

		local var_3_0 = arg_3_0.fsm.state or {}

		for iter_3_0, iter_3_1 in ipairs(var_3_0) do
			local var_3_1 = arg_3_0:createState(iter_3_1)

			table.insert(arg_3_0.stateList, var_3_1)
		end
	end

	return arg_3_0.stateList
end

function var_0_1.createState(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_1["@name"]
	local var_4_1 = arg_4_1["@entering"]
	local var_4_2 = arg_4_1["@exiting"]
	local var_4_3 = arg_4_1["@changed"]
	local var_4_4 = var_0_3.New(var_4_0, var_4_1, var_4_2, var_4_3)
	local var_4_5 = arg_4_1.transition or {}

	for iter_4_0, iter_4_1 in ipairs(var_4_5) do
		var_4_4:defineTrans(iter_4_1["@action"], iter_4_1["@target"])
	end

	return var_4_4
end

function var_0_1.isInitial(arg_5_0, arg_5_1)
	return arg_5_1 == arg_5_0.fsm["@initial"]
end

return var_0_1
