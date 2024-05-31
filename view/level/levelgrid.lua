local var_0_0 = class("LevelGrid", import("..base.BasePanel"))
local var_0_1 = require("Mgr/Pool/PoolPlural")

var_0_0.MapDefaultPos = Vector3(420, -1000, -1000)

function var_0_0.init(arg_1_0)
	var_0_0.super.init(arg_1_0)

	arg_1_0.levelCam = GameObject.Find("LevelCamera"):GetComponent(typeof(Camera))
	GameObject.Find("LevelCamera/Canvas"):GetComponent(typeof(Canvas)).sortingOrder = ChapterConst.PriorityMin
	arg_1_0.quadTws = {}
	arg_1_0.presentTws = {}
	arg_1_0.markTws = {}
	arg_1_0.tweens = {}
	arg_1_0.markQuads = {}
	arg_1_0.pools = {}
	arg_1_0.edgePools = {}
	arg_1_0.poolParent = GameObject.Find("__Pool__")
	arg_1_0.opBtns = {}
	arg_1_0.itemCells = {}
	arg_1_0.attachmentCells = {}
	arg_1_0.extraAttachmentCells = {}
	arg_1_0.weatherCells = {}
	arg_1_0.onShipStepChange = nil
	arg_1_0.onShipArrived = nil
	arg_1_0.lastSelectedId = -1
	arg_1_0.quadState = -1
	arg_1_0.subTeleportTargetLine = nil
	arg_1_0.missileStrikeTargetLine = nil
	arg_1_0.cellEdges = {}
	arg_1_0.walls = {}
	arg_1_0.material_Add = LoadAny("ui/commonUI_atlas", "add", typeof(Material))
	arg_1_0.loader = AutoLoader.New()
end

function var_0_0.ExtendItem(arg_2_0, arg_2_1, arg_2_2)
	if IsNil(arg_2_0[arg_2_1]) then
		arg_2_0[arg_2_1] = arg_2_2
	end
end

function var_0_0.getFleetPool(arg_3_0, arg_3_1)
	local var_3_0 = "fleet_" .. arg_3_1
	local var_3_1 = arg_3_0.pools[var_3_0]

	if not var_3_1 then
		local var_3_2 = arg_3_0.shipTpl

		if arg_3_1 == FleetType.Submarine then
			var_3_2 = arg_3_0.subTpl
		elseif arg_3_1 == FleetType.Transport then
			var_3_2 = arg_3_0.transportTpl
		end

		var_3_1 = var_0_1.New(var_3_2.gameObject, 2)
		arg_3_0.pools[var_3_0] = var_3_1
	end

	return var_3_1
end

function var_0_0.getChampionPool(arg_4_0, arg_4_1)
	local var_4_0 = "champion_" .. arg_4_1
	local var_4_1 = arg_4_0.pools[var_4_0]

	if not var_4_1 then
		local var_4_2 = arg_4_0.championTpl

		if arg_4_1 == ChapterConst.TemplateOni then
			var_4_2 = arg_4_0.oniTpl
		elseif arg_4_1 == ChapterConst.TemplateEnemy then
			var_4_2 = arg_4_0.enemyTpl
		end

		var_4_1 = var_0_1.New(var_4_2.gameObject, 3)
		arg_4_0.pools[var_4_0] = var_4_1
	end

	return var_4_1
end

function var_0_0.AddEdgePool(arg_5_0, arg_5_1, arg_5_2, arg_5_3, arg_5_4, arg_5_5)
	if arg_5_0.edgePools[arg_5_1] then
		return
	end

	local var_5_0 = GameObject.New(arg_5_1)

	var_5_0:AddComponent(typeof(Image)).enabled = false
	arg_5_0.edgePools[arg_5_1] = var_0_1.New(var_5_0, 32)

	local var_5_1
	local var_5_2

	parallelAsync({
		function(arg_6_0)
			if not arg_5_3 then
				arg_6_0()

				return
			end

			arg_5_0.loader:LoadReference(arg_5_2, arg_5_3, typeof(Sprite), function(arg_7_0)
				var_5_1 = arg_7_0

				arg_6_0()
			end)
		end,
		function(arg_8_0)
			if not arg_5_5 then
				arg_8_0()

				return
			end

			arg_5_0.loader:LoadReference(arg_5_2, arg_5_5, typeof(Material), function(arg_9_0)
				var_5_2 = arg_9_0

				arg_8_0()
			end)
		end
	}, function()
		local function var_10_0(arg_11_0)
			local var_11_0 = go(arg_11_0):GetComponent(typeof(Image))

			var_11_0.enabled = true
			var_11_0.color = type(arg_5_4) == "table" and Color.New(unpack(arg_5_4)) or Color.white
			var_11_0.sprite = arg_5_3 and var_5_1 or nil
			var_11_0.material = arg_5_5 and var_5_2 or nil
		end

		local var_10_1 = arg_5_0.edgePools[arg_5_1]

		if var_10_1.prefab then
			var_10_0(var_10_1.prefab)
		end

		if var_10_1.items then
			for iter_10_0, iter_10_1 in pairs(var_10_1.items) do
				var_10_0(iter_10_1)
			end
		end

		if arg_5_0.cellEdges[arg_5_1] and next(arg_5_0.cellEdges[arg_5_1]) then
			for iter_10_2, iter_10_3 in pairs(arg_5_0.cellEdges[arg_5_1]) do
				var_10_0(iter_10_3)
			end
		end
	end)
end

function var_0_0.GetEdgePool(arg_12_0, arg_12_1)
	assert(arg_12_1, "Missing Key")

	local var_12_0 = arg_12_0.edgePools[arg_12_1]

	assert(var_12_0, "Must Create Pool before Using")

	return var_12_0
end

function var_0_0.initAll(arg_13_0, arg_13_1)
	seriesAsync({
		function(arg_14_0)
			arg_13_0:initPlane()
			arg_13_0:initDrag()
			onNextTick(arg_14_0)
		end,
		function(arg_15_0)
			if arg_13_0.exited then
				return
			end

			arg_13_0:initTargetArrow()
			arg_13_0:InitDestinationMark()
			onNextTick(arg_15_0)
		end,
		function(arg_16_0)
			if arg_13_0.exited then
				return
			end

			for iter_16_0 = 0, ChapterConst.MaxRow - 1 do
				for iter_16_1 = 0, ChapterConst.MaxColumn - 1 do
					arg_13_0:initCell(iter_16_0, iter_16_1)
				end
			end

			arg_13_0:UpdateItemCells()
			arg_13_0:updateQuadCells(ChapterConst.QuadStateFrozen)
			onNextTick(arg_16_0)
		end,
		function(arg_17_0)
			if arg_13_0.exited then
				return
			end

			arg_13_0:AddEdgePool("SubmarineHunting", "ui/commonUI_atlas", "white_dot", {
				1,
				0,
				0
			}, "add")
			arg_13_0:UpdateFloor()
			arg_13_0:updateAttachments()
			arg_13_0:InitWalls()
			arg_13_0:InitIdolsAnim()
			onNextTick(arg_17_0)
		end,
		function(arg_18_0)
			if arg_13_0.exited then
				return
			end

			parallelAsync({
				function(arg_19_0)
					arg_13_0:initFleets(arg_19_0)
				end,
				function(arg_20_0)
					arg_13_0:initChampions(arg_20_0)
				end
			}, arg_18_0)
		end,
		function()
			arg_13_0:OnChangeSubAutoAttack()
			arg_13_0:updateQuadCells(ChapterConst.QuadStateNormal)
			existCall(arg_13_1)
		end
	})
end

function var_0_0.clearAll(arg_22_0)
	for iter_22_0, iter_22_1 in pairs(arg_22_0.tweens) do
		LeanTween.cancel(iter_22_0)
	end

	table.clear(arg_22_0.tweens)
	arg_22_0.loader:Clear()

	if not IsNil(arg_22_0.cellRoot) then
		arg_22_0:clearFleets()
		arg_22_0:clearChampions()
		arg_22_0:clearTargetArrow()
		arg_22_0:ClearDestinationMark()
		arg_22_0:ClearIdolsAnim()

		for iter_22_2, iter_22_3 in pairs(arg_22_0.itemCells) do
			iter_22_3:Clear()
		end

		table.clear(arg_22_0.itemCells)

		for iter_22_4, iter_22_5 in pairs(arg_22_0.attachmentCells) do
			iter_22_5:Clear()
		end

		table.clear(arg_22_0.attachmentCells)

		for iter_22_6, iter_22_7 in pairs(arg_22_0.extraAttachmentCells) do
			iter_22_7:Clear()
		end

		table.clear(arg_22_0.extraAttachmentCells)

		for iter_22_8, iter_22_9 in pairs(arg_22_0.weatherCells) do
			iter_22_9:Clear()
		end

		table.clear(arg_22_0.weatherCells)

		for iter_22_10 = 0, ChapterConst.MaxRow - 1 do
			for iter_22_11 = 0, ChapterConst.MaxColumn - 1 do
				arg_22_0:clearCell(iter_22_10, iter_22_11)
			end
		end

		for iter_22_12, iter_22_13 in pairs(arg_22_0.walls) do
			iter_22_13:Clear()
		end

		table.clear(arg_22_0.walls)
		arg_22_0:clearPlane()
	end

	arg_22_0.material_Add = nil

	for iter_22_14, iter_22_15 in pairs(arg_22_0.edgePools) do
		iter_22_15:Clear()
	end

	arg_22_0.edgePools = nil

	for iter_22_16, iter_22_17 in pairs(arg_22_0.pools) do
		iter_22_17:ClearItems()
	end

	arg_22_0.pools = nil
	GetOrAddComponent(arg_22_0._tf, "EventTriggerListener").enabled = false

	if arg_22_0.dragTrigger then
		ClearEventTrigger(arg_22_0.dragTrigger)

		arg_22_0.dragTrigger = nil
	end

	LeanTween.cancel(arg_22_0._tf)
end

local var_0_2 = 640

function var_0_0.initDrag(arg_23_0)
	local var_23_0, var_23_1, var_23_2 = getSizeRate()
	local var_23_3 = arg_23_0.contextData.chapterVO
	local var_23_4 = var_23_3.theme
	local var_23_5 = var_23_2 * 0.5 / math.tan(math.deg2Rad * var_23_4.fov * 0.5)
	local var_23_6 = math.deg2Rad * var_23_4.angle
	local var_23_7 = Vector3(0, -math.sin(var_23_6), -math.cos(var_23_6))
	local var_23_8 = Vector3(var_23_4.offsetx, var_23_4.offsety, var_23_4.offsetz) + var_0_0.MapDefaultPos
	local var_23_9 = Vector3.Dot(var_23_7, var_23_8)
	local var_23_10 = var_23_0 * math.clamp((var_23_5 - var_23_9) / var_23_5, 0, 1)
	local var_23_11 = arg_23_0.plane:Find("display").anchoredPosition
	local var_23_12 = var_0_2 - var_23_8.x - var_23_11.x
	local var_23_13 = var_0_0.MapDefaultPos.y - var_23_8.y - var_23_11.y
	local var_23_14, var_23_15, var_23_16, var_23_17 = var_23_3:getDragExtend()

	arg_23_0.leftBound = var_23_12 - var_23_15
	arg_23_0.rightBound = var_23_12 + var_23_14
	arg_23_0.topBound = var_23_13 + var_23_17
	arg_23_0.bottomBound = var_23_13 - var_23_16
	arg_23_0._tf.sizeDelta = Vector2(var_23_1 * 2, var_23_2 * 2)
	arg_23_0.dragTrigger = GetOrAddComponent(arg_23_0._tf, "EventTriggerListener")
	arg_23_0.dragTrigger.enabled = true

	arg_23_0.dragTrigger:AddDragFunc(function(arg_24_0, arg_24_1)
		local var_24_0 = arg_23_0._tf.anchoredPosition

		var_24_0.x = math.clamp(var_24_0.x + arg_24_1.delta.x * var_23_10.x, arg_23_0.leftBound, arg_23_0.rightBound)
		var_24_0.y = math.clamp(var_24_0.y + arg_24_1.delta.y * var_23_10.y / math.cos(var_23_6), arg_23_0.bottomBound, arg_23_0.topBound)
		arg_23_0._tf.anchoredPosition = var_24_0
	end)
end

function var_0_0.initPlane(arg_25_0)
	local var_25_0 = arg_25_0.contextData.chapterVO
	local var_25_1 = var_25_0.theme

	arg_25_0.levelCam.fieldOfView = var_25_1.fov

	local var_25_2

	PoolMgr.GetInstance():GetPrefab("chapter/plane", "", false, function(arg_26_0)
		var_25_2 = arg_26_0.transform
	end)

	arg_25_0.plane = var_25_2
	var_25_2.name = ChapterConst.PlaneName

	var_25_2:SetParent(arg_25_0._tf, false)

	var_25_2.anchoredPosition3D = Vector3(var_25_1.offsetx, var_25_1.offsety, var_25_1.offsetz) + var_0_0.MapDefaultPos
	arg_25_0.cellRoot = var_25_2:Find("cells")
	arg_25_0.quadRoot = var_25_2:Find("quads")
	arg_25_0.bottomMarkRoot = var_25_2:Find("buttomMarks")
	arg_25_0.topMarkRoot = var_25_2:Find("topMarks")
	arg_25_0.restrictMap = var_25_2:Find("restrictMap")
	arg_25_0.UIFXList = var_25_2:Find("UI_FX_list")

	for iter_25_0 = 1, arg_25_0.UIFXList.childCount do
		local var_25_3 = arg_25_0.UIFXList:GetChild(iter_25_0 - 1)

		setActive(var_25_3, false)
	end

	local var_25_4 = arg_25_0.UIFXList:Find(var_25_0:getConfig("uifx"))

	if var_25_4 then
		setActive(var_25_4, true)
	end

	local var_25_5 = var_25_0:getConfig("chapter_fx")

	if type(var_25_5) == "table" then
		for iter_25_1, iter_25_2 in pairs(var_25_5) do
			if #iter_25_1 <= 0 then
				return
			end

			arg_25_0.loader:GetPrefab("effect/" .. iter_25_1, iter_25_1, function(arg_27_0)
				setParent(arg_27_0, arg_25_0.UIFXList)

				if iter_25_2.offset then
					tf(arg_27_0).localPosition = Vector3(unpack(iter_25_2.offset))
				end

				if iter_25_2.rotation then
					tf(arg_27_0).localRotation = Quaternion.Euler(unpack(iter_25_2.rotation))
				end
			end)
		end
	end

	local var_25_6 = var_25_2:Find("display")
	local var_25_7 = var_25_6:Find("mask/sea")

	GetImageSpriteFromAtlasAsync("chapter/pic/" .. var_25_1.assetSea, var_25_1.assetSea, var_25_7)

	arg_25_0.indexMin, arg_25_0.indexMax = var_25_0.indexMin, var_25_0.indexMax

	local var_25_8 = Vector2(arg_25_0.indexMin.y, ChapterConst.MaxRow * 0.5 - arg_25_0.indexMax.x - 1)
	local var_25_9 = Vector2(arg_25_0.indexMax.y - arg_25_0.indexMin.y + 1, arg_25_0.indexMax.x - arg_25_0.indexMin.x + 1)
	local var_25_10 = var_25_1.cellSize + var_25_1.cellSpace
	local var_25_11 = Vector2.Scale(var_25_8, var_25_10)
	local var_25_12 = Vector2.Scale(var_25_9, var_25_10)

	var_25_6.anchoredPosition = var_25_11 + var_25_12 * 0.5
	var_25_6.sizeDelta = var_25_12
	arg_25_0.restrictMap.anchoredPosition = var_25_11 + var_25_12 * 0.5
	arg_25_0.restrictMap.sizeDelta = var_25_12

	local var_25_13 = Vector2(math.floor(var_25_6.sizeDelta.x / var_25_10.x), math.floor(var_25_6.sizeDelta.y / var_25_10.y))
	local var_25_14 = var_25_6:Find("ABC")
	local var_25_15 = var_25_14:GetChild(0)
	local var_25_16 = var_25_14:GetComponent(typeof(GridLayoutGroup))

	var_25_16.cellSize = Vector2(var_25_1.cellSize.x, var_25_1.cellSize.y)
	var_25_16.spacing = Vector2(var_25_1.cellSpace.x, var_25_1.cellSpace.y)
	var_25_16.padding.left = var_25_1.cellSpace.x

	for iter_25_3 = var_25_14.childCount - 1, var_25_13.x, -1 do
		Destroy(var_25_14:GetChild(iter_25_3))
	end

	for iter_25_4 = var_25_14.childCount, var_25_13.x - 1 do
		Instantiate(var_25_15).transform:SetParent(var_25_14, false)
	end

	for iter_25_5 = 0, var_25_13.x - 1 do
		setText(var_25_14:GetChild(iter_25_5), string.char(string.byte("A") + iter_25_5))
	end

	local var_25_17 = var_25_6:Find("123")
	local var_25_18 = var_25_17:GetChild(0)
	local var_25_19 = var_25_17:GetComponent(typeof(GridLayoutGroup))

	var_25_19.cellSize = Vector2(var_25_1.cellSize.x, var_25_1.cellSize.y)
	var_25_19.spacing = Vector2(var_25_1.cellSpace.x, var_25_1.cellSpace.y)
	var_25_19.padding.top = var_25_1.cellSpace.y

	for iter_25_6 = var_25_17.childCount - 1, var_25_13.y, -1 do
		Destroy(var_25_17:GetChild(iter_25_6))
	end

	for iter_25_7 = var_25_17.childCount, var_25_13.y - 1 do
		Instantiate(var_25_18).transform:SetParent(var_25_17, false)
	end

	for iter_25_8 = 0, var_25_13.y - 1 do
		setText(var_25_17:GetChild(iter_25_8), 1 + iter_25_8)
	end

	local var_25_20 = var_25_6:Find("linev")
	local var_25_21 = var_25_20:GetChild(0)
	local var_25_22 = var_25_20:GetComponent(typeof(GridLayoutGroup))

	var_25_22.cellSize = Vector2(ChapterConst.LineCross, var_25_6.sizeDelta.y)
	var_25_22.spacing = Vector2(var_25_10.x - ChapterConst.LineCross, 0)
	var_25_22.padding.left = math.floor(var_25_22.spacing.x)

	for iter_25_9 = var_25_20.childCount - 1, math.max(var_25_13.x - 1, 0), -1 do
		if iter_25_9 > 0 then
			Destroy(var_25_20:GetChild(iter_25_9))
		end
	end

	for iter_25_10 = var_25_20.childCount, var_25_13.x - 2 do
		Instantiate(var_25_21).transform:SetParent(var_25_20, false)
	end

	local var_25_23 = var_25_6:Find("lineh")
	local var_25_24 = var_25_23:GetChild(0)
	local var_25_25 = var_25_23:GetComponent(typeof(GridLayoutGroup))

	var_25_25.cellSize = Vector2(var_25_6.sizeDelta.x, ChapterConst.LineCross)
	var_25_25.spacing = Vector2(0, var_25_10.y - ChapterConst.LineCross)
	var_25_25.padding.top = math.floor(var_25_25.spacing.y)

	for iter_25_11 = var_25_23.childCount - 1, math.max(var_25_13.y - 1, 0), -1 do
		if iter_25_11 > 0 then
			Destroy(var_25_23:GetChild(iter_25_11))
		end
	end

	for iter_25_12 = var_25_23.childCount, var_25_13.y - 2 do
		Instantiate(var_25_24).transform:SetParent(var_25_23, false)
	end

	local var_25_26 = GetOrAddComponent(var_25_6:Find("mask"), "RawImage")
	local var_25_27 = var_25_6:Find("seaBase/sea")

	if var_25_1.seaBase and var_25_1.seaBase ~= "" then
		setActive(var_25_27, true)
		GetImageSpriteFromAtlasAsync("chapter/pic/" .. var_25_1.seaBase, var_25_1.seaBase, var_25_27)

		var_25_26.enabled = true
		var_25_26.uvRect = UnityEngine.Rect.New(0, 0, 1, -1)
	else
		setActive(var_25_27, false)

		var_25_26.enabled = false
	end
