﻿local var_0_0 = class("WorldInPictureScene", import("...base.BaseUI"))
local var_0_1 = 0
local var_0_2 = 1

function var_0_0.getUIName(arg_1_0)
	return "WorldInPictureUI"
end

function var_0_0.emit(arg_2_0, ...)
	if arg_2_0.inAniming then
		return
	end

	var_0_0.super.emit(arg_2_0, ...)
end

function var_0_0.OnOpenCellErro(arg_3_0, arg_3_1)
	if arg_3_1 then
		arg_3_0.onkeyTravelProcess = false

		arg_3_0:UpdateTravelBtnState()
	end
end

function var_0_0.OnOpenCell(arg_4_0, arg_4_1, arg_4_2, arg_4_3)
	arg_4_0:CloseSelector(arg_4_1, arg_4_2)
	arg_4_0:HideBox(arg_4_1, arg_4_2)

	arg_4_0.inAniming = true

	local var_4_0 = arg_4_0.cells[arg_4_1][arg_4_2]
	local var_4_1 = var_4_0.gameObject.transform.anchoredPosition

	arg_4_0:DoAnimtion("picture_faguang", var_4_1, function()
		var_4_0.alpha = 1

		if arg_4_3 and arg_4_0.data:ExistBox(arg_4_1, arg_4_2) then
			arg_4_0:RpAnim(arg_4_1, arg_4_2)
		end

		arg_4_0:HightLightOpenArea(arg_4_1, arg_4_2)
		arg_4_0:UpdatePoints()
		arg_4_0:UpdateSwitcherState()

		local var_5_0 = arg_4_0.data:IsFirstTravel()

		arg_4_0:UpdateChar(Vector2(arg_4_1, arg_4_2), not var_5_0)
		arg_4_0:SaveCharPosition(arg_4_1, arg_4_2)

		arg_4_0.inAniming = false
		arg_4_0.forceStopTravelPorcess = false

		if arg_4_3 then
			local var_5_1 = arg_4_0.onkeyTravelProcess

			arg_4_0.onkeyTravelProcess = false

			arg_4_0:UpdateTravelBtnState()

			if not var_5_1 or not arg_4_0.data:FindNextTravelable() then
				arg_4_0:emit(WorldInPictureMediator.RESULT_ONEKEY_AWARD)
			elseif var_5_1 == true then
				triggerButton(arg_4_0.onekeyTravelBtn)
			end
		end
	end)
end

function var_0_0.CloseSelector(arg_6_0, arg_6_1, arg_6_2)
	if arg_6_0.data:IsFirstTravel() then
		for iter_6_0, iter_6_1 in ipairs(arg_6_0.selectors) do
			for iter_6_2, iter_6_3 in ipairs(iter_6_1) do
				iter_6_3.alpha = 0
			end
		end
	else
		local var_6_0 = arg_6_0.selectors[arg_6_1][arg_6_2]

		if var_6_0 and var_6_0.alpha ~= 0 then
			var_6_0.alpha = 0
		end
	end
end

function var_0_0.HightLightOpenArea(arg_7_0, arg_7_1, arg_7_2)
	local var_7_0 = {
		Vector2(arg_7_1 + 1, arg_7_2),
		Vector2(arg_7_1, arg_7_2 + 1),
		Vector2(arg_7_1 - 1, arg_7_2),
		Vector2(arg_7_1, arg_7_2 - 1)
	}

	local function var_7_1(arg_8_0)
		if arg_7_0.data:IsOpened(arg_8_0.x, arg_8_0.y) or arg_7_0.data:OutSide(arg_8_0.x, arg_8_0.y) then
			return
		end

		if not arg_7_0.selectors[arg_8_0.x] or not arg_7_0.selectors[arg_8_0.x][arg_8_0.y] then
			arg_7_0:CreateSelector(arg_8_0.x, arg_8_0.y)
		else
			arg_7_0.selectors[arg_8_0.x][arg_8_0.y].alpha = 1
		end
	end

	_.each(var_7_0, var_7_1)
end

