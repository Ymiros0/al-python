local var_0_0 = class("ChatBubbleWorldBoss")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.tf = tf(arg_1_1)
	arg_1_0.interactable = defaultValue(arg_1_2, True)
	arg_1_0.nameTF = findTF(arg_1_0.tf, "desc/name").GetComponent("Text")
	arg_1_0.face = findTF(arg_1_0.tf, "face/content")
	arg_1_0.circle = findTF(arg_1_0.tf, "shipicon/frame")
	arg_1_0.timeTF = findTF(arg_1_0.tf, "time").GetComponent("Text")
	arg_1_0.headTF = findTF(arg_1_0.tf, "shipicon/icon").GetComponent("Image")
	arg_1_0.stars = findTF(arg_1_0.tf, "shipicon/stars")
	arg_1_0.star = findTF(arg_1_0.stars, "star")
	arg_1_0.dutyTF = findTF(arg_1_0.tf, "desc/duty")
	arg_1_0.channel = findTF(arg_1_0.tf, "desc/channel")
	arg_1_0.chatframe = findTF(arg_1_0.tf, "chat_fram")
	arg_1_0.chatContent = findTF(arg_1_0.tf, "chat_fram/Text").GetComponent("Text")
	arg_1_0.chatframeSel = findTF(arg_1_0.tf, "chat_fram/sel")
	arg_1_0.chatframeUnsel = findTF(arg_1_0.tf, "chat_fram/unsel")

	setActive(arg_1_0.chatframeSel, True)
	setActive(arg_1_0.chatframeUnsel, False)

def var_0_0.update(arg_2_0, arg_2_1):
	if arg_2_0.data == arg_2_1:
		return

	arg_2_0.data = arg_2_1

	local var_2_0 = False
	local var_2_1 = arg_2_1.player

	if var_2_1.icon == 0:
		var_2_1.icon = 101171

	local var_2_2 = var_2_1.propose

	arg_2_0.nameTF.text = var_2_1.name

	local var_2_3 = arg_2_1.timestamp
	local var_2_4 = getOfflineTimeStamp(var_2_3)

	arg_2_0.timeTF.text = var_2_4

	local var_2_5 = pg.ship_data_statistics[var_2_1.icon]
	local var_2_6 = Ship.New({
		configId = var_2_5.id
	})
	local var_2_7 = arg_2_0.stars.childCount
	local var_2_8 = var_2_6.getStar()

	for iter_2_0 = var_2_7, var_2_8 - 1:
		cloneTplTo(arg_2_0.star, arg_2_0.stars)

	local var_2_9 = arg_2_0.stars.childCount

	for iter_2_1 = 0, var_2_9 - 1:
		arg_2_0.stars.GetChild(iter_2_1).gameObject.SetActive(iter_2_1 < var_2_5.star)

	if arg_2_0.channel:
		local var_2_10 = GetSpriteFromAtlas("channel", ChatConst.GetChannelSprite(arg_2_1.type) .. "_1920")

		setImageSprite(arg_2_0.channel, var_2_10, True)

	arg_2_0.headTF.color = Color.New(1, 1, 1, 0)

	LoadSpriteAsync("qicon/" .. var_2_1.getPainting(), function(arg_3_0)
		if not IsNil(arg_2_0.headTF):
			arg_2_0.headTF.color = Color.white
			arg_2_0.headTF.sprite = arg_3_0 or LoadSprite("heroicon/unknown"))

	if arg_2_0.dutyTF:
		setActive(arg_2_0.dutyTF, var_2_1.duty)

		if var_2_1.duty:
			local var_2_11 = GetSpriteFromAtlas("dutyicon", var_2_1.duty)

			setImageSprite(arg_2_0.dutyTF, var_2_11, True)

	local var_2_12 = AttireFrame.attireFrameRes(var_2_1, var_2_0, AttireConst.TYPE_ICON_FRAME, var_2_2)

	PoolMgr.GetInstance().GetPrefab("IconFrame/" .. var_2_12, var_2_12, True, function(arg_4_0)
		if IsNil(arg_2_0.tf):
			return

		if arg_2_0.circle and arg_2_0.data:
			arg_4_0.name = var_2_12
			findTF(arg_4_0.transform, "icon").GetComponent(typeof(Image)).raycastTarget = False

			setParent(arg_4_0, arg_2_0.circle, False)
		else
			PoolMgr.GetInstance().ReturnPrefab("IconFrame/" .. var_2_12, var_2_12, arg_4_0))

	local var_2_13 = arg_2_1.args.wordBossId

	onButton(None, arg_2_0.chatframe, function()
		if not arg_2_0.interactable:
			pg.TipsMgr.GetInstance().ShowTips(i18n("world_boss_inbattle"))

			return

		if arg_2_1.args.isDeath:
			arg_2_0.SetGray()
			pg.TipsMgr.GetInstance().ShowTips(i18n("world_boss_none"))

			return

		pg.WorldBossTipMgr.GetInstance().OnClick("", var_2_13, arg_2_1.args.lastTime, function()
			arg_2_0.SetGray()), SFX_PANEL)

	if arg_2_1.args.isDeath:
		arg_2_0.SetGray()

	arg_2_0.chatContent.text = i18n("world_boss_ad", arg_2_1.args.bossName, arg_2_1.args.level)

def var_0_0.SetGray(arg_7_0):
	setActive(arg_7_0.chatframeSel, False)
	setActive(arg_7_0.chatframeUnsel, True)

def var_0_0.dispose(arg_8_0):
	removeOnButton(arg_8_0.chatframe)

	if arg_8_0.circle.childCount > 0:
		local var_8_0 = arg_8_0.circle.GetChild(0).gameObject

		PoolMgr.GetInstance().ReturnPrefab("IconFrame/" .. var_8_0.name, var_8_0.name, var_8_0)

return var_0_0
