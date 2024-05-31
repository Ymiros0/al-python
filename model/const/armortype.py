local var_0_0 = class("ArmorType")

var_0_0.Light = 1
var_0_0.Medium = 2
var_0_0.Heavy = 3

def var_0_0.Type2Name(arg_1_0):
	if not var_0_0.names:
		var_0_0.names = {
			i18n("word_lightArmor"),
			i18n("word_mediumArmor"),
			i18n("word_heavyarmor")
		}

	return var_0_0.names[arg_1_0]

return var_0_0
