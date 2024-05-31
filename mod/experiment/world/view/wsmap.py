local var_0_0 = class("WSMap", import("...BaseEntity"))

var_0_0.Fields = {
	map = "table",
	rtQuads = "userdata",
	wsMapQuads = "table",
	wsMapArtifactsFA = "table",
	wsMapPath = "table",
	wsMapCells = "table",
	wsMapAttachments = "table",
	world = "table",
	rtTop = "userdata",
	rtTargetArrow = "userdata",
	rtItems = "userdata",
	rtEffectA = "userdata",
	wsTerrainEffects = "table",
	wsPool = "table",
	rtEffectB = "userdata",
	twTimerId = "number",
	wsMapArtifacts = "table",
	displayRangeTimer = "table",
	wsMapFleets = "table",
	transform = "userdata",
	wsMapResource = "table",
	twTimer = "userdata",
	rtCells = "userdata",
	displayRangeLines = "table",
	wsTimer = "table",
	wsMapItems = "table",
	transportDisplay = "number",
	wsCarryItems = "table",
	rangeVisible = "boolean",
	wsMapTransports = "table",
	rtEffectC = "userdata"
}
var_0_0.Listeners = {
	onRemoveCarry = "OnRemoveCarry",
	onUpdateAttachment = "OnUpdateAttachment",
	onUpdateTerrain = "OnUpdateTerrain",
	onUpdateFleetFOV = "OnUpdateFleetFOV",
	onAddAttachment = "OnAddAttachment",
	onRemoveAttachment = "OnRemoveAttachment",
	onAddCarry = "OnAddCarry"
}
var_0_0.EventUpdateEventTips = "WSMap.EventUpdateEventTips"

def var_0_0.Setup(arg_1_0, arg_1_1):
	arg_1_0.map = arg_1_1
	arg_1_0.wsMapQuads = {}
	arg_1_0.wsMapItems = {}
	arg_1_0.wsMapCells = {}
	arg_1_0.wsMapFleets = {}
	arg_1_0.wsMapArtifacts = {}
	arg_1_0.wsMapArtifactsFA = {}
	arg_1_0.wsMapTransports = {}
	arg_1_0.wsMapAttachments = {}
	arg_1_0.wsTerrainEffects = {}
	arg_1_0.wsCarryItems = {}
	arg_1_0.wsMapPath = WSMapPath.New()

	arg_1_0.wsMapPath.Setup(arg_1_0.map.theme)

	arg_1_0.wsMapResource = WSMapResource.New()

	arg_1_0.wsMapResource.Setup(arg_1_0.map)

	arg_1_0.transportDisplay = WorldConst.TransportDisplayNormal

	pg.DelegateInfo.New(arg_1_0)

def var_0_0.Dispose(arg_2_0):
	pg.DelegateInfo.Dispose(arg_2_0)
	arg_2_0.wsMapPath.Dispose()
	arg_2_0.ClearTargetArrow()
	arg_2_0.Unload()
	arg_2_0.Clear()

def var_0_0.Load(arg_3_0, arg_3_1):
	local var_3_0 = {}

	table.insert(var_3_0, function(arg_4_0)
		arg_3_0.InitPlane(arg_4_0))
	table.insert(var_3_0, function(arg_5_0)
		arg_3_0.wsMapResource.Load(arg_5_0))
	table.insert(var_3_0, function(arg_6_0)
		arg_3_0.InitClutter()
		arg_3_0.InitMap()
		arg_6_0())
	seriesAsync(var_3_0, arg_3_1)

def var_0_0.Unload(arg_7_0):
	arg_7_0.DisposeMap()
	arg_7_0.wsMapResource.Unload()

	if arg_7_0.transform:
		PoolMgr.GetInstance().ReturnPrefab("world/object/world_plane", "world_plane", arg_7_0.transform.gameObject, True)

		arg_7_0.transform = None

