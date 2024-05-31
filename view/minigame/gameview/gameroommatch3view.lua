﻿local var_0_0 = class("GameRoomMatch3View", import("..BaseMiniGameView"))
local var_0_1 = 6
local var_0_2 = 7
local var_0_3 = -405
local var_0_4 = -275
local var_0_5 = 135
local var_0_6 = 110
local var_0_7 = false
local var_0_8 = 0.1
local var_0_9 = 0
local var_0_10 = 0.3
local var_0_11 = 0.5
local var_0_12 = 100
local var_0_13 = 0.2
local var_0_14 = 0.4
local var_0_15 = 180
local var_0_16 = 60
local var_0_17 = 3
local var_0_18 = 2
local var_0_19 = 0.3
local var_0_20 = 0.3
local var_0_21 = 2.5
local var_0_22 = "event:/ui/ddldaoshu2"
local var_0_23 = "event:/ui/boat_drag"
local var_0_24 = "event:/ui/break_out_full"
local var_0_25 = "event:/ui/sx-good"
local var_0_26 = "event:/ui/sx-perfect"
local var_0_27 = "event:/ui/sx-jishu"
local var_0_28 = "event:/ui/furnitrue_save"

function var_0_0.getUIName(arg_1_0)
	return "GameRoomMatch3UI"
end

function var_0_0.getBGM(arg_2_0)
	return "backyard"
end

function var_0_0.init(arg_3_0)
	arg_3_0.matchEffect = arg_3_0:findTF("effects/sanxiaoxiaoshi")
	arg_3_0.goodEffect = arg_3_0:findTF("effects/sanxiaoGood")
	arg_3_0.greatEffect = arg_3_0:findTF("effects/sanxiaoGreat")
	arg_3_0.perfectEffect = arg_3_0:findTF("effects/sanxiaoPerfect")
	arg_3_0.hintEffect = arg_3_0:findTF("effects/hint")
	arg_3_0.selectedEffect = arg_3_0:findTF("effects/selected")
	arg_3_0.whitenMat = arg_3_0:findTF("effects/whiten"):GetComponent("Image").material
	arg_3_0.backBtn = arg_3_0:findTF("button/back")
	arg_3_0.mainPage = arg_3_0:findTF("main")
	arg_3_0.startBtn = arg_3_0:findTF("main/start")
	arg_3_0.helpBtn = arg_3_0:findTF("main/rule")
	arg_3_0.countdownPage = arg_3_0:findTF("countdown")
	arg_3_0.countdownAnim = arg_3_0:findTF("countdown")
	arg_3_0.gamePage = arg_3_0:findTF("game")
	arg_3_0.gameMask = arg_3_0:findTF("game/mask")
	arg_3_0.warning = arg_3_0:findTF("game/warning")
	arg_3_0.countdownTf = arg_3_0:findTF("game/countdown")
	arg_3_0.countdownText = arg_3_0:findTF("game/countdown/Text")
	arg_3_0.inf = arg_3_0:findTF("game/countdown/inf")
	arg_3_0.scoreText = arg_3_0:findTF("game/score/Text")
	arg_3_0.floatText = arg_3_0:findTF("game/floatText")
	arg_3_0.floatChar = {}
	arg_3_0.pausePage = arg_3_0:findTF("game/pause")
	arg_3_0.pauseYes = arg_3_0:findTF("game/pause/yes")
	arg_3_0.pauseNo = arg_3_0:findTF("game/pause/no")

	for iter_3_0 = 0, 9 do
		arg_3_0.floatChar[iter_3_0] = arg_3_0:findTF("game/floatText/" .. iter_3_0)
	end

	arg_3_0.tilesRoot = arg_3_0:findTF("game/tiles")
	arg_3_0.gameListener = arg_3_0.tilesRoot:GetComponent("EventTriggerListener")
	arg_3_0.longPressListener = arg_3_0.tilesRoot:GetComponent("UILongPressTrigger")
	arg_3_0.endPage = arg_3_0:findTF("end")
	arg_3_0.endBtn = arg_3_0:findTF("end/end_btn")
	arg_3_0.endScore = arg_3_0:findTF("end/score/Text")
	arg_3_0.newSign = arg_3_0:findTF("end/score/Text/new")
	arg_3_0.bestScore = arg_3_0:findTF("end/highest/Text")
	arg_3_0.tiles = {
		arg_3_0:findTF("tiles/Akashi"),
		arg_3_0:findTF("tiles/Ayanami"),
		arg_3_0:findTF("tiles/Javelin"),
		arg_3_0:findTF("tiles/Laffey"),
		arg_3_0:findTF("tiles/Z23")
	}
end

function var_0_0.onBackPressed(arg_4_0)
	if isActive(arg_4_0.mainPage) then
		arg_4_0:emit(var_0_0.ON_BACK)
	elseif isActive(arg_4_0.pausePage) then
		triggerButton(arg_4_0.pauseNo)
	elseif isActive(arg_4_0.gamePage) then
		arg_4_0:pause()
	elseif isActive(arg_4_0.endPage) and arg_4_0.endBtn:GetComponent("Button").enabled then
		triggerButton(arg_4_0.endBtn)
	end
end

