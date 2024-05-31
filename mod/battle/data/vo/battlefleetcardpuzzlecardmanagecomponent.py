ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleUnitEvent
local var_0_2 = var_0_0.Battle.BattleEvent
local var_0_3 = var_0_0.Battle.BattleCardPuzzleEvent
local var_0_4 = var_0_0.Battle.BattleFormulas
local var_0_5 = var_0_0.Battle.BattleConst
local var_0_6 = var_0_0.Battle.BattleConfig
local var_0_7 = var_0_0.Battle.BattleAttr
local var_0_8 = var_0_0.Battle.BattleDataFunction
local var_0_9 = var_0_0.Battle.BattleAttr
local var_0_10 = class("BattleFleetCardPuzzleCardManageComponent")

var_0_0.Battle.BattleFleetCardPuzzleCardManageComponent = var_0_10
var_0_10.__name = "BattleFleetCardPuzzleCardManageComponent"
var_0_10.FUNC_NAME_SHUFFLE = "Shuffle"
var_0_10.FUNC_NAME_POP = "Pop"
var_0_10.FUNC_NAME_ADD = "Add"
var_0_10.FUNC_NAME_BOTTOM = "Bottom"
var_0_10.FUNC_NAME_REMOVE = "Remove"
var_0_10.FUNC_NAME_SEARCH = "Search"
var_0_10.FUNC_NAME_SORT = "Sort"
var_0_10.FUNC_NAME_GET_LENGTH = "GetLength"
var_0_10.SEARCH_BY_ID = "ID"
var_0_10.SEARCH_BY_LABEL = "LABEL"
var_0_10.SEARCH_BY_TYPE = "TYPE"

def var_0_10.AttachCardManager(arg_1_0):
	assert(arg_1_0.GetCardList != None, "该类>>" .. arg_1_0.__name .. "<<使用card puzzle卡牌管理组件需要支持接口>>GetCardList<<，并返回所有的卡牌列表")
	assert(arg_1_0.DispatchEvent != None, "该类>>" .. arg_1_0.__name .. "<<使用card puzzle卡牌管理组件需要事件派发组件")
	var_0_10.New(arg_1_0)

def var_0_10.DetachCardManager(arg_2_0):
	if arg_2_0._cardManager_ == None:
		return

	arg_2_0._cardManager_._destroy_()

	arg_2_0._cardManager_ = None

def var_0_10.Ctor(arg_3_0, arg_3_1):
	arg_3_0._target_ = arg_3_1

	arg_3_0._init_()

def var_0_10._init_(arg_4_0):
	arg_4_0._overrideAttachFunc(var_0_10.FUNC_NAME_SHUFFLE, var_0_10._shuffle_)
	arg_4_0._overrideAttachFunc(var_0_10.FUNC_NAME_POP, var_0_10._pop_)
	arg_4_0._overrideAttachFunc(var_0_10.FUNC_NAME_ADD, var_0_10._add_)
	arg_4_0._overrideAttachFunc(var_0_10.FUNC_NAME_BOTTOM, var_0_10._bottom_)
	arg_4_0._overrideAttachFunc(var_0_10.FUNC_NAME_REMOVE, var_0_10._remove_)
	arg_4_0._overrideAttachFunc(var_0_10.FUNC_NAME_SEARCH, var_0_10._search_)
	arg_4_0._overrideAttachFunc(var_0_10.FUNC_NAME_SORT, var_0_10._sort_)
	arg_4_0._overrideAttachFunc(var_0_10.FUNC_NAME_GET_LENGTH, var_0_10._getLength_)

def var_0_10._overrideAttachFunc(arg_5_0, arg_5_1, arg_5_2):
	if arg_5_0._target_[arg_5_1] != None:
		local var_5_0 = arg_5_0._target_[arg_5_1]

		local function var_5_1(...)
			var_5_0(...)
			arg_5_2(...)

		arg_5_0._target_[arg_5_1] = var_5_1
	else
		arg_5_0._target_[arg_5_1] = arg_5_2

