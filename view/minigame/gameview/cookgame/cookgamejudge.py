local var_0_0 = class("CookGameJudge")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4, arg_1_5):
	arg_1_0._tf = arg_1_1
	arg_1_0._judgeDatas = arg_1_3
	arg_1_0._gameData = arg_1_4
	arg_1_0._event = arg_1_5
	arg_1_0._index = arg_1_2
	arg_1_0.wantedTf = findTF(arg_1_0._tf, "wanted")
	arg_1_0.smokeTf = findTF(arg_1_0._tf, "wanted/smoke")
	arg_1_0.dftEvent = GetComponent(findTF(arg_1_0._tf, "mask/anim"), typeof(DftAniEvent))

	arg_1_0.dftEvent.SetEndEvent(function(arg_2_0)
		arg_1_0.onAniEnd())

	arg_1_0.animator = GetComponent(findTF(arg_1_0._tf, "mask/anim"), typeof(Animator))

	onButton(arg_1_0._event, findTF(arg_1_0._tf, "collider"), function()
		if arg_1_0.clickCallback:
			arg_1_0.clickCallback(), SFX_CANCEL)

def var_0_0.clear(arg_4_0):
	arg_4_0._puzzleTime = None
	arg_4_0._puzzleWeight = None
	arg_4_0._puzzleCamp = None
	arg_4_0.cakeId = 1
	arg_4_0.inTrigger = False
	arg_4_0.serveData = None
	arg_4_0.serveCallback = None

	arg_4_0.updateWanted(None)
	arg_4_0.showCard(None)
	setActive(arg_4_0.wantedTf, False)
	setActive(arg_4_0._tf, False)

	local var_4_0 = arg_4_0.getAnimData(arg_4_0.cakeId)

	arg_4_0.animator.runtimeAnimatorController = var_4_0.runtimeAnimator

	arg_4_0.select(False)

def var_0_0.start(arg_5_0):
	arg_5_0.clear()
	setActive(arg_5_0._tf, True)
	arg_5_0.updateWanted(math.random(1, arg_5_0._gameData.cake_num))

def var_0_0.step(arg_6_0, arg_6_1):
	if arg_6_0.wantedCakeTime and arg_6_0.wantedCakeTime > 0:
		arg_6_0.wantedCakeTime = arg_6_0.wantedCakeTime - arg_6_1

		if arg_6_0.wantedCakeTime <= 0:
			arg_6_0.wantedCakeTime = None

			arg_6_0.updateWanted(math.random(1, arg_6_0._gameData.cake_num))

	if arg_6_0._puzzleTime:
		arg_6_0._puzzleTime = arg_6_0._puzzleTime - arg_6_1

		if arg_6_0._puzzleTime <= 0:
			arg_6_0._puzzleTime = None
			arg_6_0._puzzleCamp = None
			arg_6_0._puzzleWeight = None

			arg_6_0.showCard(False)

	if arg_6_0.readyServeTime and arg_6_0.readyServeTime > 0:
		arg_6_0.readyServeTime = arg_6_0.readyServeTime - arg_6_1

		if arg_6_0.readyServeTime <= 0:
			arg_6_0.readyServeTime = None
			arg_6_0.serveData = None
			arg_6_0.serveCallback = None

def var_0_0.destroy(arg_7_0):
	return

def var_0_0.changeSpeed(arg_8_0, arg_8_1):
	arg_8_0.animator.speed = arg_8_1

def var_0_0.onAniEnd(arg_9_0):
	arg_9_0.inTrigger = False

	if arg_9_0.freshWanted:
		arg_9_0.freshWanted = False
		arg_9_0.wantedCakeTime = None

		arg_9_0.updateWanted(math.random(1, arg_9_0._gameData.cake_num))

def var_0_0.getIndex(arg_10_0):
	return arg_10_0._index

def var_0_0.getTf(arg_11_0):
	return arg_11_0._tf

