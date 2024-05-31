local var_0_0 = class("AtelierFormula", import("model.vo.BaseVO"))

var_0_0.TYPE = {
	TOOL = 3,
	EQUIP = 1,
	OTHER = 4,
	ITEM = 2
}

function var_0_0.bindConfigTable(arg_1_0)
	return pg.activity_ryza_recipe
end

function var_0_0.Ctor(arg_2_0, ...)
	var_0_0.super.Ctor(arg_2_0, ...)

	arg_2_0.times = arg_2_0.times or 0
end

function var_0_0.GetConfigID(arg_3_0)
	return arg_3_0.configId
end

function var_0_0.GetName(arg_4_0)
	return arg_4_0:getConfig("name")
end

function var_0_0.GetIconPath(arg_5_0)
	return arg_5_0:getConfig("icon")
end

function var_0_0.GetType(arg_6_0)
	return arg_6_0:getConfig("type")
end

function var_0_0.GetDesc(arg_7_0)
	return arg_7_0:getConfig("display")
end

function var_0_0.GetMaxLimit(arg_8_0)
	return arg_8_0:getConfig("item_num")
end

function var_0_0.SetUsedCount(arg_9_0, arg_9_1)
	arg_9_0.times = arg_9_1
end

function var_0_0.GetUsedCount(arg_10_0)
	return arg_10_0.times
end

function var_0_0.IsAvaliable(arg_11_0)
	return arg_11_0:GetMaxLimit() < 0 or arg_11_0:GetUsedCount() < arg_11_0:GetMaxLimit()
end

function var_0_0.GetProduction(arg_12_0)
	return arg_12_0:getConfig("item_id")
end

function var_0_0.GetCircleList(arg_13_0)
	return arg_13_0:getConfig("recipe_circle")
end

function var_0_0.IsFormualCanComposite(arg_14_0, arg_14_1)
	local var_14_0 = {}
	local var_14_1 = arg_14_1:GetItems()

	local function var_14_2(arg_15_0)
		local var_15_0 = var_14_0[arg_15_0:GetConfigID()] or Clone(var_14_1[arg_15_0:GetConfigID()])

		assert(var_15_0, "Using Unexist material")

		var_15_0.count = var_15_0.count - 1
		var_14_0[arg_15_0:GetConfigID()] = var_15_0
	end

	local var_14_3 = _.map(arg_14_0:GetCircleList(), function(arg_16_0)
		return AtelierFormulaCircle.New({
			configId = arg_16_0
		})
	end)

	if _.any(var_14_3, function(arg_17_0)
		if arg_17_0:GetType() == AtelierFormulaCircle.TYPE.BASE or arg_17_0:GetType() == AtelierFormulaCircle.TYPE.SAIREN then
			local var_17_0 = arg_17_0:GetLimitItemID()
			local var_17_1 = var_14_0[var_17_0] or var_14_1[var_17_0]

			if var_17_1 and var_17_1.count > 0 then
				var_14_2(var_17_1)
			else
				return true
			end
		end
	end) then
		return false
	end

	local var_14_4 = AtelierMaterial.bindConfigTable()

	local function var_14_5(arg_18_0)
		for iter_18_0, iter_18_1 in ipairs(var_14_4.all) do
			local var_18_0 = var_14_0[iter_18_1] or var_14_1[iter_18_1]

			if var_18_0 and var_18_0.count > 0 and arg_18_0:CanUseMaterial(var_18_0, arg_14_0) then
				var_14_2(var_18_0)

				return
			end
		end

		return true
	end

	if _.any(var_14_3, function(arg_19_0)
		if arg_19_0:GetType() == AtelierFormulaCircle.TYPE.NORMAL then
			return var_14_5(arg_19_0)
		end
	end) then
		return false
	end

	if _.any(var_14_3, function(arg_20_0)
		if arg_20_0:GetType() == AtelierFormulaCircle.TYPE.ANY then
			return var_14_5(arg_20_0)
		end
	end) then
		return false
	end

	return true
end

return var_0_0
