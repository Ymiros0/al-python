﻿local var_0_0 = class("EducateScene", import(".base.EducateBaseUI"))

function var_0_0.getUIName(arg_1_0)
	return "EducateUI"
end

function var_0_0.preload(arg_2_0, arg_2_1)
	pg.PerformMgr.GetInstance():CheckLoad(function()
		arg_2_1()
	end)
end

function var_0_0.init(arg_4_0)
	arg_4_0:initData()
	arg_4_0:findUI()
	arg_4_0:addListener()
end

function var_0_0.PlayBGM(arg_5_0)
	local var_5_0 = getProxy(EducateProxy):GetCharData():GetBgm()

	if var_5_0 then
		pg.BgmMgr.GetInstance():Push(arg_5_0.__cname, var_5_0)
	end
end

function var_0_0.initData(arg_6_0)
	return
end

function var_0_0.findUI(arg_7_0)
	arg_7_0.mainAnim = arg_7_0:findTF("anim_root"):GetComponent(typeof(Animation))
	arg_7_0.bgTF = arg_7_0:findTF("anim_root/bg")
	arg_7_0.blurPanel = arg_7_0:findTF("anim_root/blur_panel")
	arg_7_0.blurPanelAnim = arg_7_0.blurPanel:GetComponent(typeof(Animation))
	arg_7_0.topTF = arg_7_0:findTF("top", arg_7_0.blurPanel)
	arg_7_0.favorBtn = arg_7_0:findTF("favor", arg_7_0.topTF)
	arg_7_0.favorLvTF = arg_7_0:findTF("anim_root/Text", arg_7_0.favorBtn)
	arg_7_0.favorMaxTF = arg_7_0:findTF("anim_root/max", arg_7_0.favorBtn)
	arg_7_0.favorBtnAnim = arg_7_0:findTF("anim_root", arg_7_0.favorBtn):GetComponent(typeof(Animation))
	arg_7_0.favorBtnAnimEvent = arg_7_0:findTF("anim_root", arg_7_0.favorBtn):GetComponent(typeof(DftAniEvent))

	arg_7_0.favorBtnAnimEvent:SetTriggerEvent(function()
		arg_7_0:updateFavorBtn()
	end)

	arg_7_0.mainTF = arg_7_0:findTF("anim_root/main")
	arg_7_0.paintTF = arg_7_0:findTF("painting", arg_7_0.mainTF)
	arg_7_0.dialogueTF = arg_7_0:findTF("dialogue", arg_7_0.blurPanel)
	arg_7_0.dialogueContent = arg_7_0:findTF("content", arg_7_0.dialogueTF)

	setActive(arg_7_0.dialogueTF, false)

	arg_7_0.bubbleTF = arg_7_0:findTF("anim_root/blur_panel/bubble")

	setActive(arg_7_0.bubbleTF, false)

	arg_7_0.bubbleBtn = arg_7_0:findTF("bubble", arg_7_0.bubbleTF)
	arg_7_0.optionsTF = arg_7_0:findTF("options", arg_7_0.mainTF)
	arg_7_0.chatBtn = arg_7_0:findTF("options/chat", arg_7_0.optionsTF)
	arg_7_0.giftBtn = arg_7_0:findTF("options/gift", arg_7_0.optionsTF)

	setActive(arg_7_0.optionsTF, false)

	arg_7_0.bottomTF = arg_7_0:findTF("bottom", arg_7_0.blurPanel)
	arg_7_0.bookBtn = arg_7_0:findTF("left/btns/book", arg_7_0.bottomTF)

	setText(arg_7_0:findTF("unlock/Text", arg_7_0.bookBtn), i18n("child_btn_collect"))

	arg_7_0.mindBtn = arg_7_0:findTF("left/btns/mind", arg_7_0.bottomTF)

	setText(arg_7_0:findTF("unlock/Text", arg_7_0.mindBtn), i18n("child_btn_mind"))

	arg_7_0.bagBtn = arg_7_0:findTF("left/btns/bag", arg_7_0.bottomTF)

	setText(arg_7_0:findTF("unlock/Text", arg_7_0.bagBtn), i18n("child_btn_bag"))

	arg_7_0.datePanel = EducateDatePanel.New(arg_7_0:findTF("date", arg_7_0.topTF), arg_7_0.event)
	arg_7_0.favorPanel = EducateFavorPanel.New(arg_7_0:findTF("favor_panel", arg_7_0.topTF), arg_7_0.event)
	arg_7_0.resPanel = EducateResPanel.New(arg_7_0:findTF("res", arg_7_0.topTF), arg_7_0.event)
	arg_7_0.topPanel = EducateTopPanel.New(arg_7_0:findTF("top_right", arg_7_0.topTF), arg_7_0.event)
	arg_7_0.targetPanel = EducateTargetPanel.New(arg_7_0:findTF("target", arg_7_0.topTF), arg_7_0.event)
	arg_7_0.bottomPanel = EducateBottomPanel.New(arg_7_0:findTF("right", arg_7_0.bottomTF), arg_7_0.event, {
		isMainEnter = arg_7_0.contextData.isMainEnter
	})
	arg_7_0.archivePanel = EducateArchivePanel.New(arg_7_0:findTF("archive_panel", arg_7_0.mainTF), arg_7_0.event, {
		isShow = true,
		isMainEnter = arg_7_0.contextData.isMainEnter
	})