function var_0_0.didEnter(arg_5_0)
	onButton(arg_5_0, arg_5_0.backBtn, function()
		arg_5_0:onBackPressed()
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0.startBtn, function()
		arg_5_0:openCoinLayer(false)

		if var_0_7 then
			setActive(arg_5_0.mainPage, false)
			setActive(arg_5_0.gamePage, true)
			arg_5_0:startGame()
		else
			arg_5_0.mainPage:GetComponent("CanvasGroup").blocksRaycasts = false

			arg_5_0:managedTween(LeanTween.value, function()
				arg_5_0.mainPage:GetComponent("CanvasGroup").alpha = 1
				arg_5_0.mainPage:GetComponent("CanvasGroup").blocksRaycasts = true

				setActive(arg_5_0.mainPage, false)
				setActive(arg_5_0.countdownPage, true)
				pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_0_22)
			end, go(arg_5_0.mainPage), 1, 0, var_0_20):setOnUpdate(System.Action_float(function(arg_9_0)
				arg_5_0.mainPage:GetComponent("CanvasGroup").alpha = arg_9_0
			end))
		end
	end)

	if arg_5_0:getGameRoomData() then
		arg_5_0.gameHelpTip = arg_5_0:getGameRoomData().game_help
	end

	onButton(arg_5_0, arg_5_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = arg_5_0.gameHelpTip
		})
	end, SFX_PANEL)
	arg_5_0.countdownAnim:GetComponent(typeof(DftAniEvent)):SetEndEvent(function(arg_11_0)
		setActive(arg_5_0.countdownPage, false)
		setActive(arg_5_0.gamePage, true)
		arg_5_0:startGame()
	end)
	onButton(arg_5_0, arg_5_0.endBtn, function()
		arg_5_0.mainPage:GetComponent("CanvasGroup").blocksRaycasts = false

		arg_5_0:managedTween(LeanTween.value, function()
			arg_5_0.mainPage:GetComponent("CanvasGroup").alpha = 1
			arg_5_0.mainPage:GetComponent("CanvasGroup").blocksRaycasts = true
		end, go(arg_5_0.endPage), 0, 1, var_0_20):setOnUpdate(System.Action_float(function(arg_14_0)
			arg_5_0.mainPage:GetComponent("CanvasGroup").alpha = arg_14_0
		end))
		setActive(arg_5_0.mainPage, true)
		setActive(arg_5_0.countdownPage, false)
		setActive(arg_5_0.gamePage, false)
		setActive(arg_5_0.endPage, false)
		arg_5_0:openCoinLayer(true)
	end)
	onButton(arg_5_0, arg_5_0.pauseYes, function()
		arg_5_0:stopGame()
	end)
	onButton(arg_5_0, arg_5_0.pauseNo, function()
		setActive(arg_5_0.pausePage, false)
		arg_5_0:resumeGame()
	end)

	local var_5_0 = false

	arg_5_0.gameListener:AddPointClickFunc(function(arg_17_0, arg_17_1)
		if var_5_0 then
			var_5_0 = false

			return
		end

		if arg_5_0.updating then
			return
		end

		if not arg_5_0.inGame then
			return
		end

		local var_17_0 = LuaHelper.ScreenToLocal(arg_5_0.tilesRoot, arg_17_1.position, GameObject.Find("UICamera"):GetComponent(typeof(Camera)))
		local var_17_1, var_17_2 = arg_5_0:pos2index(var_17_0)

		if arg_5_0.selected then
			if arg_5_0.selected == arg_5_0.tileTfs[var_17_1][var_17_2] then
				arg_5_0:unselect()
			elseif math.abs(var_17_1 - arg_5_0.selectedIndex.i) + math.abs(var_17_2 - arg_5_0.selectedIndex.j) == 1 then
				arg_5_0:tryMoveTo({
					i = var_17_1,
					j = var_17_2
				})
			else
				arg_5_0:select(var_17_1, var_17_2)
			end
		else
			arg_5_0:select(var_17_1, var_17_2)
		end
	end)
	arg_5_0.longPressListener.onLongPressed:AddListener(function()
		if arg_5_0.updating then
			return
		end

		if not arg_5_0.inGame then
			return
		end

		local var_18_0 = LuaHelper.ScreenToLocal(arg_5_0.tilesRoot, Input.mousePosition, GameObject.Find("UICamera"):GetComponent(typeof(Camera)))
		local var_18_1, var_18_2 = arg_5_0:pos2index(var_18_0)

		arg_5_0:unselect()
		arg_5_0:animate(var_18_1, var_18_2, true)
	end)
	arg_5_0.gameListener:AddBeginDragFunc(function(arg_19_0, arg_19_1)
		if arg_5_0.updating then
			return
		end

		if not arg_5_0.inGame then
			return
		end

		var_5_0 = true

		local var_19_0 = arg_19_1.delta
		local var_19_1 = LuaHelper.ScreenToLocal(arg_5_0.tilesRoot, arg_19_1.position, GameObject.Find("UICamera"):GetComponent(typeof(Camera)))
		local var_19_2, var_19_3 = arg_5_0:pos2index(var_19_1)

		arg_5_0:animate(var_19_2, var_19_3, false)
		arg_5_0:unselect()

		arg_5_0.selected = arg_5_0.tileTfs[var_19_2][var_19_3]
		arg_5_0.selectedIndex = {
			i = var_19_2,
			j = var_19_3
		}

		if math.abs(var_19_0.x) > math.abs(var_19_0.y) then
			var_19_2 = 0
			var_19_3 = var_19_0.x > 0 and 1 or -1
		else
			var_19_2 = var_19_0.y > 0 and 1 or -1
			var_19_3 = 0
		end

		arg_5_0:tryMoveTo({
			i = arg_5_0.selectedIndex.i + var_19_2,
			j = arg_5_0.selectedIndex.j + var_19_3
		})
	end)
	setActive(arg_5_0.mainPage, true)
	arg_5_0:updateData()
