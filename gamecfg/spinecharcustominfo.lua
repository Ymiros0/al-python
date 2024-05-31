pg = pg or {}

local var_0_0 = pg

this = {}
var_0_0.SpineCharCustomInfo = this
this.char_material_default_alpha = {}

function this.GetCharMaterial(arg_1_0)
	local var_1_0

	if table.contains(var_0_0.SpineCharCustomInfo.char_material_default_alpha, arg_1_0) then
		PoolMgr:GetInstance():LoadAsset("spinematerials", "CharDefaultAlpha", false, typeof(Material), function(arg_2_0)
			var_1_0 = arg_2_0
		end, false)

		var_1_0.name = "SkeletonGraphicDefault"
	end

	return var_1_0
end
