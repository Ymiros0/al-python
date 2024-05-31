pg = pg or {}

local var_0_0 = pg

var_0_0.TipsMgr = singletonClass("TipsMgr")

local var_0_1 = var_0_0.TipsMgr

def var_0_1.Ctor(arg_1_0):
	arg_1_0._go = None

def var_0_1.Init(arg_2_0, arg_2_1):
	print("initializing tip manager...")

	arg_2_0._count = 0
	arg_2_0._tipTable = {}

	PoolMgr.GetInstance().GetUI("TipPanel", True, function(arg_3_0)
		arg_2_0._go = arg_3_0

		arg_2_0._go.SetActive(False)

		local var_3_0 = GameObject.Find("Overlay/UIOverlay")

		arg_2_0._go.transform.SetParent(var_3_0.transform, False)

		arg_2_0._tips = arg_2_0._go.transform.Find("toolTip")
		arg_2_0._picTips = arg_2_0._go.transform.Find("toolPicTip")
		arg_2_0._grid = arg_2_0._go.transform.Find("Grid")

		arg_2_1())

def var_0_1.ShowTips(arg_4_0, arg_4_1, arg_4_2, arg_4_3):
	var_0_0.CriMgr.GetInstance().PlaySoundEffect_V3(arg_4_3 or SFX_UI_TIP)
	arg_4_0._go.transform.SetAsLastSibling()
	SetActive(arg_4_0._go, True)

	arg_4_0._count = arg_4_0._count + 1

	local var_4_0 = cloneTplTo(arg_4_0._tips, arg_4_0._grid)
	local var_4_1 = arg_4_2 or "white"

	setText(var_4_0.transform.Find("Text"), "<color=" .. var_4_1 .. ">" .. arg_4_1 .. "</color>")

	var_4_0.transform.localScale = Vector3(0, 0.1, 1)

	LeanTween.scale(var_4_0, Vector3(1.8, 0.1, 1), 0.1).setUseEstimatedTime(True)
	LeanTween.scale(var_4_0, Vector3(1.1, 1.1, 1), 0.1).setDelay(0.1).setUseEstimatedTime(True)

	local function var_4_2(arg_5_0, arg_5_1)
		local var_5_0 = GetOrAddComponent(arg_5_0, "CanvasGroup")

		Timer.New(function()
			if IsNil(arg_5_0):
				return

			LeanTween.scale(arg_5_0, Vector3(0.1, 1.5, 1), 0.1).setUseEstimatedTime(True).setOnComplete(System.Action(function()
				LeanTween.scale(arg_5_0, Vector3.zero, 0.1).setUseEstimatedTime(True).setOnComplete(System.Action(function()
					Destroy(arg_5_0)

					for iter_8_0, iter_8_1 in pairs(arg_4_0._tipTable):
						if iter_8_1 == arg_5_0:
							table.remove(arg_4_0._tipTable, iter_8_0)

					arg_4_0._count = arg_4_0._count - 1

					if arg_4_0._count == 0:
						SetActive(arg_4_0._go, False))))), 3).Start()

	if arg_4_0._count <= 3:
		arg_4_0._tipTable[arg_4_0._count] = var_4_0

		var_4_2(var_4_0, arg_4_0._count)
	else
		Destroy(arg_4_0._tipTable[1])
		table.remove(arg_4_0._tipTable, 1)

		arg_4_0._count = 3
		arg_4_0._tipTable[3] = var_4_0

		var_4_2(var_4_0, arg_4_0._count)

def var_0_1.ShowPicTips(arg_9_0, arg_9_1, arg_9_2, arg_9_3, arg_9_4):
	var_0_0.CriMgr.GetInstance().PlaySoundEffect_V3(arg_9_4 or SFX_UI_TIP)
	arg_9_0._go.transform.SetAsLastSibling()
	SetActive(arg_9_0._go, True)

	arg_9_0._count = arg_9_0._count + 1

	local var_9_0 = cloneTplTo(arg_9_0._picTips, arg_9_0._grid)
	local var_9_1 = arg_9_3 or "white"

	setText(var_9_0.transform.Find("Text"), "<color=" .. var_9_1 .. ">\"" .. arg_9_1 .. "\" x" .. arg_9_2 .. "</color>")

	local function var_9_2(arg_10_0)
		local var_10_0 = GetOrAddComponent(arg_10_0, "CanvasGroup")

		var_10_0.alpha = 1

		local var_10_1 = LeanTween.alphaCanvas(var_10_0, 0, 5).setUseEstimatedTime(True).setOnComplete(System.Action(function()
			Destroy(arg_10_0)

			for iter_11_0, iter_11_1 in pairs(arg_9_0._tipTable):
				if iter_11_1 == arg_10_0:
					table.remove(arg_9_0._tipTable, iter_11_0)

			arg_9_0._count = arg_9_0._count - 1

			if arg_9_0._count == 0:
				SetActive(arg_9_0._go, False)))

	if arg_9_0._count <= 3:
		arg_9_0._tipTable[arg_9_0._count] = var_9_0

		var_9_2(var_9_0)
	else
		Destroy(arg_9_0._tipTable[1])
		table.remove(arg_9_0._tipTable, 1)

		arg_9_0._count = 3
		arg_9_0._tipTable[3] = var_9_0

		var_9_2(var_9_0)
