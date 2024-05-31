local var_0_0 = {}

var_0_0.__cname = "ResponsableTree"
var_0_0.__ctype = 2

local var_0_1 = {
	__mode = "kv"
}

var_0_0.InstanceMap = setmetatable({}, var_0_1)
var_0_0.DATA_ADD = 1
var_0_0.DATA_UPDATE = 0
var_0_0.DATA_DELETE = -1

function var_0_0.__index(arg_1_0, arg_1_1)
	return var_0_0[arg_1_1] or arg_1_0._properties[arg_1_1]
end

local var_0_2 = 1000
local var_0_3 = 0

function var_0_0.__newindex(arg_2_0, arg_2_1, arg_2_2)
	local var_2_0 = rawget(arg_2_0._properties, arg_2_1)

	if var_2_0 ~= arg_2_2 and not arg_2_0._quiet then
		local var_2_1 = var_2_0
		local var_2_2 = var_0_0.CreateShell(arg_2_2, arg_2_0)

		arg_2_0._properties[arg_2_1] = var_2_2

		local var_2_3 = var_0_0.DATA_UDPATE

		var_2_3 = var_2_1 == nil and var_0_0.DATA_ADD or var_2_3
		var_2_3 = var_2_2 == nil and var_0_0.DATA_DELETE or var_2_3

		if type(var_2_1) == "table" and var_2_1.class == var_0_0 then
			var_2_1._parents[arg_2_0] = nil
		end

		if type(var_2_2) == "table" and var_2_2.class == var_0_0 then
			var_2_2._parents[arg_2_0] = true
		end

		var_0_3 = 0

		arg_2_0:Response(arg_2_0, {
			arg_2_1
		}, {
			var_2_0,
			var_2_3
		})
	end
end

function var_0_0.Response(arg_3_0, arg_3_1, arg_3_2, arg_3_3)
	if var_0_3 >= var_0_2 then
		errorMsg("Exceed the Iterate Limitation, Might have inherit loop")

		return
	end

	var_0_3 = var_0_3 + 1

	local var_3_0 = not next(arg_3_0._listeners)

	if not var_3_0 then
		local var_3_1 = table.concat(arg_3_2, ".")

		for iter_3_0, iter_3_1 in ipairs(arg_3_0._listeners) do
			local var_3_2 = iter_3_1.settings

			for iter_3_2, iter_3_3 in ipairs(iter_3_1.keys) do
				local var_3_3 = "^" .. iter_3_3 .. "$"
				local var_3_4 = string.match(var_3_1, var_3_3)

				if not var_3_4 and (not var_3_2 or not var_3_2.strict) then
					local var_3_5 = "^" .. iter_3_3 .. "%."

					var_3_4 = string.match(var_3_1, var_3_5)
				end

				if var_3_4 then
					var_3_0 = var_3_0 or var_3_2 and not var_3_2.NoAffectOnTransparent

					arg_3_0:DoAction(iter_3_1, arg_3_2, arg_3_3)

					break
				end
			end
		end
	end

	if not var_3_0 or not next(arg_3_0._parents) then
		return
	end

	local var_3_6 = table.getCount(arg_3_0._parents)

	for iter_3_4, iter_3_5 in pairs(arg_3_0._parents) do
		var_3_6 = var_3_6 - 1

		local var_3_7 = var_3_6 > 0 and Clone(arg_3_2) or arg_3_2

		table.insert(var_3_7, 1, table.keyof(iter_3_4:GetRawData(), arg_3_0))
		iter_3_4:Response(arg_3_1, var_3_7, arg_3_3)
	end
end

function var_0_0.DoAction(arg_4_0, arg_4_1, arg_4_2, arg_4_3)
	local var_4_0 = {}
	local var_4_1 = #arg_4_1.keys

	for iter_4_0, iter_4_1 in ipairs(arg_4_1.keys) do
		local var_4_2 = string.split(iter_4_1, ".") or {}
		local var_4_3 = arg_4_0
		local var_4_4 = 0

		while var_4_3 and var_4_4 < #var_4_2 do
			var_4_4 = var_4_4 + 1
			var_4_3 = var_4_3[var_4_2[var_4_4]]
		end

		var_4_0[iter_4_0] = var_4_3
	end

	if arg_4_1.settings and arg_4_1.settings.useOldRef then
		local var_4_5 = table.shallowCopy(var_4_0)

		for iter_4_2, iter_4_3 in ipairs(arg_4_1.keys) do
			local var_4_6 = string.split(iter_4_3, ".") or {}

			if table.equal(var_4_6, arg_4_2) then
				var_4_5[iter_4_2] = arg_4_3[1]

				break
			end
		end

		arg_4_1.listener(var_4_1, var_4_0, var_4_5, arg_4_3[2])
	else
		arg_4_1.listener(unpack(var_4_0, 1, var_4_1))
	end