end

function var_0_0._loadSubViews(arg_9_0)
	arg_9_0.datePanel:Load()
	arg_9_0.favorPanel:Load()
	arg_9_0.resPanel:Load()
	arg_9_0.topPanel:Load()
	arg_9_0.targetPanel:Load()
	arg_9_0.bottomPanel:Load()
	arg_9_0.archivePanel:Load()
	pg.UIMgr.GetInstance():OverlayPanelPB(arg_9_0.blurPanel, {
		pbList = {
			arg_9_0:findTF("bottom/left", arg_9_0.blurPanel)
		},
		groupName = arg_9_0:getGroupNameFromData()
	})

	local var_9_0 = arg_9_0.contextData.isMainEnter and "anim_educate_educateUI_bg_in" or "anim_educate_educateUI_bg_show"

	arg_9_0.mainAnim:Play(var_9_0)

	local var_9_1 = arg_9_0.contextData.isMainEnter and "anim_educate_educateUI_in" or "anim_educate_educateUI_show"

	arg_9_0.blurPanelAnim:Play(var_9_1)
end

function var_0_0.addListener(arg_10_0)
	onButton(arg_10_0, arg_10_0.chatBtn, function()
		pg.TipsMgr.GetInstance():ShowTips("触发对话[待开发]...")
	end, SFX_PANEL)
	onButton(arg_10_0, arg_10_0.giftBtn, function()
		pg.TipsMgr.GetInstance():ShowTips("送礼(?)...")
	end, SFX_PANEL)
	onButton(arg_10_0, arg_10_0.favorBtn, function()
		arg_10_0.favorPanel:Show()
	end, SFX_PANEL)
	onButton(arg_10_0, arg_10_0.bookBtn, function()
		arg_10_0:emit(var_0_0.EDUCATE_GO_SUBLAYER, Context.New({
			mediator = EducateCollectEntranceMediator,
			viewComponent = EducateCollectEntranceLayer
		}))
	end, SFX_PANEL)
	onButton(arg_10_0, arg_10_0.mindBtn, function()
		if isActive(arg_10_0:findTF("lock", arg_10_0.mindBtn)) then
			return
		end

		arg_10_0:emit(var_0_0.EDUCATE_GO_SUBLAYER, Context.New({
			mediator = EducateMindMediator,
			viewComponent = EducateMindLayer,
			data = {
				onExit = function()
					arg_10_0:checkBubbleShow()
				end
			}
		}))
	end, SFX_PANEL)
	onButton(arg_10_0, arg_10_0.bagBtn, function()
		if isActive(arg_10_0:findTF("lock", arg_10_0.bagBtn)) then
			return
		end

		arg_10_0:emit(var_0_0.EDUCATE_GO_SUBLAYER, Context.New({
			mediator = EducateBagMediator,
			viewComponent = EducateBagLayer
		}))
	end, SFX_PANEL)
	onButton(arg_10_0, arg_10_0:findTF("fitter", arg_10_0.paintTF), function()
		arg_10_0:ShowDialogue()
	end, SFX_PANEL)
