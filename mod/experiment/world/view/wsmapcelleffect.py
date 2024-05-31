local var_0_0 = class("WSMapCellEffect", import(".WSMapEffect"))

var_0_0.Fields = {
	cell = "table",
	theme = "table"
}
var_0_0.Listeners = {
	onUpdate = "Update"
}

def var_0_0.GetName(arg_1_0, arg_1_1):
	return "cell_effect_" .. arg_1_0 .. "_" .. arg_1_1

def var_0_0.Setup(arg_2_0, arg_2_1, arg_2_2):
	assert(arg_2_0.cell == None)

	arg_2_0.cell = arg_2_1

	arg_2_0.cell.AddListener(WorldMapCell.EventUpdateInFov, arg_2_0.onUpdate)
	arg_2_0.cell.AddListener(WorldMapCell.EventUpdateDiscovered, arg_2_0.onUpdate)
	arg_2_0.cell.AddListener(WorldMapCell.EventUpdateFog, arg_2_0.onUpdate)

	arg_2_0.theme = arg_2_2

	var_0_0.super.Setup(arg_2_0, WorldConst.GetTerrainEffectRes(arg_2_0.cell.GetTerrain(), arg_2_0.cell.terrainDir, arg_2_0.cell.terrainStrong))
	arg_2_0.Load(function()
		local var_3_0 = arg_2_0.cell
		local var_3_1 = var_3_0.GetTerrain()

		if var_3_1 == WorldMapCell.TerrainStream:
			arg_2_0.SetModelOrder(WorldConst.LOEffectB, var_3_0.row)
		elif var_3_1 == WorldMapCell.TerrainWind:
			arg_2_0.SetModelOrder(WorldConst.LOEffectC, var_3_0.row)
			setActive(arg_2_0.model.GetChild(0).Find("Xyz/Arrow"), var_3_0.terrainStrong > 0)
			arg_2_0.UpdateModelScale(WorldConst.GetWindScale(var_3_0.terrainStrong))
		elif var_3_1 == WorldMapCell.TerrainIce:
			arg_2_0.SetModelOrder(WorldConst.LOEffectA, var_3_0.row)
		elif var_3_1 == WorldMapCell.TerrainPoison:
			arg_2_0.SetModelOrder(WorldConst.LOEffectA, var_3_0.row)

		arg_2_0.Init())

def var_0_0.Dispose(arg_4_0):
	arg_4_0.cell.RemoveListener(WorldMapCell.EventUpdateInFov, arg_4_0.onUpdate)
	arg_4_0.cell.RemoveListener(WorldMapCell.EventUpdateDiscovered, arg_4_0.onUpdate)
	arg_4_0.cell.RemoveListener(WorldMapCell.EventUpdateFog, arg_4_0.onUpdate)
	var_0_0.super.Dispose(arg_4_0)

def var_0_0.Init(arg_5_0):
	local var_5_0 = arg_5_0.cell
	local var_5_1 = arg_5_0.transform

	var_5_1.name = var_0_0.GetName(var_5_0.row, var_5_0.column)
	var_5_1.anchoredPosition3D = arg_5_0.theme.GetLinePosition(var_5_0.row, var_5_0.column)

	arg_5_0.Update()

def var_0_0.Update(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_0.cell

	if arg_6_1 == None or arg_6_1 == WorldMapCell.EventUpdateInFov or arg_6_1 == WorldMapCell.EventUpdateFog:
		setActive(arg_6_0.transform, var_6_0.GetInFOV() and not var_6_0.InFog())

return var_0_0
