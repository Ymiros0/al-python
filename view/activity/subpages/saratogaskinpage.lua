﻿local var_0_0 = class("SaratogaSkinPage", import(".TemplatePage.PreviewTemplatePage"))

function var_0_0.OnInit(arg_1_0)
	var_0_0.super.OnInit(arg_1_0)

	arg_1_0.shopBtn = arg_1_0:findTF("btn_list/shop", arg_1_0.bg)
	arg_1_0.fightBtn = arg_1_0:findTF("btn_list/fight", arg_1_0.bg)
end

function var_0_0.OnFirstFlush(arg_2_0)
	var_0_0.super.OnFirstFlush(arg_2_0)
	onButton(arg_2_0, arg_2_0.shopBtn, function()
		arg_2_0:emit(ActivityMediator.GO_SHOPS_LAYER, {
			warp = NewShopsScene.TYPE_ACTIVITY,
			actId = arg_2_0.activity.id
		})
	end)
	onButton(arg_2_0, arg_2_0.fightBtn, function()
		arg_2_0:emit(ActivityMediator.SPECIAL_BATTLE_OPERA)
	end)
end

return var_0_0
