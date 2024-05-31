﻿local var_0_0 = class("EmojiProxy", import(".NetProxy"))

var_0_0.NEW_EMOJI_SAVE_TAG = "new_emoji_save_tag_"

function var_0_0.register(arg_1_0)
	arg_1_0._initedTag = false
	arg_1_0._emojiIDList = {}
	arg_1_0._newIDList = {}
end

function var_0_0.getInitedTag(arg_2_0)
	return arg_2_0._initedTag
end

function var_0_0.setInitedTag(arg_3_0)
	arg_3_0._initedTag = true
end

function var_0_0.getNewEmojiIDLIst(arg_4_0)
	return Clone(arg_4_0._newIDList)
end

function var_0_0.addToEmojiIDLIst(arg_5_0, arg_5_1)
	if table.indexof(arg_5_0._emojiIDList, arg_5_1, 1) then
		return
	end

	table.insert(arg_5_0._emojiIDList, arg_5_1)
end

function var_0_0.saveNewEmojiIDList(arg_6_0)
	local var_6_0 = {}

	for iter_6_0, iter_6_1 in pairs(arg_6_0._newIDList) do
		table.insert(var_6_0, iter_6_1)
	end

	local var_6_1 = getProxy(PlayerProxy):getRawData().id

	PlayerPrefs.SetString(var_0_0.NEW_EMOJI_SAVE_TAG .. var_6_1, table.concat(var_6_0, ":"))
end

function var_0_0.loadNewEmojiIDList(arg_7_0)
	arg_7_0._newIDList = {}

	local var_7_0 = getProxy(PlayerProxy):getRawData().id
	local var_7_1 = string.split(PlayerPrefs.GetString(var_0_0.NEW_EMOJI_SAVE_TAG .. var_7_0) or "", ":")

	if #var_7_1 > 0 then
		for iter_7_0, iter_7_1 in pairs(var_7_1) do
			table.insert(arg_7_0._newIDList, tonumber(iter_7_1))
		end
	end
end

function var_0_0.addNewEmojiID(arg_8_0, arg_8_1)
	if table.indexof(arg_8_0._emojiIDList, arg_8_1, 1) then
		return
	end

	table.insert(arg_8_0._emojiIDList, arg_8_1)
	table.insert(arg_8_0._newIDList, arg_8_1)
	arg_8_0:saveNewEmojiIDList()
end

function var_0_0.removeNewEmojiID(arg_9_0, arg_9_1)
	local var_9_0 = table.indexof(arg_9_0._newIDList, arg_9_1, 1)

	if not var_9_0 then
		assert(false, "new emoji list does not exit this emojiID:" .. arg_9_1)
	else
		table.remove(arg_9_0._newIDList, var_9_0)
	end

	arg_9_0:saveNewEmojiIDList()
end

function var_0_0.fliteNewEmojiDataByType(arg_10_0)
	local var_10_0 = {}

	for iter_10_0, iter_10_1 in pairs(arg_10_0._newIDList) do
		local var_10_1 = pg.emoji_template[iter_10_1]
		local var_10_2 = var_10_1.type[1]

		if not var_10_0[var_10_2] then
			var_10_0[var_10_2] = {
				var_10_1
			}
		else
			table.insert(var_10_0[var_10_2], var_10_1)
		end
	end

	return var_10_0
end

function var_0_0.getEmojiDataByType(arg_11_0, arg_11_1)
	local var_11_0 = {}

	for iter_11_0, iter_11_1 in pairs(arg_11_0._emojiIDList) do
		local var_11_1 = pg.emoji_template[iter_11_1]

		if table.contains(var_11_1.type, arg_11_1) then
			table.insert(var_11_0, var_11_1)
		end
	end

	return var_11_0
end

function var_0_0.getExEmojiDataByType(arg_12_0, arg_12_1)
	local var_12_0 = {}

	for iter_12_0, iter_12_1 in pairs(arg_12_0._emojiIDList) do
		if not table.contains(arg_12_0._newIDList, iter_12_1) then
			local var_12_1 = pg.emoji_template[iter_12_1]

			if table.contains(var_12_1.type, arg_12_1) then
				table.insert(var_12_0, var_12_1)
			end
		end
	end

	return var_12_0
end

return var_0_0
