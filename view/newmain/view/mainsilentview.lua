local var_0_0 = class("MainSilentView", import("view.base.BaseSubView"))
local var_0_1 = 1
local var_0_2 = 2
local var_0_3 = 3
local var_0_4 = 4
local var_0_5 = 1
local var_0_6 = 2

function var_0_0.getUIName(arg_1_0)
	return "MainSilentViewUI"
end

function var_0_0.OnLoaded(arg_2_0)
	arg_2_0.cg = arg_2_0._tf:GetComponent(typeof(CanvasGroup))
	arg_2_0.animationPlayer = arg_2_0._tf:GetComponent(typeof(Animation))
	arg_2_0.dftAniEvent = arg_2_0._tf:GetComponent(typeof(DftAniEvent))
	arg_2_0.timeTxt = arg_2_0:findTF("adapt/en/time"):GetComponent(typeof(Text))
	arg_2_0.timeEnTxt = arg_2_0:findTF("adapt/en"):GetComponent(typeof(Text))
	arg_2_0.batteryTxt = arg_2_0:findTF("adapt/battery/Text"):GetComponent(typeof(Text))
	arg_2_0.electric = {
		arg_2_0:findTF("adapt/battery/kwh/1"),
		arg_2_0:findTF("adapt/battery/kwh/2"),
		arg_2_0:findTF("adapt/battery/kwh/3")
	}
	arg_2_0.dateTxt = arg_2_0:findTF("adapt/date"):GetComponent(typeof(Text))
	arg_2_0.changeBtn = arg_2_0:findTF("change")
	arg_2_0.tips = UIItemList.New(arg_2_0:findTF("tips"), arg_2_0:findTF("tips/tpl"))
	arg_2_0.changeSkinBtn = MainChangeSkinBtn.New(arg_2_0.changeBtn, arg_2_0.event)
	arg_2_0.systemTimeUtil = SystemTimeUtil.New()
	arg_2_0.playedList = {}
end

function var_0_0.OnInit(arg_3_0)
	onButton(arg_3_0, arg_3_0.changeBtn, function()
		arg_3_0:TrackingSwitchShip()

		arg_3_0.changeSkinCount = arg_3_0.changeSkinCount + 1

		arg_3_0.changeSkinBtn:OnClick()
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0:Tracking(var_0_5)
		arg_3_0:Exit()
	end, SFX_PANEL)
	arg_3_0:bind(GAME.ZERO_HOUR_OP_DONE, function()
		arg_3_0:FlushDate()
	end)
	arg_3_0:bind(GAME.REMOVE_LAYERS, function(arg_7_0, arg_7_1)
		arg_3_0:OnRemoveLayer(arg_7_1.context)
	end)
	arg_3_0.changeSkinBtn:Flush()
end

function var_0_0.OnRemoveLayer(arg_8_0, arg_8_1)
	if arg_8_1.mediator == CommissionInfoMediator or arg_8_1.mediator == NotificationMediator then
		arg_8_0:Exit()
	end
end

function var_0_0.Exit(arg_9_0, arg_9_1)
	arg_9_0:TrackingSwitchShip()
	arg_9_0.dftAniEvent:SetEndEvent(nil)
	arg_9_0.dftAniEvent:SetEndEvent(function()
		arg_9_0:emit(NewMainScene.EXIT_SILENT_VIEW)

		if arg_9_1 then
			arg_9_1()
		end
	end)
	arg_9_0.animationPlayer:Play("anim_silentview_out")
end

function var_0_0.Tracking(arg_11_0, arg_11_1)
	local var_11_0 = pg.TimeMgr.GetInstance():GetServerTime()
	local var_11_1 = arg_11_0.enterTime
	local var_11_2 = arg_11_0.changeSkinCount
	local var_11_3 = arg_11_1

	TrackConst.TrackingExitSilentView(var_11_1, var_11_0, var_11_3)
end

function var_0_0.TrackingSwitchShip(arg_12_0)
	if not getProxy(PlayerProxy) then
		return
	end

	local var_12_0 = getProxy(PlayerProxy):getRawData()

	if not var_12_0 then
		return
	end

	local var_12_1 = var_12_0:GetFlagShip()
	local var_12_2 = var_12_1.skinId

	if isa(var_12_1, VirtualEducateCharShip) then
		var_12_2 = 0
	end

	local var_12_3 = pg.TimeMgr.GetInstance():GetServerTime()
	local var_12_4 = var_12_3 - arg_12_0.paintingTime

	TrackConst.TrackingSwitchPainting(var_12_2, var_12_4)

	arg_12_0.paintingTime = var_12_3