def var_0_0.InitPlane(arg_8_0, arg_8_1):
	PoolMgr.GetInstance().GetPrefab("world/object/world_plane", "world_plane", True, function(arg_9_0)
		arg_8_0.transform = arg_9_0.transform

		setActive(arg_8_0.transform, False)

		arg_8_0.rtQuads = arg_8_0.transform.Find("quads")
		arg_8_0.rtItems = arg_8_0.transform.Find("items")
		arg_8_0.rtCells = arg_8_0.transform.Find("cells")
		arg_8_0.rtTop = arg_8_0.transform.Find("top")
		arg_8_0.rtEffectA = arg_8_0.transform.Find("effect-a-1-999")
		arg_8_0.rtEffectB = arg_8_0.transform.Find("effect-b-1001-1999")
		arg_8_0.rtEffectC = arg_8_0.transform.Find("effect-c-2001-2999")

		local var_9_0 = arg_8_0.map

		assert(var_9_0 and var_9_0.active, "map not exist or map not active.")

		local var_9_1 = var_9_0.theme
		local var_9_2 = arg_8_0.transform

		var_9_2.name = "plane"
		var_9_2.anchoredPosition3D = Vector3(var_9_1.offsetx, var_9_1.offsety, var_9_1.offsetz) + WorldConst.DefaultMapOffset

		local var_9_3 = var_9_2.Find("display")
		local var_9_4 = var_9_3.Find("mask/sea")

		setImageAlpha(var_9_4, 0)
		GetSpriteFromAtlasAsync("chapter/pic/" .. var_9_1.assetSea, var_9_1.assetSea, function(arg_10_0)
			if var_9_4:
				setImageSprite(var_9_4, arg_10_0, False)
				setImageAlpha(var_9_4, 1))

		local var_9_5 = Vector2(10000, 10000)
		local var_9_6 = Vector2.zero
		local var_9_7 = Vector2(WorldConst.MaxColumn, WorldConst.MaxRow)
		local var_9_8 = Vector2(-WorldConst.MaxColumn, -WorldConst.MaxRow)

		for iter_9_0 = 0, WorldConst.MaxRow - 1:
			for iter_9_1 = 0, WorldConst.MaxColumn - 1:
				if var_9_0.GetCell(iter_9_0, iter_9_1):
					var_9_5.x = math.min(var_9_5.x, iter_9_1)
					var_9_5.y = math.min(var_9_5.y, WorldConst.MaxRow * 0.5 - iter_9_0 - 1)
					var_9_7.x = math.min(var_9_7.x, iter_9_1)
					var_9_7.y = math.min(var_9_7.y, iter_9_0)
					var_9_8.x = math.max(var_9_8.x, iter_9_1)
					var_9_8.y = math.max(var_9_8.y, iter_9_0)

		local var_9_9 = var_9_1.cellSize + var_9_1.cellSpace

		var_9_5.x = var_9_5.x * var_9_9.x
		var_9_5.y = var_9_5.y * var_9_9.y
		var_9_6.x = (var_9_8.x - var_9_7.x + 1) * var_9_9.x
		var_9_6.y = (var_9_8.y - var_9_7.y + 1) * var_9_9.y
		var_9_3.anchoredPosition = var_9_5 + var_9_6 * 0.5
		var_9_3.sizeDelta = var_9_6

		local var_9_10 = Vector2(math.floor(var_9_3.sizeDelta.x / var_9_9.x), math.floor(var_9_3.sizeDelta.y / var_9_9.y))
		local var_9_11 = var_9_3.Find("linev")
		local var_9_12 = var_9_11.GetChild(0)
		local var_9_13 = var_9_11.GetComponent(typeof(GridLayoutGroup))

		var_9_13.cellSize = Vector2(WorldConst.LineCross, var_9_3.sizeDelta.y)
		var_9_13.spacing = Vector2(var_9_9.x - WorldConst.LineCross, 0)
		var_9_13.padding.left = math.floor(var_9_13.spacing.x)

		for iter_9_2 = var_9_11.childCount - 1, math.max(var_9_10.x - 1, 0), -1:
			if iter_9_2 > 0:
				Destroy(var_9_11.GetChild(iter_9_2))

		for iter_9_3 = var_9_11.childCount, var_9_10.x - 2:
			Instantiate(var_9_12).transform.SetParent(var_9_11, False)

		local var_9_14 = var_9_3.Find("lineh")
		local var_9_15 = var_9_14.GetChild(0)
		local var_9_16 = var_9_14.GetComponent(typeof(GridLayoutGroup))

		var_9_16.cellSize = Vector2(var_9_3.sizeDelta.x, WorldConst.LineCross)
		var_9_16.spacing = Vector2(0, var_9_9.y - WorldConst.LineCross)
		var_9_16.padding.top = math.floor(var_9_16.spacing.y)

		for iter_9_4 = var_9_14.childCount - 1, math.max(var_9_10.y - 1, 0), -1:
			if iter_9_4 > 0:
				Destroy(var_9_14.GetChild(iter_9_4))

		for iter_9_5 = var_9_14.childCount, var_9_10.y - 2:
			Instantiate(var_9_15).transform.SetParent(var_9_14, False)

		arg_8_1())

def var_0_0.InitClutter(arg_11_0):
	arg_11_0.twTimer = LeanTween.value(arg_11_0.transform.gameObject, 1, 0, WorldConst.QuadBlinkDuration).setEase(LeanTweenType.easeInOutSine).setLoopPingPong()

	arg_11_0.wsTimer.AddInMapTween(arg_11_0.twTimer.uniqueId)
	arg_11_0.NewTargetArrow()

def var_0_0.InitMap(arg_12_0):
	local var_12_0 = arg_12_0.map
	local var_12_1 = var_12_0.theme
	local var_12_2 = _.values(var_12_0.cells)

	table.sort(var_12_2, function(arg_13_0, arg_13_1)
		return arg_13_0.row < arg_13_1.row or arg_13_0.row == arg_13_1.row and arg_13_0.column < arg_13_1.column)

	for iter_12_0, iter_12_1 in ipairs(var_12_2):
		local var_12_3 = arg_12_0.NewQuad(iter_12_1)

		arg_12_0.wsMapQuads[WSMapQuad.GetName(iter_12_1.row, iter_12_1.column)] = var_12_3

		local var_12_4 = arg_12_0.NewCell(iter_12_1)

		arg_12_0.wsMapCells[WSMapCell.GetName(iter_12_1.row, iter_12_1.column)] = var_12_4

	for iter_12_2, iter_12_3 in ipairs(var_12_0.config.float_items):
		local var_12_5 = iter_12_3[1]
		local var_12_6 = iter_12_3[2]
		local var_12_7 = var_12_0.GetCell(var_12_5, var_12_6)

		if var_12_7:
			local var_12_8 = arg_12_0.GetItem(var_12_5, var_12_6)

			if not var_12_8:
				var_12_8 = arg_12_0.NewItem(var_12_7)
				arg_12_0.wsMapItems[WSMapItem.GetName(var_12_7.row, var_12_7.column)] = var_12_8

			local var_12_9 = arg_12_0.NewArtifact(var_12_8, iter_12_3)

			table.insert(arg_12_0.wsMapArtifacts, var_12_9)

	for iter_12_4, iter_12_5 in ipairs(var_12_2):
		for iter_12_6, iter_12_7 in ipairs(iter_12_5.attachments):
			local var_12_10 = arg_12_0.GetCell(iter_12_7.row, iter_12_7.column)

			if iter_12_7.type == WorldMapAttachment.TypeArtifact:
				local var_12_11 = arg_12_0.GetItem(iter_12_5.row, iter_12_5.column)

				if not var_12_11:
					var_12_11 = arg_12_0.NewItem(iter_12_5)
					arg_12_0.wsMapItems[WSMapItem.GetName(iter_12_5.row, iter_12_5.column)] = var_12_11

				local var_12_12 = arg_12_0.NewArtifact(var_12_11, iter_12_7.GetArtifaceInfo(), iter_12_7)

				table.insert(arg_12_0.wsMapArtifactsFA, var_12_12)
			else
				local var_12_13 = arg_12_0.NewAttachment(var_12_10, iter_12_7)

				table.insert(arg_12_0.wsMapAttachments, var_12_13)

	for iter_12_8, iter_12_9 in ipairs(var_12_0.GetNormalFleets()):
		local var_12_14 = arg_12_0.NewFleet(iter_12_9)

		table.insert(arg_12_0.wsMapFleets, var_12_14)

		for iter_12_10, iter_12_11 in ipairs(iter_12_9.GetCarries()):
			local var_12_15 = arg_12_0.NewCarryItem(iter_12_9, iter_12_11)

			table.insert(arg_12_0.wsCarryItems, var_12_15)

	arg_12_0.FlushFleets()
	var_12_0.AddListener(WorldMap.EventUpdateFleetFOV, arg_12_0.onUpdateFleetFOV)

