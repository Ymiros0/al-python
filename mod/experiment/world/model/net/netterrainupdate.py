local var_0_0 = class("NetTerrainUpdate", import("....BaseEntity"))

var_0_0.Fields = {
	row = "number",
	terrain = "number",
	terrainDir = "number",
	column = "number",
	terrainStrong = "number"
}

def var_0_0.DebugPrint(arg_1_0):
	return "{" .. arg_1_0.row .. "," .. arg_1_0.column .. "} " .. arg_1_0.terrain

def var_0_0.Setup(arg_2_0, arg_2_1):
	arg_2_0.row = arg_2_1.pos.row
	arg_2_0.column = arg_2_1.pos.column
	arg_2_0.terrain = arg_2_1.type

	if arg_2_0.terrain == WorldMapCell.TerrainStream:
		arg_2_0.terrainDir = WorldConst.ParseConfigDir(arg_2_1.dir.row - 1, arg_2_1.dir.column - 1)
	elif arg_2_0.terrain == WorldMapCell.TerrainWind:
		arg_2_0.terrainDir = WorldConst.ParseConfigDir(arg_2_1.dir.row - 1, arg_2_1.dir.column - 1)
		arg_2_0.terrainStrong = arg_2_1.distance
	elif arg_2_0.terrain == WorldMapCell.TerrainFog:
		arg_2_0.terrainStrong = arg_2_1.distance
	elif arg_2_0.terrain == WorldMapCell.TerrainPoison:
		arg_2_0.terrainStrong = arg_2_1.distance

def var_0_0.GetTerrain(arg_3_0):
	return arg_3_0.terrain

return var_0_0
