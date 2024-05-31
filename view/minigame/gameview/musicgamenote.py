local var_0_0 = class("MusicGameNote")

var_0_0.easyTriggerStepTime = None
var_0_0.type_left = 1
var_0_0.type_right = 2
var_0_0.type_pu_normal = 1
var_0_0.type_pu_both = 2
var_0_0.type_dgree_easy = 1
var_0_0.type_dgree_hard = 2

local var_0_1 = 1
local var_0_2 = 2
local var_0_3 = 3
local var_0_4 = 4
local var_0_5 = 4
local var_0_6 = 0
local var_0_7 = 1
local var_0_8 = 2
local var_0_9 = {
	500,
	800,
	1250,
	1450
}
local var_0_10 = {
	0.26,
	0.2,
	0.15,
	0.13
}
local var_0_11 = 3
local var_0_12
local var_0_13 = False

local function var_0_14(arg_1_0)
	local var_1_0 = {
		_tf = arg_1_0
	}

	var_1_0.type = None
	var_1_0.beginTime = None
	var_1_0.endTime = None
	var_1_0.longFlag = None
	var_1_0.removeTime = None
	var_1_0.speedOffsetX = None
	var_1_0.longTime = 0
	var_1_0.triggerDown = None
	var_1_0.triggerUp = None
	var_1_0.fixedScoreType = None

	function var_1_0.Ctor(arg_2_0)
		arg_2_0.longTf = findTF(arg_2_0._tf, "longNote")
		arg_2_0.singleTf = findTF(arg_2_0._tf, "singleNote")

	function var_1_0.stepUpdate(arg_3_0, arg_3_1)
		if not isActive(arg_3_0._tf):
			arg_3_0.changeActive(True)

		local var_3_0 = (arg_3_1 - arg_3_0.beginTime) * arg_3_0.speedOffsetX

		if var_3_0 > 0:
			var_3_0 = 0

		arg_3_0._tf.localPosition = Vector3(var_3_0, 0, 0)

		if arg_3_0.longFlag:
			local var_3_1

			if var_3_0 == 0:
				var_3_1 = (arg_3_0.endTime - arg_3_1) * arg_3_0.speedOffsetX

				if not arg_3_0.triggerDown and not arg_3_0.removeTime:
					arg_3_0.removeTime = arg_3_1 + var_0_12
			else
				var_3_1 = (arg_3_0.endTime - arg_3_0.beginTime) * arg_3_0.speedOffsetX

			if var_3_1 < 0:
				var_3_1 = 0

			arg_3_0.longTf.sizeDelta = Vector2(var_3_1, arg_3_0.longTf.sizeDelta.y)

			if var_3_1 == 0 and not arg_3_0.triggerUp and not arg_3_0.removeTime:
				arg_3_0.removeTime = arg_3_1 + var_0_12
		elif var_3_0 == 0 and not arg_3_0.removeTime:
			arg_3_0.removeTime = arg_3_1 + var_0_12

	function var_1_0.setNoteData(arg_4_0, arg_4_1, arg_4_2, arg_4_3, arg_4_4)
		arg_4_0.removeTime = None
		arg_4_0.triggerDown = None
		arg_4_0.triggerUp = None
		arg_4_0.fixedScoreType = None
		arg_4_0.keyType = arg_4_1.key_flag == "K_BOTH" and MusicGameNote.type_pu_both or MusicGameNote.type_pu_normal
		arg_4_0.beginTime = tonumber(arg_4_1.begin_time)
		arg_4_0.endTime = tonumber(arg_4_1.end_time)
		arg_4_0.longTime = arg_4_0.endTime - arg_4_0.beginTime
		arg_4_0.longFlag = arg_4_1.begin_time != arg_4_1.end_time
		arg_4_0.speedOffsetX = arg_4_2
		arg_4_0.dgree = arg_4_3
		arg_4_0.directType = arg_4_4
		arg_4_0.imgType = arg_4_0.getImageType()
		arg_4_0._tf.localPosition = Vector3(0, 0, 0)
		arg_4_0._tf.name = "beginTime" .. arg_4_0.beginTime

		arg_4_0.updateNoteTf()

	function var_1_0.updateNoteTf(arg_5_0)
		setActive(findTF(arg_5_0._tf, "singleNote"), False)
		setActive(findTF(arg_5_0._tf, "longNote"), False)

		if arg_5_0.longFlag:
			setActive(findTF(arg_5_0._tf, "longNote"), True)

			for iter_5_0 = 1, var_0_5:
				setActive(findTF(arg_5_0._tf, "longNote/note/img" .. iter_5_0), iter_5_0 == arg_5_0.imgType)
				setActive(findTF(arg_5_0._tf, "longNote/long/img" .. iter_5_0), iter_5_0 == arg_5_0.imgType)
		else
			setActive(findTF(arg_5_0._tf, "singleNote"), True)

			for iter_5_1 = 1, var_0_5:
				setActive(findTF(arg_5_0._tf, "singleNote/note/img" .. iter_5_1), iter_5_1 == arg_5_0.imgType)

	function var_1_0.getImageType(arg_6_0)
		if arg_6_0.dgree == MusicGameNote.type_dgree_easy:
			return var_0_1
		elif arg_6_0.keyType == MusicGameNote.type_pu_both:
			return var_0_4
		elif arg_6_0.directType == MusicGameNote.type_left:
			return var_0_2
		elif arg_6_0.directType == MusicGameNote.type_right:
			return var_0_3

		return var_0_1

	function var_1_0.getRemoveTime(arg_7_0)
		return arg_7_0.removeTime

	function var_1_0.triggerScore(arg_8_0)
		if arg_8_0.removeTime:
			arg_8_0.removeTime = None

	function var_1_0.changeActive(arg_9_0, arg_9_1)
		setActive(arg_9_0._tf, arg_9_1)

	function var_1_0.dispose(arg_10_0)
		if arg_10_0._tf:
			Destroy(arg_10_0._tf)

	var_1_0.Ctor()

	return var_1_0