def var_0_0.DisposeMap(arg_14_0):
	arg_14_0.map.RemoveListener(WorldMap.EventUpdateFleetFOV, arg_14_0.onUpdateFleetFOV)
	_.each(arg_14_0.wsCarryItems, function(arg_15_0)
		arg_14_0.DisposeCarryItem(arg_15_0))

	arg_14_0.wsCarryItems = {}

	_.each(arg_14_0.wsMapFleets, function(arg_16_0)
		arg_14_0.DisposeFleet(arg_16_0))

	arg_14_0.wsMapFleets = {}

	_.each(arg_14_0.wsMapAttachments, function(arg_17_0)
		arg_14_0.DisposeAttachment(arg_17_0))

	arg_14_0.wsMapAttachments = {}

	_.each(arg_14_0.wsMapArtifacts, function(arg_18_0)
		arg_14_0.DisposeArtifact(arg_18_0))

	arg_14_0.wsMapArtifacts = {}

	for iter_14_0, iter_14_1 in pairs(arg_14_0.wsMapTransports):
		arg_14_0.DisposeTransport(iter_14_1)

	arg_14_0.wsMapTransports = {}

	_.each(arg_14_0.wsMapArtifactsFA, function(arg_19_0)
		arg_14_0.DisposeArtifact(arg_19_0))

	arg_14_0.wsMapArtifactsFA = {}

	for iter_14_2, iter_14_3 in pairs(arg_14_0.wsMapCells):
		arg_14_0.DisposeCell(iter_14_3)

	arg_14_0.wsMapCells = {}

	for iter_14_4, iter_14_5 in pairs(arg_14_0.wsMapItems):
		arg_14_0.DisposeItem(iter_14_5)

	arg_14_0.wsMapItems = {}

	for iter_14_6, iter_14_7 in pairs(arg_14_0.wsMapQuads):
		arg_14_0.DisposeQuad(iter_14_7)

	arg_14_0.wsMapQuads = {}

	for iter_14_8, iter_14_9 in ipairs(arg_14_0.wsTerrainEffects):
		arg_14_0.DisposeTerrainEffect(iter_14_9)

	arg_14_0.wsTerrainEffects = {}

def var_0_0.OnAddAttachment(arg_20_0, arg_20_1, arg_20_2, arg_20_3):
	local var_20_0 = arg_20_0.GetCell(arg_20_2.row, arg_20_2.column)

	assert(var_20_0, "cell not exist. " .. arg_20_2.row .. ", " .. arg_20_2.column)

	if arg_20_3.type == WorldMapAttachment.TypeArtifact:
		local var_20_1 = arg_20_0.GetItem(arg_20_2.row, arg_20_2.column)

		if not var_20_1:
			var_20_1 = arg_20_0.NewItem(arg_20_2)
			arg_20_0.wsMapItems[WSMapItem.GetName(arg_20_2.row, arg_20_2.column)] = var_20_1

		local var_20_2 = arg_20_0.NewArtifact(var_20_1, arg_20_3.GetArtifaceInfo(), arg_20_3)

		table.insert(arg_20_0.wsMapArtifactsFA, var_20_2)
	else
		local var_20_3 = arg_20_0.NewAttachment(var_20_0, arg_20_3)

		table.insert(arg_20_0.wsMapAttachments, var_20_3)
		arg_20_0.OnUpdateAttachment(None, arg_20_3)

def var_0_0.OnRemoveAttachment(arg_21_0, arg_21_1, arg_21_2, arg_21_3):
	if arg_21_3.type == WorldMapAttachment.TypeArtifact:
		for iter_21_0 = #arg_21_0.wsMapArtifactsFA, 1, -1:
			local var_21_0 = arg_21_0.wsMapArtifactsFA[iter_21_0]

			if var_21_0.attachment == arg_21_3:
				arg_21_0.DisposeArtifact(var_21_0)
				table.remove(arg_21_0.wsMapArtifactsFA, iter_21_0)

				break
	else
		for iter_21_1 = #arg_21_0.wsMapAttachments, 1, -1:
			local var_21_1 = arg_21_0.wsMapAttachments[iter_21_1]

			if var_21_1.attachment == arg_21_3:
				arg_21_0.DisposeAttachment(var_21_1)
				table.remove(arg_21_0.wsMapAttachments, iter_21_1)
				arg_21_0.OnUpdateAttachment(None, arg_21_3)

				break

def var_0_0.OnUpdateAttachment(arg_22_0, arg_22_1, arg_22_2):
	local var_22_0 = arg_22_0.FindAttachments(arg_22_2.row, arg_22_2.column)

	_.each(var_22_0, function(arg_23_0)
		arg_23_0.Update(arg_22_1))

	if arg_22_0.FindFleet(arg_22_2.row, arg_22_2.column):
		arg_22_0.FlushFleets()

	arg_22_0.DispatchEvent(var_0_0.EventUpdateEventTips)

