local var_0_0 = {
	sort = {
		{
			type = 1,
			spr = "sort_rarity",
			tag = i18n("word_equipment_rarity"),
			values = {
				"rarity",
				"id",
				"level"
			}
		},
		{
			type = 2,
			spr = "sort_intensify",
			tag = i18n("word_equipment_intensify"),
			values = {
				"level",
				"rarity",
				"id"
			}
		}
	},
	def getWeight:(arg_1_0, arg_1_1)
		return SpWeapon.bindConfigTable()[arg_1_0.GetConfigID()][arg_1_1]
}

def var_0_0.sortFunc(arg_2_0, arg_2_1):
	local var_2_0 = {}

	for iter_2_0, iter_2_1 in ipairs(arg_2_0.values):
		table.insert(var_2_0, function(arg_3_0)
			return (arg_2_1 and -1 or 1) * -var_0_0.getWeight(arg_3_0, iter_2_1))

	return var_2_0

return var_0_0