def var_0_0.Ctor(arg_11_0, arg_11_1, arg_11_2, arg_11_3):
	arg_11_0._tf = arg_11_1
	arg_11_0.noteTpl = arg_11_2
	arg_11_0.directType = arg_11_3
	arg_11_0.noteStateCallback = None
	arg_11_0.notePool = {}
	arg_11_0.noteList = {}

def var_0_0.setStateCallback(arg_12_0, arg_12_1):
	arg_12_0.noteStateCallback = arg_12_1

def var_0_0.setLongTimeCallback(arg_13_0, arg_13_1):
	arg_13_0.longNoteCallback = arg_13_1

def var_0_0.setStartData(arg_14_0, arg_14_1, arg_14_2, arg_14_3, arg_14_4):
	var_0_12 = var_0_10[arg_14_2]
	arg_14_0.puList = arg_14_1
	arg_14_0.speedLevel = arg_14_2
	arg_14_0.dgree = arg_14_3
	arg_14_0.noteType = arg_14_4
	arg_14_0.speedOffsetX = var_0_9[arg_14_2]
	arg_14_0.tplNote = findTF(arg_14_0.noteTpl, "tplNote" .. arg_14_4)

	if arg_14_0.lastNoteType and arg_14_0.lastNoteType != arg_14_4:
		arg_14_0.destroyNoteAll()
	else
		arg_14_0.clearNote()

	arg_14_0.lastNoteType = arg_14_0.noteType

