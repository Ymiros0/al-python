local var_0_0 = class("GuideUIFinder")

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0.queue = {}
end

function var_0_0.Search(arg_2_0, arg_2_1)
	table.insert(arg_2_0.queue, arg_2_1)

	if #arg_2_0.queue == 1 then
		arg_2_0:Start()
	end
end

function var_0_0.Start(arg_3_0)
	if #arg_3_0.queue <= 0 then
		return
	end

	local var_3_0 = arg_3_0.queue[1]

	arg_3_0:Clear()

	local function var_3_1()
		table.remove(arg_3_0.queue, 1)
		arg_3_0:Start()
	end

	if (var_3_0.delay or 0) > 0 then
		arg_3_0.delayTimer = Timer.New(function()
			arg_3_0:AddSearchTimer(var_3_0, var_3_1)
		end, var_3_0.delay)

		arg_3_0.delayTimer:Start()
	else
		arg_3_0:AddSearchTimer(var_3_0, var_3_1)
	end
end

local function var_0_1(arg_6_0, arg_6_1)
	local var_6_0 = {}

	for iter_6_0 = 0, arg_6_0.childCount - 1 do
		local var_6_1 = arg_6_0:GetChild(iter_6_0)
		local var_6_2 = var_6_1:GetComponent(typeof(LayoutElement))

		if not IsNil(var_6_1) and go(var_6_1).activeInHierarchy and (not var_6_2 or not var_6_2.ignoreLayout) then
			table.insert(var_6_0, var_6_1)
		end
	end

	return arg_6_1 and var_6_0[arg_6_1 + 1] or var_6_0[#var_6_0]
end

local function var_0_2(arg_7_0)
	local var_7_0 = GameObject.Find(arg_7_0.path)

	if var_7_0 and arg_7_0.childIndex and arg_7_0.childIndex == "#" then
		return var_0_1(var_7_0.transform)
	elseif var_7_0 and arg_7_0.childIndex and arg_7_0.childIndex == -999 then
		return var_0_1(var_7_0.transform, 0)
	elseif var_7_0 and arg_7_0.childIndex and arg_7_0.childIndex >= 0 then
		return var_0_1(var_7_0.transform, arg_7_0.childIndex)
	elseif var_7_0 then
		return var_7_0.transform
	end

	return nil
end

local function var_0_3(arg_8_0)
	local var_8_0 = var_0_2(arg_8_0)

	if var_8_0 ~= nil then
		for iter_8_0, iter_8_1 in ipairs(arg_8_0.conditionData) do
			local var_8_1 = var_8_0:Find(iter_8_1)

			if var_8_1 then
				return var_8_1
			end
		end
	end

	return nil
end

local function var_0_4(arg_9_0)
	local var_9_0

	if arg_9_0.conditionData then
		var_9_0 = var_0_3(arg_9_0)
	else
		var_9_0 = var_0_2(arg_9_0)
	end

	if var_9_0 then
		return var_9_0
	end

	return nil
end

function var_0_0.AddSearchTimer(arg_10_0, arg_10_1, arg_10_2)
	local var_10_0 = 20

	arg_10_0.timer = Timer.New(function()
		var_10_0 = var_10_0 - 1

		if var_10_0 <= 0 then
			arg_10_0:Clear()
			arg_10_2()
			print("should exist ui node : " .. arg_10_1.path)
			arg_10_1.callback(nil)

			return
		end

		local var_11_0 = var_0_4(arg_10_1)

		if var_11_0 then
			arg_10_0:Clear()
			arg_10_2()
			arg_10_1.callback(var_11_0)
		end
	end, 0.5, -1)

	arg_10_0.timer:Start()
	arg_10_0.timer.func()
end

function var_0_0.SearchWithoutDelay(arg_12_0, arg_12_1)
	local var_12_0 = var_0_2(arg_12_1)

	arg_12_0:Clear()
	arg_12_1.callback(var_12_0)
end

function var_0_0.Clear(arg_13_0)
	if arg_13_0.delayTimer then
		arg_13_0.delayTimer:Stop()

		arg_13_0.delayTimer = nil
	end

	if arg_13_0.timer then
		arg_13_0.timer:Stop()

		arg_13_0.timer = nil
	end
end

return var_0_0