end

function var_0_0.didEnter(arg_19_0)
	if arg_19_0.contextData.onEnter then
		arg_19_0.contextData.onEnter()

		arg_19_0.contextData.onEnter = nil
	end

	arg_19_0:updatePaintingUI()
	arg_19_0:updateUnlockBtns()
	arg_19_0:updateNewTips()
	arg_19_0:updateMindTip()
	arg_19_0:updateFavorBtn()
	arg_19_0:SeriesCheck()
end

function var_0_0.SeriesCheck(arg_20_0)
	local var_20_0 = {}

	table.insert(var_20_0, function(arg_21_0)
		arg_20_0:CheckNewChar(arg_21_0)
	end)
	table.insert(var_20_0, function(arg_22_0)
		if getProxy(EducateProxy):GetPlanProxy():CheckExcute() then
			arg_20_0:emit(EducateMediator.ON_EXECTUE_PLANS)
		else
			arg_22_0()
		end
	end)
	table.insert(var_20_0, function(arg_23_0)
		arg_20_0:CheckTips(arg_23_0)
	end)
	table.insert(var_20_0, function(arg_24_0)
		if getProxy(EducateProxy):GetEventProxy():NeedGetHomeEventData() then
			arg_20_0:emit(EducateMediator.ON_GET_EVENT, arg_24_0)
		else
			arg_24_0()
		end
	end)
	arg_20_0:checkBubbleShow()
	table.insert(var_20_0, function(arg_25_0)
		if not arg_20_0.contextData.ingoreGuideCheck then
			EducateGuideSequence.CheckGuide(arg_20_0.__cname, arg_25_0)
		else
			arg_20_0.contextData.ingoreGuideCheck = nil

			arg_25_0()
		end
	end)
	seriesAsync(var_20_0, function()
		return
	end)
end

function var_0_0.OnCheckGuide(arg_27_0)
	EducateGuideSequence.CheckGuide(arg_27_0.__cname, function()
		return
	end)
end

function var_0_0.CheckTips(arg_29_0, arg_29_1)
	local var_29_0 = {}

	for iter_29_0, iter_29_1 in ipairs(EducateTipHelper.GetSystemUnlockTips()) do
		table.insert(var_29_0, function(arg_30_0)
			arg_29_0:emit(var_0_0.EDUCATE_ON_UNLOCK_TIP, {
				type = EducateUnlockTipLayer.UNLOCK_TYPE_SYSTEM,
				single = iter_29_1,
				onExit = arg_30_0
			})
		end)
	end

	seriesAsync(var_29_0, function()
		arg_29_1()
	end)
end

function var_0_0.CheckNewChar(arg_32_0, arg_32_1)
	if getProxy(EducateProxy):GetCharData():GetCallName() == "" then
		setActive(arg_32_0._tf, false)

		local var_32_0 = {}

		table.insert(var_32_0, function(arg_33_0)
			pg.PerformMgr.GetInstance():PlayGroup(EducateConst.FIRST_ENTER_PERFORM_IDS, arg_33_0)
		end)
		table.insert(var_32_0, function(arg_34_0)
			arg_32_0:emit(var_0_0.EDUCATE_GO_SUBLAYER, Context.New({
				mediator = EducateNewCharMediator,
				viewComponent = EducateNewCharLayer,
				data = {
					callback = arg_34_0
				}
			}))
		end)
		table.insert(var_32_0, function(arg_35_0)
			pg.PerformMgr.GetInstance():PlayOne(EducateConst.AFTER_SET_CALLNAME_PERFORM_ID, arg_35_0)
		end)
		seriesAsync(var_32_0, function()
			setActive(arg_32_0._tf, true)
			arg_32_0:_loadSubViews()
			arg_32_1()
		end)
	else
		arg_32_0:_loadSubViews()
		arg_32_1()
	end
