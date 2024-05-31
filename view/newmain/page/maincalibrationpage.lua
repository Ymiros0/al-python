local var_0_0 = class("MainCalibrationPage", import("view.base.BaseSubView"))

function var_0_0.getUIName(arg_1_0)
	return "MainCalibrationUI"
end

function var_0_0.OnLoaded(arg_2_0)
	arg_2_0.moveBtn = arg_2_0:findTF("move")
	arg_2_0.setBtn = arg_2_0:findTF("set")
	arg_2_0.backBtn = arg_2_0:findTF("back")
	arg_2_0.resetBtn = arg_2_0:findTF("reset")
	arg_2_0.saveBtn = arg_2_0:findTF("save")
	arg_2_0.bgImage = arg_2_0._tf:Find("adapt/bg"):GetComponent(typeof(Image))
	arg_2_0.paintingTF = arg_2_0._parentTf:Find("paint")
	arg_2_0._bgTf = arg_2_0._parentTf:Find("paintBg")
	arg_2_0.l2dContainer = arg_2_0.paintingTF:Find("live2d")
	arg_2_0.spineContainer = arg_2_0.paintingTF:Find("spinePainting")
	arg_2_0.setBtnX = arg_2_0.setBtn.localPosition.x
	arg_2_0.showing = false
end

function var_0_0.OnInit(arg_3_0)
	local var_3_0 = false
	local var_3_1 = false

	onToggle(arg_3_0, arg_3_0.moveBtn, function(arg_4_0)
		var_3_0 = arg_4_0

		arg_3_0:Move(arg_4_0)
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0._parentTf, function()
		if var_3_1 then
			return
		end

		if arg_3_0.showing and not var_3_0 then
			if var_3_1 then
				triggerToggle(arg_3_0.setBtn, false)
			end

			arg_3_0:emit(NewMainScene.FOLD, false)
		end
	end)
	onButton(arg_3_0, arg_3_0.backBtn, function()
		if var_3_0 then
			triggerToggle(arg_3_0.moveBtn, false)
		end

		arg_3_0:emit(NewMainScene.FOLD, false)
	end, SFX_PANEL)
	onToggle(arg_3_0, arg_3_0.setBtn, function(arg_7_0)
		var_3_1 = arg_7_0

		arg_3_0:SetPostion(arg_7_0)
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0.saveBtn, function()
		arg_3_0:SavePostion()
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0.resetBtn, function()
		arg_3_0:ResetPostion()
	end, SFX_PANEL)
end

function var_0_0.Move(arg_10_0, arg_10_1)
	setToggleEnabled(arg_10_0.setBtn, not arg_10_1)
	arg_10_0:emit(NewMainScene.ENABLE_PAITING_MOVE, arg_10_1)
end

function var_0_0.SetPostion(arg_11_0, arg_11_1)
	local function var_11_0()
		setActive(arg_11_0.moveBtn, not arg_11_1)
		setActive(arg_11_0.backBtn, not arg_11_1)
	end

	arg_11_0.bgImage.enabled = arg_11_1

	local var_11_1 = arg_11_1 and arg_11_0.moveBtn.localPosition.x or arg_11_0.setBtnX

	LeanTween.moveLocalX(arg_11_0.setBtn.gameObject, var_11_1, 0.2)

	local var_11_2 = arg_11_1 and -150 or 0
	local var_11_3 = arg_11_1 and 0 or -150
	local var_11_4 = LeanTween.value(arg_11_0.backBtn.gameObject, var_11_3, var_11_2, 0.3):setOnUpdate(System.Action_float(function(arg_13_0)
		arg_11_0.resetBtn.anchoredPosition = Vector2(arg_13_0, arg_11_0.resetBtn.anchoredPosition.y)
		arg_11_0.saveBtn.anchoredPosition = Vector2(arg_13_0, arg_11_0.saveBtn.anchoredPosition.y)
	end))

	if arg_11_1 then
		var_11_0()
	else
		var_11_4:setOnComplete(System.Action(var_11_0))
	end

	arg_11_0:emit(NewMainScene.ENABLE_PAITING_MOVE, arg_11_1)
end

