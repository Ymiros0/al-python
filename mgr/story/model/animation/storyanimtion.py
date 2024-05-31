local var_0_0 = class("StoryAnimtion")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.tweens = {}
	arg_1_0.timers = {}
	arg_1_0.timeScale = 1

def var_0_0.SetTimeScale(arg_2_0, arg_2_1):
	arg_2_0.timeScale = arg_2_1

def var_0_0.moveLocal(arg_3_0, arg_3_1, arg_3_2, arg_3_3, arg_3_4, arg_3_5, arg_3_6, arg_3_7):
	local function var_3_0()
		local var_4_0 = LeanTween.moveLocal(arg_3_1.gameObject, arg_3_3, arg_3_4 * arg_3_0.timeScale)

		var_4_0.setFrom(arg_3_2)

		if arg_3_7:
			var_4_0.setOnComplete(System.Action(arg_3_7))

		if arg_3_6:
			var_4_0.setEase(arg_3_6)

		table.insert(arg_3_0.tweens, arg_3_1)

	arg_3_0.DelayCall(arg_3_5, var_3_0)

def var_0_0.moveLocalPath(arg_5_0, arg_5_1, arg_5_2, arg_5_3, arg_5_4, arg_5_5, arg_5_6):
	if #arg_5_2 <= 3:
		local var_5_0 = arg_5_2[1]
		local var_5_1 = arg_5_2[#arg_5_2]

		arg_5_0.moveLocal(arg_5_1, var_5_0, var_5_1, arg_5_3, arg_5_4, arg_5_5, arg_5_6)

		return

	local var_5_2 = System.Array.CreateInstance(typeof(UnityEngine.Vector3), #arg_5_2)

	for iter_5_0, iter_5_1 in ipairs(arg_5_2):
		var_5_2[iter_5_0 - 1] = iter_5_1

	local function var_5_3()
		local var_6_0 = LeanTween.moveLocal(arg_5_1.gameObject, var_5_2, arg_5_3 * arg_5_0.timeScale)

		if arg_5_6:
			var_6_0.setOnComplete(System.Action(arg_5_6))

		if arg_5_5:
			var_6_0.setEase(arg_5_5)

		table.insert(arg_5_0.tweens, arg_5_1)

	arg_5_0.DelayCall(arg_5_4, var_5_3)

def var_0_0.TweenMove(arg_7_0, arg_7_1, arg_7_2, arg_7_3, arg_7_4, arg_7_5, arg_7_6):
	local function var_7_0()
		local var_8_0 = LeanTween.move(rtf(arg_7_1), arg_7_2, arg_7_3 * arg_7_0.timeScale)

		if arg_7_4 > 1:
			var_8_0.setLoopPingPong(arg_7_4)

		if arg_7_6:
			var_8_0.setOnComplete(System.Action(arg_7_6))

		table.insert(arg_7_0.tweens, arg_7_1)

	arg_7_0.DelayCall(arg_7_5, var_7_0)

def var_0_0.TweenScale(arg_9_0, arg_9_1, arg_9_2, arg_9_3, arg_9_4, arg_9_5):
	local function var_9_0()
		local var_10_0 = LeanTween.scale(rtf(arg_9_1), arg_9_2, arg_9_3 * arg_9_0.timeScale)

		if arg_9_5:
			var_10_0.setOnComplete(System.Action(arg_9_5))

		table.insert(arg_9_0.tweens, arg_9_1)

	arg_9_0.DelayCall(arg_9_4, var_9_0)

def var_0_0.TweenRotate(arg_11_0, arg_11_1, arg_11_2, arg_11_3, arg_11_4, arg_11_5, arg_11_6):
	local function var_11_0()
		local var_12_0 = LeanTween.rotate(rtf(arg_11_1), arg_11_2, arg_11_3 * arg_11_0.timeScale).setLoopPingPong(arg_11_4)

		if arg_11_6:
			var_12_0.setOnComplete(System.Action(arg_11_6))

		table.insert(arg_11_0.tweens, arg_11_1)

	arg_11_0.DelayCall(arg_11_5, var_11_0)

def var_0_0.TweenValueForcanvasGroup(arg_13_0, arg_13_1, arg_13_2, arg_13_3, arg_13_4, arg_13_5, arg_13_6):
	local function var_13_0()
		local var_14_0 = LeanTween.value(go(arg_13_1), arg_13_2, arg_13_3, arg_13_4 * arg_13_0.timeScale).setOnUpdate(System.Action_float(function(arg_15_0)
			arg_13_1.alpha = arg_15_0))

		if arg_13_6:
			var_14_0.setOnComplete(System.Action(arg_13_6))

		table.insert(arg_13_0.tweens, arg_13_1.gameObject.transform)

	arg_13_0.DelayCall(arg_13_5, var_13_0)

def var_0_0.TweenValue(arg_16_0, arg_16_1, arg_16_2, arg_16_3, arg_16_4, arg_16_5, arg_16_6, arg_16_7):
	local function var_16_0()
		local var_17_0 = LeanTween.value(go(arg_16_1), arg_16_2, arg_16_3, arg_16_4 * arg_16_0.timeScale).setOnUpdate(System.Action_float(arg_16_6))

		if arg_16_7:
			var_17_0.setOnComplete(System.Action(function()
				if arg_16_7:
					arg_16_7()))

		table.insert(arg_16_0.tweens, arg_16_1)

	arg_16_0.DelayCall(arg_16_5, var_16_0)

def var_0_0.TweenValueLoop(arg_19_0, arg_19_1, arg_19_2, arg_19_3, arg_19_4, arg_19_5, arg_19_6, arg_19_7):
	local function var_19_0()
		local var_20_0 = LeanTween.value(go(arg_19_1), arg_19_2, arg_19_3, arg_19_4 * arg_19_0.timeScale).setOnUpdate(System.Action_float(arg_19_6)).setLoopClamp()

		if arg_19_7:
			var_20_0.setOnComplete(System.Action(function()
				if arg_19_7:
					arg_19_7()))

		table.insert(arg_19_0.tweens, arg_19_1)

	arg_19_0.DelayCall(arg_19_5, var_19_0)

def var_0_0.TweenTextAlpha(arg_22_0, arg_22_1, arg_22_2, arg_22_3, arg_22_4, arg_22_5):
	local function var_22_0()
		local var_23_0 = LeanTween.textAlpha(arg_22_1, arg_22_2, (arg_22_3 or 1) * arg_22_0.timeScale)

		if arg_22_5:
			var_23_0.setOnComplete(System.Action(arg_22_5))

		table.insert(arg_22_0.tweens, arg_22_1)

	arg_22_0.DelayCall(arg_22_4, var_22_0)

def var_0_0.TweenAlpha(arg_24_0, arg_24_1, arg_24_2, arg_24_3, arg_24_4, arg_24_5, arg_24_6):
	local function var_24_0()
		local var_25_0 = LeanTween.alpha(arg_24_1, arg_24_3, arg_24_4 * arg_24_0.timeScale).setFrom(arg_24_2)

		if arg_24_6:
			var_25_0.setOnComplete(System.Action(arg_24_6))

		table.insert(arg_24_0.tweens, arg_24_1)

	arg_24_0.DelayCall(arg_24_5, var_24_0)

def var_0_0.TweenMovex(arg_26_0, arg_26_1, arg_26_2, arg_26_3, arg_26_4, arg_26_5, arg_26_6, arg_26_7):
	local function var_26_0()
		local var_27_0 = LeanTween.moveX(arg_26_1, arg_26_2, arg_26_4 * arg_26_0.timeScale).setFrom(arg_26_3)

		if arg_26_6:
			var_27_0.setLoopPingPong(arg_26_6)

		if arg_26_7:
			var_27_0.setOnComplete(System.Action(arg_26_7))

		table.insert(arg_26_0.tweens, arg_26_1)

	arg_26_0.DelayCall(arg_26_5, var_26_0)

def var_0_0.TweenMovey(arg_28_0, arg_28_1, arg_28_2, arg_28_3, arg_28_4, arg_28_5, arg_28_6, arg_28_7):
	local function var_28_0()
		local var_29_0 = LeanTween.moveY(arg_28_1, arg_28_2, arg_28_4 * arg_28_0.timeScale).setFrom(arg_28_3)

		if arg_28_6:
			var_29_0.setLoopPingPong(arg_28_6)

		if arg_28_7:
			var_29_0.setOnComplete(System.Action(arg_28_7))

		table.insert(arg_28_0.tweens, arg_28_1)

	arg_28_0.DelayCall(arg_28_5, var_28_0)

def var_0_0.IsTweening(arg_30_0, arg_30_1):
	return LeanTween.isTweening(arg_30_1)

def var_0_0.CancelTween(arg_31_0, arg_31_1):
	if arg_31_0.IsTweening(arg_31_1):
		LeanTween.cancel(arg_31_1)

def var_0_0.DelayCall(arg_32_0, arg_32_1, arg_32_2):
	if not arg_32_1 or arg_32_1 <= 0:
		arg_32_2()

		return

	arg_32_0.timers[arg_32_2] = StoryTimer.New(function()
		arg_32_0.timers[arg_32_2].Stop()

		arg_32_0.timers[arg_32_2] = None

		arg_32_2(), arg_32_1 * arg_32_0.timeScale, 1)

	arg_32_0.timers[arg_32_2].Start()

def var_0_0.UnscaleDelayCall(arg_34_0, arg_34_1, arg_34_2):
	if arg_34_1 <= 0:
		arg_34_2()

		return

	arg_34_0.timers[arg_34_2] = StoryTimer.New(function()
		arg_34_0.timers[arg_34_2].Stop()

		arg_34_0.timers[arg_34_2] = None

		arg_34_2(), arg_34_1, 1)

	arg_34_0.timers[arg_34_2].Start()

def var_0_0.CreateDelayTimer(arg_36_0, arg_36_1, arg_36_2):
	if arg_36_1 == 0:
		arg_36_2()

		return None

	local var_36_0 = StoryTimer.New(arg_36_2, arg_36_1 * arg_36_0.timeScale, 1)

	var_36_0.Start()

	return var_36_0

def var_0_0.PauseAllTween(arg_37_0):
	for iter_37_0, iter_37_1 in ipairs(arg_37_0.tweens):
		if not IsNil(iter_37_1) and arg_37_0.IsTweening(iter_37_1.gameObject):
			LeanTween.pause(iter_37_1.gameObject)

def var_0_0.ResumeAllTween(arg_38_0):
	for iter_38_0, iter_38_1 in ipairs(arg_38_0.tweens):
		if not IsNil(iter_38_1):
			LeanTween.resume(iter_38_1.gameObject)

def var_0_0.PauseAllTimer(arg_39_0):
	for iter_39_0, iter_39_1 in pairs(arg_39_0.timers):
		iter_39_1.Pause()

def var_0_0.ResumeAllTimer(arg_40_0):
	for iter_40_0, iter_40_1 in pairs(arg_40_0.timers):
		iter_40_1.Resume()

def var_0_0.ResumeAllAnimation(arg_41_0):
	arg_41_0.ResumeAllTween()
	arg_41_0.ResumeAllTimer()

def var_0_0.PauseAllAnimation(arg_42_0):
	arg_42_0.PauseAllTween()
	arg_42_0.PauseAllTimer()

def var_0_0.ClearAllTween(arg_43_0):
	for iter_43_0, iter_43_1 in ipairs(arg_43_0.tweens):
		if not IsNil(iter_43_1) and arg_43_0.IsTweening(iter_43_1.gameObject):
			LeanTween.cancel(iter_43_1.gameObject)

	arg_43_0.tweens = {}

def var_0_0.ClearAllTimers(arg_44_0):
	for iter_44_0, iter_44_1 in pairs(arg_44_0.timers):
		iter_44_1.Stop()

	arg_44_0.timers = {}

def var_0_0.ClearAnimation(arg_45_0):
	arg_45_0.ClearAllTween()
	arg_45_0.ClearAllTimers()

return var_0_0
