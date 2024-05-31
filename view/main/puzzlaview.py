local var_0_0 = class("PuzzlaView")
local var_0_1 = 0.3
local var_0_2 = 0
local var_0_3 = 5
local var_0_4 = 4
local var_0_5 = 4
local var_0_6 = {
	3,
	3,
	2,
	4,
	2,
	4,
	2,
	3,
	1,
	3,
	2,
	4,
	1,
	4,
	1,
	3,
	2,
	2,
	3,
	1,
	4,
	1,
	1,
	3,
	3,
	2,
	4,
	4,
	2,
	2,
	3,
	1,
	4,
	1,
	1,
	3,
	2,
	4,
	2,
	4,
	2,
	3,
	3,
	3,
	1,
	4,
	2,
	3,
	1,
	4,
	1,
	3,
	1,
	4,
	2,
	2,
	3,
	1,
	1,
	4,
	2,
	4,
	2,
	3,
	3,
	1,
	4,
	2,
	2,
	3,
	1,
	4,
	4,
	2,
	4,
	1,
	1,
	1,
	3,
	3,
	3,
	2,
	4,
	4,
	2,
	2,
	4,
	1,
	1,
	1,
	3,
	3,
	2,
	4,
	4,
	1,
	3,
	2,
	2,
	2,
	1,
	1,
	1,
	4
}
local var_0_7 = True
local var_0_8 = {
	"BOTTOM",
	"TOP",
	"LEFT",
	"RIGHT"
}
local var_0_9 = {
	TOP = 2,
	BOTTOM = 1,
	LEFT = 3,
	RIGHT = 4
}
local var_0_10 = {
	BOTTOM = 2,
	TOP = 1,
	LEFT = 4,
	RIGHT = 3
}

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	pg.DelegateInfo.New(arg_1_0)

	arg_1_0.showDesc = arg_1_1.descs
	arg_1_0.openlist = arg_1_1.list
	arg_1_0._go = arg_1_1.go
	arg_1_0._tf = tf(arg_1_0._go)
	arg_1_0.fetch = arg_1_1.fetch

	arg_1_0.load(arg_1_1.bg, arg_1_2)

	arg_1_0.onFinish = None