end

function var_0_0.updateData(arg_20_0)
	arg_20_0.infinite = arg_20_0:GetMGHubData().count == 0

	local var_20_0 = arg_20_0:GetMGData():GetRuntimeData("elements")

	arg_20_0.best = var_20_0 and var_20_0[1] or 0
end

function var_0_0.index2pos(arg_21_0, arg_21_1, arg_21_2)
	return Vector3.New(var_0_3 + (arg_21_2 - 1) * var_0_5, var_0_4 + (arg_21_1 - 1) * var_0_6)
end

function var_0_0.pos2index(arg_22_0, arg_22_1)
	local var_22_0 = var_0_3 - var_0_5 / 2
	local var_22_1 = var_0_4 - var_0_6 / 2

	return math.ceil((arg_22_1.y - var_22_1) / var_0_6), math.ceil((arg_22_1.x - var_22_0) / var_0_5)
end

function var_0_0.dropTime(arg_23_0)
	return math.max(arg_23_0 * var_0_8, var_0_9)
end

function var_0_0.cancelHint(arg_24_0)
	if arg_24_0.hint then
		Destroy(arg_24_0.hint)
		arg_24_0.hint1:GetComponent("Animator"):SetBool("selected", false)
		arg_24_0.hint2:GetComponent("Animator"):SetBool("selected", false)

		arg_24_0.hint = nil
		arg_24_0.hint1 = nil
		arg_24_0.hint2 = nil
	end
end

local var_0_29 = {
	{
		0,
		1
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
		1,
		0
	}
}

function var_0_0.unselect(arg_25_0)
	if arg_25_0.selectedEffectTf then
		Destroy(arg_25_0.selectedEffectTf)

		arg_25_0.selectedEffectTf = nil
	end

	if arg_25_0.selected then
		arg_25_0:animate(arg_25_0.selectedIndex.i, arg_25_0.selectedIndex.j, false)

		arg_25_0.selected = nil
		arg_25_0.selectedIndex = nil

		arg_25_0:reorderTiles()
	end
end

function var_0_0.select(arg_26_0, arg_26_1, arg_26_2)
	arg_26_0:unselect()

	arg_26_0.selected = arg_26_0.tileTfs[arg_26_1][arg_26_2]
	arg_26_0.selectedIndex = {
		i = arg_26_1,
		j = arg_26_2
	}
	arg_26_0.selectedEffectTf = rtf(cloneTplTo(arg_26_0.selectedEffect, arg_26_0.tilesRoot))
	arg_26_0.selectedEffectTf.anchoredPosition = arg_26_0.selected.anchoredPosition

	arg_26_0.selected:SetAsLastSibling()
	arg_26_0:animate(arg_26_1, arg_26_2, true)
end

function var_0_0.animate(arg_27_0, arg_27_1, arg_27_2, arg_27_3)
	if not arg_27_0.tileTfs[arg_27_1][arg_27_2] then
		warning("bad position", arg_27_1, arg_27_2)
	end

	arg_27_0.tileTfs[arg_27_1][arg_27_2]:GetComponent("Animator"):SetBool("selected", arg_27_3)

	for iter_27_0, iter_27_1 in pairs(var_0_29) do
		local var_27_0 = arg_27_0.tileTfs[arg_27_1 + iter_27_1[1]][arg_27_2 + iter_27_1[2]]

		if var_27_0 then
			var_27_0:GetComponent("Animator"):SetBool("selected", arg_27_3)
		end
	end

	if arg_27_0.hint then
		arg_27_0.hint1:GetComponent("Animator"):SetBool("selected", true)
		arg_27_0.hint2:GetComponent("Animator"):SetBool("selected", true)
	end
end

function var_0_0.tryMoveTo(arg_28_0, arg_28_1)
	if arg_28_0.selectedIndex == nil then
		return
	end

	if arg_28_0.hintTimer then
		arg_28_0.hintTimer:Pause()
	end

	if not arg_28_0.tileIndicies[arg_28_1.i][arg_28_1.j] then
		return
	end

	pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_0_23)

	if arg_28_0:moveValid(arg_28_0.selectedIndex, arg_28_1) then
		local var_28_0 = arg_28_0.selectedIndex

		arg_28_0:unselect()

		arg_28_0.updating = true

		arg_28_0:swap(var_28_0, arg_28_1)
		arg_28_0:managedTween(LeanTween.delayedCall, function()
			if not arg_28_0.inGame then
				return
			end

			arg_28_0.combo = 0

			arg_28_0:update()
		end, var_0_13, nil)
	else
		local var_28_1 = arg_28_0.tileTfs[arg_28_0.selectedIndex.i][arg_28_0.selectedIndex.j]
		local var_28_2 = arg_28_0.tileTfs[arg_28_1.i][arg_28_1.j]
		local var_28_3 = arg_28_0:index2pos(arg_28_0.selectedIndex.i, arg_28_0.selectedIndex.j)
		local var_28_4 = arg_28_0:index2pos(arg_28_1.i, arg_28_1.j)

		arg_28_0:managedTween(LeanTween.move, nil, var_28_1, var_28_4, var_0_13):setLoopPingPong(1)
		arg_28_0:managedTween(LeanTween.move, nil, var_28_2, var_28_3, var_0_13):setLoopPingPong(1)

		arg_28_0.updating = true

		arg_28_0:managedTween(LeanTween.delayedCall, function()
			arg_28_0.updating = false

			arg_28_0.hintTimer:Resume()
		end, var_0_13 * 2 + 0.1, nil)
		arg_28_0:unselect()
	end
