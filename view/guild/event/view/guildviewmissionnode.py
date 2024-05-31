local var_0_0 = class("GuildViewMissionNode")
local var_0_1 = 200
local var_0_2 = 150
local var_0_3 = 100

var_0_0.LINE_LEFT = 1
var_0_0.LINE_RIGHT = 2
var_0_0.TOP_LINK = 3
var_0_0.BOTTOM_LINK = 4
var_0_0.CENTER_LINK = 5
var_0_0.TOP_HRZ_LINK = 6
var_0_0.BOTTOM_HRZ_LINK = 7

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0._go = arg_1_1.go
	arg_1_0._tf = tf(arg_1_0._go)
	arg_1_0.slot = arg_1_1.slot
	arg_1_0.data = arg_1_1.data
	arg_1_0.parent = arg_1_1.parent
	arg_1_0.childs = {}
	arg_1_0.offset = 0
	arg_1_0.lineContainer = arg_1_0._tf.Find("lines")
	arg_1_0.lines = {}
	arg_1_0.subLockBg = arg_1_0._tf.Find("sub_lock")
	arg_1_0.subUnlockBg = arg_1_0._tf.Find("sub_unlock")
	arg_1_0.unlockBg = arg_1_0._tf.Find("unlock")
	arg_1_0.lockBg = arg_1_0._tf.Find("lock")
	arg_1_0.nameTxt = arg_1_0._tf.Find("Text").GetComponent(typeof(Text))
	arg_1_0.selected = arg_1_0._tf.Find("selected")
	arg_1_0.tip = arg_1_0._tf.Find("tip")

def var_0_0.Init(arg_2_0):
	arg_2_0.UpdateStyle()
	arg_2_0.CalcOffset()
	arg_2_0.SetPosition()

def var_0_0.IsFinish(arg_3_0):
	return arg_3_0.data.IsFinish()

def var_0_0.IsUnLock(arg_4_0):
	if not arg_4_0.parent:
		return True
	else
		return arg_4_0.ParentIFinish() and arg_4_0.IsActive()

def var_0_0.ParentIFinish(arg_5_0):
	if not arg_5_0.parent:
		return False

	return arg_5_0.parent.IsFinish()

def var_0_0.ParentIsFinishByServer(arg_6_0):
	if not arg_6_0.parent:
		return False

	return arg_6_0.parent.data.IsFinishedByServer()

def var_0_0.IsActive(arg_7_0):
	return arg_7_0.data.IsActive()

def var_0_0.GetParentId(arg_8_0):
	if not arg_8_0.parent:
		return 0

	return arg_8_0.parent.data.id

def var_0_0.UpdateData(arg_9_0, arg_9_1):
	arg_9_0.data = arg_9_1

	arg_9_0.UpdateStyle()
	arg_9_0.UpdateLineStyle()

	for iter_9_0, iter_9_1 in ipairs(arg_9_0.childs):
		iter_9_1.UpdateStyle()
		iter_9_1.UpdateLineStyle()

def var_0_0.UpdateStyle(arg_10_0):
	local var_10_0 = arg_10_0.IsFinish()
	local var_10_1 = not arg_10_0.IsUnLock()
	local var_10_2 = arg_10_0.IsMain()

	setActive(arg_10_0.subLockBg, not var_10_0 and not var_10_2 and var_10_1)
	setActive(arg_10_0.subUnlockBg, not var_10_0 and not var_10_2 and not var_10_1)
	setActive(arg_10_0.unlockBg, not var_10_0 and var_10_2 and not var_10_1)
	setActive(arg_10_0.lockBg, not var_10_0 and var_10_2 and var_10_1)

	arg_10_0.nameTxt.text = var_10_1 and "" or arg_10_0.data.GetName()

	arg_10_0.UpdateTip()

def var_0_0.UpdateTip(arg_11_0):
	local var_11_0 = arg_11_0.IsUnLock() and arg_11_0.data.CanFormation() and not arg_11_0.IsFinish()

	setActive(arg_11_0.tip, var_11_0)

