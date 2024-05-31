﻿local var_0_0 = class("SkinAtlasIndexLayer", import("...common.CustomIndexLayer"))

var_0_0.ExtraL2D = bit.lshift(1, 0)
var_0_0.ExtraDBG = bit.lshift(1, 1)
var_0_0.ExtraBG = bit.lshift(1, 2)
var_0_0.ExtraBGM = bit.lshift(1, 3)
var_0_0.ExtraCANTUSE = bit.lshift(1, 4)
var_0_0.ExtraUNUSE = bit.lshift(1, 5)
var_0_0.ExtraIndexs = {
	var_0_0.ExtraL2D,
	var_0_0.ExtraDBG,
	var_0_0.ExtraBG,
	var_0_0.ExtraBGM,
	var_0_0.ExtraCANTUSE,
	var_0_0.ExtraUNUSE
}
var_0_0.ExtraALL = IndexConst.BitAll(var_0_0.ExtraIndexs)

table.insert(var_0_0.ExtraIndexs, 1, var_0_0.ExtraALL)

var_0_0.ExtraNames = {
	"index_all",
	"index_L2D",
	"index_DBG",
	"index_BG",
	"index_BGM",
	"index_CANTUSE",
	"index_UNUSE"
}

local var_0_1 = {
	function()
		return true
	end,
	function(arg_2_0)
		return arg_2_0:IsLive2d()
	end,
	function(arg_3_0)
		return arg_3_0:IsDbg()
	end,
	function(arg_4_0)
		return arg_4_0:IsBG()
	end,
	function(arg_5_0)
		return arg_5_0:isBgm()
	end,
	function(arg_6_0)
		return arg_6_0:CantUse()
	end,
	function(arg_7_0)
		return arg_7_0:WithoutUse()
	end
}

function var_0_0.filterByExtra(arg_8_0, arg_8_1)
	if not arg_8_1 or arg_8_1 == var_0_0.ExtraALL then
		return true
	end

	for iter_8_0 = 2, #var_0_1 do
		local var_8_0 = bit.lshift(1, iter_8_0 - 2)

		if bit.band(var_8_0, arg_8_1) > 0 and var_0_1[iter_8_0](arg_8_0) then
			return true
		end
	end

	return false
end

function var_0_0.init(arg_9_0)
	var_0_0.super.init(arg_9_0)

	local var_9_0 = arg_9_0.contextData

	arg_9_0.OnFilter = var_9_0.OnFilter
	arg_9_0.indexDatas = var_9_0.defaultIndex or {}
end

function var_0_0.BlurPanel(arg_10_0)
	pg.UIMgr.GetInstance():BlurPanel(arg_10_0._tf, false, {
		weight = LayerWeightConst.SECOND_LAYER + 1
	})
end

function var_0_0.didEnter(arg_11_0)
	arg_11_0.contextData = arg_11_0:InitData()

	var_0_0.super.didEnter(arg_11_0)
end

function var_0_0.InitData(arg_12_0)
	return {
		indexDatas = Clone(arg_12_0.indexDatas),
		customPanels = {
			minHeight = 650,
			typeIndex = {
				blueSeleted = true,
				mode = CustomIndexLayer.Mode.AND,
				options = ShipIndexConst.TypeIndexs,
				names = ShipIndexConst.TypeNames
			},
			campIndex = {
				blueSeleted = true,
				mode = CustomIndexLayer.Mode.AND,
				options = ShipIndexConst.CampIndexs,
				names = ShipIndexConst.CampNames
			},
			rarityIndex = {
				blueSeleted = true,
				mode = CustomIndexLayer.Mode.AND,
				options = ShipIndexConst.RarityIndexs,
				names = ShipIndexConst.RarityNames
			},
			extraIndex = {
				blueSeleted = true,
				mode = CustomIndexLayer.Mode.AND,
				options = var_0_0.ExtraIndexs,
				names = var_0_0.ExtraNames
			},
			layoutPos = Vector2(0, -25)
		},
		groupList = {
			{
				dropdown = false,
				titleTxt = "indexsort_index",
				titleENTxt = "indexsort_indexeng",
				tags = {
					"typeIndex"
				}
			},
			{
				dropdown = false,
				titleTxt = "indexsort_camp",
				titleENTxt = "indexsort_campeng",
				tags = {
					"campIndex"
				}
			},
			{
				dropdown = false,
				titleTxt = "indexsort_rarity",
				titleENTxt = "indexsort_rarityeng",
				tags = {
					"rarityIndex"
				}
			},
			{
				dropdown = false,
				titleTxt = "indexsort_extraindex",
				titleENTxt = "indexsort_indexeng",
				tags = {
					"extraIndex"
				}
			}
		},
		callback = function(arg_13_0)
			arg_12_0.OnFilter(arg_13_0)
		end
	}
end

return var_0_0
