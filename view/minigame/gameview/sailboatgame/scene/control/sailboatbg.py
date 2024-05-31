local var_0_0 = class("SailBoatBg")
local var_0_1 = 1920
local var_0_2 = 1080
local var_0_3 = Vector2(1, 0)
local var_0_4 = Vector2(-1, 0)
local var_0_5 = Vector2(0, 1)
local var_0_6 = Vector2(0, -1)
local var_0_7

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_7 = SailBoatGameVo
	arg_1_0._tf = arg_1_1
	arg_1_0._event = arg_1_2
	arg_1_0._layerBack = findTF(arg_1_0._tf, "scene_background/content")
	arg_1_0._layerMid = findTF(arg_1_0._tf, "scene/content")
	arg_1_0._layerTop = findTF(arg_1_0._tf, "scene_front/content")
	arg_1_0._layerContent = None
	arg_1_0._bgGrids = {}
	arg_1_0._bgDic = {}
	arg_1_0._bgPrepareGrids = {}
	arg_1_0._bgTfPool = {}
	arg_1_0._sceneWidth = var_0_7.scene_width
	arg_1_0._sceneHeight = var_0_7.scene_height

def var_0_0.setRuleData(arg_2_0, arg_2_1):
	arg_2_0._bgTplName = arg_2_1.tpl
	arg_2_0._layerType = arg_2_1.layer
	arg_2_0._showType = arg_2_1.show
	arg_2_0._width = arg_2_1.width
	arg_2_0._height = arg_2_1.height
	arg_2_0._removeBound = arg_2_1.remove_bound

	if arg_2_0._layerType == SailBoatGameConst.bg_layer_back:
		arg_2_0._layerContent = arg_2_0._layerBack
	elif arg_2_0._layerType == SailBoatGameConst.bg_layer_mid:
		arg_2_0._layerContent = arg_2_0._layerMid
	elif arg_2_0._layerType == SailBoatGameConst.bg_layer_top:
		arg_2_0._layerContent = arg_2_0._layerTop

	arg_2_0._content = findTF(arg_2_0._layerContent, arg_2_1.content)

def var_0_0.start(arg_3_0):
	arg_3_0.createGrid(0, 0, True)
	arg_3_0.createGrid(0, 0, True)
	arg_3_0.createGrid(0, 0, True)
	arg_3_0.clear()
	arg_3_0.createGrid(0, 0, True)
	arg_3_0.updateGrid()

def var_0_0.step(arg_4_0):
	arg_4_0.checkEmptyGrid()
	arg_4_0.updateGrid()

def var_0_0.updateGrid(arg_5_0):
	for iter_5_0 = #arg_5_0._bgGrids, 1, -1:
		local var_5_0 = arg_5_0._bgGrids[iter_5_0]
		local var_5_1 = var_5_0.w
		local var_5_2 = var_5_0.h

		var_5_0.anchoredPos.x = arg_5_0._moveAmount.x + var_5_0.pos.x
		var_5_0.anchoredPos.y = arg_5_0._moveAmount.y + var_5_0.pos.y

		local var_5_3 = False

		if math.abs(var_5_0.anchoredPos.x) > arg_5_0._removeBound.x or math.abs(var_5_0.anchoredPos.y) > arg_5_0._removeBound.y:
			if not var_5_0.stop:
				var_5_0.stop = True

				arg_5_0.removeGrid(var_5_0)
		else
			var_5_0.stop = False

		if not var_5_0.stop:
			if math.abs(var_5_0.anchoredPos.x) < arg_5_0._sceneWidth and math.abs(var_5_0.anchoredPos.y) < arg_5_0._sceneHeight:
				local var_5_4 = arg_5_0.checkPrepareCreate(var_5_0)

				if #var_5_4 > 0:
					arg_5_0.createPrepareGrid(var_5_4)

			if var_5_0.tf == None:
				var_5_0.tf = arg_5_0.getBgTf()
				GetComponent(var_5_0.tf, typeof(CanvasGroup)).alpha = 1

			var_5_0.tf.anchoredPosition = var_5_0.anchoredPos

	for iter_5_1 = #arg_5_0._bgPrepareGrids, 1, -1:
		local var_5_5 = table.remove(arg_5_0._bgPrepareGrids, iter_5_1)

		table.insert(arg_5_0._bgGrids, var_5_5)

def var_0_0.checkEmptyGrid(arg_6_0):
	return

def var_0_0.checkPrepareCreate(arg_7_0, arg_7_1):
	local var_7_0 = {}
	local var_7_1 = arg_7_1.w
	local var_7_2 = arg_7_1.h
	local var_7_3 = arg_7_1.anchoredPos
	local var_7_4

	if var_7_3.x + arg_7_0._width / 2 < arg_7_0._sceneWidth / 2 + var_0_7.fill_offsetX:
		local var_7_5 = arg_7_0.checkPrepare(var_7_1, var_7_2, var_0_3)

		if var_7_5:
			table.insert(var_7_0, var_7_5)

	if var_7_3.x - arg_7_0._width / 2 > -arg_7_0._sceneWidth / 2 - var_0_7.fill_offsetX:
		local var_7_6 = arg_7_0.checkPrepare(var_7_1, var_7_2, var_0_4)

		if var_7_6:
			table.insert(var_7_0, var_7_6)

	if var_7_3.y + arg_7_0._height / 2 < arg_7_0._sceneHeight / 2 + var_0_7.fill_offsetY:
		local var_7_7 = arg_7_0.checkPrepare(var_7_1, var_7_2, var_0_5)

		if var_7_7:
			table.insert(var_7_0, var_7_7)

	if var_7_3.y - arg_7_0._height / 2 > -arg_7_0._sceneHeight / 2 - var_0_7.fill_offsetY:
		local var_7_8 = arg_7_0.checkPrepare(var_7_1, var_7_2, var_0_6)

		if var_7_8:
			table.insert(var_7_0, var_7_8)

	return var_7_0

