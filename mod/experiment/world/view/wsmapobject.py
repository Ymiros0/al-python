local var_0_0 = class("WSMapObject", import("...BaseEntity"))

var_0_0.Fields = {
	modelType = "number",
	modelAction = "string",
	modelResPath = "string",
	modelParent = "userdata",
	modelAngles = "table",
	modelActionTimer = "table",
	modelScale = "table",
	model = "userdata",
	modelComps = "table",
	modelResAsync = "boolean",
	modelResName = "string"
}

def var_0_0.GetModelAngles(arg_1_0):
	return arg_1_0.modelAngles and arg_1_0.modelAngles.Clone() or Vector3.zero

def var_0_0.UpdateModelAngles(arg_2_0, arg_2_1):
	if arg_2_0.modelAngles != arg_2_1:
		arg_2_0.modelAngles = arg_2_1

		arg_2_0.FlushModelAngles()

def var_0_0.FlushModelAngles(arg_3_0):
	if arg_3_0.model and arg_3_0.modelAngles:
		arg_3_0.model.localEulerAngles = arg_3_0.modelAngles

def var_0_0.GetModelScale(arg_4_0):
	return arg_4_0.modelScale and arg_4_0.modelScale.Clone() or Vector3.one

def var_0_0.UpdateModelScale(arg_5_0, arg_5_1):
	if arg_5_0.modelScale != arg_5_1:
		arg_5_0.modelScale = arg_5_1

		arg_5_0.FlushModelScale()

def var_0_0.GetModelAction(arg_6_0):
	return arg_6_0.modelAction

def var_0_0.FlushModelScale(arg_7_0):
	if arg_7_0.model and arg_7_0.modelScale:
		arg_7_0.model.localScale = arg_7_0.modelScale

def var_0_0.UpdateModelAction(arg_8_0, arg_8_1):
	if arg_8_0.modelAction != arg_8_1:
		arg_8_0.modelAction = arg_8_1

		arg_8_0.FlushModelAction()

def var_0_0.FlushModelAction(arg_9_0):
	if arg_9_0.model and arg_9_0.modelAction:
		if arg_9_0.modelType == WorldConst.ModelSpine:
			local var_9_0 = arg_9_0.modelComps and arg_9_0.modelComps[1]

			if var_9_0:
				var_9_0.SetAction(arg_9_0.modelAction, 0)
		elif arg_9_0.modelType == WorldConst.ModelPrefab:
			local var_9_1 = arg_9_0.modelComps and arg_9_0.modelComps[1]

			if var_9_1:
				local var_9_2 = Animator.StringToHash(arg_9_0.modelAction)

				if var_9_1.HasState(0, var_9_2):
					var_9_1.Play(var_9_2)

def var_0_0.PlayModelAction(arg_10_0, arg_10_1, arg_10_2, arg_10_3):
	assert(arg_10_1)

	local var_10_0 = {}

	if arg_10_0.model:
		if arg_10_0.modelType == WorldConst.ModelSpine:
			local var_10_1 = arg_10_0.modelComps and arg_10_0.modelComps[1]

			if var_10_1 and var_10_1.transform.gameObject.activeInHierarchy:
				table.insert(var_10_0, function(arg_11_0)
					var_10_1.SetAction(arg_10_1, 0)

					if arg_10_2:
						arg_10_0.NewActionTimer(arg_10_2, arg_11_0)
					else
						var_10_1.SetActionCallBack(function(arg_12_0)
							if arg_12_0 == "finish":
								var_10_1.SetActionCallBack(None)
								arg_11_0()))
		elif arg_10_0.modelType == WorldConst.ModelPrefab:
			local var_10_2 = arg_10_0.modelComps and arg_10_0.modelComps[1]

			if var_10_2 and var_10_2.transform.gameObject.activeInHierarchy:
				local var_10_3 = Animator.StringToHash(arg_10_1)

				if var_10_2.HasState(0, var_10_3):
					table.insert(var_10_0, function(arg_13_0)
						var_10_2.Play(var_10_3)

						if arg_10_2:
							arg_10_0.NewActionTimer(arg_10_2, arg_13_0)
						else
							local var_13_0 = arg_10_0.modelComps[2]

							var_13_0.SetEndEvent(function()
								var_13_0.SetEndEvent(None)
								arg_13_0()))

	seriesAsync(var_10_0, arg_10_3)

