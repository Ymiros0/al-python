local var_0_0 = class("TechnologyConst")

var_0_0.OPEN_TECHNOLOGY_TREE_SCENE = "TechnologyConst.OPEN_TECHNOLOGY_TREE_SCENE"
var_0_0.OPEN_SHIP_BUFF_DETAIL = "TechnologyConst.OPEN_SHIP_BUFF_DETAIL"
var_0_0.OPEN_TECHNOLOGY_NATION_LAYER = "TechnologyConst.OPEN_TECHNOLOGY_NATION_LAYER"
var_0_0.CLOSE_TECHNOLOGY_NATION_LAYER = "TechnologyConst.CLOSE_TECHNOLOGY_NATION_LAYER"
var_0_0.CLOSE_TECHNOLOGY_NATION_LAYER_NOTIFICATION = "TechnologyConst.CLOSE_TECHNOLOGY_NATION_LAYER_NOTIFICATION"
var_0_0.OPEN_ALL_BUFF_DETAIL = "TechnologyConst.OPEN_ALL_BUFF_DETAIL"
var_0_0.UPDATE_REDPOINT_ON_TOP = "TechnologyConst.UPDATE_REDPOINT_ON_TOP"
var_0_0.CLICK_UP_TEC_BTN = "TechnologyConst.CLICK_UP_TEC_BTN"
var_0_0.START_TEC_BTN_SUCCESS = "TechnologyConst.START_TEC_BTN_SUCCESS"
var_0_0.FINISH_UP_TEC = "TechnologyConst.FINISH_UP_TEC"
var_0_0.FINISH_TEC_SUCCESS = "TechnologyConst.FINISH_TEC_SUCCESS"
var_0_0.GOT_TEC_CAMP_AWARD = "TechnologyConst.GOT_TEC_CAMP_AWARD"
var_0_0.GOT_TEC_CAMP_AWARD_ONESTEP = "TechnologyConst.GOT_TEC_CAMP_AWARD_ONESTEP"
var_0_0.SET_TEC_ATTR_ADDITION_FINISH = "TechnologyConst.SET_TEC_ATTR_ADDITION_FINISH"
var_0_0.SHIP_LEVEL_FOR_BUFF = 120
var_0_0.AtlasName = "ui/technologytreeui_atlas"
var_0_0.QUEUE_TOTAL_COUNT = 5
var_0_0.NationOrder = {
	Nation.US,
	Nation.EN,
	Nation.JP,
	Nation.DE,
	Nation.CN,
	Nation.SN,
	Nation.FF,
	Nation.MNF,
	Nation.ITA
}
var_0_0.NationResName = {
	"nation_all_",
	"nation_baiying_",
	"nation_huangjia_",
	"nation_chongying_",
	"nation_tiexue_",
	"nation_donghuang_",
	"nation_beilian_",
	"nation_ziyou_",
	"nation_weixi_",
	"nation_sading_"
}
var_0_0.TECH_NATION_ATTRS = {
	AttributeType.Durability,
	AttributeType.Cannon,
	AttributeType.Torpedo,
	AttributeType.AntiAircraft,
	AttributeType.Air,
	AttributeType.Reload,
	AttributeType.Armor,
	AttributeType.Hit,
	AttributeType.Dodge,
	AttributeType.Speed,
	AttributeType.Luck,
	AttributeType.AntiSub
}

def var_0_0.GetNationSpriteByIndex(arg_1_0):
	local var_1_0 = GetSpriteFromAtlas(var_0_0.AtlasName, var_0_0.NationResName[arg_1_0] .. "01")
	local var_1_1 = GetSpriteFromAtlas(var_0_0.AtlasName, var_0_0.NationResName[arg_1_0] .. "02")

	return var_1_0, var_1_1

var_0_0.TypeOrder = {
	{
		ShipType.QuZhu
	},
	{
		ShipType.QingXun
	},
	{
		ShipType.ZhongXun,
		ShipType.ChaoXun
	},
	{
		ShipType.QingHang,
		ShipType.ZhengHang
	},
	{
		ShipType.ZhanXun,
		ShipType.ZhanLie
	},
	{
		ShipType.QianTing,
		ShipType.QianMu
	},
	{
		ShipType.WeiXiu,
		ShipType.ZhongPao,
		ShipType.Yunshu,
		ShipType.HangZhan,
		ShipType.FengFanS,
		ShipType.FengFanV,
		ShipType.FengFanM
	}
}
var_0_0.TypeResName = {
	"type_qvzhu_",
	"type_qingxun_",
	"type_zhongxun_",
	"type_hangmu_",
	"type_zhanlie_",
	"type_qianting_",
	"type_other_",
	"type_all_"
}