def var_0_0.OnUpdateTerrain(arg_24_0, arg_24_1, arg_24_2):
	local var_24_0, var_24_1 = arg_24_0.GetTerrainEffect(arg_24_2.row, arg_24_2.column)

	if var_24_0:
		arg_24_0.DisposeTerrainEffect(var_24_0)
		table.remove(arg_24_0.wsTerrainEffects, var_24_1)

	local var_24_2 = arg_24_2.GetTerrain()

	if var_24_2 == WorldMapCell.TerrainStream or var_24_2 == WorldMapCell.TerrainWind or var_24_2 == WorldMapCell.TerrainIce or var_24_2 == WorldMapCell.TerrainPoison:
		local var_24_3 = arg_24_0.NewTerrainEffect(arg_24_2)

		table.insert(arg_24_0.wsTerrainEffects, var_24_3)

def var_0_0.OnAddCarry(arg_25_0, arg_25_1, arg_25_2, arg_25_3):
	local var_25_0 = arg_25_0.NewCarryItem(arg_25_2, arg_25_3)

	table.insert(arg_25_0.wsCarryItems, var_25_0)

def var_0_0.OnRemoveCarry(arg_26_0, arg_26_1, arg_26_2, arg_26_3):
	for iter_26_0 = #arg_26_0.wsCarryItems, 1, -1:
		local var_26_0 = arg_26_0.wsCarryItems[iter_26_0]

		if var_26_0.carryItem == arg_26_3:
			arg_26_0.DisposeCarryItem(var_26_0)
			table.remove(arg_26_0.wsCarryItems, iter_26_0)

			break

def var_0_0.OnUpdateFleetFOV(arg_27_0):
	arg_27_0.FlushFleets()

def var_0_0.NewQuad(arg_28_0, arg_28_1):
	local var_28_0 = WPool.Get(WSMapQuad)
	local var_28_1 = WSMapQuad.GetResName()

	var_28_0.transform = arg_28_0.wsPool.Get(var_28_1).transform

	var_28_0.transform.SetParent(arg_28_0.rtQuads, False)

	var_28_0.twTimer = arg_28_0.twTimer

	var_28_0.Setup(arg_28_1, arg_28_0.map.theme)

	return var_28_0

def var_0_0.DisposeQuad(arg_29_0, arg_29_1):
	local var_29_0 = WSMapQuad.GetResName()

	arg_29_0.wsPool.Return(var_29_0, arg_29_1.transform.gameObject)
	WPool.Return(arg_29_1)

def var_0_0.NewItem(arg_30_0, arg_30_1):
	local var_30_0 = WPool.Get(WSMapItem)
	local var_30_1 = WSMapItem.GetResName()

	var_30_0.transform = arg_30_0.wsPool.Get(var_30_1).transform

	var_30_0.transform.SetParent(arg_30_0.rtItems, False)
	var_30_0.Setup(arg_30_1, arg_30_0.map.theme)

	return var_30_0

def var_0_0.DisposeItem(arg_31_0, arg_31_1):
	local var_31_0 = WSMapItem.GetResName()

	arg_31_0.wsPool.Return(var_31_0, arg_31_1.transform.gameObject)
	WPool.Return(arg_31_1)

def var_0_0.NewCell(arg_32_0, arg_32_1):
	local var_32_0 = WPool.Get(WSMapCell)
	local var_32_1 = WSMapCell.GetResName()

	var_32_0.transform = arg_32_0.wsPool.Get(var_32_1).transform

	var_32_0.transform.SetParent(arg_32_0.rtCells, False)

	var_32_0.wsMapResource = arg_32_0.wsMapResource
	var_32_0.wsTimer = arg_32_0.wsTimer

	var_32_0.Setup(arg_32_0.map, arg_32_1)
	var_32_0.rtFog.SetParent(arg_32_0.rtCells.Find("fogs"), True)
	arg_32_1.AddListener(WorldMapCell.EventAddAttachment, arg_32_0.onAddAttachment)
	arg_32_1.AddListener(WorldMapCell.EventRemoveAttachment, arg_32_0.onRemoveAttachment)
	arg_32_1.AddListener(WorldMapCell.EventUpdateTerrain, arg_32_0.onUpdateTerrain)
	arg_32_0.OnUpdateTerrain(None, arg_32_1)

	return var_32_0

def var_0_0.DisposeCell(arg_33_0, arg_33_1):
	local var_33_0 = arg_33_1.cell

	arg_33_1.rtFog.SetParent(arg_33_1.transform, True)
	var_33_0.RemoveListener(WorldMapCell.EventAddAttachment, arg_33_0.onAddAttachment)
	var_33_0.RemoveListener(WorldMapCell.EventRemoveAttachment, arg_33_0.onRemoveAttachment)
	var_33_0.RemoveListener(WorldMapCell.EventUpdateTerrain, arg_33_0.onUpdateTerrain)

	local var_33_1 = WSMapCell.GetResName()

	arg_33_0.wsPool.Return(var_33_1, arg_33_1.transform.gameObject)
	WPool.Return(arg_33_1)

def var_0_0.NewTransport(arg_34_0, arg_34_1, arg_34_2, arg_34_3):
	local var_34_0 = WPool.Get(WSMapTransport)
	local var_34_1 = WSMapTransport.GetResName()

	var_34_0.transform = arg_34_0.wsPool.Get(var_34_1).transform

	var_34_0.transform.SetParent(arg_34_0.rtQuads, False)

	var_34_0.wsMapPath = arg_34_0.wsMapPath

	var_34_0.Setup(arg_34_1, arg_34_2, arg_34_3, arg_34_0.map)

	return var_34_0

def var_0_0.DisposeTransport(arg_35_0, arg_35_1):
	local var_35_0 = WSMapTransport.GetResName()

	arg_35_0.wsPool.Return(var_35_0, arg_35_1.transform.gameObject)
	WPool.Return(arg_35_1)