function var_0_0.SavePostion(arg_14_0)
	local var_14_0 = arg_14_0.paintingTF.anchoredPosition
	local var_14_1 = arg_14_0.paintingTF.localScale.x
	local var_14_2 = arg_14_0.flagShip.skinId

	pg.MsgboxMgr.GetInstance():ShowMsgBox({
		content = i18n("secretary_pos_save"),
		onYes = function()
			getProxy(SettingsProxy):setSkinPosSetting(arg_14_0.flagShip, var_14_0.x, var_14_0.y, var_14_1)
			pg.TipsMgr.GetInstance():ShowTips(i18n("secretary_pos_save_success"))
			triggerToggle(arg_14_0.setBtn, false)
			arg_14_0:emit(NewMainScene.FOLD, false)
		end
	})
end

function var_0_0.ResetPostion(arg_16_0)
	getProxy(SettingsProxy):resetSkinPosSetting(arg_16_0.flagShip)

	local var_16_0 = MainPaintingView.GetAssistantStatus(arg_16_0.flagShip)
	local var_16_1, var_16_2 = arg_16_0.shift:GetMeshImageShift()

	arg_16_0.paintingTF.anchoredPosition = var_16_1
	arg_16_0._bgTf.anchoredPosition = var_16_1

	local var_16_3, var_16_4 = arg_16_0.shift:GetL2dShift()

	arg_16_0.l2dContainer.anchoredPosition = var_16_3

	local var_16_5, var_16_6 = arg_16_0.shift:GetSpineShift()

	arg_16_0.spineContainer.anchoredPosition = var_16_5

	if var_16_0 == MainPaintingView.STATE_L2D then
		arg_16_0._bgTf.localScale = var_16_4
		arg_16_0.paintingTF.localScale = var_16_4
	elseif var_16_0 == MainPaintingView.STATE_SPINE_PAINTING then
		arg_16_0._bgTf.localScale = var_16_6
		arg_16_0.paintingTF.localScale = var_16_6
	else
		arg_16_0._bgTf.localScale = var_16_2
		arg_16_0.paintingTF.localScale = var_16_2
	end
end

function var_0_0.ShowOrHide(arg_17_0, arg_17_1, arg_17_2, arg_17_3, arg_17_4)
	if arg_17_1 then
		arg_17_0:Show(arg_17_3)
		arg_17_0:UpdateBg(arg_17_4)
	else
		arg_17_0:Hide()
	end

	arg_17_0.flagShip = arg_17_2
	arg_17_0.showing = arg_17_1
end

function var_0_0.UpdateBg(arg_18_0, arg_18_1)
	if arg_18_1 == arg_18_0.bgName then
		return
	end

	LoadSpriteAsync("clutter/" .. arg_18_1, function(arg_19_0)
		if arg_18_0.exited then
			return
		end

		arg_18_0.bgImage.sprite = arg_19_0
	end)

	arg_18_0.bgName = arg_18_1
end

function var_0_0.Show(arg_20_0, arg_20_1)
	var_0_0.super.Show(arg_20_0)

	arg_20_0.shift = arg_20_1

	arg_20_0:DoBottomAnimation(0, 100)
	arg_20_0:DoLeftAnimation(0, -150, function()
		return
	end)
end

function var_0_0.DoLeftAnimation(arg_22_0, arg_22_1, arg_22_2, arg_22_3)
	LeanTween.value(arg_22_0.backBtn.gameObject, arg_22_1, arg_22_2, 0.3):setOnUpdate(System.Action_float(function(arg_23_0)
		arg_22_0.backBtn.anchoredPosition = Vector2(arg_23_0, arg_22_0.backBtn.anchoredPosition.y)
	end)):setOnComplete(System.Action(arg_22_3))
end

function var_0_0.DoBottomAnimation(arg_24_0, arg_24_1, arg_24_2)
	LeanTween.value(arg_24_0.moveBtn.gameObject, arg_24_1, arg_24_2, 0.3):setOnUpdate(System.Action_float(function(arg_25_0)
		arg_24_0.moveBtn.anchoredPosition = Vector2(arg_24_0.moveBtn.anchoredPosition.x, arg_25_0)
		arg_24_0.setBtn.anchoredPosition = Vector2(arg_24_0.setBtn.anchoredPosition.x, arg_25_0)
	end))
end

function var_0_0.Hide(arg_26_0)
	arg_26_0:DoBottomAnimation(100, 0)
	arg_26_0:DoLeftAnimation(-150, 0, function()
		var_0_0.super.Hide(arg_26_0)
	end)
end

function var_0_0.Reset(arg_28_0)
	var_0_0.super.Reset(arg_28_0)

	arg_28_0.exited = false
end

function var_0_0.OnDestroy(arg_29_0)
	arg_29_0.exited = true
	arg_29_0.bgName = nil
end

return var_0_0
