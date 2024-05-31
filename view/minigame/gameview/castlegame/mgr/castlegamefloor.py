local var_0_0 = class("CastleGameFloor")
local var_0_1 = 999999

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._tpl = arg_1_1
	arg_1_0._event = arg_1_2
	arg_1_0.floors = {}
	arg_1_0.colliders = {}
	arg_1_0.floorTfs = {}
	arg_1_0.bounds = {}

	local var_1_0 = CastleGameVo.h_count * CastleGameVo.w_count

	for iter_1_0 = 0, var_1_0 - 1:
		local var_1_1 = tf(instantiate(arg_1_0._tpl))

		var_1_1.name = tostring(iter_1_0 + 1)

		setActive(var_1_1, True)

		local var_1_2 = findTF(var_1_1, "zPos")
		local var_1_3 = findTF(var_1_1, "zPos/floor/img")

		setImageSprite(var_1_3, CastleGameVo.getFloorImage(iter_1_0 + 1), True)

		local var_1_4 = var_1_1.anchoredPosition
		local var_1_5 = findTF(var_1_1, "zPos/collider")
		local var_1_6 = GetComponent(var_1_5, typeof("UnityEngine.PolygonCollider2D"))
		local var_1_7 = GetComponent(findTF(var_1_1, "zPos/floor"), typeof(Animator))
		local var_1_8 = iter_1_0 % CastleGameVo.h_count
		local var_1_9 = math.floor(iter_1_0 / CastleGameVo.w_count)

		table.insert(arg_1_0.colliders, var_1_6)
		table.insert(arg_1_0.floorTfs, var_1_1)
		table.insert(arg_1_0.floors, {
			fall = False,
			tf = var_1_1,
			zPos = var_1_2,
			anim = var_1_7,
			index = iter_1_0,
			collider = var_1_6,
			w = var_1_8,
			h = var_1_9
		})

	arg_1_0.updateFloorPos()
	arg_1_0.updateBounds()

def var_0_0.getTfs(arg_2_0):
	return arg_2_0.floorTfs

def var_0_0.getFloors(arg_3_0):
	return arg_3_0.floors

def var_0_0.getActiveIndexs(arg_4_0):
	return arg_4_0.activeIndexs

def var_0_0.updateBounds(arg_5_0):
	for iter_5_0 = 1, #arg_5_0.floors:
		local var_5_0 = arg_5_0.floors[iter_5_0].collider.points
		local var_5_1 = arg_5_0.floors[iter_5_0].tf.anchoredPosition
		local var_5_2 = {}

		for iter_5_1 = 0, var_5_0.Length - 1:
			local var_5_3 = Vector2(var_5_1.x + var_5_0[iter_5_1].x, var_5_1.y + var_5_0[iter_5_1].y)

			table.insert(var_5_2, var_5_3)

		arg_5_0.floors[iter_5_0].bound = var_5_2

		table.insert(arg_5_0.bounds, var_5_2)

def var_0_0.getBounds(arg_6_0):
	return arg_6_0.bounds

def var_0_0.setContent(arg_7_0, arg_7_1):
	if not arg_7_1:
		print("地板的容器不能为None")

		return

	arg_7_0._content = arg_7_1

	for iter_7_0 = 1, #arg_7_0.floorTfs:
		SetParent(arg_7_0.floorTfs[iter_7_0], arg_7_1)

def var_0_0.start(arg_8_0):
	arg_8_0.fallDatas = arg_8_0.getFallDatas()
	arg_8_0.floorFallStep = var_0_1
	arg_8_0.activeIndexs = {}

	for iter_8_0 = 1, #arg_8_0.floors:
		arg_8_0.floors[iter_8_0].fall = False
		arg_8_0.floors[iter_8_0].removeTime = None
		arg_8_0.floors[iter_8_0].revertTime = None

		setActive(arg_8_0.floors[iter_8_0].tf, False)
		setActive(arg_8_0.floors[iter_8_0].tf, True)
		table.insert(arg_8_0.activeIndexs, arg_8_0.floors[iter_8_0].index)

	arg_8_0.updateFloorPos()

def var_0_0.step(arg_9_0):
	if arg_9_0.floorFallStep and arg_9_0.floorFallStep > 0:
		arg_9_0.floorFallStep = arg_9_0.floorFallStep - CastleGameVo.deltaTime

		if arg_9_0.floorFallStep <= 0:
			-- block empty

	for iter_9_0 = #arg_9_0.floors, 1, -1:
		local var_9_0 = arg_9_0.floors[iter_9_0]

		if var_9_0.removeTime and var_9_0.removeTime > 0:
			var_9_0.removeTime = var_9_0.removeTime - CastleGameVo.deltaTime

			if var_9_0.removeTime <= 0:
				var_9_0.removeTime = None

				arg_9_0.applyFloorFall(var_9_0)

	for iter_9_1 = #arg_9_0.floors, 1, -1:
		local var_9_1 = arg_9_0.floors[iter_9_1]

		if var_9_1.revertTime and var_9_1.revertTime > 0:
			var_9_1.revertTime = var_9_1.revertTime - CastleGameVo.deltaTime

			if var_9_1.revertTime <= 0:
				var_9_1.revertTime = None

				arg_9_0.revertFloorFall(var_9_1)
				arg_9_0.revertActiveFloor(var_9_1)

	for iter_9_2 = #arg_9_0.fallDatas, 1, -1:
		if CastleGameVo.gameStepTime >= arg_9_0.fallDatas[iter_9_2].time:
			local var_9_2 = table.remove(arg_9_0.fallDatas, iter_9_2)

			arg_9_0.removeFloorByFallData(var_9_2)

			break

