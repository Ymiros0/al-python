local var_0_0 = class("InstagramLayer", import("...base.BaseUI"))

function var_0_0.getUIName(arg_1_0)
	return "InstagramUI"
end

function var_0_0.SetProxy(arg_2_0, arg_2_1)
	arg_2_0.proxy = arg_2_1
	arg_2_0.instagramVOById = arg_2_1:GetData()
	arg_2_0.messages = arg_2_1:GetMessages()
end

function var_0_0.UpdateSelectedInstagram(arg_3_0, arg_3_1)
	if arg_3_0.contextData.instagram and arg_3_0.contextData.instagram.id == arg_3_1 then
		arg_3_0.contextData.instagram = arg_3_0.instagramVOById[arg_3_1]

		arg_3_0:UpdateCommentList()
	end
end

function var_0_0.init(arg_4_0)
	local var_4_0 = GameObject.Find("MainObject")

	arg_4_0.downloadmgr = BulletinBoardMgr.Inst
	arg_4_0.listTF = arg_4_0:findTF("list")
	arg_4_0.listAnimationPlayer = arg_4_0._tf:GetComponent(typeof(Animation))
	arg_4_0.listDftAniEvent = arg_4_0._tf:GetComponent(typeof(DftAniEvent))
	arg_4_0.mainTF = arg_4_0:findTF("main")
	arg_4_0.closeBtn = arg_4_0:findTF("close_btn")
	arg_4_0.helpBtn = arg_4_0:findTF("list/bg/help")
	arg_4_0.noMsgTF = arg_4_0:findTF("list/bg/no_msg")
	arg_4_0.list = arg_4_0:findTF("list/bg/scrollrect"):GetComponent("LScrollRect")
	arg_4_0.imageTF = arg_4_0:findTF("main/left_panel/Image"):GetComponent(typeof(RawImage))
	arg_4_0.likeBtn = arg_4_0:findTF("main/left_panel/heart")
	arg_4_0.bubbleTF = arg_4_0:findTF("main/left_panel/bubble")
	arg_4_0.planeTF = arg_4_0:findTF("main/left_panel/plane")
	arg_4_0.likeCntTxt = arg_4_0:findTF("main/left_panel/zan"):GetComponent(typeof(Text))
	arg_4_0.pushTimeTxt = arg_4_0:findTF("main/left_panel/time"):GetComponent(typeof(Text))
	arg_4_0.iconTF = arg_4_0:findTF("main/right_panel/top/head/icon")
	arg_4_0.nameTxt = arg_4_0:findTF("main/right_panel/top/name"):GetComponent(typeof(Text))
	arg_4_0.centerTF = arg_4_0:findTF("main/right_panel/center")
	arg_4_0.contentTxt = arg_4_0:findTF("main/right_panel/center/Text/Text"):GetComponent(typeof(Text))
	arg_4_0.commentList = UIItemList.New(arg_4_0:findTF("main/right_panel/center/bottom/scroll/content"), arg_4_0:findTF("main/right_panel/center/bottom/scroll/content/tpl"))
	arg_4_0.commentPanel = arg_4_0:findTF("main/right_panel/last/bg2")
	arg_4_0.optionalPanel = arg_4_0:findTF("main/right_panel/last/bg2/option")
	arg_4_0.scroll = arg_4_0:findTF("main/right_panel/center/bottom/scroll")
	arg_4_0.sprites = {}
	arg_4_0.timers = {}
	arg_4_0.toDownloadList = {}

	pg.UIMgr.GetInstance():BlurPanel(arg_4_0._tf, false, {
		weight = LayerWeightConst.SECOND_LAYER
	})
end

function var_0_0.SetImageByUrl(arg_5_0, arg_5_1, arg_5_2, arg_5_3)
	if not arg_5_1 or arg_5_1 == "" then
		setActive(arg_5_2.gameObject, false)

		if arg_5_3 then
			arg_5_3()
		end
	else
		setActive(arg_5_2.gameObject, true)

		local var_5_0 = arg_5_0.sprites[arg_5_1]

		if var_5_0 then
			arg_5_2.texture = var_5_0

			if arg_5_3 then
				arg_5_3()
			end
		else
			arg_5_2.enabled = false

			arg_5_0.downloadmgr:GetTexture("ins", "1", arg_5_1, UnityEngine.Events.UnityAction_UnityEngine_Texture(function(arg_6_0)
				if arg_5_0.exited then
					return
				end

				if not arg_5_0.sprites then
					return
				end

				arg_5_0.sprites[arg_5_1] = arg_6_0
				arg_5_2.texture = arg_6_0
				arg_5_2.enabled = true

				if arg_5_3 then
					arg_5_3()
				end
			end))
			table.insert(arg_5_0.toDownloadList, arg_5_1)
		end
	end
