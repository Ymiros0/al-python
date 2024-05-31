local var_0_0 = class("EquipmentRarity")

var_0_0.Gray = 2
var_0_0.Blue = 3
var_0_0.Purple = 4
var_0_0.Gold = 5
var_0_0.SSR = 6

def var_0_0.Rarity2Print(arg_1_0):
	return ItemRarity.Rarity2Print(arg_1_0 - 1)

var_0_0.correctedLevel = {
	{
		0
	},
	{
		0
	},
	{
		0,
		7
	},
	{
		0,
		11
	},
	{
		0,
		11,
		12,
		13
	},
	{
		0,
		11,
		12,
		13
	}
}

def var_0_0.Rarity2CorrectedLevel(arg_2_0, arg_2_1):
	local var_2_0 = var_0_0.correctedLevel[arg_2_0]
	local var_2_1

	for iter_2_0, iter_2_1 in ipairs(var_2_0):
		if iter_2_1 > arg_2_1 - 1:
			break
		else
			var_2_1 = iter_2_0 - 1

	return i18n("equip_info_extralevel_" .. var_2_1)

return var_0_0
