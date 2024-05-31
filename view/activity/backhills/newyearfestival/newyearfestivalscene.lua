﻿local var_0_0 = class("NewyearFestivalScene", import("..TemplateMV.BackHillTemplate"))

function var_0_0.getUIName(arg_1_0)
	return "NewyearFestivalUI"
end

var_0_0.HUB_ID = 4

function var_0_0.init(arg_2_0)
	arg_2_0.top = arg_2_0:findTF("top")
	arg_2_0._closeBtn = arg_2_0:findTF("top/back")
	arg_2_0._homeBtn = arg_2_0:findTF("top/home")
	arg_2_0._helpBtn = arg_2_0:findTF("top/help")
	arg_2_0.ticketTimes = arg_2_0.top:Find("ticket/text")
	arg_2_0.yinhuace = arg_2_0.top:Find("sign")
	arg_2_0.yinhuaceTimes = arg_2_0.yinhuace:Find("get")
	arg_2_0.yinhuaceTips = arg_2_0.yinhuace:Find("tip")
	arg_2_0.shouce = arg_2_0.top:Find("yinhuashouceye")
	arg_2_0.shouce_bg = arg_2_0.shouce:Find("bg")
	arg_2_0.layout_shouce = arg_2_0.shouce:Find("yinhuace/layout")
	arg_2_0.group_get = CustomIndexLayer.Clone2Full(arg_2_0.layout_shouce, 7)
	arg_2_0.btn_receive = arg_2_0.shouce:Find("yinhuace/receive")
	arg_2_0.btn_shouce_help = arg_2_0.shouce:Find("yinhuace/help")
	arg_2_0.img_get = arg_2_0.shouce:Find("yinhuace/get")

	setActive(arg_2_0.shouce, false)

	arg_2_0._map = arg_2_0:findTF("map")
	arg_2_0.shrine = arg_2_0._map:Find("shrine")
	arg_2_0.snack_street = arg_2_0._map:Find("snack")
	arg_2_0.divination = arg_2_0._map:Find("divination")
	arg_2_0.shop = arg_2_0._map:Find("shop")
	arg_2_0.cube = arg_2_0._map:Find("magiccube")
	arg_2_0.bottom2 = arg_2_0._map:Find("bottom2")
	arg_2_0.bottom = arg_2_0._map:Find("bottom")
	arg_2_0.middle = arg_2_0._map:Find("middle")
	arg_2_0.front = arg_2_0._map:Find("top")
	arg_2_0.containers = {
		arg_2_0.front,
		arg_2_0.middle,
		arg_2_0.bottom,
		arg_2_0.bottom2
	}
	arg_2_0._shipTpl = arg_2_0._map:Find("ship")
	arg_2_0.graphPath = GraphPath.New(import("GameCfg.BackHillGraphs.NewyearFestivalGraph"))
	arg_2_0.effectReq = LoadPrefabRequestPackage.New("ui/xuedichangjing", "xuedichangjing", function(arg_3_0)
		setParent(arg_3_0, arg_2_0._map, false)

		local var_3_0 = GameObject.Find("UICamera/Canvas"):GetComponent(typeof(Canvas)).sortingOrder
		local var_3_1 = arg_3_0:GetComponentsInChildren(typeof(Renderer))

		for iter_3_0 = 0, var_3_1.Length - 1 do
			var_3_1[iter_3_0].sortingOrder = var_3_0 + 1
		end
	end):Start()
end