end

function var_0_0.didEnter(arg_7_0)
	arg_7_0.animTF:GetComponent(typeof(UIEventTrigger)).didEnter:AddListener(function()
		arg_7_0:SetUp()
	end)

	arg_7_0.cards = {}

	function arg_7_0.list.onInitItem(arg_9_0)
		local var_9_0 = InstagramCard.New(arg_9_0, arg_7_0)

		onButton(arg_7_0, var_9_0._go, function()
			arg_7_0:EnterDetail(var_9_0.instagram)
		end, SFX_PANEL)

		arg_7_0.cards[arg_9_0] = var_9_0
	end

	function arg_7_0.list.onUpdateItem(arg_11_0, arg_11_1)
		local var_11_0 = arg_7_0.cards[arg_11_1]

		if not var_11_0 then
			var_11_0 = InstagramCard.New(arg_11_1)
			arg_7_0.cards[arg_11_1] = var_11_0
		end

		local var_11_1 = arg_7_0.display[arg_11_0 + 1]
		local var_11_2 = arg_7_0.instagramVOById[var_11_1.id]

		var_11_0:Update(var_11_2)
	end

	arg_7_0:InitList()
end

function var_0_0.SetUp(arg_12_0)
	onButton(arg_12_0, arg_12_0.closeBtn, function()
		arg_12_0:OnClose()
	end, SFX_PANEL)
	onButton(arg_12_0, arg_12_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.music_juus.tip
		})
	end, SFX_PANEL)
	onButton(arg_12_0, arg_12_0._tf, function()
		arg_12_0:OnClose()
	end, SFX_PANEL)
end

function var_0_0.OnClose(arg_16_0)
	if arg_16_0.inDetail then
		arg_16_0:ExitDetail()
	else
		arg_16_0:PlayExitAnimation(function()
			arg_16_0:emit(var_0_0.ON_CLOSE)
		end)
	end
end