def var_0_0.load(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0.puzzlaWidth, arg_2_0.puzzlaHeight = 0, 0
	arg_2_0.startPosition = Vector2(0, 0)
	arg_2_0.totalCount = var_0_4 * var_0_5
	arg_2_0.pics = {}

	for iter_2_0 = 1, arg_2_0.totalCount:
		local var_2_0 = "pic_" .. iter_2_0

		arg_2_0.pics[iter_2_0] = GetSpriteFromAtlas("puzzla/" .. arg_2_1, var_2_0)

	if #arg_2_0.pics > 0:
		local var_2_1 = arg_2_0.pics[1]

		arg_2_0.puzzlaWidth = var_2_1.rect.width * var_0_4
		arg_2_0.puzzlaHeight = var_2_1.rect.height * var_0_5
		arg_2_0.startPosition = Vector2(arg_2_0.puzzlaWidth / 2, arg_2_0.puzzlaHeight / 2)

		arg_2_0.init()

	if arg_2_2:
		arg_2_2()

def var_0_0.init(arg_3_0):
	arg_3_0.puzzlaItems = {}

	local var_3_0 = 1

	for iter_3_0 = 1, var_0_4:
		local var_3_1 = {}

		for iter_3_1 = 1, var_0_5:
			local var_3_2 = table.contains(arg_3_0.openlist, var_3_0)
			local var_3_3

			if not var_3_2 and arg_3_0.showDesc[var_3_0]:
				var_3_3 = arg_3_0.showDesc[var_3_0]

			local var_3_4 = arg_3_0.createItem(arg_3_0.pics[var_3_0], Vector2(iter_3_1, iter_3_0), var_3_0, var_3_2, var_3_3)
			local var_3_5 = Vector2((iter_3_1 - 1) * var_3_4.width - arg_3_0.startPosition.x, arg_3_0.startPosition.y + (iter_3_0 - 1) * var_3_4.height * -1)

			var_3_4.setLocalPosition(var_3_5)
			table.insert(var_3_1, var_3_4)

			var_3_0 = var_3_0 + 1

		table.insert(arg_3_0.puzzlaItems, var_3_1)

	if arg_3_0.fetch:
		arg_3_0.blockEvent = True

		arg_3_0.getBlockItem().setHightLight()

		return

	if var_0_7 and #var_0_6 > 0:
		arg_3_0.disorganizePuzzla(var_0_6)
	else
		arg_3_0.disorganizePuzzla()

def var_0_0.createItem(arg_4_0, arg_4_1, arg_4_2, arg_4_3, arg_4_4, arg_4_5):
	local var_4_0 = GameObject(arg_4_2.x .. "-" .. arg_4_2.y)

	var_4_0.AddComponent(typeof(Image))
	SetParent(var_4_0, arg_4_0._tf)

	local var_4_1 = PuzzlaItem.New(var_4_0, arg_4_3, arg_4_4, arg_4_5)
	local var_4_2 = arg_4_3 == arg_4_0.totalCount

	var_4_1.update(arg_4_1, arg_4_2, var_4_2)
	onButton(arg_4_0, var_4_1._go, function()
		if arg_4_0.blockEvent:
			return

		arg_4_0.checkSurround(var_4_1), SFX_PANEL)

	return var_4_1

def var_0_0.checkSurround(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_1.getSurroundPosition()
	local var_6_1 = arg_6_0.getBlockItemByPositions(var_6_0)

	if var_6_1:
		arg_6_0.swop(arg_6_1, var_6_1)

def var_0_0.swop(arg_7_0, arg_7_1, arg_7_2):
	local var_7_0 = arg_7_2.getPosition()
	local var_7_1 = arg_7_1.getPosition()
	local var_7_2 = arg_7_2.getCurrIndex()
	local var_7_3 = arg_7_1.getCurrIndex()
	local var_7_4 = arg_7_2.getLocalPosition()
	local var_7_5 = arg_7_1.getLocalPosition()

	arg_7_1.setPosition(var_7_0, var_7_2)
	arg_7_2.setPosition(var_7_1, var_7_3)

	arg_7_0.puzzlaItems[var_7_0.y][var_7_0.x], arg_7_0.puzzlaItems[var_7_1.y][var_7_1.x] = arg_7_1, arg_7_2

	arg_7_2.setLocalPosition(var_7_5)
	arg_7_1.setLocalPosition(var_7_4)

	if arg_7_0.isFinish():
		arg_7_0.blockEvent = True

		arg_7_2.setHightLight()

		if arg_7_0.onFinish:
			arg_7_0.onFinish()
	else
		arg_7_2.setBlock()

def var_0_0.getBlockItemByPositions(arg_8_0, arg_8_1):
	local var_8_0

	for iter_8_0, iter_8_1 in ipairs(arg_8_1):
		if arg_8_0.isValidPosition(iter_8_1) and arg_8_0.isBlockItem(iter_8_1):
			var_8_0 = arg_8_0.getItemByPosition(iter_8_1)

			break

	return var_8_0

def var_0_0.isBlockItem(arg_9_0, arg_9_1):
	return arg_9_0.getItemByPosition(arg_9_1).isBlock()

def var_0_0.getItemByPosition(arg_10_0, arg_10_1):
	assert(arg_10_0.puzzlaItems[arg_10_1.y], "position y" .. arg_10_1.y)

	return arg_10_0.puzzlaItems[arg_10_1.y][arg_10_1.x]

def var_0_0.isValidPosition(arg_11_0, arg_11_1):
	if arg_11_1.x > 0 and arg_11_1.y > 0 and arg_11_1.x <= var_0_4 and arg_11_1.y <= var_0_5:
		return True

	return False

def var_0_0.printTable(arg_12_0):
	for iter_12_0, iter_12_1 in ipairs(arg_12_0.puzzlaItems):
		local var_12_0 = ""

		for iter_12_2, iter_12_3 in ipairs(iter_12_1):
			var_12_0 = var_12_0 .. iter_12_0 .. "-" .. iter_12_2 .. "-" .. iter_12_3.getCurrIndex() .. " "

		print(var_12_0)

def var_0_0.disorganizePuzzla(arg_13_0, arg_13_1):
	arg_13_0.paths = {}

	local function var_13_0()
		return

	if arg_13_1 and #arg_13_1 > 0:
		arg_13_0.orderDisorganize(arg_13_1, var_0_2, function(arg_15_0)
			arg_13_0.paths = arg_15_0

			var_13_0())
	else
		for iter_13_0 = 1, var_0_3:
			local var_13_1 = arg_13_0.disorganizeStep()

			table.insert(arg_13_0.paths, var_13_1)

			arg_13_0.prevDir = var_0_10[var_13_1]

		var_13_0()

def var_0_0.disorganizeStep(arg_16_0):
	local var_16_0 = arg_16_0.getBlockItem()

	local function var_16_1(arg_17_0)
		if arg_16_0.prevDir:
			return arg_16_0.prevDir == arg_17_0

		return False

	local var_16_2 = var_16_0.getSurroundPosition()
	local var_16_3 = {}

	for iter_16_0, iter_16_1 in ipairs(var_16_2):
		if arg_16_0.isValidPosition(iter_16_1) and not var_16_1(iter_16_0):
			table.insert(var_16_3, {
				pos = iter_16_1,
				dir = var_0_8[iter_16_0]
			})

	local var_16_4 = var_16_3[math.random(1, #var_16_3)]
	local var_16_5 = arg_16_0.getItemByPosition(var_16_4.pos)

	arg_16_0.swop(var_16_5, var_16_0)

	return var_16_4.dir

def var_0_0.printPaths(arg_18_0):
	local var_18_0 = ""

	for iter_18_0, iter_18_1 in ipairs(arg_18_0.paths or {}):
		var_18_0 = var_18_0 .. var_0_9[iter_18_1] .. ","

	print(var_18_0)

def var_0_0.decodePuzzla(arg_19_0, arg_19_1):
	local var_19_0 = {}

	for iter_19_0, iter_19_1 in ipairs(arg_19_1 or {}):
		local var_19_1 = var_0_10[iter_19_1]
		local var_19_2 = var_0_8[var_19_1]
		local var_19_3 = var_0_9[var_19_2]

		table.insert(var_19_0, 1, {
			dir = var_19_2,
			index = var_19_3
		})

	return var_19_0

def var_0_0.aotuDecode(arg_20_0):
	local var_20_0 = arg_20_0.decodePuzzla(arg_20_0.paths)
	local var_20_1 = {}

	for iter_20_0, iter_20_1 in ipairs(var_20_0):
		table.insert(var_20_1, iter_20_1.index)

	arg_20_0.revertPuzzla(var_20_1)

def var_0_0.printDecode(arg_21_0):
	local var_21_0 = arg_21_0.decodePuzzla(arg_21_0.paths)
	local var_21_1 = ""

	for iter_21_0, iter_21_1 in ipairs(var_21_0):
		var_21_1 = var_21_1 .. " - " .. iter_21_1.dir

	print(var_21_1)

def var_0_0.revertPuzzla(arg_22_0, arg_22_1):
	arg_22_0.orderDisorganize(arg_22_1, var_0_1)

def var_0_0.getBlockItem(arg_23_0):
	local var_23_0

	for iter_23_0, iter_23_1 in ipairs(arg_23_0.puzzlaItems):
		for iter_23_2, iter_23_3 in ipairs(iter_23_1):
			if iter_23_3.isBlock():
				var_23_0 = iter_23_3

				break

	return var_23_0

def var_0_0.orderDisorganize(arg_24_0, arg_24_1, arg_24_2, arg_24_3):
	local var_24_0 = {}

	arg_24_0.blockEvent = True

	local var_24_1 = arg_24_0.getBlockItem()
	local var_24_2 = {}

	local function var_24_3(arg_25_0)
		local var_25_0 = var_24_1.getSurroundPosition()[arg_25_0]
		local var_25_1 = arg_24_0.getItemByPosition(var_25_0)

		arg_24_0.swop(var_25_1, var_24_1)
		table.insert(var_24_0, var_0_8[arg_25_0])

	for iter_24_0, iter_24_1 in ipairs(arg_24_1):
		table.insert(var_24_2, function(arg_26_0)
			if arg_24_2 == 0:
				var_24_3(iter_24_1)
				arg_26_0()
			else
				arg_24_0.removeTimer()

				arg_24_0.delayTimer = Timer.New(function()
					arg_24_0.removeTimer()
					var_24_3(iter_24_1)
					arg_26_0(), arg_24_2, 1)

				arg_24_0.delayTimer.Start())

	seriesAsync(var_24_2, function()
		arg_24_0.blockEvent = None

		if arg_24_3:
			arg_24_3(var_24_0))

def var_0_0.isFinish(arg_29_0):
	for iter_29_0, iter_29_1 in ipairs(arg_29_0.puzzlaItems):
		for iter_29_2, iter_29_3 in ipairs(iter_29_1):
			assert(isa(iter_29_3, PuzzlaItem), "item should instance of PuzzlaItem")

			if not iter_29_3.isRestoration():
				return False

	return True

def var_0_0.removeTimer(arg_30_0):
	if arg_30_0.delayTimer:
		arg_30_0.delayTimer.Stop()

		arg_30_0.delayTimer = None

def var_0_0.dispose(arg_31_0):
	pg.DelegateInfo.Dispose(arg_31_0)
	arg_31_0.removeTimer()

return var_0_0
