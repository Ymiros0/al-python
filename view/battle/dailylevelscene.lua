local var_0_0 = class("DailyLevelScene", import("..base.BaseUI"))
local var_0_1 = 3
local var_0_2 = 4
local var_0_3 = 101

function var_0_0.getUIName(arg_1_0)
	return "dailylevelui"
end

function var_0_0.ResUISettings(arg_2_0)
	return true
end

function var_0_0.init(arg_3_0)
	arg_3_0.blurPanel = arg_3_0:findTF("blur_panel")
	arg_3_0.topPanel = arg_3_0:findTF("blur_panel/adapt/top")
	arg_3_0.backBtn = arg_3_0:findTF("back_button", arg_3_0.topPanel)
	arg_3_0.listPanel = arg_3_0:findTF("list_panel")
	arg_3_0.content = arg_3_0:findTF("list", arg_3_0.listPanel)

	setActive(arg_3_0.content, true)

	arg_3_0.dailylevelTpl = arg_3_0:getTpl("list_panel/list/captertpl")
	arg_3_0.descPanel = arg_3_0:findTF("desc_panel")
	arg_3_0.selectedPanel = arg_3_0.descPanel:Find("selected")
	arg_3_0.descMain = arg_3_0:findTF("main_mask/main", arg_3_0.descPanel)
	arg_3_0.stageTpl = arg_3_0:getTpl("scrollview/content/stagetpl", arg_3_0.descMain)
	arg_3_0.stageScrollRect = arg_3_0:findTF("scrollview", arg_3_0.descMain):GetComponent(typeof(ScrollRect))
	arg_3_0.stageContain = arg_3_0:findTF("scrollview/content", arg_3_0.descMain)
	arg_3_0.arrows = arg_3_0:findTF("arrows")
	arg_3_0.itemTpl = arg_3_0:getTpl("item_tpl")
	arg_3_0.selStageTF = arg_3_0.selectedPanel:Find("stagetpl/info")
	arg_3_0.selQuicklyTF = arg_3_0.selStageTF.parent:Find("quickly/bg")
	arg_3_0.selQuicklyTFSizeDeltaY = arg_3_0.selQuicklyTF.sizeDelta.y
	arg_3_0.descChallengeNum = arg_3_0:findTF("challenge_count", arg_3_0.descMain)
	arg_3_0.descChallengeText = arg_3_0:findTF("Text", arg_3_0.descChallengeNum)
	arg_3_0.challengeQuotaDaily = arg_3_0:findTF("challenge_count/label", arg_3_0.descMain)
	arg_3_0.challengeQuotaWeekly = arg_3_0:findTF("challenge_count/week_label", arg_3_0.descMain)
	arg_3_0.fleetEditView = arg_3_0:findTF("fleet_edit")
	arg_3_0.resource = arg_3_0:findTF("resource")
	arg_3_0.rightBtn = arg_3_0:findTF("arrows/arrow1")
	arg_3_0.leftBtn = arg_3_0:findTF("arrows/arrow2")

	arg_3_0:initItems()
end

function var_0_0.getWeek()
	return (pg.TimeMgr.GetInstance():GetServerWeek())
end

function var_0_0.setDailyCounts(arg_5_0, arg_5_1)
	arg_5_0.dailyCounts = arg_5_1
end

function var_0_0.setShips(arg_6_0, arg_6_1)
	arg_6_0.shipVOs = arg_6_1
end

function var_0_0.updateRes(arg_7_0, arg_7_1)
	arg_7_0.player = arg_7_1
end

function var_0_0.didEnter(arg_8_0)
	onButton(arg_8_0, arg_8_0:findTF("help_btn"), function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.help_daily_task.tip
		})
	end, SFX_PANEL)
	onButton(arg_8_0, arg_8_0.backBtn, function()
		if arg_8_0.descMode then
			if LeanTween.isTweening(go(arg_8_0.stageContain)) or LeanTween.isTweening(go(arg_8_0.selQuicklyTF)) then
				return
			end

			arg_8_0:enableDescMode(false)
		else
			arg_8_0:emit(var_0_0.ON_BACK)
		end
	end, SFX_CANCEL)
	onButton(arg_8_0, arg_8_0.leftBtn, function()
		arg_8_0:flipToSpecificCard(arg_8_0:getNextCardId(true))
	end)
	onButton(arg_8_0, arg_8_0.rightBtn, function()
		arg_8_0:flipToSpecificCard(arg_8_0:getNextCardId(false))
	end)
	arg_8_0:displayDailyLevels()

	if arg_8_0.contextData.dailyLevelId then
		arg_8_0:tryOpenDesc(arg_8_0.contextData.dailyLevelId)
	else
		arg_8_0:enableDescMode(false)
	end

	arg_8_0:tryPlayGuide()
	arg_8_0:ShowGuildTaskTip()
