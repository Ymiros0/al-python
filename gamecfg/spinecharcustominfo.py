pg = pg or {}

local var_0_0 = pg

this = {}
var_0_0.SpineCharCustomInfo = this
this.char_material_default_alpha = {}

def this.GetCharMaterial(arg_1_0):
	local var_1_0

	if table.contains(var_0_0.SpineCharCustomInfo.char_material_default_alpha, arg_1_0):
		PoolMgr.GetInstance().LoadAsset("spinematerials", "CharDefaultAlpha", False, typeof(Material), function(arg_2_0)
			var_1_0 = arg_2_0, False)

		var_1_0.name = "SkeletonGraphicDefault"

	return var_1_0