function var_0_0.didEnter(arg_4_0)
	local var_4_0 = getProxy(MiniGameProxy)

	onButton(arg_4_0, arg_4_0._closeBtn, function()
		arg_4_0:emit(var_0_0.ON_BACK)
	end)
	onButton(arg_4_0, arg_4_0._homeBtn, function()
		arg_4_0:emit(var_0_0.ON_HOME)
	end)
	onButton(arg_4_0, arg_4_0._helpBtn, function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.help_newyear_feast.tip
		})
	end)
	onButton(arg_4_0, arg_4_0.yinhuace, function()
		setActive(arg_4_0.shouce, true)
	end)
	onButton(arg_4_0, arg_4_0.shouce_bg, function()
		setActive(arg_4_0.shouce, false)
	end)
	onButton(arg_4_0, arg_4_0.btn_shouce_help, function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.help_newyear_stamp.tip
		})
	end)
	onButton(arg_4_0, arg_4_0.btn_receive, function()
		local var_11_0 = var_4_0:GetHubByHubId(arg_4_0.HUB_ID)

		if var_11_0.ultimate ~= 0 or var_11_0.usedtime < var_11_0:getConfig("reward_need") then
			return
		end

		arg_4_0:emit(NewYearFestivalMediator.MINI_GAME_OPERATOR, {
			hubid = var_11_0.id,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		})
	end)
	arg_4_0:InitFacility(arg_4_0.shrine, function()
		pg.m02:sendNotification(GAME.GO_MINI_GAME, 3)
	end)
	arg_4_0:InitFacility(arg_4_0.snack_street, function()
		pg.m02:sendNotification(GAME.GO_MINI_GAME, 8)
	end)
	arg_4_0:InitFacility(arg_4_0.divination, function()
		arg_4_0:emit(NewYearFestivalMediator.GO_SCENE, SCENE.ACTIVITY, {
			id = ActivityConst.CYGNET_BATHROBE_PAGE_ID
		})
	end)
	arg_4_0:InitFacility(arg_4_0.shop, function()
		arg_4_0:emit(NewYearFestivalMediator.GO_SCENE, SCENE.SKINSHOP)
	end)
	arg_4_0:InitFacility(arg_4_0.cube, function()
		arg_4_0:emit(NewYearFestivalMediator.GO_SCENE, SCENE.GETBOAT, {
			projectName = "new",
			page = 1
		})
	end)
	pg.UIMgr.GetInstance():OverlayPanel(arg_4_0.top, false)

	arg_4_0.academyStudents = {}

	arg_4_0:InitStudents(ActivityConst.NEWYEAR_ACTIVITY, 3, 5)
	arg_4_0:UpdateView()

	if arg_4_0.contextData.isOpenShrine then
		arg_4_0.contextData.isOpenShrine = nil

		pg.m02:sendNotification(GAME.GO_MINI_GAME, 3)
	end

	local var_4_1 = var_4_0:GetMiniGameData(3)

	if var_4_1 and not var_4_1:GetRuntimeData("isInited") then
		arg_4_0:emit(NewYearFestivalMediator.MINIGAME_OPERATION, arg_4_0.HUB_ID, MiniGameOPCommand.CMD_SPECIAL_GAME, {
			3,
			1
		})
	end
end

function var_0_0.UpdateView(arg_17_0)
	local var_17_0 = getProxy(MiniGameProxy)
	local var_17_1 = var_17_0:GetHubByHubId(arg_17_0.HUB_ID)
	local var_17_2 = var_17_1.usedtime

	setText(arg_17_0.ticketTimes, "X " .. var_17_1.count)
	setText(arg_17_0.yinhuaceTimes, string.format("%02d", var_17_2))

	for iter_17_0, iter_17_1 in ipairs(arg_17_0.group_get) do
		setActive(iter_17_1, iter_17_0 <= var_17_2)
	end

	local var_17_3 = var_17_2 >= #arg_17_0.group_get and var_17_1.ultimate == 0

	setActive(arg_17_0.btn_receive, var_17_3)
	setActive(arg_17_0.yinhuaceTips, var_17_3)
	setActive(arg_17_0.img_get, var_17_1.ultimate ~= 0)

	if var_17_1.ultimate == 1 then
		arg_17_0:TryPlayStory()
	end

	local var_17_4 = arg_17_0.snack_street:Find("tip")

	setActive(var_17_4, var_17_1.count > 0)

	local var_17_5 = arg_17_0.shrine:Find("tip")
	local var_17_6 = var_17_0:GetMiniGameData(3)
	local var_17_7 = false

	if var_17_6 then
		var_17_7 = (var_17_6:GetRuntimeData("count") or 0) > 0 and NewYearShrinePage.IsTip()
	end

	setActive(var_17_5, var_17_7)

	local var_17_8 = arg_17_0.divination:Find("tip")

	setActive(var_17_8, CygnetBathrobePage.IsTip())
end

var_0_0.edge2area = {
	["7_8"] = "bottom2",
	["3_8"] = "bottom",
	["5_6"] = "front"
}

function var_0_0.TryPlayStory(arg_18_0)
	return
end

function var_0_0.willExit(arg_19_0)
	arg_19_0.effectReq:Stop()
	pg.UIMgr.GetInstance():UnOverlayPanel(arg_19_0.top, arg_19_0._tf)
	arg_19_0:clearStudents()
end

return var_0_0
