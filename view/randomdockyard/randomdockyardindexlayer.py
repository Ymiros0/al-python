local var_0_0 = class("RandomDockYardIndexLayer", import("..common.CustomIndexLayer"))

def var_0_0.init(arg_1_0):
	var_0_0.super.init(arg_1_0)

	local var_1_0 = arg_1_0.contextData

	arg_1_0.OnFilter = var_1_0.OnFilter
	arg_1_0.indexDatas = var_1_0.defaultIndex or {}

def var_0_0.didEnter(arg_2_0):
	arg_2_0.contextData = arg_2_0.InitData()

	var_0_0.super.didEnter(arg_2_0)

def var_0_0.InitData(arg_3_0):
	return {
		indexDatas = Clone(arg_3_0.indexDatas),
		customPanels = {
			minHeight = 650,
			sortIndex = {
				isSort = True,
				mode = CustomIndexLayer.Mode.OR,
				options = ShipIndexConst.SortIndexs,
				names = ShipIndexConst.SortNames
			},
			sortPropertyIndex = {
				blueSeleted = True,
				mode = CustomIndexLayer.Mode.OR,
				options = ShipIndexConst.SortPropertyIndexs,
				names = ShipIndexConst.SortPropertyNames
			},
			typeIndex = {
				blueSeleted = True,
				mode = CustomIndexLayer.Mode.AND,
				options = ShipIndexConst.TypeIndexs,
				names = ShipIndexConst.TypeNames
			},
			campIndex = {
				blueSeleted = True,
				mode = CustomIndexLayer.Mode.AND,
				options = ShipIndexConst.CampIndexs,
				names = ShipIndexConst.CampNames
			},
			rarityIndex = {
				blueSeleted = True,
				mode = CustomIndexLayer.Mode.AND,
				options = ShipIndexConst.RarityIndexs,
				names = ShipIndexConst.RarityNames
			},
			extraIndex = {
				blueSeleted = True,
				mode = CustomIndexLayer.Mode.OR,
				options = ShipIndexConst.ExtraIndexs,
				names = ShipIndexConst.ExtraNames
			},
			layoutPos = Vector2(0, -25)
		},
		groupList = {
			{
				dropdown = False,
				titleTxt = "indexsort_sort",
				titleENTxt = "indexsort_sorteng",
				tags = {
					"sortIndex"
				},
				simpleDropdown = {
					"sortPropertyIndex"
				}
			},
			{
				dropdown = False,
				titleTxt = "indexsort_index",
				titleENTxt = "indexsort_indexeng",
				tags = {
					"typeIndex"
				}
			},
			{
				dropdown = False,
				titleTxt = "indexsort_camp",
				titleENTxt = "indexsort_campeng",
				tags = {
					"campIndex"
				}
			},
			{
				dropdown = False,
				titleTxt = "indexsort_rarity",
				titleENTxt = "indexsort_rarityeng",
				tags = {
					"rarityIndex"
				}
			},
			{
				dropdown = False,
				titleTxt = "indexsort_extraindex",
				titleENTxt = "indexsort_indexeng",
				tags = {
					"extraIndex"
				}
			}
		},
		def callback:(arg_4_0)
			arg_3_0.OnFilter(arg_4_0)
	}

return var_0_0