def var_0_0.LoadModel(arg_15_0, arg_15_1, arg_15_2, arg_15_3, arg_15_4, arg_15_5):
	if arg_15_0.modelType != arg_15_1 or arg_15_0.modelResPath != arg_15_2 or arg_15_0.modelResName != arg_15_3:
		arg_15_0.UnloadModel()

		arg_15_0.model = createNewGameObject("model")
		arg_15_0.modelType = arg_15_1
		arg_15_0.modelResPath = arg_15_2
		arg_15_0.modelResName = arg_15_3
		arg_15_0.modelResAsync = defaultValue(arg_15_4, True)

		local var_15_0 = {}

		if arg_15_0.modelType == WorldConst.ModelSpine:
			arg_15_0.modelAction = arg_15_0.modelAction or WorldConst.ActionIdle

			table.insert(var_15_0, function(arg_16_0)
				arg_15_0.LoadSpine(arg_16_0))
		elif arg_15_0.modelType == WorldConst.ModelPrefab:
			arg_15_0.modelAction = arg_15_0.modelAction or "idle"

			table.insert(var_15_0, function(arg_17_0)
				arg_15_0.LoadPrefab(arg_17_0))
		else
			assert("invalid model type. " .. arg_15_1)

		seriesAsync(var_15_0, function()
			if arg_15_0.modelScale == None:
				arg_15_0.modelScale = arg_15_0.model.localScale
			else
				arg_15_0.FlushModelScale()

			if arg_15_0.modelAngles == None:
				arg_15_0.modelAngles = arg_15_0.model.localEulerAngles
			else
				arg_15_0.FlushModelAngles()

			arg_15_0.FlushModelAction()

			if arg_15_5:
				arg_15_5())

def var_0_0.UnloadModel(arg_19_0):
	arg_19_0.DisposeActionTimer()

	if arg_19_0.model:
		if arg_19_0.model.childCount > 0:
			if arg_19_0.modelType == WorldConst.ModelSpine:
				arg_19_0.UnloadSpine()
			elif arg_19_0.modelType == WorldConst.ModelPrefab:
				arg_19_0.UnloadPrefab()

		Destroy(arg_19_0.model)

	arg_19_0.model = None
	arg_19_0.modelComps = None
	arg_19_0.modelType = None
	arg_19_0.modelResPath = None
	arg_19_0.modelResName = None
	arg_19_0.modelResAsync = None

def var_0_0.LoadSpine(arg_20_0, arg_20_1):
	local var_20_0 = arg_20_0.modelResPath
	local var_20_1 = arg_20_0.modelResAsync

	PoolMgr.GetInstance().GetSpineChar(var_20_0, var_20_1, function(arg_21_0)
		if arg_20_0.modelType != WorldConst.ModelSpine or arg_20_0.modelResPath != var_20_0:
			PoolMgr.GetInstance().ReturnSpineChar(var_20_0, arg_21_0)

			return

		local var_21_0 = arg_21_0.transform

		var_21_0.GetComponent("SkeletonGraphic").raycastTarget = False
		var_21_0.anchoredPosition3D = Vector3.zero
		var_21_0.localScale = Vector3.one

		pg.ViewUtils.SetLayer(var_21_0, Layer.UI)
		var_21_0.SetParent(arg_20_0.model, False)

		arg_20_0.modelComps = {
			var_21_0.GetComponent("SpineAnimUI")
		}

		arg_20_1())

def var_0_0.LoadPrefab(arg_22_0, arg_22_1):
	local var_22_0 = arg_22_0.modelResPath
	local var_22_1 = arg_22_0.modelResName
	local var_22_2 = arg_22_0.modelResAsync

	PoolMgr.GetInstance().GetPrefab(var_22_0, var_22_1, var_22_2, function(arg_23_0)
		if arg_22_0.modelType != WorldConst.ModelPrefab or arg_22_0.modelResPath != var_22_0 or arg_22_0.modelResName != var_22_1:
			PoolMgr.GetInstance().ReturnPrefab(var_22_0, var_22_1, arg_23_0, True)

			return

		local var_23_0 = arg_23_0.GetComponentsInChildren(typeof(Image))

		for iter_23_0 = 0, var_23_0.Length - 1:
			var_23_0[iter_23_0].raycastTarget = False

		arg_23_0.transform.SetParent(arg_22_0.model, False)

		arg_22_0.modelComps = {}

		local var_23_1 = arg_23_0.GetComponentInChildren(typeof(Animator))

		if var_23_1:
			local var_23_2 = var_23_1.GetComponent("DftAniEvent")

			arg_22_0.modelComps = {
				var_23_1,
				var_23_2
			}

		arg_22_1())

def var_0_0.UnloadSpine(arg_24_0):
	arg_24_0.modelComps[1].SetActionCallBack(None)
	PoolMgr.GetInstance().ReturnSpineChar(arg_24_0.modelResPath, arg_24_0.model.GetChild(0).gameObject)

def var_0_0.UnloadPrefab(arg_25_0):
	local var_25_0 = arg_25_0.modelComps[2]

	if var_25_0:
		var_25_0.SetEndEvent(None)

	PoolMgr.GetInstance().ReturnPrefab(arg_25_0.modelResPath, arg_25_0.modelResName, arg_25_0.model.GetChild(0).gameObject, True)

def var_0_0.NewActionTimer(arg_26_0, arg_26_1, arg_26_2):
	arg_26_0.DisposeActionTimer()

	arg_26_0.modelActionTimer = Timer.New(arg_26_2, arg_26_1, 1)

	arg_26_0.modelActionTimer.Start()

def var_0_0.DisposeActionTimer(arg_27_0):
	if arg_27_0.modelActionTimer:
		arg_27_0.modelActionTimer.Stop()

		arg_27_0.modelActionTimer = None

return var_0_0
