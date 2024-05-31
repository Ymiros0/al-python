local var_0_0 = class("SailBoatBg")
local var_0_1 = 1920
local var_0_2 = 1080
local var_0_3 = Vector2(1, 0)
local var_0_4 = Vector2(-1, 0)
local var_0_5 = Vector2(0, 1)
local var_0_6 = Vector2(0, -1)
local var_0_7

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	var_0_7 = SailBoatGameVo
	arg_1_0._tf = arg_1_1
	arg_1_0._event = arg_1_2
	arg_1_0._layerBack = findTF(arg_1_0._tf, "scene_background/content")
	arg_1_0._layerMid = findTF(arg_1_0._tf, "scene/content")
	arg_1_0._layerTop = findTF(arg_1_0._tf, "scene_front/content")
	arg_1_0._layerContent = nil
	arg_1_0._bgGrids = {}
	arg_1_0._bgDic = {}
	arg_1_0._bgPrepareGrids = {}
	arg_1_0._bgTfPool = {}
	arg_1_0._sceneWidth = var_0_7.scene_width
	arg_1_0._sceneHeight = var_0_7.scene_height
end

function var_0_0.setRuleData(arg_2_0, arg_2_1)
	arg_2_0._bgTplName = arg_2_1.tpl
	arg_2_0._layerType = arg_2_1.layer
	arg_2_0._showType = arg_2_1.show
	arg_2_0._width = arg_2_1.width
	arg_2_0._height = arg_2_1.height
	arg_2_0._removeBound = arg_2_1.remove_bound

	if arg_2_0._layerType == SailBoatGameConst.bg_layer_back then
		arg_2_0._layerContent = arg_2_0._layerBack
	elseif arg_2_0._layerType == SailBoatGameConst.bg_layer_mid then
		arg_2_0._layerContent = arg_2_0._layerMid
	elseif arg_2_0._layerType == SailBoatGameConst.bg_layer_top then
		arg_2_0._layerContent = arg_2_0._layerTop
	end

	arg_2_0._content = findTF(arg_2_0._layerContent, arg_2_1.content)
end

function var_0_0.start(arg_3_0)
	arg_3_0:createGrid(0, 0, true)
	arg_3_0:createGrid(0, 0, true)
	arg_3_0:createGrid(0, 0, true)
	arg_3_0:clear()
	arg_3_0:createGrid(0, 0, true)
	arg_3_0:updateGrid()
end

function var_0_0.step(arg_4_0)
	arg_4_0:checkEmptyGrid()
	arg_4_0:updateGrid()
end

function var_0_0.updateGrid(arg_5_0)
	for iter_5_0 = #arg_5_0._bgGrids, 1, -1 do
		local var_5_0 = arg_5_0._bgGrids[iter_5_0]
		local var_5_1 = var_5_0.w
		local var_5_2 = var_5_0.h

		var_5_0.anchoredPos.x = arg_5_0._moveAmount.x + var_5_0.pos.x
		var_5_0.anchoredPos.y = arg_5_0._moveAmount.y + var_5_0.pos.y

		local var_5_3 = false

		if math.abs(var_5_0.anchoredPos.x) > arg_5_0._removeBound.x or math.abs(var_5_0.anchoredPos.y) > arg_5_0._removeBound.y then
			if not var_5_0.stop then
				var_5_0.stop = true

				arg_5_0:removeGrid(var_5_0)
			end
		else
			var_5_0.stop = false
		end

		if not var_5_0.stop then
			if math.abs(var_5_0.anchoredPos.x) < arg_5_0._sceneWidth and math.abs(var_5_0.anchoredPos.y) < arg_5_0._sceneHeight then
				local var_5_4 = arg_5_0:checkPrepareCreate(var_5_0)

				if #var_5_4 > 0 then
					arg_5_0:createPrepareGrid(var_5_4)
				end
			end

			if var_5_0.tf == nil then
				var_5_0.tf = arg_5_0:getBgTf()
				GetComponent(var_5_0.tf, typeof(CanvasGroup)).alpha = 1
			end

			var_5_0.tf.anchoredPosition = var_5_0.anchoredPos
		end
	end

	for iter_5_1 = #arg_5_0._bgPrepareGrids, 1, -1 do
		local var_5_5 = table.remove(arg_5_0._bgPrepareGrids, iter_5_1)

		table.insert(arg_5_0._bgGrids, var_5_5)
	end
end

function var_0_0.checkEmptyGrid(arg_6_0)
	return
end

function var_0_0.checkPrepareCreate(arg_7_0, arg_7_1)
	local var_7_0 = {}
	local var_7_1 = arg_7_1.w
	local var_7_2 = arg_7_1.h
	local var_7_3 = arg_7_1.anchoredPos
	local var_7_4

	if var_7_3.x + arg_7_0._width / 2 < arg_7_0._sceneWidth / 2 + var_0_7.fill_offsetX then
		local var_7_5 = arg_7_0:checkPrepare(var_7_1, var_7_2, var_0_3)

		if var_7_5 then
			table.insert(var_7_0, var_7_5)
		end
	end

	if var_7_3.x - arg_7_0._width / 2 > -arg_7_0._sceneWidth / 2 - var_0_7.fill_offsetX then
		local var_7_6 = arg_7_0:checkPrepare(var_7_1, var_7_2, var_0_4)

		if var_7_6 then
			table.insert(var_7_0, var_7_6)
		end
	end

	if var_7_3.y + arg_7_0._height / 2 < arg_7_0._sceneHeight / 2 + var_0_7.fill_offsetY then
		local var_7_7 = arg_7_0:checkPrepare(var_7_1, var_7_2, var_0_5)

		if var_7_7 then
			table.insert(var_7_0, var_7_7)
		end
	end

	if var_7_3.y - arg_7_0._height / 2 > -arg_7_0._sceneHeight / 2 - var_0_7.fill_offsetY then
		local var_7_8 = arg_7_0:checkPrepare(var_7_1, var_7_2, var_0_6)

		if var_7_8 then
			table.insert(var_7_0, var_7_8)
		end
	end

	return var_7_0
