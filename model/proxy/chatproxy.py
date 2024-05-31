local var_0_0 = class("ChatProxy", import(".NetProxy"))

var_0_0.NEW_MSG = "ChatProxy public msg"

def var_0_0.InjectPublic(arg_1_0, arg_1_1, arg_1_2):
	if arg_1_1.id == 0:
		arg_1_0.text = arg_1_1.args[1] and arg_1_1.args[1].string or ""

		return

	local var_1_0 = i18n("ad_" .. arg_1_1.id)

	for iter_1_0 = 1, #arg_1_1.args:
		local var_1_1 = arg_1_1.args[iter_1_0]
		local var_1_2

		if var_1_1.type == PublicArg.TypePlayerName:
			var_1_2 = var_1_1.string
		elif var_1_1.type == PublicArg.TypeShipId:
			local var_1_3 = pg.ship_data_statistics[var_1_1.int]
			local var_1_4 = "shiptype" .. iter_1_0
			local var_1_5 = GetSpriteFromAtlas("shiptype", shipType2print(var_1_3.type))

			arg_1_0.AddSprite(var_1_4, var_1_5)

			local var_1_6 = "shipcolor" .. iter_1_0

			var_1_0 = string.gsub(var_1_0, var_1_6, ItemRarity.Rarity2HexColor(var_1_3.rarity - 1))
			var_1_2 = var_1_3.name

			if arg_1_2:
				local var_1_7 = False

				if PLATFORM_CODE == PLATFORM_JP:
					var_1_7, var_1_2 = contentWrap(var_1_2, 18, 1.65)

				if var_1_7:
					var_1_2 = var_1_2 .. "..." or var_1_2
		elif var_1_1.type == PublicArg.TypeEquipId:
			var_1_2 = pg.equip_data_statistics[var_1_1.int].name
		elif var_1_1.type == PublicArg.TypeItemId:
			var_1_2 = Item.getConfigData(var_1_1.int).name
		elif var_1_1.type == PublicArg.TypeNums:
			var_1_2 = var_1_1.int
		elif var_1_1.type == PublicArg.TypeWorldBoss:
			var_1_2 = var_1_1.string
		else
			var_1_2 = var_1_1.string

		var_1_0 = string.gsub(var_1_0, "$" .. iter_1_0, var_1_2)

	arg_1_0.text = var_1_0

def var_0_0.register(arg_2_0):
	arg_2_0.on(50101, function(arg_3_0)
		if arg_3_0.type == ChatConst.CODE_BANED:
			pg.TipsMgr.GetInstance().ShowTips(arg_3_0.content)
		elif arg_3_0.type == ChatConst.CODE_ACTOBSS_MSG_WORD:
			local var_3_0 = {
				name = arg_3_0.player.name,
				score = arg_3_0.content
			}

			arg_2_0.sendNotification(GAME.ACTIVITY_BOSS_MSG_ADDED, var_3_0)
			table.insert(arg_2_0.actBossMsg, var_3_0)

			if #arg_2_0.actBossMsg > 6:
				table.remove(arg_2_0.actBossMsg, 1)
		else
			local var_3_1, var_3_2 = wordVer(arg_3_0.content, {
				isReplace = True
			})
			local var_3_3

			string.gsub(var_3_2, ChatConst.EmojiCodeMatch, function(arg_4_0)
				var_3_3 = tonumber(arg_4_0))

			if var_3_3:
				local var_3_4 = pg.emoji_template[var_3_3]

				if var_3_4:
					var_3_2 = var_3_4.desc
				else
					var_3_3 = None

			local var_3_5 = {
				player = Player.New(arg_3_0.player),
				content = var_3_2,
				emojiId = var_3_3,
				timestamp = pg.TimeMgr.GetInstance().GetServerTime()
			}

			arg_2_0.addNewMsg(ChatMsg.New(ChatConst.ChannelWorld, var_3_5)))
	arg_2_0.on(50103, function(arg_5_0)
		local var_5_0 = {}

		for iter_5_0, iter_5_1 in ipairs(arg_5_0.arg_list):
			table.insert(var_5_0, PublicArg.New(iter_5_1))

		local var_5_1 = {
			id = arg_5_0.ad_id,
			args = var_5_0,
			timestamp = pg.TimeMgr.GetInstance().GetServerTime()
		}

		arg_2_0.addNewMsg(ChatMsg.New(ChatConst.ChannelPublic, var_5_1)))

	arg_2_0.informs = {}
	arg_2_0.actBossMsg = {}

def var_0_0.addNewMsg(arg_6_0, arg_6_1):
	if arg_6_1.id == 0:
		arg_6_0.top = arg_6_1

		_.each(arg_6_1.args, function(arg_7_0)
			if arg_7_0.string:
				pg.TipsMgr.GetInstance().ShowTips(arg_7_0.string))
	else
		table.insert(arg_6_0.data, arg_6_1)

		if #arg_6_0.data > 100:
			table.remove(arg_6_0.data, 1)

	arg_6_0.sendNotification(var_0_0.NEW_MSG, arg_6_1)

def var_0_0.UpdateMsg(arg_8_0, arg_8_1):
	for iter_8_0, iter_8_1 in ipairs(arg_8_0.data):
		if iter_8_1.IsSame(arg_8_1.uniqueId):
			arg_8_0.data[iter_8_0] = arg_8_1

