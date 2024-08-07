﻿local var_0_0 = class("BuildShipDetailLayer", import("...base.BaseUI"))
local var_0_1 = 10
local var_0_2 = 2
local var_0_3 = 1
local var_0_4 = 2
local var_0_5 = {
	"resources/1",
	"resources/2",
	"resources/3",
	"resources/1"
}

function var_0_0.getUIName(arg_1_0)
	return "BuildShipDetailUI1"
end

function var_0_0.setItems(arg_2_0, arg_2_1)
	arg_2_0.itemVO = arg_2_1[ITEM_ID_EQUIP_QUICK_FINISH] or {
		count = 0,
		id = ITEM_ID_EQUIP_QUICK_FINISH
	}
end

function var_0_0.setWorkCount(arg_3_0, arg_3_1)
	arg_3_0.workCount = arg_3_1
end

function var_0_0.setBuildSpeedUpRemind(arg_4_0, arg_4_1)
	arg_4_0.isStopSpeedUpRemind = arg_4_1
end

var_0_0.MODEL_INDEX = 2

function var_0_0.setProjectList(arg_5_0, arg_5_1)
	arg_5_0.projectList = arg_5_1
	arg_5_0.MODEL = #arg_5_0.projectList > var_0_0.MODEL_INDEX and var_0_2 or var_0_3
end

function var_0_0.init(arg_6_0)
	arg_6_0.UIMgr = pg.UIMgr.GetInstance()
	arg_6_0.multLineTF = arg_6_0:findTF("list_mult_line")
	arg_6_0.multLineContain = arg_6_0:findTF("list_mult_line/content")
	arg_6_0.multLineTpl = arg_6_0:findTF("project_tpl", arg_6_0.multLineContain)
	arg_6_0.multList = UIItemList.New(arg_6_0.multLineContain, arg_6_0.multLineTpl)
	arg_6_0.singleLineTF = arg_6_0:findTF("list_single_line")
	arg_6_0.singleLineContain = arg_6_0:findTF("list_single_line/content")
	arg_6_0.singleLineTpl = arg_6_0:findTF("project_tpl", arg_6_0.singleLineContain)
	arg_6_0.singleList = UIItemList.New(arg_6_0.singleLineContain, arg_6_0.singleLineTpl)
	arg_6_0.listCountTF = arg_6_0:findTF("title/value")
	arg_6_0.quickCount = arg_6_0:findTF("quick_count")
	arg_6_0.quickCountTF = arg_6_0:findTF("quick_count/value")
	arg_6_0.noneBg = arg_6_0:findTF("none_bg")
	arg_6_0.allLaunch = arg_6_0:findTF("all_launch")
	arg_6_0.aniBgTF = arg_6_0:findTF("aniBg")
	arg_6_0.canvasgroup = GetOrAddComponent(arg_6_0._tf, typeof(CanvasGroup))

	setText(arg_6_0:findTF("title/text"), i18n("build_detail_intro"))
end

function var_0_0.updatePlayer(arg_7_0, arg_7_1)
	arg_7_0._player = arg_7_1
end

