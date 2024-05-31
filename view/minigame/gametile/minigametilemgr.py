pg = pg or {}

local var_0_0 = pg

var_0_0.MiniGameTileMgr = singletonClass("MiniGameTileMgr")

local var_0_1 = var_0_0.MiniGameTileMgr

def var_0_1.Ctor(arg_1_0):
	arg_1_0.tileDatas = {}
	arg_1_0.tileDataDic = {}

	local var_1_0 = MiniGameTile.tiles

	for iter_1_0, iter_1_1 in pairs(var_1_0):
		local var_1_1 = MiniGameTileData.New(iter_1_1)

		table.insert(arg_1_0.tileDatas, var_1_1)

		arg_1_0.tileDataDic[iter_1_0] = var_1_1

def var_0_1.getData(arg_2_0, arg_2_1):
	return arg_2_0.tileDataDic[arg_2_1]

def var_0_1.getDataLayers(arg_3_0, arg_3_1, arg_3_2):
	local var_3_0 = arg_3_0.getData(arg_3_1)

	if var_3_0:
		return var_3_0.getTileDataLayer(arg_3_2)

	return None

def var_0_1.dumpDataLayers(arg_4_0, arg_4_1, arg_4_2, arg_4_3):
	local var_4_0 = arg_4_0.getData(arg_4_1)

	if var_4_0:
		var_4_0.dumpTileDataLayer(arg_4_2, arg_4_3)