end

function var_0_0.PropertyChange(arg_5_0, arg_5_1)
	var_0_3 = 0

	arg_5_0:Response(arg_5_0, {
		arg_5_1
	}, {
		arg_5_0[arg_5_1],
		var_0_0.DATA_UPDATE
	})
end

function var_0_0.CreateShell(arg_6_0, arg_6_1)
	if type(arg_6_0) ~= "table" or arg_6_0.class == var_0_0 then
		return arg_6_0
	end

	if var_0_0.InstanceMap[arg_6_0] then
		if arg_6_1 then
			var_0_0.InstanceMap[arg_6_0]._parents[arg_6_1] = true
		end

		return var_0_0.InstanceMap[arg_6_0]
	end

	local var_6_0 = {
		_quiet = false,
		class = var_0_0,
		_properties = {},
		_listeners = {},
		_parents = {}
	}

	if arg_6_1 then
		var_6_0._parents[arg_6_1] = true
	end

	setmetatable(var_6_0, var_0_0)
	setmetatable(var_6_0._parents, var_0_1)

	var_0_0.InstanceMap[arg_6_0] = var_6_0

	local var_6_1 = getmetatable(arg_6_0)

	if var_6_1 then
		setmetatable(var_6_0._properties, var_6_1)
	end

	for iter_6_0, iter_6_1 in pairs(arg_6_0) do
		if type(iter_6_1) == "table" and iter_6_1.class ~= var_0_0 then
			rawset(var_6_0._properties, iter_6_0, var_0_0.CreateShell(iter_6_1, var_6_0))
		else
			rawset(var_6_0._properties, iter_6_0, iter_6_1)
		end
	end

	return var_6_0
end

function var_0_0.AddRawListener(arg_7_0, arg_7_1, arg_7_2, arg_7_3)
	local var_7_0 = {
		keys = arg_7_1,
		listener = arg_7_2,
		settings = arg_7_3
	}

	table.insert(arg_7_0._listeners, var_7_0)

	return function()
		return table.removebyvalue(arg_7_0._listeners, var_7_0)
	end
end

function var_0_0.GetRawData(arg_9_0, arg_9_1)
	return arg_9_1 and arg_9_0._properties[arg_9_1] or arg_9_0._properties
end

function var_0_0.SetRawData(arg_10_0, arg_10_1, arg_10_2)
	arg_10_0._properties[arg_10_1] = arg_10_2
end

function var_0_0.EnterQuietMode(arg_11_0)
	arg_11_0._quiet = true
end

function var_0_0.ExitQuietMode(arg_12_0)
	arg_12_0._quiet = false
end

function var_0_0.insert(arg_13_0, ...)
	if select("#", ...) > 1 then
		local var_13_0 = select(1, ...)
		local var_13_1 = select(2, ...)

		assert(var_13_0 ~= nil, "invalid param 1 for insert, expect number but got " .. type(var_13_0))

		if var_13_1 == nil then
			return
		end

		local var_13_2 = #arg_13_0._properties
		local var_13_3 = arg_13_0._properties[var_13_0]
		local var_13_4

		arg_13_0[var_13_0] = var_13_1

		for iter_13_0 = var_13_0 + 1, var_13_2 + 1 do
			var_13_3, arg_13_0[iter_13_0] = arg_13_0._properties[iter_13_0], var_13_3
		end
	else
		local var_13_5 = select(1, ...)

		if var_13_5 == nil then
			return
		end

		arg_13_0[#arg_13_0._properties + 1] = var_13_5
	end
end

function var_0_0.remove(arg_14_0, arg_14_1)
	if arg_14_1 == 0 then
		return
	end

	local var_14_0 = #arg_14_0._properties

	if var_14_0 == 0 or var_14_0 < arg_14_1 or arg_14_1 + var_14_0 <= 0 then
		return
	end

	arg_14_1 = arg_14_1 or var_14_0
	arg_14_1 = arg_14_1 > 0 and arg_14_1 or var_14_0 + arg_14_1

	local var_14_1 = arg_14_0[arg_14_1]

	arg_14_0[arg_14_1] = nil

	for iter_14_0 = arg_14_1, var_14_0 - 1 do
		arg_14_0[iter_14_0] = arg_14_0._properties[iter_14_0 + 1]
	end

	arg_14_0[var_14_0] = nil

	return var_14_1
end

return var_0_0
