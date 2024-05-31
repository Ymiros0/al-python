local var_0_0 = class("AtelierActivity", import(".VirtualBagActivity"))

function var_0_0.Ctor(arg_1_0, ...)
	var_0_0.super.Ctor(arg_1_0, ...)

	arg_1_0.items = {}
	arg_1_0.completeAllTools = false
	arg_1_0.slots = _.map({
		1,
		2,
		3,
		4,
		5
	}, function()
		return {
			0,
			0
		}
	end)

	arg_1_0:InitAllFormulas()
end

function var_0_0.GetItems(arg_3_0)
	return arg_3_0.items
end

function var_0_0.InitItems(arg_4_0, arg_4_1)
	_.each(arg_4_1, function(arg_5_0)
		local var_5_0 = arg_5_0.key
		local var_5_1 = arg_5_0.value

		arg_4_0.items[var_5_0] = arg_4_0.items[var_5_0] or AtelierMaterial.New({
			configId = var_5_0
		})
		arg_4_0.items[var_5_0].count = arg_4_0.items[var_5_0].count + var_5_1
	end)
end

function var_0_0.GetSlots(arg_6_0)
	return arg_6_0.slots
end

function var_0_0.UpdateBuffSlots(arg_7_0, arg_7_1)
	_.each(arg_7_1, function(arg_8_0)
		arg_7_0.slots[arg_8_0.pos] = {
			arg_8_0.itemid,
			arg_8_0.itemnum
		}
	end)
end

function var_0_0.AddItem(arg_9_0, arg_9_1)
	local var_9_0 = arg_9_1:GetConfigID()
	local var_9_1 = arg_9_1.count

	arg_9_0.items[var_9_0] = arg_9_0.items[var_9_0] or AtelierMaterial.New({
		configId = var_9_0
	})
	arg_9_0.items[var_9_0].count = arg_9_0.items[var_9_0].count + var_9_1
end

function var_0_0.GetItemById(arg_10_0, arg_10_1)
	return arg_10_0.items[arg_10_1]
end

function var_0_0.subItemCount(arg_11_0, arg_11_1, arg_11_2)
	if not arg_11_0.items[arg_11_1] then
		return
	end

	arg_11_0.items[arg_11_1].count = math.max(0, arg_11_0.items[arg_11_1].count - arg_11_2)
end

function var_0_0.GetAllVitems(arg_12_0)
	return table.map(arg_12_0:GetItems(), function(arg_13_0)
		return arg_13_0.count
	end)
end

function var_0_0.getVitemNumber(arg_14_0, arg_14_1)
	local var_14_0 = arg_14_0:GetItemById(arg_14_1)

	return var_14_0 and var_14_0.count or 0
end

function var_0_0.addVitemNumber(arg_15_0, arg_15_1, arg_15_2)
	arg_15_0:AddItem(AtelierMaterial.New({
		configId = arg_15_1,
		count = arg_15_2
	}))
end

function var_0_0.subVitemNumber(arg_16_0, arg_16_1, arg_16_2)
	arg_16_0:subItemCount(arg_16_1, arg_16_2)
end

function var_0_0.GetFormulas(arg_17_0)
	return arg_17_0.formulas
end

function var_0_0.InitAllFormulas(arg_18_0)
	arg_18_0.formulas = {}

	_.each(pg.activity_ryza_recipe.all, function(arg_19_0)
		arg_18_0.formulas[arg_19_0] = AtelierFormula.New({
			configId = arg_19_0
		})
	end)
end

function var_0_0.InitFormulaUseCounts(arg_20_0, arg_20_1)
	_.each(arg_20_1, function(arg_21_0)
		local var_21_0 = arg_21_0.key
		local var_21_1 = arg_21_0.value

		arg_20_0.formulas[var_21_0]:SetUsedCount(var_21_1)
	end)
	arg_20_0:CheckCompleteAllTool()
end

function var_0_0.AddFormulaUseCount(arg_22_0, arg_22_1, arg_22_2)
	arg_22_0.formulas[arg_22_1]:SetUsedCount(arg_22_0.formulas[arg_22_1]:GetUsedCount() + arg_22_2)
	arg_22_0:CheckCompleteAllTool()
end

function var_0_0.CheckCompleteAllTool(arg_23_0)
	if arg_23_0.completeAllTools then
		return
	end

	arg_23_0.completeAllTools = _.all(_.values(arg_23_0.formulas), function(arg_24_0)
		if arg_24_0:GetType() ~= AtelierFormula.TYPE.TOOL then
			return true
		end

		return not arg_24_0:IsAvaliable()
	end)
end

function var_0_0.IsCompleteAllTools(arg_25_0)
	return arg_25_0.completeAllTools
end

function var_0_0.IsActivityBuffMap(arg_26_0)
	return ChapterConst.IsAtelierMap(arg_26_0) and arg_26_0:getMapType() > Map.ACTIVITY_EASY
end

return var_0_0