def var_0_0.NewAttachment(arg_36_0, arg_36_1, arg_36_2):
	local var_36_0 = WPool.Get(WSMapAttachment)
	local var_36_1 = WSMapAttachment.GetResName(arg_36_2)

	var_36_0.transform = arg_36_0.wsPool.Get(var_36_1).transform

	var_36_0.transform.SetParent(arg_36_1.rtAttachments, False)

	var_36_0.twTimer = arg_36_0.twTimer

	var_36_0.Setup(arg_36_0.map, arg_36_1.cell, arg_36_2)
	arg_36_2.AddListener(WorldMapAttachment.EventUpdateFlag, arg_36_0.onUpdateAttachment)
	arg_36_2.AddListener(WorldMapAttachment.EventUpdateData, arg_36_0.onUpdateAttachment)
	arg_36_2.AddListener(WorldMapAttachment.EventUpdateLurk, arg_36_0.onUpdateAttachment)

	return var_36_0

def var_0_0.DisposeAttachment(arg_37_0, arg_37_1):
	local var_37_0 = arg_37_1.attachment

	var_37_0.RemoveListener(WorldMapAttachment.EventUpdateFlag, arg_37_0.onUpdateAttachment)
	var_37_0.RemoveListener(WorldMapAttachment.EventUpdateData, arg_37_0.onUpdateAttachment)
	var_37_0.RemoveListener(WorldMapAttachment.EventUpdateLurk, arg_37_0.onUpdateAttachment)

	local var_37_1 = WSMapAttachment.GetResName(var_37_0)

	arg_37_0.wsPool.Return(var_37_1, arg_37_1.transform.gameObject)
	WPool.Return(arg_37_1)

def var_0_0.NewArtifact(arg_38_0, arg_38_1, arg_38_2, arg_38_3):
	local var_38_0 = WPool.Get(WSMapArtifact)

	var_38_0.transform.SetParent(arg_38_1.rtArtifacts, False)
	var_38_0.Setup(arg_38_2, arg_38_0.map.theme, arg_38_3)

	return var_38_0

def var_0_0.DisposeArtifact(arg_39_0, arg_39_1):
	WPool.Return(arg_39_1)

def var_0_0.GetTerrainEffectParent(arg_40_0, arg_40_1):
	if arg_40_1 == WorldMapCell.TerrainStream:
		return arg_40_0.rtEffectB
	elif arg_40_1 == WorldMapCell.TerrainWind:
		return arg_40_0.rtEffectC
	elif arg_40_1 == WorldMapCell.TerrainIce:
		return arg_40_0.rtEffectA
	elif arg_40_1 == WorldMapCell.TerrainPoison:
		return arg_40_0.rtEffectA
	else
		assert(False, "terrain type error. " .. arg_40_1)

def var_0_0.NewTerrainEffect(arg_41_0, arg_41_1):
	local var_41_0 = WPool.Get(WSMapCellEffect)

	var_41_0.transform = createNewGameObject("mapCellEffect")

	var_41_0.transform.SetParent(arg_41_0.GetTerrainEffectParent(arg_41_1.GetTerrain()), False)
	var_41_0.Setup(arg_41_1, arg_41_0.map.theme)

	return var_41_0

def var_0_0.DisposeTerrainEffect(arg_42_0, arg_42_1):
	local var_42_0 = arg_42_1.transform

	WPool.Return(arg_42_1)
	Destroy(var_42_0)

def var_0_0.GetTerrainEffect(arg_43_0, arg_43_1, arg_43_2):
	for iter_43_0, iter_43_1 in ipairs(arg_43_0.wsTerrainEffects):
		if iter_43_1.cell.row == arg_43_1 and iter_43_1.cell.column == arg_43_2:
			return iter_43_1, iter_43_0

def var_0_0.NewFleet(arg_44_0, arg_44_1):
	local var_44_0 = WPool.Get(WSMapFleet)
	local var_44_1 = WSMapFleet.GetResName()

	var_44_0.transform = arg_44_0.wsPool.Get(var_44_1).transform

	var_44_0.transform.SetParent(arg_44_0.rtCells, False)
	var_44_0.Setup(arg_44_1, arg_44_0.map.theme)
	var_44_0.rtRetreat.SetParent(arg_44_0.rtTop, False)
	arg_44_1.AddListener(WorldMapFleet.EventAddCarry, arg_44_0.onAddCarry)
	arg_44_1.AddListener(WorldMapFleet.EventRemoveCarry, arg_44_0.onRemoveCarry)

	return var_44_0

def var_0_0.DisposeFleet(arg_45_0, arg_45_1):
	arg_45_1.fleet.RemoveListener(WorldMapFleet.EventAddCarry, arg_45_0.onAddCarry)
	arg_45_1.fleet.RemoveListener(WorldMapFleet.EventRemoveCarry, arg_45_0.onRemoveCarry)
	arg_45_1.rtRetreat.SetParent(arg_45_1.transform, False)
	arg_45_0.wsPool.Return(WSMapFleet.GetResName(), arg_45_1.transform.gameObject)
	WPool.Return(arg_45_1)

def var_0_0.NewCarryItem(arg_46_0, arg_46_1, arg_46_2):
	local var_46_0 = WPool.Get(WSCarryItem)
	local var_46_1 = WSCarryItem.GetResName()

	var_46_0.transform = arg_46_0.wsPool.Get(var_46_1).transform

	var_46_0.transform.SetParent(arg_46_0.rtCells, False)
	var_46_0.Setup(arg_46_1, arg_46_2, arg_46_0.map.theme)

	return var_46_0

def var_0_0.DisposeCarryItem(arg_47_0, arg_47_1):
	arg_47_0.wsPool.Return(WSCarryItem.GetResName(), arg_47_1.transform.gameObject)
	WPool.Return(arg_47_1)

def var_0_0.GetCarryItem(arg_48_0, arg_48_1):
	return _.detect(arg_48_0.wsCarryItems, function(arg_49_0)
		return arg_49_0.carryItem == arg_48_1)

def var_0_0.FindCarryItems(arg_50_0, arg_50_1):
	return _.filter(arg_50_0.wsCarryItems, function(arg_51_0)
		return arg_51_0.fleet == arg_50_1)

def var_0_0.GetFleet(arg_52_0, arg_52_1):
	arg_52_1 = arg_52_1 or arg_52_0.map.GetFleet()

	return _.detect(arg_52_0.wsMapFleets, function(arg_53_0)
		return arg_53_0.fleet == arg_52_1)

