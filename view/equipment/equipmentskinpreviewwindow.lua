local var_0_0 = class("EquipmentSkinPreviewWindow", import("view.ship.ShipPreviewLayer"))

function var_0_0.getUIName(arg_1_0)
	return "EquipSkinPreviewUI"
end

function var_0_0.init(arg_2_0)
	arg_2_0.buttonList = arg_2_0._tf:Find("left_panel/Buttons")
	arg_2_0.hitToggle = arg_2_0.buttonList:Find("HitEffect")
	arg_2_0.spawnToggle = arg_2_0.buttonList:Find("SpawnEffect")

	var_0_0.super.init(arg_2_0)
	setText(arg_2_0.hitToggle:Find("Text"), i18n("hit_preview"))
	setText(arg_2_0.spawnToggle:Find("Text"), i18n("shoot_preview"))
end

function var_0_0.didEnter(arg_3_0)
	local var_3_0 = pg.equip_skin_template[arg_3_0.equipSkinId]
	local var_3_1 = var_3_0.hit_fx_name ~= ""
	local var_3_2 = {
		EquipType.CannonQuZhu,
		EquipType.CannonQingXun,
		EquipType.CannonZhongXun,
		EquipType.Torpedo,
		EquipType.SubmarineTorpedo
	}

	var_3_1 = var_3_1 and _.any(var_3_0.equip_type, function(arg_4_0)
		return table.contains(var_3_2, arg_4_0)
	end)

	setActive(arg_3_0.hitToggle, var_3_1)

	if var_3_1 then
		arg_3_0.contextData.hitEffect = defaultValue(arg_3_0.contextData.hitEffect, true)

		triggerToggle(arg_3_0.hitToggle, arg_3_0.contextData.hitEffect)
		onToggle(arg_3_0, arg_3_0.hitToggle, function(arg_5_0)
			arg_3_0.contextData.hitEffect = arg_5_0

			arg_3_0:RefreshFXMode()
		end)
	else
		arg_3_0.contextData.hitEffect = defaultValue(arg_3_0.contextData.hitEffect, false)
	end

	local var_3_3 = var_3_0.fire_fx_name ~= ""

	setActive(arg_3_0.spawnToggle, var_3_3)

	if var_3_3 then
		arg_3_0.contextData.spawnEffect = defaultValue(arg_3_0.contextData.spawnEffect, true)

		triggerToggle(arg_3_0.spawnToggle, arg_3_0.contextData.spawnEffect)
		onToggle(arg_3_0, arg_3_0.spawnToggle, function(arg_6_0)
			arg_3_0.contextData.spawnEffect = arg_6_0

			arg_3_0:RefreshFXMode()
		end)
	else
		arg_3_0.contextData.spawnEffect = defaultValue(arg_3_0.contextData.spawnEffect, true)
	end

	var_0_0.super.didEnter(arg_3_0)
end

function var_0_0.RefreshFXMode(arg_7_0)
	if not arg_7_0.previewer then
		return
	end

	arg_7_0.previewer:SetFXMode(arg_7_0.contextData.spawnEffect, arg_7_0.contextData.hitEffect)
	arg_7_0.previewer:onWeaponUpdate()
end

function var_0_0.showBarrage(arg_8_0)
	var_0_0.super.showBarrage(arg_8_0)
	arg_8_0.previewer:SetFXMode(arg_8_0.contextData.spawnEffect, arg_8_0.contextData.hitEffect)
end

function var_0_0.playLoadingAni(arg_9_0)
	var_0_0.super.playLoadingAni(arg_9_0)
	setActive(arg_9_0.buttonList, false)
end

function var_0_0.stopLoadingAni(arg_10_0)
	var_0_0.super.stopLoadingAni(arg_10_0)
	setActive(arg_10_0.buttonList, true)
end

return var_0_0
