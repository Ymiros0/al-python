local var_0_0 = class("NotificationLayer", import("..base.BaseUI"))

var_0_0.InitCount = 10
var_0_0.MaxCount = 100
var_0_0.FORM_COMMON = 0
var_0_0.FORM_BATTLE = 1
var_0_0.FORM_MAIN = 2
var_0_0.ChannelBits = {
	send = ChatConst.ChannelWorld,
	recv = IndexConst.Flags2Bits({
		ChatConst.ChannelAll
	})
}

def var_0_0.getUIName(arg_1_0):
	if getProxy(SettingsProxy).IsMellowStyle():
		return "NotificationUI4Mellow"
	else
		return "NotificationUI"

def var_0_0.getGroupName(arg_2_0):
	return "group_NotificationUI"

def var_0_0.setPlayer(arg_3_0, arg_3_1):
	arg_3_0.player = arg_3_1

def var_0_0.setInGuild(arg_4_0, arg_4_1):
	arg_4_0.inGuild = arg_4_1

def var_0_0.setMessages(arg_5_0, arg_5_1):
	arg_5_0.messages = arg_5_1

def var_0_0.init(arg_6_0):
	arg_6_0.close = arg_6_0.findTF("close")
	arg_6_0.frame = arg_6_0.findTF("frame")
	arg_6_0.contain = arg_6_0.frame.Find("contain")

	local var_6_0 = arg_6_0.contain.Find("ListContainer/list")

	arg_6_0.content = var_6_0.Find("content")
	arg_6_0.emptySign = var_6_0.Find("EmptySign")

	setActive(arg_6_0.emptySign, False)

	arg_6_0.prefabSelf = var_6_0.Find("popo_self").gameObject
	arg_6_0.prefabOthers = var_6_0.Find("popo_other").gameObject
	arg_6_0.prefabPublic = var_6_0.Find("popo_public").gameObject
	arg_6_0.prefabWorldBoss = var_6_0.Find("popo_worldboss").gameObject
	arg_6_0.prefabWorldBossArchives = var_6_0.Find("popo_worldboss_archives").gameObject
	arg_6_0.input = arg_6_0.frame.Find("contain/ListContainer/inputbg/input").GetComponent("InputField")

	setText(arg_6_0.frame.Find("contain/ListContainer/inputbg/input/Placeholder"), i18n("notice_input_desc"))

	arg_6_0.send = arg_6_0.frame.Find("send")
	arg_6_0.channelSend = arg_6_0.frame.Find("channel_send")
	arg_6_0.channelSendPop = arg_6_0.frame.Find("channel_pop")
	arg_6_0.scroll = var_6_0.GetComponent("ScrollRect")
	arg_6_0.topMsg = arg_6_0.contain.Find("topmsg")

	SetActive(arg_6_0.topMsg, False)

	arg_6_0.topPublic = arg_6_0.findTF("popo_public", arg_6_0.topMsg)
	arg_6_0.emoji = arg_6_0.frame.Find("contain/ListContainer/inputbg/emoji")
	arg_6_0.changeRoomPanel = arg_6_0.findTF("change_room_Panel")
	arg_6_0.roomSendBtns = arg_6_0.findTF("frame/bg/type_send", arg_6_0.changeRoomPanel)
	arg_6_0.roomRecvBtns = arg_6_0.findTF("frame/bg/type_recv", arg_6_0.changeRoomPanel)
	arg_6_0.enterRoomTip = arg_6_0.frame.Find("enter_room_tip")
	arg_6_0.enterRoomCG = arg_6_0.enterRoomTip.GetComponent(typeof(CanvasGroup))
	arg_6_0.roomBtn = arg_6_0.contain.Find("top/room")
	arg_6_0.typeBtns = arg_6_0.contain.Find("top/type")
	arg_6_0.inputTF = arg_6_0.findTF("frame/bg/InputField", arg_6_0.changeRoomPanel).GetComponent(typeof(InputField))
	arg_6_0.switchTpl = arg_6_0.findTF("switch_tpl", arg_6_0.changeRoomPanel)
	arg_6_0.switchNormalSprite = arg_6_0.findTF("switch_normal", arg_6_0.changeRoomPanel).GetComponent(typeof(Image)).sprite
	arg_6_0.switchSelectedSprite = arg_6_0.findTF("switch_selected", arg_6_0.changeRoomPanel).GetComponent(typeof(Image)).sprite

	setText(findTF(arg_6_0.changeRoomPanel, "frame/bg/label_send"), i18n("notice_label_send"))
	setText(findTF(arg_6_0.changeRoomPanel, "frame/bg/label_recv"), i18n("notice_label_recv"))
	setText(findTF(arg_6_0.changeRoomPanel, "frame/bg/label_room"), i18n("notice_label_room"))
	setText(findTF(arg_6_0.changeRoomPanel, "frame/bg/label_tip"), i18n("notice_label_tip"))
	setText(findTF(arg_6_0.changeRoomPanel, "frame/cancel/Image"), i18n("word_cancel"))
	setText(findTF(arg_6_0.changeRoomPanel, "frame/confirm/Image"), i18n("word_ok"))

	arg_6_0.resource = arg_6_0.findTF("resource")
	arg_6_0.typeTpl = arg_6_0.findTF("type_tpl", arg_6_0.resource)
	arg_6_0.normalSprite = arg_6_0.findTF("normal", arg_6_0.resource).GetComponent(typeof(Image)).sprite
	arg_6_0.selectedSprite = arg_6_0.findTF("selected", arg_6_0.resource).GetComponent(typeof(Image)).sprite
	arg_6_0.bottomChannelTpl = arg_6_0.findTF("channel_tpl", arg_6_0.resource)
	arg_6_0.bottomChannelNormalSprite = arg_6_0.findTF("channel_normal", arg_6_0.resource).GetComponent(typeof(Image)).sprite
	arg_6_0.bottomChannelSelectedSprite = arg_6_0.findTF("channel_selected", arg_6_0.resource).GetComponent(typeof(Image)).sprite

	local var_6_1 = {
		ChatConst.ChannelAll,
		ChatConst.ChannelWorld,
		ChatConst.ChannelPublic,
		ChatConst.ChannelFriend,
		ChatConst.ChannelGuild,
		ChatConst.ChannelWorldBoss
	}

	arg_6_0.textSprites = {}
	arg_6_0.textSelectedSprites = {}
	arg_6_0.bottomChannelTextSprites = {}
	arg_6_0.switchTextSprites = {}

	for iter_6_0, iter_6_1 in pairs(var_6_1):
		local var_6_2 = ChatConst.GetChannelSprite(iter_6_0)

		arg_6_0.textSprites[iter_6_0] = arg_6_0.findTF("text_" .. var_6_2, arg_6_0.resource).GetComponent(typeof(Image)).sprite
		arg_6_0.textSelectedSprites[iter_6_0] = arg_6_0.findTF("text_" .. var_6_2 .. "_selected", arg_6_0.resource).GetComponent(typeof(Image)).sprite
		arg_6_0.switchTextSprites[iter_6_0] = arg_6_0.findTF("text_" .. var_6_2 .. "_switch", arg_6_0.changeRoomPanel).GetComponent(typeof(Image)).sprite

		if table.contains(ChatConst.SendChannels, iter_6_0):
			arg_6_0.bottomChannelTextSprites[iter_6_0] = arg_6_0.findTF("channel_" .. var_6_2, arg_6_0.resource).GetComponent(typeof(Image)).sprite

	arg_6_0.prefabSelf.SetActive(False)
	arg_6_0.prefabOthers.SetActive(False)
	arg_6_0.prefabPublic.SetActive(False)

	arg_6_0.bubbleCards = {}
	arg_6_0.worldBossCards = {}
	arg_6_0.poolBubble = {
		self = {},
		public = {},
		others = {}
	}
	var_0_0.ChannelBits.recv = getProxy(SettingsProxy).GetChatFlag()

