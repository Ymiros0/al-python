ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleDataFunction
local var_0_2 = class("BattleAirStrikeIconView")

var_0_0.Battle.BattleAirStrikeIconView = var_0_2
var_0_2.__name = "BattleAirStrikeIconView"
var_0_2.DEFAULT_ICON_NAME = "99shijianbao"

function var_0_2.Ctor(arg_1_0, arg_1_1)
	arg_1_0._iconList = {}

	arg_1_0:ConfigIconSkin(arg_1_1)
end

function var_0_2.ConfigIconSkin(arg_2_0, arg_2_1)
	arg_2_0._iconTpl = arg_2_1
	arg_2_0._iconContainer = arg_2_1.parent
end

function var_0_2.AppendIcon(arg_3_0, arg_3_1, arg_3_2)
	local var_3_0 = cloneTplTo(arg_3_0._iconTpl, arg_3_0._iconContainer).gameObject
	local var_3_1 = var_3_0.transform:Find("FighterIcon")

	var_3_0:SetActive(true)
	arg_3_0:setIconNumber(var_3_1, arg_3_2.totalNumber)

	local var_3_2 = var_0_1.GetAircraftTmpDataFromID(arg_3_2.templateID).icon or var_0_2.DEFAULT_ICON_NAME
	local var_3_3 = var_0_0.Battle.BattleResourceManager.GetInstance():GetAircraftIcon(var_3_2)

	setImageSprite(var_3_1, var_3_3)

	arg_3_0._iconList[arg_3_1] = var_3_0
end

function var_0_2.RemoveIcon(arg_4_0, arg_4_1, arg_4_2)
	local var_4_0 = arg_4_0._iconList[arg_4_1]

	if not var_4_0 then
		return
	end

	if arg_4_2.totalNumber <= 0 then
		Object.Destroy(var_4_0)

		arg_4_0._iconList[arg_4_1] = nil
	else
		arg_4_0:setIconNumber(var_4_0.transform:Find("FighterIcon"), arg_4_2.totalNumber)
	end
end

function var_0_2.Dispose(arg_5_0)
	for iter_5_0, iter_5_1 in pairs(arg_5_0._iconList) do
		Object.Destroy(iter_5_1)
	end

	arg_5_0._iconList = nil
end

function var_0_2.setIconNumber(arg_6_0, arg_6_1, arg_6_2)
	arg_6_1.transform:Find("FighterNum"):GetComponent(typeof(Text)).text = "X" .. arg_6_2
end
