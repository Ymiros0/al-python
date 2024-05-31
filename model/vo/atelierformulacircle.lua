local var_0_0 = class("AtelierFormulaCircle", import("model.vo.BaseVO"))

var_0_0.TYPE = {
	BASE = 1,
	SAIREN = 3,
	NORMAL = 2,
	ANY = 4
}
var_0_0.ELEMENT_TYPE = {
	PYRO = 1,
	SAIREN = 5,
	ELECTRO = 3,
	ANEMO = 4,
	CRYO = 2,
	ANY = 0
}
var_0_0.ELEMENT_NAME = {}

for iter_0_0, iter_0_1 in pairs(var_0_0.ELEMENT_TYPE) do
	var_0_0.ELEMENT_NAME[iter_0_1] = iter_0_0
end

var_0_0.ELEMENT_RING_COLOR = {
	[var_0_0.ELEMENT_TYPE.ANY] = "FFFED5",
	[var_0_0.ELEMENT_TYPE.PYRO] = "F74F41",
	[var_0_0.ELEMENT_TYPE.CRYO] = "64CAFF",
	[var_0_0.ELEMENT_TYPE.ELECTRO] = "FFDD3F",
	[var_0_0.ELEMENT_TYPE.ANEMO] = "B0E860",
	[var_0_0.ELEMENT_TYPE.SAIREN] = "AF97FF"
}

function var_0_0.bindConfigTable(arg_1_0)
	return pg.activity_ryza_recipe_circle
end

function var_0_0.GetConfigID(arg_2_0)
	return arg_2_0.configId
end

function var_0_0.GetIconPath(arg_3_0)
	return arg_3_0:getConfig("icon")
end

function var_0_0.GetType(arg_4_0)
	return arg_4_0:getConfig("type")
end

function var_0_0.GetProp(arg_5_0)
	return arg_5_0:getConfig("prop")
end

function var_0_0.GetElement(arg_6_0)
	if arg_6_0:GetType() == var_0_0.TYPE.SAIREN then
		return var_0_0.ELEMENT_TYPE.SAIREN
	elseif arg_6_0:GetType() == var_0_0.TYPE.ANY then
		return var_0_0.ELEMENT_TYPE.ANY
	end

	return arg_6_0:GetProp()
end

function var_0_0.GetElementName(arg_7_0)
	return var_0_0.ELEMENT_NAME[arg_7_0:GetElement()]
end

function var_0_0.GetRingElement(arg_8_0, arg_8_1)
	local var_8_0 = arg_8_0:GetElement()

	if arg_8_0:GetType() == var_0_0.TYPE.ANY and arg_8_1 then
		if arg_8_1:GetType() == AtelierMaterial.TYPE.SAIREN then
			var_8_0 = var_0_0.ELEMENT_TYPE.SAIREN
		else
			var_8_0 = arg_8_1:GetProps()[1]
		end
	end

	return var_8_0
end

function var_0_0.GetElementRingColor(arg_9_0, arg_9_1)
	local var_9_0 = var_0_0.ELEMENT_RING_COLOR[arg_9_0:GetRingElement(arg_9_1)]

	return SummerFeastScene.TransformColor(var_9_0)
end

function var_0_0.GetLevel(arg_10_0)
	return arg_10_0:getConfig("prop_level")
end

function var_0_0.GetLimitItemID(arg_11_0)
	return arg_11_0:getConfig("ryza_item_id")
end

function var_0_0.GetNeighbors(arg_12_0)
	return arg_12_0:getConfig("circle_connect")
end

function var_0_0.GetFormulaId(arg_13_0)
	return arg_13_0:getConfig("recipe_id")
end

function var_0_0.CanUseMaterial(arg_14_0, arg_14_1, arg_14_2)
	local function var_14_0()
		if arg_14_2:GetProduction()[1] ~= DROP_TYPE_RYZA_DROP then
			return false
		end

		if arg_14_2:GetProduction()[2] == arg_14_1:GetConfigID() then
			return true
		end

		local var_15_0 = AtelierMaterial.New({
			configId = arg_14_2:GetProduction()[2]
		})

		return var_15_0:GetType() == AtelierMaterial.TYPE.NEUTRALIZER and arg_14_1:GetType() == AtelierMaterial.TYPE.NEUTRALIZER and var_15_0:GetLevel() == arg_14_1:GetLevel()
	end

	if arg_14_0:GetType() == var_0_0.TYPE.BASE or arg_14_0:GetType() == var_0_0.TYPE.SAIREN then
		return arg_14_0:GetLimitItemID() == arg_14_1:GetConfigID()
	elseif arg_14_0:GetType() == var_0_0.TYPE.NORMAL then
		if arg_14_1:GetType() ~= AtelierMaterial.TYPE.NORMAL and arg_14_1:GetType() ~= AtelierMaterial.TYPE.NEUTRALIZER then
			return false
		end

		if not table.contains(arg_14_1:GetProps(), arg_14_0:GetElement()) then
			return false
		end

		if var_14_0() then
			return false
		end

		return arg_14_1:GetLevel() == arg_14_0:GetLevel()
	elseif arg_14_0:GetType() == var_0_0.TYPE.ANY then
		if arg_14_1:GetType() ~= AtelierMaterial.TYPE.NORMAL and arg_14_1:GetType() ~= AtelierMaterial.TYPE.NEUTRALIZER and arg_14_1:GetType() ~= AtelierMaterial.TYPE.SAIREN then
			return false
		end

		if var_14_0() then
			return false
		end

		return arg_14_1:GetLevel() == arg_14_0:GetLevel()
	end
end

return var_0_0
