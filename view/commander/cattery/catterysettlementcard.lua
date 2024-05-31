local var_0_0 = class("CatterySettlementCard")
local var_0_1 = 1

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0.tr = arg_1_1
	arg_1_0.go = arg_1_1.gameObject
	arg_1_0.emptyTF = findTF(arg_1_0.tr, "empty")
	arg_1_0.commanderTF = findTF(arg_1_0.tr, "commander")
	arg_1_0.nameTxt = findTF(arg_1_0.commanderTF, "name"):GetComponent(typeof(Text))
	arg_1_0.char = findTF(arg_1_0.commanderTF, "mask/char")
	arg_1_0.expTxt = findTF(arg_1_0.commanderTF, "exp/Text"):GetComponent(typeof(Text))
	arg_1_0.slider = findTF(arg_1_0.commanderTF, "exp_bar"):GetComponent(typeof(Slider))
	arg_1_0.levelTxt = findTF(arg_1_0.commanderTF, "level"):GetComponent(typeof(Text))
end

function var_0_0.Update(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0.cattery = arg_2_1
	arg_2_0.exp = arg_2_2

	local var_2_0 = arg_2_1:ExistCommander()

	if var_2_0 then
		arg_2_0:UpdateCommander()
	end

	setActive(arg_2_0.emptyTF, not var_2_0)
	setActive(arg_2_0.commanderTF, var_2_0)
end

function var_0_0.UpdateCommander(arg_3_0)
	local var_3_0 = arg_3_0.exp
	local var_3_1 = arg_3_0.cattery:GetCommander()
	local var_3_2 = arg_3_0:GetOldCommander(var_3_1, var_3_0)

	arg_3_0.oldCommander = var_3_2
	arg_3_0.commander = var_3_1

	arg_3_0:LoadCommander(var_3_1)

	arg_3_0.slider.value = var_3_2.exp / var_3_2:getNextLevelExp()
	arg_3_0.levelTxt.text = "LV." .. var_3_2:getLevel()
	arg_3_0.expTxt.text = var_3_2.exp .. "/" .. var_3_2:getNextLevelExp()
	arg_3_0.nameTxt.text = var_3_2:getName()
end

function var_0_0.InitAnim(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_0.commander:getLevel()
	local var_4_1 = arg_4_0.oldCommander:getLevel()
	local var_4_2 = arg_4_0.commander:getNextLevelExp()
	local var_4_3 = arg_4_0.commander.exp / var_4_2

	if var_4_1 < var_4_0 then
		table.insert(arg_4_1, function(arg_5_0)
			arg_4_0:DoUpgradeAnim(arg_5_0)
		end)
	else
		table.insert(arg_4_1, function(arg_6_0)
			arg_4_0:AddExpAnim(arg_4_0.slider.value, var_4_3, arg_4_0.oldCommander.exp, arg_4_0.commander.exp, var_4_2, arg_6_0)
		end)
	end
end

function var_0_0.Action(arg_7_0, arg_7_1)
	if not arg_7_0.commander then
		arg_7_1()

		return
	end

	local var_7_0 = {}

	arg_7_0:InitAnim(var_7_0)
	parallelAsync(var_7_0, arg_7_1)
end

function var_0_0.DoUpgradeAnim(arg_8_0, arg_8_1)
	local var_8_0 = arg_8_0.commander:getLevel()
	local var_8_1 = arg_8_0.oldCommander:getLevel()
	local var_8_2 = var_8_1
	local var_8_3 = arg_8_0.commander:getNextLevelExp()
	local var_8_4 = arg_8_0.commander.exp / var_8_3

	local function var_8_5()
		var_8_2 = var_8_2 + 1
		arg_8_0.levelTxt.text = "LV." .. var_8_2
	end

	local var_8_6 = {}
	local var_8_7 = var_8_1 + 1

	table.insert(var_8_6, function(arg_10_0)
		local var_10_0 = arg_8_0.oldCommander:getNextLevelExp()
		local var_10_1 = arg_8_0.oldCommander.exp

		arg_8_0:AddExpAnim(arg_8_0.slider.value, 1, var_10_1, var_10_0, var_10_0, function()
			var_8_5()
			arg_10_0()
		end)
	end)

	while var_8_7 ~= var_8_0 do
		var_8_7 = var_8_7 + 1

		table.insert(var_8_6, function(arg_12_0)
			local var_12_0 = arg_8_0.oldCommander:getConfigExp(var_8_2)

			arg_8_0:AddExpAnim(0, 1, 0, var_12_0, var_12_0, function()
				var_8_5()
				arg_12_0()
			end)
		end)
	end

	table.insert(var_8_6, function(arg_14_0)
		arg_8_0:AddExpAnim(0, var_8_4, 0, arg_8_0.commander.exp, var_8_3, arg_14_0)
	end)
	seriesAsync(var_8_6, arg_8_1)
end

function var_0_0.LoadCommander(arg_15_0, arg_15_1)
	arg_15_0:ReturnCommander()

	arg_15_0.painting = arg_15_1:getPainting()

	setCommanderPaintingPrefab(arg_15_0.char, arg_15_0.painting, "result")
end

function var_0_0.ReturnCommander(arg_16_0)
	if arg_16_0.painting then
		retCommanderPaintingPrefab(arg_16_0.char, arg_16_0.painting)

		arg_16_0.painting = nil
	end
end

function var_0_0.Clear(arg_17_0)
	if LeanTween.isTweening(go(arg_17_0.slider)) then
		LeanTween.cancel(go(arg_17_0.slider))
	end

	if LeanTween.isTweening(go(arg_17_0.expTxt)) then
		LeanTween.cancel(go(arg_17_0.expTxt))
	end
end

function var_0_0.Dispose(arg_18_0)
	arg_18_0:Clear()
	arg_18_0:ReturnCommander()
end

function var_0_0.GetOldCommander(arg_19_0, arg_19_1, arg_19_2)
	local var_19_0 = Clone(arg_19_1)

	var_19_0:ReduceExp(arg_19_2)

	return var_19_0
end

function var_0_0.AddExpAnim(arg_20_0, arg_20_1, arg_20_2, arg_20_3, arg_20_4, arg_20_5, arg_20_6)
	parallelAsync({
		function(arg_21_0)
			LeanTween.value(go(arg_20_0.slider), arg_20_1, arg_20_2, var_0_1):setOnUpdate(System.Action_float(function(arg_22_0)
				arg_20_0.slider.value = arg_22_0
			end)):setOnComplete(System.Action(arg_21_0))
		end,
		function(arg_23_0)
			LeanTween.value(go(arg_20_0.expTxt), arg_20_3, arg_20_4, var_0_1):setOnUpdate(System.Action_float(function(arg_24_0)
				local var_24_0 = math.ceil(arg_24_0)

				arg_20_0.expTxt.text = "<color=#94d53eFF>" .. var_24_0 .. "/</color>" .. "<color=" .. arg_20_0:GetColor() .. ">" .. arg_20_5 .. "</color>"
			end)):setOnComplete(System.Action(arg_23_0))
		end
	}, function()
		if arg_20_6 then
			arg_20_6()
		end
	end)
end

function var_0_0.GetColor(arg_26_0)
	return "#9f9999"
end

return var_0_0
