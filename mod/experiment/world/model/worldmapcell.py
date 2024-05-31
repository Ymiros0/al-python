local var_0_0 = class("WorldMapCell", import("...BaseEntity"))

var_0_0.Fields = {
	terrainDir = "number",
	discovered = "boolean",
	attachments = "table",
	fogSairen = "boolean",
	dir = "number",
	column = "number",
	walkable = "boolean",
	fog = "boolean",
	row = "number",
	infov = "number",
	terrain = "number",
	inLight = "number",
	terrainStrong = "number",
	fogLight = "boolean"
}
var_0_0.EventAddAttachment = "WorldMapCell.EventAddAttachment"
var_0_0.EventRemoveAttachment = "WorldMapCell.EventRemoveAttachment"
var_0_0.EventUpdateInFov = "WorldMapCell.EventUpdateInFov"
var_0_0.EventUpdateDiscovered = "WorldMapCell.EventUpdateDiscovered"
var_0_0.EventUpdateFog = "WorldMapCell.EventUpdateFog"
var_0_0.EventUpdateFogImage = "WorldMapCell.EventUpdateFogImage"
var_0_0.EventUpdateTerrain = "WorldMapCell.EventUpdateTerrain"

def var_0_0.GetName(arg_1_0, arg_1_1):
	return "cell_" .. arg_1_0 .. "_" .. arg_1_1

var_0_0.TerrainNone = 0
var_0_0.TerrainStream = 1
var_0_0.TerrainIce = 2
var_0_0.TerrainWind = 3
var_0_0.TerrainFog = 4
var_0_0.TerrainFire = 5
var_0_0.TerrainPoison = 6

def var_0_0.Build(arg_2_0):
	arg_2_0.attachments = {}
	arg_2_0.dir = 0
	arg_2_0.infov = 0
	arg_2_0.inLight = 0
	arg_2_0.fog = False
	arg_2_0.fogLight = False
	arg_2_0.fogSairen = False

def var_0_0.Setup(arg_3_0, arg_3_1):
	arg_3_0.row = arg_3_1[1]
	arg_3_0.column = arg_3_1[2]
	arg_3_0.walkable = arg_3_1[3]

def var_0_0.Dispose(arg_4_0):
	WPool.ReturnArray(arg_4_0.attachments)
	arg_4_0.Clear()

def var_0_0.AddAttachment(arg_5_0, arg_5_1):
	assert(not _.any(arg_5_0.attachments, function(arg_6_0)
		return arg_6_0.row == arg_5_1.row and arg_6_0.column == arg_5_1.column and arg_6_0.type == arg_5_1.type and arg_6_0.id == arg_5_1.id))
	assert(arg_5_1.row == arg_5_0.row and arg_5_1.column == arg_5_0.column)
	assert(WorldMapAttachment.SortOrder[arg_5_1.type], arg_5_1.type .. " . sort order not set.")

	local var_5_0 = WorldMapAttachment.SortOrder[arg_5_1.type]
	local var_5_1 = #arg_5_0.attachments + 1

	for iter_5_0, iter_5_1 in ipairs(arg_5_0.attachments):
		if var_5_0 > WorldMapAttachment.SortOrder[iter_5_1.type]:
			var_5_1 = iter_5_0

			break

	table.insert(arg_5_0.attachments, var_5_1, arg_5_1)
	arg_5_0.DispatchEvent(var_0_0.EventAddAttachment, arg_5_1)

	if not arg_5_0.discovered and arg_5_1.ShouldMarkAsLurk():
		arg_5_1.UpdateLurk(True)