function var_0_0.RpAnim(arg_9_0, arg_9_1, arg_9_2)
	local var_9_0 = arg_9_0:GetRedPacket()

	var_9_0.anchoredPosition = arg_9_0.cells[arg_9_1][arg_9_2].gameObject.transform.anchoredPosition + Vector2(48, 48)

	LeanTween.value(var_9_0.gameObject, var_9_0.anchoredPosition.y, var_9_0.anchoredPosition.y + 35, 0.75):setOnUpdate(System.Action_float(function(arg_10_0)
		var_9_0.anchoredPosition = Vector2(var_9_0.anchoredPosition.x, arg_10_0)
	end)):setOnComplete(System.Action(function()
		if arg_9_0.exited then
			return
		end

		setActive(var_9_0, false)
		table.insert(arg_9_0.redpackets, var_9_0)
	end))
end

function var_0_0.HideBox(arg_12_0, arg_12_1, arg_12_2)
	local var_12_0

	if arg_12_0.boxes[arg_12_1] then
		var_12_0 = arg_12_0.boxes[arg_12_1][arg_12_2]
	end

	if var_12_0 then
		var_12_0.alpha = 0
	end
end

function var_0_0.OnDrawAreaErro(arg_13_0, arg_13_1)
	if arg_13_1 then
		arg_13_0.onkeyDrawPorcess = false

		arg_13_0:UpdateDrawBtnState()
	end
end

function var_0_0.OnDrawArea(arg_14_0, arg_14_1, arg_14_2, arg_14_3)
	arg_14_0:HideDrawarea(arg_14_1, arg_14_2)

	arg_14_0.inAniming = true

	arg_14_0:CreateAnimal(arg_14_1, arg_14_2, false, function(arg_15_0)
		local var_15_0 = arg_14_0.data:GetDrawAnimData(arg_14_1, arg_14_2)
		local var_15_1 = arg_15_0.sizeDelta.x * arg_15_0.localScale.x * 0.5 + 90
		local var_15_2 = arg_15_0.sizeDelta.y * arg_15_0.localScale.y * 0.5
		local var_15_3 = Vector2(var_15_0[2] + var_15_1, var_15_0[3] - var_15_2)

		arg_14_0:DoAnimtion("picture_bichu", var_15_3, function()
			LeanTween.value(arg_15_0.gameObject, 0, 1, 0.5):setOnUpdate(System.Action_float(function(arg_17_0)
				if arg_14_0.exited then
					return
				end

				arg_15_0:GetComponent(typeof(CanvasGroup)).alpha = arg_17_0
			end))
			arg_14_0:UpdatePoints()

			arg_14_0.inAniming = false
			arg_14_0.forceStopDrawPorcess = false

			if arg_14_3 then
				local var_16_0 = arg_14_0.onkeyDrawPorcess

				arg_14_0.onkeyDrawPorcess = false

				arg_14_0:UpdateDrawBtnState()

				if not var_16_0 or not arg_14_0.data:FindNextDrawableAreaHead() then
					arg_14_0:emit(WorldInPictureMediator.RESULT_ONEKEY_AWARD)
				elseif arg_14_3 and var_16_0 == true then
					triggerButton(arg_14_0.onekeyDrawBtn)
				end
			end
		end)
	end)
end

function var_0_0.HideDrawarea(arg_18_0, arg_18_1, arg_18_2)
	local var_18_0

	if arg_18_0.drawableAare[arg_18_1] then
		var_18_0 = arg_18_0.drawableAare[arg_18_1][arg_18_2]
	end

	if var_18_0 then
		var_18_0.alpha = 0
	end
end

function var_0_0.SetData(arg_19_0, arg_19_1)
	arg_19_0.data = arg_19_1
end