def var_0_0.step(arg_15_0, arg_15_1):
	arg_15_0.stepTime = arg_15_1 / 1000

	if #arg_15_0.noteList > 0:
		local var_15_0 = arg_15_0.noteList[1]
		local var_15_1 = arg_15_0.checkScoreType(var_15_0)

		if var_15_1:
			var_15_0.triggerScore()
			arg_15_0.noteStateCallback(var_15_1)

			if not var_15_0.longFlag or var_15_1 == var_0_6:
				arg_15_0.returnNote(table.remove(arg_15_0.noteList, 1))
			elif var_15_0.longFlag and var_15_0.triggerUp:
				arg_15_0.returnNote(table.remove(arg_15_0.noteList, 1))

				if arg_15_0.longNoteCallback:
					arg_15_0.longNoteCallback(var_15_0.longTime)

	for iter_15_0 = #arg_15_0.noteList, 1, -1:
		local var_15_2 = arg_15_0.noteList[iter_15_0].fixedScoreType

		if var_15_2 and arg_15_0.noteStateCallback:
			arg_15_0.noteStateCallback(var_15_2)

			if arg_15_0.loopFlag:
				arg_15_0.loopFlag = False

			arg_15_0.returnNote(table.remove(arg_15_0.noteList, iter_15_0))

	for iter_15_1 = #arg_15_0.noteList, 1, -1:
		local var_15_3 = arg_15_0.noteList[iter_15_1]
		local var_15_4 = var_15_3.longFlag
		local var_15_5 = var_15_3.triggerDown
		local var_15_6 = arg_15_0.noteList[iter_15_1].getRemoveTime()

		if var_15_6 and var_15_6 < arg_15_0.stepTime:
			if arg_15_0.noteStateCallback:
				if not var_0_13:
					arg_15_0.noteStateCallback(var_0_6)
				else
					arg_15_0.noteStateCallback(var_0_8)

			if arg_15_0.loopFlag:
				arg_15_0.loopFlag = False

			arg_15_0.returnNote(table.remove(arg_15_0.noteList, iter_15_1))

	for iter_15_2 = #arg_15_0.noteList, 1, -1:
		arg_15_0.noteList[iter_15_2].stepUpdate(arg_15_0.stepTime)

	if arg_15_0.puList and #arg_15_0.puList > 0:
		local var_15_7 = arg_15_0.puList[1]

		if arg_15_0.checkPuShow(var_15_7):
			arg_15_0.pushNoteToList(arg_15_0.getNote(var_15_7))
			table.remove(arg_15_0.puList, 1)

def var_0_0.checkScoreType(arg_16_0, arg_16_1):
	if arg_16_0.dgree == MusicGameNote.type_dgree_easy and arg_16_0.keyDownStepTime and arg_16_0.keyDownStepTime and arg_16_0.keyDownStepTime == MusicGameNote.easyTriggerStepTime:
		arg_16_0.keyDownTrigger = True

	local var_16_0
	local var_16_1
	local var_16_2 = False

	if not arg_16_1.longFlag:
		local var_16_3 = arg_16_1.beginTime

		if arg_16_0.keyDownStepTime and not arg_16_0.keyDownTrigger:
			local var_16_4 = math.abs(arg_16_0.keyDownStepTime - var_16_3)

			if arg_16_1.keyType == MusicGameNote.type_pu_both:
				if arg_16_0.keyBothDown:
					var_16_0 = arg_16_0.getScoreType(var_16_4)
			else
				var_16_0 = arg_16_0.getScoreType(var_16_4)

			if var_16_0:
				arg_16_1.triggerDown = True
				arg_16_0.keyDownTrigger = True

				if arg_16_0.dgree == MusicGameNote.type_dgree_easy:
					MusicGameNote.easyTriggerStepTime = arg_16_0.keyDownStepTime
	elif not arg_16_1.triggerDown:
		local var_16_5 = arg_16_1.beginTime

		if arg_16_0.keyDownStepTime and not arg_16_0.keyDownTrigger:
			local var_16_6 = math.abs(arg_16_0.keyDownStepTime - var_16_5)

			if arg_16_1.keyType == MusicGameNote.type_pu_both:
				if arg_16_0.keyBothDown:
					var_16_0 = arg_16_0.getScoreType(var_16_6)
			else
				var_16_0 = arg_16_0.getScoreType(var_16_6)

			if var_16_0:
				arg_16_1.triggerDown = True
				arg_16_0.keyDownTrigger = True
				arg_16_0.loopFlag = True
	else
		local var_16_7 = arg_16_1.endTime
		local var_16_8 = arg_16_0.stepTime < var_16_7 - var_0_12

		if not arg_16_0.keyDown and var_16_8:
			if arg_16_0.loopFlag:
				arg_16_0.loopFlag = False

			arg_16_1.fixedScoreType, arg_16_1.endTime = arg_16_0.getScoreType(math.abs(arg_16_0.stepTime - arg_16_1.endTime)) or var_0_7, arg_16_1.beginTime
			var_16_0 = None
		elif arg_16_0.keyUpStepTime and not arg_16_0.keyUpTrigger:
			local var_16_9 = math.abs(arg_16_0.keyUpStepTime - var_16_7)

			if arg_16_1.keyType == MusicGameNote.type_pu_both:
				if arg_16_0.keyBothUp:
					var_16_0 = arg_16_0.getScoreType(var_16_9)
			else
				var_16_0 = arg_16_0.getScoreType(var_16_9)

			if var_16_0:
				if arg_16_0.loopFlag:
					arg_16_0.loopFlag = False

				arg_16_1.triggerUp = True
				arg_16_0.keyUpTrigger = True

	return var_16_0

