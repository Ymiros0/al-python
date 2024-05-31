﻿local var_0_0 = class("XiefeierIdolMusicPage", import("...base.BaseActivityPage"))
local var_0_1 = {
	0.08,
	0.19,
	0.4,
	0.6,
	0.734,
	0.876,
	1,
	1
}

function var_0_0.OnInit(arg_1_0)
	arg_1_0.bg = arg_1_0:findTF("AD")
	arg_1_0.masklist = arg_1_0.bg:Find("maskList")
	arg_1_0.slider = arg_1_0.bg:Find("slider")
end

function var_0_0.OnDataSetting(arg_2_0)
	arg_2_0.HubID = arg_2_0.activity:getConfig("config_id")

	print("self.HubID:" .. arg_2_0.HubID)

	arg_2_0.mgProxy = getProxy(MiniGameProxy)
end

function var_0_0.OnFirstFlush(arg_3_0)
	onButton(arg_3_0, arg_3_0.bg:Find("battle_btn"), function()
		pg.m02:sendNotification(GAME.GO_MINI_GAME, 16)
	end, SFX_PANEL)
end

function var_0_0.OnUpdateFlush(arg_5_0)
	arg_5_0.hubData = arg_5_0.mgProxy:GetHubByHubId(arg_5_0.HubID)
	arg_5_0.finish_times = arg_5_0.hubData.usedtime
	arg_5_0.all_times = arg_5_0.hubData.usedtime + arg_5_0.hubData.count

	for iter_5_0 = 1, 7 do
		setActive(arg_5_0.masklist:Find("mask" .. iter_5_0 .. "/dot"), iter_5_0 <= arg_5_0.finish_times)
		setActive(arg_5_0.masklist:Find("mask" .. iter_5_0 .. "/frame"), iter_5_0 <= arg_5_0.all_times and not isActive(arg_5_0.masklist:Find("mask" .. iter_5_0 .. "/dot")))
	end

	if arg_5_0.finish_times > 0 then
		setSlider(arg_5_0.slider, 0, 1, var_0_1[arg_5_0.finish_times])
	else
		setSlider(arg_5_0.slider, 0, 1, 0)
	end

	if arg_5_0.finish_times >= arg_5_0.hubData:getConfig("reward_need") and arg_5_0.hubData.ultimate == 0 then
		arg_5_0:emit(ActivityMediator.MUSIC_GAME_OPERATOR, {
			hubid = arg_5_0.HubID,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		})
	end

	setActive(arg_5_0.bg:Find("got_icon"), arg_5_0.hubData.ultimate ~= 0)
end

function var_0_0.OnDestroy(arg_6_0)
	clearImageSprite(arg_6_0.bg)
end

return var_0_0