def var_0_0.setBroken(arg_10_0, arg_10_1, arg_10_2):
	local var_10_0 = arg_10_0.getFloorByIndex(arg_10_1)

	arg_10_0.setFloorFallTime(var_10_0, False, arg_10_2)

def var_0_0.removeFloorByFallData(arg_11_0, arg_11_1):
	local var_11_0 = table.remove(arg_11_1.rule_id, math.random(1, #arg_11_1.rule_id))
	local var_11_1 = CastleGameVo.floor_rule[var_11_0]

	for iter_11_0 = 1, #var_11_1:
		local var_11_2 = arg_11_0.getFloorByIndex(var_11_1[iter_11_0])

		arg_11_0.setFloorFallTime(var_11_2, True, None)

def var_0_0.clear(arg_12_0):
	return

def var_0_0.setFloorFallCallback(arg_13_0, arg_13_1):
	arg_13_0.floorFallCallback = arg_13_1

def var_0_0.getFallDatas(arg_14_0):
	return CastleGameVo.roundData.floors

def var_0_0.applyFloorFall(arg_15_0, arg_15_1):
	local var_15_0 = arg_15_1.zPos
	local var_15_1 = arg_15_1.anim

	arg_15_1.fall = True
	arg_15_1.revertTime = CastleGameVo.floor_revert_time

	var_15_1.Play("hide")

def var_0_0.revertFloorFall(arg_16_0, arg_16_1):
	local var_16_0 = arg_16_1.anim

	arg_16_1.fall = False

	var_16_0.Play("revert")

def var_0_0.revertActiveFloor(arg_17_0, arg_17_1):
	if not table.contains(arg_17_0.activeIndexs, arg_17_1.index):
		table.insert(arg_17_0.activeIndexs, arg_17_1.index)

def var_0_0.removeActiveFloor(arg_18_0, arg_18_1):
	for iter_18_0 = #arg_18_0.activeIndexs, 1, -1:
		if arg_18_0.activeIndexs[iter_18_0] == arg_18_1.index:
			table.remove(arg_18_0.activeIndexs, iter_18_0)

def var_0_0.setFloorFallTime(arg_19_0, arg_19_1, arg_19_2, arg_19_3):
	for iter_19_0 = 1, #arg_19_1:
		if arg_19_2:
			arg_19_1[iter_19_0].anim.Play("shake")

		if not arg_19_1[iter_19_0].fall:
			arg_19_1[iter_19_0].removeTime = arg_19_3 and arg_19_3 or CastleGameVo.floor_remove_time
			arg_19_1[iter_19_0].revertTime = None

			arg_19_0.removeActiveFloor(arg_19_1[iter_19_0])
		else
			print(arg_19_1[iter_19_0].index .. "已经被移除，无法设置掉落")

def var_0_0.getFloorByIndex(arg_20_0, arg_20_1, arg_20_2):
	for iter_20_0 = 1, #arg_20_0.floors:
		if arg_20_0.floors[iter_20_0].index == arg_20_1:
			return {
				arg_20_0.floors[iter_20_0]
			}

	print("找不到index = " .. arg_20_1 .. "的地板")

	return {}

def var_0_0.updateFloorPos(arg_21_0):
	for iter_21_0 = 1, #arg_21_0.floors:
		local var_21_0 = arg_21_0.floors[iter_21_0].index
		local var_21_1 = var_21_0 % CastleGameVo.w_count
		local var_21_2 = math.floor(var_21_0 / CastleGameVo.h_count)

		arg_21_0.floors[iter_21_0].tf.anchoredPosition = CastleGameVo.GetRotationPosByWH(var_21_1, var_21_2)

def var_0_0.getOutLandPoint(arg_22_0):
	local var_22_0 = arg_22_0.floors[1].bound[1]
	local var_22_1 = arg_22_0.floors[(CastleGameVo.h_count - 1) * CastleGameVo.w_count + 1].bound[2]
	local var_22_2 = arg_22_0.floors[CastleGameVo.w_count].bound[4]
	local var_22_3 = arg_22_0.floors[CastleGameVo.h_count * CastleGameVo.w_count].bound[3]

	return {
		lb = var_22_0,
		lt = var_22_1,
		rt = var_22_3,
		rb = var_22_2
	}

def var_0_0.press(arg_23_0, arg_23_1):
	return

return var_0_0