end

function var_0_0.showBubble(arg_37_0, arg_37_1)
	setActive(arg_37_0.bubbleTF, true)
	onButton(arg_37_0, arg_37_0.bubbleBtn, function()
		arg_37_1()
		setActive(arg_37_0.bubbleTF, false)
	end, SFX_PANEL)
end

function var_0_0.PlayPerformWithDrops(arg_39_0, arg_39_1, arg_39_2, arg_39_3)
	local var_39_0 = EducateHelper.GetDialogueShowDrops(arg_39_2)
	local var_39_1 = EducateHelper.GetCommonShowDrops(arg_39_2)

	local function var_39_2()
		if #var_39_1 > 0 then
			arg_39_0:emit(var_0_0.EDUCATE_ON_AWARD, {
				items = var_39_1,
				removeFunc = function()
					if arg_39_3 then
						arg_39_3()
					end
				end
			})
		elseif arg_39_3 then
			arg_39_3()
		end
	end

	if #arg_39_1 > 0 then
		pg.PerformMgr.GetInstance():PlayGroup(arg_39_1, var_39_2, var_39_0)
	elseif var_39_2 then
		var_39_2()
	end
end

function var_0_0.ShowFavorUpgrade(arg_42_0, arg_42_1, arg_42_2, arg_42_3)
	arg_42_0:PlayPerformWithDrops(arg_42_2, arg_42_1, function()
		if #arg_42_1 > 0 then
			arg_42_0:emit(var_0_0.EDUCATE_ON_AWARD, {
				items = arg_42_1,
				removeFunc = function()
					arg_42_0.favorBtnAnim:Play("anim_educate_favor_levelup")

					if arg_42_3 then
						arg_42_3()
					end
				end
			})
		else
			arg_42_0.favorBtnAnim:Play("anim_educate_favor_levelup")

			if arg_42_3 then
				arg_42_3()
			end
		end
	end)
end

function var_0_0.ShowSpecialEvent(arg_45_0, arg_45_1, arg_45_2, arg_45_3)
	local var_45_0 = pg.child_event_special[arg_45_1].performance

	arg_45_0:PlayPerformWithDrops(var_45_0, arg_45_2, function()
		if #arg_45_2 > 0 then
			arg_45_0:emit(var_0_0.EDUCATE_ON_AWARD, {
				items = arg_45_2,
				removeFunc = function()
					if arg_45_3 then
						arg_45_3()
					end
				end
			})
		elseif arg_45_3 then
			arg_45_3()
		end
	end)
end

function var_0_0.checkBubbleShow(arg_48_0)
	local var_48_0 = getProxy(EducateProxy):GetEventProxy():GetHomeSpecEvents()
	local var_48_1 = getProxy(EducateProxy):GetCharData()

	if #var_48_0 > 0 then
		setActive(arg_48_0:findTF("Text", arg_48_0.bubbleBtn), true)
		setActive(arg_48_0:findTF("Image", arg_48_0.bubbleBtn), false)
		arg_48_0:showBubble(function()
			arg_48_0:emit(EducateMediator.ON_SPECIAL_EVENT_TRIGGER, {
				id = var_48_0[1].id,
				callback = function()
					arg_48_0:checkBubbleShow()
					EducateGuideSequence.CheckGuide(arg_48_0.__cname, function()
						return
					end)
				end
			})
		end)
	elseif var_48_1:CheckFavor() then
		setActive(arg_48_0:findTF("Text", arg_48_0.bubbleBtn), false)
		setActive(arg_48_0:findTF("Image", arg_48_0.bubbleBtn), true)
		arg_48_0:showBubble(function()
			arg_48_0:emit(EducateMediator.ON_UPGRADE_FAVOR, function()
				arg_48_0:checkBubbleShow()
				EducateGuideSequence.CheckGuide(arg_48_0.__cname, function()
					return
				end)
			end)
		end)
	else
		setActive(arg_48_0.bubbleTF, false)
		removeOnButton(arg_48_0.bubbleTF)
	end
