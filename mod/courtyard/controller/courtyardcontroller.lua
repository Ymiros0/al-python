local var_0_0 = class("CourtYardController")

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	arg_1_0.bridge = arg_1_1
	arg_1_0.system = arg_1_2.system
	arg_1_0.storeyId = arg_1_2.storeyId
	arg_1_0.storeyDatas = arg_1_2.storeys
	arg_1_0.storey = arg_1_0:System2Storey(arg_1_2)
	arg_1_0.isInit = false
end

function var_0_0.GetBridge(arg_2_0)
	return arg_2_0.bridge
end

function var_0_0.IsLoaed(arg_3_0)
	return arg_3_0.isInit
end

function var_0_0.SetUp(arg_4_0)
	local var_4_0 = arg_4_0.storeyDatas[arg_4_0.storeyId]

	arg_4_0.storey:SetLevel(var_4_0.level)

	local var_4_1 = var_4_0.furnitures[1]

	if not var_4_1 or not var_0_0.IsFloorPaper(var_4_1) then
		arg_4_0.storey:SetFloorPaper(nil)
	end

	local var_4_2 = math.ceil(#var_4_0.furnitures / 3)
	local var_4_3 = {}

	for iter_4_0, iter_4_1 in ipairs(var_4_0.furnitures) do
		table.insert(var_4_3, function(arg_5_0)
			arg_4_0:AddFurniture({
				id = iter_4_1.id,
				configId = iter_4_1.configId,
				dir = iter_4_1.dir,
				parent = iter_4_1.parent,
				position = iter_4_1.position,
				date = iter_4_1.date
			}, true)

			if (iter_4_0 - 1) % var_4_2 == 0 then
				onNextTick(arg_5_0)
			else
				arg_5_0()
			end
		end)
	end

	for iter_4_2, iter_4_3 in ipairs(var_4_0.ships) do
		table.insert(var_4_3, function(arg_6_0)
			arg_4_0:AddShip(iter_4_3)
			onNextTick(arg_6_0)
		end)
	end

	seriesAsync(var_4_3, function()
		if arg_4_0.storey then
			arg_4_0.storey:DispatchEvent(CourtYardEvent.INITED)
		end

		arg_4_0.isInit = true

		arg_4_0:SendNotification(CourtYardEvent._INITED)
	end)
end

function var_0_0.Update(arg_8_0)
	if arg_8_0.storey then
		arg_8_0.storey:Update()
	end
end

function var_0_0.GetStorey(arg_9_0)
	return arg_9_0.storey
end

function var_0_0.AddFurniture(arg_10_0, arg_10_1, arg_10_2)
	if not arg_10_0.storey then
		return
	end

	local function var_10_0(arg_11_0, arg_11_1)
		local var_11_0 = arg_10_0:DataToFurnitureVO(arg_10_1)

		var_11_0:Init(arg_11_1, arg_10_1.dir or 1)

		return arg_10_0.storey:IsLegalAreaForFurniture(var_11_0, arg_11_1)
	end

	local var_10_1 = arg_10_0:DataToFurnitureVO(arg_10_1)

	var_10_1.selectedFlag = arg_10_1.selected

	if not arg_10_0.storey:CanAddFurniture(var_10_1) then
		return
	end

	local var_10_2 = var_10_1:GetType()

	if arg_10_1.parent and arg_10_1.parent ~= 0 then
		var_10_1:Init(arg_10_1.position, arg_10_1.dir or 1)
		arg_10_0.storey:AddChildFurniture(var_10_1, arg_10_1.parent)
	elseif var_10_2 == Furniture.TYPE_WALLPAPER or var_10_2 == Furniture.TYPE_FLOORPAPER then
		arg_10_0.storey:AddPaper(var_10_1)
	else
		local var_10_3 = arg_10_1.position or arg_10_0.storey:GetEmptyArea(var_10_1)

		if not var_10_3 then
			arg_10_0.storey:DispatchEvent(CourtYardEvent.ADD_ITEM_FAILED)
		elseif var_10_3 and var_10_0(var_10_1, var_10_3) then
			var_10_1:Init(var_10_3, arg_10_1.dir or 1)
			arg_10_0.storey:AddFurniture(var_10_1, arg_10_2)
		else
			arg_10_0:SendNotification(CourtYardEvent._ADD_ITEM_FAILED, var_10_1.id)
		end
	end

	arg_10_0:CheckChange()
end

function var_0_0.AddShip(arg_12_0, arg_12_1)
	if not arg_12_0.storey then
		return
	end

	local var_12_0 = arg_12_0:DataToShip(arg_12_1)
	local var_12_1 = arg_12_0.storey:GetRandomPosition(var_12_0)

	if var_12_1 then
		var_12_0:SetPosition(var_12_1)
		arg_12_0.storey:AddShip(var_12_0)
	else
		arg_12_0:SendNotification(CourtYardEvent._NO_POS_TO_ADD_SHIP, var_12_0.id)
	end
end

function var_0_0.AddVisitorShip(arg_13_0, arg_13_1)
	if not arg_13_0.storey then
		return
	end

	local var_13_0 = arg_13_0:DataToVisitorShip(arg_13_1)
	local var_13_1 = arg_13_0.storey:GetRandomPosition(var_13_0)

	if var_13_1 then
		var_13_0:SetPosition(var_13_1)
		arg_13_0.storey:AddShip(var_13_0)
	end
end

function var_0_0.ExitShip(arg_14_0, arg_14_1)
	arg_14_0.storey:ExitShip(arg_14_1)
end

function var_0_0.Extend(arg_15_0)
	arg_15_0:SendNotification(CourtYardEvent._EXTEND)
end

function var_0_0.LevelUp(arg_16_0)
	arg_16_0.storey:LevelUp(id)
end

function var_0_0.DragShip(arg_17_0, arg_17_1)
	arg_17_0.storey:DragShip(arg_17_1)
	arg_17_0:SendNotification(CourtYardEvent._DRAG_ITEM)
end

function var_0_0.DragingShip(arg_18_0, arg_18_1, arg_18_2)
	arg_18_0.storey:DragingShip(arg_18_1, arg_18_2)
end

function var_0_0.DragShipEnd(arg_19_0, arg_19_1, arg_19_2)
	arg_19_0.storey:DragShipEnd(arg_19_1, arg_19_2)
	arg_19_0:SendNotification(CourtYardEvent._DRAG_ITEM_END)
end

function var_0_0.TouchShip(arg_20_0, arg_20_1)
	arg_20_0.storey:TouchShip(arg_20_1)
	arg_20_0:SendNotification(CourtYardEvent._TOUCH_SHIP, arg_20_1)
end

function var_0_0.GetShipInimacy(arg_21_0, arg_21_1)
	arg_21_0:SendNotification(GAME.BACKYARD_ADD_INTIMACY, arg_21_1)
end

function var_0_0.GetShipCoin(arg_22_0, arg_22_1)
	arg_22_0:SendNotification(GAME.BACKYARD_ADD_MONEY, arg_22_1)
end

function var_0_0.ClearShipCoin(arg_23_0, arg_23_1)
	arg_23_0.storey:ClearShipCoin(arg_23_1)
end

function var_0_0.ClearShipIntimacy(arg_24_0, arg_24_1)
	arg_24_0.storey:ClearShipIntimacy(arg_24_1)
end

function var_0_0.UpdateShipCoinAndIntimacy(arg_25_0, arg_25_1, arg_25_2, arg_25_3)
	arg_25_0.storey:UpdateShipCoin(arg_25_1, arg_25_2)
	arg_25_0.storey:UpdateShipIntimacy(arg_25_1, arg_25_3)
end

function var_0_0.AddShipExp(arg_26_0, arg_26_1, arg_26_2)
	arg_26_0.storey:AddShipExp(arg_26_1, arg_26_2)
end

function var_0_0.ShipAnimtionFinish(arg_27_0, arg_27_1, arg_27_2)
	arg_27_0.storey:ShipAnimtionFinish(arg_27_1, arg_27_2)
end

function var_0_0.GetMaxCntForShip(arg_28_0)
	return #arg_28_0.storey:GetEmptyPositions(CourtYardShip.New(arg_28_0, Ship.New({
		id = 999,
		configId = 100001
	}))) + table.getCount(arg_28_0.storey:GetShips())
