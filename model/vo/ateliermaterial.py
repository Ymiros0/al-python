local var_0_0 = class("AtelierMaterial", import("model.vo.BaseVO"))

var_0_0.TYPE = {
	STRENGTHEN = 5,
	SAIREN = 4,
	NORMAL = 1,
	NEUTRALIZER = 2,
	TOOL = 6,
	MOD = 3
}
var_0_0.ELEMENT_TYPE = {
	CRYO = 2,
	SAIREN = 5,
	ELECTRO = 3,
	ANEMO = 4,
	PYRO = 1
}

def var_0_0.Ctor(arg_1_0, ...):
	var_0_0.super.Ctor(arg_1_0, ...)

	arg_1_0.count = arg_1_0.count or 0

def var_0_0.bindConfigTable(arg_2_0):
	return pg.activity_ryza_item

def var_0_0.GetName(arg_3_0):
	return arg_3_0.getConfig("name")

def var_0_0.GetRarity(arg_4_0):
	return arg_4_0.getConfig("rarity")

def var_0_0.GetIconPath(arg_5_0):
	return "props/" .. arg_5_0.getConfig("icon")

def var_0_0.GetDesc(arg_6_0):
	return arg_6_0.getConfig("display")

def var_0_0.GetType(arg_7_0):
	return arg_7_0.getConfig("type")

def var_0_0.GetProps(arg_8_0):
	return arg_8_0.getConfig("prop")

def var_0_0.GetLevel(arg_9_0):
	return arg_9_0.getConfig("prop_level")

def var_0_0.GetSource(arg_10_0):
	return arg_10_0.getConfig("get_access")

def var_0_0.GetBuffs(arg_11_0):
	local var_11_0 = arg_11_0.getConfig("benefit_buff")

	return type(var_11_0) == "table" and var_11_0 or None

def var_0_0.GetVoices(arg_12_0):
	return arg_12_0.getConfig("got_voice")

local var_0_1 = {
	1,
	1,
	1,
	0,
	0
}

def var_0_0.GetBaseCircleTransform(arg_13_0):
	local var_13_0 = arg_13_0.getConfig("base_circle")

	return type(var_13_0) == "table" and var_13_0 or var_0_1

def var_0_0.GetNormalCircleTransform(arg_14_0):
	local var_14_0 = arg_14_0.getConfig("normal_circle")

	return type(var_14_0) == "table" and var_14_0 or var_0_1

def var_0_0.IsNormal(arg_15_0):
	local var_15_0 = arg_15_0.GetType()

	return var_15_0 == var_0_0.TYPE.NORMAL or var_15_0 == var_0_0.TYPE.MOD or var_15_0 == var_0_0.TYPE.SAIREN

def var_0_0.UpdateRyzaItem(arg_16_0, arg_16_1, arg_16_2):
	arg_16_2 = arg_16_2 or {}

	local var_16_0 = ItemRarity.Rarity2Print(arg_16_1.GetRarity())

	setImageSprite(findTF(arg_16_0, "icon_bg"), GetSpriteFromAtlas("weaponframes", "bg" .. var_16_0))
	setFrame(findTF(arg_16_0, "icon_bg/frame"), var_16_0)

	local var_16_1 = findTF(arg_16_0, "icon_bg/icon")

	GetImageSpriteFromAtlasAsync(arg_16_1.GetIconPath(), "", var_16_1)
	setIconStars(arg_16_0, False)
	setIconName(arg_16_0, arg_16_1.GetName(), arg_16_2)
	setIconColorful(arg_16_0, arg_16_1.GetRarity(), arg_16_2)

return var_0_0