local var_0_4 = {
	"blue",
	"gray",
	"yellow"
}

def var_0_0.UpdateLineStyle(arg_12_0):
	local var_12_0

	local function var_12_1(arg_13_0, arg_13_1)
		if arg_13_0.gameObject.name == "line":
			arg_13_0.GetComponent(typeof(Image)).sprite = GetSpriteFromAtlas("ui/guildmissionui_atlas", arg_13_1 .. "_line")
		elif arg_13_0.gameObject.name == "head":
			arg_13_0.GetComponent(typeof(Image)).sprite = GetSpriteFromAtlas("ui/guildmissionui_atlas", arg_13_1)
		elif arg_13_0.gameObject.name == "adapter":
			eachChild(arg_13_0, function(arg_14_0)
				var_12_1(arg_14_0, arg_13_1))

	local var_12_2 = arg_12_0.IsFinish()

	for iter_12_0, iter_12_1 in ipairs(arg_12_0.childs):
		local var_12_3 = arg_12_0.lines[iter_12_1]
		local var_12_4 = iter_12_1.IsMain()

		for iter_12_2, iter_12_3 in ipairs(var_12_3):
			local var_12_5 = var_12_2 and var_0_4[2] or var_12_4 and var_0_4[3] or var_0_4[1]

			var_12_1(iter_12_3.tf, var_12_5)

	local var_12_6 = arg_12_0.lines[arg_12_0] or {}
	local var_12_7 = arg_12_0.IsMain()
	local var_12_8 = True

	if arg_12_0.parent:
		var_12_8 = arg_12_0.parent.IsFinish()

	for iter_12_4, iter_12_5 in ipairs(var_12_6):
		local var_12_9

		if iter_12_5.type == var_0_0.LINE_LEFT:
			var_12_9 = (var_12_2 or var_12_8) and var_0_4[2] or var_12_7 and var_0_4[3] or var_0_4[1]
		else
			var_12_9 = var_12_2 and var_0_4[2] or var_12_7 and var_0_4[3] or var_0_4[1]

		var_12_1(iter_12_5.tf, var_12_9)

def var_0_0.Selected(arg_15_0, arg_15_1):
	setActive(arg_15_0.selected, arg_15_1)

def var_0_0.CalcOffset(arg_16_0):
	if not arg_16_0.parent:
		arg_16_0.offset = 0

		return

	if #arg_16_0.parent.childs == 2:
		local var_16_0 = arg_16_0.IsMain()
		local var_16_1 = arg_16_0.GetParentOffset()
		local var_16_2 = 1
		local var_16_3 = -1
		local var_16_4 = math.abs(var_16_1 + var_16_2)
		local var_16_5 = math.abs(var_16_1 + var_16_3)

		if var_16_5 <= var_16_4:
			arg_16_0.offset = var_16_0 and var_16_3 or var_16_2
		elif var_16_4 < var_16_5:
			arg_16_0.offset = var_16_0 and var_16_2 or var_16_3
	elif #arg_16_0.parent.childs == 1:
		arg_16_0.offset = 0 - arg_16_0.parent.GetFirstNodeOffset()

def var_0_0.GetLocalPosition(arg_17_0):
	if arg_17_0.parent:
		local var_17_0 = arg_17_0.GetOffset()
		local var_17_1 = (arg_17_0.slot - 1) * (var_0_1 + arg_17_0._tf.sizeDelta.x)
		local var_17_2 = arg_17_0.parent.GetLocalPosition()
		local var_17_3 = arg_17_0.IsMain() and 0 or var_0_3
		local var_17_4 = var_17_2.y + var_17_0 * var_0_2 + (var_17_0 > 0 and var_17_3 or -var_17_3)

		return Vector3(var_17_1, var_17_4, 0)
	else
		return Vector3(0, 0, 0)

def var_0_0.SetPosition(arg_18_0):
	local var_18_0 = arg_18_0.GetLocalPosition()

	arg_18_0._tf.anchoredPosition = var_18_0