def var_0_0.FindFleet(arg_54_0, arg_54_1, arg_54_2):
	return _.detect(arg_54_0.wsMapFleets, function(arg_55_0)
		return arg_55_0.fleet.row == arg_54_1 and arg_55_0.fleet.column == arg_54_2)

def var_0_0.GetCell(arg_56_0, arg_56_1, arg_56_2):
	local var_56_0 = WSMapCell.GetName(arg_56_1, arg_56_2)

	return arg_56_0.wsMapCells[var_56_0]

def var_0_0.GetAttachment(arg_57_0, arg_57_1, arg_57_2, arg_57_3):
	return _.detect(arg_57_0.wsMapAttachments, function(arg_58_0)
		return arg_58_0.attachment.row == arg_57_1 and arg_58_0.attachment.column == arg_57_2 and arg_58_0.attachment.type == arg_57_3)

def var_0_0.FindAttachments(arg_59_0, arg_59_1, arg_59_2):
	return _.filter(arg_59_0.wsMapAttachments, function(arg_60_0)
		return arg_60_0.attachment.row == arg_59_1 and arg_60_0.attachment.column == arg_59_2)

def var_0_0.GetQuad(arg_61_0, arg_61_1, arg_61_2):
	local var_61_0 = WSMapQuad.GetName(arg_61_1, arg_61_2)

	return arg_61_0.wsMapQuads[var_61_0]

def var_0_0.GetItem(arg_62_0, arg_62_1, arg_62_2):
	local var_62_0 = WSMapItem.GetName(arg_62_1, arg_62_2)

	return arg_62_0.wsMapItems[var_62_0]

def var_0_0.GetTransport(arg_63_0, arg_63_1, arg_63_2, arg_63_3):
	local var_63_0 = WSMapTransport.GetName(arg_63_1, arg_63_2, arg_63_3)

	return arg_63_0.wsMapTransports[var_63_0]

def var_0_0.UpdateRangeVisible(arg_64_0, arg_64_1):
	if arg_64_0.rangeVisible != arg_64_1:
		arg_64_0.rangeVisible = arg_64_1

		if arg_64_1:
			arg_64_0.DisplayMoveRange()
		else
			arg_64_0.HideMoveRange()

def var_0_0.DisplayMoveRange(arg_65_0):
	arg_65_0.displayRangeLines = {}

	local var_65_0 = arg_65_0.map.GetFleet()
	local var_65_1 = nowWorld().GetMoveRange(var_65_0)
	local var_65_2 = 0

	for iter_65_0, iter_65_1 in ipairs(var_65_1):
		local var_65_3 = arg_65_0.GetQuad(iter_65_1.row, iter_65_1.column)

		setImageAlpha(var_65_3.rtWalkQuad, math.pow(0.75, iter_65_1.stay and iter_65_1.stay - 1 or 0))
		setLocalScale(var_65_3.rtWalkQuad, Vector3.zero)

		local var_65_4 = ManhattonDist(var_65_0, iter_65_1)

		var_65_2 = math.max(var_65_2, var_65_4)

		local var_65_5 = {
			line = iter_65_1
		}

		function var_65_5.func()
			var_65_5.uid = LeanTween.scale(var_65_3.rtWalkQuad, Vector3.one, 0.2).setEase(LeanTweenType.easeInOutSine).uniqueId

			arg_65_0.wsTimer.AddInMapTween(var_65_5.uid)

		arg_65_0.displayRangeLines[var_65_4] = arg_65_0.displayRangeLines[var_65_4] or {}

		table.insert(arg_65_0.displayRangeLines[var_65_4], var_65_5)

	if var_65_2 > 0:
		local var_65_6 = 0

		arg_65_0.displayRangeTimer = arg_65_0.wsTimer.AddInMapTimer(function()
			var_65_6 = var_65_6 + 1

			if arg_65_0.displayRangeLines[var_65_6]:
				for iter_67_0, iter_67_1 in ipairs(arg_65_0.displayRangeLines[var_65_6]):
					iter_67_1.func(), 0.1, var_65_2)

		arg_65_0.displayRangeTimer.Start()

def var_0_0.HideMoveRange(arg_68_0):
	if arg_68_0.displayRangeTimer:
		arg_68_0.wsTimer.RemoveInMapTimer(arg_68_0.displayRangeTimer)

		arg_68_0.displayRangeTimer = None

	if arg_68_0.displayRangeLines:
		for iter_68_0, iter_68_1 in pairs(arg_68_0.displayRangeLines):
			for iter_68_2, iter_68_3 in ipairs(iter_68_1):
				if iter_68_3.uid:
					arg_68_0.wsTimer.RemoveInMapTween(iter_68_3.uid)

				local var_68_0 = iter_68_3.line
				local var_68_1 = arg_68_0.GetQuad(var_68_0.row, var_68_0.column)

				setImageAlpha(var_68_1.rtWalkQuad, 0)
				setLocalScale(var_68_1.rtWalkQuad, Vector3.one)

		arg_68_0.displayRangeLines = None