def var_0_0.checkPrepare(arg_8_0, arg_8_1, arg_8_2, arg_8_3):
	local var_8_0, var_8_1 = arg_8_0.getDirecWH(arg_8_1, arg_8_2, arg_8_3)
	local var_8_2 = arg_8_0.getGrid(var_8_0, var_8_1)
	local var_8_3 = arg_8_0.getPrepareGrid(var_8_0, var_8_1)

	assert(not var_8_2 or not var_8_3, "创建了两个相同位置的grid,请检查代码")

	if not var_8_2 and not var_8_3:
		return {
			w = var_8_0,
			h = var_8_1
		}

	return None

def var_0_0.getPrepareGrid(arg_9_0, arg_9_1, arg_9_2):
	for iter_9_0 = 1, #arg_9_0._bgPrepareGrids:
		local var_9_0 = arg_9_0._bgPrepareGrids[iter_9_0]

		if var_9_0.w == arg_9_1 and var_9_0.h == arg_9_2:
			return var_9_0

	return None

def var_0_0.createPrepareGrid(arg_10_0, arg_10_1):
	for iter_10_0 = 1, #arg_10_1:
		local var_10_0 = arg_10_1[iter_10_0]
		local var_10_1 = arg_10_0.createGrid(var_10_0.w, var_10_0.h, False)

		table.insert(arg_10_0._bgPrepareGrids, var_10_1)

def var_0_0.getDirecWH(arg_11_0, arg_11_1, arg_11_2, arg_11_3):
	return arg_11_1 + arg_11_3.x, arg_11_2 + arg_11_3.y

def var_0_0.getGrid(arg_12_0, arg_12_1, arg_12_2):
	for iter_12_0 = 1, #arg_12_0._bgGrids:
		local var_12_0 = arg_12_0._bgGrids[iter_12_0]

		if var_12_0.w == arg_12_1 and var_12_0.h == arg_12_2:
			return var_12_0

	return None

def var_0_0.createGrid(arg_13_0, arg_13_1, arg_13_2, arg_13_3):
	if not arg_13_0._bgDic[arg_13_1]:
		arg_13_0._bgDic[arg_13_1] = {}

	if arg_13_0._bgDic[arg_13_1][arg_13_2]:
		print("已经存在的grid 无需创建")

		return

	local var_13_0 = {
		pos = Vector2(arg_13_1 * arg_13_0._width, arg_13_2 * arg_13_0._height),
		w = arg_13_1,
		h = arg_13_2,
		anchoredPos = Vector2(0, 0)
	}

	if arg_13_3:
		table.insert(arg_13_0._bgGrids, var_13_0)

		arg_13_0._bgDic[var_13_0.w][var_13_0.h] = var_13_0

	return var_13_0

def var_0_0.removeGrid(arg_14_0, arg_14_1):
	if arg_14_1.tf:
		local var_14_0 = arg_14_1.tf

		GetComponent(arg_14_1.tf, typeof(CanvasGroup)).alpha = 0

		table.insert(arg_14_0._bgTfPool, var_14_0)

		arg_14_1.tf = None

	arg_14_0._bgDic[arg_14_1.w][arg_14_1.h] = None

def var_0_0.getBgTf(arg_15_0):
	local var_15_0

	if arg_15_0._bgTfPool and #arg_15_0._bgTfPool > 0:
		var_15_0 = table.remove(arg_15_0._bgTfPool, 1)

	if not var_15_0:
		var_15_0 = var_0_7.GetGameBgTf(arg_15_0._bgTplName)

		setParent(var_15_0, arg_15_0._content)

	return var_15_0

def var_0_0.stop(arg_16_0):
	return

def var_0_0.setMoveAmount(arg_17_0, arg_17_1):
	arg_17_0._moveAmount = arg_17_1

def var_0_0.clear(arg_18_0):
	arg_18_0._moveAmount = Vector2(0, 0)

	for iter_18_0 = #arg_18_0._bgGrids, 1, -1:
		local var_18_0 = table.remove(arg_18_0._bgGrids, iter_18_0)

		if var_18_0.tf:
			GetComponent(var_18_0.tf, typeof(CanvasGroup)).alpha = 0

			table.insert(arg_18_0._bgTfPool, var_18_0.tf)

	for iter_18_1 = #arg_18_0._bgPrepareGrids, 1, -1:
		local var_18_1 = table.remove(arg_18_0._bgPrepareGrids, iter_18_1)

		GetComponent(var_18_1.tf, typeof(CanvasGroup)).alpha = 0

		table.insert(arg_18_0._bgTfPool, var_18_1.tf)

	arg_18_0._bgDic = {}

def var_0_0.dispose(arg_19_0):
	return

return var_0_0