function var_0_0.didEnter(arg_8_0)
	arg_8_0.projectTFs = {}

	arg_8_0.multList:make(function(arg_9_0, arg_9_1, arg_9_2)
		if arg_9_0 == UIItemList.EventUpdate then
			arg_9_2.gameObject.name = "project_" .. arg_9_1 + 1
			arg_8_0.projectTFs[arg_9_1 + 1] = arg_9_2

			arg_8_0:updateProject(arg_9_1 + 1, arg_8_0.projectList[arg_9_1 + 1])
		end
	end)
	arg_8_0.singleList:make(function(arg_10_0, arg_10_1, arg_10_2)
		if arg_10_0 == UIItemList.EventUpdate then
			arg_10_2.gameObject.name = "project_" .. arg_10_1 + 1
			arg_8_0.projectTFs[arg_10_1 + 1] = arg_10_2

			arg_8_0:updateProject(arg_10_1 + 1, arg_8_0.projectList[arg_10_1 + 1])
		end
	end)
	arg_8_0:initProjectList()
	arg_8_0:updateItem()
	arg_8_0:updateListCount()

	local var_8_0 = GameObject.Find("Overlay/UIOverlay")

	arg_8_0.aniBgTF.transform:SetParent(var_8_0.transform, false)
	onButton(arg_8_0, arg_8_0.allLaunch, function()
		local var_11_0 = arg_8_0:getNeedCount()

		if var_11_0 > 0 and not arg_8_0.isStopSpeedUpRemind then
			local var_11_1 = pg.MsgboxMgr.GetInstance()

			var_11_1:ShowMsgBox({
				showStopRemind = true,
				content = i18n("ship_buildShipScene_quest_quickFinish", var_11_0, arg_8_0.itemVO.count == 0 and COLOR_RED or COLOR_GREEN, arg_8_0.itemVO.count),
				stopRamindContent = i18n("common_dont_remind_dur_login"),
				onYes = function()
					arg_8_0:emit(BuildShipDetailMediator.LAUNCH_ALL, var_11_1.stopRemindToggle.isOn)
				end
			})
		elseif #arg_8_0.projectList > 0 then
			arg_8_0:emit(BuildShipDetailMediator.LAUNCH_ALL)
		else
			pg.TipsMgr.GetInstance():ShowTips(i18n("ship_getShip_error_noShip"))
		end
	end, SFX_UI_BUILDING_FASTBUILDING)
	onButton(arg_8_0, arg_8_0.quickCount, function()
		local var_13_0 = pg.shop_template[61009]

		shoppingBatch(61009, {
			id = var_13_0.effect_args[1]
		}, 9, "build_ship_quickly_buy_tool")
	end)
end

function var_0_0.onBackPressed(arg_14_0)
	if arg_14_0.isPlayAnim then
		return
	end

	arg_14_0:emit(var_0_0.ON_BACK_PRESSED, true)
end

function var_0_0.getNeedCount(arg_15_0)
	local var_15_0 = 0

	for iter_15_0, iter_15_1 in ipairs(arg_15_0.projectList) do
		if iter_15_1.state ~= BuildShip.FINISH then
			var_15_0 = var_15_0 + 1
		end
	end

	return var_15_0
end

function var_0_0.updateListCount(arg_16_0)
	setText(arg_16_0.listCountTF, arg_16_0.workCount)
end

function var_0_0.updateItem(arg_17_0)
	setText(arg_17_0.quickCountTF, arg_17_0.itemVO.count)
end