end

function var_0_0.Show(arg_13_0)
	var_0_0.super.Show(arg_13_0)
	arg_13_0:FlushTips()
	arg_13_0:FlushBattery()
	arg_13_0:FlushTime()
	arg_13_0:FlushDate()
	arg_13_0:AddTimer()

	arg_13_0.changeSkinCount = 0
	arg_13_0.enterTime = pg.TimeMgr.GetInstance():GetServerTime()
	arg_13_0.paintingTime = arg_13_0.enterTime
end

function var_0_0.Reset(arg_14_0)
	var_0_0.super.Reset(arg_14_0)

	arg_14_0.exited = false
end

function var_0_0.AddTimer(arg_15_0)
	arg_15_0:RemoveTimer()

	arg_15_0.timer = Timer.New(function()
		arg_15_0:FlushTips()
		arg_15_0:FlushBattery()
	end, 30, -1)

	arg_15_0.timer:Start()
end

function var_0_0.RemoveTimer(arg_17_0)
	if arg_17_0.timer then
		arg_17_0.timer:Stop()

		arg_17_0.timer = nil
	end
end

function var_0_0.FlushTips(arg_18_0)
	local var_18_0 = {}

	arg_18_0:CollectTips(var_18_0)

	local var_18_1 = {}

	arg_18_0.tips:make(function(arg_19_0, arg_19_1, arg_19_2)
		if UIItemList.EventUpdate == arg_19_0 then
			local var_19_0 = var_18_0[arg_19_1 + 1]
			local var_19_1 = GetSpriteFromAtlas("ui/MainUI_atlas", "noti_" .. var_19_0.type)

			arg_19_2:Find("icon"):GetComponent(typeof(Image)).sprite = var_19_1

			setText(arg_19_2:Find("num"), var_19_0.count)
			setText(arg_19_2:Find("Text"), i18n("main_silent_tip_" .. var_19_0.type))
			onButton(arg_18_0, arg_19_2, function()
				arg_18_0:PlayTipOutAnimation(arg_19_2, function()
					arg_18_0:Skip(var_19_0.type)
				end)
			end, SFX_PANEL)
			arg_18_0:InsertAnimation(var_18_1, arg_19_2)
		end
	end)
	arg_18_0.tips:align(#var_18_0)
	seriesAsync(var_18_1, function()
		return
	end)
end

function var_0_0.PlayTipOutAnimation(arg_23_0, arg_23_1, arg_23_2)
	arg_23_0.cg.blocksRaycasts = false

	local var_23_0 = arg_23_1:GetComponent(typeof(Animation))
	local var_23_1 = arg_23_1:GetComponent(typeof(DftAniEvent))

	var_23_1:SetEndEvent(nil)
	var_23_1:SetEndEvent(function()
		arg_23_0.cg.blocksRaycasts = true

		var_23_1:SetEndEvent(nil)
		arg_23_2()
	end)
	var_23_0:Play("anim_silentview_tip_out")
end

function var_0_0.InsertAnimation(arg_25_0, arg_25_1, arg_25_2)
	if table.contains(arg_25_0.playedList, arg_25_2) then
		return
	end

	local var_25_0 = GetOrAddComponent(arg_25_2, typeof(CanvasGroup))

	var_25_0.alpha = 0

	table.insert(arg_25_1, function(arg_26_0)
		if arg_25_0.exited then
			return
		end

		var_25_0.alpha = 1

		arg_25_2:GetComponent(typeof(Animation)):Play("anim_silentview_tip_in")
		onDelayTick(arg_26_0, 0.066)
	end)
	table.insert(arg_25_0.playedList, arg_25_2)
end

function var_0_0.Skip(arg_27_0, arg_27_1)
	arg_27_0:Tracking(var_0_6)
	arg_27_0:Exit(function()
		if arg_27_1 == var_0_1 then
			pg.m02:sendNotification(GAME.GO_SCENE, SCENE.EVENT)
		elseif arg_27_1 == var_0_2 then
			pg.m02:sendNotification(GAME.GO_SCENE, SCENE.GETBOAT)
		elseif arg_27_1 == var_0_3 then
			pg.m02:sendNotification(GAME.GO_SCENE, SCENE.TECHNOLOGY)
		elseif arg_27_1 == var_0_4 then
			pg.m02:sendNotification(GAME.GO_SCENE, SCENE.NAVALACADEMYSCENE, {
				warp = NavalAcademyScene.WARP_TO_TACTIC
			})
		end
	end)
end

function var_0_0.CollectTips(arg_29_0, arg_29_1)
	arg_29_0:CollectEventTips(arg_29_1)
	arg_29_0:CollectBuildTips(arg_29_1)
	arg_29_0:CollectTechTips(arg_29_1)
	arg_29_0:CollectStudentTips(arg_29_1)
end

function var_0_0.CollectEventTips(arg_30_0, arg_30_1)
	local var_30_0 = getProxy(EventProxy):countByState(EventInfo.StateFinish)

	if var_30_0 > 0 then
		table.insert(arg_30_1, {
			count = var_30_0,
			type = var_0_1
		})
	end
end

function var_0_0.CollectBuildTips(arg_31_0, arg_31_1)
	local var_31_0 = getProxy(BuildShipProxy):getFinishCount()

	if var_31_0 > 0 then
		table.insert(arg_31_1, {
			count = var_31_0,
			type = var_0_2
		})
	end
end

function var_0_0.CollectTechTips(arg_32_0, arg_32_1)
	local var_32_0 = getProxy(TechnologyProxy):getPlanningTechnologys()
	local var_32_1 = 0

	for iter_32_0, iter_32_1 in pairs(var_32_0) do
		if iter_32_1:isCompleted() then
			var_32_1 = var_32_1 + 1
		end
	end

	if var_32_1 > 0 then
		table.insert(arg_32_1, {
			count = var_32_1,
			type = var_0_3
		})
	end
end

function var_0_0.CollectStudentTips(arg_33_0, arg_33_1)
	local var_33_0 = getProxy(NavalAcademyProxy):RawGetStudentList()
	local var_33_1 = 0

	for iter_33_0, iter_33_1 in pairs(var_33_0) do
		if iter_33_1:IsFinish() then
			var_33_1 = var_33_1 + 1
		end
	end

	if var_33_1 > 0 then
		table.insert(arg_33_1, {
			count = var_33_1,
			type = var_0_4
		})
	end
end

function var_0_0.FlushBattery(arg_34_0)
	local var_34_0 = SystemInfo.batteryLevel

	if var_34_0 < 0 then
		var_34_0 = 1
	end

	local var_34_1 = math.floor(var_34_0 * 100)

	arg_34_0.batteryTxt.text = var_34_1 .. "%"

	local var_34_2 = 1 / #arg_34_0.electric

	for iter_34_0, iter_34_1 in ipairs(arg_34_0.electric) do
		local var_34_3 = var_34_1 < (iter_34_0 - 1) * var_34_2

		setActive(iter_34_1, not var_34_3)
	end
end

function var_0_0.FlushTime(arg_35_0)
	arg_35_0.systemTimeUtil:SetUp(function(arg_36_0, arg_36_1, arg_36_2)
		local var_36_0 = arg_36_0 > 12 and arg_36_0 - 12 or arg_36_0

		if var_36_0 < 10 then
			var_36_0 = "0" .. var_36_0
		end

		arg_35_0.timeTxt.text = var_36_0 .. ":" .. arg_36_1
		arg_35_0.timeEnTxt.text = arg_36_2
	end)
end

local var_0_7 = {
	"MONDAY",
	"TUESDAY",
	"WEDNESDAY",
	"THURSDAY",
	"FRIDAY",
	"SATURDAY",
	"SUNDAY"
}
local var_0_8 = {
	"JAN",
	"FEB",
	"MAR",
	"APR",
	"MAY",
	"JUN",
	"JUL",
	"AUG",
	"SEP",
	"OCT",
	"NOV",
	"DEC"
}

function var_0_0.FlushDate(arg_37_0)
	local var_37_0 = pg.TimeMgr.GetInstance():CurrentSTimeDesc("%Y/%m/%d", true)
	local var_37_1 = string.split(var_37_0, "/")
	local var_37_2 = var_37_1[1]
	local var_37_3 = tonumber(var_37_1[2])
	local var_37_4 = var_37_1[3]
	local var_37_5 = pg.TimeMgr.GetInstance():GetServerWeek()
	local var_37_6 = {
		var_0_7[var_37_5],
		var_0_8[var_37_3],
		var_37_4,
		var_37_2
	}

	arg_37_0.dateTxt.text = table.concat(var_37_6, " / ")
end

function var_0_0.OnDestroy(arg_38_0)
	arg_38_0.exited = true

	arg_38_0.dftAniEvent:SetEndEvent(nil)
	arg_38_0:RemoveTimer()
	arg_38_0.changeSkinBtn:Dispose()

	arg_38_0.changeSkinBtn = nil

	arg_38_0.systemTimeUtil:Dispose()

	arg_38_0.systemTimeUtil = nil
end

return var_0_0
