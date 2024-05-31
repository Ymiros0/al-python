local var_0_0 = class("ChatBubble")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.tf = tf(arg_1_1)
	arg_1_0.isLoadChatBg = False

	arg_1_0.init()

	arg_1_0.chatFrameTr = findTF(arg_1_0.tf, "chat_fram")

	if IsNil(arg_1_0.chatFrameTr):
		arg_1_0.chatFrameTr = arg_1_0.tf

def var_0_0.init(arg_2_0):
	arg_2_0.nameTF = findTF(arg_2_0.tf, "desc/name").GetComponent("Text")
	arg_2_0.face = findTF(arg_2_0.tf, "face/content")
	arg_2_0.circle = findTF(arg_2_0.tf, "shipicon/frame")
	arg_2_0.timeTF = findTF(arg_2_0.tf, "time").GetComponent("Text")
	arg_2_0.headTF = findTF(arg_2_0.tf, "shipicon/icon").GetComponent("Image")
	arg_2_0.stars = findTF(arg_2_0.tf, "shipicon/stars")
	arg_2_0.star = findTF(arg_2_0.stars, "star")
	arg_2_0.dutyTF = findTF(arg_2_0.tf, "desc/duty")
	arg_2_0.channel = findTF(arg_2_0.tf, "desc/channel")
	arg_2_0.chatBgWidth = 665