end

function var_0_0.updatePoisonArea(arg_28_0)
	local var_28_0 = arg_28_0:findTF("plane/display/mask")
	local var_28_1 = GetOrAddComponent(var_28_0, "RawImage")

	if not var_28_1.enabled then
		return
	end

	var_28_1.texture = arg_28_0:getPoisonTex()
end

function var_0_0.getPoisonTex(arg_29_0)
	local var_29_0 = arg_29_0.contextData.chapterVO
	local var_29_1 = arg_29_0:findTF("plane/display")
	local var_29_2 = var_29_1.sizeDelta.x / var_29_1.sizeDelta.y
	local var_29_3 = 256
	local var_29_4 = math.floor(var_29_3 / var_29_2)
	local var_29_5

	if arg_29_0.preChapterId ~= var_29_0.id then
		var_29_5 = UnityEngine.Texture2D.New(var_29_3, var_29_4)
		arg_29_0.maskTexture = var_29_5
		arg_29_0.preChapterId = var_29_0.id
	else
		var_29_5 = arg_29_0.maskTexture
	end

	local var_29_6 = {}
	local var_29_7 = var_29_0:getPoisonArea(var_29_3 / var_29_1.sizeDelta.x)

	if arg_29_0.poisonRectDir == nil then
		var_29_6 = var_29_7
	else
		for iter_29_0, iter_29_1 in pairs(var_29_7) do
			if arg_29_0.poisonRectDir[iter_29_0] == nil then
				var_29_6[iter_29_0] = iter_29_1
			end
		end
	end

	local function var_29_8(arg_30_0)
		for iter_30_0 = arg_30_0.x, arg_30_0.w + arg_30_0.x do
			for iter_30_1 = arg_30_0.y, arg_30_0.h + arg_30_0.y do
				var_29_5:SetPixel(iter_30_0, iter_30_1, Color.New(1, 1, 1, 0))
			end
		end
	end

	for iter_29_2, iter_29_3 in pairs(var_29_6) do
		var_29_8(iter_29_3)
	end

	var_29_5:Apply()

	arg_29_0.poisonRectDir = var_29_7

	return var_29_5
end

function var_0_0.showFleetPoisonDamage(arg_31_0, arg_31_1, arg_31_2)
	local var_31_0 = arg_31_0.contextData.chapterVO.fleets[arg_31_1].id
	local var_31_1 = arg_31_0.cellFleets[var_31_0]

	if var_31_1 then
		var_31_1:showPoisonDamage(arg_31_2)
	end
end

function var_0_0.clearPlane(arg_32_0)
	arg_32_0:killQuadTws()
	arg_32_0:killPresentTws()
	arg_32_0:ClearEdges()
	arg_32_0:hideQuadMark()
	removeAllChildren(arg_32_0.cellRoot)
	removeAllChildren(arg_32_0.quadRoot)
	removeAllChildren(arg_32_0.bottomMarkRoot)
	removeAllChildren(arg_32_0.topMarkRoot)
	removeAllChildren(arg_32_0.restrictMap)

	arg_32_0.cellRoot = nil
	arg_32_0.quadRoot = nil
	arg_32_0.bottomMarkRoot = nil
	arg_32_0.topMarkRoot = nil
	arg_32_0.restrictMap = nil

	local var_32_0 = arg_32_0._tf:Find(ChapterConst.PlaneName)
	local var_32_1 = var_32_0:Find("display/seaBase/sea")

	clearImageSprite(var_32_1)
	pg.PoolMgr.GetInstance():ReturnPrefab("chapter/plane", "", var_32_0.gameObject)
end

function var_0_0.initFleets(arg_33_0, arg_33_1)
	if arg_33_0.cellFleets then
		existCall(arg_33_1)

		return
	end

	local var_33_0 = arg_33_0.contextData.chapterVO

	arg_33_0.cellFleets = {}

	table.ParallelIpairsAsync(var_33_0.fleets, function(arg_34_0, arg_34_1, arg_34_2)
		if arg_34_1:getFleetType() == FleetType.Support then
			return arg_34_2()
		end

		arg_33_0:InitFleetCell(arg_34_1.id, arg_34_2)
	end, arg_33_1)
end

function var_0_0.InitFleetCell(arg_35_0, arg_35_1, arg_35_2)
	local var_35_0 = arg_35_0.contextData.chapterVO
	local var_35_1 = var_35_0:getFleetById(arg_35_1)

	if not var_35_1:isValid() then
		existCall(arg_35_2)

		return
	end

	local var_35_2
	local var_35_3 = arg_35_0:getFleetPool(var_35_1:getFleetType()):Dequeue()

	var_35_3.transform.localEulerAngles = Vector3(-var_35_0.theme.angle, 0, 0)

	setParent(var_35_3, arg_35_0.cellRoot, false)
	setActive(var_35_3, true)

	local var_35_4 = var_35_1:getFleetType()
	local var_35_5

	if var_35_4 == FleetType.Transport then
		var_35_5 = TransportCellView
	elseif var_35_4 == FleetType.Submarine then
		var_35_5 = SubCellView
	else
		var_35_5 = FleetCellView
	end

	local var_35_6 = var_35_5.New(var_35_3)

	var_35_6.fleetType = var_35_4

	if var_35_4 == FleetType.Normal or var_35_4 == FleetType.Submarine then
		var_35_6:SetAction(ChapterConst.ShipIdleAction)
	end

	var_35_6.tf.localPosition = var_35_0.theme:GetLinePosition(var_35_1.line.row, var_35_1.line.column)
	arg_35_0.cellFleets[arg_35_1] = var_35_6

	arg_35_0:RefreshFleetCell(arg_35_1, arg_35_2)
end

function var_0_0.RefreshFleetCells(arg_36_0, arg_36_1)
	if not arg_36_0.cellFleets then
		arg_36_0:initFleets(arg_36_1)

		return
	end

	local var_36_0 = arg_36_0.contextData.chapterVO
	local var_36_1 = {}

	for iter_36_0, iter_36_1 in pairs(arg_36_0.cellFleets) do
		if not var_36_0:getFleetById(iter_36_0) then
			table.insert(var_36_1, iter_36_0)
		end
	end

	for iter_36_2, iter_36_3 in pairs(var_36_1) do
		arg_36_0:ClearFleetCell(iter_36_3)
	end

	table.ParallelIpairsAsync(var_36_0.fleets, function(arg_37_0, arg_37_1, arg_37_2)
		if arg_37_1:getFleetType() == FleetType.Support then
			return arg_37_2()
		end

		if not arg_36_0.cellFleets[arg_37_1.id] then
			arg_36_0:InitFleetCell(arg_37_1.id, arg_37_2)
		else
			arg_36_0:RefreshFleetCell(arg_37_1.id, arg_37_2)
		end
	end, arg_36_1)
end

function var_0_0.RefreshFleetCell(arg_38_0, arg_38_1, arg_38_2)
	local var_38_0 = arg_38_0.contextData.chapterVO
	local var_38_1 = var_38_0:getFleetById(arg_38_1)
	local var_38_2 = arg_38_0.cellFleets[arg_38_1]
	local var_38_3
	local var_38_4

	if var_38_1:isValid() then
		if var_38_1:getFleetType() == FleetType.Transport then
			var_38_3 = var_38_1:getPrefab()
		else
			local var_38_5 = var_38_0:getMapShip(var_38_1)

			if var_38_5 then
				var_38_3 = var_38_5:getPrefab()
				var_38_4 = var_38_5:getAttachmentPrefab()
			end
		end
	end

	if not var_38_3 then
		arg_38_0:ClearFleetCell(arg_38_1)
		existCall(arg_38_2)

		return
	end

	var_38_2.go.name = "cell_fleet_" .. var_38_3

	var_38_2:SetLine(var_38_1.line)

	if var_38_2.fleetType == FleetType.Transport then
		var_38_2:LoadIcon(var_38_3, function()
			var_38_2:GetRotatePivot().transform.localRotation = var_38_1.rotation

			arg_38_0:updateFleet(arg_38_1, arg_38_2)
		end)
	else
		var_38_2:LoadSpine(var_38_3, nil, var_38_4, function()
			var_38_2:GetRotatePivot().transform.localRotation = var_38_1.rotation

			arg_38_0:updateFleet(arg_38_1, arg_38_2)
		end)
	end
end

function var_0_0.clearFleets(arg_41_0)
	if arg_41_0.cellFleets then
		for iter_41_0, iter_41_1 in pairs(arg_41_0.cellFleets) do
			arg_41_0:ClearFleetCell(iter_41_0)
		end

		arg_41_0.cellFleets = nil
	end
end

function var_0_0.ClearFleetCell(arg_42_0, arg_42_1)
	local var_42_0 = arg_42_0.cellFleets[arg_42_1]

	if not var_42_0 then
		return
	end

	var_42_0:Clear()
	LeanTween.cancel(var_42_0.go)
	setActive(var_42_0.go, false)
	setParent(var_42_0.go, arg_42_0.poolParent, false)
	arg_42_0:getFleetPool(var_42_0.fleetType):Enqueue(var_42_0.go, false)

	if arg_42_0.opBtns[arg_42_1] then
		Destroy(arg_42_0.opBtns[arg_42_1].gameObject)

		arg_42_0.opBtns[arg_42_1] = nil
	end

	arg_42_0.cellFleets[arg_42_1] = nil
end

function var_0_0.UpdateFleets(arg_43_0, arg_43_1)
	local var_43_0 = arg_43_0.contextData.chapterVO

	table.ParallelIpairsAsync(var_43_0.fleets, function(arg_44_0, arg_44_1, arg_44_2)
		if arg_44_1:getFleetType() == FleetType.Support then
			return arg_44_2()
		end

		arg_43_0:updateFleet(arg_44_1.id, arg_44_2)
	end, arg_43_1)
end

function var_0_0.updateFleet(arg_45_0, arg_45_1, arg_45_2)
	local var_45_0 = arg_45_0.contextData.chapterVO
	local var_45_1 = arg_45_0.cellFleets[arg_45_1]
	local var_45_2 = var_45_0:getFleetById(arg_45_1)

	if var_45_1 then
		local var_45_3 = var_45_2.line
		local var_45_4 = var_45_2:isValid()

		setActive(var_45_1.go, var_45_4)
		var_45_1:RefreshLinePosition(var_45_0, var_45_3)

		local var_45_5 = var_45_2:getFleetType()

		if var_45_5 == FleetType.Normal then
			local var_45_6 = var_45_0:GetEnemy(var_45_3.row, var_45_3.column)
			local var_45_7 = tobool(var_45_6)
			local var_45_8 = var_45_6 and var_45_6.attachment or nil
			local var_45_9 = var_45_0:existFleet(FleetType.Transport, var_45_3.row, var_45_3.column)

			var_45_1:SetSpineVisible(not var_45_7 and not var_45_9)

			local var_45_10 = table.indexof(var_45_0.fleets, var_45_2) == var_45_0.findex

			setActive(var_45_1.tfArrow, var_45_10)
			setActive(var_45_1.tfOp, false)

			local var_45_11 = arg_45_0.opBtns[arg_45_1]

			if not var_45_11 then
				var_45_11 = tf(Instantiate(var_45_1.tfOp))
				var_45_11.name = "op" .. arg_45_1

				var_45_11:SetParent(arg_45_0._tf, false)

				var_45_11.localEulerAngles = Vector3(-var_45_0.theme.angle, 0, 0)

				local var_45_12 = GetOrAddComponent(var_45_11, typeof(Canvas))

				GetOrAddComponent(go(var_45_11), typeof(GraphicRaycaster))

				var_45_12.overrideSorting = true
				var_45_12.sortingOrder = ChapterConst.PriorityMax
				arg_45_0.opBtns[arg_45_1] = var_45_11

				arg_45_0:UpdateOpBtns()
			end

			var_45_11.position = var_45_1.tfOp.position

			local var_45_13 = var_45_6 and ChapterConst.IsBossCell(var_45_6)
			local var_45_14 = false

			if var_45_7 and var_45_8 == ChapterConst.AttachChampion then
				local var_45_15 = var_45_0:getChampion(var_45_3.row, var_45_3.column):GetLastID()
				local var_45_16 = pg.expedition_data_template[var_45_15]

				if var_45_16 then
					var_45_14 = var_45_16.ai == ChapterConst.ExpeditionAILair
				end
			end

			var_45_13 = var_45_13 or var_45_14

			local var_45_17 = _.any(var_45_0.fleets, function(arg_46_0)
				return arg_46_0.id ~= var_45_2.id and arg_46_0:getFleetType() == FleetType.Normal and arg_46_0:isValid()
			end)
			local var_45_18 = var_45_10 and var_45_4 and var_45_7
			local var_45_19 = var_45_11:Find("retreat")

			setActive(var_45_19:Find("retreat"), var_45_18 and not var_45_13 and var_45_17)
			setActive(var_45_19:Find("escape"), var_45_18 and var_45_13)
			setActive(var_45_19, var_45_19:Find("retreat").gameObject.activeSelf or var_45_19:Find("escape").gameObject.activeSelf)

			if var_45_19.gameObject.activeSelf then
				onButton(arg_45_0, var_45_19, function()
					if arg_45_0.parent:isfrozen() then
						return
					end

					if var_45_13 then
						(function()
							local var_48_0 = {
								{
									1,
									0
								},
								{
									-1,
									0
								},
								{
									0,
									1
								},
								{
									0,
									-1
								}
							}

							for iter_48_0, iter_48_1 in ipairs(var_48_0) do
								if var_45_0:considerAsStayPoint(ChapterConst.SubjectPlayer, var_45_3.row + iter_48_1[1], var_45_3.column + iter_48_1[2]) and not var_45_0:existEnemy(ChapterConst.SubjectPlayer, var_45_3.row + iter_48_1[1], var_45_3.column + iter_48_1[2]) then
									arg_45_0:emit(LevelMediator2.ON_OP, {
										type = ChapterConst.OpMove,
										id = var_45_2.id,
										arg1 = var_45_3.row + iter_48_1[1],
										arg2 = var_45_3.column + iter_48_1[2],
										ordLine = var_45_2.line
									})

									return false
								end
							end

							pg.TipsMgr.GetInstance():ShowTips(i18n("no_way_to_escape"))

							return true
						end)()
					else
						pg.MsgboxMgr.GetInstance():ShowMsgBox({
							content = i18n("levelScene_who_to_retreat", var_45_2.name),
							onYes = function()
								arg_45_0:emit(LevelMediator2.ON_OP, {
									type = ChapterConst.OpRetreat,
									id = var_45_2.id
								})
							end
						})
					end
				end, SFX_UI_WEIGHANCHOR_WITHDRAW)
			end

			local var_45_20 = var_45_11:Find("exchange")

			setActive(var_45_20, false)
			setActive(var_45_1.tfAmmo, not var_45_9)

			local var_45_21, var_45_22 = var_45_0:getFleetAmmo(var_45_2)
			local var_45_23 = var_45_22 .. "/" .. var_45_21

			if var_45_22 == 0 then
				var_45_23 = setColorStr(var_45_23, COLOR_RED)
			end

			setText(var_45_1.tfAmmoText, var_45_23)

			if var_45_7 or var_45_9 then
				local var_45_24 = var_45_0:getChampion(var_45_3.row, var_45_3.column)

				if var_45_7 and var_45_8 == ChapterConst.AttachChampion and var_45_24:getPoolType() == ChapterConst.TemplateChampion then
					var_45_1.tfArrow.anchoredPosition = Vector2(0, 180)
					var_45_1.tfAmmo.anchoredPosition = Vector2(60, 100)
				else
					var_45_1.tfArrow.anchoredPosition = Vector2(0, 100)
					var_45_1.tfAmmo.anchoredPosition = Vector2(22, 56)
				end

				var_45_1.tfAmmo:SetAsLastSibling()
			else
				var_45_1.tfArrow.anchoredPosition = Vector2(0, 175)
				var_45_1.tfAmmo.anchoredPosition = Vector2(-60, 85)
			end

			if var_45_1:GetSpineRole() and var_45_10 and arg_45_0.lastSelectedId ~= var_45_2.id then
				if not var_45_7 and not var_45_9 and arg_45_0.lastSelectedId ~= -1 then
					var_45_1:TweenShining()
				end

				arg_45_0.lastSelectedId = var_45_2.id
			end

			local var_45_25 = var_45_0:existBarrier(var_45_3.row, var_45_3.column)

			var_45_1:SetActiveNoPassIcon(var_45_25)

			local var_45_26 = table.contains(var_45_2:GetStatusStrategy(), ChapterConst.StrategyIntelligenceRecorded)

			var_45_1:UpdateIconRecordedFlag(var_45_26)
		elseif var_45_5 == FleetType.Submarine then
			local var_45_27 = var_45_0:existEnemy(ChapterConst.SubjectPlayer, var_45_3.row, var_45_3.column) or var_45_0:existAlly(var_45_2)
			local var_45_28 = var_45_0.subAutoAttack == 1

			var_45_1:SetActiveModel(not var_45_27 and var_45_28)
			setActive(var_45_1.tfAmmo, not var_45_27)

			local var_45_29, var_45_30 = var_45_0:getFleetAmmo(var_45_2)
			local var_45_31 = var_45_30 .. "/" .. var_45_29

			if var_45_30 == 0 then
				var_45_31 = setColorStr(var_45_31, COLOR_RED)
			end

			setText(var_45_1.tfAmmoText, var_45_31)
		elseif var_45_5 == FleetType.Transport then
			setText(var_45_1.tfHpText, var_45_2:getRestHp() .. "/" .. var_45_2:getTotalHp())

			local var_45_32 = var_45_0:existEnemy(ChapterConst.SubjectPlayer, var_45_3.row, var_45_3.column)

			GetImageSpriteFromAtlasAsync("enemies/" .. var_45_2:getPrefab(), "", var_45_1.tfIcon, true)
			setActive(var_45_1.tfFighting, var_45_32)
		end
	end

	existCall(arg_45_2)