end

local var_0_30 = {
	{
		{
			0,
			-2
		},
		{
			0,
			-1
		}
	},
	{
		{
			0,
			-1
		},
		{
			0,
			1
		}
	},
	{
		{
			0,
			1
		},
		{
			0,
			2
		}
	}
}

function var_0_0.isConnected(arg_31_0, arg_31_1)
	for iter_31_0, iter_31_1 in pairs(var_0_30) do
		local var_31_0
		local var_31_1
		local var_31_2
		local var_31_3 = arg_31_0.tileIndicies[arg_31_1.i][arg_31_1.j]
		local var_31_4 = arg_31_0.tileIndicies[arg_31_1.i + iter_31_1[1][1]][arg_31_1.j + iter_31_1[1][2]]
		local var_31_5 = arg_31_0.tileIndicies[arg_31_1.i + iter_31_1[2][1]][arg_31_1.j + iter_31_1[2][2]]

		if var_31_3 == var_31_4 and var_31_3 == var_31_5 then
			return true
		end

		local var_31_6 = arg_31_0.tileIndicies[arg_31_1.i + iter_31_1[1][2]][arg_31_1.j + iter_31_1[1][1]]
		local var_31_7 = arg_31_0.tileIndicies[arg_31_1.i + iter_31_1[2][2]][arg_31_1.j + iter_31_1[2][1]]

		if var_31_3 == var_31_6 and var_31_3 == var_31_7 then
			return true
		end
	end

	return false
end

function var_0_0.moveValid(arg_32_0, arg_32_1, arg_32_2)
	arg_32_0.tileIndicies[arg_32_1.i][arg_32_1.j], arg_32_0.tileIndicies[arg_32_2.i][arg_32_2.j] = arg_32_0.tileIndicies[arg_32_2.i][arg_32_2.j], arg_32_0.tileIndicies[arg_32_1.i][arg_32_1.j]

	local var_32_0 = arg_32_0:isConnected(arg_32_1) or arg_32_0:isConnected(arg_32_2)

	arg_32_0.tileIndicies[arg_32_1.i][arg_32_1.j], arg_32_0.tileIndicies[arg_32_2.i][arg_32_2.j] = arg_32_0.tileIndicies[arg_32_2.i][arg_32_2.j], arg_32_0.tileIndicies[arg_32_1.i][arg_32_1.j]

	return var_32_0
end

function var_0_0.moveTile(arg_33_0, arg_33_1, arg_33_2, arg_33_3)
	local var_33_0 = arg_33_0:index2pos(arg_33_2.i, arg_33_2.j)

	arg_33_0:managedTween(LeanTween.move, nil, arg_33_1, var_33_0, arg_33_3 or 0):setEase(LeanTweenType.easeInQuad)
end

function var_0_0.swap(arg_34_0, arg_34_1, arg_34_2)
	local var_34_0 = arg_34_0.tileTfs[arg_34_1.i][arg_34_1.j]
	local var_34_1 = arg_34_0.tileTfs[arg_34_2.i][arg_34_2.j]

	arg_34_0:moveTile(var_34_0, arg_34_2, var_0_13)
	arg_34_0:moveTile(var_34_1, arg_34_1, var_0_13)

	arg_34_0.tileTfs[arg_34_1.i][arg_34_1.j], arg_34_0.tileTfs[arg_34_2.i][arg_34_2.j] = arg_34_0.tileTfs[arg_34_2.i][arg_34_2.j], arg_34_0.tileTfs[arg_34_1.i][arg_34_1.j]
	arg_34_0.tileIndicies[arg_34_1.i][arg_34_1.j], arg_34_0.tileIndicies[arg_34_2.i][arg_34_2.j] = arg_34_0.tileIndicies[arg_34_2.i][arg_34_2.j], arg_34_0.tileIndicies[arg_34_1.i][arg_34_1.j]
end

function var_0_0.formatTime(arg_35_0, arg_35_1)
	local var_35_0 = math.floor(arg_35_1 / 60)

	arg_35_1 = arg_35_1 - var_35_0 * 60

	local var_35_1 = math.floor(arg_35_1)

	return var_35_0 .. ":" .. var_35_1
end

function dir2Angle(arg_36_0)
	if arg_36_0[1] == 1 then
		return -90
	elseif arg_36_0[1] == -1 then
		return 90
	elseif arg_36_0[2] == 1 then
		return 180
	elseif arg_36_0[2] == -1 then
		return 0
	end
end

