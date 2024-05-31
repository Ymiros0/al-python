local var_0_0 = class("PileGameModel")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.controller = arg_1_1
	arg_1_0.items = {}
	arg_1_0.level = 0
	arg_1_0.score = 0
	arg_1_0.failedCnt = 0
	arg_1_0.deathLine = Vector2(0, 0)
	arg_1_0.safeLine = Vector2(0, 0)
	arg_1_0.highestScore = 0
	arg_1_0.screen = Vector2(0, 0)
	arg_1_0.maxFailedCnt = PileGameConst.MAX_FAILED_CNT

def var_0_0.NetData(arg_2_0, arg_2_1):
	arg_2_0.highestScore = arg_2_1.highestScore or 0
	arg_2_0.screen = Vector2(arg_2_1.screen.x, arg_2_1.screen.y)

def var_0_0.UpdateHighestScore(arg_3_0):
	if arg_3_0.score > arg_3_0.highestScore:
		arg_3_0.highestScore = arg_3_0.score

def var_0_0.RandomPile(arg_4_0):
	local var_4_0 = math.random(1, #PileGameConst.Prefabs)

	return PileGameConst.Prefabs[var_4_0]

def var_0_0.AddHeadPile(arg_5_0):
	local var_5_0 = PileGameConst.HEAD

	return arg_5_0.AddPile(var_5_0)

def var_0_0.AddPileByRandom(arg_6_0):
	local var_6_0 = arg_6_0.RandomPile()

	return arg_6_0.AddPile(var_6_0)

def var_0_0.AddPile(arg_7_0, arg_7_1):
	arg_7_0.level = arg_7_0.level + 1

	local var_7_0 = arg_7_0.GetSpeed()
	local var_7_1 = {
		onTheMove = False,
		gname = arg_7_1.name,
		name = arg_7_0.level,
		position = Vector3(0, PileGameConst.START_Y, 0),
		leftMaxPosition = Vector3(-PileGameConst.MAX_SLIDE_DISTANCE, PileGameConst.START_Y, 0),
		rightMaxPosition = Vector3(PileGameConst.MAX_SLIDE_DISTANCE, PileGameConst.START_Y, 0),
		speed = var_7_0,
		dropSpeed = PileGameConst.DROP_SPEED,
		sizeDelta = Vector2(arg_7_1.size[1], arg_7_1.size[2]),
		pivot = PileGameConst.ITEM_PIVOT,
		collider = {
			offset = Vector2(arg_7_1.boundary[1], arg_7_1.boundary[2]),
			sizeDelta = Vector2(arg_7_1.boundary[3], arg_7_1.boundary[4])
		},
		speActionCount = arg_7_1.speActionCount or 0
	}

	table.insert(arg_7_0.items, var_7_1)

	return var_7_1

def var_0_0.GetSpeed(arg_8_0):
	local var_8_0 = PileGameConst.SLIDE_SPEED
	local var_8_1 = PileGameConst.SLIDE_GROWTH[1]
	local var_8_2 = PileGameConst.SLIDE_GROWTH[2]

	return var_8_0 * (1 + math.floor(arg_8_0.level / var_8_1) * var_8_2)

def var_0_0.AddGround(arg_9_0):
	arg_9_0.ground = {
		position = Vector3(0, -arg_9_0.screen.y / 2, 0),
		pivot = PileGameConst.GROUND_PIVOT,
		sizeDelta = PileGameConst.GROUND_SIZE
	}

def var_0_0.AddDeathLineRight(arg_10_0):
	arg_10_0.deathLine.x = -PileGameConst.DEATH_LINE_DISTANCE

def var_0_0.AddDeathLineLeft(arg_11_0):
	arg_11_0.deathLine.y = PileGameConst.DEATH_LINE_DISTANCE

def var_0_0.AddSafeLineRight(arg_12_0):
	arg_12_0.safeLine.x = -PileGameConst.SAFE_LINE_DISTANCE

def var_0_0.AddSafeLineLeft(arg_13_0):
	arg_13_0.safeLine.y = PileGameConst.SAFE_LINE_DISTANCE

def var_0_0.IsStopDrop(arg_14_0, arg_14_1):
	local var_14_0 = arg_14_0.IsOnGround(arg_14_1)
	local var_14_1 = arg_14_0.OnPrevItem(arg_14_1)

	return var_14_0 or var_14_1

def var_0_0.IsOnGround(arg_15_0, arg_15_1):
	return arg_15_1.position.y <= arg_15_0.ground.position.y

def var_0_0.GetIndex(arg_16_0):
	return #arg_16_0.items

def var_0_0.OnPrevItem(arg_17_0, arg_17_1):
	local var_17_0 = #arg_17_0.items - 1

	if var_17_0 > 0:
		local var_17_1 = arg_17_0.items[var_17_0]

		return arg_17_0.IsOverlap(arg_17_1, var_17_1)

def var_0_0.IsOverTailItem(arg_18_0, arg_18_1):
	local var_18_0 = arg_18_0.items[#arg_18_0.items - 1]

	if var_18_0:
		return arg_18_0.IsOverItem(arg_18_1, var_18_0)

	return False

def var_0_0.IsOverItem(arg_19_0, arg_19_1, arg_19_2):
	local var_19_0 = Vector2(arg_19_1.position.x + (0.5 - arg_19_1.pivot.x) * arg_19_1.sizeDelta.x + arg_19_1.collider.offset.x, arg_19_1.position.y + (0.5 - arg_19_1.pivot.y) * arg_19_1.sizeDelta.y + arg_19_1.collider.offset.y)

	return arg_19_2.position.y + (0.5 - arg_19_2.pivot.y) * arg_19_2.sizeDelta.y + arg_19_2.collider.offset.y + arg_19_2.collider.sizeDelta.y / 2 >= var_19_0.y - arg_19_1.collider.sizeDelta.y / 2

def var_0_0.IsOverlap(arg_20_0, arg_20_1, arg_20_2):
	if arg_20_0.IsOverItem(arg_20_1, arg_20_2):
		local var_20_0 = Vector2(arg_20_1.position.x + (0.5 - arg_20_1.pivot.x) * arg_20_1.sizeDelta.x + arg_20_1.collider.offset.x, arg_20_1.position.y + (0.5 - arg_20_1.pivot.y) * arg_20_1.sizeDelta.y + arg_20_1.collider.offset.y)
		local var_20_1 = arg_20_2.position.x + (0.5 - arg_20_2.pivot.x) * arg_20_2.sizeDelta.x + arg_20_2.collider.offset.x
		local var_20_2 = Vector2(var_20_1 - arg_20_2.collider.sizeDelta.x / 2, var_20_1 + arg_20_2.collider.sizeDelta.x / 2)

		return var_20_0.x >= var_20_2.x and var_20_0.x <= var_20_2.y

def var_0_0.CanDropOnPrev(arg_21_0, arg_21_1):
	local var_21_0 = #arg_21_0.items - 1

	if var_21_0 > 0:
		local var_21_1 = Vector2(arg_21_1.position.x + (0.5 - arg_21_1.pivot.x) * arg_21_1.sizeDelta.x + arg_21_1.collider.offset.x, arg_21_1.position.y + (0.5 - arg_21_1.pivot.y) * arg_21_1.sizeDelta.y + arg_21_1.collider.offset.y)
		local var_21_2 = arg_21_0.items[var_21_0]
		local var_21_3 = var_21_2.position.x + (0.5 - var_21_2.pivot.x) * var_21_2.sizeDelta.x + var_21_2.collider.offset.x
		local var_21_4 = Vector2(var_21_3 - var_21_2.collider.sizeDelta.x / 2, var_21_3 + var_21_2.collider.sizeDelta.x / 2)

		return var_21_1.x >= var_21_4.x and var_21_1.x <= var_21_4.y

def var_0_0.AddFailedCnt(arg_22_0):
	arg_22_0.failedCnt = arg_22_0.failedCnt + 1

def var_0_0.RemoveTailItem(arg_23_0):
	table.remove(arg_23_0.items, #arg_23_0.items)

def var_0_0.AddScore(arg_24_0):
	arg_24_0.score = arg_24_0.score + 1

def var_0_0.IsMaxfailedCnt(arg_25_0):
	return arg_25_0.maxFailedCnt == arg_25_0.failedCnt

def var_0_0.IsOverDeathLine(arg_26_0, arg_26_1):
	local var_26_0 = arg_26_1.position.x
	local var_26_1 = var_26_0 - arg_26_1.collider.sizeDelta.x / 2 <= arg_26_0.deathLine.x
	local var_26_2 = var_26_0 + arg_26_1.collider.sizeDelta.x / 2 >= arg_26_0.deathLine.y

	return var_26_1 or var_26_2

def var_0_0.ShouldSink(arg_27_0):
	return arg_27_0.GetIndex() == PileGameConst.SINK_LEVEL + 1

def var_0_0.GetPrevItem(arg_28_0, arg_28_1):
	arg_28_1 = arg_28_1 - 1

	return arg_28_0.items[arg_28_1]

def var_0_0.GetNextPos(arg_29_0, arg_29_1):
	local var_29_0 = arg_29_0.items[arg_29_1]
	local var_29_1 = arg_29_0.GetPrevItem(arg_29_1)
	local var_29_2 = 0

	if var_29_1:
		var_29_2 = var_29_1.position.y + var_29_1.sizeDelta.y
	else
		var_29_2 = var_29_0.position.y - var_29_0.sizeDelta.y

	return Vector3(var_29_0.position.x, var_29_2, 0)

def var_0_0.IsExceedingTheHighestScore(arg_30_0):
	return arg_30_0.score - arg_30_0.highestScore == 1

def var_0_0.RemoveFirstItem(arg_31_0):
	return table.remove(arg_31_0.items, 1)

def var_0_0.GetFirstItem(arg_32_0):
	return arg_32_0.items[1]

def var_0_0.GetTailItem(arg_33_0):
	return arg_33_0.items[#arg_33_0.items]

def var_0_0.GetDropArea(arg_34_0, arg_34_1):
	local var_34_0
	local var_34_1 = arg_34_1.position.x - arg_34_1.collider.sizeDelta.x / 2
	local var_34_2 = arg_34_1.position.x + arg_34_1.collider.sizeDelta.x / 2

	if var_34_1 <= arg_34_0.deathLine.x or var_34_2 >= arg_34_0.deathLine.y:
		var_34_0 = PileGameController.DROP_AREA_DANGER
	elif var_34_1 <= arg_34_0.safeLine.x or var_34_2 >= arg_34_0.safeLine.y:
		var_34_0 = PileGameController.DROP_AREA_WARN
	else
		var_34_0 = PileGameController.DROP_AREA_SAFE

	return var_34_0

def var_0_0.GetInitPos(arg_35_0):
	local var_35_0 = {}
	local var_35_1 = PileGameConst.SHAKE_DIS + arg_35_0.score * PileGameConst.SHAKE_DIS_RATIO

	for iter_35_0, iter_35_1 in ipairs(arg_35_0.items):
		table.insert(var_35_0, {
			iter_35_1,
			iter_35_1.position.x - var_35_1,
			iter_35_1.position.x + var_35_1
		})

	return var_35_0

def var_0_0.Clear(arg_36_0):
	arg_36_0.level = 0
	arg_36_0.score = 0
	arg_36_0.failedCnt = 0
	arg_36_0.items = {}

def var_0_0.Dispose(arg_37_0):
	arg_37_0.Clear()

return var_0_0