end

function var_0_0.SelectFurnitureByConfigId(arg_29_0, arg_29_1)
	if arg_29_0.storey.wallPaper and arg_29_0.storey.wallPaper.configId == arg_29_1 then
		return
	end

	if arg_29_0.storey.floorPaper and arg_29_0.storey.floorPaper.configId == arg_29_1 then
		return
	end

	local var_29_0

	for iter_29_0, iter_29_1 in pairs(arg_29_0.storey.furnitures) do
		if iter_29_1.configId == arg_29_1 then
			var_29_0 = iter_29_1

			break
		end
	end

	if var_29_0 then
		arg_29_0:SelectFurniture(var_29_0.id)
	else
		pg.TipsMgr.GetInstance():ShowTips(i18n("courtyard_tip_furniture_not_in_layer"))
	end
end

function var_0_0.SelectFurniture(arg_30_0, arg_30_1)
	if arg_30_0.storey:InEidtMode() then
		arg_30_0.storey:SelectFurniture(arg_30_1)

		local var_30_0 = arg_30_0.storey:GetFurniture(arg_30_1)

		if var_30_0:GetOpFlag() then
			arg_30_0:SendNotification(CourtYardEvent._FURNITURE_SELECTED, var_30_0.configId)
		end
	else
		arg_30_0.storey:ClickFurniture(arg_30_1)
	end