function var_0_0.startGame(arg_37_0)
	arg_37_0:updateData()

	local var_37_0 = Timer.New(function()
		arg_37_0:managedTween(LeanTween.value, function()
			arg_37_0.gamePage:GetComponent("CanvasGroup").alpha = 1

			arg_37_0:stopGame()
		end, go(arg_37_0.gamePage), 1, 0, var_0_10):setOnUpdate(System.Action_float(function(arg_40_0)
			arg_37_0.gamePage:GetComponent("CanvasGroup").alpha = arg_40_0
		end))
		UpdateBeat:RemoveListener(arg_37_0.handle)
	end, arg_37_0.infinite and var_0_15 or var_0_16)

	arg_37_0.handle = UpdateBeat:CreateListener(function()
		setText(arg_37_0.countdownText, math.floor(var_37_0.time))

		if var_37_0.time <= var_0_17 and not isActive(arg_37_0.warning) then
			setActive(arg_37_0.warning, true)
		end
	end, arg_37_0)

	var_37_0:Start()
	UpdateBeat:AddListener(arg_37_0.handle)

	arg_37_0.timer = var_37_0

	setActive(arg_37_0.inf, false)
	setActive(arg_37_0.countdownText, true)

	arg_37_0.tileIndicies = {}

	for iter_37_0 = -1, var_0_1 + 2 do
		arg_37_0.tileIndicies[iter_37_0] = {}
	end

	arg_37_0.tileTfs = {}

	for iter_37_1 = -1, var_0_1 + 2 do
		arg_37_0.tileTfs[iter_37_1] = {}
	end

	arg_37_0:fillTileIndicies()
	arg_37_0:fillTiles(true)

	arg_37_0.selected = nil
	arg_37_0.updating = false
	arg_37_0.score = 0
	arg_37_0.combo = 0
	arg_37_0.inGame = true

	setText(arg_37_0.scoreText, arg_37_0.score)

	function arg_37_0.hintFunc()
		if arg_37_0.hint then
			return
		end

		local var_42_0, var_42_1, var_42_2 = arg_37_0:findMove()
		local var_42_3

		var_42_3.anchoredPosition, var_42_3 = (arg_37_0:index2pos(var_42_0, var_42_1) + arg_37_0:index2pos(var_42_0 + var_42_2[1], var_42_1 + var_42_2[2])) / 2, rtf(cloneTplTo(arg_37_0.hintEffect, arg_37_0.tilesRoot))
		var_42_3.localEulerAngles = Vector3.New(0, 0, dir2Angle(var_42_2))
		arg_37_0.hint = var_42_3
		arg_37_0.hint1 = arg_37_0.tileTfs[var_42_0][var_42_1]
		arg_37_0.hint2 = arg_37_0.tileTfs[var_42_0 + var_42_2[1]][var_42_1 + var_42_2[2]]

		arg_37_0.hint1:GetComponent("Animator"):SetBool("selected", true)
		arg_37_0.hint2:GetComponent("Animator"):SetBool("selected", true)
	end

	arg_37_0.hintTimer = Timer.New(arg_37_0.hintFunc, var_0_21)

	arg_37_0.hintTimer:Start()
end

function var_0_0.pauseGame(arg_43_0)
	if arg_43_0.timer then
		arg_43_0.timer:Pause()
	end

	if arg_43_0.hintTimer then
		arg_43_0.hintTimer:Pause()
	end

	if arg_43_0.warning then
		arg_43_0.warning:GetComponent("Animator").enabled = false
	end

	arg_43_0:pauseManagedTween()
end

function var_0_0.pause(arg_44_0)
	setActive(arg_44_0.pausePage, true)
	arg_44_0:pauseGame()
end

function var_0_0.resumeGame(arg_45_0)
	if arg_45_0.timer then
		arg_45_0.timer:Resume()
	end

	if arg_45_0.hintTimer then
		arg_45_0.hintTimer:Resume()
	end

	if arg_45_0.warning then
		arg_45_0.warning:GetComponent("Animator").enabled = true
	end

	arg_45_0:resumeManagedTween()
end

