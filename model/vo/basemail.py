local var_0_0 = class("BaseMail", import(".BaseVO"))

var_0_0.ATTACHMENT_UNTAKEN = 1
var_0_0.ATTACHMENT_TAKEN = 2

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.id = arg_1_1.id
	arg_1_0.date = arg_1_1.date
	arg_1_0.title, arg_1_0.sender = unpack(string.split(HXSet.hxLan(arg_1_1.title), "||"))
	arg_1_0.sender = arg_1_0.sender or i18n("mail_sender_default")
	arg_1_0.content = string.gsub(HXSet.hxLan(arg_1_1.content), "\\n", "\n")
	arg_1_0.attachments = {}

	for iter_1_0, iter_1_1 in ipairs(arg_1_1.attachment_list):
		table.insert(arg_1_0.attachments, Drop.New({
			type = iter_1_1.type,
			id = iter_1_1.id,
			count = iter_1_1.number
		}))

local var_0_1

def var_0_0.IsRare(arg_2_0):
	if not var_0_1:
		var_0_1 = {}

		for iter_2_0, iter_2_1 in ipairs({
			PlayerConst.ResGold,
			PlayerConst.ResOil,
			PlayerConst.ResExploit
		}):
			table.insert(var_0_1, Drop.New({
				type = DROP_TYPE_RESOURCE,
				id = iter_2_1
			}))

		table.insert(var_0_1, Drop.New({
			type = DROP_TYPE_ITEM,
			id = ITEM_ID_CUBE
		}))

	return #arg_2_0.attachments > 0 and underscore.any(arg_2_0.attachments, function(arg_3_0)
		for iter_3_0, iter_3_1 in ipairs(var_0_1):
			if arg_3_0.type == iter_3_1.type and arg_3_0.id == iter_3_1.id:
				return False

		return True)

def var_0_0.IsMatchKey(arg_4_0, arg_4_1):
	if not arg_4_1 or arg_4_1 == "":
		return True

	arg_4_1 = string.lower(string.gsub(arg_4_1, "%.", "%%."))
	arg_4_1 = string.lower(string.gsub(arg_4_1, "%-", "%%-"))

	return underscore.any({
		arg_4_0.title,
		arg_4_0.sender,
		arg_4_0.content
	}, function(arg_5_0)
		return string.find(string.lower(arg_5_0), arg_4_1))

return var_0_0