end

function var_0_0.UpdateOpBtns(arg_50_0)
	table.Foreach(arg_50_0.opBtns, function(arg_51_0, arg_51_1)
		setActive(arg_51_1, arg_50_0.quadState == ChapterConst.QuadStateNormal)
	end)
end

function var_0_0.GetCellFleet(arg_52_0, arg_52_1)
	return arg_52_0.cellFleets[arg_52_1]
end

function var_0_0.initTargetArrow(arg_53_0)
	local var_53_0 = arg_53_0.contextData.chapterVO

	arg_53_0.arrowTarget = cloneTplTo(arg_53_0.arrowTpl, arg_53_0._tf)

	local var_53_1 = arg_53_0.arrowTarget

	pg.ViewUtils.SetLayer(tf(var_53_1), Layer.UI)

	GetOrAddComponent(var_53_1, typeof(Canvas)).overrideSorting = true
	arg_53_0.arrowTarget.localEulerAngles = Vector3(-var_53_0.theme.angle, 0, 0)

	setActive(arg_53_0.arrowTarget, false)
end

function var_0_0.updateTargetArrow(arg_54_0, arg_54_1)
	local var_54_0 = arg_54_0.contextData.chapterVO
	local var_54_1 = ChapterCell.Line2Name(arg_54_1.row, arg_54_1.column)
	local var_54_2 = arg_54_0.cellRoot:Find(var_54_1)

	arg_54_0.arrowTarget:SetParent(var_54_2)

	local var_54_3, var_54_4 = (function()
		local var_55_0, var_55_1 = var_54_0:existEnemy(ChapterConst.SubjectPlayer, arg_54_1.row, arg_54_1.column)

		if not var_55_0 then
			return false
		end

		if var_55_1 == ChapterConst.AttachChampion then
			local var_55_2 = var_54_0:getChampion(arg_54_1.row, arg_54_1.column)

			if not var_55_2 then
				return false
			end

			return var_55_2:getPoolType() == "common", var_55_2:getScale() / 100
		elseif ChapterConst.IsEnemyAttach(var_55_1) then
			local var_55_3 = var_54_0:getChapterCell(arg_54_1.row, arg_54_1.column)

			if not var_55_3 or var_55_3.flag ~= ChapterConst.CellFlagActive then
				return false
			end

			local var_55_4 = pg.expedition_data_template[var_55_3.attachmentId]

			return var_55_4.icon_type == 2, var_55_4.scale / 100
		end
	end)()

	if var_54_3 then
		arg_54_0.arrowTarget.localPosition = Vector3(0, 20 + 80 * var_54_4, -80 * var_54_4)
	else
		arg_54_0.arrowTarget.localPosition = Vector3(0, 20, 0)
	end

	local var_54_5 = arg_54_0.arrowTarget:GetComponent(typeof(Canvas))

	if var_54_5 then
		var_54_5.sortingOrder = arg_54_1.row * ChapterConst.PriorityPerRow + ChapterConst.CellPriorityTopMark
	end
end

function var_0_0.clearTargetArrow(arg_56_0)
	if not IsNil(arg_56_0.arrowTarget) then
		Destroy(arg_56_0.arrowTarget)

		arg_56_0.arrowTarget = nil
	end
end

function var_0_0.InitDestinationMark(arg_57_0)
	local var_57_0 = cloneTplTo(arg_57_0.destinationMarkTpl, arg_57_0._tf)

	pg.ViewUtils.SetLayer(tf(var_57_0), Layer.UI)

	GetOrAddComponent(var_57_0, typeof(Canvas)).overrideSorting = true

	setActive(var_57_0, false)

	local var_57_1 = arg_57_0.contextData.chapterVO

	tf(var_57_0).localEulerAngles = Vector3(-var_57_1.theme.angle, 0, 0)
	arg_57_0.destinationMark = tf(var_57_0)
end

function var_0_0.UpdateDestinationMark(arg_58_0, arg_58_1)
	if not arg_58_1 then
		arg_58_0.destinationMark:SetParent(arg_58_0._tf)
		setActive(go(arg_58_0.destinationMark), false)

		return
	end

	setActive(go(arg_58_0.destinationMark), true)

	local var_58_0 = ChapterCell.Line2Name(arg_58_1.row, arg_58_1.column)
	local var_58_1 = arg_58_0.cellRoot:Find(var_58_0)

	arg_58_0.destinationMark:SetParent(var_58_1)

	arg_58_0.destinationMark.localPosition = Vector3(0, 40, -40)

	local var_58_2 = arg_58_0.destinationMark:GetComponent(typeof(Canvas))

	if var_58_2 then
		var_58_2.sortingOrder = arg_58_1.row * ChapterConst.PriorityPerRow + ChapterConst.CellPriorityTopMark
	end
end

function var_0_0.ClearDestinationMark(arg_59_0)
	if not IsNil(arg_59_0.destinationMark) then
		Destroy(arg_59_0.destinationMark)

		arg_59_0.destinationMark = nil
	end
end

function var_0_0.initChampions(arg_60_0, arg_60_1)
	if arg_60_0.cellChampions then
		existCall(arg_60_1)

		return
	end

	arg_60_0.cellChampions = {}

	local var_60_0 = arg_60_0.contextData.chapterVO

	table.ParallelIpairsAsync(var_60_0.champions, function(arg_61_0, arg_61_1, arg_61_2)
		arg_60_0.cellChampions[arg_61_0] = false

		if arg_61_1.flag ~= ChapterConst.CellFlagDisabled then
			arg_60_0:InitChampion(arg_61_0, arg_61_2)
		else
			arg_61_2()
		end
	end, arg_60_1)
end

function var_0_0.InitChampion(arg_62_0, arg_62_1, arg_62_2)
	local var_62_0 = arg_62_0.contextData.chapterVO
	local var_62_1 = var_62_0.champions[arg_62_1]
	local var_62_2 = var_62_1:getPoolType()
	local var_62_3 = arg_62_0:getChampionPool(var_62_2):Dequeue()

	var_62_3.name = "cell_champion_" .. var_62_1:getPrefab()
	var_62_3.transform.localEulerAngles = Vector3(-var_62_0.theme.angle, 0, 0)

	setParent(var_62_3, arg_62_0.cellRoot, false)
	setActive(var_62_3, true)

	local var_62_4

	if var_62_2 == ChapterConst.TemplateChampion then
		var_62_4 = DynamicChampionCellView
	elseif var_62_2 == ChapterConst.TemplateEnemy then
		var_62_4 = DynamicEggCellView
	elseif var_62_2 == ChapterConst.TemplateOni then
		var_62_4 = OniCellView
	end

	local var_62_5 = var_62_4.New(var_62_3)

	arg_62_0.cellChampions[arg_62_1] = var_62_5

	var_62_5:SetLine({
		row = var_62_1.row,
		column = var_62_1.column
	})
	var_62_5:SetPoolType(var_62_2)

	if var_62_5.GetRotatePivot then
		tf(var_62_5:GetRotatePivot()).localRotation = var_62_1.rotation
	end

	if var_62_2 == ChapterConst.TemplateChampion then
		var_62_5:SetAction(ChapterConst.ShipIdleAction)

		if var_62_1.flag == ChapterConst.CellFlagDiving then
			var_62_5:SetAction(ChapterConst.ShipSwimAction)
		end

		var_62_5:LoadSpine(var_62_1:getPrefab(), var_62_1:getScale(), var_62_1:getConfig("effect_prefab"), function()
			arg_62_0:updateChampion(arg_62_1, arg_62_2)
		end)
	elseif var_62_2 == ChapterConst.TemplateEnemy then
		var_62_5:LoadIcon(var_62_1:getPrefab(), var_62_1:getConfigTable(), function()
			arg_62_0:updateChampion(arg_62_1, arg_62_2)
		end)
	elseif var_62_2 == ChapterConst.TemplateOni then
		arg_62_0:updateChampion(arg_62_1, arg_62_2)
	end
end

function var_0_0.updateChampions(arg_65_0, arg_65_1)
	table.ParallelIpairsAsync(arg_65_0.cellChampions, function(arg_66_0, arg_66_1, arg_66_2)
		arg_65_0:updateChampion(arg_66_0, arg_66_2)
	end, arg_65_1)
end

function var_0_0.updateChampion(arg_67_0, arg_67_1, arg_67_2)
	local var_67_0 = arg_67_0.contextData.chapterVO
	local var_67_1 = arg_67_0.cellChampions[arg_67_1]
	local var_67_2 = var_67_0.champions[arg_67_1]

	if var_67_1 and var_67_2 then
		var_67_1:UpdateChampionCell(var_67_0, var_67_2, arg_67_2)
	end
end

function var_0_0.updateOni(arg_68_0)
	local var_68_0 = arg_68_0.contextData.chapterVO
	local var_68_1

	for iter_68_0, iter_68_1 in ipairs(var_68_0.champions) do
		if iter_68_1.attachment == ChapterConst.AttachOni then
			var_68_1 = iter_68_0

			break
		end
	end

	if var_68_1 then
		arg_68_0:updateChampion(var_68_1)
	end
end

function var_0_0.clearChampions(arg_69_0)
	if arg_69_0.cellChampions then
		for iter_69_0, iter_69_1 in ipairs(arg_69_0.cellChampions) do
			if iter_69_1 then
				iter_69_1:Clear()
				LeanTween.cancel(iter_69_1.go)
				setActive(iter_69_1.go, false)
				setParent(iter_69_1.go, arg_69_0.poolParent, false)
				arg_69_0:getChampionPool(iter_69_1:GetPoolType()):Enqueue(iter_69_1.go, false)
			end
		end

		arg_69_0.cellChampions = nil
	end
end

function var_0_0.initCell(arg_70_0, arg_70_1, arg_70_2)
	local var_70_0 = arg_70_0.contextData.chapterVO
	local var_70_1 = var_70_0:getChapterCell(arg_70_1, arg_70_2)

	if var_70_1 then
		local var_70_2 = var_70_0.theme.cellSize
		local var_70_3 = ChapterCell.Line2QuadName(arg_70_1, arg_70_2)
		local var_70_4

		if var_70_1:IsWalkable() then
			PoolMgr.GetInstance():GetPrefab("chapter/cell_quad", "", false, function(arg_71_0)
				var_70_4 = arg_71_0.transform
			end)

			var_70_4.name = var_70_3

			var_70_4:SetParent(arg_70_0.quadRoot, false)

			var_70_4.sizeDelta = var_70_2
			var_70_4.anchoredPosition = var_70_0.theme:GetLinePosition(arg_70_1, arg_70_2)

			var_70_4:SetAsLastSibling()
			onButton(arg_70_0, var_70_4, function()
				if arg_70_0:isfrozen() then
					return
				end

				arg_70_0:ClickGridCell(var_70_1)
			end, SFX_CONFIRM)
		end

		local var_70_5 = ChapterCell.Line2Name(arg_70_1, arg_70_2)
		local var_70_6

		PoolMgr.GetInstance():GetPrefab("chapter/cell", "", false, function(arg_73_0)
			var_70_6 = arg_73_0.transform
		end)

		var_70_6.name = var_70_5

		var_70_6:SetParent(arg_70_0.cellRoot, false)

		var_70_6.sizeDelta = var_70_2
		var_70_6.anchoredPosition = var_70_0.theme:GetLinePosition(arg_70_1, arg_70_2)

		var_70_6:SetAsLastSibling()

		local var_70_7 = var_70_6:Find(ChapterConst.ChildItem)

		var_70_7.localEulerAngles = Vector3(-var_70_0.theme.angle, 0, 0)

		setActive(var_70_7, var_70_1.item)

		local var_70_8 = ItemCell.New(var_70_7, arg_70_1, arg_70_2)

		arg_70_0.itemCells[ChapterCell.Line2Name(arg_70_1, arg_70_2)] = var_70_8
		var_70_8.loader = arg_70_0.loader

		var_70_8:Init(var_70_1)

		var_70_6:Find(ChapterConst.ChildAttachment).localEulerAngles = Vector3(-var_70_0.theme.angle, 0, 0)
	end
end

function var_0_0.clearCell(arg_74_0, arg_74_1, arg_74_2)
	local var_74_0 = ChapterCell.Line2Name(arg_74_1, arg_74_2)
	local var_74_1 = ChapterCell.Line2QuadName(arg_74_1, arg_74_2)
	local var_74_2 = arg_74_0.cellRoot:Find(var_74_0)
	local var_74_3 = arg_74_0.quadRoot:Find(var_74_1)

	if not IsNil(var_74_2) then
		PoolMgr.GetInstance():ReturnPrefab("chapter/cell", "", var_74_2.gameObject)
	end

	if not IsNil(var_74_3) then
		if arg_74_0.quadTws[var_74_1] then
			LeanTween.cancel(arg_74_0.quadTws[var_74_1].uniqueId)

			arg_74_0.quadTws[var_74_1] = nil
		end

		local var_74_4 = var_74_3:Find("grid"):GetComponent(typeof(Image))

		var_74_4.sprite = GetSpriteFromAtlas("chapter/pic/cellgrid", "cell_grid")
		var_74_4.material = nil

		PoolMgr.GetInstance():ReturnPrefab("chapter/cell_quad", "", var_74_3.gameObject)
	end
end