function var_0_0.fillTileIndicies(arg_46_0)
	local var_46_0 = {}

	for iter_46_0 = -1, var_0_1 + 2 do
		var_46_0[iter_46_0] = {}

		for iter_46_1 = 1, var_0_2 do
			var_46_0[iter_46_0][iter_46_1] = arg_46_0.tileIndicies[iter_46_0][iter_46_1]
		end
	end

	repeat
		arg_46_0.tileIndicies = {}

		for iter_46_2 = -1, var_0_1 + 2 do
			arg_46_0.tileIndicies[iter_46_2] = {}

			for iter_46_3 = 1, var_0_2 do
				arg_46_0.tileIndicies[iter_46_2][iter_46_3] = var_46_0[iter_46_2][iter_46_3]
			end
		end

		for iter_46_4 = 1, var_0_1 do
			for iter_46_5 = 1, var_0_2 do
				if not arg_46_0.tileIndicies[iter_46_4][iter_46_5] then
					local var_46_1
					local var_46_2

					if arg_46_0.tileIndicies[iter_46_4 - 1][iter_46_5] and arg_46_0.tileIndicies[iter_46_4 - 1][iter_46_5] == arg_46_0.tileIndicies[iter_46_4 - 2][iter_46_5] then
						var_46_1 = arg_46_0.tileIndicies[iter_46_4 - 1][iter_46_5]
					end

					if arg_46_0.tileIndicies[iter_46_4][iter_46_5 - 1] and arg_46_0.tileIndicies[iter_46_4][iter_46_5 - 1] == arg_46_0.tileIndicies[iter_46_4][iter_46_5 - 2] then
						var_46_2 = arg_46_0.tileIndicies[iter_46_4][iter_46_5 - 2]
					end

					local var_46_3 = math.random(1, #arg_46_0.tiles)

					while var_46_3 == var_46_1 or var_46_3 == var_46_2 do
						var_46_3 = math.random(1, #arg_46_0.tiles)
					end

					arg_46_0.tileIndicies[iter_46_4][iter_46_5] = var_46_3
				end
			end
		end
	until arg_46_0:findMove()
end

function var_0_0.reorderTiles(arg_47_0)
	for iter_47_0 = 1, var_0_1 do
		for iter_47_1 = 1, var_0_2 do
			if arg_47_0.tileTfs[iter_47_0][iter_47_1] then
				arg_47_0.tileTfs[iter_47_0][iter_47_1]:SetAsFirstSibling()
			end
		end
	end
end

function var_0_0.fillTiles(arg_48_0, arg_48_1)
	local var_48_0 = 0

	for iter_48_0 = 1, var_0_2 do
		local var_48_1 = 0

		for iter_48_1 = var_0_1, 1, -1 do
			if not arg_48_0.tileTfs[iter_48_1][iter_48_0] then
				var_48_1 = var_48_1 + 1
			end
		end

		var_48_0 = math.max(var_48_1, var_48_0)

		for iter_48_2 = 1, var_0_1 do
			if not arg_48_0.tileTfs[iter_48_2][iter_48_0] then
				local var_48_2 = rtf(cloneTplTo(arg_48_0.tiles[arg_48_0.tileIndicies[iter_48_2][iter_48_0]], arg_48_0.tilesRoot))

				if arg_48_1 then
					var_48_2.anchoredPosition = arg_48_0:index2pos(iter_48_2, iter_48_0)
				else
					var_48_2.anchoredPosition = arg_48_0:index2pos(iter_48_2 + var_48_1, iter_48_0)

					arg_48_0:moveTile(var_48_2, {
						i = iter_48_2,
						j = iter_48_0
					}, arg_48_0.dropTime(var_48_1))
				end

				arg_48_0.tileTfs[iter_48_2][iter_48_0] = var_48_2
			end
		end
	end

	arg_48_0:reorderTiles()

	return var_48_0
end

local var_0_31 = {
	{
		{
			-1,
			-2
		},
		{
			-1,
			-1
		}
	},
	{
		{
			-1,
			-1
		},
		{
			-1,
			1
		}
	},
	{
		{
			-1,
			1
		},
		{
			-1,
			2
		}
	}
}

function var_0_0.findMove(arg_49_0)
	for iter_49_0 = 1, var_0_1 do
		for iter_49_1 = 1, var_0_2 do
			local var_49_0 = arg_49_0.tileIndicies[iter_49_0][iter_49_1]
			local var_49_1
			local var_49_2

			for iter_49_2, iter_49_3 in pairs(var_0_31) do
				local var_49_3 = arg_49_0.tileIndicies[iter_49_0 + iter_49_3[1][1]][iter_49_1 + iter_49_3[1][2]]
				local var_49_4 = arg_49_0.tileIndicies[iter_49_0 + iter_49_3[2][1]][iter_49_1 + iter_49_3[2][2]]

				if var_49_0 == var_49_3 and var_49_0 == var_49_4 then
					return iter_49_0, iter_49_1, {
						-1,
						0
					}
				end

				local var_49_5 = arg_49_0.tileIndicies[iter_49_0 - iter_49_3[1][1]][iter_49_1 - iter_49_3[1][2]]
				local var_49_6 = arg_49_0.tileIndicies[iter_49_0 - iter_49_3[2][1]][iter_49_1 - iter_49_3[2][2]]

				if var_49_0 == var_49_5 and var_49_0 == var_49_6 then
					return iter_49_0, iter_49_1, {
						1,
						0
					}
				end

				local var_49_7 = arg_49_0.tileIndicies[iter_49_0 - iter_49_3[1][2]][iter_49_1 + iter_49_3[1][1]]
				local var_49_8 = arg_49_0.tileIndicies[iter_49_0 - iter_49_3[2][2]][iter_49_1 + iter_49_3[2][1]]

				if var_49_0 == var_49_7 and var_49_0 == var_49_8 then
					return iter_49_0, iter_49_1, {
						0,
						-1
					}
				end

				local var_49_9 = arg_49_0.tileIndicies[iter_49_0 + iter_49_3[1][2]][iter_49_1 - iter_49_3[1][1]]
				local var_49_10 = arg_49_0.tileIndicies[iter_49_0 + iter_49_3[2][2]][iter_49_1 - iter_49_3[2][1]]

				if var_49_0 == var_49_9 and var_49_0 == var_49_10 then
					return iter_49_0, iter_49_1, {
						0,
						1
					}
				end
			end
		end
	end
end

function var_0_0.stopGame(arg_50_0)
	arg_50_0.inGame = false

	setActive(arg_50_0.warning, false)
	arg_50_0.hintTimer:Reset(arg_50_0.hintFunc, 5)
	arg_50_0.hintTimer:Stop()
	arg_50_0:cleanManagedTween(true)
	arg_50_0:cancelHint()

	if arg_50_0.timer then
		arg_50_0.timer:Pause()
	end

	if arg_50_0.handle then
		UpdateBeat:RemoveListener(arg_50_0.handle)
	end

	for iter_50_0 = 1, var_0_1 do
		for iter_50_1 = 1, var_0_2 do
			if arg_50_0.tileTfs[iter_50_0][iter_50_1] then
				Destroy(arg_50_0.tileTfs[iter_50_0][iter_50_1])
			end
		end
	end

	if arg_50_0.selectedEffectTf then
		Destroy(arg_50_0.selectedEffectTf)

		arg_50_0.selectedEffectTf = nil
	end

	setText(arg_50_0.bestScore, math.max(arg_50_0.best, arg_50_0.score))
	setActive(arg_50_0.gamePage, false)
	setActive(arg_50_0.pausePage, false)
	setActive(arg_50_0.endBtn, false)
	setActive(arg_50_0.endPage, true)

	if arg_50_0.score > 0 then
		pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_0_27)
	end

	setActive(arg_50_0.newSign, false)
	setText(arg_50_0.endScore, 0)
	arg_50_0:managedTween(LeanTween.value, function()
		setActive(arg_50_0.newSign, arg_50_0.best < arg_50_0.score)
		setActive(arg_50_0.endBtn, true)
		setImageAlpha(arg_50_0.endBtn, 0)

		arg_50_0.endBtn:GetComponent("Button").enabled = false

		pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_0_28)
		arg_50_0:managedTween(LeanTween.value, function()
			arg_50_0.endBtn:GetComponent("Button").enabled = true
			arg_50_0.timer = nil

			arg_50_0:SendSuccess(arg_50_0.score)
		end, go(arg_50_0.endBtn), 0, 1, var_0_19):setOnUpdate(System.Action_float(function(arg_53_0)
			setImageAlpha(arg_50_0.endBtn, arg_53_0)
		end))
	end, go(arg_50_0.endScore), 0, arg_50_0.score, arg_50_0.score > 0 and var_0_18 or 0):setOnUpdate(System.Action_float(function(arg_54_0)
		setText(arg_50_0.endScore, math.floor(arg_54_0))
	end))
