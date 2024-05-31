local var_0_0 = class("StoryRecorder")
local var_0_1 = "#5ce6ff"
local var_0_2 = "#70747F"
local var_0_3 = "#BCBCBC"
local var_0_4 = "#FFFFFF"

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.recordList = {}
	arg_1_0.displays = {}

def var_0_0.Add(arg_2_0, arg_2_1):
	table.insert(arg_2_0.recordList, arg_2_1)

def var_0_0.GetContentList(arg_3_0):
	local var_3_0 = arg_3_0.Convert()

	for iter_3_0, iter_3_1 in ipairs(var_3_0):
		table.insert(arg_3_0.displays, iter_3_1)

	return arg_3_0.displays

def var_0_0.Convert(arg_4_0):
	local var_4_0 = {}

	for iter_4_0, iter_4_1 in ipairs(arg_4_0.recordList):
		local var_4_1 = iter_4_1.GetMode()

		if var_4_1 == Story.MODE_ASIDE:
			arg_4_0.CollectAsideContent(var_4_0, iter_4_1)
		elif var_4_1 == Story.MODE_DIALOGUE or var_4_1 == Story.MODE_BG:
			arg_4_0.CollectDialogueContent(var_4_0, iter_4_1)

	arg_4_0.recordList = {}

	return var_4_0

local function var_0_5(arg_5_0)
	local var_5_0 = {
		"<size=%d+>",
		"</size>",
		"<color=%w+>",
		"</color>"
	}
	local var_5_1 = arg_5_0

	for iter_5_0, iter_5_1 in ipairs(var_5_0):
		var_5_1 = string.gsub(var_5_1, iter_5_1, "")

	return var_5_1

def var_0_0.CollectAsideContent(arg_6_0, arg_6_1, arg_6_2):
	local var_6_0 = arg_6_2.GetSequence()
	local var_6_1 = {}

	for iter_6_0, iter_6_1 in ipairs(var_6_0):
		table.insert(var_6_1, var_0_5(iter_6_1[1]))

	table.insert(arg_6_1, {
		isPlayer = False,
		list = var_6_1
	})

def var_0_0.CollectDialogueContent(arg_7_0, arg_7_1, arg_7_2):
	local var_7_0 = arg_7_2.GetPaintingIcon()
	local var_7_1 = arg_7_2.GetName()
	local var_7_2 = ""

	if getProxy(PlayerProxy):
		var_7_2 = getProxy(PlayerProxy).getRawData().name

	local var_7_3 = var_7_1 == var_7_2

	local function var_7_4()
		local var_8_0 = arg_7_2.GetNameColor()

		return var_7_3 and var_0_1 or var_8_0 or var_0_3

	local var_7_5 = arg_7_2.GetContent()

	table.insert(arg_7_1, {
		icon = var_7_0,
		name = var_7_1,
		nameColor = var_7_4(),
		list = {
			setColorStr(var_0_5(var_7_5), var_7_3 and var_0_1 or var_0_4)
		},
		isPlayer = var_7_3
	})

	if arg_7_2.ExistOption():
		local var_7_6 = arg_7_2.GetSelectedBranchCode()
		local var_7_7 = {}

		for iter_7_0, iter_7_1 in ipairs(arg_7_2.GetOptions()):
			local var_7_8 = iter_7_1[2] == var_7_6
			local var_7_9 = setColorStr("[ " .. var_0_5(iter_7_1[1]) .. " ]", var_7_8 and var_0_1 or var_0_2)

			table.insert(var_7_7, var_7_9)

		table.insert(arg_7_1, {
			isPlayer = True,
			name = var_7_2,
			nameColor = var_0_1,
			list = var_7_7
		})

def var_0_0.Clear(arg_9_0):
	arg_9_0.recordList = {}
	arg_9_0.displays = {}

def var_0_0.Dispose(arg_10_0):
	arg_10_0.Clear()

return var_0_0
