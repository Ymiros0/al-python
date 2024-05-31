local var_0_0 = class("ShopPaintingView")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._painting = arg_1_1
	arg_1_0._paintingInitPos = arg_1_0._painting.anchoredPosition
	arg_1_0._paintingOffsetMin = Vector2(arg_1_0._painting.offsetMin.x, arg_1_0._painting.offsetMin.y)
	arg_1_0._paintingOffsetMax = Vector2(arg_1_0._painting.offsetMax.x, arg_1_0._painting.offsetMax.y)
	arg_1_0.touch = arg_1_0._painting.Find("paint_touch")
	arg_1_0.chat = arg_1_2
	arg_1_0.chatText = arg_1_0.chat.Find("Text")
	arg_1_0.name = None
	arg_1_0.chatting = False
	arg_1_0.chatTrOffset = Vector3(118, -276, 0)

def var_0_0.InitChatPosition(arg_2_0):
	local var_2_0 = arg_2_0._painting.localPosition + arg_2_0.chatTrOffset
	local var_2_1 = arg_2_0._painting.parent.TransformPoint(var_2_0)
	local var_2_2 = arg_2_0.chat.parent.InverseTransformPoint(var_2_1)

	arg_2_0.chat.localPosition = Vector3(var_2_2.x, var_2_2.y, 0)

def var_0_0.Init(arg_3_0, arg_3_1, arg_3_2, arg_3_3, arg_3_4):
	if not arg_3_0.isInitChatPosition:
		arg_3_0.isInitChatPosition = True

		arg_3_0.InitChatPosition()

	arg_3_0.UnLoad()

	arg_3_0.name = arg_3_1

	if arg_3_2 and arg_3_0.secretaryTf:
		arg_3_0._painting.anchoredPosition = arg_3_0.secretaryTf.anchoredPosition
		arg_3_0._painting.offsetMin = arg_3_0.secretaryTf.offsetMin
		arg_3_0._painting.offsetMax = arg_3_0.secretaryTf.offsetMax
	else
		arg_3_0._painting.anchoredPosition = arg_3_0._paintingInitPos
		arg_3_0._painting.offsetMin = arg_3_0._paintingOffsetMin
		arg_3_0._painting.offsetMax = arg_3_0._paintingOffsetMax

	arg_3_0.Load(arg_3_3, arg_3_4)

def var_0_0.Load(arg_4_0, arg_4_1, arg_4_2):
	local var_4_0

	if arg_4_0.name == "mingshi_live2d":
		var_4_0 = ShopMingShiPainting.New(arg_4_0._painting)
	else
		var_4_0 = ShopMeshPainting.New(arg_4_0._painting)

	arg_4_0.iShopPainting = var_4_0

	var_4_0.Load(arg_4_0.name, arg_4_1, arg_4_2)

def var_0_0.setSecretaryPos(arg_5_0, arg_5_1):
	if arg_5_1:
		arg_5_0.secretaryTf = arg_5_1

def var_0_0.Chat(arg_6_0, arg_6_1, arg_6_2, arg_6_3, arg_6_4):
	local var_6_0 = 1

	if type(arg_6_1) == "table":
		var_6_0 = math.random(1, #arg_6_1)
		arg_6_1 = arg_6_1[var_6_0]

	if type(arg_6_2) == "table":
		arg_6_2 = arg_6_2[var_6_0]

	if type(arg_6_3) == "table":
		arg_6_3 = arg_6_3[var_6_0]

	local function var_6_1()
		if arg_6_1:
			arg_6_0.ShowShipWord(arg_6_1)

		if arg_6_3 and arg_6_0.iShopPainting:
			arg_6_0.iShopPainting.Action(arg_6_3)

	if not arg_6_0.chatting or arg_6_4:
		arg_6_0.StopChat()

		if arg_6_2:
			arg_6_0.PlayCV(arg_6_2, function(arg_8_0)
				if arg_8_0:
					arg_6_0._cueInfo = arg_8_0.cueInfo

				var_6_1())
		else
			var_6_1()

def var_0_0.ShowShipWord(arg_9_0, arg_9_1):
	arg_9_0.chatting = True

	if LeanTween.isTweening(go(arg_9_0.chat)):
		LeanTween.cancel(go(arg_9_0.chat))

	local var_9_0 = 0.3
	local var_9_1 = 3

	if arg_9_0._cueInfo:
		local var_9_2 = long2int(arg_9_0._cueInfo.length) / 1000

		if var_9_1 < var_9_2:
			var_9_1 = var_9_2

	setActive(arg_9_0.chat, True)
	setText(arg_9_0.chatText, arg_9_1)
	LeanTween.scale(arg_9_0.chat.gameObject, Vector3.New(1, 1, 1), var_9_0).setFrom(Vector3.New(0, 0, 0)).setEase(LeanTweenType.easeOutBack).setOnComplete(System.Action(function()
		if IsNil(arg_9_0.chat):
			return

		LeanTween.scale(arg_9_0.chat.gameObject, Vector3.New(0, 0, 1), var_9_0).setFrom(Vector3.New(1, 1, 1)).setEase(LeanTweenType.easeInBack).setDelay(var_9_1).setOnComplete(System.Action(function()
			if IsNil(arg_9_0.chat):
				return

			arg_9_0.StopChat()))))

def var_0_0.StopChat(arg_12_0):
	arg_12_0.chatting = None

	if LeanTween.isTweening(go(arg_12_0.chat)):
		LeanTween.cancel(go(arg_12_0.chat))

	setActive(arg_12_0.chat, False)
	arg_12_0.StopCV()

local function var_0_1(arg_13_0, arg_13_1)
	local var_13_0
	local var_13_1

	if string.find(arg_13_1, "/"):
		local var_13_2 = string.split(arg_13_1, "/")

		var_13_0 = var_13_2[1]
		var_13_1 = var_13_2[2]
	elif arg_13_0.name == "mingshi_live2d":
		var_13_0 = "cv-chargeShop"
		var_13_1 = arg_13_1
	elif string.find(arg_13_1, "ryza_shop"):
		var_13_0 = "cv-1090002"
		var_13_1 = arg_13_1
	else
		var_13_0 = "cv-shop"
		var_13_1 = arg_13_1

	return var_13_0, var_13_1

def var_0_0.PlayCV(arg_14_0, arg_14_1, arg_14_2):
	local var_14_0, var_14_1 = var_0_1(arg_14_0, arg_14_1)

	arg_14_0.StopCV()
	pg.CriMgr.GetInstance().PlayCV_V3(var_14_0, var_14_1, arg_14_2)

	arg_14_0._currentVoice = var_14_0

def var_0_0.StopCV(arg_15_0):
	if arg_15_0._currentVoice:
		pg.CriMgr.GetInstance().UnloadSoundEffect_V3(arg_15_0._currentVoice)

	arg_15_0._currentVoice = None
	arg_15_0._cueInfo = None

def var_0_0.UnLoad(arg_16_0):
	if arg_16_0.iShopPainting and arg_16_0.name:
		arg_16_0.iShopPainting.UnLoad(arg_16_0.name)

		arg_16_0.name = None
		arg_16_0.iShopPainting = None

def var_0_0.Dispose(arg_17_0):
	arg_17_0.UnLoad()
	arg_17_0.StopCV()

return var_0_0