end

function var_0_0.updateResPanel(arg_55_0)
	arg_55_0.resPanel:Flush()
end

function var_0_0.updateArchivePanel(arg_56_0)
	arg_56_0.archivePanel:Flush()
end

function var_0_0.showArchivePanel(arg_57_0)
	arg_57_0.archivePanel:showPanel()
end

function var_0_0.updateDatePanel(arg_58_0)
	arg_58_0.datePanel:Flush()
	arg_58_0:updateUnlockBtns()
end

function var_0_0.updateUnlockBtns(arg_59_0)
	local var_59_0 = EducateHelper.IsSystemUnlock(EducateConst.SYSTEM_MEMORY)

	setActive(arg_59_0:findTF("lock", arg_59_0.bookBtn), not var_59_0)
	setActive(arg_59_0:findTF("unlock", arg_59_0.bookBtn), var_59_0)

	local var_59_1 = EducateHelper.IsSystemUnlock(EducateConst.SYSTEM_BAG)

	setActive(arg_59_0:findTF("lock", arg_59_0.bagBtn), not var_59_1)
	setActive(arg_59_0:findTF("unlock", arg_59_0.bagBtn), var_59_1)

	local var_59_2 = EducateHelper.IsSystemUnlock(EducateConst.SYSTEM_FAVOR_AND_MIND)

	setActive(arg_59_0:findTF("lock", arg_59_0.mindBtn), not var_59_2)
	setActive(arg_59_0:findTF("unlock", arg_59_0.mindBtn), var_59_2)
	setActive(arg_59_0.favorBtn, var_59_2)
end

function var_0_0.updateMindTip(arg_60_0)
	setActive(arg_60_0:findTF("unlock/tip", arg_60_0.mindBtn), getProxy(EducateProxy):GetTaskProxy():IsShowMindTasksTip())
end

function var_0_0.updateWeekDay(arg_61_0, arg_61_1)
	arg_61_0.datePanel:UpdateWeekDay(arg_61_1)
end

function var_0_0.updateFavorBtn(arg_62_0)
	local var_62_0 = getProxy(EducateProxy):GetCharData()
	local var_62_1 = var_62_0:GetFavor()

	setText(arg_62_0.favorLvTF, var_62_1.lv)

	local var_62_2 = var_62_0:GetFavorMaxLv()

	setActive(arg_62_0.favorMaxTF, var_62_1.lv == var_62_2)
end

function var_0_0.updateTargetPanel(arg_63_0)
	arg_63_0.targetPanel:Flush()
end

function var_0_0.updateBottomPanel(arg_64_0)
	arg_64_0.bottomPanel:Flush()
end

function var_0_0.updatePaintingUI(arg_65_0)
	local var_65_0 = getProxy(EducateProxy):GetCharData()

	arg_65_0.bgName = var_65_0:GetBGName()
	arg_65_0.paintingName = var_65_0:GetPaintingName()
	arg_65_0.wordList, arg_65_0.faceList = var_65_0:GetMainDialogueInfo()

	local var_65_1 = LoadSprite("bg/" .. arg_65_0.bgName)

	setImageSprite(arg_65_0.bgTF, var_65_1, false)
	setPaintingPrefab(arg_65_0.paintTF, arg_65_0.paintingName, "yangcheng")
end

