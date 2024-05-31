local var_0_0 = class("CourtYardStoreyModule", import("..CourtYardBaseModule"))
local var_0_1 = false

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0.modules = {}
	arg_1_0.gridAgents = {
		CourtYardGridAgent.New(arg_1_0),
		CourtYardWallGridAgent.New(arg_1_0)
	}
	arg_1_0.effectAgent = CourtYardEffectAgent.New(arg_1_0)
	arg_1_0.soundAgent = CourtYardSoundAgent.New(arg_1_0)
	arg_1_0.bgAgent = CourtYardBGAgent.New(arg_1_0)
	arg_1_0.bgmAgent = CourtYardBGMAgent.New(arg_1_0)
	arg_1_0.factorys = {
		[CourtYardConst.OBJ_TYPE_SHIP] = CourtYardShipFactory.New(arg_1_0:GetView().poolMgr),
		[CourtYardConst.OBJ_TYPE_COMMOM] = CourtYardFurnitureFactory.New(arg_1_0:GetView().poolMgr)
	}
	arg_1_0.descPage = CourtYardFurnitureDescPage.New(arg_1_0)
	arg_1_0.playTheLutePage = CourtyardPlayTheLutePage.New(arg_1_0)
end

function var_0_0.GetDefaultBgm(arg_2_0)
	return pg.voice_bgm.CourtYardScene.default_bgm
end

function var_0_0.OnInit(arg_3_0)
	arg_3_0.zoomAgent = arg_3_0._tf:Find("bg"):GetComponent("PinchZoom")
	arg_3_0.scrollrect = arg_3_0._tf:Find("scroll_view")
	arg_3_0.bg = arg_3_0._tf:Find("bg")
	arg_3_0.rectTF = arg_3_0._tf:Find("bg/rect")
	arg_3_0.gridsTF = arg_3_0.rectTF:Find("grids")
	arg_3_0.rootTF = arg_3_0._tf:Find("root")
	arg_3_0.selectedTF = arg_3_0._tf:Find("root/drag")
	arg_3_0.selectedAnimation = arg_3_0.selectedTF:GetComponent(typeof(Animation))
	arg_3_0.dftAniEvent = arg_3_0.selectedTF:GetComponent(typeof(DftAniEvent))
	arg_3_0.rotationBtn = arg_3_0.selectedTF:Find("panel/animroot/rotation")
	arg_3_0.removeBtn = arg_3_0.selectedTF:Find("panel/animroot/cancel")
	arg_3_0.confirmBtn = arg_3_0.selectedTF:Find("panel/animroot/ok")
	arg_3_0.dragBtn = CourtYardStoreyDragBtn.New(arg_3_0.selectedTF:Find("panel/animroot"), arg_3_0.rectTF)
	arg_3_0.effectContainer = arg_3_0._tf:Find("effects")

	local var_3_0 = arg_3_0.rootTF:Find("white"):GetComponent(typeof(Image)).material
	local var_3_1 = arg_3_0.rootTF:Find("green"):GetComponent(typeof(Image)).material
	local var_3_2 = arg_3_0.rootTF:Find("red"):GetComponent(typeof(Image)).material

	arg_3_0.furnitureStateMgrs = {
		CourtyardFurnitureState.New(arg_3_0._tf:Find("root/furnitureState"), arg_3_0.rectTF, var_3_0, var_3_1, var_3_2),
		CourtyardSpineFurnitureState.New(arg_3_0._tf:Find("root/furnitureSpineState"), arg_3_0.rectTF, var_3_0, var_3_1, var_3_2)
	}

	arg_3_0:InitPedestalModule()

	arg_3_0.bg.localScale = Vector3(1.438, 1.438, 1)
end

function var_0_0.GetFurnitureStateMgr(arg_4_0, arg_4_1)
	return arg_4_1:IsSpine() and arg_4_0.furnitureStateMgrs[2] or arg_4_0.furnitureStateMgrs[1]
end

function var_0_0.InitPedestalModule(arg_5_0)
	arg_5_0.pedestalModule = CourtYardPedestalModule.New(arg_5_0.data, arg_5_0.bg)
end