def var_0_0.loopTime(arg_17_0):
	return arg_17_0.loopFlag

def var_0_0.getScoreType(arg_18_0, arg_18_1):
	if arg_18_1 < var_0_12 / 2:
		return var_0_8
	elif arg_18_1 < var_0_12:
		return var_0_7

	return None

def var_0_0.pushNoteToList(arg_19_0, arg_19_1):
	table.insert(arg_19_0.noteList, arg_19_1)

def var_0_0.checkPuShow(arg_20_0, arg_20_1):
	if arg_20_1.begin_time - arg_20_0.stepTime <= var_0_11:
		return True

	return False

def var_0_0.destroyNoteAll(arg_21_0):
	for iter_21_0 = #arg_21_0.noteList, 1, -1:
		arg_21_0.noteList[iter_21_0].dispose()

	for iter_21_1 = #arg_21_0.notePool, 1, -1:
		arg_21_0.notePool[iter_21_1].dispose()

	arg_21_0.noteList = {}
	arg_21_0.notePool = {}

def var_0_0.clearNote(arg_22_0):
	for iter_22_0 = #arg_22_0.noteList, 1, -1:
		local var_22_0 = table.remove(arg_22_0.noteList, iter_22_0)

		arg_22_0.returnNote(var_22_0)

def var_0_0.getNote(arg_23_0, arg_23_1):
	if #arg_23_0.notePool == 0:
		local var_23_0 = arg_23_0.createNote()

		table.insert(arg_23_0.notePool, var_23_0)

	local var_23_1 = table.remove(arg_23_0.notePool, 1)

	var_23_1.setNoteData(arg_23_1, arg_23_0.speedOffsetX, arg_23_0.dgree, arg_23_0.directType)

	return var_23_1

def var_0_0.returnNote(arg_24_0, arg_24_1):
	arg_24_1.changeActive(False)
	table.insert(arg_24_0.notePool, arg_24_1)

def var_0_0.createNote(arg_25_0):
	local var_25_0 = tf(instantiate(arg_25_0.tplNote))

	setActive(var_25_0, False)

	local var_25_1 = var_0_14(var_25_0)

	setParent(var_25_0, arg_25_0._tf)

	return var_0_14(var_25_0)

def var_0_0.onKeyDown(arg_26_0):
	arg_26_0.keyDown = True
	arg_26_0.keyUp = False
	arg_26_0.keyDownStepTime = arg_26_0.stepTime
	arg_26_0.keyDownTrigger = False
	arg_26_0.keyBothDown = False

def var_0_0.onKeyUp(arg_27_0):
	arg_27_0.keyUp = True
	arg_27_0.keyDown = False
	arg_27_0.keyUpStepTime = arg_27_0.stepTime
	arg_27_0.keyUpTrigger = False
	arg_27_0.keyBothUp = False

def var_0_0.bothDown(arg_28_0):
	arg_28_0.keyDownStepTime = arg_28_0.stepTime
	arg_28_0.keyBothDown = True
	arg_28_0.keyBothUp = False

def var_0_0.bothUp(arg_29_0):
	arg_29_0.keyBothUp = True
	arg_29_0.keyBothDown = False
	arg_29_0.keyUpStepTime = arg_29_0.stepTime

return var_0_0