end

function var_0_0.initItems(arg_13_0)
	local var_13_0 = getProxy(DailyLevelProxy)

	var_13_0:setDailyTip(false)

	arg_13_0.dailyCounts = var_13_0:getRawData()

	local var_13_1 = pg.expedition_daily_template

	arg_13_0.dailyLevelTFs = {}
	arg_13_0.dailyList = _.reverse(Clone(var_13_1.all))

	for iter_13_0 = #arg_13_0.dailyList, 1, -1 do
		local var_13_2 = var_13_1[arg_13_0.dailyList[iter_13_0]].limit_period
		local var_13_3 = var_13_1[arg_13_0.dailyList[iter_13_0]].insert_daily

		if var_13_2 and type(var_13_2) == "table" then
			if not pg.TimeMgr:GetInstance():inTime(var_13_2) then
				table.remove(arg_13_0.dailyList, iter_13_0)
			end
		elseif var_13_3 == 1 then
			table.remove(arg_13_0.dailyList, iter_13_0)
		end
	end

	arg_13_0:sortDailyList()
	arg_13_0:updateShowCenter()

	if arg_13_0.contextData.dailyLevelId then
		local var_13_4 = arg_13_0.contextData.dailyLevelId

		table.removebyvalue(arg_13_0.dailyList, var_13_4)
		table.insert(arg_13_0.dailyList, math.ceil(#var_13_1.all / 2), var_13_4)
	end

	for iter_13_1, iter_13_2 in pairs(arg_13_0.dailyList) do
		arg_13_0.dailyLevelTFs[iter_13_2] = cloneTplTo(arg_13_0.dailylevelTpl, arg_13_0.content, iter_13_2)
	end
end

function var_0_0.sortDailyList(arg_14_0)
	if #arg_14_0.dailyList % 2 ~= 1 then
		table.insert(arg_14_0.dailyList, var_0_3)
	end

	table.sort(arg_14_0.dailyList, function(arg_15_0, arg_15_1)
		return tonumber(pg.expedition_daily_template[arg_15_0].sort) > tonumber(pg.expedition_daily_template[arg_15_1].sort)
	end)
end

function var_0_0.updateShowCenter(arg_16_0)
	if not arg_16_0.dailyList or #arg_16_0.dailyList == 0 then
		return
	end

	local var_16_0 = #arg_16_0.dailyList
	local var_16_1 = pg.expedition_daily_template
	local var_16_2 = math.ceil(var_16_0 / 2)
	local var_16_3

	for iter_16_0 = 1, var_16_0 do
		local var_16_4 = var_16_1[arg_16_0.dailyList[iter_16_0]]

		if var_16_4.show_with_count and var_16_4.show_with_count == 1 then
			local var_16_5 = var_16_4.id
			local var_16_6 = arg_16_0.dailyCounts and arg_16_0.dailyCounts[var_16_5] or 0

			if var_16_4.limit_time - var_16_6 > 0 then
				var_16_3 = var_16_3 or iter_16_0
			end
		end
	end

	if var_16_3 then
		local var_16_7 = var_16_2 - var_16_3 < 0 and true or false
		local var_16_8 = math.abs(var_16_2 - var_16_3)

		for iter_16_1 = 1, var_16_8 do
			local var_16_9

			if var_16_7 then
				local var_16_10 = table.remove(arg_16_0.dailyList, 1)

				table.insert(arg_16_0.dailyList, var_16_10)
			else
				local var_16_11 = table.remove(arg_16_0.dailyList, #arg_16_0.dailyList)

				table.insert(arg_16_0.dailyList, 1, var_16_11)
			end
		end
	end
end

function var_0_0.displayDailyLevels(arg_17_0)
	for iter_17_0, iter_17_1 in pairs(arg_17_0.dailyLevelTFs) do
		arg_17_0:initDailyLevel(iter_17_0)
	end

	arg_17_0.content:GetComponent(typeof(EnhancelScrollView)).onCenterClick = function(arg_18_0)
		arg_17_0:tryOpenDesc(tonumber(arg_18_0.name))
	end
	arg_17_0.centerAniItem = nil
	arg_17_0.centerCardId = nil
	arg_17_0.checkAniTimer = Timer.New(function()
		if not arg_17_0.descMode then
			local var_19_0
			local var_19_1

			for iter_19_0, iter_19_1 in pairs(arg_17_0.dailyLevelTFs) do
				GetComponent(iter_19_1, typeof(CanvasGroup)).alpha = 1

				if not var_19_0 and not var_19_1 then
					var_19_0 = iter_19_1
					var_19_1 = iter_19_1
				elseif iter_19_1.anchoredPosition.x < var_19_0.anchoredPosition.x then
					var_19_0 = iter_19_1
				elseif iter_19_1.anchoredPosition.x > var_19_1.anchoredPosition.x then
					var_19_1 = iter_19_1
				end
			end

			GetComponent(var_19_0, typeof(CanvasGroup)).alpha = 0.5
			GetComponent(var_19_1, typeof(CanvasGroup)).alpha = 0.5
		end

		for iter_19_2, iter_19_3 in pairs(arg_17_0.dailyLevelTFs) do
			local var_19_2 = iter_19_3.localScale.x >= 0.98

			if arg_17_0.centerAniItem == iter_19_3 and var_19_2 then
				return
			else
				if var_19_2 then
					arg_17_0.centerAniItem = iter_19_3
					arg_17_0.centerCardId = iter_19_2
				end

				local var_19_3 = arg_17_0:findTF("icon/card", iter_19_3)

				if var_19_3 then
					local var_19_4 = arg_17_0:findTF("mask/char", var_19_3):GetComponent(typeof(Animator))
					local var_19_5 = arg_17_0:findTF("effect", var_19_3)

					setActive(var_19_5, var_19_2)

					if var_19_4 then
						var_19_4.speed = var_19_2 and 1 or 0
					end
				end
			end
		end
	end, 0.1, -1)

	arg_17_0.checkAniTimer:Start()
end

function var_0_0.tryOpenDesc(arg_20_0, arg_20_1)
	local var_20_0 = arg_20_0.dailyLevelTFs[arg_20_1]
	local var_20_1 = pg.expedition_daily_template[arg_20_1]

	if table.contains(var_20_1.weekday, tonumber(arg_20_0:getWeek())) then
		arg_20_0:openDailyDesc(arg_20_1)
	else
		pg.TipsMgr.GetInstance():ShowTips(var_20_1.tips)
	end
end

function var_0_0.CanOpenDailyLevel(arg_21_0)
	local var_21_0 = pg.expedition_daily_template[arg_21_0]
	local var_21_1 = false

	if table.contains(var_21_0.weekday, tonumber(var_0_0.getWeek())) then
		var_21_1 = true
	end

	return var_21_1, var_21_0.tips
end

function var_0_0.getNextCardId(arg_22_0, arg_22_1)
	local var_22_0 = table.indexof(arg_22_0.dailyList, arg_22_0.centerCardId)

	if arg_22_1 then
		var_22_0 = var_22_0 - 1

		if var_22_0 <= 0 then
			var_22_0 = #arg_22_0.dailyList or var_22_0
		end
	else
		var_22_0 = var_22_0 + 1
		var_22_0 = var_22_0 > #arg_22_0.dailyList and 1 or var_22_0
	end

	return arg_22_0.dailyList[var_22_0]
end

function var_0_0.initDailyLevel(arg_23_0, arg_23_1)
	local var_23_0 = pg.expedition_daily_template[arg_23_1]
	local var_23_1 = arg_23_0.dailyLevelTFs[arg_23_1]
	local var_23_2 = table.contains(var_23_0.weekday, tonumber(arg_23_0:getWeek()))

	if var_23_2 then
		arg_23_0.index = arg_23_1
	end

	setActive(findTF(var_23_1, "lock"), not var_23_2 and not table.isEmpty(var_23_0.weekday))
	setText(findTF(var_23_1, "name"), var_23_0.title)
	setActive(findTF(var_23_1, "time"), false)

	local var_23_3 = findTF(var_23_1, "icon")

	PoolMgr.GetInstance():GetPrefab("dailyui/" .. var_23_0.pic, "", true, function(arg_24_0)
		arg_24_0 = tf(arg_24_0)

		arg_24_0:SetParent(var_23_3, false)

		arg_24_0.localPosition = Vector3.zero
		arg_24_0.name = "card"
	end)
	setText(findTF(var_23_1, "Text"), "")
	setActive(findTF(var_23_1, "lastTime"), false)

	local var_23_4 = Clone(var_23_0.limit_period)
	local var_23_5

	if var_23_4 and type(var_23_4) == "table" and pg.TimeMgr:GetInstance():inTime(var_23_4) then
		local var_23_6 = pg.TimeMgr:GetInstance():GetServerTime()

		var_23_5 = pg.TimeMgr:GetInstance():Table2ServerTime({
			year = var_23_4[2][1][1],
			month = var_23_4[2][1][2],
			day = var_23_4[2][1][3],
			hour = var_23_4[2][2][1],
			min = var_23_4[2][2][2],
			sec = var_23_4[2][2][3]
		}) - var_23_6
	end

	if var_23_5 then
		local var_23_7 = ""
		local var_23_8 = ""

		if var_23_5 > 86400 then
			var_23_7 = math.floor(tonumber(var_23_5) / 86400)
			var_23_8 = i18n("word_date")
		elseif var_23_5 >= 3600 then
			var_23_7 = math.floor(tonumber(var_23_5) / 3600)
			var_23_8 = i18n("word_hour")
		elseif var_23_5 > 0 then
			var_23_7 = math.floor(tonumber(var_23_5) / 60)
			var_23_8 = i18n("word_minute")
		end

		setText(findTF(var_23_1, "lastTime/content/text"), tostring(var_23_7) .. " ")
		setText(findTF(var_23_1, "lastTime/content/word"), tostring(var_23_8))
		setActive(findTF(var_23_1, "lastTime"), true)
	end

	arg_23_0:UpdateDailyLevelCnt(arg_23_1)
end

function var_0_0.UpdateDailyLevelCnt(arg_25_0, arg_25_1)
	local var_25_0 = pg.expedition_daily_template[arg_25_1]
	local var_25_1 = arg_25_0.dailyLevelTFs[arg_25_1]
	local var_25_2 = findTF(var_25_1, "count")
	local var_25_3 = arg_25_0.dailyCounts[arg_25_1] or 0

	if var_25_0.limit_time == 0 then
		setText(var_25_2, "N/A")
	else
		setText(var_25_2, string.format("%d/%d", var_25_0.limit_time - var_25_3, var_25_0.limit_time))
	end

	setActive(var_25_2, var_25_0.limit_time > 0)
end

function var_0_0.openDailyDesc(arg_26_0, arg_26_1)
	arg_26_0.curId = arg_26_1

	arg_26_0:enableDescMode(true)
	arg_26_0:displayStageList(arg_26_1)
end

function var_0_0.UpdateDailyLevelCntForDescPanel(arg_27_0, arg_27_1)
	local var_27_0 = pg.expedition_daily_template[arg_27_1]
	local var_27_1 = arg_27_0.dailyCounts[arg_27_1] or 0

	if var_27_0.limit_time == 0 then
		setText(arg_27_0.descChallengeText, i18n("challenge_count_unlimit"))
	else
		setText(arg_27_0.descChallengeText, string.format("%d/%d", var_27_0.limit_time - var_27_1, var_27_0.limit_time))
	end
end

function var_0_0.displayStageList(arg_28_0, arg_28_1)
	arg_28_0.dailyLevelId = arg_28_1
	arg_28_0.contextData.dailyLevelId = arg_28_0.dailyLevelId

	local var_28_0 = pg.expedition_daily_template[arg_28_1]

	arg_28_0:UpdateDailyLevelCntForDescPanel(arg_28_1)
	setActive(arg_28_0.challengeQuotaDaily, var_28_0.limit_type == 1)
	setActive(arg_28_0.challengeQuotaWeekly, var_28_0.limit_type == 2)
	removeAllChildren(arg_28_0.stageContain)

	arg_28_0.stageTFs = {}

	local var_28_1 = _.sort(var_28_0.expedition_and_lv_limit_list, function(arg_29_0, arg_29_1)
		local var_29_0 = arg_29_0[2] <= arg_28_0.player.level and 1 or 0
		local var_29_1 = arg_29_1[2] <= arg_28_0.player.level and 1 or 0

		if arg_29_0[2] == arg_29_1[2] then
			return arg_29_0[1] < arg_29_1[1]
		end

		if var_29_0 == var_29_1 then
			if var_29_0 == 1 then
				return arg_29_0[2] > arg_29_1[2]
			else
				return arg_29_0[2] < arg_29_1[2]
			end
		else
			return var_29_1 < var_29_0
		end
	end)

	for iter_28_0, iter_28_1 in ipairs(var_28_1) do
		local var_28_2 = iter_28_1[1]
		local var_28_3 = iter_28_1[2]

		arg_28_0.stageTFs[var_28_2] = cloneTplTo(arg_28_0.stageTpl, arg_28_0.stageContain)

		local var_28_4 = {
			id = var_28_2,
			level = var_28_3
		}

		arg_28_0:updateStage(var_28_4)
	end
end

function var_0_0.updateStageTF(arg_30_0, arg_30_1, arg_30_2)
	local var_30_0 = pg.expedition_data_template[arg_30_2.id]

	setText(findTF(arg_30_1, "left_panel/name"), var_30_0.name)
	setText(findTF(arg_30_1, "left_panel/lv/Text"), "Lv." .. arg_30_2.level)

	local var_30_1 = arg_30_0:findTF("mask", arg_30_1)

	setActive(var_30_1, arg_30_2.level > arg_30_0.player.level)

	if arg_30_2.level > arg_30_0.player.level then
		setText(arg_30_0:findTF("msg/msg_contain/Text", var_30_1), "Lv." .. arg_30_2.level .. " ")

		if PLATFORM_CODE == PLATFORM_US then
			arg_30_0:findTF("msg/msg_contain/Text", var_30_1):SetAsLastSibling()
		end
	end

	local var_30_2 = UIItemList.New(arg_30_0:findTF("scrollView/right_panel", arg_30_1), arg_30_0.itemTpl)

	var_30_2:make(function(arg_31_0, arg_31_1, arg_31_2)
		if arg_31_0 == UIItemList.EventUpdate then
			local var_31_0 = var_30_0.award_display[arg_31_1 + 1]

			updateDrop(arg_31_2, {
				type = var_31_0[1],
				id = var_31_0[2],
				count = var_31_0[3]
			})
			setActive(arg_31_2, arg_31_1 <= 3)
		end
	end)
	var_30_2:align(#var_30_0.award_display)
	setImageSprite(arg_30_1, getImageSprite(findTF(arg_30_0.resource, "normal_bg")))
	setActive(findTF(arg_30_1, "score"), false)
	onButton(arg_30_0, var_30_1, function()
		pg.TipsMgr.GetInstance():ShowTips(i18n("dailyLevel_unopened"))
	end, SFX_PANEL)
end

function var_0_0.updateStage(arg_33_0, arg_33_1)
	local var_33_0 = arg_33_0.stageTFs[arg_33_1.id]:Find("info")

	arg_33_0:updateStageTF(var_33_0, arg_33_1)
	onButton(arg_33_0, var_33_0, function()
		if getProxy(DailyLevelProxy):CanQuickBattle(arg_33_1.id) then
			local var_34_0 = pg.expedition_daily_template[arg_33_0.dailyLevelId]

			if (arg_33_0.dailyCounts[arg_33_0.dailyLevelId] or 0) >= var_34_0.limit_time then
				pg.TipsMgr.GetInstance():ShowTips(i18n("dailyLevel_restCount_notEnough"))

				return
			end

			if LeanTween.isTweening(go(arg_33_0.descMain)) or LeanTween.isTweening(go(arg_33_0.listPanel)) then
				return
			end

			arg_33_0:OnSelectStage(arg_33_1)
		else
			arg_33_0:OnOpenPreCombat(arg_33_1)
		end
	end, SFX_PANEL)
end

function var_0_0.OnOpenPreCombat(arg_35_0, arg_35_1)
	local var_35_0 = pg.expedition_daily_template[arg_35_0.dailyLevelId]

	if (arg_35_0.dailyCounts[arg_35_0.dailyLevelId] or 0) >= var_35_0.limit_time then
		pg.TipsMgr.GetInstance():ShowTips(i18n("dailyLevel_restCount_notEnough"))

		return
	end

	setActive(arg_35_0.blurPanel, false)
	arg_35_0:emit(DailyLevelMediator.ON_STAGE, arg_35_1)
end

function var_0_0.OnSelectStage(arg_36_0, arg_36_1)
	local var_36_0 = arg_36_0.selectedPanel:Find("stagetpl/info")

	onButton(arg_36_0, var_36_0, function()
		arg_36_0:EnableOrDisable(arg_36_1, false)
	end, SFX_PANEL)
	onButton(arg_36_0, arg_36_0.selectedPanel, function()
		arg_36_0:EnableOrDisable(arg_36_1, false)
	end, SFX_PANEL)
	arg_36_0:EnableOrDisable(arg_36_1, true)
end

function var_0_0.EnableOrDisable(arg_39_0, arg_39_1, arg_39_2)
	local var_39_0 = arg_39_0.stageTFs[arg_39_1.id]:Find("quickly")

	if LeanTween.isTweening(go(arg_39_0.stageContain)) or LeanTween.isTweening(go(arg_39_0.selQuicklyTF)) then
		return
	end

	local var_39_1 = arg_39_0.stageContain:GetComponent(typeof(VerticalLayoutGroup)).padding.top
	local var_39_2 = arg_39_0.stageContain.parent:InverseTransformPoint(var_39_0.parent.position)
	local var_39_3 = -1 * var_39_1 - var_39_2.y

	if arg_39_2 then
		arg_39_0:updateStageTF(arg_39_0.selStageTF, arg_39_1)
		arg_39_0:UpdateBattleBtn(arg_39_1)
		arg_39_0:DoSelectedAnimation(var_39_0, var_39_3, function()
			arg_39_0.selectedStage = arg_39_1
		end)
	else
		arg_39_0:DoUnselectAnimtion(var_39_0, function()
			arg_39_0.selectedStage = nil
		end)
	end
end

function var_0_0.DoSelectedAnimation(arg_42_0, arg_42_1, arg_42_2, arg_42_3)
	local var_42_0 = math.abs(arg_42_2) / 2000

	seriesAsync({
		function(arg_43_0)
			arg_42_0.stageScrollRect.enabled = false

			pg.UIMgr.GetInstance():BlurPanel(arg_42_0.selectedPanel, true, {
				groupName = LayerWeightConst.GROUP_DAILY,
				weight = LayerWeightConst.BASE_LAYER - 1
			})

			arg_42_1.sizeDelta = Vector2(arg_42_1.sizeDelta.x, 0)

			setActive(arg_42_1, true)

			local var_43_0 = arg_42_0.stageContain.anchoredPosition

			arg_42_0.stageContainLposY = var_43_0.y
			arg_42_0.offsetY = arg_42_2

			LeanTween.value(go(arg_42_0.stageContain), var_43_0.y, var_43_0.y + arg_42_2, var_42_0):setOnUpdate(System.Action_float(function(arg_44_0)
				arg_42_0.stageContain.anchoredPosition = Vector3(var_43_0.x, arg_44_0, 0)

				local var_44_0 = arg_42_0.selectedPanel:InverseTransformPoint(arg_42_1.parent.position)

				arg_42_0.selStageTF.parent.localPosition = Vector3(var_44_0.x, var_44_0.y, 0)
				arg_42_0.selQuicklyTF.sizeDelta = Vector2(arg_42_0.selQuicklyTF.sizeDelta.x, 0)

				setActive(arg_42_0.selectedPanel, true)
			end)):setEase(LeanTweenType.easeInOutCirc):setOnComplete(System.Action(arg_43_0))
		end,
		function(arg_45_0)
			local var_45_0 = arg_42_1:GetComponent(typeof(LayoutElement))

			LeanTween.value(go(arg_42_0.selQuicklyTF), 0, arg_42_0.selQuicklyTFSizeDeltaY, 0.1):setOnUpdate(System.Action_float(function(arg_46_0)
				var_45_0.preferredHeight = arg_46_0
				arg_42_0.selQuicklyTF.sizeDelta = Vector2(arg_42_0.selQuicklyTF.sizeDelta.x, arg_46_0)
			end)):setEase(LeanTweenType.easeInOutCirc):setOnComplete(System.Action(arg_45_0))
		end
	}, arg_42_3)
end

function var_0_0.DoUnselectAnimtion(arg_47_0, arg_47_1, arg_47_2)
	local var_47_0 = arg_47_0.stageContain.anchoredPosition

	seriesAsync({
		function(arg_48_0)
			pg.UIMgr.GetInstance():UnblurPanel(arg_47_0.selectedPanel, arg_47_0._tf)
			setActive(arg_47_0.selectedPanel, false)

			local var_48_0 = arg_47_1:GetComponent(typeof(LayoutElement))

			LeanTween.value(go(arg_47_0.selQuicklyTF), arg_47_0.selQuicklyTFSizeDeltaY, 0, 0.1):setOnUpdate(System.Action_float(function(arg_49_0)
				var_48_0.preferredHeight = arg_49_0
				arg_47_0.selQuicklyTF.sizeDelta = Vector2(arg_47_0.selQuicklyTF.sizeDelta.x, arg_49_0)
			end)):setEase(LeanTweenType.easeInOutCirc):setOnComplete(System.Action(arg_48_0))
		end,
		function(arg_50_0)
			local var_50_0 = var_47_0.y - arg_47_0.offsetY
			local var_50_1 = var_50_0 / 2000

			LeanTween.value(go(arg_47_0.stageContain), var_47_0.y, var_50_0, 0.15):setOnUpdate(System.Action_float(function(arg_51_0)
				arg_47_0.stageContain.anchoredPosition = Vector3(var_47_0.x, arg_51_0, 0)
			end)):setDelay(0.1):setEase(LeanTweenType.easeInOutCirc):setOnComplete(System.Action(arg_50_0))
		end
	}, function()
		arg_47_0.stageScrollRect.enabled = true

		arg_47_2()
	end)
end

function var_0_0.UpdateBattleBtn(arg_53_0, arg_53_1)
	local var_53_0 = arg_53_0.selectedPanel:Find("stagetpl/info").parent:Find("quickly/bg")
	local var_53_1 = pg.expedition_daily_template[arg_53_0.dailyLevelId].limit_time - (arg_53_0.dailyCounts[arg_53_0.dailyLevelId] or 0)
	local var_53_2 = var_53_0:Find("challenge")

	onButton(arg_53_0, var_53_2, function()
		arg_53_0:OnOpenPreCombat(arg_53_1)
	end, SFX_PANEL)
	setText(var_53_2:Find("Text"), i18n("daily_level_quick_battle_label2"))

	local var_53_3 = var_53_0:Find("mult")

	onButton(arg_53_0, var_53_3, function()
		arg_53_0:OnQuickBattle(arg_53_1, var_53_1)
	end, SFX_PANEL)

	local var_53_4 = var_53_0:Find("once")

	onButton(arg_53_0, var_53_4, function()
		arg_53_0:OnQuickBattle(arg_53_1, 1)
	end, SFX_PANEL)
	setText(var_53_3:Find("label"), i18n("daily_level_quick_battle_label1", "   ", COLOR_WHITE))
	setText(var_53_3:Find("Text"), "<color=" .. COLOR_GREEN .. ">" .. math.max(1, var_53_1) .. "</color>")
	setText(var_53_4:Find("label"), i18n("daily_level_quick_battle_label3"))
	setText(var_53_4:Find("Text"), "")

	if var_53_1 == 0 then
		arg_53_0:EnableOrDisable(arg_53_1, false)
	end
end

function var_0_0.OnQuickBattle(arg_57_0, arg_57_1, arg_57_2)
	if arg_57_2 <= 0 then
		pg.TipsMgr.GetInstance():ShowTips(i18n("dailyLevel_restCount_notEnough"))

		return
	end

	if PlayerPrefs.GetInt("daily_level_quick_battle_tip", 0) == 0 then
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			content = i18n("dailyLevel_quickfinish"),
			onYes = function()
				arg_57_0:emit(DailyLevelMediator.ON_QUICK_BATTLE, arg_57_0.dailyLevelId, arg_57_1.id, arg_57_2)
			end
		})
		PlayerPrefs.SetInt("daily_level_quick_battle_tip", 1)
		PlayerPrefs.Save()
	else
		arg_57_0:emit(DailyLevelMediator.ON_QUICK_BATTLE, arg_57_0.dailyLevelId, arg_57_1.id, arg_57_2)
	end
end

function var_0_0.enableDescMode(arg_59_0, arg_59_1, arg_59_2)
	arg_59_0.descMode = arg_59_1

	setActive(arg_59_0:findTF("help_btn"), not arg_59_1)

	local function var_59_0(arg_60_0, arg_60_1, arg_60_2)
		if LeanTween.isTweening(go(arg_60_0)) then
			LeanTween.cancel(go(arg_60_0))
		end

		LeanTween.moveX(rtf(arg_60_0), arg_60_1, 0.3):setEase(LeanTweenType.linear):setOnComplete(System.Action(function()
			if arg_60_2 then
				arg_60_2()
			end
		end))
	end

	local function var_59_1()
		for iter_62_0, iter_62_1 in pairs(arg_59_0.dailyLevelTFs) do
			setButtonEnabled(iter_62_1, not arg_59_1)

			if iter_62_0 ~= arg_59_0.curId then
				if LeanTween.isTweening(go(iter_62_1)) then
					LeanTween.cancel(go(iter_62_1))
				end

				local var_62_0 = GetComponent(iter_62_1, typeof(CanvasGroup))

				if arg_59_1 then
					LeanTween.value(go(iter_62_1), 1, 0, 0.3):setOnUpdate(System.Action_float(function(arg_63_0)
						var_62_0.alpha = arg_63_0
					end))
				else
					LeanTween.value(go(iter_62_1), 0, 1, 0.3):setOnUpdate(System.Action_float(function(arg_64_0)
						var_62_0.alpha = arg_64_0
					end))
				end
			end
		end
	end

	local function var_59_2()
		setActive(arg_59_0.listPanel, true)
		setActive(arg_59_0.content, true)
		setActive(arg_59_0.descPanel, arg_59_1)
		setActive(arg_59_0.arrows, not arg_59_1)
	end

	if arg_59_1 then
		var_59_2()
		var_59_1()
		var_59_0(arg_59_0.listPanel, -622, function()
			var_59_0(arg_59_0.descMain, 0, arg_59_2)
		end)
	else
		if arg_59_0.selectedStage then
			arg_59_0:EnableOrDisable(arg_59_0.selectedStage, false)
		end

		var_59_2()
		var_59_1()
		var_59_0(arg_59_0.listPanel, 0)
		var_59_0(arg_59_0.descMain, -1342, arg_59_2)
	end
end

function var_0_0.flipToSpecificCard(arg_67_0, arg_67_1)
	local var_67_0 = arg_67_0.content:GetComponent(typeof(EnhancelScrollView))

	for iter_67_0, iter_67_1 in pairs(arg_67_0.dailyLevelTFs) do
		if arg_67_1 == iter_67_0 then
			local var_67_1 = iter_67_1:GetComponent(typeof(EnhanceItem))

			var_67_0:SetHorizontalTargetItemIndex(var_67_1.scrollViewItemIndex)
		end
	end
end

function var_0_0.tryPlayGuide(arg_68_0)
	pg.SystemGuideMgr.GetInstance():PlayDailyLevel(function()
		triggerButton(arg_68_0:findTF("help_btn"))
	end)
end

function var_0_0.ShowGuildTaskTip(arg_70_0)
	pg.GuildMsgBoxMgr.GetInstance():NotificationForDailyBattle()
end

function var_0_0.clearTween(arg_71_0)
	if arg_71_0.tweens then
		cancelTweens(arg_71_0.tweens)
	end

	local function var_71_0(arg_72_0)
		if LeanTween.isTweening(go(arg_72_0)) then
			LeanTween.cancel(go(arg_72_0))
		end
	end

	for iter_71_0, iter_71_1 in pairs(arg_71_0.dailyLevelTFs) do
		var_71_0(iter_71_1)
	end

	var_71_0(arg_71_0.listPanel)
	var_71_0(arg_71_0.descMain)
end

function var_0_0.onBackPressed(arg_73_0)
	if arg_73_0.descMode then
		if LeanTween.isTweening(go(arg_73_0.stageContain)) or LeanTween.isTweening(go(arg_73_0.selQuicklyTF)) then
			return
		end

		arg_73_0:enableDescMode(false)

		return
	end

	var_0_0.super.onBackPressed(arg_73_0)
end

function var_0_0.willExit(arg_74_0)
	if arg_74_0.selectedStage then
		pg.UIMgr.GetInstance():UnblurPanel(arg_74_0.selectedPanel, arg_74_0._tf)
	end

	arg_74_0:clearTween()

	if arg_74_0.checkAniTimer then
		arg_74_0.checkAniTimer:Stop()

		arg_74_0.checkAniTimer = nil
	end
end

return var_0_0