def var_0_0.AddChild(arg_19_0, arg_19_1):
	table.insert(arg_19_0.childs, arg_19_1)

def var_0_0.GetChilds(arg_20_0):
	return arg_20_0.childs

def var_0_0.HasParent(arg_21_0):
	return arg_21_0.parent != None

def var_0_0.HasChild(arg_22_0):
	return #arg_22_0.childs > 0

def var_0_0.IsMain(arg_23_0):
	return arg_23_0.data.IsMain()

def var_0_0.GetOffset(arg_24_0):
	return arg_24_0.offset

def var_0_0.GetParentOffset(arg_25_0):
	assert(arg_25_0.parent)

	return arg_25_0.parent.GetOffset()

def var_0_0.GetFirstNodeOffset(arg_26_0):
	local var_26_0 = 0
	local var_26_1 = arg_26_0

	while var_26_1.parent != None:
		var_26_0 = var_26_0 + var_26_1.GetOffset()
		var_26_1 = var_26_1.parent

	return var_26_0

def var_0_0.AddLine(arg_27_0, arg_27_1, arg_27_2, arg_27_3):
	arg_27_1 = tf(arg_27_1)

	SetParent(arg_27_1, arg_27_0.lineContainer)

	if arg_27_2 == var_0_0.LINE_LEFT:
		if arg_27_0.IsMain():
			arg_27_1.anchorMax = Vector2(0, 0.5)
			arg_27_1.anchorMin = Vector2(0, 0.5)
			arg_27_1.pivot = Vector2(1, 0.5)
			arg_27_1.anchoredPosition = Vector2(0, 0)
		else
			arg_27_1.pivot = Vector2(1, 0.5)

			if arg_27_0.GetOffset() > 0:
				arg_27_1.anchorMax = Vector2(0.5, 0)
				arg_27_1.anchorMin = Vector2(0.5, 0)
				arg_27_1.eulerAngles = Vector3(0, 0, 90)
				arg_27_1.anchoredPosition = Vector2(0, 0)
			else
				arg_27_1.anchorMax = Vector2(0.5, 1)
				arg_27_1.anchorMin = Vector2(0.5, 1)
				arg_27_1.eulerAngles = Vector3(0, 0, -90)
				arg_27_1.anchoredPosition = Vector2(0, 0)
	elif arg_27_2 == var_0_0.LINE_RIGHT:
		arg_27_1.anchorMax = Vector2(1, 0.5)
		arg_27_1.anchorMin = Vector2(1, 0.5)
		arg_27_1.pivot = Vector2(0, 0.5)
		arg_27_1.anchoredPosition = Vector2(0, 0)
	elif arg_27_2 == var_0_0.TOP_LINK:
		arg_27_1.anchorMax = Vector2(1, 0.5)
		arg_27_1.anchorMin = Vector2(1, 0.5)
		arg_27_1.pivot = Vector2(1, 0.5)

		local var_27_0 = arg_27_0.lines[arg_27_0][1].tf.sizeDelta.x

		arg_27_1.anchoredPosition = Vector2(var_27_0, 0)
		arg_27_1.eulerAngles = Vector3(0, 0, -90)

		local var_27_1 = arg_27_3.GetLocalPosition().y - arg_27_0.GetLocalPosition().y

		if arg_27_3.IsMain():
			arg_27_1.sizeDelta = Vector2(var_27_1, arg_27_1.sizeDelta.y)
		else
			arg_27_1.sizeDelta = Vector2(var_27_1 - var_27_0 - arg_27_0._tf.sizeDelta.y / 2, arg_27_1.sizeDelta.y)
	elif arg_27_2 == var_0_0.BOTTOM_LINK:
		arg_27_1.anchorMax = Vector2(1, 0.5)
		arg_27_1.anchorMin = Vector2(1, 0.5)
		arg_27_1.pivot = Vector2(1, 0.5)

		local var_27_2 = arg_27_0.lines[arg_27_0][1].tf.sizeDelta.x

		arg_27_1.anchoredPosition = Vector2(var_27_2, 0)
		arg_27_1.eulerAngles = Vector3(0, 0, 90)

		local var_27_3 = arg_27_3.GetLocalPosition().y - arg_27_0.GetLocalPosition().y

		if arg_27_3.IsMain():
			arg_27_1.sizeDelta = Vector2(-var_27_3, arg_27_1.sizeDelta.y)
		else
			arg_27_1.sizeDelta = Vector2(-var_27_3 - var_27_2 - arg_27_0._tf.sizeDelta.y / 2, arg_27_1.sizeDelta.y)
	elif arg_27_2 == var_0_0.TOP_HRZ_LINK:
		local var_27_4 = arg_27_0.lines[arg_27_3][1].tf
		local var_27_5 = arg_27_0.lines[arg_27_0][1].tf.sizeDelta.x
		local var_27_6 = var_27_4.sizeDelta.x + var_27_4.anchoredPosition.y

		arg_27_1.anchoredPosition = Vector2(var_27_4.anchoredPosition.x, var_27_6)

		local var_27_7 = arg_27_3.GetLocalPosition()
		local var_27_8 = arg_27_0.GetLocalPosition()
		local var_27_9

		if arg_27_3.IsMain():
			var_27_9 = var_27_7.x - var_27_8.x - 2 * var_27_5 - arg_27_0._tf.sizeDelta.x
		else
			nextNodeLposX = var_27_7.x + arg_27_0._tf.sizeDelta.x / 2
			var_27_9 = nextNodeLposX - var_27_8.x - arg_27_0._tf.sizeDelta.x - var_27_5

		arg_27_1.sizeDelta = Vector2(var_27_9, arg_27_1.sizeDelta.y)
	elif arg_27_2 == var_0_0.BOTTOM_HRZ_LINK:
		local var_27_10 = arg_27_0.lines[arg_27_3][1].tf
		local var_27_11 = arg_27_0.lines[arg_27_0][1].tf.sizeDelta.x
		local var_27_12 = var_27_10.anchoredPosition.y - var_27_10.sizeDelta.x

		arg_27_1.anchoredPosition = Vector2(var_27_10.anchoredPosition.x, var_27_12)

		local var_27_13 = arg_27_3.GetLocalPosition()
		local var_27_14 = arg_27_0.GetLocalPosition()
		local var_27_15

		if arg_27_3.IsMain():
			var_27_15 = var_27_13.x - var_27_14.x - 2 * var_27_11 - arg_27_0._tf.sizeDelta.x
		else
			nextNodeLposX = var_27_13.x + arg_27_0._tf.sizeDelta.x / 2
			var_27_15 = nextNodeLposX - var_27_14.x - arg_27_0._tf.sizeDelta.x - var_27_11

		arg_27_1.sizeDelta = Vector2(var_27_15, arg_27_1.sizeDelta.y)
	elif arg_27_2 == var_0_0.CENTER_LINK:
		local var_27_16 = arg_27_3.GetLocalPosition()
		local var_27_17 = arg_27_0.GetLocalPosition()
		local var_27_18 = arg_27_0.lines[arg_27_0][1].tf.sizeDelta.x
		local var_27_19 = var_27_16.x - var_27_17.x - arg_27_0._tf.sizeDelta.x - 2 * var_27_18

		arg_27_1.anchorMax = Vector2(1, 0.5)
		arg_27_1.anchorMin = Vector2(1, 0.5)
		arg_27_1.anchoredPosition = Vector2(var_27_18, 0)
		arg_27_1.sizeDelta = Vector2(var_27_19, arg_27_1.sizeDelta.y)

	if not arg_27_0.lines[arg_27_3]:
		arg_27_0.lines[arg_27_3] = {}

	table.insert(arg_27_0.lines[arg_27_3], {
		tf = arg_27_1,
		type = arg_27_2
	})

return var_0_0