function var_0_0.AddListeners(arg_6_0)
	arg_6_0:AddListener(CourtYardEvent.INITED, arg_6_0.OnInited)
	arg_6_0:AddListener(CourtYardEvent.CREATE_ITEM, arg_6_0.OnCreateItem)
	arg_6_0:AddListener(CourtYardEvent.REMOVE_ITEM, arg_6_0.OnRemoveItem)
	arg_6_0:AddListener(CourtYardEvent.ADD_MAT_ITEM, arg_6_0.OnAddMatItem)
	arg_6_0:AddListener(CourtYardEvent.REMOVE_MAT_ITEM, arg_6_0.OnRemoveMatItem)
	arg_6_0:AddListener(CourtYardEvent.ADD_ITEM, arg_6_0.OnAddItem)
	arg_6_0:AddListener(CourtYardEvent.DRAG_ITEM, arg_6_0.OnDragItem)
	arg_6_0:AddListener(CourtYardEvent.DRAGING_ITEM, arg_6_0.OnDragingItem)
	arg_6_0:AddListener(CourtYardEvent.DRAG_ITEM_END, arg_6_0.OnDragItemEnd)
	arg_6_0:AddListener(CourtYardEvent.SELETED_ITEM, arg_6_0.OnSelectedItem)
	arg_6_0:AddListener(CourtYardEvent.UNSELETED_ITEM, arg_6_0.OnUnSelectedItem)
	arg_6_0:AddListener(CourtYardEvent.ENTER_EDIT_MODE, arg_6_0.OnEnterEidtMode)
	arg_6_0:AddListener(CourtYardEvent.EXIT_EDIT_MODE, arg_6_0.OnExitEidtMode)
	arg_6_0:AddListener(CourtYardEvent.ROTATE_ITEM, arg_6_0.OnItemDirChange)
	arg_6_0:AddListener(CourtYardEvent.ROTATE_ITEM_FAILED, arg_6_0.OnRotateItemFailed)
	arg_6_0:AddListener(CourtYardEvent.DETORY_ITEM, arg_6_0.OnDestoryItem)
	arg_6_0:AddListener(CourtYardEvent.CHILD_ITEM, arg_6_0.OnChildItem)
	arg_6_0:AddListener(CourtYardEvent.UN_CHILD_ITEM, arg_6_0.OnUnChildItem)
	arg_6_0:AddListener(CourtYardEvent.REMIND_SAVE, arg_6_0.OnRemindSave)
	arg_6_0:AddListener(CourtYardEvent.ADD_ITEM_FAILED, arg_6_0.OnAddItemFailed)
	arg_6_0:AddListener(CourtYardEvent.SHOW_FURNITURE_DESC, arg_6_0.OnShowFurnitureDesc)
	arg_6_0:AddListener(CourtYardEvent.ITEM_INTERACTION, arg_6_0.OnItemInterAction)
	arg_6_0:AddListener(CourtYardEvent.CLEAR_ITEM_INTERACTION, arg_6_0.OnClearItemInterAction)
	arg_6_0:AddListener(CourtYardEvent.ON_TOUCH_ITEM, arg_6_0.OnTouchItem)
	arg_6_0:AddListener(CourtYardEvent.ON_CANCEL_TOUCH_ITEM, arg_6_0.OnCancelTouchItem)
	arg_6_0:AddListener(CourtYardEvent.ON_ITEM_PLAY_MUSIC, arg_6_0.OnItemPlayMusic)
	arg_6_0:AddListener(CourtYardEvent.ON_ITEM_STOP_MUSIC, arg_6_0.OnItemStopMusic)
	arg_6_0:AddListener(CourtYardEvent.ON_ADD_EFFECT, arg_6_0.OnAddEffect)
	arg_6_0:AddListener(CourtYardEvent.ON_REMOVE_EFFECT, arg_6_0.OnRemoveEffect)
	arg_6_0:AddListener(CourtYardEvent.DISABLE_ROTATE_ITEM, arg_6_0.OnDisableRotation)
	arg_6_0:AddListener(CourtYardEvent.TAKE_PHOTO, arg_6_0.OnTakePhoto)
	arg_6_0:AddListener(CourtYardEvent.END_TAKE_PHOTO, arg_6_0.OnEndTakePhoto)
	arg_6_0:AddListener(CourtYardEvent.ENTER_ARCH, arg_6_0.OnEnterArch)
	arg_6_0:AddListener(CourtYardEvent.EXIT_ARCH, arg_6_0.OnExitArch)
	arg_6_0:AddListener(CourtYardEvent.REMOVE_ILLEGALITY_ITEM, arg_6_0.OnRemoveIllegalityItem)
	arg_6_0:AddListener(CourtYardEvent.OPEN_LAYER, arg_6_0.OnOpenLayer)
	arg_6_0:AddListener(CourtYardEvent.FURNITURE_PLAY_MUSICALINSTRUMENTS, arg_6_0.OnPlayMusicalInstruments)
	arg_6_0:AddListener(CourtYardEvent.FURNITURE_STOP_PLAY_MUSICALINSTRUMENTS, arg_6_0.OnStopPlayMusicalInstruments)
	arg_6_0:AddListener(CourtYardEvent.FURNITURE_MUTE_ALL, arg_6_0.OnMuteAll)
	arg_6_0:AddListener(CourtYardEvent.BACK_PRESSED, arg_6_0.OnBackPressed)
end