end

function var_0_0.PlayFurnitureVoice(arg_31_0, arg_31_1)
	arg_31_0.storey:PlayFurnitureVoice(arg_31_1)
end

function var_0_0.PlayMusicalInstruments(arg_32_0, arg_32_1)
	arg_32_0.storey:PlayMusicalInstruments(arg_32_1)
end

function var_0_0.StopPlayMusicalInstruments(arg_33_0, arg_33_1)
	arg_33_0.storey:StopPlayMusicalInstruments(arg_33_1)
end

function var_0_0.PlayFurnitureBg(arg_34_0, arg_34_1)
	arg_34_0.storey:PlayFurnitureBg(arg_34_1)
end

function var_0_0.UnSelectFurniture(arg_35_0, arg_35_1)
	arg_35_0.storey:UnSelectFurniture(arg_35_1)

	if not arg_35_0.storey:GetFurniture(arg_35_1):GetOpFlag() then
		arg_35_0:SendNotification(CourtYardEvent._FURNITURE_SELECTED, -99999)
	end
end

function var_0_0.BeginDragFurniture(arg_36_0, arg_36_1)
	arg_36_0.storey:BeginDragFurniture(arg_36_1)
	arg_36_0:SendNotification(CourtYardEvent._DRAG_ITEM)
end

function var_0_0.DragingFurniture(arg_37_0, arg_37_1, arg_37_2)
	arg_37_0.storey:DragingFurniture(arg_37_1, arg_37_2)
end

function var_0_0.DragFurnitureEnd(arg_38_0, arg_38_1, arg_38_2)
	arg_38_0.storey:DragFurnitureEnd(arg_38_1, arg_38_2)
	arg_38_0:CheckChange()
	arg_38_0:SendNotification(CourtYardEvent._DRAG_ITEM_END)
end

function var_0_0.FurnitureAnimtionFinish(arg_39_0, arg_39_1, arg_39_2)
	arg_39_0.storey:FurnitureAnimtionFinish(arg_39_1, arg_39_2)
end

function var_0_0.RotateFurniture(arg_40_0, arg_40_1)
	arg_40_0.storey:RotateFurniture(arg_40_1)
	arg_40_0:CheckChange()
