﻿local var_0_0 = class("NewYear22SkinShowPage", import("...base.BaseActivityPage"))
local var_0_1 = {
	{
		id = 403101,
		name = "Y22_adaerbote"
	},
	{
		id = 499061,
		name = "Y22_aogusite"
	},
	{
		id = 399051,
		name = "Y22_bailong"
	},
	{
		id = 405011,
		name = "Y22_bisimai"
	},
	{
		id = 108021,
		name = "Y22_daqinghuayu"
	},
	{
		id = 205091,
		name = "Y22_hao"
	},
	{
		id = 402041,
		name = "Y22_laibixi"
	},
	{
		id = 302211,
		name = "Y22_lei"
	},
	{
		id = 402061,
		name = "Y22_magedebao"
	},
	{
		id = 699011,
		name = "Y22_makeboluo"
	},
	{
		id = 202071,
		name = "Y22_nananpudun"
	},
	{
		id = 303141,
		name = "Y22_niaohai"
	},
	{
		id = 202291,
		name = "Y22_peineiluopo"
	},
	{
		id = 408021,
		name = "Y22_U47"
	},
	{
		id = 408121,
		name = "Y22_U1206"
	},
	{
		id = 405031,
		name = "Y22_wuerlixi"
	},
	{
		id = 401461,
		name = "Y22_Z46"
	},
	{
		id = 406021,
		name = "Y22_yibei"
	},
	{
		id = 201331,
		name = "Y22_yikaluosi"
	},
	{
		id = 205011,
		name = "Y22_yilishabai"
	}
}

function var_0_0.OnInit(arg_1_0)
	arg_1_0:findUI()
	arg_1_0:initData()
end

function var_0_0.findUI(arg_2_0)
	arg_2_0.paintBackTF = arg_2_0:findTF("Paints/PaintBack")
	arg_2_0.paintFrontTF = arg_2_0:findTF("Paints/PaintFront")
	arg_2_0.skinShopBtn = arg_2_0:findTF("BtnShop")
	arg_2_0.goBtn = arg_2_0:findTF("BtnGO")

	onButton(arg_2_0, arg_2_0.skinShopBtn, function()
		arg_2_0:emit(ActivityMediator.EVENT_GO_SCENE, SCENE.SKINSHOP)
	end, SFX_PANEL)
	onButton(arg_2_0, arg_2_0.goBtn, function()
		arg_2_0:emit(ActivityMediator.EVENT_GO_SCENE, SCENE.NEWYEAR_BACKHILL_2022)
	end, SFX_PANEL)
end

function var_0_0.initData(arg_5_0)
	arg_5_0.paintCount = 20
	arg_5_0.curPaintIndex = 1
	arg_5_0.paintSwitchTime = 1
	arg_5_0.paintStaticTime = 3.5
	arg_5_0.paintStaticCountValue = 0
	arg_5_0.paintPathPrefix = "NewYear22SkinShowPage/"
end

function var_0_0.switchNextPaint(arg_6_0)
	arg_6_0.frameTimer:Stop()

	local var_6_0 = arg_6_0.curPaintIndex % arg_6_0.paintCount + 1
	local var_6_1 = var_0_1[var_6_0].name
	local var_6_2 = arg_6_0.paintPathPrefix .. var_6_1
	local var_6_3 = pg.ship_data_statistics[var_0_1[var_6_0].id].name

	setImageSprite(arg_6_0.paintBackTF, LoadSprite(var_6_2, var_6_1))
	setText(findTF(arg_6_0.paintBackTF, "txt"), var_6_3)
	setText(findTF(arg_6_0.paintBackTF, "outlineTxt"), var_6_3)

	local var_6_4 = GetComponent(arg_6_0.paintFrontTF, typeof(CanvasGroup))
	local var_6_5 = GetComponent(arg_6_0.paintBackTF, typeof(CanvasGroup))

	LeanTween.value(go(arg_6_0.paintFrontTF), 1, 0, arg_6_0.paintSwitchTime):setOnUpdate(System.Action_float(function(arg_7_0)
		var_6_4.alpha = arg_7_0
		var_6_5.alpha = 1 - arg_7_0
	end)):setOnComplete(System.Action(function()
		setImageFromImage(arg_6_0.paintFrontTF, arg_6_0.paintBackTF)

		var_6_4.alpha = 1
		var_6_5.alpha = 0

		setText(findTF(arg_6_0.paintFrontTF, "txt"), var_6_3)
		setText(findTF(arg_6_0.paintFrontTF, "outlineTxt"), var_6_3)

		arg_6_0.curPaintIndex = var_6_0

		arg_6_0.frameTimer:Start()
	end))
end

function var_0_0.OnFirstFlush(arg_9_0)
	arg_9_0:initPaint()
	arg_9_0:initTimer()
end

function var_0_0.initPaint(arg_10_0)
	local var_10_0 = arg_10_0.curPaintIndex
	local var_10_1 = (var_10_0 - 1) % arg_10_0.paintCount + 1
	local var_10_2 = pg.ship_data_statistics[var_0_1[var_10_1].id].name
	local var_10_3 = var_0_1[var_10_0].name
	local var_10_4 = arg_10_0.paintPathPrefix .. var_10_3

	setImageSprite(arg_10_0.paintFrontTF, LoadSprite(var_10_4, var_10_3))
	setText(findTF(arg_10_0.paintFrontTF, "txt"), var_10_2)
	setText(findTF(arg_10_0.paintFrontTF, "outlineTxt"), var_10_2)

	local var_10_5 = pg.ship_data_statistics[var_0_1[var_10_1].id].name
	local var_10_6 = var_0_1[var_10_1].name
	local var_10_7 = arg_10_0.paintPathPrefix .. var_10_6

	setImageSprite(arg_10_0.paintBackTF, LoadSprite(var_10_7, var_10_6))
	setText(findTF(arg_10_0.paintBackTF, "txt"), var_10_5)
	setText(findTF(arg_10_0.paintBackTF, "outlineTxt"), var_10_5)
end

function var_0_0.initTimer(arg_11_0)
	local var_11_0 = 0.016666666666666666

	arg_11_0.paintStaticCountValue = 0
	arg_11_0.frameTimer = Timer.New(function()
		arg_11_0.paintStaticCountValue = arg_11_0.paintStaticCountValue + var_11_0

		if arg_11_0.paintStaticCountValue >= arg_11_0.paintStaticTime then
			arg_11_0.paintStaticCountValue = 0

			arg_11_0:switchNextPaint()
		end
	end, var_11_0, -1, false)

	arg_11_0.frameTimer:Start()
end

function var_0_0.OnDestroy(arg_13_0)
	if arg_13_0.frameTimer then
		arg_13_0.frameTimer:Stop()

		arg_13_0.frameTimer = nil
	end
end

return var_0_0