def var_0_0.MovePath(arg_69_0, arg_69_1, arg_69_2, arg_69_3, arg_69_4, arg_69_5):
	local var_69_0 = arg_69_0.map
	local var_69_1 = _.map(arg_69_2, function(arg_70_0)
		return arg_69_0.GetQuad(arg_70_0.row, arg_70_0.column))
	local var_69_2

	if arg_69_5:
		var_69_2 = WPool.Get(WSMapEffect)
		var_69_2.transform = createNewGameObject("mapEffect")

		var_69_2.transform.SetParent(arg_69_1.transform, False)

		var_69_2.transform.anchoredPosition3D = Vector3.zero
		var_69_2.transform.localEulerAngles = Vector3(arg_69_0.map.theme.angle, 0, 0)
		var_69_2.modelOrder = arg_69_1.modelOrder

		var_69_2.Setup(WorldConst.GetWindEffect())
		var_69_2.Load()

	local var_69_3 = 0

	for iter_69_0, iter_69_1 in ipairs(var_69_1):
		LeanTween.cancel(iter_69_1.rtWalkQuad)
		setLocalScale(iter_69_1.rtWalkQuad, Vector3.one)
		setImageAlpha(iter_69_1.rtWalkQuad, 0)
		LeanTween.alpha(iter_69_1.rtWalkQuad, 1, arg_69_2[iter_69_0].duration / 2).setDelay(var_69_3)

		var_69_3 = var_69_3 + arg_69_2[iter_69_0].duration / 2

	local var_69_4 = 0
	local var_69_5

	local function var_69_6(arg_71_0, arg_71_1, arg_71_2)
		var_69_4 = var_69_4 + 1

		if var_69_4 <= #var_69_1:
			local var_71_0 = var_69_1[var_69_4]

			LeanTween.cancel(var_71_0.rtWalkQuad)
			setImageAlpha(var_71_0.rtWalkQuad, 1)
			LeanTween.alpha(var_71_0.rtWalkQuad, 0, arg_69_2[var_69_4].duration)

	local var_69_7

	local function var_69_8()
		arg_69_0.wsMapPath.RemoveListener(WSMapPath.EventArrivedStep, var_69_6)
		arg_69_0.wsMapPath.RemoveListener(WSMapPath.EventArrived, var_69_8)
		_.each(var_69_1, function(arg_73_0)
			LeanTween.cancel(arg_73_0.rtWalkQuad)
			setImageAlpha(arg_73_0.rtWalkQuad, 0))

		if arg_69_5:
			local var_72_0 = var_69_2.transform

			WPool.Return(var_69_2)
			Destroy(var_72_0)

	arg_69_0.wsMapPath.AddListener(WSMapPath.EventArrivedStep, var_69_6)
	arg_69_0.wsMapPath.AddListener(WSMapPath.EventArrived, var_69_8)
	arg_69_0.wsMapPath.UpdateObject(arg_69_1)
	arg_69_0.wsMapPath.UpdateAction(arg_69_5 and WorldConst.ActionDrag or WorldConst.ActionMove)
	arg_69_0.wsMapPath.UpdateDirType(arg_69_4)
	arg_69_0.wsMapPath.StartMove(arg_69_3, arg_69_2, arg_69_5 and 100 or 0)

	return arg_69_0.wsMapPath

def var_0_0.FlushFleets(arg_74_0):
	arg_74_0.FlushFleetVisibility()
	arg_74_0.FlushFleetRetreatBtn()
	arg_74_0.FlushEnemyFightingMark()
	arg_74_0.FlushTransportDisplay()

	local var_74_0 = arg_74_0.map.GetFleet()

	_.each(arg_74_0.wsMapFleets, function(arg_75_0)
		arg_75_0.UpdateSelected(arg_75_0.fleet == var_74_0))

def var_0_0.FlushFleetRetreatBtn(arg_76_0):
	local var_76_0 = arg_76_0.map.GetFleet()

	_.each(arg_76_0.wsMapFleets, function(arg_77_0)
		local var_77_0 = arg_77_0.fleet
		local var_77_1 = arg_76_0.map.GetCell(var_77_0.row, var_77_0.column)
		local var_77_2 = var_77_1.ExistEnemy() and var_77_0 == var_76_0 and not WorldConst.IsWorldGuideEnemyId(var_77_1.GetStageEnemy().id)

		setActive(arg_77_0.rtRetreat, var_77_2)

		if var_77_2:
			arg_77_0.rtRetreat.localPosition = arg_76_0.rtTop.InverseTransformPoint(arg_77_0.transform.position) + Vector3(89, 0, 0)
			arg_77_0.rtRetreat.localEulerAngles = Vector3(-arg_76_0.map.theme.angle, 0, 0)

			arg_77_0.rtRetreat.SetAsLastSibling())

def var_0_0.FlushEnemyFightingMark(arg_78_0):
	_.each(arg_78_0.wsMapAttachments, function(arg_79_0)
		local var_79_0 = arg_79_0.attachment

		if WorldMapAttachment.IsEnemyType(var_79_0.type):
			arg_79_0.UpdateIsFighting(arg_78_0.map.ExistFleet(var_79_0.row, var_79_0.column)))

def var_0_0.FlushTransportVisibleByFleet(arg_80_0):
	for iter_80_0, iter_80_1 in pairs(arg_80_0.wsMapTransports):
		if not _.any(arg_80_0.wsMapFleets, function(arg_81_0)
			return ManhattonDist({
				row = arg_81_0.fleet.row,
				column = arg_81_0.fleet.column
			}, {
				row = iter_80_1.row,
				column = iter_80_1.column
			}) <= 1):
			arg_80_0.DisposeTransport(iter_80_1)

			arg_80_0.wsMapTransports[iter_80_0] = None

	_.each(arg_80_0.wsMapFleets, function(arg_82_0)
		for iter_82_0 = WorldConst.DirNone, WorldConst.DirLeft:
			local var_82_0 = WorldConst.DirToLine(iter_82_0)
			local var_82_1 = arg_80_0.map.GetCell(arg_82_0.fleet.row + var_82_0.row, arg_82_0.fleet.column + var_82_0.column)

			if var_82_1:
				for iter_82_1 = WorldConst.DirUp, WorldConst.DirLeft:
					if bit.band(var_82_1.dir, bit.lshift(1, iter_82_1)) > 0:
						local var_82_2 = WSMapTransport.GetName(var_82_1.row, var_82_1.column, iter_82_1)
						local var_82_3 = arg_80_0.wsMapTransports[var_82_2]

						if not var_82_3:
							var_82_3 = arg_80_0.NewTransport(var_82_1.row, var_82_1.column, iter_82_1)
							arg_80_0.wsMapTransports[var_82_2] = var_82_3

							setActive(var_82_3.rtClick, False)

						local var_82_4 = _.any(arg_80_0.wsMapFleets, function(arg_83_0)
							return arg_83_0.fleet.row == var_82_1.row and arg_83_0.fleet.column == var_82_1.column)

						var_82_3.UpdateAlpha(var_82_4 and 1 or 0)
						setActive(var_82_3.rtForbid, arg_80_0.map.config.is_transfer == 0))