end

function var_0_0.RemoveFurniture(arg_41_0, arg_41_1)
	arg_41_0.storey:RemoveFurniture(arg_41_1)
	arg_41_0:CheckChange()
end

function var_0_0.RemovePaper(arg_42_0, arg_42_1)
	arg_42_0.storey:RemovePaper(arg_42_1)
	arg_42_0:CheckChange()
end

function var_0_0.ClearFurnitures(arg_43_0)
	arg_43_0.storey:RemoveAllFurniture()
	arg_43_0:CheckChange()
end

function var_0_0.SaveFurnitures(arg_44_0)
	if arg_44_0.storey.recoder:HasChange() then
		local var_44_0 = arg_44_0.storey:ToTable()

		arg_44_0:SendNotification(GAME.PUT_FURNITURE, {
			tip = true,
			furnsPos = var_44_0
		})
	end

	arg_44_0:ExitEditMode()
end

function var_0_0.GetStoreyData(arg_45_0)
	return (arg_45_0.storey:ToTable())
end

function var_0_0.RestoreFurnitures(arg_46_0)
	arg_46_0:ClearFurnitures()

	local var_46_0 = arg_46_0.storey.recoder:GetHeadSample()

	for iter_46_0, iter_46_1 in ipairs(var_46_0) do
		arg_46_0:AddFurniture(iter_46_1)
	end

	arg_46_0:ExitEditMode()
end

function var_0_0.EnterEditMode(arg_47_0)
	arg_47_0.storey:EnterEditMode()
	arg_47_0:SendNotification(CourtYardEvent._ENTER_MODE)
end

function var_0_0.ExitEditMode(arg_48_0)
	arg_48_0.storey:ExitEditMode()
	arg_48_0:SendNotification(CourtYardEvent._EXIT_MODE)
end

function var_0_0.CheckChange(arg_49_0)
	local var_49_0, var_49_1 = arg_49_0.storey:GetDirty()

	if var_49_0 and var_49_1 then
		arg_49_0:SendNotification(CourtYardEvent._SYN_FURNITURE, {
			var_49_0,
			var_49_1
		})
	end
end

function var_0_0.Quit(arg_50_0)
	if arg_50_0.storey:InEidtMode() then
		if arg_50_0.storey.recoder:HasChange() then
			arg_50_0.storey:DispatchEvent(CourtYardEvent.REMIND_SAVE)
		else
			arg_50_0:ExitEditMode()
		end
	else
		arg_50_0:SendNotification(CourtYardEvent._QUIT)
	end
end

function var_0_0.IsVisit(arg_51_0)
	return arg_51_0.system == CourtYardConst.SYSTEM_VISIT
end

function var_0_0.IsFeast(arg_52_0)
	return arg_52_0.system == CourtYardConst.SYSTEM_FEAST
end

function var_0_0.IsEditModeOrIsVisit(arg_53_0)
	return arg_53_0:IsVisit() or arg_53_0.storey:InEidtMode()
end

function var_0_0.Receive(arg_54_0, arg_54_1, ...)
	if not arg_54_0.storey then
		return
	end

	arg_54_0[arg_54_1](arg_54_0, ...)
end

function var_0_0.OnTakeThemePhoto(arg_55_0)
	if arg_55_0.storey then
		arg_55_0.storey:DispatchEvent(CourtYardEvent.TAKE_PHOTO)
	end
end

function var_0_0.OnEndTakeThemePhoto(arg_56_0)
	if arg_56_0.storey then
		arg_56_0.storey:DispatchEvent(CourtYardEvent.END_TAKE_PHOTO)
	end
end

function var_0_0.OnApplicationPaused(arg_57_0)
	if arg_57_0.storey then
		arg_57_0.storey:StopAllDragState()
		arg_57_0:SendNotification(CourtYardEvent._DRAG_ITEM_END)
	end
end