function var_0_0.InitList(arg_18_0)
	arg_18_0.display = _.map(arg_18_0.messages, function(arg_19_0)
		return {
			time = arg_19_0:GetLasterUpdateTime(),
			id = arg_19_0.id,
			order = arg_19_0:GetSortIndex()
		}
	end)

	table.sort(arg_18_0.display, function(arg_20_0, arg_20_1)
		if arg_20_0.order == arg_20_1.order then
			return arg_20_0.id > arg_20_1.id
		else
			return arg_20_0.order > arg_20_1.order
		end
	end)
	arg_18_0.list:SetTotalCount(#arg_18_0.display)
	setActive(arg_18_0.noMsgTF, #arg_18_0.display == 0)
end

function var_0_0.UpdateInstagram(arg_21_0, arg_21_1, arg_21_2)
	for iter_21_0, iter_21_1 in pairs(arg_21_0.cards) do
		if iter_21_1.instagram and iter_21_1.instagram.id == arg_21_1 then
			iter_21_1:Update(arg_21_0.instagramVOById[arg_21_1], arg_21_2)
		end
	end
end

function var_0_0.EnterDetail(arg_22_0, arg_22_1)
	arg_22_0.contextData.instagram = arg_22_1

	arg_22_0:InitDetailPage()

	arg_22_0.inDetail = true

	pg.SystemGuideMgr.GetInstance():Play(arg_22_0)
	arg_22_0:RefreshInstagram()
	arg_22_0.listAnimationPlayer:Play("anim_snsLoad_list_out")
	scrollTo(arg_22_0.scroll, 0, 1)
end

function var_0_0.ExitDetail(arg_23_0)
	local var_23_0 = arg_23_0.contextData.instagram

	if var_23_0 and not var_23_0:IsReaded() then
		arg_23_0:emit(InstagramMediator.ON_READED, var_23_0.id)
	end

	arg_23_0.contextData.instagram = nil
	arg_23_0.inDetail = false

	arg_23_0:CloseCommentPanel()
	arg_23_0.listAnimationPlayer:Play("anim_snsLoad_list_in")
end

function var_0_0.RefreshInstagram(arg_24_0)
	local var_24_0 = arg_24_0.contextData.instagram
	local var_24_1 = var_24_0:GetFastestRefreshTime()

	if var_24_1 and var_24_1 - pg.TimeMgr.GetInstance():GetServerTime() <= 0 then
		arg_24_0:emit(InstagramMediator.ON_REPLY_UPDATE, var_24_0.id)
	end
end

function var_0_0.InitDetailPage(arg_25_0)
	local var_25_0 = arg_25_0.contextData.instagram

	arg_25_0:SetImageByUrl(var_25_0:GetImage(), arg_25_0.imageTF)
	onButton(arg_25_0, arg_25_0.planeTF, function()
		arg_25_0:emit(InstagramMediator.ON_SHARE, var_25_0.id)
	end, SFX_PANEL)

	arg_25_0.pushTimeTxt.text = var_25_0:GetPushTime()

	setImageSprite(arg_25_0.iconTF, LoadSprite("qicon/" .. var_25_0:GetIcon()), false)

	arg_25_0.nameTxt.text = var_25_0:GetName()
	arg_25_0.contentTxt.text = var_25_0:GetContent()

	onToggle(arg_25_0, arg_25_0.commentPanel, function(arg_27_0)
		if arg_27_0 then
			arg_25_0:OpenCommentPanel()
		else
			arg_25_0:CloseCommentPanel()
		end
	end, SFX_PANEL)
	arg_25_0:UpdateLikeBtn()
	arg_25_0:UpdateCommentList()
end

function var_0_0.UpdateLikeBtn(arg_28_0)
	local var_28_0 = arg_28_0.contextData.instagram
	local var_28_1 = var_28_0:IsLiking()

	if not var_28_1 then
		onButton(arg_28_0, arg_28_0.likeBtn, function()
			arg_28_0:emit(InstagramMediator.ON_LIKE, var_28_0.id)
		end, SFX_PANEL)
	else
		removeOnButton(arg_28_0.likeBtn)
	end

	setActive(arg_28_0.likeBtn:Find("heart"), var_28_1)

	arg_28_0.likeBtn:GetComponent(typeof(Image)).enabled = not var_28_1
	arg_28_0.likeCntTxt.text = i18n("ins_word_like", var_28_0:GetLikeCnt())
end

function var_0_0.UpdateCommentList(arg_30_0)
	local var_30_0 = arg_30_0.contextData.instagram

	if not var_30_0 then
		return
	end

	local var_30_1, var_30_2 = var_30_0:GetCanDisplayComments()

	table.sort(var_30_1, function(arg_31_0, arg_31_1)
		return arg_31_0.time < arg_31_1.time
	end)
	arg_30_0.commentList:make(function(arg_32_0, arg_32_1, arg_32_2)
		if arg_32_0 == UIItemList.EventUpdate then
			local var_32_0 = var_30_1[arg_32_1 + 1]
			local var_32_1 = var_32_0:HasReply()

			setText(arg_32_2:Find("main/reply"), var_32_0:GetReplyBtnTxt())

			local var_32_2 = var_32_0:GetContent()
			local var_32_3 = SwitchSpecialChar(var_32_2)

			setText(arg_32_2:Find("main/content"), HXSet.hxLan(var_32_3))
			setText(arg_32_2:Find("main/bubble/Text"), var_32_0:GetReplyCnt())
			setText(arg_32_2:Find("main/time"), var_32_0:GetTime())

			if var_32_0:GetType() == Instagram.TYPE_PLAYER_COMMENT then
				local var_32_4, var_32_5 = var_32_0:GetIcon()

				setImageSprite(arg_32_2:Find("main/head/icon"), GetSpriteFromAtlas(var_32_4, var_32_5))
			else
				setImageSprite(arg_32_2:Find("main/head/icon"), LoadSprite("qicon/" .. var_32_0:GetIcon()), false)
			end

			if var_32_1 then
				onToggle(arg_30_0, arg_32_2:Find("main/bubble"), function(arg_33_0)
					setActive(arg_32_2:Find("replys"), arg_33_0)
				end, SFX_PANEL)
				arg_30_0:UpdateReplys(arg_32_2, var_32_0)
				triggerToggle(arg_32_2:Find("main/bubble"), true)
			else
				setActive(arg_32_2:Find("replys"), false)
				triggerToggle(arg_32_2:Find("main/bubble"), false)
			end

			arg_32_2:Find("main/bubble"):GetComponent(typeof(Toggle)).enabled = var_32_1
		end
	end)
	setActive(arg_30_0.centerTF, false)
	setActive(arg_30_0.centerTF, true)
	Canvas.ForceUpdateCanvases()
	arg_30_0.commentList:align(#var_30_1)
end

function var_0_0.UpdateReplys(arg_34_0, arg_34_1, arg_34_2)
	local var_34_0, var_34_1 = arg_34_2:GetCanDisplayReply()
	local var_34_2 = UIItemList.New(arg_34_1:Find("replys"), arg_34_1:Find("replys/sub"))

	table.sort(var_34_0, function(arg_35_0, arg_35_1)
		if arg_35_0.level == arg_35_1.level then
			if arg_35_0.time == arg_35_1.time then
				return arg_35_0.id < arg_35_1.id
			else
				return arg_35_0.time < arg_35_1.time
			end
		else
			return arg_35_0.level < arg_35_1.level
		end
	end)
	var_34_2:make(function(arg_36_0, arg_36_1, arg_36_2)
		if arg_36_0 == UIItemList.EventUpdate then
			local var_36_0 = var_34_0[arg_36_1 + 1]

			setImageSprite(arg_36_2:Find("head/icon"), LoadSprite("qicon/" .. var_36_0:GetIcon()), false)

			local var_36_1 = var_36_0:GetContent()
			local var_36_2 = SwitchSpecialChar(var_36_1)

			setText(arg_36_2:Find("content"), HXSet.hxLan(var_36_2))
		end
	end)
	var_34_2:align(#var_34_0)
end

function var_0_0.OpenCommentPanel(arg_37_0)
	local var_37_0 = arg_37_0.contextData.instagram

	if not var_37_0:CanOpenComment() then
		return
	end

	setActive(arg_37_0.optionalPanel, true)

	local var_37_1 = var_37_0:GetOptionComment()

	arg_37_0.commentPanel.sizeDelta = Vector2(642.6, (#var_37_1 + 1) * 150)

	local var_37_2 = UIItemList.New(arg_37_0.optionalPanel, arg_37_0.optionalPanel:Find("option1"))

	var_37_2:make(function(arg_38_0, arg_38_1, arg_38_2)
		if arg_38_0 == UIItemList.EventUpdate then
			local var_38_0 = arg_38_1 + 1
			local var_38_1 = var_37_1[var_38_0].text
			local var_38_2 = var_37_1[var_38_0].id
			local var_38_3 = var_37_1[var_38_0].index

			setText(arg_38_2:Find("Text"), HXSet.hxLan(var_38_1))
			onButton(arg_37_0, arg_38_2, function()
				arg_37_0:emit(InstagramMediator.ON_COMMENT, var_37_0.id, var_38_3, var_38_2)
				arg_37_0:CloseCommentPanel()
			end, SFX_PANEL)
		end
	end)
	var_37_2:align(#var_37_1)
end

function var_0_0.CloseCommentPanel(arg_40_0)
	arg_40_0.commentPanel.sizeDelta = Vector2(642.6, 150)

	setActive(arg_40_0.optionalPanel, false)
end

function var_0_0.onBackPressed(arg_41_0)
	if arg_41_0.inDetail then
		arg_41_0:ExitDetail()

		return
	end

	var_0_0.super.onBackPressed(arg_41_0)
end

function var_0_0.willExit(arg_42_0)
	for iter_42_0, iter_42_1 in ipairs(arg_42_0.toDownloadList or {}) do
		arg_42_0.downloadmgr:StopLoader(iter_42_1)
	end

	arg_42_0.toDownloadList = {}

	pg.UIMgr.GetInstance():UnblurPanel(arg_42_0._tf, pg.UIMgr.GetInstance()._normalUIMain)
	arg_42_0:ExitDetail()

	for iter_42_2, iter_42_3 in pairs(arg_42_0.sprites) do
		if not IsNil(iter_42_3) then
			Object.Destroy(iter_42_3)
		end
	end

	arg_42_0.sprites = nil

	for iter_42_4, iter_42_5 in pairs(arg_42_0.cards) do
		iter_42_5:Dispose()
	end

	arg_42_0.cards = {}
end

return var_0_0