def var_0_0.update(arg_3_0, arg_3_1):
	if arg_3_0.data == arg_3_1:
		return

	arg_3_0.data = arg_3_1

	local var_3_0 = arg_3_1.isSelf
	local var_3_1 = arg_3_1.player

	if var_3_1.icon == 0:
		var_3_1.icon = 101171

	local var_3_2 = pg.ship_data_statistics[var_3_1.icon]
	local var_3_3 = False

	if not var_3_0:
		var_3_3 = var_3_1.propose
	else
		local var_3_4 = var_3_1.character

		if var_3_4:
			local var_3_5 = getProxy(BayProxy).getShipById(var_3_4)

			if var_3_5:
				var_3_3 = var_3_5.ShowPropose()

	arg_3_0.nameTF.text = var_3_1.name

	local var_3_6 = arg_3_1.timestamp
	local var_3_7 = getOfflineTimeStamp(var_3_6)

	arg_3_0.timeTF.text = var_3_7

	if arg_3_0.dutyTF:
		setActive(arg_3_0.dutyTF, var_3_1.duty)

		if var_3_1.duty:
			local var_3_8 = GetSpriteFromAtlas("dutyicon", var_3_1.duty)

			setImageSprite(arg_3_0.dutyTF, var_3_8, True)

	local var_3_9 = Ship.New({
		configId = var_3_2.id
	})
	local var_3_10 = arg_3_0.stars.childCount
	local var_3_11 = var_3_9.getStar()

	for iter_3_0 = var_3_10, var_3_11 - 1:
		cloneTplTo(arg_3_0.star, arg_3_0.stars)

	local var_3_12 = arg_3_0.stars.childCount

	for iter_3_1 = 0, var_3_12 - 1:
		arg_3_0.stars.GetChild(iter_3_1).gameObject.SetActive(iter_3_1 < var_3_2.star)

	if arg_3_0.channel:
		local var_3_13 = GetSpriteFromAtlas("channel", ChatConst.GetChannelSprite(arg_3_1.type) .. "_1920")

		setImageSprite(arg_3_0.channel, var_3_13, True)

	arg_3_0.headTF.color = Color.New(1, 1, 1, 0)

	LoadSpriteAsync("qicon/" .. var_3_1.getPainting(), function(arg_4_0)
		if not IsNil(arg_3_0.headTF):
			arg_3_0.headTF.color = Color.white
			arg_3_0.headTF.sprite = arg_4_0 or LoadSprite("heroicon/unknown"))

	local var_3_14 = AttireFrame.attireFrameRes(var_3_1, var_3_0, AttireConst.TYPE_ICON_FRAME, var_3_3)

	PoolMgr.GetInstance().GetPrefab("IconFrame/" .. var_3_14, var_3_14, True, function(arg_5_0)
		if IsNil(arg_3_0.tf):
			return

		if arg_3_0.circle and arg_3_0.data:
			arg_5_0.name = var_3_14
			findTF(arg_5_0.transform, "icon").GetComponent(typeof(Image)).raycastTarget = False

			setParent(arg_5_0, arg_3_0.circle, False)
		else
			PoolMgr.GetInstance().ReturnPrefab("IconFrame/" .. var_3_14, var_3_14, arg_5_0))

	if arg_3_1.emojiId:
		local var_3_15 = pg.emoji_template[arg_3_1.emojiId]

		PoolMgr.GetInstance().GetPrefab("emoji/" .. var_3_15.pic, var_3_15.pic, True, function(arg_6_0)
			if IsNil(arg_3_0.tf):
				return

			if arg_3_0.face and arg_3_0.data:
				arg_6_0.name = var_3_15.pic

				local var_6_0 = arg_6_0.GetComponent("Animator")

				if var_6_0:
					var_6_0.enabled = True

				setParent(arg_6_0, arg_3_0.face, False)

				rtf(arg_6_0).sizeDelta = Vector2.New(180, 180)
				rtf(arg_6_0).localPosition = var_3_0 and Vector3(-50, 0, 0) or Vector3(50, 0, 0)
			else
				PoolMgr.GetInstance().ReturnPrefab("emoji/" .. var_3_15.pic, var_3_15.pic, arg_6_0))
	else
		local var_3_16 = AttireFrame.attireFrameRes(var_3_1, var_3_0, AttireConst.TYPE_CHAT_FRAME, var_3_3)

		PoolMgr.GetInstance().GetPrefab("ChatFrame/" .. var_3_16, var_3_16, True, function(arg_7_0)
			if IsNil(arg_3_0.tf):
				return

			if arg_3_0.tf and arg_3_0.data:
				local var_7_0 = tf(arg_7_0).Find("Text").GetComponent("RichText")

				var_7_0.supportRichText = False

				eachChild(tf(arg_7_0).Find("Text"), function(arg_8_0)
					Destroy(arg_8_0))

				local var_7_1 = string.gmatch(arg_3_1.content, ChatConst.EmojiIconCodeMatch)
				local var_7_2 = False

				for iter_7_0 in var_7_1:
					if table.contains(pg.emoji_small_template.all, tonumber(iter_7_0)):
						var_7_2 = True

						local var_7_3 = pg.emoji_small_template[tonumber(iter_7_0)]
						local var_7_4 = LoadSprite("emoji/" .. var_7_3.pic .. "_small", None)

						var_7_0.AddSprite(iter_7_0, var_7_4)

				local var_7_5 = GetComponent(arg_7_0, "VerticalLayoutGroup")

				if var_7_2:
					onNextTick(function()
						var_7_5.padding.bottom = 30

						Canvas.ForceUpdateCanvases())
				else
					var_7_5.padding.bottom = var_7_5.padding.top

				local var_7_6 = arg_3_1.content

				if arg_3_1.needBanRichText:
					var_7_6 = SwitchSpecialChar(arg_3_1.content)

				var_7_0.text = string.gsub(var_7_6, ChatConst.EmojiIconCodeMatch, function(arg_10_0)
					if table.contains(pg.emoji_small_template.all, tonumber(arg_10_0)):
						return string.format("<icon name=%s w=1 h=1/>", arg_10_0))
				arg_3_0.isLoadChatBg = True
				arg_7_0.GetComponent(typeof(LayoutElement)).preferredWidth = arg_3_0.chatBgWidth
				arg_7_0.name = var_3_16

				setParent(arg_7_0, arg_3_0.chatFrameTr, False)
				tf(arg_7_0).SetAsFirstSibling()
				Canvas.ForceUpdateCanvases()
				arg_3_0.OnChatFrameLoaded(arg_7_0)
			else
				PoolMgr.GetInstance().ReturnPrefab("ChatFrame/" .. var_3_16, var_3_16, arg_7_0))

	setActive(arg_3_0.face.parent, arg_3_1.emojiId)

def var_0_0.dispose(arg_11_0):
	if arg_11_0.face.childCount > 0:
		local var_11_0 = arg_11_0.face.GetChild(0).gameObject

		PoolMgr.GetInstance().ReturnPrefab("emoji/" .. var_11_0.name, var_11_0.name, var_11_0)

	if arg_11_0.circle.childCount > 0:
		local var_11_1 = arg_11_0.circle.GetChild(0).gameObject

		PoolMgr.GetInstance().ReturnPrefab("IconFrame/" .. var_11_1.name, var_11_1.name, var_11_1)

	if arg_11_0.isLoadChatBg:
		local var_11_2 = arg_11_0.chatFrameTr.GetChild(0).gameObject

		PoolMgr.GetInstance().ReturnPrefab("ChatFrame/" .. var_11_2.name, var_11_2.name, var_11_2)

		arg_11_0.isLoadChatBg = False

	arg_11_0.data = None

def var_0_0.OnChatFrameLoaded(arg_12_0, arg_12_1):
	return

return var_0_0