function var_0_0.UpdateItemCells(arg_75_0)
	local var_75_0 = arg_75_0.contextData.chapterVO

	if not var_75_0 then
		return
	end

	for iter_75_0, iter_75_1 in pairs(arg_75_0.itemCells) do
		local var_75_1 = iter_75_1:GetOriginalInfo()
		local var_75_2 = var_75_1 and var_75_1.item
		local var_75_3 = ItemCell.TransformItemAsset(var_75_0, var_75_2)

		iter_75_1:UpdateAsset(var_75_3)
	end
end

function var_0_0.updateAttachments(arg_76_0)
	for iter_76_0 = 0, ChapterConst.MaxRow - 1 do
		for iter_76_1 = 0, ChapterConst.MaxColumn - 1 do
			arg_76_0:updateAttachment(iter_76_0, iter_76_1)
		end
	end

	arg_76_0:updateExtraAttachments()
	arg_76_0:updateCoastalGunAttachArea()
	arg_76_0:displayEscapeGrid()
end

function var_0_0.UpdateFloor(arg_77_0)
	local var_77_0 = arg_77_0.contextData.chapterVO
	local var_77_1 = var_77_0.cells
	local var_77_2 = {}

	for iter_77_0, iter_77_1 in pairs(var_77_1) do
		local var_77_3 = iter_77_1:GetFlagList()

		for iter_77_2, iter_77_3 in pairs(var_77_3) do
			var_77_2[iter_77_3] = var_77_2[iter_77_3] or {}

			table.insert(var_77_2[iter_77_3], iter_77_1)
		end
	end

	if var_77_2[ChapterConst.FlagBanaiAirStrike] and next(var_77_2[ChapterConst.FlagBanaiAirStrike]) then
		arg_77_0:hideQuadMark(ChapterConst.MarkBanaiAirStrike)
		arg_77_0:showQuadMark(var_77_2[ChapterConst.FlagBanaiAirStrike], ChapterConst.MarkBanaiAirStrike, "cell_coastal_gun", Vector2(110, 110), nil, true)
	end

	arg_77_0:updatePoisonArea()

	if var_77_2[ChapterConst.FlagLava] and next(var_77_2[ChapterConst.FlagLava]) then
		arg_77_0:hideQuadMark(ChapterConst.MarkLava)
		arg_77_0:showQuadMark(var_77_2[ChapterConst.FlagLava], ChapterConst.MarkLava, "cell_lava", Vector2(110, 110), nil, true)
	end

	if var_77_2[ChapterConst.FlagNightmare] and next(var_77_2[ChapterConst.FlagNightmare]) then
		arg_77_0:hideQuadMark(ChapterConst.MarkNightMare)
		arg_77_0:hideQuadMark(ChapterConst.MarkHideNight)

		local var_77_4 = var_77_0:getExtraFlags()[1]

		if var_77_4 == ChapterConst.StatusDay then
			arg_77_0:showQuadMark(var_77_2[ChapterConst.FlagNightmare], ChapterConst.MarkHideNight, "cell_hidden_nightmare", Vector2(110, 110), nil, true)
		elseif var_77_4 == ChapterConst.StatusNight then
			arg_77_0:showQuadMark(var_77_2[ChapterConst.FlagNightmare], ChapterConst.MarkNightMare, "cell_nightmare", Vector2(110, 110), nil, true)
		end
	end

	local var_77_5 = {}

	for iter_77_4, iter_77_5 in pairs(var_77_0:GetChapterCellAttachemnts()) do
		if iter_77_5.data == ChapterConst.StoryTrigger then
			local var_77_6 = pg.map_event_template[iter_77_5.attachmentId]

			assert(var_77_6, "map_event_template not exists " .. iter_77_5.attachmentId)

			if var_77_6 and var_77_6.c_type == ChapterConst.EvtType_AdditionalFloor then
				var_77_5[var_77_6.icon] = var_77_5[var_77_6.icon] or {}

				table.insert(var_77_5[var_77_6.icon], iter_77_5)
			end
		end
	end

	for iter_77_6, iter_77_7 in pairs(var_77_5) do
		arg_77_0:hideQuadMark(iter_77_6)
		arg_77_0:showQuadMark(iter_77_7, iter_77_6, iter_77_6, Vector2(110, 110), nil, true)
	end

	local var_77_7 = var_77_0:getConfig("alarm_cell")

	if var_77_7 and #var_77_7 > 0 then
		local var_77_8 = var_77_7[3]

		arg_77_0:ClearEdges(var_77_8)
		arg_77_0:ClearEdges(var_77_8 .. "corner")
		arg_77_0:AddEdgePool(var_77_8, "chapter/celltexture/" .. var_77_8, "")
		arg_77_0:AddEdgePool(var_77_8 .. "_corner", "chapter/celltexture/" .. var_77_8 .. "_corner", "")

		local var_77_9 = _.map(var_77_7[1], function(arg_78_0)
			return {
				row = arg_78_0[1],
				column = arg_78_0[2]
			}
		end)

		arg_77_0:AddOutlines(var_77_9, nil, var_77_7[5], var_77_7[4], var_77_8)

		local var_77_10 = var_77_7[2]

		arg_77_0:hideQuadMark(var_77_10)
		arg_77_0:showQuadMark(var_77_9, var_77_10, var_77_10, Vector2(104, 104), nil, true)
	end

	arg_77_0:HideMissileAimingMarks()

	if var_77_2[ChapterConst.FlagMissleAiming] and next(var_77_2[ChapterConst.FlagMissleAiming]) then
		arg_77_0:ShowMissileAimingMarks(var_77_2[ChapterConst.FlagMissleAiming])
	end

	arg_77_0:UpdateWeatherCells()

	local var_77_11 = var_77_0.fleet

	if var_77_0:isPlayingWithBombEnemy() then
		local var_77_12 = _.map({
			{
				-1,
				0
			},
			{
				1,
				0
			},
			{
				0,
				-1
			},
			{
				0,
				1
			}
		}, function(arg_79_0)
			return {
				row = arg_79_0[1] + var_77_11.line.row,
				column = arg_79_0[2] + var_77_11.line.column
			}
		end)

		arg_77_0:showQuadMark(var_77_12, ChapterConst.MarkBomb, "cell_bomb", Vector2(100, 100), nil, true)
	end
end

function var_0_0.updateExtraAttachments(arg_80_0)
	local var_80_0 = arg_80_0.contextData.chapterVO
	local var_80_1 = var_80_0:GetChapterCellAttachemnts()

	for iter_80_0, iter_80_1 in pairs(var_80_1) do
		local var_80_2 = iter_80_1.row
		local var_80_3 = iter_80_1.column
		local var_80_4 = arg_80_0.cellRoot:Find(iter_80_0):Find(ChapterConst.ChildAttachment)
		local var_80_5 = pg.map_event_template[iter_80_1.attachmentId]
		local var_80_6 = iter_80_1.data
		local var_80_7

		if var_80_6 == ChapterConst.StoryTrigger and var_80_5.c_type ~= ChapterConst.EvtType_AdditionalFloor then
			var_80_7 = MapEventStoryTriggerCellView
		end

		local var_80_8 = arg_80_0.extraAttachmentCells[iter_80_0]

		if var_80_8 and var_80_8.class ~= var_80_7 then
			var_80_8:Clear()

			var_80_8 = nil
			arg_80_0.extraAttachmentCells[iter_80_0] = nil
		end

		if var_80_7 then
			if not var_80_8 then
				var_80_8 = var_80_7.New(var_80_4)
				arg_80_0.extraAttachmentCells[iter_80_0] = var_80_8
			end

			var_80_8.info = iter_80_1
			var_80_8.chapter = var_80_0

			var_80_8:SetLine({
				row = var_80_2,
				column = var_80_3
			})
			var_80_8:Update()
		end
	end
end

function var_0_0.updateAttachment(arg_81_0, arg_81_1, arg_81_2)
	local var_81_0 = arg_81_0.contextData.chapterVO
	local var_81_1 = var_81_0:getChapterCell(arg_81_1, arg_81_2)

	if not var_81_1 then
		return
	end

	local var_81_2 = ChapterCell.Line2Name(arg_81_1, arg_81_2)
	local var_81_3 = arg_81_0.cellRoot:Find(var_81_2):Find(ChapterConst.ChildAttachment)
	local var_81_4
	local var_81_5 = {}

	if ChapterConst.IsEnemyAttach(var_81_1.attachment) then
		local var_81_6 = pg.expedition_data_template[var_81_1.attachmentId]

		assert(var_81_6, "expedition_data_template not exist: " .. var_81_1.attachmentId)

		if var_81_1.flag == ChapterConst.CellFlagDisabled then
			if var_81_1.attachment ~= ChapterConst.AttachAmbush then
				var_81_4 = EnemyDeadCellView
				var_81_5.chapter = var_81_0
				var_81_5.config = var_81_6
			end
		elseif var_81_1.flag == ChapterConst.CellFlagActive then
			var_81_4 = var_81_6.icon_type == 1 and StaticEggCellView or StaticChampionCellView
			var_81_5.config = var_81_6
			var_81_5.chapter = var_81_0
			var_81_5.viewParent = arg_81_0
		end
	elseif var_81_1.attachment == ChapterConst.AttachBox then
		var_81_4 = AttachmentBoxCell
	elseif var_81_1.attachment == ChapterConst.AttachSupply then
		var_81_4 = AttachmentSupplyCell
	elseif var_81_1.attachment == ChapterConst.AttachTransport_Target then
		var_81_4 = AttachmentTransportTargetCell
	elseif var_81_1.attachment == ChapterConst.AttachStory then
		if var_81_1.data == ChapterConst.Story then
			var_81_4 = MapEventStoryCellView
		elseif var_81_1.data == ChapterConst.StoryObstacle then
			var_81_4 = MapEventStoryObstacleCellView
			var_81_5.chapter = var_81_0
		end
	elseif var_81_1.attachment == ChapterConst.AttachBomb_Enemy then
		var_81_4 = AttachmentBombEnemyCell
	elseif var_81_1.attachment == ChapterConst.AttachLandbase then
		local var_81_7 = pg.land_based_template[var_81_1.attachmentId]

		assert(var_81_7, "land_based_template not exist: " .. var_81_1.attachmentId)

		if var_81_7.type == ChapterConst.LBCoastalGun then
			var_81_4 = AttachmentLBCoastalGunCell
		elseif var_81_7.type == ChapterConst.LBHarbor then
			var_81_4 = AttachmentLBHarborCell
		elseif var_81_7.type == ChapterConst.LBDock then
			var_81_4 = AttachmentLBDockCell
			var_81_5.chapter = var_81_0
		elseif var_81_7.type == ChapterConst.LBAntiAir then
			var_81_4 = AttachmentLBAntiAirCell
			var_81_5.info = var_81_1
			var_81_5.chapter = var_81_0
			var_81_5.grid = arg_81_0
		elseif var_81_7.type == ChapterConst.LBIdle and var_81_1.attachmentId == ChapterConst.LBIDAirport then
			var_81_4 = AttachmentLBAirport
			var_81_5.extraFlagList = var_81_0:getExtraFlags()
		end
	elseif var_81_1.attachment == ChapterConst.AttachBarrier then
		var_81_4 = AttachmentBarrierCell
	elseif var_81_1.attachment == ChapterConst.AttachNone then
		var_81_5.fadeAnim = (function()
			local var_82_0 = arg_81_0.attachmentCells[var_81_2]

			if not var_82_0 then
				return
			end

			if var_82_0.class ~= StaticEggCellView and var_82_0.class ~= StaticChampionCellView then
				return
			end

			local var_82_1 = var_82_0.info

			if not var_82_1 then
				return
			end

			return pg.expedition_data_template[var_82_1.attachmentId].dungeon_id == 0
		end)()
	end

	if var_81_5.fadeAnim then
		arg_81_0:PlayAttachmentEffect(arg_81_1, arg_81_2, "miwuxiaosan")
	end

	local var_81_8 = arg_81_0.attachmentCells[var_81_2]

	if var_81_8 and var_81_8.class ~= var_81_4 then
		var_81_8:Clear()

		var_81_8 = nil
		arg_81_0.attachmentCells[var_81_2] = nil
	end

	if var_81_4 then
		if not var_81_8 then
			var_81_8 = var_81_4.New(var_81_3)

			var_81_8:SetLine({
				row = arg_81_1,
				column = arg_81_2
			})

			arg_81_0.attachmentCells[var_81_2] = var_81_8
		end

		var_81_8.info = var_81_1

		for iter_81_0, iter_81_1 in pairs(var_81_5) do
			var_81_8[iter_81_0] = iter_81_1
		end

		var_81_8:Update()
	end
end

function var_0_0.InitWalls(arg_83_0)
	local var_83_0 = arg_83_0.contextData.chapterVO

	for iter_83_0 = arg_83_0.indexMin.x, arg_83_0.indexMax.x do
		for iter_83_1 = arg_83_0.indexMin.y, arg_83_0.indexMax.y do
			local var_83_1 = var_83_0:GetRawChapterCell(iter_83_0, iter_83_1)

			if var_83_1 then
				local var_83_2 = ChapterConst.ForbiddenUp

				while var_83_2 > 0 do
					arg_83_0:InitWallDirection(var_83_1, var_83_2)

					var_83_2 = var_83_2 / 2
				end
			end
		end
	end

	for iter_83_2, iter_83_3 in pairs(arg_83_0.walls) do
		if iter_83_3.WallPrefabs then
			iter_83_3:SetAsset(iter_83_3.WallPrefabs[5 - iter_83_3.BanCount])
		end
	end
end

local var_0_3 = {
	[ChapterConst.ForbiddenUp] = {
		-1,
		0
	},
	[ChapterConst.ForbiddenDown] = {
		1,
		0
	},
	[ChapterConst.ForbiddenLeft] = {
		0,
		-1
	},
	[ChapterConst.ForbiddenRight] = {
		0,
		1
	}
}

function var_0_0.InitWallDirection(arg_84_0, arg_84_1, arg_84_2)
	local var_84_0 = arg_84_0.contextData.chapterVO

	if bit.band(arg_84_1.forbiddenDirections, arg_84_2) == 0 then
		return
	end

	if arg_84_1.walkable == false then
		return
	end

	local var_84_1 = var_0_3[arg_84_2]
	local var_84_2 = 2 * arg_84_1.row + var_84_1[1]
	local var_84_3 = 2 * arg_84_1.column + var_84_1[2]
	local var_84_4 = var_84_0:GetRawChapterCell(arg_84_1.row + var_84_1[1], arg_84_1.column + var_84_1[2])
	local var_84_5 = not var_84_4 or var_84_4.walkable == false
	local var_84_6 = var_84_2 .. "_" .. var_84_3
	local var_84_7 = arg_84_0.walls[var_84_6]

	if not var_84_7 then
		local var_84_8 = var_84_0.theme:GetLinePosition(arg_84_1.row, arg_84_1.column)

		var_84_8.x = var_84_8.x + var_84_1[2] * (var_84_0.theme.cellSize.x + var_84_0.theme.cellSpace.x) * 0.5
		var_84_8.y = var_84_8.y - var_84_1[1] * (var_84_0.theme.cellSize.y + var_84_0.theme.cellSpace.y) * 0.5

		local var_84_9 = WallCell.New(var_84_2, var_84_3, bit.band(arg_84_2, ChapterConst.ForbiddenRow) > 0, var_84_8)

		var_84_9.girdParent = arg_84_0
		arg_84_0.walls[var_84_6] = var_84_9
		var_84_7 = var_84_9

		local var_84_10 = var_84_0.wallAssets[arg_84_1.row .. "_" .. arg_84_1.column]

		if var_84_10 then
			var_84_7.WallPrefabs = var_84_10
		end
	end

	var_84_7.BanCount = var_84_7.BanCount + (var_84_5 and 2 or 1)
end

function var_0_0.UpdateWeatherCells(arg_85_0)
	local var_85_0 = arg_85_0.contextData.chapterVO

	for iter_85_0, iter_85_1 in pairs(var_85_0.cells) do
		local var_85_1
		local var_85_2 = iter_85_1:GetWeatherFlagList()

		if #var_85_2 > 0 then
			var_85_1 = MapWeatherCellView
		end

		local var_85_3 = arg_85_0.weatherCells[iter_85_0]

		if var_85_3 and var_85_3.class ~= var_85_1 then
			var_85_3:Clear()

			var_85_3 = nil
			arg_85_0.weatherCells[iter_85_0] = nil
		end

		if var_85_1 then
			if not var_85_3 then
				local var_85_4 = arg_85_0.cellRoot:Find(iter_85_0):Find(ChapterConst.ChildAttachment)

				var_85_3 = var_85_1.New(var_85_4)

				var_85_3:SetLine({
					row = iter_85_1.row,
					column = iter_85_1.column
				})

				arg_85_0.weatherCells[iter_85_0] = var_85_3
			end

			var_85_3.info = iter_85_1

			var_85_3:Update(var_85_2)
		end
	end
end