function var_0_0.init(arg_20_0)
	Input.multiTouchEnabled = false
	arg_20_0.redpacket = arg_20_0:findTF("redpackets/redpacket")
	arg_20_0.lineHrzTpl = arg_20_0:findTF("lines/line_hrz")
	arg_20_0.lineVecTpl = arg_20_0:findTF("lines/line_vec")
	arg_20_0.animalTpl = arg_20_0:findTF("animals/animal")
	arg_20_0.areaTpl = arg_20_0:findTF("drawablearea/area")
	arg_20_0.boxTpl = arg_20_0:findTF("boxes/box")
	arg_20_0.selectorTpl = arg_20_0:findTF("selectors/selector")
	arg_20_0.tpl = arg_20_0:findTF("grids/grid")
	arg_20_0.backBtn = arg_20_0:findTF("back")
	arg_20_0.helpBtn = arg_20_0:findTF("help")
	arg_20_0.travelPointTxt = arg_20_0:findTF("points/travel"):GetComponent(typeof(Text))
	arg_20_0.drawPointTxt = arg_20_0:findTF("points/draw"):GetComponent(typeof(Text))
	arg_20_0.travelProgressTxt = arg_20_0:findTF("progress/travel"):GetComponent(typeof(Text))
	arg_20_0.drawProgressTxt = arg_20_0:findTF("progress/draw"):GetComponent(typeof(Text))
	arg_20_0.switchBtn = arg_20_0:findTF("swticher")
	arg_20_0.onDisable = arg_20_0.switchBtn:Find("on_disable")
	arg_20_0.btnOn = arg_20_0.switchBtn:Find("on_enable/draw")
	arg_20_0.btnOff = arg_20_0.switchBtn:Find("on_enable/off")
	arg_20_0.onekeyTravelBtn = arg_20_0:findTF("onekey_travel")
	arg_20_0.onekeyTravelingBtn = arg_20_0:findTF("onekey_travel/Image")
	arg_20_0.onekeyDrawBtn = arg_20_0:findTF("onekey_draw")
	arg_20_0.onekeyDrawingBtn = arg_20_0:findTF("onekey_draw/Image")
	arg_20_0.char = arg_20_0:findTF("char/char")

	setActive(arg_20_0.char, false)

	arg_20_0.selectorContainer = arg_20_0:findTF("selectors"):GetComponent(typeof(CanvasGroup))
	arg_20_0.drawableAreaContainer = arg_20_0:findTF("drawablearea"):GetComponent(typeof(CanvasGroup))
	arg_20_0.startPos = arg_20_0.tpl.anchoredPosition
	arg_20_0.offset = Vector2(0.5, 0.5)
	arg_20_0.width = arg_20_0.tpl.sizeDelta.x
	arg_20_0.height = arg_20_0.tpl.sizeDelta.y
	arg_20_0.cells = {}
	arg_20_0.selectors = {}
	arg_20_0.boxes = {}
	arg_20_0.drawableAare = {}
	arg_20_0.animals = {}
	arg_20_0.redpackets = {
		arg_20_0.redpacket
	}
end

