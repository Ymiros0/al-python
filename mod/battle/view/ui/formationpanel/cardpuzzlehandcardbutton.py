ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig

var_0_0.Battle.CardPuzzleHandCardButton = class("CardPuzzleHandCardButton")

local var_0_2 = var_0_0.Battle.CardPuzzleHandCardButton

var_0_2.__name = "CardPuzzleHandCardButton"

def var_0_2.Ctor(arg_1_0, arg_1_1):
	arg_1_0._go = arg_1_1

	arg_1_0.init()

def var_0_2.SetCardInfo(arg_2_0, arg_2_1):
	arg_2_0._cardInfo = arg_2_1

	arg_2_0.updateCardView()

def var_0_2.UpdateTotalCost(arg_3_0):
	if arg_3_0._cardInfo:
		setText(arg_3_0._costTxt, arg_3_0._cardInfo.GetTotalCost())

def var_0_2.ConfigCallback(arg_4_0, arg_4_1):
	arg_4_0._callback = arg_4_1

def var_0_2.init(arg_5_0):
	arg_5_0._btnTF = arg_5_0._go.transform
	arg_5_0._icon = arg_5_0._btnTF.Find("skill_icon/unfill")
	arg_5_0._costTxt = arg_5_0._btnTF.Find("cost/cost_label")
	arg_5_0._cardName = arg_5_0._btnTF.Find("name")
	arg_5_0._cardType = arg_5_0._btnTF.Find("icon_bg")
	arg_5_0._cardTypeList = {}

	for iter_5_0 = 1, 3:
		table.insert(arg_5_0._cardTypeList, arg_5_0._cardType.Find("card_type_" .. iter_5_0))

	arg_5_0._cardRarity = arg_5_0._btnTF.Find("bg")
	arg_5_0._cardRarityList = {}

	for iter_5_1 = 0, 4:
		table.insert(arg_5_0._cardRarityList, arg_5_0._cardRarity.Find("rarity_" .. iter_5_1))

	arg_5_0._tag = arg_5_0._btnTF.Find("tag")

	GetComponent(arg_5_0._btnTF, "EventTriggerListener").AddPointUpFunc(function()
		if arg_5_0._cardInfo:
			arg_5_0._callback(arg_5_0._cardInfo))

def var_0_2.updateCardView(arg_7_0):
	if arg_7_0._cardInfo:
		setActive(arg_7_0._btnTF, True)
		setText(arg_7_0._costTxt, arg_7_0._cardInfo.GetTotalCost())
		setText(arg_7_0._cardName, arg_7_0._cardInfo.GetCardTemplate().name)
		setText(arg_7_0._tag, "词缀功能TODO")

		local var_7_0 = arg_7_0._cardInfo.GetRarity()
		local var_7_1 = arg_7_0._cardInfo.GetCardType()

		for iter_7_0, iter_7_1 in ipairs(arg_7_0._cardRarityList):
			setActive(iter_7_1, iter_7_0 == var_7_0 + 1)

		for iter_7_2, iter_7_3 in ipairs(arg_7_0._cardTypeList):
			setActive(iter_7_3, iter_7_2 == var_7_1)

		GetImageSpriteFromAtlasAsync("skillicon/" .. arg_7_0._cardInfo.GetIconID(), "", arg_7_0._icon)
	else
		setActive(arg_7_0._btnTF, False)

def var_0_2.Dispose(arg_8_0):
	return
