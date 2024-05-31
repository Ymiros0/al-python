ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleUnitEvent
local var_0_2 = var_0_0.Battle.BattleEvent
local var_0_3 = var_0_0.Battle.BattleCardPuzzleEvent
local var_0_4 = var_0_0.Battle.BattleFormulas
local var_0_5 = var_0_0.Battle.BattleCardPuzzleFormulas
local var_0_6 = var_0_0.Battle.BattleConst
local var_0_7 = var_0_0.Battle.BattleConfig
local var_0_8 = var_0_0.Battle.BattleAttr
local var_0_9 = var_0_0.Battle.BattleDataFunction
local var_0_10 = var_0_0.Battle.BattleAttr
local var_0_11 = class("BattleCardPuzzleCard")

var_0_0.Battle.BattleCardPuzzleCard = var_0_11
var_0_11.__name = "BattleCardPuzzleCard"

def var_0_11.GetCardEffectConfig(arg_1_0):
	local var_1_0 = "card_" .. arg_1_0

	return pg.cardCfg[var_1_0]

def var_0_11.Ctor(arg_2_0, arg_2_1):
	arg_2_0._client = arg_2_1

	arg_2_0.init()

def var_0_11.init(arg_3_0):
	arg_3_0._timeStampList = {}

def var_0_11.SetCardTemplate(arg_4_0, arg_4_1):
	arg_4_0._cardID = arg_4_1
	arg_4_0._cardTemp = var_0_9.GetPuzzleCardDataTemplate(arg_4_0._cardID)

	local var_4_0 = var_0_11.GetCardEffectConfig(arg_4_0._cardTemp.effect[1])

	arg_4_0._iconID = arg_4_0._cardTemp.icon
	arg_4_0._cost = arg_4_0._cardTemp.cost
	arg_4_0._returnCost = var_4_0.shuffle_cost
	arg_4_0._labelList = arg_4_0._cardTemp.label
	arg_4_0._effectList = var_4_0.effect_list
	arg_4_0._shuffleEffectList = var_4_0.shuffle_effect_list

	arg_4_0.initCardEffectList()

	arg_4_0._extraCost = var_4_0.extra_cost
	arg_4_0._castCondition = var_4_0.cast_condition
	arg_4_0._boostCondition = var_4_0.boost_hint

def var_0_11.GetCardTemplate(arg_5_0):
	return arg_5_0._cardTemp

def var_0_11.GetCardID(arg_6_0):
	return arg_6_0._cardID

def var_0_11.GetRarity(arg_7_0):
	return arg_7_0._cardTemp.rarity

def var_0_11.GetCardType(arg_8_0):
	return arg_8_0._cardTemp.card_type

def var_0_11.GetCardCD(arg_9_0):
	return arg_9_0._cardTemp.cooldown

def var_0_11.GetLabels(arg_10_0):
	return arg_10_0._labelList

def var_0_11.GetCurrentPile(arg_11_0):
	return arg_11_0._currentPile

def var_0_11.SetCurrentPile(arg_12_0, arg_12_1):
	arg_12_0._currentPile = arg_12_1

def var_0_11.GetFromPile(arg_13_0):
	return arg_13_0._fromPile

def var_0_11.SetFromPile(arg_14_0, arg_14_1):
	arg_14_0._fromPile = arg_14_1

def var_0_11.LabelContain(arg_15_0, arg_15_1):
	for iter_15_0, iter_15_1 in ipairs(arg_15_1):
		if table.contains(arg_15_0._labelList, iter_15_1):
			return True

	return False

def var_0_11.GetCastCondition(arg_16_0):
	if not arg_16_0._castCondition:
		return None
	else
		return var_0_5.parseCompare(arg_16_0._castCondition, arg_16_0._client.GetAttrManager())

def var_0_11.GetBaseCost(arg_17_0):
	return arg_17_0._cost

def var_0_11.GetExtraCost(arg_18_0):
	if not arg_18_0._extraCost:
		return 0
	else
		return var_0_5.parseFormula(arg_18_0._extraCost, arg_18_0._client.GetAttrManager())

def var_0_11.GetTotalCost(arg_19_0):
	return math.max(arg_19_0.GetBaseCost() + arg_19_0.GetExtraCost(), 0)

def var_0_11.GetReturnCost(arg_20_0):
	return arg_20_0._returnCost