def var_0_0.FlushFleetVisibility(arg_84_0):
	underscore.each(arg_84_0.wsMapFleets, function(arg_85_0)
		local var_85_0 = arg_85_0.fleet
		local var_85_1 = arg_84_0.map.GetCell(var_85_0.row, var_85_0.column)
		local var_85_2 = not var_85_1.ExistEnemy() and not var_85_1.InFog()

		arg_85_0.UpdateActive(var_85_2)
		_.each(arg_84_0.FindCarryItems(var_85_0), function(arg_86_0)
			arg_86_0.UpdateActive(var_85_2)))

def var_0_0.UpdateSubmarineSupport(arg_87_0):
	_.each(arg_87_0.wsMapFleets, function(arg_88_0)
		arg_88_0.UpdateSubmarineSupport())

def var_0_0.FlushMovingAttachment(arg_89_0, arg_89_1):
	if arg_89_1.transform.parent != arg_89_0.rtCells:
		arg_89_1.transform.SetParent(arg_89_0.rtCells, True)

	local var_89_0 = {
		row = arg_89_1.attachment.row,
		column = arg_89_1.attachment.column
	}

	if WorldMapAttachment.IsEnemyType(arg_89_1.attachment.type):
		local var_89_1 = arg_89_0.FindFleet(var_89_0.row, var_89_0.column)

		if var_89_1:
			var_89_1.UpdateActive(True)
			setActive(var_89_1.rtRetreat, False)
			arg_89_1.UpdateIsFighting(False)

	arg_89_0.FlushMovingAttachmentOrder(arg_89_1, var_89_0)

def var_0_0.FlushMovingAttachmentOrder(arg_90_0, arg_90_1, arg_90_2):
	local var_90_0 = arg_90_0.GetCell(arg_90_2.row, arg_90_2.column).cell

	setActive(arg_90_1.transform, var_90_0.GetInFOV() and not var_90_0.InFog())
	arg_90_1.SetModelOrder(arg_90_1.attachment.GetModelOrder(), arg_90_2.row)

def var_0_0.UpdateTransportDisplay(arg_91_0, arg_91_1):
	if arg_91_0.transportDisplay != arg_91_1:
		arg_91_0.transportDisplay = arg_91_1

		arg_91_0.FlushTransportDisplay()

def var_0_0.FlushTransportDisplay(arg_92_0):
	if arg_92_0.transportDisplay == WorldConst.TransportDisplayNormal:
		arg_92_0.FlushTransportVisibleByFleet()
	else
		arg_92_0.FlushTransportVisibleByState()

def var_0_0.FlushTransportVisibleByState(arg_93_0):
	local var_93_0 = arg_93_0.map.GetCellsInFOV()

	for iter_93_0, iter_93_1 in pairs(arg_93_0.wsMapTransports):
		if not _.any(var_93_0, function(arg_94_0)
			return arg_94_0.row == iter_93_1.row and arg_94_0.column == iter_93_1.column):
			arg_93_0.DisposeTransport(iter_93_1)

			arg_93_0.wsMapTransports[iter_93_0] = None

	local var_93_1 = WorldConst.DirUp

	_.each(var_93_0, function(arg_95_0)
		for iter_95_0 = var_93_1, WorldConst.DirLeft:
			if bit.band(arg_95_0.dir, bit.lshift(1, iter_95_0)) > 0:
				local var_95_0 = WSMapTransport.GetName(arg_95_0.row, arg_95_0.column, iter_95_0)
				local var_95_1 = arg_93_0.wsMapTransports[var_95_0]

				if not var_95_1:
					var_95_1 = arg_93_0.NewTransport(arg_95_0.row, arg_95_0.column, iter_95_0)
					arg_93_0.wsMapTransports[var_95_0] = var_95_1

				setActive(var_95_1.rtForbid, arg_93_0.transportDisplay == WorldConst.TransportDisplayGuideForbid)
				setActive(var_95_1.rtDanger, arg_93_0.transportDisplay == WorldConst.TransportDisplayGuideDanger)
				var_95_1.UpdateAlpha(1))

def var_0_0.NewTargetArrow(arg_96_0):
	arg_96_0.rtTargetArrow = arg_96_0.wsPool.Get("arrow_tpl").transform

	setActive(arg_96_0.rtTargetArrow, False)

def var_0_0.DisplayTargetArrow(arg_97_0, arg_97_1, arg_97_2):
	local var_97_0 = arg_97_0.GetCell(arg_97_1, arg_97_2)

	arg_97_0.rtTargetArrow.SetParent(var_97_0.transform, False)

	arg_97_0.rtTargetArrow.anchoredPosition = Vector2.zero
	arg_97_0.rtTargetArrow.localEulerAngles = Vector3(-arg_97_0.map.theme.angle, 0, 0)
	arg_97_0.rtTargetArrow.GetComponent(typeof(Canvas)).sortingOrder = WorldConst.LOFleet + defaultValue(arg_97_1, 0) * 10

	setActive(arg_97_0.rtTargetArrow, True)

def var_0_0.HideTargetArrow(arg_98_0):
	arg_98_0.rtTargetArrow.SetParent(arg_98_0.transform, False)
	setActive(arg_98_0.rtTargetArrow, False)

def var_0_0.ClearTargetArrow(arg_99_0):
	arg_99_0.wsPool.Return("arrow_tpl", arg_99_0.rtTargetArrow)

def var_0_0.ShowScannerMap(arg_100_0, arg_100_1):
	for iter_100_0, iter_100_1 in pairs(arg_100_0.wsMapQuads):
		if arg_100_1:
			iter_100_1.UpdateStatic(True, True)
		else
			iter_100_1.UpdateStatic(False)

return var_0_0
