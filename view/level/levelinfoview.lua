local var_0_0 = class("LevelInfoView", import("..base.BaseSubView"))

function var_0_0.getUIName(arg_1_0)
	return "LevelStageInfoView"
end

function var_0_0.OnInit(arg_2_0)
	arg_2_0:InitUI()
end

function var_0_0.OnDestroy(arg_3_0)
	if arg_3_0:isShowing() then
		arg_3_0:Hide()
	end

	arg_3_0.onConfirm = nil
	arg_3_0.onCancel = nil

	if arg_3_0.LTid then
		LeanTween.cancel(arg_3_0.LTid)

		arg_3_0.LTid = nil
	end
end

function var_0_0.Show(arg_4_0)
	setActive(arg_4_0._tf, true)
	pg.UIMgr.GetInstance():BlurPanel(arg_4_0._tf)
end

function var_0_0.Hide(arg_5_0)
	arg_5_0:clear()
	setActive(arg_5_0._tf, false)
	pg.UIMgr.GetInstance():UnblurPanel(arg_5_0._tf, arg_5_0._parentTf)
end

function var_0_0.setCBFunc(arg_6_0, arg_6_1, arg_6_2)
	arg_6_0.onConfirm = arg_6_1
	arg_6_0.onCancel = arg_6_2
end

function var_0_0.InitUI(arg_7_0)
	arg_7_0.titleBG = arg_7_0:findTF("panel/title")
	arg_7_0.titleBGDecoration = arg_7_0:findTF("panel/title/Image")
	arg_7_0.titleIcon = arg_7_0:findTF("panel/title/icon")
	arg_7_0.txTitle = arg_7_0:findTF("panel/title_form")
	arg_7_0.txTitleOriginPosY = arg_7_0.txTitle.anchoredPosition.y
	arg_7_0.txTitleHead = arg_7_0:findTF("panel/title_head")

	setActive(arg_7_0.txTitleHead, false)

	arg_7_0.txIntro = arg_7_0:findTF("panel/intro")
	arg_7_0.txCost = arg_7_0:findTF("panel/cost/text")
	arg_7_0.progressBar = arg_7_0:findTF("panel/progress")
	arg_7_0.txProgress = arg_7_0:findTF("panel/progress/Text/value")
	arg_7_0.progress = arg_7_0:findTF("panel/progress")
	arg_7_0.head = arg_7_0:findTF("panel/head/Image")
	arg_7_0.trAchieveTpl = arg_7_0:findTF("panel/achieve")
	arg_7_0.trAchieves = arg_7_0:findTF("panel/achieves")
	arg_7_0.passStateMask = arg_7_0:findTF("panel/passState")
	arg_7_0.passState = arg_7_0:findTF("panel/passState/Image")

	setActive(arg_7_0.passState, true)

	arg_7_0.winCondDesc = arg_7_0:findTF("panel/win_conditions/desc")
	arg_7_0.winCondAwardBtn = arg_7_0:findTF("panel/win_conditions/icon")
	arg_7_0.loseCondDesc = arg_7_0:findTF("panel/lose_conditions/desc")
	arg_7_0.achieveList = UIItemList.New(arg_7_0.trAchieves, arg_7_0.trAchieveTpl)

	arg_7_0.achieveList:make(function(arg_8_0, arg_8_1, arg_8_2)
		arg_7_0:updateAchieve(arg_8_0, arg_8_1, arg_8_2)
	end)
	setActive(arg_7_0.trAchieveTpl, false)

	arg_7_0.trDropTpl = arg_7_0:findTF("panel/drops/frame/list/item")
	arg_7_0.trDrops = arg_7_0:findTF("panel/drops/frame/list")
	arg_7_0.dropList = UIItemList.New(arg_7_0.trDrops, arg_7_0.trDropTpl)

	arg_7_0.dropList:make(function(arg_9_0, arg_9_1, arg_9_2)
		arg_7_0:updateDrop(arg_9_0, arg_9_1, arg_9_2)
	end)
	setActive(arg_7_0.trDropTpl, false)

	arg_7_0.btnConfirm = arg_7_0:findTF("panel/start_button")
	arg_7_0.btnCancel = arg_7_0:findTF("panel/btnBack")
	arg_7_0.quickPlayGroup = arg_7_0:findTF("panel/quickPlay")
	arg_7_0.descQuickPlay = arg_7_0:findTF("desc", arg_7_0.quickPlayGroup)
	arg_7_0.toggleQuickPlay = arg_7_0.quickPlayGroup:GetComponent(typeof(Toggle))
	arg_7_0.bottomExtra = arg_7_0:findTF("panel/BottomExtra")
	arg_7_0.layoutView = GetComponent(arg_7_0.bottomExtra:Find("LoopGroup/view"), typeof(LayoutElement))
	arg_7_0.rtViewContainer = arg_7_0.bottomExtra:Find("LoopGroup/view/container")

	setText(arg_7_0.bottomExtra:Find("LoopGroup/Loop/Text"), i18n("autofight_farm"))

	arg_7_0.loopToggle = arg_7_0.bottomExtra:Find("LoopGroup/Loop/Toggle")
	arg_7_0.loopOn = arg_7_0.loopToggle:Find("on")
	arg_7_0.loopOff = arg_7_0.loopToggle:Find("off")
	arg_7_0.loopHelp = arg_7_0.bottomExtra:Find("ButtonHelp")
	arg_7_0.costLimitTip = arg_7_0.bottomExtra:Find("LoopGroup/view/container/CostLimit")

	setActive(arg_7_0.costLimitTip, false)

	arg_7_0.autoFightToggle = arg_7_0.bottomExtra:Find("LoopGroup/view/container/AutoFight")

	setText(arg_7_0.autoFightToggle:Find("Text"), i18n("autofight"))

	arg_7_0.delayTween = {}
