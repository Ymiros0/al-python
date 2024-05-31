local var_0_0 = class("MailProxy", import(".NetProxy"))

var_0_0.MAIL_TOTAL = "mail total"
var_0_0.MAIL_OPENNED = "mail openned"
var_0_0.MAIL_ATTACHMENT_TAKEN = "mail attachment taken"
var_0_0.UPDATE_ATTACHMENT_COUNT = "UPDATE_ATTACHMENT_COUNT"
var_0_0.DEAL_CMD_LIST = {
	"read",
	"important",
	"unimportant",
	"delete",
	"attachment",
	"overflow",
	"move"
}
var_0_0.MailMessageBoxType = {
	ReceiveAward = 1,
	ShowTips = 2,
	OverflowConfirm = 3
}

def var_0_0.register(arg_1_0):
	arg_1_0.data = {}
	arg_1_0.total = 0
	arg_1_0.totalExist = 0
	arg_1_0.totalExistMailId = None
	arg_1_0.ids = {}
	arg_1_0.importantIds = None
	arg_1_0.rareIds = None
	arg_1_0.collectionData = {}
	arg_1_0.collectionIds = None

	arg_1_0.on(30001, function(arg_2_0)
		arg_1_0.unpdateUnreadCount(arg_2_0.unread_number)
		arg_1_0.updateTotal(arg_2_0.total_number))

def var_0_0.getMail(arg_3_0, arg_3_1):
	if arg_3_0.data[arg_3_1] != None:
		return arg_3_0.data[arg_3_1].clone()

def var_0_0.updateMail(arg_4_0, arg_4_1):
	assert(isa(arg_4_1, Mail), "should be an instance of Mail")

	arg_4_0.data[arg_4_1.id] = arg_4_1.clone()

def var_0_0.removeMail(arg_5_0, arg_5_1):
	arg_5_0.total = arg_5_0.total - 1

	if arg_5_0.totalExist > 0 and arg_5_1 <= arg_5_0.totalExistMailId:
		arg_5_0.totalExist = arg_5_0.totalExist - 1

		table.removebyvalue(arg_5_0.ids, arg_5_1)

	if arg_5_0.data[arg_5_1]:
		if arg_5_0.importantIds and arg_5_0.data[arg_5_1].importantFlag:
			table.removebyvalue(arg_5_0.importantIds, arg_5_1)

		if arg_5_0.rareIds and arg_5_0.data[arg_5_1].IsRare():
			table.removebyvalue(arg_5_0.rareIds, arg_5_1)

	arg_5_0.data[arg_5_1] = None

def var_0_0.getCollecitonMail(arg_6_0, arg_6_1):
	if arg_6_0.collectionData[arg_6_1]:
		return arg_6_0.collectionData[arg_6_1].clone()

def var_0_0.updateCollectionMail(arg_7_0, arg_7_1):
	assert(isa(arg_7_1, BaseMail), "should be an instance of BaseMail")

	arg_7_0.collectionData[arg_7_1.id] = arg_7_1.clone()

def var_0_0.removeCollectionMail(arg_8_0, arg_8_1):
	assert(arg_8_0.collectionData[arg_8_1] != None, "mail should exist")

	arg_8_0.collectionData[arg_8_1] = None

	table.removebyvalue(arg_8_0.collectionIds, arg_8_1)

def var_0_0.DealMailOperation(arg_9_0, arg_9_1, arg_9_2):
	switch(arg_9_2, {
		def read:()
			arg_9_0._existUnreadCount = arg_9_0._existUnreadCount - 1

			if arg_9_0.data[arg_9_1]:
				arg_9_0.data[arg_9_1].setReadFlag(True),
		def important:()
			if arg_9_0.data[arg_9_1]:
				arg_9_0.data[arg_9_1].setImportantFlag(True)

				if arg_9_0.importantIds:
					table.dichotomyInsert(arg_9_0.importantIds, arg_9_1),
		def unimportant:()
			if arg_9_0.data[arg_9_1]:
				arg_9_0.data[arg_9_1].setImportantFlag(False)

				if arg_9_0.importantIds:
					table.removebyvalue(arg_9_0.importantIds, arg_9_1),
		def delete:()
			arg_9_0.removeMail(arg_9_1),
		def attachment:()
			if arg_9_0.data[arg_9_1]:
				arg_9_0.data[arg_9_1].setAttachFlag(True)
				arg_9_0.data[arg_9_1].setReadFlag(True),
		def overflow:()
			return,
		def move:()
			if arg_9_0.data[arg_9_1]:
				local var_16_0 = arg_9_0.data[arg_9_1]

				arg_9_0.removeMail(arg_9_1)
				arg_9_0.updateCollectionMail(var_16_0)

				if arg_9_0.collectionIds:
					table.dichotomyInsert(arg_9_0.collectionIds, arg_9_1)
	})