function var_0_0.didEnter(arg_21_0)
	onButton(arg_21_0, arg_21_0.backBtn, function()
		if arg_21_0.opType == var_0_1 and arg_21_0.onkeyTravelProcess then
			arg_21_0.onkeyTravelProcess = false

			arg_21_0:UpdateTravelBtnState()

			return
		elseif arg_21_0.opType == var_0_2 and arg_21_0.onkeyDrawPorcess then
			arg_21_0.onkeyDrawPorcess = false

			arg_21_0:UpdateDrawBtnState()

			return
		end

		arg_21_0:emit(var_0_0.ON_BACK)
	end, SFX_CANCEL)
	onButton(arg_21_0, arg_21_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.worldinpicture_help.tip
		})
	end, SFX_PANEL)
	onButton(arg_21_0, arg_21_0.onekeyTravelBtn, function()
		if arg_21_0.forceStopTravelPorcess then
			return
		end

		if arg_21_0.data:IsTravelAll() then
			return
		end

		if arg_21_0.data:GetTravelPoint() <= 0 then
			pg.TipsMgr.GetInstance():ShowTips(i18n("worldinpicture_tavel_point_tip"))

			return
		end

		if arg_21_0.onkeyTravelProcess then
			arg_21_0.onkeyTravelProcess = false
			arg_21_0.forceStopTravelPorcess = true

			arg_21_0:UpdateTravelBtnState()

			return
		end

		local var_24_0, var_24_1 = arg_21_0.data:FindNextTravelable()

		if var_24_0 and var_24_1 then
			arg_21_0.onkeyTravelProcess = true

			arg_21_0:UpdateTravelBtnState()
			arg_21_0:emit(WorldInPictureMediator.ON_AUTO_TRAVEL, var_24_0.x, var_24_0.y, var_24_1)
		end
	end, SFX_PANEL)
	onButton(arg_21_0, arg_21_0.onekeyDrawBtn, function()
		if arg_21_0.forceStopDrawPorcess then
			return
		end

		if arg_21_0.data:IsDrawAll() then
			return
		end

		if arg_21_0.data:GetDrawPoint() <= 0 then
			pg.TipsMgr.GetInstance():ShowTips(i18n("worldinpicture_draw_point_tip"))

			return
		end

		if arg_21_0.onkeyDrawPorcess then
			arg_21_0.onkeyDrawPorcess = false
			arg_21_0.forceStopDrawPorcess = true

			arg_21_0:UpdateDrawBtnState()

			return
		end

		local var_25_0, var_25_1 = arg_21_0.data:FindNextDrawableAreaHead()

		if var_25_0 and var_25_1 then
			arg_21_0.onkeyDrawPorcess = true

			arg_21_0:UpdateDrawBtnState()
			arg_21_0:emit(WorldInPictureMediator.ON_AUTO_DRAW, var_25_0.x, var_25_0.y, var_25_1)
		end
	end, SFX_PANEL)

	arg_21_0.opType = var_0_1

	onButton(arg_21_0, arg_21_0.onDisable, function()
		pg.TipsMgr.GetInstance():ShowTips(i18n("worldinpicture_not_area_can_draw"))
	end, SFX_PANEL)
	onButton(arg_21_0, arg_21_0.btnOn, function()
		if arg_21_0.opType == var_0_1 and arg_21_0.onkeyTravelProcess then
			arg_21_0.onkeyTravelProcess = false

			arg_21_0:UpdateTravelBtnState()

			return
		elseif arg_21_0.opType == var_0_2 and arg_21_0.onkeyDrawPorcess then
			arg_21_0.onkeyDrawPorcess = false

			arg_21_0:UpdateDrawBtnState()

			return
		end

		if arg_21_0.inAniming then
			return
		end

		arg_21_0.opType = var_0_2

		arg_21_0:UpdateSwitcherState()
	end, SFX_PANEL)
	onButton(arg_21_0, arg_21_0.btnOff, function()
		if arg_21_0.opType == var_0_1 and arg_21_0.onkeyTravelProcess then
			arg_21_0.onkeyTravelProcess = false

			arg_21_0:UpdateTravelBtnState()

			return
		elseif arg_21_0.opType == var_0_2 and arg_21_0.onkeyDrawPorcess then
			arg_21_0.onkeyDrawPorcess = false

			arg_21_0:UpdateDrawBtnState()

			return
		end

		if arg_21_0.inAniming then
			return
		end

		arg_21_0.opType = var_0_1

		arg_21_0:UpdateSwitcherState()
	end, SFX_PANEL)
	arg_21_0:UpdateSwitcherState()
	arg_21_0:InitView()
end

function var_0_0.UpdateDrawBtnState(arg_29_0)
	setActive(arg_29_0.onekeyDrawingBtn, arg_29_0.onkeyDrawPorcess)
end

function var_0_0.UpdateTravelBtnState(arg_30_0)
	setActive(arg_30_0.onekeyTravelingBtn, arg_30_0.onkeyTravelProcess)
end

function var_0_0.GetRecordCharPos(arg_31_0)
	local var_31_0 = getProxy(PlayerProxy):getRawData().id
	local var_31_1 = PlayerPrefs.GetString("WorldInPictureScene_1" .. var_31_0, "0#0")
	local var_31_2 = string.split(var_31_1, "#")

	return Vector2(tonumber(var_31_2[1]), tonumber(var_31_2[2]))
end

function var_0_0.SaveCharPosition(arg_32_0, arg_32_1, arg_32_2)
	local var_32_0 = getProxy(PlayerProxy):getRawData().id

	PlayerPrefs.SetString("WorldInPictureScene_1" .. var_32_0, arg_32_1 .. "#" .. arg_32_2)
	PlayerPrefs.Save()
end

function var_0_0.moveChar(arg_33_0, arg_33_1, arg_33_2, arg_33_3)
	if LeanTween.isTweening(go(arg_33_0.char)) then
		LeanTween.cancel(go(arg_33_0.char))
	end

	if isActive(arg_33_0.char) then
		arg_33_0:hideChar(function()
			arg_33_0:showChar(arg_33_1, arg_33_2, arg_33_3)
		end)
	else
		arg_33_0:showChar(arg_33_1, arg_33_2, arg_33_3)
	end
end