function var_0_0.RemoveListeners(arg_7_0)
	arg_7_0:RemoveListener(CourtYardEvent.INITED, arg_7_0.OnInited)
	arg_7_0:RemoveListener(CourtYardEvent.CREATE_ITEM, arg_7_0.OnCreateItem)
	arg_7_0:RemoveListener(CourtYardEvent.REMOVE_ITEM, arg_7_0.OnRemoveItem)
	arg_7_0:RemoveListener(CourtYardEvent.ADD_MAT_ITEM, arg_7_0.OnAddMatItem)
	arg_7_0:RemoveListener(CourtYardEvent.REMOVE_MAT_ITEM, arg_7_0.OnRemoveMatItem)
	arg_7_0:RemoveListener(CourtYardEvent.ADD_ITEM, arg_7_0.OnAddItem)
	arg_7_0:RemoveListener(CourtYardEvent.DRAG_ITEM, arg_7_0.OnDragItem)
	arg_7_0:RemoveListener(CourtYardEvent.DRAGING_ITEM, arg_7_0.OnDragingItem)
	arg_7_0:RemoveListener(CourtYardEvent.DRAG_ITEM_END, arg_7_0.OnDragItemEnd)
	arg_7_0:RemoveListener(CourtYardEvent.SELETED_ITEM, arg_7_0.OnSelectedItem)
	arg_7_0:RemoveListener(CourtYardEvent.UNSELETED_ITEM, arg_7_0.OnUnSelectedItem)
	arg_7_0:RemoveListener(CourtYardEvent.ENTER_EDIT_MODE, arg_7_0.OnEnterEidtMode)
	arg_7_0:RemoveListener(CourtYardEvent.EXIT_EDIT_MODE, arg_7_0.OnExitEidtMode)
	arg_7_0:RemoveListener(CourtYardEvent.ROTATE_ITEM, arg_7_0.OnItemDirChange)
	arg_7_0:RemoveListener(CourtYardEvent.ROTATE_ITEM_FAILED, arg_7_0.OnRotateItemFailed)
	arg_7_0:RemoveListener(CourtYardEvent.DETORY_ITEM, arg_7_0.OnDestoryItem)
	arg_7_0:RemoveListener(CourtYardEvent.CHILD_ITEM, arg_7_0.OnChildItem)
	arg_7_0:RemoveListener(CourtYardEvent.UN_CHILD_ITEM, arg_7_0.OnUnChildItem)
	arg_7_0:RemoveListener(CourtYardEvent.REMIND_SAVE, arg_7_0.OnRemindSave)
	arg_7_0:RemoveListener(CourtYardEvent.ADD_ITEM_FAILED, arg_7_0.OnAddItemFailed)
	arg_7_0:RemoveListener(CourtYardEvent.SHOW_FURNITURE_DESC, arg_7_0.OnShowFurnitureDesc)
	arg_7_0:RemoveListener(CourtYardEvent.ITEM_INTERACTION, arg_7_0.OnItemInterAction)
	arg_7_0:RemoveListener(CourtYardEvent.CLEAR_ITEM_INTERACTION, arg_7_0.OnClearItemInterAction)
	arg_7_0:RemoveListener(CourtYardEvent.ON_TOUCH_ITEM, arg_7_0.OnTouchItem)
	arg_7_0:RemoveListener(CourtYardEvent.ON_CANCEL_TOUCH_ITEM, arg_7_0.OnCancelTouchItem)
	arg_7_0:RemoveListener(CourtYardEvent.ON_ITEM_PLAY_MUSIC, arg_7_0.OnItemPlayMusic)
	arg_7_0:RemoveListener(CourtYardEvent.ON_ITEM_STOP_MUSIC, arg_7_0.OnItemStopMusic)
	arg_7_0:RemoveListener(CourtYardEvent.ON_ADD_EFFECT, arg_7_0.OnAddEffect)
	arg_7_0:RemoveListener(CourtYardEvent.ON_REMOVE_EFFECT, arg_7_0.OnRemoveEffect)
	arg_7_0:RemoveListener(CourtYardEvent.DISABLE_ROTATE_ITEM, arg_7_0.OnDisableRotation)
	arg_7_0:RemoveListener(CourtYardEvent.TAKE_PHOTO, arg_7_0.OnTakePhoto)
	arg_7_0:RemoveListener(CourtYardEvent.END_TAKE_PHOTO, arg_7_0.OnEndTakePhoto)
	arg_7_0:RemoveListener(CourtYardEvent.ENTER_ARCH, arg_7_0.OnEnterArch)
	arg_7_0:RemoveListener(CourtYardEvent.EXIT_ARCH, arg_7_0.OnExitArch)
	arg_7_0:RemoveListener(CourtYardEvent.REMOVE_ILLEGALITY_ITEM, arg_7_0.OnRemoveIllegalityItem)
	arg_7_0:RemoveListener(CourtYardEvent.OPEN_LAYER, arg_7_0.OnOpenLayer)
	arg_7_0:RemoveListener(CourtYardEvent.FURNITURE_PLAY_MUSICALINSTRUMENTS, arg_7_0.OnPlayMusicalInstruments)
	arg_7_0:RemoveListener(CourtYardEvent.FURNITURE_STOP_PLAY_MUSICALINSTRUMENTS, arg_7_0.OnStopPlayMusicalInstruments)
	arg_7_0:RemoveListener(CourtYardEvent.FURNITURE_MUTE_ALL, arg_7_0.OnMuteAll)
	arg_7_0:RemoveListener(CourtYardEvent.BACK_PRESSED, arg_7_0.OnBackPressed)
