﻿local var_0_0 = class("AnimeMidtermLoginPage", import(".TemplatePage.LoginTemplatePage"))

function var_0_0.OnInit(arg_1_0)
	arg_1_0.dayProgressImg = arg_1_0:findTF("DayProgress")
	arg_1_0.awardImg = arg_1_0:findTF("Award")
	arg_1_0.maskImg = arg_1_0:findTF("Mask", arg_1_0.awardImg)

	addSlip(SLIP_TYPE_HRZ, arg_1_0.awardImg, function()
		if arg_1_0.curShowDay > 1 then
			triggerButton(arg_1_0.arrowLeft)
		end
	end, function()
		if arg_1_0.curShowDay < arg_1_0.allDaycount then
			triggerButton(arg_1_0.arrowRight)
		end
	end)

	arg_1_0.arrowLeft = arg_1_0:findTF("ArrowLeft")
	arg_1_0.arrowRight = arg_1_0:findTF("ArrowRight")

	onButton(arg_1_0, arg_1_0.arrowLeft, function()
		arg_1_0.curShowDay = arg_1_0.curShowDay - 1

		arg_1_0:updateAwardInfo(arg_1_0.curShowDay)
	end, SFX_PANEL)
	onButton(arg_1_0, arg_1_0.arrowRight, function()
		arg_1_0.curShowDay = arg_1_0.curShowDay + 1

		arg_1_0:updateAwardInfo(arg_1_0.curShowDay)
	end, SFX_PANEL)

	arg_1_0.pointTpl = arg_1_0:findTF("Point")
	arg_1_0.pointContainer = arg_1_0:findTF("PointList")
	arg_1_0.pointUIItemList = UIItemList.New(arg_1_0.pointContainer, arg_1_0.pointTpl)

	arg_1_0.pointUIItemList:make(function(arg_6_0, arg_6_1, arg_6_2)
		if arg_6_0 == UIItemList.EventUpdate then
			arg_6_1 = arg_6_1 + 1

			local var_6_0 = arg_1_0:findTF("Selected", arg_6_2)

			if arg_6_1 <= arg_1_0.nday then
				setImageAlpha(arg_6_2, 1)
			else
				setImageAlpha(arg_6_2, 0.3)
			end

			setActive(var_6_0, arg_6_1 == arg_1_0.curShowDay)
		end
	end)

	arg_1_0.loader = AutoLoader.New()
end

function var_0_0.OnDataSetting(arg_7_0)
	arg_7_0.config = pg.activity_7_day_sign[arg_7_0.activity:getConfig("config_id")]
	arg_7_0.allDaycount = #arg_7_0.config.front_drops
	arg_7_0.nday = arg_7_0.activity.data1
	arg_7_0.curShowDay = arg_7_0.nday
end

function var_0_0.OnFirstFlush(arg_8_0)
	return
end

function var_0_0.OnUpdateFlush(arg_9_0)
	arg_9_0.nday = arg_9_0.activity.data1
	arg_9_0.curShowDay = arg_9_0.nday

	arg_9_0:updateAwardInfo(arg_9_0.curShowDay)
end

function var_0_0.OnDestroy(arg_10_0)
	arg_10_0.loader:Clear()
end

function var_0_0.updateAwardInfo(arg_11_0, arg_11_1)
	arg_11_1 = math.max(arg_11_1, 1)

	arg_11_0.loader:GetOffSpriteRequest(arg_11_0.dayProgressImg)
	arg_11_0.loader:GetOffSpriteRequest(arg_11_0.awardImg)
	arg_11_0.loader:GetSprite("ui/activityuipage/animelogin_atlas", "tianshu_" .. arg_11_1, arg_11_0.dayProgressImg, true)
	arg_11_0.loader:GetSprite("ui/activityuipage/animemidtermloginpage_atlas", "icon_" .. arg_11_1, arg_11_0.awardImg, true)
	setActive(arg_11_0.maskImg, arg_11_1 <= arg_11_0.nday)
	setActive(arg_11_0.arrowLeft, arg_11_1 ~= 1)
	setActive(arg_11_0.arrowRight, arg_11_1 ~= arg_11_0.allDaycount)
	arg_11_0.pointUIItemList:align(arg_11_0.allDaycount)
end

return var_0_0