function var_0_0.updateQuadCells(arg_86_0, arg_86_1)
	arg_86_1 = arg_86_1 or ChapterConst.QuadStateNormal
	arg_86_0.quadState = arg_86_1

	arg_86_0:updateQuadBase()

	if arg_86_1 == ChapterConst.QuadStateNormal then
		arg_86_0:UpdateQuadStateNormal()
	elseif arg_86_1 == ChapterConst.QuadStateBarrierSetting then
		arg_86_0:UpdateQuadStateBarrierSetting()
	elseif arg_86_1 == ChapterConst.QuadStateTeleportSub then
		arg_86_0:UpdateQuadStateTeleportSub()
	elseif arg_86_1 == ChapterConst.QuadStateMissileStrike or arg_86_1 == ChapterConst.QuadStateAirSuport then
		arg_86_0:UpdateQuadStateMissileStrike()
	elseif arg_86_1 == ChapterConst.QuadStateExpel then
		arg_86_0:UpdateQuadStateAirExpel()
	end

	arg_86_0:UpdateOpBtns()
end

function var_0_0.PlayQuadsParallelAnim(arg_87_0, arg_87_1)
	arg_87_0:frozen()
	table.ParallelIpairsAsync(arg_87_1, function(arg_88_0, arg_88_1, arg_88_2)
		local var_88_0 = ChapterCell.Line2QuadName(arg_88_1.row, arg_88_1.column)
		local var_88_1 = arg_87_0.quadRoot:Find(var_88_0)

		arg_87_0:cancelQuadTween(var_88_0, var_88_1)
		setImageAlpha(var_88_1, 0.4)

		local var_88_2 = LeanTween.scale(var_88_1, Vector3.one, 0.2):setFrom(Vector3.zero):setEase(LeanTweenType.easeInOutSine):setOnComplete(System.Action(arg_88_2))

		arg_87_0.presentTws[var_88_0] = {
			uniqueId = var_88_2.uniqueId
		}
	end, function()
		arg_87_0:unfrozen()
	end)
end

function var_0_0.updateQuadBase(arg_90_0)
	local var_90_0 = arg_90_0.contextData.chapterVO

	if var_90_0.fleet == nil then
		return
	end

	arg_90_0:killPresentTws()

	local function var_90_1(arg_91_0)
		if not arg_91_0 or not arg_91_0:IsWalkable() then
			return
		end

		local var_91_0 = arg_91_0.row
		local var_91_1 = arg_91_0.column
		local var_91_2 = ChapterCell.Line2QuadName(var_91_0, var_91_1)
		local var_91_3 = arg_90_0.quadRoot:Find(var_91_2)

		var_91_3.localScale = Vector3.one

		local var_91_4 = var_91_3:Find("grid"):GetComponent(typeof(Image))
		local var_91_5 = var_90_0:getChampion(var_91_0, var_91_1)

		if var_91_5 and var_91_5.flag == ChapterConst.CellFlagActive and var_91_5.trait ~= ChapterConst.TraitLurk and var_90_0:getChampionVisibility(var_91_5) and not var_90_0:existFleet(FleetType.Transport, var_91_0, var_91_1) then
			arg_90_0:startQuadTween(var_91_2, var_91_3)
			setImageSprite(var_91_3, GetSpriteFromAtlas("chapter/pic/cellgrid", "cell_enemy"))
			setImageSprite(var_91_3:Find("grid"), GetSpriteFromAtlas("chapter/pic/cellgrid", "cell_enemy_grid"))

			var_91_4.material = arg_90_0.material_Add

			return
		end

		local var_91_6 = var_90_0:GetRawChapterAttachemnt(var_91_0, var_91_1)

		if var_91_6 then
			local var_91_7 = var_90_0:getQuadCellPic(var_91_6)

			if var_91_7 then
				arg_90_0:startQuadTween(var_91_2, var_91_3)
				setImageSprite(var_91_3, GetSpriteFromAtlas("chapter/pic/cellgrid", var_91_7))

				return
			end
		end

		if var_90_0:getChapterCell(var_91_0, var_91_1) then
			local var_91_8 = var_90_0:getQuadCellPic(arg_91_0)

			if var_91_8 then
				arg_90_0:startQuadTween(var_91_2, var_91_3)

				if var_91_8 == "cell_enemy" then
					setImageSprite(var_91_3:Find("grid"), GetSpriteFromAtlas("chapter/pic/cellgrid", "cell_enemy_grid"))

					var_91_4.material = arg_90_0.material_Add
				else
					setImageSprite(var_91_3:Find("grid"), GetSpriteFromAtlas("chapter/pic/cellgrid", "cell_grid"))

					var_91_4.material = nil
				end

				setImageSprite(var_91_3, GetSpriteFromAtlas("chapter/pic/cellgrid", var_91_8))

				return
			end
		end

		arg_90_0:cancelQuadTween(var_91_2, var_91_3)
		setImageAlpha(var_91_3, ChapterConst.CellEaseOutAlpha)
		setImageSprite(var_91_3, GetSpriteFromAtlas("chapter/pic/cellgrid", "cell_normal"))
		setImageSprite(var_91_3:Find("grid"), GetSpriteFromAtlas("chapter/pic/cellgrid", "cell_grid"))

		var_91_4.material = nil
	end

	for iter_90_0, iter_90_1 in pairs(var_90_0.cells) do
		var_90_1(iter_90_1)
	end

	if var_90_0:isPlayingWithBombEnemy() then
		arg_90_0:hideQuadMark(ChapterConst.MarkBomb)
	end
end

function var_0_0.UpdateQuadStateNormal(arg_92_0)
	local var_92_0 = arg_92_0.contextData.chapterVO
	local var_92_1 = var_92_0.fleet
	local var_92_2

	if var_92_0:existMoveLimit() and not var_92_0:checkAnyInteractive() then
		var_92_2 = var_92_0:calcWalkableCells(ChapterConst.SubjectPlayer, var_92_1.line.row, var_92_1.line.column, var_92_1:getSpeed())
	end

	if not var_92_2 or #var_92_2 == 0 then
		return
	end

	local var_92_3 = _.min(var_92_2, function(arg_93_0)
		return ManhattonDist(arg_93_0, var_92_1.line)
	end)
	local var_92_4 = ManhattonDist(var_92_3, var_92_1.line)

	_.each(var_92_2, function(arg_94_0)
		local var_94_0 = ChapterCell.Line2QuadName(arg_94_0.row, arg_94_0.column)
		local var_94_1 = arg_92_0.quadRoot:Find(var_94_0)

		arg_92_0:cancelQuadTween(var_94_0, var_94_1)
		setImageSprite(var_94_1, GetSpriteFromAtlas("chapter/pic/cellgrid", "cell_normal"))

		local var_94_2 = var_94_1:Find("grid"):GetComponent(typeof(Image))

		var_94_2.sprite = GetSpriteFromAtlas("chapter/pic/cellgrid", "cell_grid")
		var_94_2.material = nil

		local var_94_3 = var_92_0:getRound() == ChapterConst.RoundPlayer

		setImageAlpha(var_94_1, var_94_3 and 1 or ChapterConst.CellEaseOutAlpha)

		var_94_1.localScale = Vector3.zero

		local var_94_4 = LeanTween.scale(var_94_1, Vector3.one, 0.2):setFrom(Vector3.zero):setEase(LeanTweenType.easeInOutSine):setDelay((ManhattonDist(arg_94_0, var_92_1.line) - var_92_4) * 0.1)

		arg_92_0.presentTws[var_94_0] = {
			uniqueId = var_94_4.uniqueId
		}
	end)
end

function var_0_0.UpdateQuadStateBarrierSetting(arg_95_0)
	local var_95_0 = 1
	local var_95_1 = arg_95_0.contextData.chapterVO
	local var_95_2 = var_95_1.fleet
	local var_95_3 = var_95_2.line
	local var_95_4 = var_95_1:calcSquareBarrierCells(var_95_3.row, var_95_3.column, var_95_0)

	if not var_95_4 or #var_95_4 == 0 then
		return
	end

	local var_95_5 = _.min(var_95_4, function(arg_96_0)
		return ManhattonDist(arg_96_0, var_95_2.line)
	end)
	local var_95_6 = ManhattonDist(var_95_5, var_95_2.line)

	_.each(var_95_4, function(arg_97_0)
		local var_97_0 = ChapterCell.Line2QuadName(arg_97_0.row, arg_97_0.column)
		local var_97_1 = arg_95_0.quadRoot:Find(var_97_0)

		arg_95_0:cancelQuadTween(var_97_0, var_97_1)
		setImageSprite(var_97_1, GetSpriteFromAtlas("chapter/pic/cellgrid", "cell_barrier_select"))

		local var_97_2 = var_97_1:Find("grid"):GetComponent(typeof(Image))

		var_97_2.sprite = GetSpriteFromAtlas("chapter/pic/cellgrid", "cell_grid")
		var_97_2.material = nil

		setImageAlpha(var_97_1, 1)

		var_97_1.localScale = Vector3.zero

		local var_97_3 = LeanTween.scale(var_97_1, Vector3.one, 0.2):setFrom(Vector3.zero):setEase(LeanTweenType.easeInOutSine):setDelay((ManhattonDist(arg_97_0, var_95_2.line) - var_95_6) * 0.1)

		arg_95_0.presentTws[var_97_0] = {
			uniqueId = var_97_3.uniqueId
		}
	end)
end

function var_0_0.UpdateQuadStateTeleportSub(arg_98_0)
	local var_98_0 = arg_98_0.contextData.chapterVO
	local var_98_1 = _.detect(var_98_0.fleets, function(arg_99_0)
		return arg_99_0:getFleetType() == FleetType.Submarine
	end)

	if not var_98_1 then
		return
	end

	local var_98_2 = var_98_0:calcWalkableCells(nil, var_98_1.line.row, var_98_1.line.column, ChapterConst.MaxStep)
	local var_98_3 = _.filter(var_98_2, function(arg_100_0)
		return not var_98_0:getQuadCellPic(var_98_0:getChapterCell(arg_100_0.row, arg_100_0.column))
	end)

	arg_98_0:PlayQuadsParallelAnim(var_98_3)
end

function var_0_0.UpdateQuadStateMissileStrike(arg_101_0)
	local var_101_0 = arg_101_0.contextData.chapterVO
	local var_101_1 = _.filter(_.values(var_101_0.cells), function(arg_102_0)
		return arg_102_0:IsWalkable() and not var_101_0:getQuadCellPic(arg_102_0)
	end)

	arg_101_0:PlayQuadsParallelAnim(var_101_1)
end

function var_0_0.UpdateQuadStateAirExpel(arg_103_0)
	local var_103_0 = arg_103_0.contextData.chapterVO
	local var_103_1 = arg_103_0.airSupportTarget

	if not var_103_1 or not var_103_1.source then
		local var_103_2 = _.filter(_.values(var_103_0.cells), function(arg_104_0)
			return arg_104_0:IsWalkable() and not var_103_0:getQuadCellPic(arg_104_0)
		end)

		arg_103_0:PlayQuadsParallelAnim(var_103_2)

		return
	end

	local var_103_3 = var_103_1.source
	local var_103_4 = var_103_0:calcWalkableCells(ChapterConst.SubjectChampion, var_103_3.row, var_103_3.column, 1)

	arg_103_0:PlayQuadsParallelAnim(var_103_4)
end

function var_0_0.ClickGridCell(arg_105_0, arg_105_1)
	if arg_105_0.quadState == ChapterConst.QuadStateBarrierSetting then
		arg_105_0:OnBarrierSetting(arg_105_1)
	elseif arg_105_0.quadState == ChapterConst.QuadStateTeleportSub then
		arg_105_0:OnTeleportConfirm(arg_105_1)
	elseif arg_105_0.quadState == ChapterConst.QuadStateMissileStrike then
		arg_105_0:OnMissileAiming(arg_105_1)
	elseif arg_105_0.quadState == ChapterConst.QuadStateAirSuport then
		arg_105_0:OnAirSupportAiming(arg_105_1)
	elseif arg_105_0.quadState == ChapterConst.QuadStateExpel then
		arg_105_0:OnAirExpelSelect(arg_105_1)
	else
		arg_105_0:emit(LevelUIConst.ON_CLICK_GRID_QUAD, arg_105_1)
	end
end

function var_0_0.OnBarrierSetting(arg_106_0, arg_106_1)
	local var_106_0 = 1
	local var_106_1 = arg_106_0.contextData.chapterVO
	local var_106_2 = var_106_1.fleet.line
	local var_106_3 = var_106_1:calcSquareBarrierCells(var_106_2.row, var_106_2.column, var_106_0)

	if not _.any(var_106_3, function(arg_107_0)
		return arg_107_0.row == arg_106_1.row and arg_107_0.column == arg_106_1.column
	end) then
		return
	end

	;(function(arg_108_0, arg_108_1)
		newChapterVO = arg_106_0.contextData.chapterVO

		if not newChapterVO:existBarrier(arg_108_0, arg_108_1) and newChapterVO.modelCount <= 0 then
			return
		end

		arg_106_0:emit(LevelMediator2.ON_OP, {
			type = ChapterConst.OpBarrier,
			id = newChapterVO.fleet.id,
			arg1 = arg_108_0,
			arg2 = arg_108_1
		})
	end)(arg_106_1.row, arg_106_1.column)
end

function var_0_0.PrepareSubTeleport(arg_109_0)
	local var_109_0 = arg_109_0.contextData.chapterVO
	local var_109_1 = var_109_0:GetSubmarineFleet()
	local var_109_2 = arg_109_0.cellFleets[var_109_1.id]
	local var_109_3 = var_109_1.startPos

	for iter_109_0, iter_109_1 in pairs(var_109_0.fleets) do
		if iter_109_1:getFleetType() == FleetType.Normal then
			arg_109_0:updateFleet(iter_109_1.id)
		end
	end

	local var_109_4 = var_109_0:existEnemy(ChapterConst.SubjectPlayer, var_109_3.row, var_109_3.column) or var_109_0:existFleet(FleetType.Normal, var_109_3.row, var_109_3.column)

	setActive(var_109_2.tfAmmo, not var_109_4)
	var_109_2:SetActiveModel(true)

	if not (var_109_0.subAutoAttack == 1) then
		arg_109_0:PlaySubAnimation(var_109_2, false, function()
			var_109_2:SetActiveModel(not var_109_4)
		end)
	else
		var_109_2:SetActiveModel(not var_109_4)
	end

	var_109_2.tf.localPosition = var_109_0.theme:GetLinePosition(var_109_3.row, var_109_3.column)

	var_109_2:ResetCanvasOrder()
end

function var_0_0.TurnOffSubTeleport(arg_111_0)
	arg_111_0.subTeleportTargetLine = nil

	local var_111_0 = arg_111_0.contextData.chapterVO

	arg_111_0:hideQuadMark(ChapterConst.MarkMovePathArrow)
	arg_111_0:hideQuadMark(ChapterConst.MarkHuntingRange)
	arg_111_0:ClearEdges("SubmarineHunting")
	arg_111_0:UpdateDestinationMark()

	local var_111_1 = var_111_0:GetSubmarineFleet()
	local var_111_2 = arg_111_0.cellFleets[var_111_1.id]
	local var_111_3 = var_111_0.subAutoAttack == 1

	var_111_2:SetActiveModel(var_111_3)

	if not var_111_3 then
		arg_111_0:PlaySubAnimation(var_111_2, true, function()
			arg_111_0:updateFleet(var_111_1.id)
		end)
	else
		arg_111_0:updateFleet(var_111_1.id)
	end

	arg_111_0:ShowHuntingRange()
end

