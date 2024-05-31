local var_0_0 = class("Instagram", import("..BaseVO"))

var_0_0.TYPE_PLAYER_COMMENT = 1
var_0_0.TYPE_NPC_COMMENT = 2

local var_0_1 = pg.activity_ins_language

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.id = arg_1_1.id
	arg_1_0.configId = arg_1_0.id

	if arg_1_0.getConfig("is_active") == 1:
		arg_1_0.InitByServer(arg_1_1)
	else
		arg_1_0.InitByConfig(arg_1_1)

	arg_1_0.good = arg_1_1.good
	arg_1_0.isLike = arg_1_1.is_good == 1
	arg_1_0.isRead = arg_1_1.is_read == 1

def var_0_0.InitByServer(arg_2_0, arg_2_1):
	arg_2_0.text = arg_2_1.text
	arg_2_0.picture = arg_2_1.picture
	arg_2_0.time = arg_2_1.time

	print(pg.TimeMgr.GetInstance().GetServerTime(), "------------", arg_2_0.time)

	arg_2_0.optionDiscuss = {}
	arg_2_0.discussList = {}
	arg_2_0.allReply = {}

	for iter_2_0, iter_2_1 in ipairs(arg_2_1.npc_reply):
		local var_2_0 = {}

		for iter_2_2, iter_2_3 in ipairs(iter_2_1.npc_reply):
			table.insert(var_2_0, iter_2_3)

		arg_2_0.allReply[iter_2_1.id] = {
			id = iter_2_1.id,
			time = iter_2_1.time,
			text = iter_2_1.text,
			npc_reply = var_2_0
		}

	for iter_2_4, iter_2_5 in ipairs(arg_2_1.player_discuss):
		if iter_2_5.text == "":
			for iter_2_6, iter_2_7 in ipairs(iter_2_5.text_list):
				table.insert(arg_2_0.optionDiscuss, 1, {
					id = iter_2_5.id,
					index = iter_2_6,
					text = iter_2_7
				})
		else
			table.insert(arg_2_0.discussList, InstagramPlayerComment.New(iter_2_5, arg_2_0, 1))

	for iter_2_8, iter_2_9 in ipairs(arg_2_1.npc_discuss):
		table.insert(arg_2_0.discussList, InstagramNpcComment.New(iter_2_9, arg_2_0, 1))

def var_0_0.InitByConfig(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_0.getConfig("message_persist")

	assert(var_0_1[var_3_0], var_3_0)

	arg_3_0.text = var_0_1[var_3_0].value
	arg_3_0.picture = arg_3_0.getConfig("picture_persist")
	arg_3_0.time = pg.TimeMgr.GetInstance().parseTimeFromConfig(arg_3_0.getConfig("time_persist"))
	arg_3_0.optionDiscuss = {}
	arg_3_0.discussList = {}
	arg_3_0.allReply = getProxy(InstagramProxy).GetAllReply()

	for iter_3_0, iter_3_1 in ipairs(arg_3_1.player_discuss):
		if iter_3_1.text == "":
			for iter_3_2, iter_3_3 in ipairs(iter_3_1.text_list):
				table.insert(arg_3_0.optionDiscuss, 1, {
					id = iter_3_1.id,
					index = iter_3_2,
					text = iter_3_3
				})
		else
			table.insert(arg_3_0.discussList, InstagramPlayerComment.New(iter_3_1, arg_3_0, 1))

	local var_3_1 = arg_3_0.getConfig("npc_discuss_persist")

	if type(var_3_1) == "table":
		for iter_3_4, iter_3_5 in ipairs(var_3_1):
			local var_3_2 = arg_3_0.allReply[iter_3_5]

			table.insert(arg_3_0.discussList, InstagramNpcComment.New(var_3_2, arg_3_0, 1))

def var_0_0.GetLasterUpdateTime(arg_4_0):
	local var_4_0 = {}

	for iter_4_0, iter_4_1 in pairs(arg_4_0.discussList):
		local var_4_1 = iter_4_1.GetLasterUpdateTime()

		table.insert(var_4_0, var_4_1)

	table.sort(var_4_0, function(arg_5_0, arg_5_1)
		return arg_5_1 < arg_5_0)

	return var_4_0[1] or 0

def var_0_0.AnyCommentUnread(arg_6_0):
	return _.any(arg_6_0.discussList, function(arg_7_0)
		return arg_7_0.AnyReplyTimeOut())

def var_0_0.GetAllReply(arg_8_0):
	return arg_8_0.allReply

def var_0_0.IsReaded(arg_9_0):
	return arg_9_0.isRead

def var_0_0.bindConfigTable(arg_10_0):
	return pg.activity_ins_template

def var_0_0.GetIcon(arg_11_0):
	return arg_11_0.getConfig("sculpture")

def var_0_0.GetName(arg_12_0):
	return arg_12_0.getConfig("name")

def var_0_0.GetSortIndex(arg_13_0):
	local var_13_0 = arg_13_0.bindConfigTable()

	if var_13_0[var_13_0.all[1]].order:
		return arg_13_0.getConfig("order")
	else
		return 0

def var_0_0.GetImage(arg_14_0):
	return arg_14_0.picture

def var_0_0.GetContent(arg_15_0):
	return HXSet.hxLan(arg_15_0.text)

def var_0_0.GetLikeCnt(arg_16_0):
	if arg_16_0.good > 999:
		return "999+"
	else
		return arg_16_0.good

def var_0_0.IsLiking(arg_17_0):
	return arg_17_0.isLike

def var_0_0.UpdateIsLike(arg_18_0):
	arg_18_0.isLike = 1

def var_0_0.GetPushTime(arg_19_0):
	return InstagramTimeStamp(arg_19_0.time)

def var_0_0.GetCanDisplayComments(arg_20_0):
	local var_20_0 = {}
	local var_20_1 = 0

	for iter_20_0, iter_20_1 in ipairs(arg_20_0.discussList):
		if not iter_20_1.ShouldWaitForShow():
			table.insert(var_20_0, iter_20_1)

			var_20_1 = var_20_1 + 1

	return var_20_0, var_20_1

def var_0_0.GetFastestRefreshTime(arg_21_0):
	local var_21_0 = {}

	for iter_21_0, iter_21_1 in ipairs(arg_21_0.discussList):
		local var_21_1 = iter_21_1.GetFasterRefreshTime()

		if var_21_1:
			table.insert(var_21_0, var_21_1)

	if #var_21_0 > 0:
		table.sort(var_21_0, function(arg_22_0, arg_22_1)
			return arg_22_0 < arg_22_1)

		return var_21_0[1]

def var_0_0.GetOptionComment(arg_23_0):
	return arg_23_0.optionDiscuss

def var_0_0.CanOpenComment(arg_24_0):
	return #arg_24_0.optionDiscuss > 0

def var_0_0.ShouldShowTip(arg_25_0):
	return not arg_25_0.IsReaded() or arg_25_0.AnyCommentUnread()

return var_0_0