def var_0_0.GetTypeSpriteByIndex(arg_2_0):
	local var_2_0 = GetSpriteFromAtlas(var_0_0.AtlasName, var_0_0.TypeResName[arg_2_0] .. "01")
	local var_2_1 = GetSpriteFromAtlas(var_0_0.AtlasName, var_0_0.TypeResName[arg_2_0] .. "02")

	return var_2_0, var_2_1

def var_0_0.ClassToGroupIDList():
	local var_3_0 = {}

	for iter_3_0, iter_3_1 in ipairs(pg.fleet_tech_ship_template.all):
		local var_3_1 = pg.fleet_tech_ship_template[iter_3_1].class

		if var_3_0[var_3_1]:
			table.insert(var_3_0[var_3_1], iter_3_1)
		else
			var_3_0[var_3_1] = {
				iter_3_1
			}

	return var_3_0

def var_0_0.GetOrderClassList():
	local var_4_0 = {}

	for iter_4_0, iter_4_1 in ipairs(pg.fleet_tech_ship_class.all):
		local var_4_1 = pg.fleet_tech_ship_class[iter_4_1].nation

		if var_4_1 != Nation.META and var_4_1 != Nation.MOT:
			table.insert(var_4_0, iter_4_1)

	local function var_4_2(arg_5_0, arg_5_1)
		local var_5_0 = pg.fleet_tech_ship_class[arg_5_0]
		local var_5_1 = pg.fleet_tech_ship_class[arg_5_1]
		local var_5_2

		if var_5_0.t_level == var_5_1.t_level:
			var_5_2 = var_5_0.t_level_1 > var_5_1.t_level_1
		else
			var_5_2 = var_5_0.t_level > var_5_1.t_level

		return var_5_2

	table.sort(var_4_0, var_4_2)

	return var_4_0

var_0_0.MetaClassConfig = None
var_0_0.MotClassConfig = None

def var_0_0.CreateMetaClassConfig():
	if var_0_0.MetaClassConfig or var_0_0.MotClassConfig:
		return

	for iter_6_0, iter_6_1 in ipairs(pg.fleet_tech_ship_class.all):
		local var_6_0 = pg.fleet_tech_ship_class[iter_6_1]
		local var_6_1 = var_6_0.nation

		if var_6_1 == Nation.META:
			if var_0_0.MetaClassConfig == None:
				var_0_0.MetaClassConfig = {}

			local var_6_2 = var_6_0.t_level
			local var_6_3 = "meta_class_t_level_" .. var_6_2

			if var_0_0.MetaClassConfig[var_6_3] == None:
				var_0_0.MetaClassConfig[var_6_3] = {}

			if var_0_0.MetaClassConfig[var_6_3].ships == None:
				var_0_0.MetaClassConfig[var_6_3].ships = {}

			local var_6_4 = i18n(var_6_3)
			local var_6_5 = var_6_0.t_level_1

			if var_0_0.MetaClassConfig[var_6_3].ships[var_6_5] == None:
				var_0_0.MetaClassConfig[var_6_3].ships[var_6_5] = {}

			if var_0_0.MetaClassConfig[var_6_3].indexList == None:
				var_0_0.MetaClassConfig[var_6_3].indexList = {}

			if not table.contains(var_0_0.MetaClassConfig[var_6_3].indexList, var_6_5):
				table.insert(var_0_0.MetaClassConfig[var_6_3].indexList, var_6_5)

			local var_6_6 = var_0_0.MetaClassConfig[var_6_3]

			var_6_6.id = var_6_3
			var_6_6.name = var_6_4
			var_6_6.nation = var_6_1
			var_6_6.t_level = var_6_2

			table.insert(var_6_6.ships[var_6_5], var_6_0.ships[1])
		elif var_6_1 == Nation.MOT:
			if var_0_0.MotClassConfig == None:
				var_0_0.MotClassConfig = {}

			local var_6_7 = var_6_0.t_level
			local var_6_8 = "mot_class_t_level_" .. var_6_7

			if var_0_0.MotClassConfig[var_6_8] == None:
				var_0_0.MotClassConfig[var_6_8] = {}

			if var_0_0.MotClassConfig[var_6_8].ships == None:
				var_0_0.MotClassConfig[var_6_8].ships = {}

			local var_6_9 = i18n(var_6_8)
			local var_6_10 = var_6_0.t_level_1

			if var_0_0.MotClassConfig[var_6_8].ships[var_6_10] == None:
				var_0_0.MotClassConfig[var_6_8].ships[var_6_10] = {}

			if var_0_0.MotClassConfig[var_6_8].indexList == None:
				var_0_0.MotClassConfig[var_6_8].indexList = {}

			if not table.contains(var_0_0.MotClassConfig[var_6_8].indexList, var_6_10):
				table.insert(var_0_0.MotClassConfig[var_6_8].indexList, var_6_10)

			local var_6_11 = var_0_0.MotClassConfig[var_6_8]

			var_6_11.id = var_6_8
			var_6_11.name = var_6_9
			var_6_11.nation = var_6_1
			var_6_11.t_level = var_6_7

			table.insert(var_6_11.ships[var_6_10], var_6_0.ships[1])

	if var_0_0.MetaClassConfig:
		for iter_6_2, iter_6_3 in pairs(var_0_0.MetaClassConfig):
			local var_6_12 = iter_6_3.indexList
			local var_6_13 = {}

			for iter_6_4, iter_6_5 in ipairs(var_6_12):
				_.each(iter_6_3.ships[iter_6_5], function(arg_7_0)
					table.insert(var_6_13, arg_7_0))

			iter_6_3.ships = var_6_13

	if var_0_0.MotClassConfig:
		for iter_6_6, iter_6_7 in pairs(var_0_0.MotClassConfig):
			local var_6_14 = iter_6_7.indexList
			local var_6_15 = {}

			for iter_6_8, iter_6_9 in ipairs(var_6_14):
				_.each(iter_6_7.ships[iter_6_9], function(arg_8_0)
					table.insert(var_6_15, arg_8_0))

			iter_6_7.ships = var_6_15

