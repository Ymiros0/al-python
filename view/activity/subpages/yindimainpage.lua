﻿local var_0_0 = class("YinDiMainPage", import(".TemplatePage.PreviewTemplatePage"))

function var_0_0.OnInit(arg_1_0)
	arg_1_0.bg = arg_1_0:findTF("AD")
	arg_1_0.btnList = arg_1_0:findTF("btn_list", arg_1_0.bg)
end

function var_0_0.OnFirstFlush(arg_2_0)
	var_0_0.super.OnFirstFlush(arg_2_0)
	onButton(arg_2_0, findTF(arg_2_0.bg, "btn_list/shop"), function()
		arg_2_0:emit(ActivityMediator.GO_SHOPS_LAYER, {
			warp = NewShopsScene.TYPE_ACTIVITY,
			actId = arg_2_0.activity.id
		})
	end)
end

return var_0_0
