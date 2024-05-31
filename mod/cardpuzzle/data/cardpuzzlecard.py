local var_0_0 = class("CardPuzzleCard", BaseVO)

var_0_0.CARD_TYPE = {
	ATTACK = 1,
	ABILITY = 3,
	TACTIC = 2
}

def var_0_0.CreateByNetData(arg_1_0):
	local var_1_0 = {}

	for iter_1_0 = 1, arg_1_0.num:
		table.insert(var_1_0, var_0_0.New({
			configId = arg_1_0.id
		}))

	return var_1_0

def var_0_0.bindConfigTable(arg_2_0):
	return pg.card_template

def var_0_0.GetIconPath(arg_3_0):
	return var_0_0.GetCardIconPath(arg_3_0.getConfig("icon"))

def var_0_0.GetConfigId(arg_4_0):
	return arg_4_0.configId

def var_0_0.GetName(arg_5_0):
	return arg_5_0.getConfig("name")

def var_0_0.GetCost(arg_6_0):
	return arg_6_0.getConfig("cost")

def var_0_0.GetType(arg_7_0):
	return arg_7_0.getConfig("card_type")

def var_0_0.GetDesc(arg_8_0):
	return arg_8_0.getConfig("discript")

def var_0_0.GetRarity(arg_9_0):
	return arg_9_0.getConfig("rarity")

def var_0_0.GetEffects(arg_10_0):
	return {
		{
			keywords = {}
		}
	}

def var_0_0.GetKeywords(arg_11_0):
	return var_0_0.GetCardKeyWord(arg_11_0.getConfig("label"))

def var_0_0.GetCardKeyWord(arg_12_0):
	return _.map(arg_12_0, function(arg_13_0)
		return pg.puzzle_card_affix[arg_13_0])

def var_0_0.GetCardIconPath(arg_14_0):
	return "RogueCards/" .. arg_14_0

return var_0_0