def var_0_10._destroy_(arg_7_0):
	arg_7_0._target_ = None

def var_0_10._add_(arg_8_0, arg_8_1):
	local var_8_0 = arg_8_0.GetCardList()

	table.insert(var_8_0, arg_8_1)
	arg_8_1.SetCurrentPile(arg_8_0.GetIndexID())
	arg_8_0.DispatchEvent(var_0_0.Event.New(var_0_3.UPDATE_CARDS, {
		type = var_0_10.FUNC_NAME_ADD
	}))

def var_0_10._bottom_(arg_9_0, arg_9_1):
	local var_9_0 = arg_9_0.GetCardList()

	table.insert(var_9_0, 1, arg_9_1)
	arg_9_0.DispatchEvent(var_0_0.Event.New(var_0_3.UPDATE_CARDS, {
		type = var_0_10.FUNC_NAME_BOTTOM
	}))

def var_0_10._remove_(arg_10_0, arg_10_1):
	local var_10_0 = arg_10_0.GetCardList()

	for iter_10_0, iter_10_1 in ipairs(var_10_0):
		if arg_10_1 == iter_10_1:
			arg_10_1.SetFromPile(arg_10_0.GetIndexID())
			table.remove(var_10_0, iter_10_0)
			arg_10_0.DispatchEvent(var_0_0.Event.New(var_0_3.UPDATE_CARDS, {
				type = var_0_10.FUNC_NAME_REMOVE
			}))

			return

def var_0_10._shuffle_(arg_11_0):
	local var_11_0 = arg_11_0.GetCardList()
	local var_11_1 = arg_11_0.GetLength()

	while var_11_1 > 0:
		local var_11_2 = math.random(var_11_1)

		var_11_0[var_11_1], var_11_0[var_11_2] = var_11_0[var_11_2], var_11_0[var_11_1]
		var_11_1 = var_11_1 - 1

	arg_11_0.DispatchEvent(var_0_0.Event.New(var_0_3.UPDATE_CARDS, {
		type = var_0_10.FUNC_NAME_SHUFFLE
	}))

def var_0_10._pop_(arg_12_0):
	local var_12_0 = arg_12_0.GetCardList()
	local var_12_1 = table.remove(var_12_0, #var_12_0)

	var_12_1.SetFromPile(arg_12_0.GetIndexID())

	return var_12_1, arg_12_0.DispatchEvent(var_0_0.Event.New(var_0_3.UPDATE_CARDS, {
		type = var_0_10.FUNC_NAME_POP
	}))

def var_0_10._sort_(arg_13_0, arg_13_1):
	return

def var_0_10._search_(arg_14_0, arg_14_1):
	local var_14_0 = {}
	local var_14_1 = arg_14_0.GetCardList()
	local var_14_2 = arg_14_1.value
	local var_14_3 = arg_14_1.type

	if var_14_3 == var_0_10.SEARCH_BY_ID:
		for iter_14_0, iter_14_1 in ipairs(var_14_1):
			if table.contains(var_14_2, iter_14_1.GetCardID()):
				table.insert(var_14_0, iter_14_1)
	elif var_14_3 == var_0_10.SEARCH_BY_LABEL:
		for iter_14_2, iter_14_3 in ipairs(var_14_1):
			if iter_14_3.LabelContain(var_14_2):
				table.insert(var_14_0, iter_14_3)
	elif var_14_3 == var_0_10.SEARCH_BY_TYPE:
		for iter_14_4, iter_14_5 in ipairs(var_14_1):
			if iter_14_5.GetType() == var_14_2:
				table.insert(var_14_0, iter_14_5)

	if arg_14_1.total == True:
		return var_14_0
	else
		return {
			var_14_0[math.random(#var_14_0)]
		}

def var_0_10._getLength_(arg_15_0):
	return #arg_15_0.GetCardList()
