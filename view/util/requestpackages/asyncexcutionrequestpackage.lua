local var_0_0 = class("AsyncExcutionRequestPackage", import(".RequestPackage"))

function var_0_0.__call(arg_1_0, ...)
	if arg_1_0.stopped then
		return
	end

	if not arg_1_0.funcs or #arg_1_0.funcs == 0 then
		return
	end

	arg_1_0:Excute(...)
end

function var_0_0.Resume(arg_2_0)
	arg_2_0.suspended = nil

	if arg_2_0.ready then
		if arg_2_0.resume then
			local var_2_0 = arg_2_0.resume

			arg_2_0.resume = nil

			arg_2_0:Excute(unpack(var_2_0.params, var_2_0.paramLength))
		else
			arg_2_0:Excute()
		end
	end
end

function var_0_0.Suspend(arg_3_0)
	arg_3_0.suspended = true
end

function var_0_0.Ctor(arg_4_0, arg_4_1)
	arg_4_0.ready = true
	arg_4_0.funcs = arg_4_1
	arg_4_0.suspended = nil
	arg_4_0.resume = nil
end

function var_0_0.Insert(arg_5_0, arg_5_1)
	table.insert(arg_5_0.funcs, arg_5_1)
end

function var_0_0.Excute(arg_6_0, ...)
	assert(arg_6_0.ready)

	if not arg_6_0.ready then
		return
	end

	local var_6_0

	local function var_6_1(...)
		if arg_6_0.stopped then
			return
		end

		if arg_6_0.suspended or not arg_6_0.funcs or not (#arg_6_0.funcs > 0) then
			arg_6_0.resume = {
				params = {
					...
				},
				paramLength = select("#", ...)
			}
			arg_6_0.ready = true

			return
		end

		arg_6_0.ready = nil

		table.remove(arg_6_0.funcs, 1)(var_6_1, ...)
	end

	var_6_1(...)
end

return var_0_0