def var_0_11.IsBoost(arg_21_0):
	if not arg_21_0._boostCondition:
		return False
	else
		return var_0_5.parseCompare(arg_21_0._boostCondition, arg_21_0._client.GetAttrManager())

def var_0_11.GetIconID(arg_22_0):
	return arg_22_0._iconID

def var_0_11.GetMoveAfterCast(arg_23_0):
	return arg_23_0._moveAfterCaster

def var_0_11.SetBaseEnergyFillDuration(arg_24_0, arg_24_1):
	local var_24_0 = arg_24_1 + pg.TimeMgr.GetInstance().GetCombatTime()

	arg_24_0._timeStampList.energy = {
		duration = arg_24_1,
		timeStamp = var_24_0
	}

def var_0_11.SetOverHeatDuration(arg_25_0, arg_25_1):
	timeStamp = arg_25_1 + pg.TimeMgr.GetInstance().GetCombatTime()
	arg_25_0._timeStampList.overheat = {
		duration = arg_25_1,
		timeStamp = timeStamp
	}

def var_0_11.GetCastRemainRate(arg_26_0):
	local var_26_0 = 0
	local var_26_1 = 0

	for iter_26_0, iter_26_1 in pairs(arg_26_0._timeStampList):
		if var_26_1 < iter_26_1.timeStamp:
			var_26_0 = iter_26_1.duration
			var_26_1 = iter_26_1.timeStamp

	if var_26_0 != 0:
		return (var_26_1 - pg.TimeMgr.GetInstance().GetCombatTime()) / var_26_0
	else
		return 0

def var_0_11.Precast(arg_27_0, arg_27_1):
	arg_27_0._castCallback = arg_27_1

	if arg_27_0._holdForInputMark:
		arg_27_0._client.HoldForInput(arg_27_0)
	else
		arg_27_0.Cast()

def var_0_11.Cast(arg_28_0):
	arg_28_0.checkAndStartQueue(arg_28_0._queueList)

	if arg_28_0._castCallback:
		arg_28_0._castCallback()

def var_0_11.Retrun(arg_29_0, arg_29_1):
	arg_29_0.checkAndStartQueue(arg_29_0._returnQueueList)
	arg_29_1()

def var_0_11.Active(arg_30_0):
	arg_30_0.checkAndStartQueue(arg_30_0._queueList)

def var_0_11.SetInputPoint(arg_31_0, arg_31_1):
	arg_31_0._inputPoint = Clone(arg_31_1)

def var_0_11.GetInputPoint(arg_32_0):
	return arg_32_0._inputPoint

def var_0_11.GetClient(arg_33_0):
	return arg_33_0._client

def var_0_11.QueueFinish(arg_34_0, arg_34_1):
	local var_34_0 = arg_34_1.GetBranch()

	if var_34_0:
		local var_34_1 = {}

		for iter_34_0, iter_34_1 in pairs(var_34_0):
			if var_0_5.parseCompare(iter_34_1, arg_34_0._client.GetAttrManager()):
				var_34_1[iter_34_0] = True

		local var_34_2

		if arg_34_1.GetQueueType() == var_0_0.Battle.BattleCardPuzzleCardEffectQueue.QUEUE_TYPE_RETURN:
			local var_34_3 = arg_34_0._returnBranchQueueList
		else
			local var_34_4 = arg_34_0._branchQueueList

		for iter_34_2, iter_34_3 in pairs(var_34_1):
			arg_34_0._branchQueueList[iter_34_2].Start()