end

function var_0_0.formatScore(arg_55_0, arg_55_1, arg_55_2)
	local var_55_0 = {}

	while arg_55_2 > 0 do
		table.insert(var_55_0, math.fmod(arg_55_2, 10))

		arg_55_2 = math.floor(arg_55_2 / 10)
	end

	for iter_55_0 = #var_55_0, 1, -1 do
		cloneTplTo(arg_55_0.floatChar[var_55_0[iter_55_0]], arg_55_1)
	end
end

function var_0_0.update(arg_56_0)
	arg_56_0.hintTimer:Stop()

	local var_56_0 = true

	arg_56_0.updating = true

	local var_56_1 = arg_56_0:tryMatch()

	if next(var_56_1) ~= nil then
		arg_56_0:cancelHint()

		var_56_0 = false
		arg_56_0.combo = arg_56_0.combo + 1

		pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_0_24)

		local var_56_2

		for iter_56_0, iter_56_1 in pairs(var_56_1) do
			if #iter_56_1 == 3 then
				var_56_2 = 30 * arg_56_0.combo
			elseif #iter_56_1 == 4 then
				var_56_2 = 60 * arg_56_0.combo
			else
				var_56_2 = 20 * #iter_56_1 * arg_56_0.combo
			end

			arg_56_0.score = arg_56_0.score + var_56_2

			setText(arg_56_0.scoreText, arg_56_0.score)

			local var_56_3 = Vector2.zero

			_.each(iter_56_1, function(arg_57_0)
				arg_56_0.tileIndicies[arg_57_0[1]][arg_57_0[2]] = nil

				if arg_56_0.tileTfs[arg_57_0[1]][arg_57_0[2]] then
					local var_57_0 = arg_56_0.tileTfs[arg_57_0[1]][arg_57_0[2]]

					var_56_3 = var_56_3 + var_57_0.anchoredPosition
					var_57_0:GetComponent("Image").material = arg_56_0.whitenMat

					local var_57_1 = var_57_0.localPosition

					var_57_1.z = -50

					local var_57_2 = cloneTplTo(arg_56_0.matchEffect, arg_56_0.tilesRoot)

					var_57_2.localPosition = var_57_1

					arg_56_0:managedTween(LeanTween.value, function()
						Destroy(var_57_0)
						Destroy(var_57_2)
					end, go(var_57_0), 1, 0, var_0_10):setOnUpdate(System.Action_float(function(arg_59_0)
						setImageAlpha(var_57_0, arg_59_0)
						setLocalScale(var_57_0, Vector3.one * arg_59_0 * 2.7)
					end))
				end

				arg_56_0.tileTfs[arg_57_0[1]][arg_57_0[2]] = nil
			end)

			var_56_3 = var_56_3 / #iter_56_1

			local var_56_4 = rtf(cloneTplTo(arg_56_0.floatText, arg_56_0.tilesRoot))

			var_56_4.anchoredPosition = var_56_3

			arg_56_0:formatScore(var_56_4, var_56_2)
			arg_56_0:managedTween(LeanTween.moveY, function()
				Destroy(var_56_4)
			end, var_56_4, var_56_3.y + var_0_12, var_0_11)
		end

		arg_56_0:managedTween(LeanTween.delayedCall, function()
			if not arg_56_0.inGame then
				return
			end

			local var_61_0 = 0

			for iter_61_0 = 1, var_0_1 do
				for iter_61_1 = 1, var_0_2 do
					if arg_56_0.tileIndicies[iter_61_0][iter_61_1] then
						local var_61_1 = iter_61_0

						for iter_61_2 = iter_61_0, 1, -1 do
							if arg_56_0.tileIndicies[iter_61_2 - 1][iter_61_1] or iter_61_2 == 1 then
								var_61_1 = iter_61_2

								break
							end
						end

						if var_61_1 ~= iter_61_0 then
							local var_61_2 = iter_61_0 - var_61_1

							var_61_0 = math.max(var_61_2, var_61_0)

							arg_56_0:moveTile(arg_56_0.tileTfs[iter_61_0][iter_61_1], {
								i = var_61_1,
								j = iter_61_1
							}, arg_56_0.dropTime(var_61_2))

							arg_56_0.tileTfs[var_61_1][iter_61_1] = arg_56_0.tileTfs[iter_61_0][iter_61_1]
							arg_56_0.tileIndicies[var_61_1][iter_61_1] = arg_56_0.tileIndicies[iter_61_0][iter_61_1]
							arg_56_0.tileTfs[iter_61_0][iter_61_1] = nil
							arg_56_0.tileIndicies[iter_61_0][iter_61_1] = nil
						end
					end
				end
			end

			arg_56_0:fillTileIndicies()

			local var_61_3 = arg_56_0:tryMatch()

			if arg_56_0.combo > 1 and next(var_61_3) == nil then
				local var_61_4
				local var_61_5 = Vector3.New(0, 0, -50)

				if arg_56_0.combo == 2 then
					var_61_4 = cloneTplTo(arg_56_0.goodEffect, arg_56_0.tilesRoot)

					pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_0_25)
				elseif arg_56_0.combo == 3 then
					var_61_4 = cloneTplTo(arg_56_0.greatEffect, arg_56_0.tilesRoot)

					pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_0_25)
				else
					var_61_4 = cloneTplTo(arg_56_0.perfectEffect, arg_56_0.tilesRoot)

					pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_0_26)
				end

				var_61_4.localPosition = var_61_5

				arg_56_0:managedTween(LeanTween.delayedCall, function()
					Destroy(var_61_4)
				end, var_0_14, nil)
			end

			local var_61_6 = math.max(arg_56_0:fillTiles(), var_61_0)

			arg_56_0:managedTween(LeanTween.delayedCall, function()
				if not arg_56_0.inGame then
					return
				end

				arg_56_0:update()
			end, math.max(var_0_14, arg_56_0.dropTime(var_61_6)), nil)
		end, var_0_10, nil)
	end

	if arg_56_0.inGame then
		arg_56_0.hintTimer:Reset(arg_56_0.hintFunc, var_0_21)
		arg_56_0.hintTimer:Start()
	end

	arg_56_0.updating = not var_56_0