end

function var_0_0.OnInited(arg_8_0)
	arg_8_0.isInit = true

	if var_0_1 then
		arg_8_0.mapDebug = CourtYardMapDebug.New(arg_8_0.data)
	end

	arg_8_0:RefreshDepth()
	arg_8_0:RefreshMatDepth()
end

function var_0_0.AllModulesAreCompletion(arg_9_0)
	for iter_9_0, iter_9_1 in pairs(arg_9_0.modules) do
		if not iter_9_1:IsCompletion() then
			return false
		end
	end

	return true
end

function var_0_0.OnRemindSave(arg_10_0)
	_BackyardMsgBoxMgr:Show({
		content = i18n("backyard_backyardScene_quest_saveFurniture"),
		onYes = function()
			arg_10_0:Emit("SaveFurnitures")
		end,
		yesSound = SFX_FURNITRUE_SAVE,
		onNo = function()
			arg_10_0:Emit("RestoreFurnitures")
		end
	})
end

function var_0_0.OnEnterEidtMode(arg_13_0)
	for iter_13_0, iter_13_1 in pairs(arg_13_0.modules) do
		if isa(iter_13_1, CourtYardShipModule) then
			iter_13_1:SetActive(false)
		else
			iter_13_1:BlocksRaycasts(true)
		end
	end

	arg_13_0.bg.localScale = Vector3(0.95, 0.95, 1)
end

function var_0_0.OnExitEidtMode(arg_14_0)
	for iter_14_0, iter_14_1 in pairs(arg_14_0.modules) do
		if isa(iter_14_1, CourtYardShipModule) then
			iter_14_1:SetActive(true)
		else
			iter_14_1:BlocksRaycasts(false)
		end
	end
end

function var_0_0.OnCreateItem(arg_15_0, arg_15_1, arg_15_2)
	local var_15_0 = arg_15_0.factorys[arg_15_1:GetObjType()]:Make(arg_15_1)

	if arg_15_2 then
		var_15_0:CreateWhenStoreyInit()
	end

	arg_15_0.modules[arg_15_1:GetDeathType() .. arg_15_1.id] = var_15_0
end

function var_0_0.OnAddItem(arg_16_0)
	if not arg_16_0.isInit then
		return
	end

	arg_16_0:RefreshDepth()

	if var_0_1 then
		arg_16_0.mapDebug:Flush()
	end
end

function var_0_0.OnRemoveItem(arg_17_0, arg_17_1)
	arg_17_0:Item2Module(arg_17_1):SetAsLastSibling()

	if var_0_1 then
		arg_17_0.mapDebug:Flush()
	end
end

function var_0_0.OnSelectedItem(arg_18_0, arg_18_1, arg_18_2)
	arg_18_0.selectedModule = arg_18_0:Item2Module(arg_18_1)
	arg_18_0.gridAgent = arg_18_0:GetGridAgent(arg_18_1, arg_18_2)

	if isa(arg_18_1, CourtYardFurniture) then
		arg_18_0.selectedAnimation:Play("anim_courtyard_dragin")

		local var_18_0 = arg_18_0:Item2Module(arg_18_1)

		arg_18_0:InitFurnitureState(var_18_0, arg_18_1)
		setParent(arg_18_0.selectedTF, arg_18_0.rectTF)

		arg_18_0.selectedTF.sizeDelta = var_18_0._tf.sizeDelta

		arg_18_0:UpdateSelectedPosition(arg_18_1)
		arg_18_0:RegisterOp(arg_18_1)
	end
end

function var_0_0.InitFurnitureState(arg_19_0, arg_19_1, arg_19_2)
	arg_19_0:GetFurnitureStateMgr(arg_19_2):OnInit(arg_19_1, arg_19_2)
end

function var_0_0.UpdateFurnitureState(arg_20_0, arg_20_1, arg_20_2, arg_20_3)
	local var_20_0 = arg_20_0:GetFurnitureStateMgr(arg_20_3)

	if _.any(arg_20_2, function(arg_21_0)
		return arg_21_0.flag == 2
	end) then
		var_20_0:OnCantPlace()
	else
		var_20_0:OnCanPlace()
	end
end

