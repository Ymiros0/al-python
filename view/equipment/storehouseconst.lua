﻿local var_0_0 = class("StoreHouseConst")

var_0_0.WARP_TO_DESIGN = "WARP_TO_DESIGN"
var_0_0.WARP_TO_MATERIAL = "WARP_TO_MATERIAL"
var_0_0.WARP_TO_WEAPON = "WARP_TO_WEAPON"
var_0_0.OVERVIEW = "StoreHouseScene_OVERVIEW"
var_0_0.DESTROY = "StoreHouseScene_DESTROY"
var_0_0.EQUIPMENT = "StoreHouseScene_EQUIPMENT"
var_0_0.SKIN = "StoreHouseScene_SKIN"
var_0_0.SPWEAPON = "StoreHouseScene_SPWEAPON"
var_0_0.EQUIPMENT_INDEX_COMMON = {
	customPanels = {
		minHeight = 650,
		typeIndex = {
			mode = CustomIndexLayer.Mode.OR,
			options = IndexConst.EquipmentTypeIndexs,
			names = IndexConst.EquipmentTypeNames
		},
		equipPropertyIndex = {
			mode = CustomIndexLayer.Mode.OR,
			options = IndexConst.EquipPropertyIndexs,
			names = IndexConst.EquipPropertyNames
		},
		equipPropertyIndex2 = {
			mode = CustomIndexLayer.Mode.OR,
			options = IndexConst.EquipPropertyIndexs,
			names = IndexConst.EquipPropertyNames
		},
		equipAmmoIndex1 = {
			mode = CustomIndexLayer.Mode.OR,
			options = IndexConst.EquipAmmoIndexs_1,
			names = IndexConst.EquipAmmoIndexs_1_Names
		},
		equipAmmoIndex2 = {
			mode = CustomIndexLayer.Mode.OR,
			options = IndexConst.EquipAmmoIndexs_2,
			names = IndexConst.EquipAmmoIndexs_2_Names
		},
		equipCampIndex = {
			mode = CustomIndexLayer.Mode.AND,
			options = IndexConst.EquipCampIndexs,
			names = IndexConst.EquipCampNames
		},
		rarityIndex = {
			mode = CustomIndexLayer.Mode.AND,
			options = IndexConst.EquipmentRarityIndexs,
			names = IndexConst.RarityNames
		},
		extraIndex = {
			mode = CustomIndexLayer.Mode.OR,
			options = IndexConst.EquipmentExtraIndexs,
			names = IndexConst.EquipmentExtraNames
		}
	},
	groupList = {
		{
			dropdown = false,
			titleTxt = "indexsort_type",
			titleENTxt = "indexsort_typeeng",
			tags = {
				"typeIndex"
			}
		},
		{
			dropdown = true,
			titleTxt = "indexsort_index",
			titleENTxt = "indexsort_indexeng",
			tags = {
				"equipPropertyIndex",
				"equipPropertyIndex2",
				"equipAmmoIndex1",
				"equipAmmoIndex2"
			}
		},
		{
			dropdown = false,
			titleTxt = "indexsort_camp",
			titleENTxt = "indexsort_campeng",
			tags = {
				"equipCampIndex"
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
	dropdownLimit = {
		equipPropertyIndex = {
			include = {
				typeIndex = IndexConst.EquipmentTypeAll
			},
			exclude = {}
		},
		equipPropertyIndex2 = {
			include = {
				typeIndex = IndexConst.EquipmentTypeEquip
			},
			exclude = {
				typeIndex = IndexConst.EquipmentTypeAll
			}
		},
		equipAmmoIndex1 = {
			include = {
				typeIndex = IndexConst.BitAll({
					IndexConst.EquipmentTypeSmallCannon,
					IndexConst.EquipmentTypeMediumCannon,
					IndexConst.EquipmentTypeBigCannon
				})
			},
			exclude = {
				typeIndex = IndexConst.EquipmentTypeAll
			}
		},
		equipAmmoIndex2 = {
			include = {
				typeIndex = IndexConst.BitAll({
					IndexConst.EquipmentTypeWarshipTorpedo,
					IndexConst.EquipmentTypeSubmaraineTorpedo
				})
			},
			exclude = {
				typeIndex = IndexConst.EquipmentTypeAll
			}
		}
	}
}
var_0_0.SPWEAPON_INDEX_COMMON = {
	customPanels = {
		typeIndex = {
			mode = CustomIndexLayer.Mode.OR,
			options = IndexConst.SpWeaponTypeIndexs,
			names = IndexConst.SpWeaponTypeNames
		},
		rarityIndex = {
			mode = CustomIndexLayer.Mode.AND,
			options = IndexConst.SpWeaponRarityIndexs,
			names = IndexConst.SpWeaponRarityNames
		}
	},
	groupList = {
		{
			dropdown = false,
			titleTxt = "indexsort_type",
			titleENTxt = "indexsort_typeeng",
			tags = {
				"typeIndex"
			}
		},
		{
			dropdown = false,
			titleTxt = "indexsort_rarity",
			titleENTxt = "indexsort_rarityeng",
			tags = {
				"rarityIndex"
			}
		}
	}
}

return var_0_0
