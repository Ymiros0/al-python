ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = var_0_0.Battle.BattleDataFunction

var_0_0.Battle.CardPuzzleCardDetail = class("CardPuzzleCardDetail")

local var_0_3 = var_0_0.Battle.CardPuzzleCardDetail

var_0_3.__name = "CardPuzzleCardDetail"

function var_0_3.Ctor(arg_1_0, arg_1_1)
	arg_1_0._go = arg_1_1
	arg_1_0._tf = arg_1_0._go.transform
	arg_1_0._desc = arg_1_0._tf:Find("Desc")
	arg_1_0._affixList = arg_1_0._tf:Find("affixList")
	arg_1_0._affixContainer = arg_1_0._affixList:Find("container")
	arg_1_0._affixTpl = arg_1_0._tf:Find("tpl")
	arg_1_0._affixViewList = {}
	arg_1_0._bound = 960 - rtf(arg_1_0._tf).rect.width * 0.5
end

function var_0_3.Dispose(arg_2_0)
	arg_2_0._affixList = nil
	arg_2_0._affixContainer = nil
	arg_2_0._affixTpl = nil
	arg_2_0._desc = nil
	arg_2_0._tf = nil
	arg_2_0._go = nil
end

function var_0_3.Active(arg_3_0, arg_3_1)
	setActive(arg_3_0._go, arg_3_1)
end

function var_0_3.SetReferenceCard(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_1:GetCardInfo():GetCardID()
	local var_4_1 = var_0_2.GetPuzzleCardDataTemplate(var_4_0)

	setText(arg_4_0._desc, var_4_1.discript)

	local var_4_2 = #var_4_1.label
	local var_4_3 = 0

	while var_4_3 < var_4_2 do
		var_4_3 = var_4_3 + 1

		local var_4_4 = arg_4_0._affixViewList[var_4_3]

		if var_4_4 == nil then
			local var_4_5 = cloneTplTo(arg_4_0._affixTpl, arg_4_0._affixContainer)

			var_4_4 = var_0_0.Battle.CardPuzzleCardDetailAffix.New(var_4_5)

			table.insert(arg_4_0._affixViewList, var_4_4)
		end

		var_4_4:SetAffixID(var_4_1.label[var_4_3])
	end

	for iter_4_0, iter_4_1 in ipairs(arg_4_0._affixViewList) do
		local var_4_6 = iter_4_0 <= var_4_3

		iter_4_1:SetActive(var_4_6)
	end

	arg_4_0._pos = arg_4_0._pos or Vector3.New(0, 0, 0)

	local var_4_7 = arg_4_1:GetUIPos()

	if var_4_7.x > arg_4_0._bound then
		arg_4_0._pos.x = arg_4_0._bound
	else
		arg_4_0._pos.x = var_4_7.x
	end

	arg_4_0._pos.y = var_4_7.y + 130
	arg_4_0._tf.anchoredPosition = arg_4_0._pos
end