function var_0_0.ResetFurnitureSelectedState(arg_22_0, arg_22_1)
	local var_22_0 = arg_22_0:GetFurnitureStateMgr(arg_22_1)
	local var_22_1 = arg_22_0:Item2Module(arg_22_1)

	var_22_0:OnReset(var_22_1)
end

function var_0_0.ClearFurnitureSelectedState(arg_23_0, arg_23_1)
	arg_23_0:GetFurnitureStateMgr(arg_23_1):OnClear()
end

function var_0_0.OnDragItem(arg_24_0, arg_24_1)
	arg_24_0:EnableZoom(false)
end

function var_0_0.OnDragingItem(arg_25_0, arg_25_1, arg_25_2, arg_25_3, arg_25_4)
	local var_25_0 = arg_25_0:Item2Module(arg_25_1)

	var_25_0:UpdatePosition(arg_25_3, arg_25_4)
	arg_25_0.gridAgent:Flush(arg_25_2)

	if isa(arg_25_1, CourtYardFurniture) then
		arg_25_0:UpdateSelectedPosition(arg_25_1)
		arg_25_0:UpdateFurnitureState(var_25_0, arg_25_2, arg_25_1)
	end
end

function var_0_0.OnDragItemEnd(arg_26_0, arg_26_1, arg_26_2)
	arg_26_0:EnableZoom(true)

	if isa(arg_26_1, CourtYardFurniture) then
		arg_26_0.gridAgent:Flush(arg_26_2)
		arg_26_0:UpdateSelectedPosition(arg_26_1)
		arg_26_0:ResetFurnitureSelectedState(arg_26_1)
	end
end

function var_0_0.OnUnSelectedItem(arg_27_0, arg_27_1)
	arg_27_0.selectedModule = nil

	arg_27_0.gridAgent:Clear()

	arg_27_0.gridAgent = nil

	if isa(arg_27_1, CourtYardFurniture) then
		arg_27_0.dftAniEvent:SetEndEvent(function()
			arg_27_0.dftAniEvent:SetEndEvent(nil)
			setParent(arg_27_0.selectedTF, arg_27_0.rootTF)
		end)
		arg_27_0:ClearFurnitureSelectedState(arg_27_1)
		arg_27_0.selectedAnimation:Play("anim_courtyard_dragout")
		arg_27_0:UnRegisterOp()
	end
end

function var_0_0.OnRemoveIllegalityItem(arg_29_0)
	pg.TipsMgr.GetInstance():ShowTips("Remove illegal Item")
end

function var_0_0.OnOpenLayer(arg_30_0, arg_30_1)
	for iter_30_0, iter_30_1 in pairs(arg_30_0.modules) do
		if isa(iter_30_1, CourtYardShipModule) then
			iter_30_1:HideAttachment(arg_30_1)
		end
	end
end

function var_0_0.EnableZoom(arg_31_0, arg_31_1)
	arg_31_0.zoomAgent.enabled = arg_31_1
end

function var_0_0.RegisterOp(arg_32_0, arg_32_1)
	setActive(arg_32_0.rotationBtn, not arg_32_1:DisableRotation())
	onButton(arg_32_0, arg_32_0.rotationBtn, function()
		arg_32_0:Emit("RotateFurniture", arg_32_1.id)
	end, SFX_PANEL)
	onButton(arg_32_0, arg_32_0.confirmBtn, function()
		arg_32_0:Emit("UnSelectFurniture", arg_32_1.id)
	end, SFX_PANEL)
	onButton(arg_32_0, arg_32_0.removeBtn, function()
		arg_32_0:Emit("RemoveFurniture", arg_32_1.id)
	end, SFX_PANEL)
	onButton(arg_32_0, arg_32_0.scrollrect, function()
		arg_32_0:Emit("UnSelectFurniture", arg_32_1.id)
	end, SFX_PANEL)

	local function var_32_0()
		arg_32_0:Emit("BeginDragFurniture", arg_32_1.id)
	end

	local function var_32_1(arg_38_0)
		arg_32_0:Emit("DragingFurniture", arg_32_1.id, arg_38_0)
	end

	local function var_32_2(arg_39_0)
		arg_32_0:Emit("DragFurnitureEnd", arg_32_1.id, arg_39_0)
	end

	arg_32_0.dragBtn:Active(var_32_0, var_32_1, var_32_2)
end

function var_0_0.UnRegisterOp(arg_40_0)
	removeOnButton(arg_40_0.rotationBtn)
	removeOnButton(arg_40_0.confirmBtn)
	removeOnButton(arg_40_0.removeBtn)
	removeOnButton(arg_40_0.scrollrect)
	arg_40_0.dragBtn:DeActive(false)
end