def var_0_0.GetOrderMetaClassList(arg_9_0):
	local var_9_0 = {}
	local var_9_1 = pg.gameset.meta_tech_sort.description
	local var_9_2 = {}

	for iter_9_0, iter_9_1 in ipairs(var_9_1):
		for iter_9_2, iter_9_3 in pairs(var_0_0.MetaClassConfig):
			if iter_9_1 == iter_9_3.t_level:
				table.insert(var_9_2, iter_9_3)

				break

	for iter_9_4, iter_9_5 in ipairs(var_9_2):
		local var_9_3 = iter_9_5.ships
		local var_9_4

		if not arg_9_0 or #arg_9_0 == 0:
			var_9_4 = var_9_3
		else
			var_9_4 = _.select(var_9_3, function(arg_10_0)
				local var_10_0 = var_0_0.GetShipTypeByGroupID(arg_10_0)

				return table.contains(arg_9_0, var_10_0))

		if #var_9_4 > 0:
			table.insert(var_9_0, iter_9_5.id)

	return var_9_0

def var_0_0.GetOrderMotClassList(arg_11_0):
	local var_11_0 = {}
	local var_11_1 = pg.gameset.tech_sort_mot.description
	local var_11_2 = {}

	for iter_11_0, iter_11_1 in ipairs(var_11_1):
		for iter_11_2, iter_11_3 in pairs(var_0_0.MotClassConfig):
			if iter_11_1 == iter_11_3.t_level:
				table.insert(var_11_2, iter_11_3)

				break

	for iter_11_4, iter_11_5 in ipairs(var_11_2):
		local var_11_3 = iter_11_5.ships
		local var_11_4

		if not arg_11_0 or #arg_11_0 == 0:
			var_11_4 = var_11_3
		else
			var_11_4 = _.select(var_11_3, function(arg_12_0)
				local var_12_0 = var_0_0.GetShipTypeByGroupID(arg_12_0)

				return table.contains(arg_11_0, var_12_0))

		if #var_11_4 > 0:
			table.insert(var_11_0, iter_11_5.id)

	return var_11_0

def var_0_0.GetMetaClassConfig(arg_13_0, arg_13_1):
	local var_13_0 = var_0_0.MetaClassConfig[arg_13_0]
	local var_13_1 = var_13_0.ships
	local var_13_2

	if not arg_13_1 or #arg_13_1 == 0:
		var_13_2 = var_13_1
	else
		var_13_2 = _.select(var_13_1, function(arg_14_0)
			local var_14_0 = var_0_0.GetShipTypeByGroupID(arg_14_0)

			return table.contains(arg_13_1, var_14_0))

	return {
		id = var_13_0.id,
		name = var_13_0.name,
		nation = var_13_0.nation,
		ships = var_13_2
	}

def var_0_0.GetMotClassConfig(arg_15_0, arg_15_1):
	local var_15_0 = var_0_0.MotClassConfig[arg_15_0]
	local var_15_1 = var_15_0.ships
	local var_15_2

	if not arg_15_1 or #arg_15_1 == 0:
		var_15_2 = var_15_1
	else
		var_15_2 = _.select(var_15_1, function(arg_16_0)
			local var_16_0 = var_0_0.GetShipTypeByGroupID(arg_16_0)

			return table.contains(arg_15_1, var_16_0))

	return {
		id = var_15_0.id,
		name = var_15_0.name,
		nation = var_15_0.nation,
		ships = var_15_2
	}

def var_0_0.GetShipTypeByGroupID(arg_17_0):
	local var_17_0 = pg.ship_data_group.get_id_list_by_group_type[arg_17_0][1]

	return pg.ship_data_group[var_17_0].type

return var_0_0