end

function var_0_0.tryMatch(arg_64_0)
	local var_64_0 = {}

	for iter_64_0 = 1, var_0_1 do
		var_64_0[iter_64_0] = {}
	end

	return arg_64_0:bfs(var_64_0)
end

function var_0_0.bfs(arg_65_0, arg_65_1)
	local var_65_0 = {}

	for iter_65_0 = 1, var_0_1 do
		for iter_65_1 = 1, var_0_2 do
			if not arg_65_1[iter_65_0][iter_65_1] then
				if not arg_65_0:isConnected({
					i = iter_65_0,
					j = iter_65_1
				}) then
					arg_65_1[iter_65_0][iter_65_1] = true
				else
					local var_65_1 = {
						{
							iter_65_0,
							iter_65_1
						}
					}
					local var_65_2 = {
						{
							iter_65_0,
							iter_65_1
						}
					}
					local var_65_3 = arg_65_0.tileIndicies[iter_65_0][iter_65_1]

					while next(var_65_1) ~= nil do
						local var_65_4, var_65_5 = unpack(table.remove(var_65_1))

						arg_65_1[var_65_4][var_65_5] = true

						for iter_65_2, iter_65_3 in pairs(var_0_29) do
							local var_65_6 = var_65_4 + iter_65_3[1]
							local var_65_7 = var_65_5 + iter_65_3[2]

							if arg_65_0.tileIndicies[var_65_6][var_65_7] and not arg_65_1[var_65_6][var_65_7] and arg_65_0.tileIndicies[var_65_6][var_65_7] == var_65_3 and arg_65_0:isConnected({
								i = var_65_6,
								j = var_65_7
							}) then
								table.insert(var_65_1, {
									var_65_6,
									var_65_7
								})
								table.insert(var_65_2, {
									var_65_6,
									var_65_7
								})
							end
						end
					end

					if #var_65_2 >= 3 then
						table.insert(var_65_0, var_65_2)
					end
				end
			end
		end
	end

	return var_65_0
end

return var_0_0