function var_0_0.showChar(arg_35_0, arg_35_1, arg_35_2, arg_35_3)
	arg_35_0.char.transform.localPosition = Vector3(arg_35_1, arg_35_2 + 50)

	setActive(arg_35_0.char, true)
	LeanTween.value(go(arg_35_0.char), 0, 1, 0.2):setOnUpdate(System.Action_float(function(arg_36_0)
		GetOrAddComponent(arg_35_0.char, typeof(CanvasGroup)).alpha = arg_36_0
	end))
	LeanTween.moveLocal(go(arg_35_0.char), Vector3(arg_35_1, arg_35_2, 0), 0.2):setOnComplete(System.Action(function()
		if arg_35_3 then
			arg_35_3()
		end
	end))
end

function var_0_0.hideChar(arg_38_0, arg_38_1)
	LeanTween.value(go(arg_38_0.char), 1, 0, 0.2):setOnUpdate(System.Action_float(function(arg_39_0)
		GetOrAddComponent(arg_38_0.char, typeof(CanvasGroup)).alpha = arg_39_0
	end))

	local var_38_0 = arg_38_0.char.transform.localPosition

	LeanTween.moveLocal(go(arg_38_0.char), Vector3(var_38_0.x, var_38_0.y + 50, 0), 0.2):setOnComplete(System.Action(function()
		setActive(arg_38_0.char, false)

		if arg_38_1 then
			arg_38_1()
		end
	end))
end

function var_0_0.UpdateChar(arg_41_0, arg_41_1, arg_41_2)
	if arg_41_1 == Vector2.zero then
		setActive(arg_41_0.char, false)

		return
	end

	if LeanTween.isTweening(arg_41_0.char) then
		LeanTween.cancel(arg_41_0.char)
	end

	if arg_41_0.data:IsTravelAll() then
		setActive(arg_41_0.char, false)

		return
	end

	local var_41_0 = arg_41_0.cells[arg_41_1.x][arg_41_1.y].gameObject.transform.anchoredPosition
	local var_41_1 = Vector2(var_41_0.x, var_41_0.y - 50)

	if arg_41_2 then
		arg_41_0:moveChar(var_41_1.x, var_41_1.y, function()
			return
		end)
	else
		arg_41_0.char.transform.localPosition = var_41_1
	end
end

function var_0_0.UpdateSwitcherState(arg_43_0)
	local var_43_0 = arg_43_0.opType == var_0_2
	local var_43_1 = arg_43_0.data:AnyAreaCanDraw()

	setActive(arg_43_0.btnOff, var_43_0)
	setActive(arg_43_0.onDisable, not var_43_0 and not var_43_1)
	setActive(arg_43_0.btnOn, not var_43_0 and var_43_1)
	setActive(arg_43_0.onekeyTravelBtn, not var_43_0)
	setActive(arg_43_0.onekeyDrawBtn, var_43_0)
	setActive(arg_43_0.char, not var_43_0 and not arg_43_0.data:IsTravelAll())

	arg_43_0.selectorContainer.alpha = var_43_0 and 0 or 1
	arg_43_0.drawableAreaContainer.alpha = var_43_0 and 1 or 0

	if var_43_0 then
		arg_43_0:UpdateDrawableAreas()
	end
end

function var_0_0.InitView(arg_44_0)
	local var_44_0, var_44_1 = arg_44_0.data:GetMapRowAndColumn()
	local var_44_2 = {}

	for iter_44_0 = 1, var_44_0 do
		table.insert(var_44_2, function(arg_45_0)
			for iter_45_0 = var_44_1, 1, -1 do
				arg_44_0:CreateCell(iter_44_0, iter_45_0, (iter_44_0 - 1) * var_44_1 + iter_45_0)
			end

			onNextTick(arg_45_0)
		end)
	end

	seriesAsync(var_44_2, function()
		arg_44_0:InitLines()
		arg_44_0:UpdateChar(arg_44_0:GetRecordCharPos())
	end)
	arg_44_0:UpdatePoints()
end

