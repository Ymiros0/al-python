ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig

var_0_0.Battle.CardPuzzleEnergyBar = class("CardPuzzleEnergyBar")

local var_0_2 = var_0_0.Battle.CardPuzzleEnergyBar

var_0_2.__name = "CardPuzzleEnergyBar"

def var_0_2.Ctor(arg_1_0, arg_1_1):
	arg_1_0._go = arg_1_1
	arg_1_0._tf = arg_1_0._go.transform
	arg_1_0._currentLabel = arg_1_0._tf.Find("count_label/count/current")
	arg_1_0._shadeLabel = arg_1_0._tf.Find("count_label/count/current")
	arg_1_0._maxLabel = arg_1_0._tf.Find("count_label/max")
	arg_1_0._recoverBlockList = arg_1_0._tf.Find("block_list")

def var_0_2.SetCardPuzzleComponent(arg_2_0, arg_2_1):
	arg_2_0._info = arg_2_1
	arg_2_0._energyInfo = arg_2_0._info.GetEnergy()
	arg_2_0._blockTFList = {}
	arg_2_0._max = arg_2_0._energyInfo.GetMaxEnergy()

	for iter_2_0 = 1, arg_2_0._max:
		local var_2_0 = arg_2_0._recoverBlockList.Find("block_" .. iter_2_0)
		local var_2_1 = var_2_0.Find("full")
		local var_2_2 = var_2_0.Find("recover")
		local var_2_3 = {
			full = var_2_1,
			recover = var_2_2
		}

		table.insert(arg_2_0._blockTFList, var_2_3)

	arg_2_0._lastPoint = 0

	local var_2_4 = arg_2_0._blockTFList[arg_2_0._lastPoint + 1]

	arg_2_0.activeRecoverBlock(var_2_4)

def var_0_2.Update(arg_3_0):
	arg_3_0.updateEnergyPoint()
	arg_3_0.updateEnergyProgress()

def var_0_2.updateEnergyProgress(arg_4_0):
	local var_4_0 = arg_4_0._energyInfo.GetCurrentEnergy()

	if arg_4_0._lastPoint == var_4_0:
		if var_4_0 >= arg_4_0._max:
			-- block empty
		else
			local var_4_1 = arg_4_0._blockTFList[var_4_0 + 1]

			arg_4_0.updateRecoverBlock(var_4_1)
	else
		local var_4_2 = arg_4_0._max
		local var_4_3 = arg_4_0._blockTFList

		for iter_4_0, iter_4_1 in ipairs(var_4_3):
			local var_4_4 = arg_4_0._blockTFList[iter_4_0]
			local var_4_5 = iter_4_0 - 1

			if var_4_5 < var_4_0:
				arg_4_0.updateSingleBlock(var_4_4, True)
			elif var_4_5 == var_4_0:
				arg_4_0.activeRecoverBlock(var_4_4)
				arg_4_0.updateRecoverBlock(var_4_4)
			elif var_4_0 < var_4_5:
				arg_4_0.updateSingleBlock(var_4_4, False)

	arg_4_0._lastPoint = var_4_0

def var_0_2.updateEnergyPoint(arg_5_0):
	setText(arg_5_0._currentLabel, arg_5_0._energyInfo.GetCurrentEnergy())
	setText(arg_5_0._shadeLabel, arg_5_0._energyInfo.GetCurrentEnergy())
	setText(arg_5_0._maxLabel, arg_5_0._energyInfo.GetMaxEnergy())

def var_0_2.activeRecoverBlock(arg_6_0, arg_6_1):
	setActive(arg_6_1.full, False)
	setActive(arg_6_1.recover, True)

def var_0_2.updateRecoverBlock(arg_7_0, arg_7_1):
	local var_7_0 = arg_7_1.full

	arg_7_1.recover.GetComponent(typeof(Image)).fillAmount = arg_7_0._energyInfo.GetGeneratingProcess()

def var_0_2.updateSingleBlock(arg_8_0, arg_8_1, arg_8_2):
	local var_8_0 = arg_8_1.full
	local var_8_1 = arg_8_1.recover

	setActive(var_8_0, arg_8_2)
	setActive(var_8_1, False)

def var_0_2.Dispose(arg_9_0):
	arg_9_0._currentLabel = None
	arg_9_0._maxLabel = None
	arg_9_0._recoverBlockList = None
