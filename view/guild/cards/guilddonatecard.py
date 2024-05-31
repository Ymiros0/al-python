local var_0_0 = class("GuildDonateCard")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0._tf = arg_1_1
	arg_1_0.title = arg_1_0._tf.Find("name").GetComponent(typeof(Text))
	arg_1_0.awardTF = arg_1_0._tf.Find("item")
	arg_1_0.awardTxtTF = arg_1_0._tf.Find("item/Text")
	arg_1_0.res = arg_1_0._tf.Find("award/Text").GetComponent(typeof(Text))
	arg_1_0.commitBtn = arg_1_0._tf.Find("submit")

def var_0_0.update(arg_2_0, arg_2_1):
	arg_2_0.dtask = arg_2_1

	local var_2_0 = arg_2_1.getCommitItem()

	updateDrop(arg_2_0.awardTF, {
		type = var_2_0[1],
		id = var_2_0[2],
		count = var_2_0[3]
	})

	arg_2_0.title.text = arg_2_1.getConfig("name")

	local var_2_1 = arg_2_0.GetResCntByAward(var_2_0)
	local var_2_2 = var_2_0[3]

	setText(arg_2_0.awardTxtTF, string.format(var_2_1 < var_2_2 and "<color=" .. COLOR_RED .. ">%s</color>/%s" or "%s/%s", arg_2_0.WrapNum(var_2_1), arg_2_0.WrapNum(var_2_2)))

	arg_2_0.res.text = arg_2_1.getConfig("award_contribution")

def var_0_0.GetResCntByAward(arg_3_0, arg_3_1):
	if arg_3_1[1] == DROP_TYPE_RESOURCE:
		return getProxy(PlayerProxy).getRawData().getResource(arg_3_1[2])
	elif arg_3_1[1] == DROP_TYPE_ITEM:
		return getProxy(BagProxy).getItemCountById(arg_3_1[2])
	else
		assert(False)

def var_0_0.WrapNum(arg_4_0, arg_4_1):
	if arg_4_1 > 1000000:
		return math.floor(arg_4_1 / 1000000) .. "M"
	elif arg_4_1 > 1000:
		return math.floor(arg_4_1 / 1000) .. "K"

	return arg_4_1

def var_0_0.Dispose(arg_5_0):
	return

return var_0_0