function var_0_0.ShowDialogue(arg_66_0)
	if LeanTween.isTweening(arg_66_0.dialogueTF) then
		return
	end

	local var_66_0 = math.random(#arg_66_0.wordList)
	local var_66_1 = pg.child_word[arg_66_0.wordList[var_66_0]].word

	if not arg_66_0.callName then
		arg_66_0.callName = getProxy(EducateProxy):GetCharData():GetCallName()
	end

	local var_66_2 = string.gsub(var_66_1, "$1", arg_66_0.callName)

	setText(arg_66_0.dialogueContent, var_66_2)

	local var_66_3 = GetSpriteFromAtlas("paintingface/" .. arg_66_0.paintingName, arg_66_0.faceList[var_66_0])
	local var_66_4 = arg_66_0:findTF("fitter", arg_66_0.paintTF):GetChild(0):Find("face")

	if var_66_4 and var_66_3 then
		setImageSprite(var_66_4, var_66_3)
		setActive(var_66_4, true)
	end

	arg_66_0.dialogueTF.localScale = Vector3.zero

	setActive(arg_66_0.dialogueTF, true)
	LeanTween.scale(arg_66_0.dialogueTF, Vector3.one, 0.3):setEase(LeanTweenType.easeOutBack):setOnComplete(System.Action(function()
		LeanTween.scale(arg_66_0.dialogueTF, Vector3.zero, 0.3):setEase(LeanTweenType.easeInBack):setDelay(3):setOnComplete(System.Action(function()
			setActive(arg_66_0.dialogueTF, false)

			if var_66_4 then
				setActive(var_66_4, false)
			end
		end))
	end))
end

function var_0_0.updateNewTips(arg_69_0)
	arg_69_0:updateBookNewTip()
	arg_69_0:updateMindNewTip()
end

function var_0_0.updateBookNewTip(arg_70_0)
	local var_70_0 = underscore.any(pg.child_memory.all, function(arg_71_0)
		return EducateTipHelper.IsShowNewTip(EducateTipHelper.NEW_MEMORY, arg_71_0)
	end)
	local var_70_1 = EducateTipHelper.IsShowNewTip(EducateTipHelper.NEW_POLAROID)

	setActive(arg_70_0:findTF("unlock/new", arg_70_0.bookBtn), var_70_0 or var_70_1)
end

function var_0_0.updateMindNewTip(arg_72_0)
	setActive(arg_72_0:findTF("unlock/new", arg_72_0.mindBtn), EducateTipHelper.IsShowNewTip(EducateTipHelper.NEW_MIND_TASK))
end

function var_0_0.FlushView(arg_73_0)
	arg_73_0.datePanel:Flush()
	arg_73_0.favorPanel:Flush()
	arg_73_0.resPanel:Flush()
	arg_73_0.targetPanel:Flush()
	arg_73_0.bottomPanel:Flush()
	arg_73_0.archivePanel:Flush()
	arg_73_0:updatePaintingUI()
	arg_73_0:updateUnlockBtns()
	arg_73_0:updateNewTips()
	arg_73_0:updateMindTip()
	arg_73_0:updateFavorBtn()
	arg_73_0:SeriesCheck()
end

function var_0_0.onBackPressed(arg_74_0)
	arg_74_0:emit(EducateBaseUI.ON_HOME)
end

function var_0_0.willExit(arg_75_0)
	arg_75_0.contextData.isMainEnter = nil

	arg_75_0.datePanel:Destroy()

	arg_75_0.datePanel = nil

	arg_75_0.favorPanel:Destroy()

	arg_75_0.favorPanel = nil

	arg_75_0.resPanel:Destroy()

	arg_75_0.resPanel = nil

	arg_75_0.topPanel:Destroy()

	arg_75_0.topPanel = nil

	arg_75_0.targetPanel:Destroy()

	arg_75_0.targetPanel = nil

	arg_75_0.bottomPanel:Destroy()

	arg_75_0.bottomPanel = nil

	arg_75_0.archivePanel:Destroy()

	arg_75_0.archivePanel = nil

	if LeanTween.isTweening(arg_75_0.dialogueTF) then
		LeanTween.cancel(arg_75_0.dialogueTF)
	end

	pg.UIMgr.GetInstance():UnOverlayPanel(arg_75_0.blurPanel, arg_75_0._tf)
end

return var_0_0
