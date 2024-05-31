local var_0_0 = class("SkinAtlasLive2dView")
local var_0_1

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	pg.DelegateInfo.New(arg_1_0)

	arg_1_0.ship = arg_1_1
	arg_1_0.paintingTr = arg_1_2.parent
	arg_1_0.live2dContainer = arg_1_2
	arg_1_0.canClick = False
	arg_1_0.inited = False
	var_0_1 = pg.AssistantInfo

	arg_1_0.Init(arg_1_3)

def var_0_0.Init(arg_2_0, arg_2_1):
	local var_2_0 = arg_2_0.ship

	setActive(arg_2_0.live2dContainer, True)

	local var_2_1 = Live2D.GenerateData({
		ship = var_2_0,
		scale = Vector3(52, 52, 52),
		position = Vector3(0, 0, -100),
		parent = arg_2_0.live2dContainer
	})

	arg_2_0.live2dChar = Live2D.New(var_2_1, function(arg_3_0)
		arg_2_0.inited = True

		if arg_2_1:
			arg_2_1())

def var_0_0.OpenClick(arg_4_0):
	onButton(arg_4_0, arg_4_0.paintingTr, function()
		if not arg_4_0.inited:
			return

		arg_4_0.OnClick())

def var_0_0.CloseClick(arg_6_0):
	removeOnButton(arg_6_0.paintingTr)

def var_0_0.OnClick(arg_7_0):
	local var_7_0

	if arg_7_0.live2dChar and arg_7_0.live2dChar.state == Live2D.STATE_INITED:
		if not Input.mousePosition:
			return

		local var_7_1 = arg_7_0.live2dChar.GetTouchPart()

		if var_7_1 > 0:
			local var_7_2 = arg_7_0.GetTouchEvent(var_7_1)

			var_7_0 = var_7_2[math.ceil(math.random(#var_7_2))]
		else
			local var_7_3 = arg_7_0.GetIdleEvents()

			var_7_0 = var_7_3[math.floor(math.Random(0, #var_7_3)) + 1]

	if var_7_0:
		arg_7_0.TriggerEvent(var_7_0)

def var_0_0.GetTouchEvent(arg_8_0, arg_8_1):
	return (var_0_1.filterAssistantEvents(var_0_1.getAssistantTouchEvents(arg_8_1), arg_8_0.ship.skinId, 0))

def var_0_0.GetIdleEvents(arg_9_0):
	return (var_0_1.filterAssistantEvents(var_0_1.IdleEvents, arg_9_0.ship.skinId, 0))

def var_0_0.GetEventConfig(arg_10_0, arg_10_1):
	return var_0_1.assistantEvents[arg_10_1]

def var_0_0.TriggerEvent(arg_11_0, arg_11_1):
	if not arg_11_1:
		return

	local var_11_0 = arg_11_0.GetEventConfig(arg_11_1)

	local function var_11_1()
		return

	local var_11_2, var_11_3, var_11_4, var_11_5, var_11_6, var_11_7 = ShipWordHelper.GetCvDataForShip(arg_11_0.ship, var_11_0.dialog)

	if not var_11_7:
		arg_11_0.live2dChar.TriggerAction(var_11_0.action)
		var_11_1()
	else
		arg_11_0.live2dChar.TriggerAction(var_11_0.action, None, None, var_11_1)

def var_0_0.Dispose(arg_13_0):
	pg.DelegateInfo.Dispose(arg_13_0)
	arg_13_0.live2dChar.Dispose()

	arg_13_0.live2dChar = None

	setActive(arg_13_0.live2dContainer, False)

return var_0_0