def var_0_0.GetMessagesByUniqueId(arg_9_0, arg_9_1):
	return _.select(arg_9_0.data, function(arg_10_0)
		return arg_10_0.uniqueId == arg_9_1)

def var_0_0.clearMsg(arg_11_0):
	arg_11_0.data = {}

def var_0_0.loadUsedEmoji(arg_12_0):
	arg_12_0.usedEmoji = {}

	local var_12_0 = getProxy(PlayerProxy).getRawData().id
	local var_12_1 = string.split(PlayerPrefs.GetString(ChatConst.EMOJI_SAVE_TAG .. var_12_0) or "", ".")

	if #var_12_1 > 0:
		_.each(var_12_1, function(arg_13_0)
			local var_13_0 = string.split(arg_13_0, "|")

			if #var_13_0 == 2:
				arg_12_0.usedEmoji[tonumber(var_13_0[1])] = tonumber(var_13_0[2]))

def var_0_0.saveUsedEmoji(arg_14_0):
	local var_14_0 = {}

	for iter_14_0, iter_14_1 in pairs(arg_14_0.usedEmoji):
		table.insert(var_14_0, iter_14_0 .. "|" .. iter_14_1)

	local var_14_1 = getProxy(PlayerProxy).getRawData().id

	PlayerPrefs.SetString(ChatConst.EMOJI_SAVE_TAG .. var_14_1, table.concat(var_14_0, "."))

def var_0_0.getUsedEmoji(arg_15_0):
	if not arg_15_0.usedEmoji:
		arg_15_0.loadUsedEmoji()

	return arg_15_0.usedEmoji

def var_0_0.addUsedEmoji(arg_16_0, arg_16_1):
	local var_16_0 = arg_16_0.getUsedEmoji()

	var_16_0[arg_16_1] = (var_16_0[arg_16_1] or 0) + 1

	arg_16_0.saveUsedEmoji()

def var_0_0.loadUsedEmojiIcon(arg_17_0):
	arg_17_0.usedEmojiIcon = {}

	for iter_17_0 = 1, 6:
		arg_17_0.usedEmojiIcon[iter_17_0] = pg.emoji_small_template.all[iter_17_0]

	local var_17_0 = getProxy(PlayerProxy).getRawData().id
	local var_17_1 = string.split(PlayerPrefs.GetString(ChatConst.EMOJI_ICON_SAVE_TAG .. var_17_0) or "", ".")

	if #var_17_1 > 0:
		for iter_17_1, iter_17_2 in ipairs(var_17_1):
			arg_17_0.usedEmojiIcon[iter_17_1] = tonumber(iter_17_2)

def var_0_0.saveUsedEmojiIcon(arg_18_0):
	local var_18_0 = {}

	for iter_18_0, iter_18_1 in ipairs(arg_18_0.usedEmojiIcon):
		table.insert(var_18_0, iter_18_1)

	local var_18_1 = getProxy(PlayerProxy).getRawData().id

	PlayerPrefs.SetString(ChatConst.EMOJI_ICON_SAVE_TAG .. var_18_1, table.concat(var_18_0, "."))

def var_0_0.getUsedEmojiIcon(arg_19_0):
	if not arg_19_0.usedEmojiIcon:
		arg_19_0.loadUsedEmojiIcon()

	return arg_19_0.usedEmojiIcon

def var_0_0.addUsedEmojiIcon(arg_20_0, arg_20_1):
	local var_20_0 = arg_20_0.getUsedEmojiIcon()
	local var_20_1 = table.indexof(var_20_0, arg_20_1, 1)

	if var_20_1:
		table.remove(var_20_0, var_20_1)
	else
		table.remove(var_20_0, #var_20_0)

	table.insert(var_20_0, 1, arg_20_1)
	arg_20_0.saveUsedEmojiIcon()

def var_0_0.GetAllTypeChatMessages(arg_21_0, arg_21_1):
	local var_21_0 = {}
	local var_21_1 = getProxy(ChatProxy)

	if not var_21_1:
		return

	_.each(var_21_1.getRawData(), function(arg_22_0)
		table.insert(var_21_0, arg_22_0))

	local var_21_2 = getProxy(GuildProxy)

	if var_21_2.getRawData():
		_.each(var_21_2.getChatMsgs(), function(arg_23_0)
			table.insert(var_21_0, arg_23_0))

	local var_21_3 = getProxy(FriendProxy)

	_.each(var_21_3.getCacheMsgList(), function(arg_24_0)
		table.insert(var_21_0, arg_24_0))

	var_21_0 = _(var_21_0).chain().filter(function(arg_25_0)
		return not var_21_3.isInBlackList(arg_25_0.playerId)).sort(function(arg_26_0, arg_26_1)
		return arg_26_0.timestamp < arg_26_1.timestamp).value()

	local var_21_4 = NotificationLayer.ChannelBits.recv
	local var_21_5 = bit.lshift(1, ChatConst.ChannelAll)

	var_21_0 = _.filter(var_21_0, function(arg_27_0)
		return var_21_4 == var_21_5 or bit.band(var_21_4, bit.lshift(1, arg_27_0.type)) > 0)
	var_21_0 = _.slice(var_21_0, #var_21_0 - arg_21_1 + 1, arg_21_1)

	return var_21_0

return var_0_0