function var_0_0.OnTeleportConfirm(arg_113_0, arg_113_1)
	local var_113_0 = arg_113_0.contextData.chapterVO
	local var_113_1 = var_113_0:getChapterCell(arg_113_1.row, arg_113_1.column)

	if var_113_1 and var_113_1:IsWalkable() and not var_113_0:existBarrier(arg_113_1.row, arg_113_1.column) then
		local var_113_2 = var_113_0:GetSubmarineFleet()

		if var_113_2.startPos.row == arg_113_1.row and var_113_2.startPos.column == arg_113_1.column then
			return
		end

		local var_113_3, var_113_4 = var_113_0:findPath(nil, var_113_2.startPos, arg_113_1)

		if var_113_3 >= PathFinding.PrioObstacle or arg_113_1.row ~= var_113_4[#var_113_4].row or arg_113_1.column ~= var_113_4[#var_113_4].column then
			return
		end

		arg_113_0:ShowTargetHuntingRange(arg_113_1)
		arg_113_0:UpdateDestinationMark(arg_113_1)

		if var_113_3 > 0 then
			arg_113_0:ShowPathInArrows(var_113_4)

			arg_113_0.subTeleportTargetLine = arg_113_1
		end
	end
end

function var_0_0.ShowPathInArrows(arg_114_0, arg_114_1)
	local var_114_0 = arg_114_0.contextData.chapterVO
	local var_114_1 = Clone(arg_114_1)

	table.remove(var_114_1, #var_114_1)

	for iter_114_0 = #var_114_1, 1, -1 do
		local var_114_2 = var_114_1[iter_114_0]

		if var_114_0:existEnemy(ChapterConst.SubjectPlayer, var_114_2.row, var_114_2.column) or var_114_0:getFleet(FleetType.Normal, var_114_2.row, var_114_2.column) then
			table.remove(var_114_1, iter_114_0)
		end
	end

	arg_114_0:hideQuadMark(ChapterConst.MarkMovePathArrow)
	arg_114_0:showQuadMark(var_114_1, ChapterConst.MarkMovePathArrow, "cell_path_arrow", Vector2(100, 100), nil, true)

	local var_114_3 = arg_114_0.markQuads[ChapterConst.MarkMovePathArrow]

	for iter_114_1 = #arg_114_1, 1, -1 do
		local var_114_4 = arg_114_1[iter_114_1]
		local var_114_5 = ChapterCell.Line2MarkName(var_114_4.row, var_114_4.column, ChapterConst.MarkMovePathArrow)
		local var_114_6 = var_114_3 and var_114_3[var_114_5]

		if var_114_6 then
			local var_114_7 = arg_114_1[iter_114_1 + 1]
			local var_114_8 = Vector3.Normalize(Vector3(var_114_7.column - var_114_4.column, var_114_4.row - var_114_7.row, 0))
			local var_114_9 = Vector3.Dot(var_114_8, Vector3.up)
			local var_114_10 = Mathf.Acos(var_114_9) * Mathf.Rad2Deg
			local var_114_11 = Vector3.Cross(Vector3.up, var_114_8).z > 0 and 1 or -1

			var_114_6.localEulerAngles = Vector3(0, 0, var_114_10 * var_114_11)
		end
	end
end

function var_0_0.ShowMissileAimingMarks(arg_115_0, arg_115_1)
	_.each(arg_115_1, function(arg_116_0)
		arg_115_0.loader:GetPrefabBYGroup("ui/miaozhun02", "miaozhun02", function(arg_117_0)
			setParent(arg_117_0, arg_115_0.restrictMap)

			local var_117_0 = arg_115_0.contextData.chapterVO.theme:GetLinePosition(arg_116_0.row, arg_116_0.column)
			local var_117_1 = arg_115_0.restrictMap.anchoredPosition

			tf(arg_117_0).anchoredPosition = Vector2(var_117_0.x - var_117_1.x, var_117_0.y - var_117_1.y)
		end, "MissileAimingMarks")
	end)
end

function var_0_0.HideMissileAimingMarks(arg_118_0)
	arg_118_0.loader:ReturnGroup("MissileAimingMarks")
end

function var_0_0.ShowMissileAimingMark(arg_119_0, arg_119_1)
	arg_119_0.loader:GetPrefab("ui/miaozhun02", "miaozhun02", function(arg_120_0)
		setParent(arg_120_0, arg_119_0.restrictMap)

		local var_120_0 = arg_119_0.contextData.chapterVO.theme:GetLinePosition(arg_119_1.row, arg_119_1.column)
		local var_120_1 = arg_119_0.restrictMap.anchoredPosition

		tf(arg_120_0).anchoredPosition = Vector2(var_120_0.x - var_120_1.x, var_120_0.y - var_120_1.y)
	end, "MissileAimingMark")
end

function var_0_0.HideMissileAimingMark(arg_121_0)
	arg_121_0.loader:ClearRequest("MissileAimingMark")
end

function var_0_0.OnMissileAiming(arg_122_0, arg_122_1)
	arg_122_0:HideMissileAimingMark()
	arg_122_0:ShowMissileAimingMark(arg_122_1)

	arg_122_0.missileStrikeTargetLine = arg_122_1
end

function var_0_0.ShowAirSupportAimingMark(arg_123_0, arg_123_1)
	arg_123_0.loader:GetPrefab("ui/miaozhun03", "miaozhun03", function(arg_124_0)
		setParent(arg_124_0, arg_123_0.restrictMap)

		local var_124_0 = arg_123_0.contextData.chapterVO.theme:GetLinePosition(arg_123_1.row - 0.5, arg_123_1.column)
		local var_124_1 = arg_123_0.restrictMap.anchoredPosition

		tf(arg_124_0).anchoredPosition = Vector2(var_124_0.x - var_124_1.x, var_124_0.y - var_124_1.y)
	end, "AirSupportAimingMark")
end

function var_0_0.HideAirSupportAimingMark(arg_125_0)
	arg_125_0.loader:ClearRequest("AirSupportAimingMark")
end

function var_0_0.OnAirSupportAiming(arg_126_0, arg_126_1)
	arg_126_0:HideAirSupportAimingMark()
	arg_126_0:ShowAirSupportAimingMark(arg_126_1)

	arg_126_0.missileStrikeTargetLine = arg_126_1
end

function var_0_0.ShowAirExpelAimingMark(arg_127_0)
	local var_127_0 = arg_127_0.airSupportTarget

	if not var_127_0 or not var_127_0.source then
		return
	end

	local var_127_1 = var_127_0.source
	local var_127_2 = ChapterCell.Line2Name(var_127_1.row, var_127_1.column)
	local var_127_3 = arg_127_0.cellRoot:Find(var_127_2)

	local function var_127_4(arg_128_0, arg_128_1)
		setParent(arg_128_0, var_127_3)

		GetOrAddComponent(arg_128_0, typeof(Canvas)).overrideSorting = true

		if not arg_128_1 then
			return
		end

		local var_128_0 = arg_127_0.contextData.chapterVO

		tf(arg_128_0).localEulerAngles = Vector3(-var_128_0.theme.angle, 0, 0)
	end

	arg_127_0.loader:GetPrefabBYGroup("leveluiview/tpl_airsupportmark", "tpl_airsupportmark", function(arg_129_0)
		var_127_4(arg_129_0, true)
	end, "AirExpelAimingMark")
	arg_127_0.loader:GetPrefabBYGroup("leveluiview/tpl_airsupportdirection", "tpl_airsupportdirection", function(arg_130_0)
		var_127_4(arg_130_0)

		local var_130_0 = arg_127_0.contextData.chapterVO
		local var_130_1 = {
			{
				-1,
				0
			},
			{
				0,
				1
			},
			{
				1,
				0
			},
			{
				0,
				-1
			}
		}

		for iter_130_0 = 1, 4 do
			local var_130_2 = tf(arg_130_0):Find(iter_130_0)
			local var_130_3 = var_127_0 and var_130_0:considerAsStayPoint(ChapterConst.SubjectChampion, var_127_1.row + var_130_1[iter_130_0][1], var_127_1.column + var_130_1[iter_130_0][2])

			setActive(var_130_2, var_130_3)
		end
	end, "AirExpelAimingMark")
end

function var_0_0.HideAirExpelAimingMark(arg_131_0)
	arg_131_0.loader:ReturnGroup("AirExpelAimingMark")
end

function var_0_0.OnAirExpelSelect(arg_132_0, arg_132_1)
	local var_132_0 = arg_132_0.contextData.chapterVO

	local function var_132_1()
		arg_132_0:HideAirExpelAimingMark()
		arg_132_0:ShowAirExpelAimingMark()
		arg_132_0:updateQuadBase()
		arg_132_0:UpdateQuadStateAirExpel()
	end

	arg_132_0.airSupportTarget = arg_132_0.airSupportTarget or {}

	local var_132_2 = arg_132_0.airSupportTarget
	local var_132_3 = var_132_0:GetEnemy(arg_132_1.row, arg_132_1.column)

	if var_132_3 then
		if ChapterConst.IsBossCell(var_132_3) then
			pg.TipsMgr.GetInstance():ShowTips(i18n("levelscene_airexpel_select_boss"))

			return
		end

		if var_132_0:existFleet(FleetType.Normal, arg_132_1.row, arg_132_1.column) then
			pg.TipsMgr.GetInstance():ShowTips(i18n("levelscene_airexpel_select_battle"))

			return
		end

		if var_132_2.source and table.equal(var_132_2.source:GetLine(), var_132_3:GetLine()) then
			var_132_3 = nil
		end

		var_132_2.source = var_132_3

		var_132_1()
	elseif not var_132_2.source then
		pg.TipsMgr.GetInstance():ShowTips(i18n("levelscene_airexpel_select_enemy"))
	elseif ManhattonDist(var_132_2.source, arg_132_1) > 1 then
		pg.TipsMgr.GetInstance():ShowTips(i18n("levelscene_airexpel_outrange"))
	elseif not var_132_0:considerAsStayPoint(ChapterConst.SubjectChampion, arg_132_1.row, arg_132_1.column) then
		pg.TipsMgr.GetInstance():ShowTips(i18n("levelscene_airexpel_outrange"))
	else
		local var_132_4 = arg_132_0.airSupportTarget.source
		local var_132_5 = arg_132_1

		if not var_132_4 or not var_132_5 then
			return
		end

		local var_132_6 = {
			arg_132_1.row - var_132_4.row,
			arg_132_1.column - var_132_4.column
		}
		local var_132_7 = {
			"up",
			"right",
			"down",
			"left"
		}
		local var_132_8

		if var_132_6[1] ~= 0 then
			var_132_8 = var_132_6[1] + 2
		else
			var_132_8 = 3 - var_132_6[2]
		end

		local var_132_9 = var_132_7[var_132_8]
		local var_132_10 = var_132_0:getChapterSupportFleet()

		local function var_132_11()
			arg_132_0:emit(LevelMediator2.ON_OP, {
				type = ChapterConst.OpStrategy,
				id = var_132_10.id,
				arg1 = ChapterConst.StrategyExpel,
				arg2 = var_132_4.row,
				arg3 = var_132_4.column,
				arg4 = var_132_5.row,
				arg5 = var_132_5.column
			})
		end

		local var_132_12 = var_132_4.attachmentId
		local var_132_13 = pg.expedition_data_template[var_132_12].name

		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			content = i18n("levelscene_airexpel_select_confirm_" .. var_132_9, var_132_13),
			onYes = var_132_11
		})
	end
end

function var_0_0.CleanAirSupport(arg_135_0)
	arg_135_0.airSupportTarget = nil
end

function var_0_0.startQuadTween(arg_136_0, arg_136_1, arg_136_2, arg_136_3, arg_136_4)
	if arg_136_0.presentTws[arg_136_1] then
		LeanTween.cancel(arg_136_0.presentTws[arg_136_1].uniqueId)

		arg_136_0.presentTws[arg_136_1] = nil
	end

	if not arg_136_0.quadTws[arg_136_1] then
		arg_136_3 = arg_136_3 or 1
		arg_136_4 = arg_136_4 or ChapterConst.CellEaseOutAlpha

		setImageAlpha(arg_136_2, arg_136_3)

		local var_136_0 = LeanTween.alpha(arg_136_2, arg_136_4, 1):setLoopPingPong()

		arg_136_0.quadTws[arg_136_1] = {
			tw = var_136_0,
			uniqueId = var_136_0.uniqueId
		}
	end
end

function var_0_0.cancelQuadTween(arg_137_0, arg_137_1, arg_137_2)
	if arg_137_0.quadTws[arg_137_1] then
		LeanTween.cancel(arg_137_0.quadTws[arg_137_1].uniqueId)

		arg_137_0.quadTws[arg_137_1] = nil
	end

	setImageAlpha(arg_137_2, ChapterConst.CellEaseOutAlpha)
end

function var_0_0.killQuadTws(arg_138_0)
	for iter_138_0, iter_138_1 in pairs(arg_138_0.quadTws) do
		LeanTween.cancel(iter_138_1.uniqueId)
	end

	arg_138_0.quadTws = {}
end

function var_0_0.killPresentTws(arg_139_0)
	for iter_139_0, iter_139_1 in pairs(arg_139_0.presentTws) do
		LeanTween.cancel(iter_139_1.uniqueId)
	end

	arg_139_0.presentTws = {}
end

function var_0_0.startMarkTween(arg_140_0, arg_140_1, arg_140_2, arg_140_3, arg_140_4)
	if not arg_140_0.markTws[arg_140_1] then
		arg_140_3 = arg_140_3 or 1
		arg_140_4 = arg_140_4 or 0.2

		setImageAlpha(arg_140_2, arg_140_3)

		local var_140_0 = LeanTween.alpha(arg_140_2, arg_140_4, 0.7):setLoopPingPong():setEase(LeanTweenType.easeInOutSine):setDelay(1)

		arg_140_0.markTws[arg_140_1] = {
			tw = var_140_0,
			uniqueId = var_140_0.uniqueId
		}
	end
end

function var_0_0.cancelMarkTween(arg_141_0, arg_141_1, arg_141_2, arg_141_3)
	if arg_141_0.markTws[arg_141_1] then
		LeanTween.cancel(arg_141_0.markTws[arg_141_1].uniqueId)

		arg_141_0.markTws[arg_141_1] = nil
	end

	setImageAlpha(arg_141_2, arg_141_3 or ChapterConst.CellEaseOutAlpha)
end

