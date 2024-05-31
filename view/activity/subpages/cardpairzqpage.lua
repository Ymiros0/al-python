local var_0_0 = class("CardPairZQPage", import("...base.BaseActivityPage"))

function var_0_0.OnInit(arg_1_0)
	arg_1_0.bg = arg_1_0:findTF("AD")
	arg_1_0.slider = arg_1_0:findTF("slider", arg_1_0.bg)
	arg_1_0.step = arg_1_0:findTF("step", arg_1_0.bg)
	arg_1_0.progress = arg_1_0:findTF("progress", arg_1_0.bg)
	arg_1_0.displayBtn = arg_1_0:findTF("display_btn", arg_1_0.bg)
	arg_1_0.battleBtn = arg_1_0:findTF("battle_btn", arg_1_0.bg)
	arg_1_0.getBtn = arg_1_0:findTF("get_btn", arg_1_0.bg)
	arg_1_0.gotBtn = arg_1_0:findTF("got_btn", arg_1_0.bg)
	arg_1_0.gotIcon = arg_1_0:findTF("icon_got", arg_1_0.bg)
	arg_1_0.maskList = arg_1_0:findTF("maskList", arg_1_0.bg)
end

function var_0_0.OnDataSetting(arg_2_0)
	local var_2_0 = arg_2_0.activity:getConfig("config_data")[1]
end

function var_0_0.OnFirstFlush(arg_3_0)
	onButton(arg_3_0, arg_3_0.battleBtn, function()
		arg_3_0:emit(ActivityMediator.EVENT_GO_SCENE, SCENE.CARD_PAIRS)
	end, SFX_PANEL)
end

function var_0_0.OnUpdateFlush(arg_5_0)
	local var_5_0 = arg_5_0.activity.data2

	for iter_5_0 = 1, 7 do
		local var_5_1 = arg_5_0:findTF("mask" .. iter_5_0, arg_5_0.maskList)

		setActive(var_5_1, iter_5_0 <= var_5_0)
		setActive(arg_5_0:findTF("frame", var_5_1), var_5_0 <= iter_5_0)
	end

	setActive(arg_5_0.gotIcon, var_5_0 >= 7)
	setSlider(arg_5_0.slider, 0, 6, var_5_0 - 1 >= 0 and var_5_0 - 1 or 0)
	setActive(arg_5_0.battleBtn, true)
	setActive(arg_5_0.getBtn, false)
	setActive(arg_5_0.gotBtn, false)
end

return var_0_0
