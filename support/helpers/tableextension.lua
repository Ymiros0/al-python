function table.indexof(arg_1_0, arg_1_1, arg_1_2)
	for iter_1_0 = arg_1_2 or 1, #arg_1_0 do
		if arg_1_0[iter_1_0] == arg_1_1 then
			return iter_1_0
		end
	end

	return false
end

function table.keyof(arg_2_0, arg_2_1)
	for iter_2_0, iter_2_1 in pairs(arg_2_0) do
		if iter_2_1 == arg_2_1 then
			return iter_2_0
		end
	end

	return nil
end

function table.removebyvalue(arg_3_0, arg_3_1, arg_3_2)
	local var_3_0 = 0
	local var_3_1 = 1
	local var_3_2 = #arg_3_0

	while var_3_1 <= var_3_2 do
		if arg_3_0[var_3_1] == arg_3_1 then
			table.remove(arg_3_0, var_3_1)

			var_3_0 = var_3_0 + 1
			var_3_1 = var_3_1 - 1
			var_3_2 = var_3_2 - 1

			if not arg_3_2 then
				break
			end
		end

		var_3_1 = var_3_1 + 1
	end

	return var_3_0
end

function table.removebykey(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_0[arg_4_1]

	arg_4_0[arg_4_1] = nil

	return var_4_0
end

function table.insertto(arg_5_0, arg_5_1, arg_5_2)
	arg_5_2 = checkint(arg_5_2)

	if arg_5_2 <= 0 then
		arg_5_2 = #arg_5_0 + 1
	end

	local var_5_0 = #arg_5_1

	for iter_5_0 = 0, var_5_0 - 1 do
		arg_5_0[iter_5_0 + arg_5_2] = arg_5_1[iter_5_0 + 1]
	end
end

function table.isEmpty(arg_6_0)
	if type(arg_6_0) == "table" then
		return next(arg_6_0) == nil
	end

	return true
end

function table.clear(arg_7_0)
	if arg_7_0 then
		for iter_7_0, iter_7_1 in pairs(arg_7_0) do
			arg_7_0[iter_7_0] = nil
		end
	end
end

function table.contains(arg_8_0, arg_8_1)
	if arg_8_0 == nil then
		return false
	end

	for iter_8_0, iter_8_1 in pairs(arg_8_0) do
		if iter_8_1 == arg_8_1 then
			return true
		end
	end

	return false
end

function table.equal(arg_9_0, arg_9_1)
	if type(arg_9_0) ~= type(arg_9_1) then
		return false
	end

	if type(arg_9_0) ~= "table" then
		return arg_9_0 == arg_9_1
	end

	if arg_9_0 == arg_9_1 then
		return true
	end

	for iter_9_0, iter_9_1 in pairs(arg_9_0) do
		if not table.equal(iter_9_1, arg_9_1[iter_9_0]) then
			return false
		end
	end

	for iter_9_2, iter_9_3 in pairs(arg_9_1) do
		if arg_9_0[iter_9_2] == nil then
			return false
		end
	end

	return true
end

function table.containsData(arg_10_0, arg_10_1)
	if arg_10_0 == nil then
		return false
	end

	for iter_10_0, iter_10_1 in pairs(arg_10_0) do
		if table.equal(iter_10_1, arg_10_1) then
			return true
		end
	end

	return false
end

function table.Foreach(arg_11_0, arg_11_1)
	for iter_11_0, iter_11_1 in pairs(arg_11_0) do
		arg_11_1(iter_11_0, iter_11_1)
	end
end

function table.Ipairs(arg_12_0, arg_12_1)
	for iter_12_0, iter_12_1 in ipairs(arg_12_0) do
		arg_12_1(iter_12_0, iter_12_1)
	end
end

function table.IpairsCArray(arg_13_0, arg_13_1)
	for iter_13_0 = 0, arg_13_0.Length - 1 do
		v = arg_13_0[iter_13_0]

		arg_13_1(iter_13_0, v)
	end
end

function table.SerialIpairsAsync(arg_14_0, arg_14_1, arg_14_2)
	if type(arg_14_0) ~= "table" then
		return
	end

	local var_14_0
	local var_14_1
	local var_14_2
	local var_14_3, var_14_4

	var_14_3, arg_14_0, var_14_4 = ipairs(arg_14_0)

	local var_14_5

	local function var_14_6()
		var_14_4, var_14_1 = var_14_3(arg_14_0, var_14_4)

		if var_14_4 == nil then
			if arg_14_2 then
				arg_14_2()
			end
		else
			arg_14_1(var_14_4, var_14_1, var_14_6)
		end
	end

	var_14_6()
end

function table.ParallelIpairsAsync(arg_16_0, arg_16_1, arg_16_2)
	if type(arg_16_0) ~= "table" then
		return
	end

	local var_16_0
	local var_16_1
	local var_16_2
	local var_16_3, var_16_4

	var_16_3, arg_16_0, var_16_4 = ipairs(arg_16_0)

	local var_16_5 = 0
	local var_16_6 = 1

	local function var_16_7()
		var_16_5 = var_16_5 + 1

		if var_16_5 == var_16_6 then
			existCall(arg_16_2)
		end
	end

	while true do
		local var_16_8

		var_16_4, var_16_8 = var_16_3(arg_16_0, var_16_4)

		if var_16_4 == nil then
			break
		end

		var_16_6 = var_16_6 + 1

		arg_16_1(var_16_4, var_16_8, var_16_7)
	end

	var_16_7()
end

function table.Find(arg_18_0, arg_18_1)
	for iter_18_0, iter_18_1 in pairs(arg_18_0) do
		if arg_18_1(iter_18_0, iter_18_1) then
			return iter_18_1, iter_18_0
		end
	end
end

function table.Checkout(arg_19_0, arg_19_1)
	for iter_19_0, iter_19_1 in pairs(arg_19_0) do
		local var_19_0 = arg_19_1(iter_19_0, iter_19_1)

		if var_19_0 ~= nil then
			return var_19_0
		end
	end
end

function table.getCount(arg_20_0)
	local var_20_0 = 0

	for iter_20_0, iter_20_1 in pairs(arg_20_0) do
		var_20_0 = var_20_0 + 1
	end

	return var_20_0
end

function table.merge(arg_21_0, arg_21_1)
	if not arg_21_1 or not arg_21_0 then
		return
	end

	for iter_21_0, iter_21_1 in pairs(arg_21_1) do
		arg_21_0[iter_21_0] = iter_21_1
	end

	return arg_21_0
end

function table.mergeArray(arg_22_0, arg_22_1, arg_22_2)
	local var_22_0 = {}
	local var_22_1 = {}

	local function var_22_2(arg_23_0)
		for iter_23_0, iter_23_1 in ipairs(arg_23_0) do
			if arg_22_2 and var_22_0[iter_23_1] then
				-- block empty
			else
				table.insert(var_22_1, iter_23_1)

				var_22_0[iter_23_1] = true
			end
		end
	end

	var_22_2(arg_22_0)
	var_22_2(arg_22_1)

	return var_22_1
end

function table.clean(arg_24_0)
	for iter_24_0 = #arg_24_0, 1, -1 do
		table.remove(arg_24_0, iter_24_0)
	end
end

function table.shallowCopy(arg_25_0)
	if type(arg_25_0) ~= "table" then
		return arg_25_0
	end

	local var_25_0 = {}

	for iter_25_0, iter_25_1 in pairs(arg_25_0) do
		var_25_0[iter_25_0] = iter_25_1
	end

	return var_25_0
end

function table.getIndex(arg_26_0, arg_26_1)
	for iter_26_0, iter_26_1 in ipairs(arg_26_0) do
		if arg_26_1(iter_26_1) then
			return iter_26_0
		end
	end
end

function table.map(arg_27_0, arg_27_1)
	local var_27_0 = {}

	for iter_27_0, iter_27_1 in pairs(arg_27_0) do
		var_27_0[iter_27_0] = arg_27_1(iter_27_1)
	end

	return var_27_0
end

function table.lastof(arg_28_0)
	return arg_28_0[#arg_28_0]
end

function table.dichotomyInsert(arg_29_0, arg_29_1, arg_29_2)
	arg_29_2 = defaultValue(arg_29_2, function(arg_30_0)
		return arg_30_0
	end)

	assert(type(arg_29_2) == "function")

	local var_29_0 = {}
	local var_29_1 = 1
	local var_29_2 = #arg_29_0
	local var_29_3

	local function var_29_4(arg_31_0)
		var_29_0[arg_31_0] = var_29_0[arg_31_0] or arg_29_2(arg_31_0)

		return var_29_0[arg_31_0]
	end

	while var_29_1 < var_29_2 do
		local var_29_5 = math.floor((var_29_1 + var_29_2) / 2)

		if var_29_4(arg_29_0[var_29_5]) < var_29_4(arg_29_1) then
			var_29_1 = var_29_5 + 1
		else
			var_29_2 = var_29_5
		end
	end

	table.insert(arg_29_0, var_29_1, arg_29_1)
end