def var_0_0.adjustMsgListPanel(arg_7_0):
	arg_7_0.listContainerTF = arg_7_0.contain.Find("ListContainer")
	arg_7_0.listTF = arg_7_0.contain.Find("ListContainer/list")

	local var_7_0 = arg_7_0.listContainerTF.rect.size.y
	local var_7_1 = 69.01791

	GetComponent(arg_7_0.listTF, "LayoutElement").preferredHeight = var_7_0 - var_7_1

def var_0_0.didEnter(arg_8_0):
	arg_8_0.adjustMsgListPanel()

	arg_8_0.currentForm = arg_8_0.contextData.form
	arg_8_0.escFlag = False

	onButton(arg_8_0, arg_8_0.close, function()
		arg_8_0.PlayExitAnimation(function()
			if arg_8_0.currentForm == var_0_0.FORM_BATTLE:
				arg_8_0.emit(NotificationMediator.BATTLE_CHAT_CLOSE)

			arg_8_0.emit(BaseUI.ON_CLOSE)), SFX_CANCEL)
	onButton(arg_8_0, arg_8_0.emoji, function()
		arg_8_0.displayEmojiPanel(), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.send, function()
		local var_12_0 = arg_8_0.input.text

		if var_12_0 == "":
			pg.TipsMgr.GetInstance().ShowTips(i18n("main_notificationLayer_sendButton"))

			return

		arg_8_0.input.text = ""

		arg_8_0.emit(NotificationMediator.ON_SEND_PUBLIC, var_0_0.ChannelBits.send, var_12_0), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.roomBtn, function()
		arg_8_0.showChangeRoomPanel(), SFX_PANEL)
	onButton(arg_8_0, findTF(arg_8_0.changeRoomPanel, "frame/cancel"), function()
		arg_8_0.closeChangeRoomPanel(), SFX_CANCEL)
	onButton(arg_8_0, findTF(arg_8_0.changeRoomPanel, "frame/confirm"), function()
		arg_8_0.emit(NotificationMediator.CHANGE_ROOM, tonumber(arg_8_0.inputTF.text)), SFX_CANCEL)
	onButton(arg_8_0, arg_8_0.channelSend, function()
		setActive(arg_8_0.channelSendPop, not isActive(arg_8_0.channelSendPop))

		if isActive(arg_8_0.channelSendPop):
			arg_8_0.updateChannelSendPop(), SFX_PANEL)
	onButton(arg_8_0, arg_8_0._tf, function()
		if isActive(arg_8_0.channelSendPop):
			setActive(arg_8_0.channelSendPop, False))
	pg.DelegateInfo.Add(arg_8_0, arg_8_0.scroll.onValueChanged)
	arg_8_0.scroll.onValueChanged.AddListener(function(arg_18_0)
		if arg_8_0.index > 1 and arg_18_0.y >= 1:
			local var_18_0 = arg_8_0.content.sizeDelta.y * arg_18_0.y
			local var_18_1 = arg_8_0.scroll.velocity
			local var_18_2 = math.max(1, arg_8_0.index - var_0_0.InitCount)

			for iter_18_0 = arg_8_0.index - 1, var_18_2, -1:
				arg_8_0.append(arg_8_0.filteredMessages[iter_18_0], 0)

			Canvas.ForceUpdateCanvases()

			arg_8_0.scroll.normalizedPosition = Vector2(0, var_18_0 / arg_8_0.content.sizeDelta.y)

			arg_8_0.scroll.onValueChanged.Invoke(arg_8_0.scroll.normalizedPosition)

			arg_8_0.scroll.velocity = var_18_1
			arg_8_0.index = var_18_2)
	arg_8_0.updateRoom()
	arg_8_0.updateChatChannel()
	arg_8_0.initFilter()
	arg_8_0.updateFilter()
	arg_8_0.updateAll()

	if arg_8_0.currentForm == var_0_0.FORM_BATTLE:
		arg_8_0._tf.SetParent(arg_8_0.contextData.chatViewParent, True)

		rtf(arg_8_0.frame.transform).offsetMax = Vector2(0, -120)
	else
		arg_8_0.BlurPanel()

	LeanTween.delayedCall(go(arg_8_0._tf), 0.2, System.Action(function()
		scrollToBottom(arg_8_0.content.parent)))

	rtf(arg_8_0._tf).offsetMax = Vector2(0, 0)
	rtf(arg_8_0._tf).offsetMin = Vector2(0, 0)

