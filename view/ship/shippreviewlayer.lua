﻿local var_0_0 = class("ShipPreviewLayer", import("..base.BaseUI"))
local var_0_1 = 12
local var_0_2 = 3
local var_0_3 = Vector3(0, 1, 40)

function var_0_0.getUIName(arg_1_0)
	return "ShipPreviewUI"
end

function var_0_0.init(arg_2_0)
	arg_2_0.UIMgr = pg.UIMgr.GetInstance()

	arg_2_0.UIMgr:BlurPanel(arg_2_0._tf, false, arg_2_0.contextData.weight and {
		weight = arg_2_0.contextData.weight
	} or {})

	arg_2_0.UIMain = arg_2_0.UIMgr.UIMain
	arg_2_0.seaCameraGO = GameObject.Find("BarrageCamera")
	arg_2_0.leftPanel = arg_2_0:findTF("left_panel")
	arg_2_0.sea = arg_2_0:findTF("sea", arg_2_0.leftPanel)
	arg_2_0.seaCamera = arg_2_0.seaCameraGO:GetComponent("Camera")
	arg_2_0.seaCamera.enabled = true
	arg_2_0.rawImage = arg_2_0.sea:GetComponent("RawImage")

	setActive(arg_2_0.rawImage, false)

	arg_2_0.seaCamera.targetTexture = arg_2_0.rawImage.texture
	arg_2_0.healTF = arg_2_0:findTF("resources/heal")
	arg_2_0.healTF.transform.localPosition = Vector3(-360, 50, 40)

	setActive(arg_2_0.healTF, false)
	arg_2_0.healTF:GetComponent("DftAniEvent"):SetEndEvent(function()
		setActive(arg_2_0.healTF, false)
		setText(arg_2_0.healTF:Find("text"), "")
	end)

	arg_2_0.seaLoading = arg_2_0:findTF("bg/loading", arg_2_0.leftPanel)

	arg_2_0:playLoadingAni()
end

function var_0_0.didEnter(arg_4_0)
	onButton(arg_4_0, arg_4_0.seaLoading, function()
		if not arg_4_0.previewer then
			arg_4_0:showBarrage()
		end
	end)
	onButton(arg_4_0, arg_4_0._tf, function()
		arg_4_0:emit(var_0_0.ON_CLOSE)
	end)
end

function var_0_0.setShip(arg_7_0, arg_7_1, arg_7_2, arg_7_3)
	arg_7_0.shipVO = arg_7_1
	arg_7_0.weaponIds = arg_7_2
	arg_7_0.equipSkinId = arg_7_3
end

function var_0_0.showBarrage(arg_8_0)
	arg_8_0.previewer = WeaponPreviewer.New(arg_8_0.rawImage)

	arg_8_0.previewer:configUI(arg_8_0.healTF)
	arg_8_0.previewer:setDisplayWeapon(arg_8_0.weaponIds, arg_8_0.equipSkinId, true)
	arg_8_0.previewer:load(40000, arg_8_0.shipVO, arg_8_0.weaponIds, function()
		arg_8_0:stopLoadingAni()
	end)
end

function var_0_0.getWaponIdsById(arg_10_0, arg_10_1)
	return arg_10_0.ship_data_breakout[arg_10_1].weapon_ids
end

function var_0_0.playLoadingAni(arg_11_0)
	setActive(arg_11_0.seaLoading, true)
end

function var_0_0.stopLoadingAni(arg_12_0)
	setActive(arg_12_0.seaLoading, false)
end

function var_0_0.willExit(arg_13_0)
	arg_13_0.UIMgr:UnblurPanel(arg_13_0._tf, arg_13_0.UIMain)

	if arg_13_0.previewer then
		arg_13_0.previewer:clear()

		arg_13_0.previewer = nil
	end
end

return var_0_0