end

function var_0_0.checkPrepare(arg_8_0, arg_8_1, arg_8_2, arg_8_3)
	local var_8_0, var_8_1 = arg_8_0:getDirecWH(arg_8_1, arg_8_2, arg_8_3)
	local var_8_2 = arg_8_0:getGrid(var_8_0, var_8_1)
	local var_8_3 = arg_8_0:getPrepareGrid(var_8_0, var_8_1)

	assert(not var_8_2 or not var_8_3, "创建了两个相同位置的grid,请检查代码")

	if not var_8_2 and not var_8_3 then
		return {
			w = var_8_0,
			h = var_8_1
		}
	end

	return nil
end

function var_0_0.getPrepareGrid(arg_9_0, arg_9_1, arg_9_2)
	for iter_9_0 = 1, #arg_9_0._bgPrepareGrids do
		local var_9_0 = arg_9_0._bgPrepareGrids[iter_9_0]

		if var_9_0.w == arg_9_1 and var_9_0.h == arg_9_2 then
			return var_9_0
		end
	end

	return nil
end

function var_0_0.createPrepareGrid(arg_10_0, arg_10_1)
	for iter_10_0 = 1, #arg_10_1 do
		local var_10_0 = arg_10_1[iter_10_0]
		local var_10_1 = arg_10_0:createGrid(var_10_0.w, var_10_0.h, false)

		table.insert(arg_10_0._bgPrepareGrids, var_10_1)
	end
end

function var_0_0.getDirecWH(arg_11_0, arg_11_1, arg_11_2, arg_11_3)
	return arg_11_1 + arg_11_3.x, arg_11_2 + arg_11_3.y
end

function var_0_0.getGrid(arg_12_0, arg_12_1, arg_12_2)
	for iter_12_0 = 1, #arg_12_0._bgGrids do
		local var_12_0 = arg_12_0._bgGrids[iter_12_0]

		if var_12_0.w == arg_12_1 and var_12_0.h == arg_12_2 then
			return var_12_0
		end
	end

	return nil
end

function var_0_0.createGrid(arg_13_0, arg_13_1, arg_13_2, arg_13_3)
	if not arg_13_0._bgDic[arg_13_1] then
		arg_13_0._bgDic[arg_13_1] = {}
	end

	if arg_13_0._bgDic[arg_13_1][arg_13_2] then
		print("已经存在的grid 无需创建")

		return
	end

	local var_13_0 = {
		pos = Vector2(arg_13_1 * arg_13_0._width, arg_13_2 * arg_13_0._height),
		w = arg_13_1,
		h = arg_13_2,
		anchoredPos = Vector2(0, 0)
	}

	if arg_13_3 then
		table.insert(arg_13_0._bgGrids, var_13_0)

		arg_13_0._bgDic[var_13_0.w][var_13_0.h] = var_13_0
	end

	return var_13_0
end

function var_0_0.removeGrid(arg_14_0, arg_14_1)
	if arg_14_1.tf then
		local var_14_0 = arg_14_1.tf

		GetComponent(arg_14_1.tf, typeof(CanvasGroup)).alpha = 0

		table.insert(arg_14_0._bgTfPool, var_14_0)

		arg_14_1.tf = nil
	end

	arg_14_0._bgDic[arg_14_1.w][arg_14_1.h] = nil
end

function var_0_0.getBgTf(arg_15_0)
	local var_15_0

	if arg_15_0._bgTfPool and #arg_15_0._bgTfPool > 0 then
		var_15_0 = table.remove(arg_15_0._bgTfPool, 1)
	end

	if not var_15_0 then
		var_15_0 = var_0_7.GetGameBgTf(arg_15_0._bgTplName)

		setParent(var_15_0, arg_15_0._content)
	end

	return var_15_0
end

function var_0_0.stop(arg_16_0)
	return
end

function var_0_0.setMoveAmount(arg_17_0, arg_17_1)
	arg_17_0._moveAmount = arg_17_1
end

function var_0_0.clear(arg_18_0)
	arg_18_0._moveAmount = Vector2(0, 0)

	for iter_18_0 = #arg_18_0._bgGrids, 1, -1 do
		local var_18_0 = table.remove(arg_18_0._bgGrids, iter_18_0)

		if var_18_0.tf then
			GetComponent(var_18_0.tf, typeof(CanvasGroup)).alpha = 0

			table.insert(arg_18_0._bgTfPool, var_18_0.tf)
		end
	end

	for iter_18_1 = #arg_18_0._bgPrepareGrids, 1, -1 do
		local var_18_1 = table.remove(arg_18_0._bgPrepareGrids, iter_18_1)

		GetComponent(var_18_1.tf, typeof(CanvasGroup)).alpha = 0

		table.insert(arg_18_0._bgTfPool, var_18_1.tf)
	end

	arg_18_0._bgDic = {}
end

function var_0_0.dispose(arg_19_0)
	return
end

return var_0_0