function var_0_0.OnItemDirChange(arg_41_0, arg_41_1, arg_41_2)
	if isa(arg_41_1, CourtYardFurniture) then
		arg_41_0:UpdateSelectedPosition(arg_41_1)

		if arg_41_0.data:InEidtMode() and arg_41_0.gridAgent then
			arg_41_0.gridAgent:Flush(arg_41_2)
		end

		arg_41_0:GetFurnitureStateMgr(arg_41_1):OnUpdateScale(arg_41_0:Item2Module(arg_41_1))
	else
		arg_41_0.gridAgent:Flush(arg_41_2)
	end
end

function var_0_0.OnRotateItemFailed(arg_42_0)
	pg.TipsMgr.GetInstance():ShowTips(i18n("backyard_backyardScene_error_canNotRotate"))
end

function var_0_0.OnDisableRotation(arg_43_0)
	pg.TipsMgr.GetInstance():ShowTips(i18n("backyard_backyardScene_Disable_Rotation"))
end

function var_0_0.OnAddItemFailed(arg_44_0)
	pg.TipsMgr.GetInstance():ShowTips(i18n("backyard_backyardScene_error_noPosPutFurniture"))
end

function var_0_0.OnDestoryItem(arg_45_0, arg_45_1)
	arg_45_0:Item2Module(arg_45_1):Dispose()

	arg_45_0.modules[arg_45_1:GetDeathType() .. arg_45_1.id] = nil
end

function var_0_0.OnChildItem(arg_46_0, arg_46_1, arg_46_2)
	local var_46_0 = arg_46_0:Item2Module(arg_46_1)
	local var_46_1 = arg_46_0:Item2Module(arg_46_2)

	var_46_1:AddChild(var_46_0)

	if isa(arg_46_1, CourtYardShip) then
		var_46_1:BlocksRaycasts(true)
	end
end

function var_0_0.OnUnChildItem(arg_47_0, arg_47_1, arg_47_2)
	local var_47_0 = arg_47_0:Item2Module(arg_47_1)
	local var_47_1 = arg_47_0:Item2Module(arg_47_2)

	var_47_1:RemoveChild(var_47_0)

	if isa(arg_47_1, CourtYardShip) then
		var_47_1:BlocksRaycasts(false)
	end
end

function var_0_0.OnEnterArch(arg_48_0, arg_48_1, arg_48_2)
	return
end

function var_0_0.OnExitArch(arg_49_0, arg_49_1, arg_49_2)
	return
end

function var_0_0.OnAddMatItem(arg_50_0)
	if not arg_50_0.isInit then
		return
	end

	arg_50_0:RefreshMatDepth()
end

function var_0_0.OnRemoveMatItem(arg_51_0, arg_51_1)
	arg_51_0:Item2Module(arg_51_1):SetAsLastSibling()
end

function var_0_0.OnShowFurnitureDesc(arg_52_0, arg_52_1)
	arg_52_0.descPage:ExecuteAction("Show", arg_52_1)
end

function var_0_0.OnItemInterAction(arg_53_0, arg_53_1, arg_53_2, arg_53_3)
	local var_53_0 = arg_53_0:Item2Module(arg_53_1)
	local var_53_1 = arg_53_0:Item2Module(arg_53_2)

	var_53_1:BlocksRaycasts(true)

	local var_53_2 = {}

	if arg_53_3:GetBodyMask() then
		table.insert(var_53_2, var_53_1:GetBodyMask(arg_53_3.id))
	end

	local var_53_3 = arg_53_3:GetUsingAnimator()

	if var_53_3 then
		table.insert(var_53_2, var_53_1:GetAnimator(var_53_3.key))
	end

	local var_53_4

	if #var_53_2 == 0 then
		var_53_0._tf:SetParent(var_53_1.interactionTF)

		var_53_4 = var_53_0._tf
	else
		local var_53_5 = var_53_0._tf

		for iter_53_0, iter_53_1 in ipairs(var_53_2) do
			var_53_5:SetParent(iter_53_1, false)

			var_53_5 = iter_53_1
		end

		var_53_4 = var_53_5

		local var_53_6 = CourtYardCalcUtil.GetSign(var_53_1._tf.localScale.x)
		local var_53_7 = var_53_0._tf.localScale

		var_53_0._tf.localScale = Vector3(var_53_6 * var_53_7.x, var_53_7.y, 1)
	end

	var_53_0:SetSiblingIndex(arg_53_3.id - 1)
	arg_53_0.bgmAgent:Play(arg_53_2:GetInterActionBgm())
	arg_53_0:AddInteractionFollower(arg_53_3, var_53_4, var_53_1)
end