function var_0_0.InitLines(arg_47_0)
	local var_47_0, var_47_1 = arg_47_0.data:GetMapRowAndColumn()
	local var_47_2 = arg_47_0.tpl.sizeDelta.y * var_47_0 + 10

	for iter_47_0 = 1, var_47_1 - 1 do
		local var_47_3 = iter_47_0 == 1 and arg_47_0.lineVecTpl or Object.Instantiate(arg_47_0.lineVecTpl, arg_47_0.lineVecTpl.parent)

		var_47_3.sizeDelta = Vector2(var_47_3.sizeDelta.x, var_47_2)

		local var_47_4 = arg_47_0.cells[1][iter_47_0]
		local var_47_5 = var_47_4.gameObject.transform.anchoredPosition.x + var_47_4.gameObject.transform.sizeDelta.x * 0.5

		var_47_3.anchoredPosition = Vector2(var_47_5 + arg_47_0.offset.x, var_47_3.anchoredPosition.y)
	end

	local var_47_6 = arg_47_0.tpl.sizeDelta.x * var_47_1 + 20

	for iter_47_1 = 1, var_47_0 - 1 do
		local var_47_7 = iter_47_1 == 1 and arg_47_0.lineHrzTpl or Object.Instantiate(arg_47_0.lineHrzTpl, arg_47_0.lineHrzTpl.parent)

		var_47_7.sizeDelta = Vector2(var_47_7.sizeDelta.x, var_47_6)

		local var_47_8 = arg_47_0.cells[iter_47_1][1]
		local var_47_9 = var_47_8.gameObject.transform.anchoredPosition.y - var_47_8.gameObject.transform.sizeDelta.y * 0.5

		var_47_7.anchoredPosition = Vector2(var_47_7.anchoredPosition.x, var_47_9 + arg_47_0.offset.y)
	end
end

function var_0_0.CreateCell(arg_48_0, arg_48_1, arg_48_2, arg_48_3)
	if arg_48_0.exited then
		return
	end

	local var_48_0 = arg_48_2 == 1 and arg_48_1 == 1 and arg_48_0.tpl or Object.Instantiate(arg_48_0.tpl, arg_48_0.tpl.parent).transform
	local var_48_1 = arg_48_0.startPos.x + (arg_48_2 - 1) * (arg_48_0.width + arg_48_0.offset.x)
	local var_48_2 = arg_48_0.startPos.y - (arg_48_1 - 1) * (arg_48_0.height + arg_48_0.offset.y)

	LoadSpriteAtlasAsync("ui/WorldInPicture_atlas", "view_" .. arg_48_3 - 1, function(arg_49_0)
		if arg_48_0.exited then
			return
		end

		local var_49_0 = var_48_0:GetComponent(typeof(Image))

		var_49_0.sprite = arg_49_0

		var_49_0:SetNativeSize()

		var_48_0.anchoredPosition = Vector2(var_48_1, var_48_2)

		arg_48_0:CreateSelector(arg_48_1, arg_48_2)
		arg_48_0:CreateBox(arg_48_1, arg_48_2)
		arg_48_0:CreateDrawableArea(arg_48_1, arg_48_2)
		arg_48_0:CreateAnimal(arg_48_1, arg_48_2, true)
	end)

	if not arg_48_0.cells[arg_48_1] then
		arg_48_0.cells[arg_48_1] = {}
	end

	onButton(arg_48_0, var_48_0, function()
		if arg_48_0.opType == var_0_1 then
			if arg_48_0.onkeyTravelProcess then
				arg_48_0.onkeyTravelProcess = false

				arg_48_0:UpdateTravelBtnState()

				return
			end

			if arg_48_0.data:IsTravelAll() then
				return
			end

			if arg_48_0.data:GetTravelPoint() <= 0 then
				pg.TipsMgr.GetInstance():ShowTips(i18n("worldinpicture_tavel_point_tip"))

				return
			end

			if arg_48_0.data:CanSelect(arg_48_1, arg_48_2) then
				arg_48_0:emit(WorldInPictureMediator.ON_TRAVEL, arg_48_1, arg_48_2, arg_48_3)
			end
		elseif arg_48_0.opType == var_0_2 then
			if arg_48_0.onkeyDrawPorcess then
				arg_48_0.onkeyDrawPorcess = false

				arg_48_0:UpdateDrawBtnState()

				return
			end

			if arg_48_0.data:IsDrawAll() then
				return
			end

			if arg_48_0.data:GetDrawPoint() <= 0 then
				pg.TipsMgr.GetInstance():ShowTips(i18n("worldinpicture_draw_point_tip"))

				return
			end

			if arg_48_0.data:CanDraw(arg_48_1, arg_48_2) then
				local var_50_0, var_50_1, var_50_2 = arg_48_0.data:Convert2DrawAreaHead(arg_48_1, arg_48_2)

				arg_48_0:emit(WorldInPictureMediator.ON_DRAW, var_50_0, var_50_1, var_50_2)
			end
		end
	end, SFX_PANEL)

	local var_48_3 = var_48_0:GetComponent(typeof(CanvasGroup))

	var_48_3.alpha = arg_48_0.data:IsOpened(arg_48_1, arg_48_2) and 1 or 0
	arg_48_0.cells[arg_48_1][arg_48_2] = var_48_3