def var_0_0.BlurPanel(arg_20_0):
	pg.UIMgr.GetInstance().BlurPanel(arg_20_0._tf, False, {
		groupName = arg_20_0.getGroupNameFromData(),
		weight = arg_20_0.getWeightFromData() + 1
	})

def var_0_0.UnblurPanel(arg_21_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_21_0._tf)

def var_0_0.onBackPressed(arg_22_0):
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_CANCEL)

	if isActive(arg_22_0.changeRoomPanel):
		arg_22_0.closeChangeRoomPanel()
	else
		triggerButton(arg_22_0.close)

def var_0_0.initFilter(arg_23_0):
	local var_23_0 = ChatConst.RecvChannels

	arg_23_0.recvTypes = UIItemList.New(arg_23_0.typeBtns, arg_23_0.typeTpl)

	arg_23_0.recvTypes.make(function(arg_24_0, arg_24_1, arg_24_2)
		if arg_24_0 == UIItemList.EventUpdate:
			local var_24_0 = var_23_0[arg_24_1 + 1]

			setImageSprite(arg_24_2.Find("text"), arg_23_0.textSprites[var_24_0], True)
			setImageSprite(arg_24_2.Find("text_selected"), arg_23_0.textSelectedSprites[var_24_0], True)
			onButton(arg_23_0, arg_24_2, function()
				local var_25_0 = _.filter(var_23_0, function(arg_26_0)
					return arg_26_0 != ChatConst.ChannelGuild or arg_23_0.inGuild)
				local var_25_1 = IndexConst.ToggleBits(var_0_0.ChannelBits.recv, var_25_0, ChatConst.ChannelAll, var_24_0)

				if var_0_0.ChannelBits.recv == var_25_1:
					return

				var_0_0.ChannelBits.recv = var_25_1

				arg_23_0.updateFilter()
				arg_23_0.updateAll()
				getProxy(SettingsProxy).SetChatFlag(var_0_0.ChannelBits.recv), SFX_UI_TAG))
	arg_23_0.recvTypes.align(#var_23_0)

def var_0_0.updateFilter(arg_27_0):
	local var_27_0 = ChatConst.RecvChannels

	arg_27_0.recvTypes.each(function(arg_28_0, arg_28_1)
		local var_28_0 = var_27_0[arg_28_0 + 1]

		if var_28_0 == ChatConst.ChannelGuild and not arg_27_0.inGuild:
			setButtonEnabled(arg_28_1, False)

		if bit.band(var_0_0.ChannelBits.recv, bit.lshift(1, var_28_0)) > 0:
			setImageSprite(arg_28_1, arg_27_0.selectedSprite)
			setActive(arg_28_1.Find("text_selected"), True)
		else
			setImageSprite(arg_28_1, arg_27_0.normalSprite)
			setActive(arg_28_1.Find("text_selected"), False))

	local var_27_1 = var_0_0.ChannelBits.recv
	local var_27_2 = bit.lshift(1, ChatConst.ChannelAll)

	arg_27_0.filteredMessages = _.filter(arg_27_0.messages, function(arg_29_0)
		return var_27_1 == var_27_2 or bit.band(var_27_1, bit.lshift(1, arg_29_0.type)) > 0)
	arg_27_0.filteredMessages = _.slice(arg_27_0.filteredMessages, #arg_27_0.filteredMessages - var_0_0.MaxCount + 1, var_0_0.MaxCount)

def var_0_0.updateChatChannel(arg_30_0):
	setImageSprite(arg_30_0.channelSend.Find("Text"), arg_30_0.bottomChannelTextSprites[var_0_0.ChannelBits.send], True)

def var_0_0.updateChannelSendPop(arg_31_0):
	local var_31_0 = ChatConst.SendChannels
	local var_31_1 = UIItemList.New(arg_31_0.channelSendPop.Find("type_send"), arg_31_0.bottomChannelTpl)

	local function var_31_2()
		var_31_1.each(function(arg_33_0, arg_33_1)
			local var_33_0 = var_31_0[arg_33_0 + 1]

			if var_33_0 == ChatConst.ChannelGuild and not arg_31_0.inGuild:
				setButtonEnabled(arg_33_1, False)

			local var_33_1 = var_0_0.ChannelBits.send == var_33_0

			if var_33_1:
				setImageSprite(arg_33_1.Find("bottom"), arg_31_0.bottomChannelSelectedSprite, True)
			else
				setImageSprite(arg_33_1.Find("bottom"), arg_31_0.bottomChannelNormalSprite, True)

			setActive(arg_33_1.Find("selected"), var_33_1)
			setActive(arg_33_1.Find("text"), not var_33_1))

	var_31_1.make(function(arg_34_0, arg_34_1, arg_34_2)
		if arg_34_0 == UIItemList.EventUpdate:
			local var_34_0 = var_31_0[arg_34_1 + 1]

			setImageSprite(arg_34_2.Find("text"), arg_31_0.bottomChannelTextSprites[var_34_0], True)
			setImageSprite(arg_34_2.Find("selected"), arg_31_0.bottomChannelTextSprites[var_34_0], True)
			onButton(arg_31_0, arg_34_2, function()
				setActive(arg_31_0.channelSendPop, False)

				var_0_0.ChannelBits.send = var_34_0

				var_31_2()
				arg_31_0.updateChatChannel(), SFX_UI_TAG))
	var_31_1.align(#var_31_0)
	var_31_2()

def var_0_0.updateRoom(arg_36_0):
	setText(arg_36_0.enterRoomTip.Find("text"), i18n("main_notificationLayer_enter_room", arg_36_0.player.chatRoomId == 0 and "" or arg_36_0.player.chatRoomId))
	setText(arg_36_0.findTF("Text", arg_36_0.roomBtn), arg_36_0.player.chatRoomId == 0 and i18n("common_not_enter_room") or arg_36_0.player.chatRoomId)
	arg_36_0.showEnterRommTip()

def var_0_0.showChangeRoomPanel(arg_37_0):
	arg_37_0.UnblurPanel()
	pg.UIMgr.GetInstance().BlurPanel(arg_37_0.changeRoomPanel, False, {
		weight = LayerWeightConst.SECOND_LAYER
	})

	arg_37_0.inputTF.text = tostring(arg_37_0.player.chatRoomId)
	arg_37_0.tempRoomSendBits = var_0_0.ChannelBits.send

	local var_37_0 = ChatConst.SendChannels
	local var_37_1 = UIItemList.New(arg_37_0.roomSendBtns, arg_37_0.switchTpl)

	local function var_37_2()
		var_37_1.each(function(arg_39_0, arg_39_1)
			local var_39_0 = var_37_0[arg_39_0 + 1]

			if var_39_0 == ChatConst.ChannelGuild and not arg_37_0.inGuild:
				setButtonEnabled(arg_39_1, False)

			if arg_37_0.tempRoomSendBits == var_39_0:
				setImageSprite(arg_39_1, arg_37_0.switchSelectedSprite)
			else
				setImageSprite(arg_39_1, arg_37_0.switchNormalSprite))

	var_37_1.make(function(arg_40_0, arg_40_1, arg_40_2)
		if arg_40_0 == UIItemList.EventUpdate:
			local var_40_0 = var_37_0[arg_40_1 + 1]

			setImageSprite(arg_40_2.Find("text"), arg_37_0.switchTextSprites[var_40_0], True)
			onButton(arg_37_0, arg_40_2, function()
				arg_37_0.tempRoomSendBits = var_40_0

				var_37_2(), SFX_UI_TAG))
	var_37_1.align(#var_37_0)
	var_37_2()

	arg_37_0.tempRoomRecvBits = var_0_0.ChannelBits.recv

	local var_37_3 = ChatConst.RecvChannels
	local var_37_4 = UIItemList.New(arg_37_0.roomRecvBtns, arg_37_0.switchTpl)

	local function var_37_5()
		var_37_4.each(function(arg_43_0, arg_43_1)
			local var_43_0 = var_37_3[arg_43_0 + 1]

			if var_43_0 == ChatConst.ChannelGuild and not arg_37_0.inGuild:
				setButtonEnabled(arg_43_1, False)

			if bit.band(arg_37_0.tempRoomRecvBits, bit.lshift(1, var_43_0)) > 0:
				setImageSprite(arg_43_1, arg_37_0.switchSelectedSprite)
			else
				setImageSprite(arg_43_1, arg_37_0.switchNormalSprite))

	var_37_4.make(function(arg_44_0, arg_44_1, arg_44_2)
		if arg_44_0 == UIItemList.EventUpdate:
			local var_44_0 = var_37_3[arg_44_1 + 1]

			setImageSprite(arg_44_2.Find("text"), arg_37_0.switchTextSprites[var_44_0], True)
			onButton(arg_37_0, arg_44_2, function()
				local var_45_0 = _.filter(var_37_3, function(arg_46_0)
					return arg_46_0 != ChatConst.ChannelGuild or arg_37_0.inGuild)

				arg_37_0.tempRoomRecvBits = IndexConst.ToggleBits(arg_37_0.tempRoomRecvBits, var_45_0, ChatConst.ChannelAll, var_44_0)

				var_37_5(), SFX_UI_TAG))
	var_37_4.align(#var_37_3)
	var_37_5()
	setActive(arg_37_0.changeRoomPanel, True)

def var_0_0.closeChangeRoomPanel(arg_47_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_47_0.changeRoomPanel, arg_47_0._tf)

	if arg_47_0.currentForm == var_0_0.FORM_BATTLE:
		arg_47_0._tf.SetParent(arg_47_0.contextData.chatViewParent, True)

		rtf(arg_47_0.frame.transform).offsetMax = Vector2(0, -120)
	else
		arg_47_0.BlurPanel()

	setActive(arg_47_0.changeRoomPanel, False)

def var_0_0.removeAllBubble(arg_48_0):
	for iter_48_0, iter_48_1 in ipairs(arg_48_0.bubbleCards or {}):
		setActive(iter_48_1.tf, False)

		local var_48_0 = arg_48_0.poolBubble.others

		if iter_48_1.__cname == "ChatBubblePublic":
			var_48_0 = arg_48_0.poolBubble.public
		elif iter_48_1.__cname == "ChatBubble" and iter_48_1.data.player and iter_48_1.data.player.id == arg_48_0.player.id:
			var_48_0 = arg_48_0.poolBubble.self

		iter_48_1.dispose()
		table.insert(var_48_0, iter_48_1)

	arg_48_0.bubbleCards = {}

	for iter_48_2, iter_48_3 in pairs(arg_48_0.worldBossCards):
		if not IsNil(iter_48_3.tf):
			Destroy(iter_48_3.tf)

	arg_48_0.worldBossCards = {}

def var_0_0.updateAll(arg_49_0):
	arg_49_0.removeAllBubble()

	arg_49_0.index = math.max(1, #arg_49_0.filteredMessages - var_0_0.InitCount)

	for iter_49_0 = arg_49_0.index, #arg_49_0.filteredMessages:
		arg_49_0.append(arg_49_0.filteredMessages[iter_49_0], -1)

	scrollToBottom(arg_49_0.content.parent)
	setActive(arg_49_0.emptySign, PLATFORM_CODE == PLATFORM_JP and #arg_49_0.filteredMessages <= 0)

def var_0_0.append(arg_50_0, arg_50_1, arg_50_2, arg_50_3):
	if #arg_50_0.filteredMessages >= var_0_0.MaxCount * 2:
		arg_50_0.updateFilter()
		arg_50_0.updateAll()
	else
		arg_50_3 = arg_50_3 and arg_50_0.scroll.normalizedPosition.y < 0.1

		if arg_50_1.type == ChatConst.ChannelPublic:
			if arg_50_1.id == 0:
				arg_50_0.appendTopPublic(arg_50_1)
			else
				arg_50_0.appendPublic(arg_50_1, arg_50_2)
		elif arg_50_1.IsWorldBossNotify():
			arg_50_0.appendPublic(arg_50_1, arg_50_2)
		else
			arg_50_0.appendOthers(arg_50_1, arg_50_2)

		if arg_50_3:
			scrollToBottom(arg_50_0.content.parent)

	setActive(arg_50_0.emptySign, PLATFORM_CODE == PLATFORM_JP and #arg_50_0.filteredMessages <= 0)

def var_0_0.appendOthers(arg_51_0, arg_51_1, arg_51_2):
	local var_51_0 = arg_51_1.player
	local var_51_1 = arg_51_0.poolBubble.others
	local var_51_2 = arg_51_0.prefabOthers

	if var_51_0.id == arg_51_0.player.id:
		var_51_1 = arg_51_0.poolBubble.self
		var_51_2 = arg_51_0.prefabSelf
		arg_51_1.isSelf = True
		arg_51_1.player = setmetatable(Clone(arg_51_0.player), {
			__index = arg_51_1.player.__index
		})

	local var_51_3

	if #var_51_1 > 0:
		var_51_3 = var_51_1[1]

		setActive(var_51_3.tf, True)
		table.remove(var_51_1, 1)
	else
		local var_51_4 = cloneTplTo(var_51_2, arg_51_0.content)

		var_51_3 = ChatBubble.New(var_51_4)

	var_51_3.tf.SetSiblingIndex(arg_51_2)
	table.insert(arg_51_0.bubbleCards, var_51_3)
	var_51_3.update(arg_51_1)
	removeOnButton(var_51_3.headTF)
	onButton(arg_51_0, var_51_3.headTF, function()
		local var_52_0 = arg_51_0.findTF("shipicon/icon", var_51_3.tf).position

		arg_51_0.emit(NotificationMediator.OPEN_INFO, var_51_0, var_52_0, arg_51_1.content), SFX_PANEL)

def var_0_0.appendPublic(arg_53_0, arg_53_1, arg_53_2):
	local var_53_0

	if arg_53_1.id == 4:
		local var_53_1 = WorldBossConst.__IsCurrBoss(arg_53_1.args.wordBossConfigId) and arg_53_0.prefabWorldBoss or arg_53_0.prefabWorldBossArchives
		local var_53_2 = cloneTplTo(var_53_1, arg_53_0.content)

		var_53_0 = ChatBubbleWorldBoss.New(var_53_2, arg_53_0.currentForm != var_0_0.FORM_BATTLE)

		table.insert(arg_53_0.worldBossCards, var_53_0)
	else
		local var_53_3 = arg_53_0.poolBubble.public

		if #var_53_3 > 0:
			var_53_0 = var_53_3[1]

			setActive(var_53_0.tf, True)
			table.remove(var_53_3, 1)
		else
			local var_53_4 = cloneTplTo(arg_53_0.prefabPublic, arg_53_0.content)

			var_53_0 = ChatBubblePublic.New(var_53_4)

		table.insert(arg_53_0.bubbleCards, var_53_0)

	var_53_0.tf.SetSiblingIndex(arg_53_2)
	var_53_0.update(arg_53_1)

def var_0_0.appendTopPublic(arg_54_0, arg_54_1):
	local var_54_0 = 120 - (pg.TimeMgr.GetInstance().GetServerTime() - arg_54_1.timestamp)

	if var_54_0 <= 0:
		return

	SetActive(arg_54_0.topMsg, True)
	ChatProxy.InjectPublic(findTF(arg_54_0.topPublic, "text").GetComponent("RichText"), arg_54_1)

	findTF(arg_54_0.topPublic, "channel").GetComponent(typeof(Image)).sprite = GetSpriteFromAtlas("channel", ChatConst.GetChannelSprite(arg_54_1.type) .. "_1920")

	if arg_54_0._topTimer:
		arg_54_0._topTimer.Stop()

		arg_54_0._topTimer = None

	arg_54_0._topTimer = Timer.New(function()
		SetActive(arg_54_0.topMsg, False)

		arg_54_0._topTimer = None, var_54_0, 1)

	arg_54_0._topTimer.Start()

def var_0_0.showEnterRommTip(arg_56_0):
	if arg_56_0.player.chatRoomId == 0:
		return

	if not LeanTween.isTweening(go(arg_56_0.enterRoomTip)):
		LeanTween.value(go(arg_56_0.enterRoomTip), 1, 0, 2).setOnUpdate(System.Action_float(function(arg_57_0)
			arg_56_0.enterRoomCG.alpha = arg_57_0)).setEase(LeanTweenType.easeInSine).setOnComplete(System.Action(function()
			arg_56_0.enterRoomCG.alpha = 0

			LeanTween.cancel(go(arg_56_0.enterRoomTip)))).setDelay(0.5)

def var_0_0.getPos(arg_59_0, arg_59_1):
	return

def var_0_0.displayEmojiPanel(arg_60_0):
	local var_60_0 = arg_60_0.emoji.position

	arg_60_0.emit(NotificationMediator.OPEN_EMOJI, function(arg_61_0)
		arg_60_0.emit(NotificationMediator.ON_SEND_PUBLIC, var_0_0.ChannelBits.send, string.gsub(ChatConst.EmojiCode, "code", arg_61_0)), Vector3(var_60_0.x, var_60_0.y, 0))

def var_0_0.willExit(arg_62_0):
	if arg_62_0.currentForm == var_0_0.FORM_BATTLE:
		if isActive(arg_62_0.changeRoomPanel):
			arg_62_0.closeChangeRoomPanel()
	else
		arg_62_0.UnblurPanel()

	LeanTween.cancel(arg_62_0._go)
	LeanTween.cancel(go(arg_62_0.enterRoomTip))

	if arg_62_0._topTimer:
		arg_62_0._topTimer.Stop()

		arg_62_0._topTimer = None

	for iter_62_0, iter_62_1 in ipairs(arg_62_0.bubbleCards or {}):
		iter_62_1.dispose()

	for iter_62_2, iter_62_3 in ipairs(arg_62_0.worldBossCards or {}):
		iter_62_3.dispose()

	arg_62_0.worldBossCards = None

	for iter_62_4, iter_62_5 in pairs(arg_62_0.poolBubble):
		for iter_62_6, iter_62_7 in ipairs(iter_62_5):
			iter_62_7.dispose()

	arg_62_0.removeLateUpdateListener()
	getProxy(GuildProxy).ClearNewChatMsgCnt()

def var_0_0.insertEmojiToInputText(arg_63_0, arg_63_1):
	arg_63_0.input.text = arg_63_0.input.text .. string.gsub(ChatConst.EmojiIconCode, "code", arg_63_1)

def var_0_0.addLateUpdateListener(arg_64_0):
	return

def var_0_0.removeLateUpdateListener(arg_65_0):
	return

return var_0_0