def var_0_11.initCardEffectList(arg_35_0):
	arg_35_0._holdForInputMark = False
	arg_35_0._moveAfterCaster = var_0_0.Battle.BattleFleetCardPuzzleComponent.CARD_PILE_INDEX_DISCARD
	arg_35_0._queueList, arg_35_0._branchQueueList = {}, {}

	for iter_35_0, iter_35_1 in ipairs(arg_35_0._effectList):
		local var_35_0 = var_0_0.Battle.BattleCardPuzzleCardEffectQueue.New(arg_35_0)

		var_35_0.ConfigData(iter_35_1)
		var_35_0.SetQueueType(var_0_0.Battle.BattleCardPuzzleCardEffectQueue.QUEUE_TYPE_NORMAL)
		table.insert(arg_35_0._queueList, var_35_0)

		if var_35_0.GetHoldForInputMark():
			arg_35_0._holdForInputMark = True

	for iter_35_2, iter_35_3 in pairs(arg_35_0._effectList):
		local var_35_1 = var_0_0.Battle.BattleCardPuzzleCardEffectQueue.New(arg_35_0)

		var_35_1.ConfigData(iter_35_3)
		var_35_1.SetQueueType(var_0_0.Battle.BattleCardPuzzleCardEffectQueue.QUEUE_TYPE_NORMAL)

		arg_35_0._branchQueueList[iter_35_2] = var_35_1

	if arg_35_0._returnCost:
		arg_35_0._returnQueueList, arg_35_0._returnBranchQueueList = {}, {}

		for iter_35_4, iter_35_5 in ipairs(arg_35_0._shuffleEffectList):
			local var_35_2 = var_0_0.Battle.BattleCardPuzzleCardEffectQueue.New(arg_35_0)

			var_35_2.ConfigData(iter_35_5)
			var_35_2.SetQueueType(var_0_0.Battle.BattleCardPuzzleCardEffectQueue.QUEUE_TYPE_RETURN)
			table.insert(arg_35_0._returnQueueList, var_35_2)

		for iter_35_6, iter_35_7 in pairs(arg_35_0._shuffleEffectList):
			local var_35_3 = var_0_0.Battle.BattleCardPuzzleCardEffectQueue.New(arg_35_0)

			var_35_3.ConfigData(iter_35_7)
			var_35_3.SetQueueType(var_0_0.Battle.BattleCardPuzzleCardEffectQueue.QUEUE_TYPE_RETURN)

			arg_35_0._returnBranchQueueList[iter_35_6] = var_35_3

def var_0_11.checkAndStartQueue(arg_36_0, arg_36_1):
	local var_36_0 = {}

	for iter_36_0, iter_36_1 in ipairs(arg_36_1):
		local var_36_1 = iter_36_1.GetCondition()

		if var_36_1 and not var_0_5.parseCompare(var_36_1, arg_36_0._client.GetAttrManager()):
			var_36_0[iter_36_0] = False
		else
			arg_36_0._moveAfterCaster = iter_36_1.GetMoveAfterCast()
			var_36_0[iter_36_0] = True

	for iter_36_2, iter_36_3 in pairs(var_36_0):
		if iter_36_3 == True:
			arg_36_1[iter_36_2].Start()

def var_0_11.GetCardEffectTargetFilterList(arg_37_0):
	local var_37_0 = {}

	for iter_37_0, iter_37_1 in ipairs(arg_37_0._effectList):
		if not iter_37_1.condition or var_0_5.parseCompare(iter_37_1.condition, arg_37_0._client.GetAttrManager()):
			arg_37_0.checkQueueTarget(iter_37_1, var_37_0)

	return var_37_0

var_0_11.AIM_FX_EFFECT = {
	"BattleCardPuzzleSkillFire"
}

def var_0_11.checkQueueTarget(arg_38_0, arg_38_1, arg_38_2):
	for iter_38_0, iter_38_1 in ipairs(arg_38_1):
		if table.contains(var_0_11.AIM_FX_EFFECT, iter_38_1.type) and iter_38_1.target_choise:
			local var_38_0 = arg_38_2[iter_38_1.caster] or {}

			table.insert(var_38_0, iter_38_1.target_choise)

			arg_38_2[iter_38_1.caster] = var_38_0

	if arg_38_1.branch:
		for iter_38_2, iter_38_3 in pairs(arg_38_1.branch):
			if var_0_5.parseCompare(iter_38_3, arg_38_0._client.GetAttrManager()):
				arg_38_0.checkQueueTarget(arg_38_0._effectList[iter_38_2])

def var_0_11.GetIconPath(arg_39_0):
	return CardPuzzleCard.GetCardIconPath(arg_39_0.GetCardTemplate().icon)

def var_0_11.GetType(arg_40_0):
	return arg_40_0.GetCardType()

def var_0_11.GetName(arg_41_0):
	return arg_41_0.GetCardTemplate().name

def var_0_11.GetDesc(arg_42_0):
	return arg_42_0.GetCardTemplate().discript

def var_0_11.GetCost(arg_43_0):
	return arg_43_0.GetTotalCost()

def var_0_11.GetKeywords(arg_44_0):
	return CardPuzzleCard.GetCardKeyWord(arg_44_0.GetCardTemplate().label)

def var_0_11.getConfig(arg_45_0, arg_45_1):
	return arg_45_0._cardTemp[arg_45_1]