function var_0_0.OnClearItemInterAction(arg_54_0, arg_54_1, arg_54_2, arg_54_3)
	local var_54_0 = arg_54_0:Item2Module(arg_54_1)
	local var_54_1 = arg_54_0:Item2Module(arg_54_2)

	if isa(var_54_1, CourtYardFurnitureModule) and #arg_54_2:GetUsingSlots() == 0 then
		var_54_1:BlocksRaycasts(false)
	end

	local var_54_2 = arg_54_0:Item2Module(arg_54_2)

	if arg_54_3:GetBodyMask() then
		local var_54_3 = var_54_1:GetBodyMask(arg_54_3.id)

		var_54_3:SetParent(var_54_1.interactionTF)

		local var_54_4 = arg_54_2:GetBodyMasks()[arg_54_3.id]

		var_54_3.sizeDelta = var_54_4.size
		var_54_3.anchoredPosition = var_54_4.offset
	end

	var_54_0._tf:SetParent(var_54_0:GetParentTF())
	arg_54_0.bgmAgent:Stop(arg_54_2:GetInterActionBgm())
	arg_54_0:ClearInteractionFollower(arg_54_3, var_54_0, var_54_1)
end

function var_0_0.AddInteractionFollower(arg_55_0, arg_55_1, arg_55_2, arg_55_3)
	local var_55_0 = arg_55_1:GetFollower()

	if not var_55_0 or not arg_55_2 then
		return
	end

	local var_55_1 = var_55_0.bone
	local var_55_2 = arg_55_3:FindBoneFollower(var_55_1)

	if IsNil(var_55_2) then
		var_55_2 = arg_55_3:NewBoneFollower(var_55_1)
	else
		setActive(var_55_2, true)
	end

	var_55_2.localScale = Vector3(1, 1, 1)

	arg_55_2:SetParent(var_55_2, false)
end

function var_0_0.ClearInteractionFollower(arg_56_0, arg_56_1, arg_56_2, arg_56_3)
	local var_56_0 = arg_56_1:GetFollower()

	if not var_56_0 then
		return
	end

	local var_56_1 = var_56_0.bone
	local var_56_2 = arg_56_3:FindBoneFollower(var_56_1)

	if not IsNil(var_56_2) then
		setActive(var_56_2, false)
	end
end

function var_0_0.OnTouchItem(arg_57_0, arg_57_1)
	if isa(arg_57_1, CourtYardFurniture) then
		arg_57_0.effectAgent:EnableEffect(arg_57_1:GetTouchEffect())
		arg_57_0.soundAgent:Play(arg_57_1:GetTouchSound())
		arg_57_0.bgAgent:Switch(true, arg_57_1:GetTouchBg())
	end
end

function var_0_0.OnCancelTouchItem(arg_58_0, arg_58_1)
	if isa(arg_58_1, CourtYardFurniture) then
		arg_58_0.effectAgent:DisableEffect(arg_58_1:GetTouchEffect())
		arg_58_0.bgAgent:Switch(false, arg_58_1:GetTouchBg())
	end
end

function var_0_0.OnItemPlayMusic(arg_59_0, arg_59_1, arg_59_2)
	if arg_59_2 == 1 then
		arg_59_0.soundAgent:Play(arg_59_1)
	elseif arg_59_2 == 2 then
		arg_59_0.bgmAgent:Play(arg_59_1)
	end
end

function var_0_0.OnItemStopMusic(arg_60_0, arg_60_1, arg_60_2)
	if arg_60_2 == 2 then
		arg_60_0.bgmAgent:Reset()
	elseif arg_60_2 == 1 then
		arg_60_0.soundAgent:Stop()
	end
end

function var_0_0.OnMuteAll(arg_61_0)
	arg_61_0.bgmAgent:Clear()
	arg_61_0.soundAgent:Clear()
end

function var_0_0.OnPlayMusicalInstruments(arg_62_0, arg_62_1)
	if arg_62_0.descPage and arg_62_0.descPage:GetLoaded() and arg_62_0.descPage:isShowing() then
		arg_62_0.descPage:Close()
	end

	if arg_62_1:GetType() == Furniture.TYPE_LUTE then
		arg_62_0.playTheLutePage:ExecuteAction("Show", arg_62_1)
	end
end

function var_0_0.OnStopPlayMusicalInstruments(arg_63_0, arg_63_1)
	arg_63_0.bgmAgent:Reset()

	if arg_63_0.descPage and arg_63_0.descPage:GetLoaded() then
		arg_63_0.descPage:ExecuteAction("Show", arg_63_1)
	end
end

function var_0_0.OnAddEffect(arg_64_0, arg_64_1)
	arg_64_0.effectAgent:EnableEffect(arg_64_1)
end

function var_0_0.OnRemoveEffect(arg_65_0, arg_65_1)
	arg_65_0.effectAgent:DisableEffect(arg_65_1)
end

function var_0_0.OnBackPressed(arg_66_0)
	if arg_66_0.playTheLutePage and arg_66_0.playTheLutePage:GetLoaded() and arg_66_0.playTheLutePage:isShowing() then
		arg_66_0.playTheLutePage:Hide()

		return
	end

	if arg_66_0.descPage and arg_66_0.descPage:GetLoaded() and arg_66_0.descPage:isShowing() then
		arg_66_0.descPage:Close()

		return
	end

	arg_66_0:Emit("Quit")