end

local var_0_1 = 525
local var_0_2 = 373

function var_0_0.set(arg_10_0, arg_10_1, arg_10_2)
	arg_10_0:cancelTween()

	arg_10_0.chapter = arg_10_1
	arg_10_0.posStart = arg_10_2 or Vector3(0, 0, 0)

	local var_10_0 = getProxy(ChapterProxy):getMapById(arg_10_1:getConfig("map"))
	local var_10_1 = arg_10_0.chapter:getConfigTable()
	local var_10_2 = string.split(var_10_1.name, "|")
	local var_10_3 = arg_10_1:getPlayType() == ChapterConst.TypeDefence

	GetSpriteFromAtlasAsync("ui/levelstageinfoview_atlas", var_10_3 and "title_print_defense" or "title_print", function(arg_11_0)
		if not IsNil(arg_10_0.titleBGDecoration) then
			arg_10_0.titleBGDecoration:GetComponent(typeof(Image)).sprite = arg_11_0
		end
	end)
	GetSpriteFromAtlasAsync("ui/levelstageinfoview_atlas", var_10_3 and "titlebar_bg_defense" or "titlebar_bg", function(arg_12_0)
		if not IsNil(arg_10_0.titleBG) then
			arg_10_0.titleBG:GetComponent(typeof(Image)).sprite = arg_12_0
		end
	end)
	setActive(arg_10_0.titleIcon, var_10_3)

	local var_10_4 = arg_10_0.progressBar.sizeDelta

	var_10_4.x = var_10_3 and var_0_2 or var_0_1
	arg_10_0.progressBar.sizeDelta = var_10_4

	setText(arg_10_0:findTF("title_index", arg_10_0.txTitle), var_10_1.chapter_name .. "  ")
	setText(arg_10_0:findTF("title", arg_10_0.txTitle), var_10_2[1])
	setText(arg_10_0:findTF("title_en", arg_10_0.txTitle), var_10_2[2] or "")
	setActive(arg_10_0.txTitleHead, var_10_2[3] and #var_10_2[3] > 0)

	local var_10_5 = var_10_2[3] and #var_10_2[3] > 0 and arg_10_0.txTitleOriginPosY or arg_10_0.txTitleOriginPosY + 8

	setAnchoredPosition(arg_10_0.txTitle, {
		y = var_10_5
	})
	setText(arg_10_0.txTitleHead, var_10_2[3] or "")
	setText(arg_10_0.winCondDesc, i18n("text_win_condition") .. "：" .. i18n(arg_10_1:getConfig("win_condition_display")))
	setText(arg_10_0.loseCondDesc, i18n("text_lose_condition") .. "：" .. i18n(arg_10_1:getConfig("lose_condition_display")))
	setActive(arg_10_0.winCondAwardBtn, arg_10_1:getPlayType() == ChapterConst.TypeDefence)

	if not arg_10_1:existAchieve() then
		setActive(arg_10_0.passState, false)
		setActive(arg_10_0.progress, false)
		setActive(arg_10_0.trAchieves, false)
	else
		setActive(arg_10_0.passState, true)
		setActive(arg_10_0.progress, true)
		setActive(arg_10_0.trAchieves, true)

		arg_10_0.passState.localPosition = Vector3(-arg_10_0.passState.rect.width, 0, 0)

		local var_10_6 = arg_10_1:hasMitigation()

		setActive(arg_10_0.passState, var_10_6)

		if var_10_6 then
			local var_10_7 = arg_10_1:getRiskLevel()

			setImageSprite(arg_10_0.passState, GetSpriteFromAtlas("passstate", var_10_7), true)
		end

		setWidgetText(arg_10_0.progress, i18n("levelScene_threat_to_rule_out", ": "))
		table.insert(arg_10_0.delayTween, LeanTween.value(go(arg_10_0.progress), 0, arg_10_0.chapter.progress, 0.5):setDelay(0.15):setOnUpdate(System.Action_float(function(arg_13_0)
			setSlider(arg_10_0.progress, 0, 100, arg_13_0)
			setText(arg_10_0.txProgress, math.floor(arg_13_0) .. "%")
		end)).uniqueId)
		arg_10_0.achieveList:align(#arg_10_0.chapter.achieves)
		arg_10_0.achieveList:each(function(arg_14_0, arg_14_1)
			local var_14_0 = arg_10_0.chapter.achieves[arg_14_0 + 1]
			local var_14_1 = ChapterConst.IsAchieved(var_14_0)

			table.insert(arg_10_0.delayTween, LeanTween.delayedCall(0.15 + (arg_14_0 + 1) * 0.15, System.Action(function()
				if not IsNil(arg_14_1) then
					local var_15_0 = findTF(arg_14_1, "desc")

					setTextColor(var_15_0, var_14_1 and Color.yellow or Color.white)
					setActive(findTF(arg_14_1, "star"), var_14_1)
					setActive(findTF(arg_14_1, "star_empty"), not var_14_1)
				end
			end)).uniqueId)
		end)
	end

	setText(arg_10_0.txIntro, var_10_1.profiles)
	setText(arg_10_0.txCost, var_10_1.oil)

	if var_10_1.icon and var_10_1.icon[1] then
		setActive(arg_10_0.head.parent, true)
		setImageSprite(arg_10_0.head, LoadSprite("qicon/" .. var_10_1.icon[1]))
	else
		setActive(arg_10_0.head.parent, false)
	end

	arg_10_0.awards = arg_10_0:getChapterAwards()

	arg_10_0.dropList:align(#arg_10_0.awards)

	local var_10_8 = arg_10_1:existLoop()

	setActive(arg_10_0.bottomExtra, var_10_8)

	if var_10_8 then
		local var_10_9 = arg_10_1:canActivateLoop()
		local var_10_10 = "chapter_loop_flag_" .. arg_10_1.id
		local var_10_11 = PlayerPrefs.GetInt(var_10_10, -1)
		local var_10_12 = (var_10_11 == 1 or var_10_11 == -1) and var_10_9
		local var_10_13 = #arg_10_1:getConfig("use_oil_limit") > 0

		setActive(arg_10_0.loopOn, var_10_12)
		setActive(arg_10_0.loopOff, not var_10_12)
		setActive(arg_10_0.costLimitTip, var_10_13)
		onNextTick(function()
			Canvas.ForceUpdateCanvases()

			arg_10_0.layoutView.preferredWidth = var_10_12 and arg_10_0.rtViewContainer.rect.width or 0
		end)
		onButton(arg_10_0, arg_10_0.loopToggle, function()
			if not var_10_9 then
				pg.TipsMgr.GetInstance():ShowTips(i18n("levelScene_activate_loop_mode_failed"))

				return
			end

			local var_17_0 = not arg_10_0.loopOn.gameObject.activeSelf

			PlayerPrefs.SetInt(var_10_10, var_17_0 and 1 or 0)
			PlayerPrefs.Save()
			setActive(arg_10_0.loopOn, var_17_0)
			setActive(arg_10_0.loopOff, not var_17_0)

			local var_17_1 = 0
			local var_17_2 = 0

			if var_17_0 then
				var_17_2 = arg_10_0.rtViewContainer.rect.width
			else
				var_17_1 = arg_10_0.rtViewContainer.rect.width
			end

			if arg_10_0.LTid then
				LeanTween.cancel(arg_10_0.LTid)

				arg_10_0.LTid = nil
			end

			arg_10_0.LTid = LeanTween.value(var_17_1, var_17_2, 0.3):setOnUpdate(System.Action_float(function(arg_18_0)
				arg_10_0.layoutView.preferredWidth = arg_18_0
			end)):setOnComplete(System.Action(function()
				arg_10_0.LTid = nil
			end)).uniqueId
		end, SFX_PANEL)
		onButton(arg_10_0, arg_10_0.loopHelp, function()
			pg.MsgboxMgr.GetInstance():ShowMsgBox({
				type = MSGBOX_TYPE_HELP,
				helps = i18n("levelScene_loop_help_tip")
			})
		end)

		local var_10_14 = AutoBotCommand.autoBotSatisfied()
		local var_10_15 = "chapter_autofight_flag_" .. arg_10_1.id
		local var_10_16 = var_10_14 and PlayerPrefs.GetInt(var_10_15, 1) == 1

		onToggle(arg_10_0, arg_10_0.autoFightToggle, function(arg_21_0)
			if arg_21_0 ~= var_10_16 then
				var_10_16 = arg_21_0

				PlayerPrefs.SetInt(var_10_15, var_10_16 and 1 or 0)
				PlayerPrefs.Save()
			end
		end, SFX_UI_TAG)
		triggerToggle(arg_10_0.autoFightToggle, var_10_16)
		setActive(arg_10_0.autoFightToggle, var_10_14)
	end

	onButton(arg_10_0, arg_10_0.btnConfirm, function()
		if arg_10_0.onConfirm then
			local var_22_0 = var_10_8 and arg_10_0.loopOn.gameObject.activeSelf and 1 or 0

			arg_10_0.onConfirm(var_22_0)
		end
	end, SFX_UI_WEIGHANCHOR_GO)
	onButton(arg_10_0, arg_10_0.btnCancel, function()
		if arg_10_0.onCancel then
			arg_10_0.onCancel()
		end
	end, SFX_CANCEL)
	onButton(arg_10_0, arg_10_0._tf:Find("bg"), function()
		if arg_10_0.onCancel then
			arg_10_0.onCancel()
		end
	end, SFX_CANCEL)

	if not arg_10_1:getConfig("risk_levels") then
		local var_10_17 = {}
	end

	onButton(arg_10_0, arg_10_0.passState, function()
		if not arg_10_1:hasMitigation() then
			return
		end

		local var_25_0 = i18n("level_risk_level_desc", arg_10_1:getChapterState()) .. i18n("level_risk_level_mitigation_rate", arg_10_1:getRemainPassCount(), arg_10_1:getMitigationRate())

		if var_10_0:getMapType() == Map.ELITE then
			var_25_0 = var_25_0 .. "\n" .. i18n("level_diffcult_chapter_state_safety")
		end

		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			hideNo = true,
			content = var_25_0
		})
	end, SFX_PANEL)
	onButton(arg_10_0, arg_10_0.head, function()
		triggerButton(arg_10_0.passState)
	end, SFX_PANEL)
	onButton(arg_10_0, arg_10_0.winCondAwardBtn, function()
		arg_10_0:ShowChapterRewardPanel()
	end)
	setText(arg_10_0.descQuickPlay, i18n("desc_quick_play"))

	local var_10_18 = arg_10_1:CanQuickPlay()

	setActive(arg_10_0.quickPlayGroup, var_10_18)

	if var_10_18 then
		local var_10_19 = "chapter_quickPlay_flag_" .. arg_10_1.id
		local var_10_20 = PlayerPrefs.GetInt(var_10_19, 1)

		onToggle(arg_10_0, arg_10_0.toggleQuickPlay, function(arg_28_0)
			PlayerPrefs.SetInt(var_10_19, arg_28_0 and 1 or 0)
			PlayerPrefs.Save()
		end, SFX_PANEL)
		triggerToggle(arg_10_0.toggleQuickPlay, var_10_20 == 1)
	end

	local var_10_21 = arg_10_0:findTF("panel")

	var_10_21.transform.localPosition = arg_10_0.posStart

	table.insert(arg_10_0.delayTween, LeanTween.move(var_10_21, Vector3.zero, 0.2).uniqueId)

	var_10_21.localScale = Vector3.zero

	table.insert(arg_10_0.delayTween, LeanTween.scale(var_10_21, Vector3(1, 1, 1), 0.2).uniqueId)
	table.insert(arg_10_0.delayTween, LeanTween.moveX(arg_10_0.passState, 0, 0.35):setEase(LeanTweenType.easeInOutSine):setDelay(0.3).uniqueId)
end

function var_0_0.cancelTween(arg_29_0)
	_.each(arg_29_0.delayTween, function(arg_30_0)
		LeanTween.cancel(arg_30_0)
	end)

	arg_29_0.delayTween = {}
end

function var_0_0.updateAchieve(arg_31_0, arg_31_1, arg_31_2, arg_31_3)
	if arg_31_1 == UIItemList.EventUpdate then
		local var_31_0 = arg_31_0.chapter.achieves[arg_31_2 + 1]
		local var_31_1 = findTF(arg_31_3, "desc")

		setText(var_31_1, ChapterConst.GetAchieveDesc(var_31_0.type, arg_31_0.chapter))
		setTextColor(var_31_1, Color.white)
		setActive(findTF(arg_31_3, "star"), false)
		setActive(findTF(arg_31_3, "star_empty"), true)
	end
end

function var_0_0.updateDrop(arg_32_0, arg_32_1, arg_32_2, arg_32_3)
	if arg_32_1 == UIItemList.EventUpdate then
		local var_32_0 = arg_32_0.awards[arg_32_2 + 1]
		local var_32_1 = Drop.Create(var_32_0)

		updateDrop(arg_32_3, var_32_1)
		onButton(arg_32_0, arg_32_3, function()
			if ({
				[99] = true
			})[var_32_1:getConfig("type")] then
				local function var_33_0(arg_34_0)
					local var_34_0 = var_32_1:getConfig("display_icon")
					local var_34_1 = {}

					for iter_34_0, iter_34_1 in ipairs(var_34_0) do
						local var_34_2 = iter_34_1[1]
						local var_34_3 = iter_34_1[2]
						local var_34_4 = var_34_2 == DROP_TYPE_SHIP and not table.contains(arg_34_0, var_34_3)

						var_34_1[#var_34_1 + 1] = {
							type = var_34_2,
							id = var_34_3,
							anonymous = var_34_4
						}
					end

					arg_32_0:emit(BaseUI.ON_DROP_LIST, {
						item2Row = true,
						itemList = var_34_1,
						content = var_32_1:getConfig("display")
					})
					arg_32_0:initTestShowDrop(var_32_1, Clone(var_34_1))
				end

				arg_32_0:emit(LevelMediator2.GET_CHAPTER_DROP_SHIP_LIST, arg_32_0.chapter.id, var_33_0)
			else
				arg_32_0:emit(BaseUI.ON_DROP, var_32_1)
			end
		end, SFX_PANEL)
	end
end

function var_0_0.getChapterAwards(arg_35_0)
	local var_35_0 = arg_35_0.chapter
	local var_35_1 = Clone(var_35_0:getConfig("awards"))
	local var_35_2 = var_35_0:getStageExtraAwards()

	if var_35_2 then
		for iter_35_0 = #var_35_2, 1, -1 do
			table.insert(var_35_1, 1, var_35_2[iter_35_0])
		end
	end

	local var_35_3 = {
		var_35_0:getConfig("boss_expedition_id"),
		var_35_0:getConfig("ai_expedition_list")
	}

	if var_35_0:getPlayType() == ChapterConst.TypeMultiStageBoss then
		table.insert(var_35_3, pg.chapter_model_multistageboss[var_35_0.id].boss_expedition_id)
	end

	local var_35_4 = _.flatten(var_35_3)
	local var_35_5 = {}
	local var_35_6 = {}

	local function var_35_7(arg_36_0)
		for iter_36_0, iter_36_1 in ipairs(var_35_5) do
			if iter_36_1 == arg_36_0 then
				return false
			end
		end

		return true
	end

	for iter_35_1, iter_35_2 in ipairs(var_35_4) do
		local var_35_8 = checkExist(pg.expedition_activity_template[iter_35_2], {
			"pt_drop_display"
		})

		if var_35_8 and type(var_35_8) == "table" then
			for iter_35_3, iter_35_4 in ipairs(var_35_8) do
				if var_35_7(iter_35_4[2]) then
					table.insert(var_35_5, iter_35_4[2])

					var_35_6[iter_35_4[2]] = {}
				end

				var_35_6[iter_35_4[2]][iter_35_4[1]] = true
			end
		end
	end

	local var_35_9 = getProxy(ActivityProxy)

	for iter_35_5 = #var_35_5, 1, -1 do
		for iter_35_6, iter_35_7 in pairs(var_35_6[var_35_5[iter_35_5]]) do
			local var_35_10 = var_35_9:getActivityById(iter_35_6)

			if var_35_10 and not var_35_10:isEnd() then
				table.insert(var_35_1, 1, {
					2,
					id2ItemId(var_35_5[iter_35_5])
				})

				break
			end
		end
	end

	return var_35_1
end

function var_0_0.initTestShowDrop(arg_37_0, arg_37_1, arg_37_2)
	if IsUnityEditor then
		local var_37_0 = pg.MsgboxMgr.GetInstance()._go
		local var_37_1 = var_37_0.transform:Find("button_test_show_drop")

		if IsNil(var_37_1) then
			var_37_1 = GameObject.New("button_test_show_drop")

			var_37_1:AddComponent(typeof(Button))
			var_37_1:AddComponent(typeof(RectTransform))
			var_37_1:AddComponent(typeof(Image))
		end

		local var_37_2 = var_37_1:GetComponent(typeof(RectTransform))

		var_37_2:SetParent(var_37_0.transform, false)

		var_37_2.anchoredPosition = Vector3(-239, 173, 0)
		var_37_2.sizeDelta = Vector2(40, 40)

		onButton(arg_37_0, var_37_2, function()
			_.each(arg_37_2, function(arg_39_0)
				arg_39_0.anonymous = false
			end)
			arg_37_0:emit(BaseUI.ON_DROP_LIST, {
				item2Row = true,
				itemList = arg_37_2,
				content = arg_37_1:getConfig("display")
			})
		end)
	end
end

function var_0_0.clearTestShowDrop(arg_40_0)
	if IsUnityEditor then
		local var_40_0 = pg.MsgboxMgr.GetInstance()._go.transform:Find("button_test_show_drop")

		if not IsNil(var_40_0) then
			Destroy(var_40_0)
		end
	end
end

function var_0_0.ShowChapterRewardPanel(arg_41_0)
	if arg_41_0.rewardPanel == nil then
		arg_41_0.rewardPanel = ChapterRewardPanel.New(arg_41_0._tf.parent, arg_41_0.event, arg_41_0.contextData)

		arg_41_0.rewardPanel:Load()
	end

	arg_41_0.rewardPanel:ActionInvoke("Enter", arg_41_0.chapter)
end

function var_0_0.ClearChapterRewardPanel(arg_42_0)
	if arg_42_0.rewardPanel ~= nil then
		arg_42_0.rewardPanel:Destroy()

		arg_42_0.rewardPanel = nil
	end
end

function var_0_0.clear(arg_43_0)
	arg_43_0:cancelTween()
	arg_43_0.dropList:each(function(arg_44_0, arg_44_1)
		clearDrop(arg_44_1)
	end)
	arg_43_0:clearTestShowDrop()
	arg_43_0:ClearChapterRewardPanel()
end

return var_0_0