function var_0_0.moveFleet(arg_142_0, arg_142_1, arg_142_2, arg_142_3, arg_142_4)
	local var_142_0 = arg_142_0.contextData.chapterVO
	local var_142_1 = var_142_0.fleet
	local var_142_2 = var_142_1.id
	local var_142_3 = arg_142_0.cellFleets[var_142_2]

	var_142_3:SetSpineVisible(true)
	setActive(var_142_3.tfShadow, true)
	setActive(arg_142_0.arrowTarget, true)
	arg_142_0:updateTargetArrow(arg_142_2[#arg_142_2])

	if arg_142_3 then
		arg_142_0:updateAttachment(arg_142_3.row, arg_142_3.column)
	end

	local function var_142_4(arg_143_0)
		var_142_1.step = var_142_1.step + 1

		if arg_142_0.onShipStepChange then
			arg_142_0.onShipStepChange(arg_143_0)
		end
	end

	local function var_142_5(arg_144_0)
		return
	end

	local function var_142_6()
		setActive(arg_142_0.arrowTarget, false)

		local var_145_0 = var_142_0.fleet.line
		local var_145_1 = var_142_0:getChapterCell(var_145_0.row, var_145_0.column)

		if ChapterConst.NeedClearStep(var_145_1) then
			var_142_1.step = 0
		end

		var_142_1.rotation = var_142_3:GetRotatePivot().transform.localRotation

		arg_142_0:updateAttachment(var_145_0.row, var_145_0.column)
		arg_142_0:updateFleet(var_142_2)
		arg_142_0:updateOni()

		local var_145_2 = var_142_0:getChampionIndex(var_145_0.row, var_145_0.column)

		if var_145_2 then
			arg_142_0:updateChampion(var_145_2)
		end

		if arg_142_0.onShipArrived then
			arg_142_0.onShipArrived()
		end

		if arg_142_4 then
			arg_142_4()
		end
	end

	arg_142_0:updateQuadCells(ChapterConst.QuadStateFrozen)
	arg_142_0:moveCellView(var_142_3, arg_142_1, arg_142_2, var_142_4, var_142_5, var_142_6)
end

function var_0_0.moveSub(arg_146_0, arg_146_1, arg_146_2, arg_146_3, arg_146_4)
	local var_146_0 = arg_146_0.contextData.chapterVO
	local var_146_1 = var_146_0.fleets[arg_146_1]
	local var_146_2 = arg_146_0.cellFleets[var_146_1.id]
	local var_146_3 = arg_146_2[#arg_146_2]

	local function var_146_4(arg_147_0)
		return
	end

	local function var_146_5(arg_148_0)
		return
	end

	local function var_146_6()
		local var_149_0 = var_146_0:existEnemy(ChapterConst.SubjectPlayer, var_146_3.row, var_146_3.column) or var_146_0:existAlly(var_146_1)
		local var_149_1 = var_146_0.subAutoAttack == 1

		var_146_2:SetActiveModel(not var_149_0 and var_149_1)

		var_146_1.rotation = var_146_2:GetRotatePivot().transform.localRotation

		if arg_146_4 then
			arg_146_4()
		end
	end

	arg_146_0:updateQuadCells(ChapterConst.QuadStateFrozen)
	arg_146_0:teleportSubView(var_146_2, var_146_2:GetLine(), var_146_3, var_146_4, var_146_5, var_146_6)
end

function var_0_0.moveChampion(arg_150_0, arg_150_1, arg_150_2, arg_150_3, arg_150_4)
	local var_150_0 = arg_150_0.contextData.chapterVO
	local var_150_1 = var_150_0.champions[arg_150_1]
	local var_150_2 = arg_150_0.cellChampions[arg_150_1]

	local function var_150_3(arg_151_0)
		return
	end

	local function var_150_4(arg_152_0)
		return
	end

	local function var_150_5()
		if var_150_2.GetRotatePivot then
			var_150_1.rotation = var_150_2:GetRotatePivot().transform.localRotation
		end

		if arg_150_4 then
			arg_150_4()
		end
	end

	if var_150_0:getChampionVisibility(var_150_1) then
		arg_150_0:moveCellView(var_150_2, arg_150_2, arg_150_3, var_150_3, var_150_4, var_150_5)
	else
		local var_150_6 = arg_150_2[#arg_150_2]

		var_150_2:RefreshLinePosition(var_150_0, var_150_6)
		var_150_5()
	end
end

function var_0_0.moveTransport(arg_154_0, arg_154_1, arg_154_2, arg_154_3, arg_154_4)
	local var_154_0 = arg_154_0.contextData.chapterVO.fleets[arg_154_1]
	local var_154_1 = arg_154_0.cellFleets[var_154_0.id]

	local function var_154_2(arg_155_0)
		return
	end

	local function var_154_3(arg_156_0)
		return
	end

	local function var_154_4()
		var_154_0.rotation = var_154_1:GetRotatePivot().transform.localRotation

		arg_154_0:updateFleet(var_154_0.id)
		existCall(arg_154_4)
	end

	arg_154_0:updateQuadCells(ChapterConst.QuadStateFrozen)
	arg_154_0:moveCellView(var_154_1, arg_154_2, arg_154_3, var_154_2, var_154_3, var_154_4)
end

function var_0_0.moveCellView(arg_158_0, arg_158_1, arg_158_2, arg_158_3, arg_158_4, arg_158_5, arg_158_6)
	local var_158_0 = arg_158_0.contextData.chapterVO
	local var_158_1

	local function var_158_2()
		if var_158_1 and coroutine.status(var_158_1) == "suspended" then
			local var_159_0, var_159_1 = coroutine.resume(var_158_1)

			assert(var_159_0, debug.traceback(var_158_1, var_159_1))
		end
	end

	var_158_1 = coroutine.create(function()
		arg_158_0:frozen()

		local var_160_0 = var_158_0:GetQuickPlayFlag() and ChapterConst.ShipStepQuickPlayScale or 1
		local var_160_1 = 0.3 * var_160_0
		local var_160_2 = ChapterConst.ShipStepDuration * ChapterConst.ShipMoveTailLength * var_160_0
		local var_160_3 = 0.1 * var_160_0
		local var_160_4 = 0

		table.insert(arg_158_3, 1, arg_158_1:GetLine())
		_.each(arg_158_3, function(arg_161_0)
			local var_161_0 = var_158_0:getChapterCell(arg_161_0.row, arg_161_0.column)

			if ChapterConst.NeedEasePathCell(var_161_0) then
				local var_161_1 = ChapterCell.Line2QuadName(var_161_0.row, var_161_0.column)
				local var_161_2 = arg_158_0.quadRoot:Find(var_161_1)

				arg_158_0:cancelQuadTween(var_161_1, var_161_2)
				LeanTween.alpha(var_161_2, 1, var_160_1):setDelay(var_160_4)

				var_160_4 = var_160_4 + var_160_3
			end
		end)
		_.each(arg_158_2, function(arg_162_0)
			arg_158_0:moveStep(arg_158_1, arg_162_0, arg_158_3[#arg_158_3], function()
				local var_163_0 = arg_158_1:GetLine()
				local var_163_1 = var_158_0:getChapterCell(var_163_0.row, var_163_0.column)

				if ChapterConst.NeedEasePathCell(var_163_1) then
					local var_163_2 = ChapterCell.Line2QuadName(var_163_1.row, var_163_1.column)
					local var_163_3 = arg_158_0.quadRoot:Find(var_163_2)

					LeanTween.scale(var_163_3, Vector3.zero, var_160_2)
				end

				arg_158_4(arg_162_0)
				arg_158_1:SetLine(arg_162_0)
				arg_158_1:ResetCanvasOrder()
			end, function()
				arg_158_5(arg_162_0)
				var_158_2()
			end)
			coroutine.yield()
		end)
		_.each(arg_158_3, function(arg_165_0)
			local var_165_0 = var_158_0:getChapterCell(arg_165_0.row, arg_165_0.column)

			if ChapterConst.NeedEasePathCell(var_165_0) then
				local var_165_1 = ChapterCell.Line2QuadName(var_165_0.row, var_165_0.column)
				local var_165_2 = arg_158_0.quadRoot:Find(var_165_1)

				LeanTween.cancel(var_165_2.gameObject)
				setImageAlpha(var_165_2, ChapterConst.CellEaseOutAlpha)

				var_165_2.localScale = Vector3.one
			end
		end)

		if arg_158_0.exited then
			return
		end

		if arg_158_1.GetAction then
			arg_158_1:SetAction(ChapterConst.ShipIdleAction)
		end

		arg_158_6()
		arg_158_0:unfrozen()
	end)

	var_158_2()
end

function var_0_0.moveStep(arg_166_0, arg_166_1, arg_166_2, arg_166_3, arg_166_4, arg_166_5)
	local var_166_0 = arg_166_0.contextData.chapterVO
	local var_166_1 = var_166_0:GetQuickPlayFlag() and ChapterConst.ShipStepQuickPlayScale or 1
	local var_166_2

	if arg_166_1.GetRotatePivot then
		var_166_2 = arg_166_1:GetRotatePivot()
	end

	local var_166_3 = arg_166_1:GetLine()

	if arg_166_1.GetAction then
		arg_166_1:SetAction(ChapterConst.ShipMoveAction)
	end

	if not IsNil(var_166_2) and (arg_166_2.column ~= var_166_3.column or arg_166_3.column ~= var_166_3.column) then
		tf(var_166_2).localRotation = Quaternion.identity

		if arg_166_2.column < var_166_3.column or arg_166_2.column == var_166_3.column and arg_166_3.column < var_166_3.column then
			tf(var_166_2).localRotation = Quaternion.Euler(0, 180, 0)
		end
	end

	local var_166_4 = arg_166_1.tf.localPosition
	local var_166_5 = var_166_0.theme:GetLinePosition(arg_166_2.row, arg_166_2.column)
	local var_166_6 = 0

	LeanTween.value(arg_166_1.go, 0, 1, ChapterConst.ShipStepDuration * var_166_1):setOnComplete(System.Action(arg_166_5)):setOnUpdate(System.Action_float(function(arg_167_0)
		arg_166_1.tf.localPosition = Vector3.Lerp(var_166_4, var_166_5, arg_167_0)

		if var_166_6 <= 0.5 and arg_167_0 > 0.5 then
			arg_166_4()
		end

		var_166_6 = arg_167_0
	end))
end

function var_0_0.teleportSubView(arg_168_0, arg_168_1, arg_168_2, arg_168_3, arg_168_4, arg_168_5, arg_168_6)
	local var_168_0 = arg_168_0.contextData.chapterVO

	local function var_168_1()
		arg_168_4(arg_168_3)
		arg_168_1:RefreshLinePosition(var_168_0, arg_168_3)
		arg_168_5(arg_168_3)
		arg_168_0:PlaySubAnimation(arg_168_1, false, arg_168_6)
	end

	arg_168_0:PlaySubAnimation(arg_168_1, true, var_168_1)
end

function var_0_0.CellToScreen(arg_170_0, arg_170_1, arg_170_2)
	local var_170_0 = arg_170_0._tf:Find(ChapterConst.PlaneName .. "/cells")

	assert(var_170_0, "plane not exist.")

	local var_170_1 = arg_170_0.contextData.chapterVO.theme
	local var_170_2 = var_170_1:GetLinePosition(arg_170_1, arg_170_2)
	local var_170_3 = var_170_2.y

	var_170_2.y = var_170_3 * math.cos(math.pi / 180 * var_170_1.angle)
	var_170_2.z = var_170_3 * math.sin(math.pi / 180 * var_170_1.angle)

	local var_170_4 = arg_170_0.levelCam.transform:GetChild(0)
	local var_170_5 = var_170_0.transform.lossyScale.x
	local var_170_6 = var_170_0.position + var_170_2 * var_170_5
	local var_170_7 = arg_170_0.levelCam:WorldToViewportPoint(var_170_6)

	return Vector3(var_170_4.rect.width * (var_170_7.x - 0.5), var_170_4.rect.height * (var_170_7.y - 0.5))
end

local var_0_4 = {
	{
		1,
		0
	},
	{
		0,
		-1
	},
	{
		-1,
		0
	},
	{
		0,
		1
	}
}
local var_0_5 = {
	{
		1,
		1
	},
	{
		1,
		-1
	},
	{
		-1,
		-1
	},
	{
		-1,
		1
	}
}

function var_0_0.AddCellEdge(arg_171_0, arg_171_1, arg_171_2, ...)
	local var_171_0 = 0
	local var_171_1 = 1

	for iter_171_0 = 1, 4 do
		if not _.any(arg_171_1, function(arg_172_0)
			return arg_172_0.row == arg_171_2.row + var_0_4[iter_171_0][1] and arg_172_0.column == arg_171_2.column + var_0_4[iter_171_0][2]
		end) then
			var_171_0 = bit.bor(var_171_0, var_171_1)
		end

		var_171_1 = var_171_1 * 2
	end

	if var_171_0 == 0 then
		return
	end

	arg_171_0:CreateEdge(var_171_0, arg_171_2, ...)
end

function var_0_0.AddOutlines(arg_173_0, arg_173_1, arg_173_2, arg_173_3, arg_173_4, arg_173_5)
	local var_173_0 = {}
	local var_173_1 = {}

	for iter_173_0, iter_173_1 in ipairs(arg_173_1) do
		for iter_173_2 = 1, 4 do
			if not underscore.any(arg_173_1, function(arg_174_0)
				return arg_174_0.row == iter_173_1.row + var_0_4[iter_173_2][1] and arg_174_0.column == iter_173_1.column + var_0_4[iter_173_2][2]
			end) then
				local var_173_2 = 2 * iter_173_1.row + var_0_4[iter_173_2][1]
				local var_173_3 = 2 * iter_173_1.column + var_0_4[iter_173_2][2]

				assert(not var_173_0[var_173_2 .. "_" .. var_173_3], "Multiple outline")

				var_173_0[var_173_2 .. "_" .. var_173_3] = {
					row = var_173_2,
					column = var_173_3,
					normal = iter_173_2
				}
			end

			if not underscore.any(arg_173_1, function(arg_175_0)
				return arg_175_0.row == iter_173_1.row + var_0_5[iter_173_2][1] and arg_175_0.column == iter_173_1.column + var_0_5[iter_173_2][2]
			end) and underscore.any(arg_173_1, function(arg_176_0)
				return arg_176_0.row == iter_173_1.row and arg_176_0.column == iter_173_1.column + var_0_5[iter_173_2][2]
			end) and underscore.any(arg_173_1, function(arg_177_0)
				return arg_177_0.row == iter_173_1.row + var_0_5[iter_173_2][1] and arg_177_0.column == iter_173_1.column
			end) then
				var_173_1[iter_173_1.row .. "_" .. iter_173_1.column .. "_" .. iter_173_2] = {
					row = iter_173_1.row,
					column = iter_173_1.column,
					corner = iter_173_2
				}
			end
		end
	end

	arg_173_0:CreateOutlines(var_173_0, arg_173_2, arg_173_3, arg_173_4, arg_173_5)
	arg_173_0:CreateOutlineCorners(var_173_1, arg_173_2, arg_173_3, arg_173_4, arg_173_5 .. "_corner")
end

function var_0_0.isHuntingRangeVisible(arg_178_0)
	return arg_178_0.contextData.huntingRangeVisibility % 2 == 0
end

function var_0_0.toggleHuntingRange(arg_179_0)
	arg_179_0:hideQuadMark(ChapterConst.MarkHuntingRange)
	arg_179_0:ClearEdges("SubmarineHunting")

	if not arg_179_0:isHuntingRangeVisible() then
		arg_179_0:ShowHuntingRange()
	end

	arg_179_0.contextData.huntingRangeVisibility = 1 - arg_179_0.contextData.huntingRangeVisibility

	arg_179_0:updateAttachments()
	arg_179_0:updateChampions()
end

function var_0_0.ShowHuntingRange(arg_180_0)
	local var_180_0 = arg_180_0.contextData.chapterVO
	local var_180_1 = var_180_0:GetSubmarineFleet()

	if not var_180_1 then
		return
	end

	local var_180_2 = var_180_1:getHuntingRange()
	local var_180_3 = _.filter(var_180_2, function(arg_181_0)
		local var_181_0 = var_180_0:getChapterCell(arg_181_0.row, arg_181_0.column)

		return var_181_0 and var_181_0:IsWalkable()
	end)

	arg_180_0:RefreshHuntingRange(var_180_3, false)
end

function var_0_0.RefreshHuntingRange(arg_182_0, arg_182_1, arg_182_2)
	arg_182_0:showQuadMark(arg_182_1, ChapterConst.MarkHuntingRange, "cell_hunting_range", Vector2(100, 100), arg_182_0.material_Add, arg_182_2)
	_.each(arg_182_1, function(arg_183_0)
		arg_182_0:AddCellEdge(arg_182_1, arg_183_0, not arg_182_2, nil, nil, "SubmarineHunting")
	end)
end

function var_0_0.ShowStaticHuntingRange(arg_184_0)
	arg_184_0:hideQuadMark(ChapterConst.MarkHuntingRange)
	arg_184_0:ClearEdges("SubmarineHunting")

	local var_184_0 = arg_184_0.contextData.chapterVO
	local var_184_1 = var_184_0:GetSubmarineFleet()

	if not arg_184_0:isHuntingRangeVisible() then
		arg_184_0.contextData.huntingRangeVisibility = arg_184_0.contextData.huntingRangeVisibility + 1
	end

	local var_184_2 = var_184_1:getHuntingRange()
	local var_184_3 = _.filter(var_184_2, function(arg_185_0)
		local var_185_0 = var_184_0:getChapterCell(arg_185_0.row, arg_185_0.column)

		return var_185_0 and var_185_0:IsWalkable()
	end)

	arg_184_0:RefreshHuntingRange(var_184_3, true)
end

function var_0_0.ShowTargetHuntingRange(arg_186_0, arg_186_1)
	arg_186_0:hideQuadMark(ChapterConst.MarkHuntingRange)
	arg_186_0:ClearEdges("SubmarineHunting")

	local var_186_0 = arg_186_0.contextData.chapterVO
	local var_186_1 = var_186_0:GetSubmarineFleet()
	local var_186_2 = var_186_1:getHuntingRange(arg_186_1)
	local var_186_3 = _.filter(var_186_2, function(arg_187_0)
		local var_187_0 = var_186_0:getChapterCell(arg_187_0.row, arg_187_0.column)

		return var_187_0 and var_187_0:IsWalkable()
	end)
	local var_186_4 = var_186_1:getHuntingRange()
	local var_186_5 = _.filter(var_186_4, function(arg_188_0)
		local var_188_0 = var_186_0:getChapterCell(arg_188_0.row, arg_188_0.column)

		return var_188_0 and var_188_0:IsWalkable()
	end)
	local var_186_6 = {}

	for iter_186_0, iter_186_1 in pairs(var_186_5) do
		if not table.containsData(var_186_3, iter_186_1) then
			table.insert(var_186_6, iter_186_1)
		end
	end

	arg_186_0:RefreshHuntingRange(var_186_6, true)
	arg_186_0:RefreshHuntingRange(var_186_3, false)
	arg_186_0:updateAttachments()
	arg_186_0:updateChampions()
end

function var_0_0.OnChangeSubAutoAttack(arg_189_0)
	local var_189_0 = arg_189_0.contextData.chapterVO
	local var_189_1 = var_189_0:GetSubmarineFleet()

	if not var_189_1 then
		return
	end

	local var_189_2 = arg_189_0.cellFleets[var_189_1.id]

	if not var_189_2 then
		return
	end

	local var_189_3 = var_189_0.subAutoAttack == 1

	var_189_2:SetActiveModel(not var_189_3)
	arg_189_0:PlaySubAnimation(var_189_2, not var_189_3, function()
		arg_189_0:updateFleet(var_189_1.id)
	end)
end

function var_0_0.displayEscapeGrid(arg_191_0)
	local var_191_0 = arg_191_0.contextData.chapterVO

	if not var_191_0:existOni() then
		return
	end

	local var_191_1 = var_191_0:getOniChapterInfo()

	arg_191_0:hideQuadMark(ChapterConst.MarkEscapeGrid)
	arg_191_0:showQuadMark(_.map(var_191_1.escape_grids, function(arg_192_0)
		return {
			row = arg_192_0[1],
			column = arg_192_0[2]
		}
	end), ChapterConst.MarkEscapeGrid, "cell_escape_grid", Vector2(105, 105))
end

function var_0_0.showQuadMark(arg_193_0, arg_193_1, arg_193_2, arg_193_3, arg_193_4, arg_193_5, arg_193_6)
	arg_193_0:ShowAnyQuadMark(arg_193_1, arg_193_2, arg_193_3, arg_193_4, arg_193_5, false, arg_193_6)
end

function var_0_0.ShowTopQuadMark(arg_194_0, arg_194_1, arg_194_2, arg_194_3, arg_194_4, arg_194_5, arg_194_6)
	arg_194_0:ShowAnyQuadMark(arg_194_1, arg_194_2, arg_194_3, arg_194_4, arg_194_5, true, arg_194_6)
end

function var_0_0.ShowAnyQuadMark(arg_195_0, arg_195_1, arg_195_2, arg_195_3, arg_195_4, arg_195_5, arg_195_6, arg_195_7)
	local var_195_0 = arg_195_0.contextData.chapterVO

	for iter_195_0, iter_195_1 in pairs(arg_195_1) do
		local var_195_1 = var_195_0:getChapterCell(iter_195_1.row, iter_195_1.column)

		if var_195_1 and var_195_1:IsWalkable() then
			local var_195_2 = ChapterCell.Line2MarkName(iter_195_1.row, iter_195_1.column, arg_195_2)

			arg_195_0.markQuads[arg_195_2] = arg_195_0.markQuads[arg_195_2] or {}

			local var_195_3 = arg_195_0.markQuads[arg_195_2][var_195_2]

			if not var_195_3 then
				PoolMgr.GetInstance():GetPrefab("chapter/cell_quad_mark", "", false, function(arg_196_0)
					var_195_3 = arg_196_0.transform
					arg_195_0.markQuads[arg_195_2][var_195_2] = var_195_3
				end)
			else
				arg_195_0:cancelMarkTween(var_195_2, var_195_3, 1)
			end

			var_195_3.name = var_195_2

			var_195_3:SetParent(arg_195_6 and arg_195_0.topMarkRoot or arg_195_0.bottomMarkRoot, false)

			var_195_3.sizeDelta = var_195_0.theme.cellSize
			var_195_3.anchoredPosition = var_195_0.theme:GetLinePosition(iter_195_1.row, iter_195_1.column)
			var_195_3.localScale = Vector3.one

			var_195_3:SetAsLastSibling()

			local var_195_4 = var_195_3:GetComponent(typeof(Image))

			var_195_4.sprite = GetSpriteFromAtlas("chapter/pic/cellgrid", arg_195_3)
			var_195_4.material = arg_195_5
			var_195_3.sizeDelta = arg_195_4

			if not arg_195_7 then
				arg_195_0:startMarkTween(var_195_2, var_195_3)
			else
				arg_195_0:cancelMarkTween(var_195_2, var_195_3, 1)
			end
		end
	end
end

function var_0_0.hideQuadMark(arg_197_0, arg_197_1)
	if arg_197_1 and not arg_197_0.markQuads[arg_197_1] then
		return
	end

	for iter_197_0, iter_197_1 in pairs(arg_197_0.markQuads) do
		if not arg_197_1 or iter_197_0 == arg_197_1 then
			for iter_197_2, iter_197_3 in pairs(iter_197_1) do
				arg_197_0:cancelMarkTween(iter_197_2, iter_197_3)

				iter_197_1[iter_197_2]:GetComponent(typeof(Image)).material = nil
				iter_197_1[iter_197_2] = nil

				PoolMgr.GetInstance():ReturnPrefab("chapter/cell_quad_mark", "", iter_197_3.gameObject)
			end

			table.clear(arg_197_0.markQuads[iter_197_0])
		end
	end
end

function var_0_0.CreateEdgeIndex(arg_198_0, arg_198_1, arg_198_2, arg_198_3)
	return ChapterCell.Line2Name(arg_198_0, arg_198_1) .. (arg_198_3 and "_" .. arg_198_3 or "") .. "_" .. arg_198_2
end

function var_0_0.CreateEdge(arg_199_0, arg_199_1, arg_199_2, arg_199_3, arg_199_4, arg_199_5, arg_199_6)
	if arg_199_1 <= 0 or arg_199_1 >= 16 then
		return
	end

	local var_199_0 = arg_199_0:GetEdgePool(arg_199_6)
	local var_199_1 = arg_199_0.contextData.chapterVO
	local var_199_2 = var_199_1.theme:GetLinePosition(arg_199_2.row, arg_199_2.column)
	local var_199_3 = var_199_1.theme.cellSize

	assert(arg_199_6, "Missing key, Please PM Programmer")

	local var_199_4 = 1
	local var_199_5 = 0

	while var_199_5 < 4 do
		var_199_5 = var_199_5 + 1

		if bit.band(arg_199_1, var_199_4) > 0 then
			local var_199_6 = arg_199_0.CreateEdgeIndex(arg_199_2.row, arg_199_2.column, var_199_5, arg_199_6)

			arg_199_0.cellEdges[arg_199_6] = arg_199_0.cellEdges[arg_199_6] or {}
			arg_199_0.cellEdges[arg_199_6][var_199_6] = arg_199_0.cellEdges[arg_199_6][var_199_6] or tf(var_199_0:Dequeue())

			local var_199_7 = arg_199_0.cellEdges[arg_199_6][var_199_6]

			var_199_7.name = var_199_6

			var_199_7:SetParent(arg_199_0.bottomMarkRoot, false)

			arg_199_4 = arg_199_4 or 0
			arg_199_5 = arg_199_5 or 3

			local var_199_8 = bit.band(var_199_5, 1) == 1 and var_199_3.x - arg_199_4 * 2 or var_199_3.y - arg_199_4 * 2
			local var_199_9 = arg_199_5

			var_199_7.sizeDelta = Vector2.New(var_199_8, var_199_9)
			var_199_7.pivot = Vector2.New(0.5, 0)

			local var_199_10 = math.pi * 0.5 * -var_199_5
			local var_199_11 = math.cos(var_199_10) * (var_199_3.x * 0.5 - arg_199_4)
			local var_199_12 = math.sin(var_199_10) * (var_199_3.y * 0.5 - arg_199_4)

			var_199_7.anchoredPosition = Vector2.New(var_199_11 + var_199_2.x, var_199_12 + var_199_2.y)
			var_199_7.localRotation = Quaternion.Euler(0, 0, (5 - var_199_5) * 90)

			if arg_199_3 then
				arg_199_0:startMarkTween(var_199_6, var_199_7)
			else
				arg_199_0:cancelMarkTween(var_199_6, var_199_7, 1)
			end
		end

		var_199_4 = var_199_4 * 2
	end
end

function var_0_0.ClearEdge(arg_200_0, arg_200_1)
	for iter_200_0, iter_200_1 in pairs(arg_200_0.cellEdges) do
		for iter_200_2 = 1, 4 do
			local var_200_0 = arg_200_0.CreateEdgeIndex(arg_200_1.row, arg_200_1.column, iter_200_2, iter_200_0)

			if iter_200_1[var_200_0] then
				local var_200_1 = arg_200_0:GetEdgePool(iter_200_0)
				local var_200_2 = tf(iter_200_1[var_200_0])

				arg_200_0:cancelMarkTween(var_200_0, var_200_2)
				var_200_1:Enqueue(var_200_2, false)

				iter_200_1[var_200_0] = nil
			end
		end
	end
end

function var_0_0.ClearEdges(arg_201_0, arg_201_1)
	if not next(arg_201_0.cellEdges) then
		return
	end

	for iter_201_0, iter_201_1 in pairs(arg_201_0.cellEdges) do
		if not arg_201_1 or arg_201_1 == iter_201_0 then
			local var_201_0 = arg_201_0:GetEdgePool(iter_201_0)

			for iter_201_2, iter_201_3 in pairs(iter_201_1) do
				arg_201_0:cancelMarkTween(iter_201_2, iter_201_3)
				var_201_0:Enqueue(go(iter_201_3), false)
			end

			arg_201_0.cellEdges[iter_201_0] = nil
		end
	end
end

function var_0_0.CreateOutlines(arg_202_0, arg_202_1, arg_202_2, arg_202_3, arg_202_4, arg_202_5)
	local var_202_0 = arg_202_0.contextData.chapterVO
	local var_202_1 = var_202_0.theme.cellSize + var_202_0.theme.cellSpace

	for iter_202_0, iter_202_1 in pairs(arg_202_1) do
		local var_202_2 = arg_202_0:GetEdgePool(arg_202_5)
		local var_202_3 = var_202_0.theme:GetLinePosition(iter_202_1.row / 2, iter_202_1.column / 2)

		assert(arg_202_5, "Missing key, Please PM Programmer")

		local var_202_4 = arg_202_0.CreateEdgeIndex(iter_202_1.row, iter_202_1.column, 0, arg_202_5)

		arg_202_0.cellEdges[arg_202_5] = arg_202_0.cellEdges[arg_202_5] or {}
		arg_202_0.cellEdges[arg_202_5][var_202_4] = arg_202_0.cellEdges[arg_202_5][var_202_4] or tf(var_202_2:Dequeue())

		local var_202_5 = arg_202_0.cellEdges[arg_202_5][var_202_4]

		var_202_5.name = var_202_4

		var_202_5:SetParent(arg_202_0.bottomMarkRoot, false)

		arg_202_3 = arg_202_3 or 0
		arg_202_4 = arg_202_4 or 3

		local var_202_6 = var_0_4[iter_202_1.normal][1] ~= 0 and var_202_1.x or var_202_1.y
		local var_202_7 = arg_202_4
		local var_202_8 = var_202_6 * 0.5
		local var_202_9 = iter_202_1.normal % 4 + 1
		local var_202_10 = (iter_202_1.normal + 2) % 4 + 1
		local var_202_11 = {
			iter_202_1.row + var_0_4[var_202_9][1],
			iter_202_1.column + var_0_4[var_202_9][2]
		}
		local var_202_12 = arg_202_1[var_202_11[1] + var_0_4[iter_202_1.normal][1] .. "_" .. var_202_11[2] + var_0_4[iter_202_1.normal][2]] or arg_202_1[var_202_11[1] - var_0_4[iter_202_1.normal][1] .. "_" .. var_202_11[2] - var_0_4[iter_202_1.normal][2]]
		local var_202_13 = {
			iter_202_1.row + var_0_4[var_202_10][1],
			iter_202_1.column + var_0_4[var_202_10][2]
		}
		local var_202_14 = arg_202_1[var_202_13[1] + var_0_4[iter_202_1.normal][1] .. "_" .. var_202_13[2] + var_0_4[iter_202_1.normal][2]] or arg_202_1[var_202_13[1] - var_0_4[iter_202_1.normal][1] .. "_" .. var_202_13[2] - var_0_4[iter_202_1.normal][2]]

		if var_202_12 then
			local var_202_15 = iter_202_1.row + var_0_4[iter_202_1.normal][1] == var_202_12.row + var_0_4[var_202_12.normal][1] or iter_202_1.column + var_0_4[iter_202_1.normal][2] == var_202_12.column + var_0_4[var_202_12.normal][2]

			var_202_6 = var_202_15 and var_202_6 + arg_202_3 or var_202_6 - arg_202_3
			var_202_8 = var_202_15 and var_202_8 + arg_202_3 or var_202_8 - arg_202_3
		end

		if var_202_14 then
			var_202_6 = (iter_202_1.row + var_0_4[iter_202_1.normal][1] == var_202_14.row + var_0_4[var_202_14.normal][1] or iter_202_1.column + var_0_4[iter_202_1.normal][2] == var_202_14.column + var_0_4[var_202_14.normal][2]) and var_202_6 + arg_202_3 or var_202_6 - arg_202_3
		end

		var_202_5.sizeDelta = Vector2.New(var_202_6, var_202_7)
		var_202_5.pivot = Vector2.New(var_202_8 / var_202_6, 0)

		local var_202_16 = var_0_4[iter_202_1.normal][2] * -arg_202_3
		local var_202_17 = var_0_4[iter_202_1.normal][1] * arg_202_3

		var_202_5.anchoredPosition = Vector2.New(var_202_16 + var_202_3.x, var_202_17 + var_202_3.y)
		var_202_5.localRotation = Quaternion.Euler(0, 0, (5 - iter_202_1.normal) * 90)

		if arg_202_2 then
			arg_202_0:startMarkTween(var_202_4, var_202_5)
		else
			arg_202_0:cancelMarkTween(var_202_4, var_202_5, 1)
		end
	end
end

function var_0_0.CreateOutlineCorners(arg_203_0, arg_203_1, arg_203_2, arg_203_3, arg_203_4, arg_203_5)
	local var_203_0 = arg_203_0.contextData.chapterVO

	for iter_203_0, iter_203_1 in pairs(arg_203_1) do
		local var_203_1 = arg_203_0:GetEdgePool(arg_203_5)
		local var_203_2 = var_203_0.theme:GetLinePosition(iter_203_1.row + var_0_5[iter_203_1.corner][1] * 0.5, iter_203_1.column + var_0_5[iter_203_1.corner][2] * 0.5)

		assert(arg_203_5, "Missing key, Please PM Programmer")

		local var_203_3 = arg_203_0.CreateEdgeIndex(iter_203_1.row, iter_203_1.column, iter_203_1.corner, arg_203_5)

		arg_203_0.cellEdges[arg_203_5] = arg_203_0.cellEdges[arg_203_5] or {}
		arg_203_0.cellEdges[arg_203_5][var_203_3] = arg_203_0.cellEdges[arg_203_5][var_203_3] or tf(var_203_1:Dequeue())

		local var_203_4 = arg_203_0.cellEdges[arg_203_5][var_203_3]

		var_203_4.name = var_203_3

		var_203_4:SetParent(arg_203_0.bottomMarkRoot, false)

		arg_203_3 = arg_203_3 or 0
		arg_203_4 = arg_203_4 or 3

		local var_203_5 = arg_203_4
		local var_203_6 = arg_203_4

		var_203_4.sizeDelta = Vector2.New(var_203_5, var_203_6)
		var_203_4.pivot = Vector2.New(1, 0)

		local var_203_7 = var_0_5[iter_203_1.corner][2] * -arg_203_3
		local var_203_8 = var_0_5[iter_203_1.corner][1] * arg_203_3

		var_203_4.anchoredPosition = Vector2.New(var_203_7 + var_203_2.x, var_203_8 + var_203_2.y)
		var_203_4.localRotation = Quaternion.Euler(0, 0, (5 - iter_203_1.corner) * 90)

		if arg_203_2 then
			arg_203_0:startMarkTween(var_203_3, var_203_4)
		else
			arg_203_0:cancelMarkTween(var_203_3, var_203_4, 1)
		end
	end
end

function var_0_0.updateCoastalGunAttachArea(arg_204_0)
	local var_204_0 = arg_204_0.contextData.chapterVO:getCoastalGunArea()

	arg_204_0:hideQuadMark(ChapterConst.MarkCoastalGun)
	arg_204_0:showQuadMark(var_204_0, ChapterConst.MarkCoastalGun, "cell_coastal_gun", Vector2(110, 110), nil, false)
end

function var_0_0.InitIdolsAnim(arg_205_0)
	local var_205_0 = arg_205_0.contextData.chapterVO
	local var_205_1 = pg.chapter_pop_template[var_205_0.id]

	if not var_205_1 then
		return
	end

	local var_205_2 = var_205_1.sd_location

	for iter_205_0, iter_205_1 in ipairs(var_205_2) do
		arg_205_0.idols = arg_205_0.idols or {}

		local var_205_3 = ChapterCell.Line2Name(iter_205_1[1][1], iter_205_1[1][2])
		local var_205_4 = arg_205_0.cellRoot:Find(var_205_3 .. "/" .. ChapterConst.ChildAttachment)

		assert(var_205_4, "cant find attachment")

		local var_205_5 = AttachmentSpineAnimationCell.New(var_205_4)

		var_205_5:SetLine({
			row = iter_205_1[1][1],
			column = iter_205_1[1][2]
		})
		table.insert(arg_205_0.idols, var_205_5)
		var_205_5:Set(iter_205_1[2])
		var_205_5:SetRoutine(var_205_1.sd_act[iter_205_0])
	end
end

function var_0_0.ClearIdolsAnim(arg_206_0)
	if arg_206_0.idols then
		for iter_206_0, iter_206_1 in ipairs(arg_206_0.idols) do
			iter_206_1:Clear()
		end

		table.clear(arg_206_0.idols)

		arg_206_0.idols = nil
	end
end

function var_0_0.GetEnemyCellView(arg_207_0, arg_207_1)
	local var_207_0 = _.detect(arg_207_0.cellChampions, function(arg_208_0)
		local var_208_0 = arg_208_0:GetLine()

		return var_208_0.row == arg_207_1.row and var_208_0.column == arg_207_1.column
	end)

	if not var_207_0 then
		local var_207_1 = ChapterCell.Line2Name(arg_207_1.row, arg_207_1.column)

		var_207_0 = arg_207_0.attachmentCells[var_207_1]
	end

	return var_207_0
end

function var_0_0.TransformLine2PlanePos(arg_209_0, arg_209_1)
	local var_209_0 = string.char(string.byte("A") + arg_209_1.column - arg_209_0.indexMin.y)
	local var_209_1 = string.char(string.byte("1") + arg_209_1.row - arg_209_0.indexMin.x)

	return var_209_0 .. var_209_1
end

function var_0_0.AlignListContainer(arg_210_0, arg_210_1)
	local var_210_0 = arg_210_0.childCount

	for iter_210_0 = arg_210_1, var_210_0 - 1 do
		local var_210_1 = arg_210_0:GetChild(iter_210_0)

		setActive(var_210_1, false)
	end

	for iter_210_1 = var_210_0, arg_210_1 - 1 do
		cloneTplTo(arg_210_0:GetChild(0), arg_210_0)
	end

	for iter_210_2 = 0, arg_210_1 - 1 do
		local var_210_2 = arg_210_0:GetChild(iter_210_2)

		setActive(var_210_2, true)
	end
end

function var_0_0.frozen(arg_211_0)
	arg_211_0.forzenCount = (arg_211_0.forzenCount or 0) + 1

	arg_211_0.parent:frozen()
end

function var_0_0.unfrozen(arg_212_0)
	if arg_212_0.exited then
		return
	end

	arg_212_0.forzenCount = (arg_212_0.forzenCount or 0) - 1

	arg_212_0.parent:unfrozen()
end

function var_0_0.isfrozen(arg_213_0)
	return arg_213_0.parent.frozenCount > 0
end

function var_0_0.clear(arg_214_0)
	arg_214_0:clearAll()

	if (arg_214_0.forzenCount or 0) > 0 then
		arg_214_0.parent:unfrozen(arg_214_0.forzenCount)
	end
end

return var_0_0