end

function var_0_0.UpdateSelectedPosition(arg_67_0, arg_67_1)
	local var_67_0 = arg_67_0:Item2Module(arg_67_1)
	local var_67_1 = var_67_0:GetCenterPoint()

	arg_67_0.selectedTF.localPosition = var_67_1

	arg_67_0:GetFurnitureStateMgr(arg_67_1):OnUpdate(var_67_0)
end

function var_0_0.GetGridAgent(arg_68_0, arg_68_1, arg_68_2)
	local var_68_0

	if isa(arg_68_1, CourtYardWallFurniture) then
		var_68_0 = arg_68_0.gridAgents[2]
	else
		var_68_0 = arg_68_0.gridAgents[1]
	end

	if arg_68_0.gridAgent and var_68_0 ~= arg_68_0.gridAgent then
		arg_68_0.gridAgent:Clear()
	end

	var_68_0:Reset(arg_68_2)

	return var_68_0
end

function var_0_0.ItemsIsLoaded(arg_69_0)
	if table.getCount(arg_69_0.modules) == 0 then
		return false
	end

	for iter_69_0, iter_69_1 in pairs(arg_69_0.modules) do
		if not iter_69_1:IsInit() then
			return false
		end
	end

	return true
end

function var_0_0.Item2Module(arg_70_0, arg_70_1)
	return arg_70_0.modules[arg_70_1:GetDeathType() .. arg_70_1.id]
end

function var_0_0.RefreshDepth(arg_71_0)
	for iter_71_0, iter_71_1 in ipairs(arg_71_0.data:GetItems()) do
		arg_71_0:Item2Module(iter_71_1):SetSiblingIndex(iter_71_0 - 1)
	end
end

function var_0_0.RefreshMatDepth(arg_72_0)
	for iter_72_0, iter_72_1 in ipairs(arg_72_0.data:GetMatItems()) do
		arg_72_0:Item2Module(iter_72_1):SetSiblingIndex(iter_72_0 - 1)
	end
end

function var_0_0.OnTakePhoto(arg_73_0)
	GetOrAddComponent(arg_73_0.selectedTF, typeof(CanvasGroup)).alpha = 0

	local var_73_0 = Vector3(0.6, 0.6, 1)

	arg_73_0.bgScale = arg_73_0.bg.localScale
	arg_73_0.bg.localScale = var_73_0

	if arg_73_0.bg.localPosition ~= Vector3(0, -100, 0) then
		arg_73_0.bgPos = arg_73_0.bg.localPosition
		arg_73_0.bg.localPosition = Vector3(0, -100, 0)
	end
end

function var_0_0.OnEndTakePhoto(arg_74_0)
	GetOrAddComponent(arg_74_0.selectedTF, typeof(CanvasGroup)).alpha = 1

	if arg_74_0.bgScale then
		arg_74_0.bg.localScale = arg_74_0.bgScale
	end

	if arg_74_0.bgPos then
		arg_74_0.bg.localPosition = arg_74_0.bgPos
	end
end

function var_0_0.OnDispose(arg_75_0)
	arg_75_0.exited = true

	arg_75_0.dftAniEvent:SetEndEvent(nil)

	for iter_75_0, iter_75_1 in pairs(arg_75_0.modules) do
		iter_75_1:Dispose()
	end

	arg_75_0.modules = nil

	for iter_75_2, iter_75_3 in pairs(arg_75_0.factorys) do
		iter_75_3:Dispose()
	end

	arg_75_0.factorys = nil

	arg_75_0.dragBtn:Dispose()

	arg_75_0.dragBtn = nil

	for iter_75_4, iter_75_5 in pairs(arg_75_0.gridAgents) do
		iter_75_5:Dispose()
	end

	arg_75_0.gridAgents = nil

	if var_0_1 then
		arg_75_0.mapDebug:Dispose()
	end

	if arg_75_0.pedestalModule then
		arg_75_0.pedestalModule:Dispose()

		arg_75_0.pedestalModule = nil
	end

	arg_75_0.effectAgent:Dispose()

	arg_75_0.effectAgent = nil

	arg_75_0.soundAgent:Dispose()

	arg_75_0.soundAgent = nil

	arg_75_0.bgAgent:Dispose()

	arg_75_0.bgAgent = nil

	arg_75_0.bgmAgent:Dispose()

	arg_75_0.bgmAgent = nil

	arg_75_0.descPage:Destroy()

	arg_75_0.descPage = nil

	arg_75_0.playTheLutePage:Destroy()

	arg_75_0.playTheLutePage = nil

	if not IsNil(arg_75_0._go) then
		Object.Destroy(arg_75_0._go)
	end
end

return var_0_0