function var_0_0.initProjectList(arg_18_0)
	for iter_18_0, iter_18_1 in pairs(arg_18_0.buildTimers or {}) do
		pg.TimeMgr.GetInstance():RemoveTimer(iter_18_1)
	end

	arg_18_0.buildTimers = {}

	local var_18_0 = arg_18_0.MODEL == var_0_2 and #arg_18_0.projectList or 0
	local var_18_1 = arg_18_0.MODEL == var_0_3 and #arg_18_0.projectList or 0

	setActive(arg_18_0.multLineTF, var_18_0 > 0)
	setActive(arg_18_0.singleLineTF, var_18_1 > 0)
	arg_18_0.multList:align(var_18_0)
	arg_18_0.singleList:align(var_18_1)
	setActive(arg_18_0.noneBg, #arg_18_0.projectList <= 0)
end

function var_0_0.initMultLine(arg_19_0)
	arg_19_0.multList:align(#arg_19_0.projectList)
end

function var_0_0.initSingleLine(arg_20_0)
	arg_20_0.singleList:align(#arg_20_0.projectList)
end

function var_0_0.updateProject(arg_21_0, arg_21_1, arg_21_2)
	assert(isa(arg_21_2, BuildShip), "必须是实例BuildShip")

	local var_21_0 = arg_21_0.projectTFs[arg_21_1]

	if IsNil(var_21_0) then
		return
	end

	local var_21_1 = arg_21_0:findTF("frame/buiding", var_21_0)
	local var_21_2 = arg_21_0:findTF("frame/finished", var_21_0)
	local var_21_3 = arg_21_0:findTF("frame/waiting", var_21_0)

	setActive(var_21_3, false)
	setActive(var_21_1, arg_21_2.state == BuildShip.ACTIVE)
	setActive(var_21_2, arg_21_2.state == BuildShip.FINISH)

	var_21_0:GetComponent("CanvasGroup").alpha = arg_21_2.state == BuildShip.INACTIVE and 0.6 or 1

	local var_21_4 = pg.ship_data_create_material[arg_21_2.type]
	local var_21_5 = tonumber(var_21_4.ship_icon)
	local var_21_6 = arg_21_0:findTF("ship_modal", var_21_1)

	for iter_21_0 = 0, var_21_6.childCount - 1 do
		local var_21_7 = var_21_6:GetChild(iter_21_0)

		setActive(var_21_7, false)
	end

	if arg_21_2.state == BuildShip.ACTIVE then
		local var_21_8 = GetComponent(var_21_1, typeof(CanvasGroup))

		if var_21_8 then
			var_21_8.alpha = 1
		end

		local var_21_9 = arg_21_0:findTF("shipModelBuliding" .. var_21_5, var_21_6)

		if not var_21_9 then
			PoolMgr.GetInstance():GetUI("shipModelBuliding" .. var_21_5, true, function(arg_22_0)
				arg_22_0.transform:SetParent(var_21_6, false)

				arg_22_0.transform.localPosition = Vector3(1, 1, 1)
				arg_22_0.transform.localScale = Vector3(1, 1, 1)

				arg_22_0.transform:SetAsFirstSibling()

				arg_22_0.name = "shipModelBuliding" .. var_21_5

				setActive(arg_22_0, true)
			end)
		else
			setActive(var_21_9, true)
		end

		local var_21_10 = arg_21_0:findTF("timer/Text", var_21_1)

		onButton(arg_21_0, arg_21_0:findTF("quick_btn", var_21_1), function()
			local var_23_0, var_23_1, var_23_2 = BuildShip.canQuickBuildShip(arg_21_1)

			if not var_23_0 then
				if var_23_2 then
					GoShoppingMsgBox(i18n("switch_to_shop_tip_1"), ChargeScene.TYPE_ITEM, var_23_2)
				else
					pg.TipsMgr.GetInstance():ShowTips(var_23_1)
				end

				return
			end

			if arg_21_0.isStopSpeedUpRemind then
				arg_21_0:emit(BuildShipDetailMediator.ON_QUICK, arg_21_1)
			else
				local var_23_3 = pg.MsgboxMgr.GetInstance()

				var_23_3:ShowMsgBox({
					showStopRemind = true,
					content = i18n("ship_buildShipScene_quest_quickFinish", 1, arg_21_0.itemVO.count == 0 and COLOR_RED or COLOR_GREEN, arg_21_0.itemVO.count),
					stopRamindContent = i18n("dont_remind_session"),
					onYes = function()
						arg_21_0:emit(BuildShipDetailMediator.ON_QUICK, arg_21_1, var_23_3.stopRemindToggle.isOn)
					end
				})
			end
		end, SFX_UI_BUILDING_FASTBUILDING)

		local function var_21_11()
			pg.TimeMgr.GetInstance():RemoveTimer(arg_21_0.buildTimers[arg_21_1])

			arg_21_0.buildTimers[arg_21_1] = nil

			setActive(var_21_1, false)
			setActive(var_21_2, true)
		end

		local function var_21_12(arg_26_0)
			local var_26_0 = pg.TimeMgr.GetInstance():DescCDTime(arg_26_0)

			setText(var_21_10, var_26_0)
		end

		if arg_21_0.buildTimers[arg_21_1] then
			pg.TimeMgr.GetInstance():RemoveTimer(arg_21_0.buildTimers[arg_21_1])

			arg_21_0.buildTimers[arg_21_1] = nil
		end

		arg_21_0.buildTimers[arg_21_1] = pg.TimeMgr.GetInstance():AddTimer("timer" .. arg_21_1, 0, 1, function()
			local var_27_0 = arg_21_2:getLeftTime()

			if var_27_0 <= 0 then
				var_21_11()
			else
				var_21_12(var_27_0)
			end
		end)
	elseif arg_21_2.state == BuildShip.FINISH then
		GetOrAddComponent(var_21_1, typeof(CanvasGroup)).alpha = 0

		setActive(var_21_1, true)

		local var_21_13 = arg_21_0:findTF("shipModelBuliding" .. var_21_5, var_21_6)

		if var_21_13 then
			setActive(var_21_13, true)
		end

		arg_21_0:setSpriteTo(var_0_5[tonumber(var_21_4.ship_icon)], arg_21_0:findTF("ship_modal", var_21_2), false)

		local var_21_14 = findTF(var_21_2, "launched_btn")

		onButton(arg_21_0, var_21_14, function()
			arg_21_0:emit(BuildShipDetailMediator.ON_LAUNCHED, arg_21_1)
		end, SFX_PANEL)
		onButton(arg_21_0, var_21_0, function()
			triggerButton(var_21_14)
		end, SFX_PANEL)
	elseif arg_21_2.state == BuildShip.INACTIVE then
		setActive(var_21_3, true)
		setActive(var_21_1, false)
		setActive(var_21_2, false)
	end
end

function var_0_0.playGetShipAnimate(arg_30_0, arg_30_1, arg_30_2)
	arg_30_0.canvasgroup.blocksRaycasts = false

	local var_30_0 = pg.ship_data_create_material[arg_30_2]

	arg_30_0.isPlayAnim = true
	arg_30_0.onLoading = true

	pg.CpkPlayMgr.GetInstance():PlayCpkMovie(function()
		arg_30_0.onLoading = false

		if var_30_0 and var_30_0.build_voice ~= "" then
			arg_30_0:playCV(var_30_0.build_voice)
		end
	end, function()
		arg_30_0.isPlayAnim = false
		arg_30_0.canvasgroup.blocksRaycasts = true

		arg_30_1()
	end, "ui", var_30_0.build_anim or "Building", true, false, {
		weight = LayerWeightConst.SECOND_LAYER
	}, 4.5, true)
end

function var_0_0.willExit(arg_33_0)
	pg.CpkPlayMgr.GetInstance():DisposeCpkMovie()

	for iter_33_0, iter_33_1 in pairs(arg_33_0.buildTimers) do
		pg.TimeMgr.GetInstance():RemoveTimer(iter_33_1)
	end

	if arg_33_0.aniBgTF then
		SetParent(arg_33_0.aniBgTF, arg_33_0._tf)
	end

	arg_33_0.buildTimers = nil

	arg_33_0:stopCV()

	arg_33_0.onLoading = false

	arg_33_0.multList:each(function(arg_34_0, arg_34_1)
		local var_34_0 = arg_33_0:findTF("frame/buiding/ship_modal", arg_34_1)

		eachChild(var_34_0, function(arg_35_0)
			PoolMgr.GetInstance():ReturnUI(arg_35_0.name, arg_35_0)
		end)
	end)
	arg_33_0.singleList:each(function(arg_36_0, arg_36_1)
		local var_36_0 = arg_33_0:findTF("frame/buiding/ship_modal", arg_36_1)

		eachChild(var_36_0, function(arg_37_0)
			PoolMgr.GetInstance():ReturnUI(arg_37_0.name, arg_37_0)
		end)
	end)
end

function var_0_0.playCV(arg_38_0, arg_38_1)
	arg_38_0:stopCV()

	local var_38_0 = "event:/cv/build/" .. arg_38_1

	pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_38_0)

	arg_38_0.voiceContent = var_38_0
end

function var_0_0.stopCV(arg_39_0)
	if arg_39_0.voiceContent then
		pg.CriMgr.GetInstance():UnloadSoundEffect_V3(arg_39_0.voiceContent)
	end

	arg_39_0.voiceContent = nil
end

return var_0_0