end

function var_0_0.CreateSelector(arg_51_0, arg_51_1, arg_51_2)
	if not arg_51_0.data:CanSelect(arg_51_1, arg_51_2) then
		return
	end

	local var_51_0 = table.getCount(arg_51_0.selectors) == 0 and arg_51_0.selectorTpl or Object.Instantiate(arg_51_0.selectorTpl, arg_51_0.selectorTpl.parent).transform

	var_51_0.anchoredPosition = arg_51_0.cells[arg_51_1][arg_51_2].gameObject.transform.anchoredPosition + Vector2(-5, -4.8)

	local var_51_1 = var_51_0:GetComponent(typeof(CanvasGroup))

	var_51_1.alpha = 1

	if not arg_51_0.selectors[arg_51_1] then
		arg_51_0.selectors[arg_51_1] = {}
	end

	arg_51_0.selectors[arg_51_1][arg_51_2] = var_51_1
end

function var_0_0.CreateBox(arg_52_0, arg_52_1, arg_52_2)
	if not arg_52_0.data:ExistBox(arg_52_1, arg_52_2) or arg_52_0.data:IsOpened(arg_52_1, arg_52_2) then
		return
	end

	local var_52_0 = table.getCount(arg_52_0.boxes) == 0 and arg_52_0.boxTpl or Object.Instantiate(arg_52_0.boxTpl, arg_52_0.boxTpl.parent).transform
	local var_52_1 = var_52_0:GetComponent(typeof(CanvasGroup))

	var_52_1.alpha = 1
	var_52_0.anchoredPosition = arg_52_0.cells[arg_52_1][arg_52_2].gameObject.transform.anchoredPosition

	if not arg_52_0.boxes[arg_52_1] then
		arg_52_0.boxes[arg_52_1] = {}
	end

	arg_52_0.boxes[arg_52_1][arg_52_2] = var_52_1
end

