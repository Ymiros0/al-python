local var_0_0 = class("GuideShowSignPlayer", import(".GuidePlayer"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.signTrs = {}

def var_0_0.OnExecution(arg_2_0, arg_2_1, arg_2_2):
	seriesAsync({
		function(arg_3_0)
			arg_2_0.loadSigns(arg_2_1, arg_3_0),
		function(arg_4_0)
			arg_2_0.InitSign(arg_2_1, arg_4_0)
	}, arg_2_2)

def var_0_0.loadSigns(arg_5_0, arg_5_1, arg_5_2):
	local var_5_0 = arg_5_1.GetSignList()
	local var_5_1 = {}

	for iter_5_0, iter_5_1 in ipairs(var_5_0):
		table.insert(var_5_1, function(arg_6_0)
			arg_5_0.LoadSignRes(iter_5_1, function(arg_7_0)
				table.insert(arg_5_0.signTrs, arg_7_0)
				arg_6_0()))

	parallelAsync(var_5_1, arg_5_2)

def var_0_0.LoadSignRes(arg_8_0, arg_8_1, arg_8_2):
	arg_8_0.uiLoader.Load(arg_8_1.signName, function(arg_9_0)
		if arg_8_1.atlasName and arg_8_1.fileName:
			local var_9_0 = LoadSprite(arg_8_1.atlasName, arg_8_1.fileName)

			setImageSprite(findTF(arg_9_0, "shadow"), var_9_0, True)

		arg_9_0.localPosition = arg_8_1.pos
		arg_9_0.eulerAngles = Vector3(0, 0, 0)
		arg_9_0.localScale = Vector3.one

		setActive(arg_9_0, True)

		if arg_8_2:
			arg_8_2(arg_9_0))

def var_0_0.InitSign(arg_10_0, arg_10_1, arg_10_2):
	local var_10_0 = arg_10_1.GetSignType()

	if var_10_0 == GuideShowSignStep.SIGN_TYPE_2:
		arg_10_0.UpdateSign2(arg_10_1, arg_10_2)
	elif var_10_0 == GuideShowSignStep.SIGN_TYPE_3:
		arg_10_0.UpdateSign3(arg_10_1, arg_10_2)
	else
		arg_10_0.UpdateCommonSign(arg_10_1, arg_10_2)

def var_0_0.UpdateSign2(arg_11_0, arg_11_1, arg_11_2):
	local var_11_0 = arg_11_0.signTrs[1]
	local var_11_1 = findTF(var_11_0, "btn")

	if arg_11_1.ShouldClick():
		setActive(var_11_0, False)

		local var_11_2 = arg_11_1.GetClickData()

		arg_11_0.SearchUI(var_11_2, function(arg_12_0)
			if IsNil(arg_12_0):
				pg.NewGuideMgr.GetInstance().Stop()

				return

			local var_12_0 = Vector3(arg_12_0.sizeDelta.x * (arg_12_0.pivot.x - 0.5), arg_12_0.sizeDelta.y * (arg_12_0.pivot.y - 0.5), 0)
			local var_12_1 = var_11_0.parent.InverseTransformPoint(arg_12_0.position)

			var_11_0.localPosition = var_12_1 - var_12_0
			var_11_1.sizeDelta = arg_12_0.sizeDelta + var_11_2.sizeDeltaPlus

			setActive(var_11_0, True))
	elif arg_11_1.ExistClickArea():
		var_11_1.sizeDelta = arg_11_1.GetClickArea()

	local var_11_3 = GetOrAddComponent(var_11_1, typeof(UILongPressTrigger))

	var_11_3.onLongPressed.RemoveAllListeners()
	var_11_3.onReleased.RemoveAllListeners()

	if arg_11_1.GetTriggerType() == 1:
		var_11_3.onLongPressed.AddListener(arg_11_2)
	else
		var_11_3.onReleased.AddListener(arg_11_2)

def var_0_0.UpdateSign3(arg_13_0, arg_13_1, arg_13_2):
	arg_13_0.signTrs[1].sizeDelta = arg_13_1.GetClickArea()

	arg_13_2()

def var_0_0.UpdateCommonSign(arg_14_0, arg_14_1, arg_14_2):
	local var_14_0 = arg_14_1.GetExitDelay()

	if var_14_0 <= 0:
		arg_14_2()
	else
		Timer.New(arg_14_2, var_14_0, 1).Start()

def var_0_0.OnClear(arg_15_0):
	arg_15_0.signTrs = {}

return var_0_0