def var_0_0.RemoveAttachment(arg_7_0, arg_7_1):
	if arg_7_1 == None or type(arg_7_1) == "number":
		arg_7_1 = arg_7_1 or #arg_7_0.attachments

		assert(arg_7_1 >= 1 and arg_7_1 <= #arg_7_0.attachments)

		local var_7_0 = arg_7_0.attachments[arg_7_1]

		table.remove(arg_7_0.attachments, arg_7_1)
		arg_7_0.DispatchEvent(var_0_0.EventRemoveAttachment, var_7_0)
		WPool.Return(var_7_0)
	elif arg_7_1.class == WorldMapAttachment:
		for iter_7_0 = #arg_7_0.attachments, 1, -1:
			if arg_7_0.attachments[iter_7_0] == arg_7_1:
				arg_7_0.RemoveAttachment(iter_7_0)

				break

def var_0_0.ContainsAttachment(arg_8_0, arg_8_1):
	return _.any(arg_8_0.attachments, function(arg_9_0)
		return arg_9_0 == arg_8_1)

def var_0_0.GetInFOV(arg_10_0):
	if arg_10_0.fog:
		return arg_10_0.fogLight
	else
		return arg_10_0.infov > 0 or arg_10_0.inLight > 0

def var_0_0.UpdateInFov(arg_11_0, arg_11_1):
	AfterCheck({
		{
			function()
				return arg_11_0.GetInFOV(),
			function()
				arg_11_0.DispatchEvent(var_0_0.EventUpdateInFov)
		}
	}, function()
		arg_11_0.infov = arg_11_1)

def var_0_0.ChangeInLight(arg_15_0, arg_15_1):
	AfterCheck({
		{
			function()
				return arg_15_0.GetInFOV(),
			function()
				arg_15_0.DispatchEvent(var_0_0.EventUpdateInFov)
		}
	}, function()
		arg_15_0.inLight = arg_15_0.inLight + (arg_15_1 and 1 or -1))

def var_0_0.InFog(arg_19_0):
	if arg_19_0.fog:
		return not arg_19_0.fogLight
	else
		return arg_19_0.GetTerrain() == var_0_0.TerrainFog

def var_0_0.LookSairenFog(arg_20_0):
	return arg_20_0.fogSairen or arg_20_0.IsTerrainSairenFog()

def var_0_0.UpdateFog(arg_21_0, arg_21_1, arg_21_2, arg_21_3):
	AfterCheck({
		{
			function()
				return arg_21_0.GetInFOV(),
			function()
				arg_21_0.DispatchEvent(var_0_0.EventUpdateInFov)
		},
		{
			function()
				return arg_21_0.InFog(),
			function()
				arg_21_0.DispatchEvent(var_0_0.EventUpdateFog)
		},
		{
			function()
				return arg_21_0.LookSairenFog(),
			function()
				arg_21_0.DispatchEvent(var_0_0.EventUpdateFogImage)
		}
	}, function()
		arg_21_0.fog = defaultValue(arg_21_1, arg_21_0.fog)
		arg_21_0.fogLight = defaultValue(arg_21_2, arg_21_0.fogLight)
		arg_21_0.fogSairen = defaultValue(arg_21_3, arg_21_0.fogSairen))

def var_0_0.UpdateDiscovered(arg_29_0, arg_29_1):
	if arg_29_0.discovered != arg_29_1:
		arg_29_0.discovered = arg_29_1

		arg_29_0.DispatchEvent(var_0_0.EventUpdateDiscovered)

def var_0_0.GetTerrain(arg_30_0):
	return arg_30_0.terrain or var_0_0.TerrainNone

def var_0_0.UpdateTerrain(arg_31_0, arg_31_1, arg_31_2, arg_31_3):
	AfterCheck({
		{
			function()
				return arg_31_0.InFog(),
			function()
				arg_31_0.DispatchEvent(var_0_0.EventUpdateFog)
		},
		{
			function()
				return arg_31_0.LookSairenFog(),
			function()
				arg_31_0.DispatchEvent(var_0_0.EventUpdateFogImage)
		}
	}, function()
		arg_31_0.terrain = arg_31_1

		if arg_31_0.terrain == var_0_0.TerrainStream:
			assert(arg_31_2)

			arg_31_0.terrainDir = arg_31_2
		elif arg_31_0.terrain == var_0_0.TerrainWind:
			assert(arg_31_2 and arg_31_3)

			arg_31_0.terrainDir = arg_31_2
			arg_31_0.terrainStrong = arg_31_3
		elif arg_31_0.terrain == var_0_0.TerrainFog:
			arg_31_0.terrainStrong = arg_31_3
		elif arg_31_0.terrain == var_0_0.TerrainPoison:
			arg_31_0.terrainStrong = arg_31_3

		arg_31_0.DispatchEvent(var_0_0.EventUpdateTerrain))

def var_0_0.GetAliveAttachments(arg_37_0):
	return _.filter(arg_37_0.attachments, function(arg_38_0)
		return arg_38_0.IsAlive())

def var_0_0.GetAliveAttachment(arg_39_0):
	return _.detect(arg_39_0.attachments, function(arg_40_0)
		return arg_40_0.IsAlive())

def var_0_0.GetDisplayAttachment(arg_41_0):
	return _.detect(arg_41_0.attachments, function(arg_42_0)
		return arg_42_0.IsAlive() and arg_42_0.IsVisible())

def var_0_0.GetInterativeAttachment(arg_43_0):
	return _.detect(arg_43_0.attachments, function(arg_44_0)
		return WorldMapAttachment.IsInteractiveType(arg_44_0.type) and arg_44_0.IsAlive() and arg_44_0.IsVisible())

def var_0_0.GetEventAttachment(arg_45_0):
	return _.detect(arg_45_0.attachments, function(arg_46_0)
		return arg_46_0.IsAlive() and arg_46_0.type == WorldMapAttachment.TypeEvent)

def var_0_0.GetCompassAttachment(arg_47_0):
	local var_47_0 = {}

	for iter_47_0, iter_47_1 in ipairs(arg_47_0.attachments):
		table.insert(var_47_0, iter_47_0)

	local var_47_1 = _.detect(_.sort(var_47_0, function(arg_48_0, arg_48_1)
		return (arg_47_0.attachments[arg_48_0].config.compass_index or 0) > (arg_47_0.attachments[arg_48_1].config.compass_index or 0)), function(arg_49_0)
		local var_49_0 = arg_47_0.attachments[arg_49_0]

		if var_49_0.ShouldMarkAsLurk():
			return var_49_0.IsAlive() and var_49_0.IsVisible() and arg_47_0.discovered
		elif var_49_0.type == WorldMapAttachment.TypeEvent:
			return var_49_0.IsAlive() and var_49_0.config.visuality == 0
		elif var_49_0.type != WorldMapAttachment.TypeFleet and var_49_0.type != WorldMapAttachment.TypePort:
			return var_49_0.IsAlive())

	return var_47_1 and arg_47_0.attachments[var_47_1]

def var_0_0.FindAliveAttachment(arg_50_0, arg_50_1):
	assert(arg_50_1 != None)

	return _.detect(arg_50_0.attachments, function(arg_51_0)
		return arg_51_0.IsAlive() and arg_51_0.type == arg_50_1)

def var_0_0.IsTerrainSairenFog(arg_52_0):
	return arg_52_0.terrain == var_0_0.TerrainFog and arg_52_0.terrainStrong == 0

def var_0_0.CanLeave(arg_53_0):
	return arg_53_0.walkable and arg_53_0.GetTerrainObstacleConfig("leave") and underscore.all(arg_53_0.attachments, function(arg_54_0)
		return not arg_54_0.IsAlive() or arg_54_0.CanLeave())

def var_0_0.CanArrive(arg_55_0):
	return arg_55_0.walkable and arg_55_0.GetTerrainObstacleConfig("arrive") and underscore.all(arg_55_0.attachments, function(arg_56_0)
		return not arg_56_0.IsAlive() or arg_56_0.CanArrive())

def var_0_0.CanPass(arg_57_0):
	return arg_57_0.walkable and arg_57_0.GetTerrainObstacleConfig("pass") and underscore.all(arg_57_0.attachments, function(arg_58_0)
		return not arg_58_0.IsAlive() or arg_58_0.CanPass())

def var_0_0.IsSign(arg_59_0):
	return _.any(arg_59_0.attachments, function(arg_60_0)
		return arg_60_0.IsAlive() and arg_60_0.IsSign())

def var_0_0.ExistEnemy(arg_61_0):
	return tobool(arg_61_0.GetStageEnemy())

def var_0_0.GetStageEnemy(arg_62_0):
	return _.detect(arg_62_0.attachments, function(arg_63_0)
		return arg_63_0.IsAlive() and WorldMapAttachment.IsEnemyType(arg_63_0.type))

def var_0_0.GetDisplayQuad(arg_64_0):
	local var_64_0
	local var_64_1 = arg_64_0.GetDisplayAttachment()

	if not arg_64_0.InFog() and var_64_1:
		if var_64_1.type == WorldMapAttachment.TypeEvent:
			local var_64_2 = var_64_1.config.object_icon

			if var_64_2 and #var_64_2 > 0:
				var_64_0 = var_64_2
		elif WorldMapAttachment.IsEnemyType(var_64_1.type):
			var_64_0 = {
				"cell_red"
			}
		elif var_64_1.type == WorldMapAttachment.TypePort or var_64_1.type == WorldMapAttachment.TypeBox:
			var_64_0 = {
				"cell_yellow"
			}

	return var_64_0

def var_0_0.GetEmotion(arg_65_0):
	return arg_65_0.terrain == var_0_0.TerrainPoison and WorldConst.PoisonEffect or None

def var_0_0.GetScannerAttachment(arg_66_0):
	local var_66_0 = arg_66_0.GetAliveAttachments()
	local var_66_1
	local var_66_2

	for iter_66_0, iter_66_1 in ipairs(var_66_0):
		local var_66_3 = iter_66_1.IsScannerAttachment()

		if var_66_3 and (not var_66_1 or var_66_2 < var_66_3):
			var_66_1 = iter_66_1
			var_66_2 = var_66_3

	return var_66_1

var_0_0.TerrainObstacleConfig = {
	SairenFog = 4,
	[var_0_0.TerrainNone] = 7,
	[var_0_0.TerrainStream] = 6,
	[var_0_0.TerrainIce] = 6,
	[var_0_0.TerrainWind] = 2,
	[var_0_0.TerrainFog] = 6,
	[var_0_0.TerrainFire] = 7,
	[var_0_0.TerrainPoison] = 7
}

def var_0_0.GetTerrainObstacleConfig(arg_67_0, arg_67_1):
	local var_67_0 = arg_67_0.IsTerrainSairenFog() and "SairenFog" or arg_67_0.GetTerrain()
	local var_67_1 = WorldConst.GetObstacleKey(arg_67_1)

	return bit.band(var_0_0.TerrainObstacleConfig[var_67_0], var_67_1) > 0

def var_0_0.IsMovingTerrain(arg_68_0):
	return arg_68_0 == var_0_0.TerrainStream or arg_68_0 == var_0_0.TerrainIce or arg_68_0 == var_0_0.TerrainWind

return var_0_0