def var_0_0.IsDirty(arg_17_0):
	return arg_17_0.totalExist < arg_17_0.total

def var_0_0.GetNewIndex(arg_18_0):
	local var_18_0 = math.min(arg_18_0.total - arg_18_0.totalExist, SINGLE_MAIL_REQUIRE_SIZE)

	return arg_18_0.total - var_18_0 + 1, arg_18_0.total

def var_0_0.GetNextIndex(arg_19_0):
	local var_19_0 = math.min(arg_19_0.totalExist - #arg_19_0.ids, SINGLE_MAIL_REQUIRE_SIZE)
	local var_19_1 = arg_19_0.totalExist - #arg_19_0.ids

	return var_19_1 - var_19_0 + 1, var_19_1

def var_0_0.AddNewMails(arg_20_0, arg_20_1):
	local var_20_0 = {}
	local var_20_1 = {}

	for iter_20_0, iter_20_1 in ipairs(arg_20_1):
		arg_20_0.updateMail(iter_20_1)

		if iter_20_1.importantFlag:
			table.insert(var_20_0, iter_20_1.id)

		if iter_20_1.IsRare():
			table.insert(var_20_1, iter_20_1.id)

	arg_20_0.ids = table.mergeArray(arg_20_0.ids, underscore.map(arg_20_1, function(arg_21_0)
		return arg_21_0.id))

	if #var_20_0 > 0 and arg_20_0.importantIds:
		arg_20_0.importantIds = table.mergeArray(arg_20_0.importantIds, var_20_0)

	if #var_20_1 > 0 and arg_20_0.rareIds:
		arg_20_0.rareIds = table.mergeArray(arg_20_0.rareIds, var_20_1)

	arg_20_0.totalExist = arg_20_0.total

	if arg_20_0.totalExist > 0:
		arg_20_0.totalExistMailId = arg_20_0.ids[#arg_20_0.ids]

def var_0_0.AddNextMails(arg_22_0, arg_22_1):
	for iter_22_0, iter_22_1 in ipairs(arg_22_1):
		arg_22_0.updateMail(iter_22_1)

	arg_22_0.ids = table.mergeArray(underscore.map(arg_22_1, function(arg_23_0)
		return arg_23_0.id), arg_22_0.ids)

def var_0_0.SetImportantMails(arg_24_0, arg_24_1):
	for iter_24_0, iter_24_1 in ipairs(arg_24_1):
		arg_24_0.updateMail(iter_24_1)

	arg_24_0.importantIds = underscore.map(arg_24_1, function(arg_25_0)
		return arg_25_0.id)

def var_0_0.SetRareMails(arg_26_0, arg_26_1):
	for iter_26_0, iter_26_1 in ipairs(arg_26_1):
		arg_26_0.updateMail(iter_26_1)

	arg_26_0.rareIds = underscore.map(arg_26_1, function(arg_27_0)
		return arg_27_0.id)

def var_0_0.AddCollectionMails(arg_28_0, arg_28_1):
	for iter_28_0, iter_28_1 in ipairs(arg_28_1):
		arg_28_0.updateCollectionMail(iter_28_1)

	arg_28_0.collectionIds = table.mergeArray(arg_28_0.collectionIds, underscore.map(arg_28_1, function(arg_29_0)
		return arg_29_0.id))

def var_0_0.GetMails(arg_30_0, arg_30_1):
	return underscore.map(arg_30_1, function(arg_31_0)
		return arg_30_0.data[arg_31_0])

def var_0_0.GetCollectionMails(arg_32_0, arg_32_1):
	return underscore.map(arg_32_1, function(arg_33_0)
		return arg_32_0.collectionData[arg_33_0])

def var_0_0.GetMailsAttachments(arg_34_0, arg_34_1):
	local var_34_0 = {}

	for iter_34_0, iter_34_1 in ipairs(arg_34_1):
		local var_34_1 = arg_34_0.data[iter_34_1]

		if not var_34_1.attachFlag:
			for iter_34_2, iter_34_3 in ipairs(var_34_1.attachments):
				table.insert(var_34_0, Clone(iter_34_3))

	return PlayerConst.MergeSameDrops(var_34_0)

def var_0_0.GetUnreadCount(arg_35_0):
	return arg_35_0._existUnreadCount

def var_0_0.unpdateUnreadCount(arg_36_0, arg_36_1):
	arg_36_0._existUnreadCount = arg_36_1

	arg_36_0.sendNotification(var_0_0.UPDATE_ATTACHMENT_COUNT)

def var_0_0.updateTotal(arg_37_0, arg_37_1):
	arg_37_0.total = arg_37_1

	arg_37_0.sendNotification(var_0_0.MAIL_TOTAL, arg_37_0.total)

return var_0_0