function var_0_0.CreateDrawableArea(arg_53_0, arg_53_1, arg_53_2)
	local var_53_0 = arg_53_0.data:GetDrawableArea(arg_53_1, arg_53_2)

	if not var_53_0 or arg_53_0.data:IsDrawed(arg_53_1, arg_53_2) then
		return
	end

	local var_53_1 = table.getCount(arg_53_0.drawableAare) == 0 and arg_53_0.areaTpl or Object.Instantiate(arg_53_0.areaTpl, arg_53_0.areaTpl.parent).transform
	local var_53_2 = var_53_0[#var_53_0] - var_53_0[1] + Vector2(1, 1)
	local var_53_3 = arg_53_0.cells[arg_53_1][arg_53_2]
	local var_53_4 = arg_53_0.tpl.sizeDelta * 0.5

	var_53_1.anchoredPosition = var_53_3.gameObject.transform.anchoredPosition - Vector2(var_53_4.x, -var_53_4.y)

	local var_53_5 = var_53_1:GetComponent(typeof(CanvasGroup))

	var_53_5.alpha = 1

	if not arg_53_0.drawableAare[arg_53_1] then
		arg_53_0.drawableAare[arg_53_1] = {}
	end

	arg_53_0.drawableAare[arg_53_1][arg_53_2] = var_53_5
end

function var_0_0.UpdateDrawableAreas(arg_54_0)
	local var_54_0 = arg_54_0.data:GetDrawableAreasState()

	for iter_54_0, iter_54_1 in ipairs(var_54_0) do
		local var_54_1 = iter_54_1.position

		if arg_54_0.drawableAare[var_54_1.x] and arg_54_0.drawableAare[var_54_1.x][var_54_1.y] then
			arg_54_0.drawableAare[var_54_1.x][var_54_1.y].alpha = iter_54_1.open and 1 or 0
		end
	end
end

function var_0_0.CreateAnimal(arg_55_0, arg_55_1, arg_55_2, arg_55_3, arg_55_4)
	if not arg_55_0.data:GetDrawableArea(arg_55_1, arg_55_2) or not arg_55_0.data:IsDrawed(arg_55_1, arg_55_2) then
		return
	end

	local var_55_0 = table.getCount(arg_55_0.animals) == 0 and arg_55_0.animalTpl or Object.Instantiate(arg_55_0.animalTpl, arg_55_0.animalTpl.parent).transform
	local var_55_1 = arg_55_0.data:GetDrawAnimData(arg_55_1, arg_55_2)
	local var_55_2 = Vector2(var_55_1[2], var_55_1[3])

	LoadSpriteAtlasAsync("ui/WorldInPicture_atlas", var_55_1[1], function(arg_56_0)
		if arg_55_0.exited then
			return
		end

		local var_56_0 = var_55_0:GetComponent(typeof(Image))

		var_56_0.sprite = arg_56_0

		var_56_0:SetNativeSize()

		var_55_0.localScale = Vector3(var_55_1[4] or 1, var_55_1[4] or 1, 1)

		if arg_55_4 then
			arg_55_4(var_55_0)
		end
	end)

	var_55_0.localScale = Vector3.zero
	var_55_0.localPosition = var_55_2

	if not arg_55_0.animals[arg_55_1] then
		arg_55_0.animals[arg_55_1] = {}
	end

	local var_55_3 = var_55_0:GetComponent(typeof(CanvasGroup))

	var_55_3.alpha = arg_55_3 and 1 or 0
	arg_55_0.animals[arg_55_1][arg_55_2] = var_55_3
end

local function var_0_3(arg_57_0, arg_57_1)
	return "<color=#DAC6B3>" .. arg_57_0 .. "</color><color=#A38052>/" .. arg_57_1 .. "</color>"
end

function var_0_0.UpdatePoints(arg_58_0)
	arg_58_0.travelPointTxt.text = arg_58_0.data:GetTravelPoint()
	arg_58_0.drawPointTxt.text = arg_58_0.data:GetDrawPoint()
	arg_58_0.travelProgressTxt.text = var_0_3(arg_58_0.data:GetTravelProgress(), arg_58_0.data:GetMaxTravelCnt())
	arg_58_0.drawProgressTxt.text = var_0_3(arg_58_0.data:GetDrawProgress(), arg_58_0.data:GetMaxDrawCnt())
end

function var_0_0.DoAnimtion(arg_59_0, arg_59_1, arg_59_2, arg_59_3)
	if arg_59_0.timer then
		arg_59_0.timer:Stop()

		arg_59_0.timer = nil
	end

	local function var_59_0(arg_60_0)
		arg_59_0[arg_59_1] = arg_60_0
		arg_60_0.anchoredPosition = arg_59_2

		setActive(arg_60_0, true)

		arg_59_0.timer = Timer.New(function()
			setActive(arg_60_0, false)
			arg_59_0.timer:Stop()

			arg_59_0.timer = nil

			arg_59_3()
		end, 0.6, 1)

		arg_59_0.timer:Start()
	end

	local var_59_1 = arg_59_0[arg_59_1]

	if not var_59_1 then
		arg_59_0:LoadEffect(arg_59_1, var_59_0)
	else
		var_59_0(var_59_1)
	end
end

function var_0_0.GetRedPacket(arg_62_0)
	if #arg_62_0.redpackets <= 0 then
		local var_62_0 = Object.Instantiate(arg_62_0.redpacket, arg_62_0.redpacket.parent)

		table.insert(arg_62_0.redpackets, var_62_0.transform)
	end

	local var_62_1 = table.remove(arg_62_0.redpackets, 1)

	setActive(var_62_1, true)

	return var_62_1
end

function var_0_0.LoadEffect(arg_63_0, arg_63_1, arg_63_2)
	ResourceMgr.Inst:getAssetAsync("UI/" .. arg_63_1, "", UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_64_0)
		if arg_63_0.exited then
			return
		end

		arg_63_2(Object.Instantiate(arg_64_0, arg_63_0._tf).transform)
	end), true, true)
end

function var_0_0.willExit(arg_65_0)
	for iter_65_0, iter_65_1 in ipairs(arg_65_0.redpackets) do
		if LeanTween.isTweening(iter_65_1.gameObject) then
			LeanTween.cancel(iter_65_1)
		end
	end

	if LeanTween.isTweening(arg_65_0.char) then
		LeanTween.cancel(arg_65_0.char)
	end

	if arg_65_0.timer then
		arg_65_0.timer:Stop()

		arg_65_0.timer = nil
	end

	Input.multiTouchEnabled = true
end

return var_0_0