def var_0_0.trigger(arg_12_0, arg_12_1, arg_12_2, arg_12_3, arg_12_4):
	if arg_12_0.inTrigger:
		print("评委已有状态")

		return

	local var_12_0 = Vector3(1, 1, 1)

	arg_12_0.inTrigger = True

	if arg_12_0.cakeId != arg_12_1:
		arg_12_0.cakeId = arg_12_1

		local var_12_1 = arg_12_0.getAnimData(arg_12_0.cakeId)

		arg_12_0.animator.runtimeAnimatorController = var_12_1.runtimeAnimator

	arg_12_0.animator.SetBool("AC", arg_12_3 or False)
	arg_12_0.animator.SetBool("right", arg_12_2 or False)
	arg_12_0.animator.SetBool("bk", arg_12_4 or False)
	arg_12_0.animator.SetBool("reject", arg_12_0._puzzleCamp and True or False)

	if arg_12_0._puzzleCamp and not arg_12_2:
		if arg_12_0._puzzleCamp == CookGameConst.camp_player:
			var_12_0 = Vector3(-1, 1, 1)
		else
			var_12_0 = Vector3(1, 1, 1)

	findTF(arg_12_0._tf, "mask").localScale = var_12_0

	arg_12_0.animator.SetTrigger("trigger")

	if arg_12_2:
		arg_12_0.updateWanted()

		arg_12_0.freshWanted = True
		arg_12_0.wantedCakeTime = 3

def var_0_0.readyServe(arg_13_0, arg_13_1, arg_13_2):
	if arg_13_0.serveCallback:
		arg_13_0.serveCallback(False)

	arg_13_0.serveData = arg_13_1
	arg_13_0.readyServeTime = 4
	arg_13_0.serveCallback = arg_13_2

	if arg_13_0.serveData.battleData.cake_allow and arg_13_0.wantedCake != arg_13_0.serveData.parameter.cakeId:
		if not arg_13_0._puzzleTime:
			setActive(arg_13_0.smokeTf, False)
			setActive(arg_13_0.smokeTf, True)

			arg_13_0.wantedCake = arg_13_0.serveData.parameter.cakeId

			arg_13_0.showCake(arg_13_0.wantedCake)
		elif arg_13_0._puzzleCamp != arg_13_0.serveData.parameter.camp and arg_13_0.serveData.parameter.weight > arg_13_0._puzzleWeight:
			setActive(arg_13_0.smokeTf, False)
			setActive(arg_13_0.smokeTf, True)

			arg_13_0.wantedCake = arg_13_0.serveData.parameter.cakeId

			arg_13_0.showCake(arg_13_0.wantedCake)

def var_0_0.setWantedImg(arg_14_0):
	return

def var_0_0.serve(arg_15_0):
	if not arg_15_0.serveData:
		return

	if (not arg_15_0.wantedCake or arg_15_0.inTrigger) and arg_15_0.serveCallback:
		arg_15_0.serveCallback(False)

	local var_15_0 = arg_15_0.serveData.parameter.cakeId
	local var_15_1 = arg_15_0.serveData.battleData.ac_able
	local var_15_2 = arg_15_0.serveData.judgeData.acPos
	local var_15_3 = arg_15_0.serveData.battleData.id
	local var_15_4 = arg_15_0.serveData.parameter.right_index
	local var_15_5 = arg_15_0.serveData.parameter.right_flag
	local var_15_6 = arg_15_0.serveData.parameter.rate
	local var_15_7 = arg_15_0.serveData.parameter.weight

	if not var_15_0:
		print("cakeId 不能为None")

		return

	local var_15_8 = var_15_1 and True or False
	local var_15_9 = False

	if var_15_8:
		local var_15_10 = arg_15_0._tf.parent

		if var_15_2.y > arg_15_0._tf.anchoredPosition.y:
			var_15_9 = True

	local var_15_11 = 1

	if arg_15_0._puzzleCamp and arg_15_0.serveData.parameter.camp == arg_15_0._puzzleCamp:
		var_15_11 = 2
	elif arg_15_0._puzzleCamp and arg_15_0.serveData.parameter.camp != arg_15_0._puzzleCamp:
		var_15_11 = 0

	if arg_15_0.serveData.parameter.puzzle:
		arg_15_0.setPuzzle(arg_15_0.serveData.parameter.camp, arg_15_0.serveData.battleData.weight)

	local var_15_12 = arg_15_0._puzzleWeight or 0

	arg_15_0.trigger(var_15_0, var_15_5, var_15_8, var_15_9)
	arg_15_0._event.emit(CookGameView.SERVE_EVENT, {
		serveData = arg_15_0.serveData,
		pos = arg_15_0._tf.position,
		right = var_15_5,
		rate = var_15_11,
		weight = var_15_12
	})

	arg_15_0.serveData = None
	arg_15_0.serveCallback = None
	arg_15_0.readyServeTime = None