function var_0_0.OnOpenLayerOrCloseLayer(arg_58_0, arg_58_1, arg_58_2)
	if not arg_58_2 or not arg_58_0.storey then
		return
	end

	arg_58_0.storey:DispatchEvent(CourtYardEvent.OPEN_LAYER, arg_58_1)
end

function var_0_0.OnBackPressed(arg_59_0)
	if arg_59_0.storey then
		arg_59_0.storey:DispatchEvent(CourtYardEvent.BACK_PRESSED)
	end
end

function var_0_0.Dispose(arg_60_0)
	if arg_60_0.storey then
		arg_60_0.storey:Dispose()

		arg_60_0.storey = nil
	end
end

function var_0_0.IsFloorPaper(arg_61_0)
	return pg.furniture_data_template[arg_61_0.configId].type == Furniture.TYPE_FLOORPAPER
end

function var_0_0.DataToFurnitureVO(arg_62_0, arg_62_1)
	local var_62_0 = pg.furniture_data_template[arg_62_1.configId]

	if var_62_0.type == Furniture.TYPE_WALLPAPER or var_62_0.type == Furniture.TYPE_FLOORPAPER then
		return CourtYardPaper.New(arg_62_0, arg_62_1)
	elseif var_62_0.type == Furniture.TYPE_FOLLOWER then
		return CourtYardFollowerFurniture.New(arg_62_0, arg_62_1)
	elseif var_62_0.type == Furniture.TYPE_RANDOM_CONTROLLER then
		return CourtYardRandomControllerFurniture.New(arg_62_0, arg_62_1)
	elseif var_62_0.type == Furniture.TYPE_MAT then
		return CourtYardMatFurniture.New(arg_62_0, arg_62_1)
	elseif var_62_0.type == Furniture.TYPE_TRANSPORT then
		return CourtYardTransportFurniture.New(arg_62_0, arg_62_1)
	elseif var_62_0.type == Furniture.TYPE_WALL_MAT then
		return CourtYardWallMatFurniture.New(arg_62_0, arg_62_1)
	elseif var_62_0.type == Furniture.TYPE_STAGE or var_62_0.type == Furniture.TYPE_ARCH then
		return CourtYardStageFurniture.New(arg_62_0, arg_62_1)
	elseif var_62_0.type == Furniture.TYPE_MOVEABLE then
		return CourtYardMoveableFurniture.New(arg_62_0, arg_62_1)
	elseif var_62_0.belong == 1 and var_62_0.canputon == 1 then
		return CourtYardCanPutFurniture.New(arg_62_0, arg_62_1)
	elseif var_62_0.belong > 1 then
		return CourtYardWallFurniture.New(arg_62_0, arg_62_1)
	else
		return CourtYardFurniture.New(arg_62_0, arg_62_1)
	end
end

function var_0_0.DataToShip(arg_63_0, arg_63_1)
	if arg_63_0.system == CourtYardConst.SYSTEM_FEAST then
		return CourtYardFeastShip.New(arg_63_0, arg_63_1)
	else
		return CourtYardShip.New(arg_63_0, arg_63_1)
	end
end

function var_0_0.DataToVisitorShip(arg_64_0, arg_64_1)
	return CourtYardVisitorShip.New(arg_64_0, arg_64_1)
end

function var_0_0.System2Storey(arg_65_0, arg_65_1)
	local var_65_0 = Vector4(arg_65_1.mapSize.z + 1, arg_65_1.mapSize.w + 1, arg_65_1.mapSize.x, arg_65_1.mapSize.y)

	if arg_65_1.system == CourtYardConst.SYSTEM_OUTSIDE then
		return CourtYardOutStorey.New(arg_65_0, arg_65_1.storeyId, arg_65_1.style, var_65_0)
	else
		return CourtYardStorey.New(arg_65_0, arg_65_1.storeyId, arg_65_1.style, var_65_0)
	end
end

function var_0_0.SendNotification(arg_66_0, ...)
	if arg_66_0.bridge then
		arg_66_0.bridge:SendNotification(...)
	end
end

return var_0_0
