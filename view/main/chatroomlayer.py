local var_0_0 = class("ChatRoomLayer", import("..base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "ChatRoomUI"

def var_0_0.setFriendVO(arg_2_0, arg_2_1):
	arg_2_0.friendVO = arg_2_1

def var_0_0.setFriends(arg_3_0, arg_3_1):
	arg_3_0.friendVOs = arg_3_1

def var_0_0.setPlayer(arg_4_0, arg_4_1):
	arg_4_0.playerVO = arg_4_1

def var_0_0.setCacheMsgs(arg_5_0, arg_5_1):
	arg_5_0.cacheMsgsVOs = arg_5_1

def var_0_0.init(arg_6_0):
	arg_6_0.frame = arg_6_0.findTF("frame")
	arg_6_0.friendView = arg_6_0.findTF("left_length/scrollView", arg_6_0.frame)
	arg_6_0.chatPanel = arg_6_0.findTF("notification_panel", arg_6_0.frame)
	arg_6_0.chatPanelTitle = arg_6_0.findTF("notification_panel/frame/top/name", arg_6_0.frame)
	arg_6_0.sendBtn = arg_6_0.findTF("frame/bottom/send", arg_6_0.chatPanel)
	arg_6_0.inputTF = arg_6_0.findTF("frame/bottom/input", arg_6_0.chatPanel)
	arg_6_0.chatsRect = arg_6_0.findTF("frame/list", arg_6_0.chatPanel)
	arg_6_0.chatsContainer = arg_6_0.findTF("frame/list/content", arg_6_0.chatPanel)
	arg_6_0.closeBtn = arg_6_0.findTF("frame/notification_panel/frame/top/close_btn")
	arg_6_0.otherPopTpl = arg_6_0.getTpl("frame/list/popo_other", arg_6_0.chatPanel)
	arg_6_0.selfPopTpl = arg_6_0.getTpl("frame/list/popo_self", arg_6_0.chatPanel)

	pg.UIMgr.GetInstance().BlurPanel(arg_6_0.frame, False, {
		groupName = LayerWeightConst.GROUP_CHATROOM
	})

	arg_6_0.mainPanel = pg.UIMgr.GetInstance().UIMain

def var_0_0.didEnter(arg_7_0):
	local var_7_0 = arg_7_0.findTF("frame/bottom/emoji", arg_7_0.chatPanel)

	onButton(arg_7_0, var_7_0, function()
		local var_8_0 = var_7_0.position

		arg_7_0.emit(ChatRoomMediator.OPEN_EMOJI, Vector3(var_8_0.x, var_8_0.y, 0), function(arg_9_0)
			arg_7_0.sendMessage(string.gsub(ChatConst.EmojiCode, "code", arg_9_0))), SFX_PANEL)
	onButton(arg_7_0, arg_7_0._tf, function()
		arg_7_0.emit(var_0_0.ON_CLOSE), SOUND_BACK)
	onButton(arg_7_0, arg_7_0.closeBtn, function()
		arg_7_0.emit(var_0_0.ON_CLOSE), SOUND_BACK)
	arg_7_0.initFriends()

def var_0_0.initFriends(arg_12_0):
	arg_12_0.friendItems = {}
	arg_12_0.friendRect = arg_12_0.friendView.GetComponent("LScrollRect")

	function arg_12_0.friendRect.onInitItem(arg_13_0)
		arg_12_0.initFriend(arg_13_0)

	function arg_12_0.friendRect.onUpdateItem(arg_14_0, arg_14_1)
		arg_12_0.updateFriend(arg_14_0, arg_14_1)

	arg_12_0.sortFriend()

def var_0_0.createFriendItem(arg_15_0, arg_15_1):
	local var_15_0 = {
		tf = tf(arg_15_1)
	}

	var_15_0.nameTF = var_15_0.tf.Find("name").GetComponent(typeof(Text))
	var_15_0.iconTF = var_15_0.tf.Find("shipicon/icon").GetComponent(typeof(Image))
	var_15_0.circle = var_15_0.tf.Find("shipicon/frame")
	var_15_0.toggle = var_15_0.tf.GetComponent(typeof(Toggle))
	var_15_0.tipTF = var_15_0.tf.Find("tip")
	var_15_0.dateTF = var_15_0.tf.Find("lv_bg/date").GetComponent(typeof(Text))
	var_15_0.onlineTF = var_15_0.tf.Find("lv_bg/online")
	var_15_0.levelTF = var_15_0.tf.Find("lv_bg/Text").GetComponent(typeof(Text))

	local var_15_1 = arg_15_0.friendVO

	function var_15_0.update(arg_16_0, arg_16_1, arg_16_2)
		arg_16_0.clear()
		setActive(var_15_0.tipTF, False)

		arg_16_0.friendVO = arg_16_1
		var_15_0.nameTF.text = arg_16_1.name
		var_15_0.levelTF.text = "LV." .. arg_16_1.level

		local var_16_0 = pg.ship_data_statistics[arg_16_1.icon]
		local var_16_1 = Ship.New({
			configId = arg_16_1.icon,
			skin_id = arg_16_1.skinId
		})

		assert(var_16_0, "shipCfg is None >> id ==" .. arg_16_1.icon)
		LoadSpriteAsync("qicon/" .. var_16_1.getPainting(), function(arg_17_0)
			if not arg_17_0:
				var_15_0.iconTF.sprite = GetSpriteFromAtlas("heroicon/unknown", "")
			else
				var_15_0.iconTF.sprite = arg_17_0)

		local var_16_2 = AttireFrame.attireFrameRes(arg_16_1, arg_16_1.id == getProxy(PlayerProxy).getRawData().id, AttireConst.TYPE_ICON_FRAME, arg_16_1.propose)

		PoolMgr.GetInstance().GetPrefab("IconFrame/" .. var_16_2, var_16_2, True, function(arg_18_0)
			if arg_16_0.circle:
				arg_18_0.name = var_16_2
				findTF(arg_18_0.transform, "icon").GetComponent(typeof(Image)).raycastTarget = False

				setParent(arg_18_0, arg_16_0.circle, False)
			else
				PoolMgr.GetInstance().ReturnPrefab("IconFrame/" .. var_16_2, var_16_2, arg_18_0))

		if var_15_1.id == arg_16_1.id and var_15_0.toggle.isOn == False:
			triggerToggle(var_15_0.tf, True)

		setActive(arg_16_0.onlineTF, arg_16_1.online == Friend.ONLINE)
		setActive(var_15_0.dateTF, arg_16_1.online == Friend.OFFLINE)

		var_15_0.dateTF.text = pg.TimeMgr.GetInstance().STimeDescC(arg_16_1.preOnLineTime, "%Y/%m/%d")

	function var_15_0.clear(arg_19_0)
		if arg_19_0.circle.childCount > 0:
			local var_19_0 = arg_19_0.circle.GetChild(0).gameObject

			PoolMgr.GetInstance().ReturnPrefab("IconFrame/" .. var_19_0.name, var_19_0.name, var_19_0)

	function var_15_0.dispose(arg_20_0)
		arg_20_0.clear()

	return var_15_0

def var_0_0.updateFriend(arg_21_0, arg_21_1, arg_21_2):
	local var_21_0 = arg_21_0.friendItems[arg_21_2]

	if not var_21_0:
		arg_21_0.initFriend(arg_21_2)

		var_21_0 = arg_21_0.friendItems[arg_21_2]

	local var_21_1 = arg_21_0.friendVOs[arg_21_1 + 1]

	var_21_0.update(var_21_1)

def var_0_0.initFriend(arg_22_0, arg_22_1):
	local var_22_0 = arg_22_0.createFriendItem(arg_22_1)

	onToggle(arg_22_0, var_22_0.tf, function(arg_23_0)
		if arg_23_0 and var_22_0.friendVO:
			arg_22_0.openChatPanel(var_22_0.friendVO)

			arg_22_0.contextData.friendVO = var_22_0.friendVO

			arg_22_0.setFriendVO(var_22_0.friendVO)
			arg_22_0.emit(ChatRoomMediator.CLEAR_UNREADCOUNT, var_22_0.friendVO.id))

	arg_22_0.friendItems[arg_22_1] = var_22_0

def var_0_0.updateFriendVO(arg_24_0, arg_24_1):
	for iter_24_0, iter_24_1 in ipairs(arg_24_0.friendVOs):
		if iter_24_1.id == arg_24_1.id:
			arg_24_0.friendVOs[iter_24_0] = arg_24_1

			break

	if arg_24_1.id == arg_24_0.friendVO.id:
		arg_24_0.friendVO = arg_24_1

	arg_24_0.sortFriend()

def var_0_0.sortFriend(arg_25_0):
	table.sort(arg_25_0.friendVOs, function(arg_26_0, arg_26_1)
		local var_26_0 = arg_26_0.id == arg_25_0.friendVO.id and 1 or 0
		local var_26_1 = arg_26_1.id == arg_25_0.friendVO.id and 1 or 0

		if var_26_0 == var_26_1:
			if arg_26_0.online == arg_26_1.online:
				if arg_26_0.level == arg_26_1.level:
					return arg_26_0.id < arg_26_1.id
				else
					return arg_26_0.level > arg_26_1.level
			else
				return arg_26_0.online > arg_26_1.online
		else
			return var_26_1 < var_26_0)
	arg_25_0.friendRect.SetTotalCount(#arg_25_0.friendVOs, -1)

def var_0_0.openChatPanel(arg_27_0, arg_27_1):
	arg_27_0.friendVO = arg_27_1

	removeAllChildren(arg_27_0.chatsContainer)

	local var_27_0 = arg_27_0.cacheMsgsVOs[arg_27_1.id]

	for iter_27_0, iter_27_1 in pairs(var_27_0 or {}):
		arg_27_0.appendMsg(iter_27_1)

	setText(arg_27_0.chatPanelTitle, arg_27_0.friendVO.name)
	setActive(arg_27_0.chatPanel, True)
	onButton(arg_27_0, arg_27_0.sendBtn, function()
		local var_28_0 = getInputText(arg_27_0.inputTF)

		setInputText(arg_27_0.inputTF, "")
		arg_27_0.sendMessage(var_28_0))

def var_0_0.sendMessage(arg_29_0, arg_29_1):
	if arg_29_1 == "":
		pg.TipsMgr.GetInstance().ShowTips(i18n("friend_send_msg_null_tip"))

		return

	arg_29_0.emit(ChatRoomMediator.SEND_FRIEND_MSG, arg_29_0.friendVO.id, arg_29_1)

def var_0_0.getPlayer(arg_30_0, arg_30_1):
	if arg_30_1 == arg_30_0.playerVO.id:
		return arg_30_0.playerVO

	for iter_30_0, iter_30_1 in ipairs(arg_30_0.friendVOs):
		if iter_30_1.id == arg_30_1:
			return iter_30_1

def var_0_0.appendMsg(arg_31_0, arg_31_1):
	if arg_31_1.playerId != arg_31_0.playerVO.id and arg_31_1.playerId != arg_31_0.friendVO.id:
		return

	arg_31_0.emit(ChatRoomMediator.CLEAR_UNREADCOUNT, arg_31_0.friendVO.id)

	local var_31_0 = arg_31_0.otherPopTpl
	local var_31_1 = arg_31_0.getPlayer(arg_31_1.playerId)

	if arg_31_1.playerId == arg_31_0.playerVO.id:
		var_31_0 = arg_31_0.selfPopTpl
		arg_31_1.player = setmetatable(Clone(arg_31_0.playerVO), {
			__index = var_31_1
		})
		arg_31_1.isSelf = True

	local var_31_2 = cloneTplTo(var_31_0, arg_31_0.chatsContainer)

	ChatRoomBubble.New(var_31_2).update(arg_31_1)
	scrollToBottom(arg_31_0.chatsRect)

def var_0_0.closeChatPanel(arg_32_0):
	setActive(arg_32_0.chatPanel, False)

def var_0_0.willExit(arg_33_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_33_0.frame, arg_33_0._tf)
	eachChild(arg_33_0.chatsContainer, function(arg_34_0)
		local var_34_0 = arg_33_0.findTF("face", arg_34_0)

		if var_34_0.childCount > 0:
			local var_34_1 = var_34_0.GetChild(0).gameObject

			PoolMgr.GetInstance().ReturnPrefab("emoji/" .. var_34_1.name, var_34_1.name, var_34_1))

	for iter_33_0, iter_33_1 in pairs(arg_33_0.friendItems):
		iter_33_1.dispose()

def var_0_0.insertEmojiToInputText(arg_35_0, arg_35_1):
	setInputText(arg_35_0.inputTF, getInputText(arg_35_0.inputTF) .. string.gsub(ChatConst.EmojiIconCode, "code", arg_35_1))

return var_0_0