def var_0_0.setPuzzle(arg_16_0, arg_16_1, arg_16_2):
	arg_16_0._puzzleCamp = arg_16_1
	arg_16_0._puzzleWeight = arg_16_2
	arg_16_0._puzzleTime = CookGameConst.puzzle_time

	arg_16_0.showCard(True)

def var_0_0.showCard(arg_17_0, arg_17_1):
	setActive(findTF(arg_17_0.wantedTf, "Card"), arg_17_1)
	arg_17_0.showCake(None)

def var_0_0.isInServe(arg_18_0):
	return arg_18_0.serveData

def var_0_0.isInTrigger(arg_19_0):
	return arg_19_0.inTrigger

def var_0_0.getPuzzleCamp(arg_20_0):
	return arg_20_0._puzzleCamp

def var_0_0.getWantedCake(arg_21_0):
	return arg_21_0.wantedCake

def var_0_0.updateWanted(arg_22_0, arg_22_1):
	if arg_22_0.wantedCake != arg_22_1 and arg_22_1:
		arg_22_0.showCake(arg_22_1)

	if arg_22_1 and arg_22_1 > 0:
		setActive(arg_22_0.wantedTf, True)

		arg_22_0.wantedCake = arg_22_1
		arg_22_0.wantedCakeTime = None
	else
		setActive(arg_22_0.wantedTf, False)

def var_0_0.showCake(arg_23_0, arg_23_1):
	arg_23_1 = arg_23_1 or arg_23_0.wantedCake

	for iter_23_0 = 1, arg_23_0._gameData.cake_num:
		setActive(findTF(arg_23_0.wantedTf, "cake_" .. iter_23_0), not arg_23_0._puzzleTime and iter_23_0 == arg_23_1)

def var_0_0.setFrontContainer(arg_24_0, arg_24_1):
	arg_24_0._frontTf = arg_24_1

	if arg_24_0._frontTf:
		SetParent(arg_24_0.wantedTf, arg_24_0._frontTf, True)

def var_0_0.getPos(arg_25_0):
	return arg_25_0._tf.anchoredPosition()

def var_0_0.getLeftTf(arg_26_0):
	return findTF(arg_26_0._tf, "leftPos")

def var_0_0.getRightTf(arg_27_0):
	return findTF(arg_27_0._tf, "rightPos")

def var_0_0.select(arg_28_0, arg_28_1):
	setActive(findTF(arg_28_0._tf, "select"), arg_28_1)

def var_0_0.setClickCallback(arg_29_0, arg_29_1):
	arg_29_0.clickCallback = arg_29_1

def var_0_0.getAcTargetTf(arg_30_0):
	return findTF(arg_30_0._tf, "acTarget")

def var_0_0.getAnimData(arg_31_0, arg_31_1):
	for iter_31_0 = 1, #arg_31_0._judgeDatas:
		local var_31_0 = arg_31_0._judgeDatas[iter_31_0]

		if var_31_0.data.cake_id == arg_31_1:
			return var_31_0

	return None

return var_0_0
