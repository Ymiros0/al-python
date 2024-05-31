local var_0_0 = class("BackYardDecorationMediator", import("...base.ContextMediator"))

var_0_0.ADD_FURNITURE = "BackYardDecorationMediator:ADD_FURNITURE"
var_0_0.REMOVE_PAPER = "BackYardDecorationMediator:REMOVE_PAPER"
var_0_0.SAVE_ALL = "BackYardDecorationMediator:SAVE_ALL"
var_0_0.ClEAR_ALL = "BackYardDecorationMediator:ClEAR_ALL"
var_0_0.OPEN_SHOP = "BackYardDecorationMediator:OPEN_SHOP"
var_0_0.GET_CUSTOM_THEME = "BackYardDecorationMediator:GET_CUSTOM_THEME"
var_0_0.DELETE_THEME = "BackYardDecorationMediator:DELETE_THEME"
var_0_0.SAVE_THEME = "BackYardDecorationMediator:SAVE_THEME"
var_0_0.APPLY_THEME = "BackYardDecorationMediator:APPLY_THEME"
var_0_0.ADD_FURNITURES = "BackYardDecorationMediator:ADD_FURNITURES"
var_0_0.ON_SELECTED_FURNITRUE = "BackYardDecorationMediator:ON_SELECTED_FURNITRUE"
var_0_0.GET_CURR_FURNITURE = "BackYardDecorationMediator:GET_CURR_FURNITURE"
var_0_0.GET_OTHER_FURNITURE = "BackYardDecorationMediator:GET_OTHER_FURNITURE"
var_0_0.GET_ALL_FURNITURE = "BackYardDecorationMediator:GET_ALL_FURNITURE"
var_0_0.START_TAKE_THEME_PHOTO = "BackYardDecorationMediator:START_TAKE_THEME_PHOTO"
var_0_0.END_TAKE_THEME_PHOTO = "BackYardDecorationMediator:END_TAKE_THEME_PHOTO"
var_0_0.ON_SET_UP = "BackYardDecorationMediator:ON_SET_UP"

function var_0_0.register(arg_1_0)
	arg_1_0:bind(var_0_0.ON_SELECTED_FURNITRUE, function(arg_2_0, arg_2_1)
		_courtyard:GetController():SelectFurnitureByConfigId(arg_2_1)
	end)
	arg_1_0:bind(var_0_0.APPLY_THEME, function(arg_3_0, arg_3_1, arg_3_2)
		local var_3_0, var_3_1 = arg_1_0:GetCanPutFurnitureForTheme(arg_1_0.dorm, arg_3_1)

		if arg_3_2 then
			arg_3_2(var_3_1, var_3_0)
		end
	end)
	arg_1_0:bind(var_0_0.SAVE_THEME, function(arg_4_0, arg_4_1, arg_4_2)
		if not arg_1_0:AnyFurnitureInFloor(arg_1_0.dorm, getProxy(DormProxy).floor) then
			pg.TipsMgr.GetInstance():ShowTips(i18n("backyard_save_empty_theme"))

			return
		end

		pg.UIMgr.GetInstance():LoadingOn()

		local var_4_0 = BackYardBaseThemeTemplate.BuildId(arg_4_1)
		local var_4_1
		local var_4_2
		local var_4_3 = pg.UIMgr.GetInstance().uiCamera:GetComponent(typeof(Camera))

		seriesAsync({
			function(arg_5_0)
				arg_1_0:sendNotification(var_0_0.START_TAKE_THEME_PHOTO)

				var_4_1 = BackYardThemeTempalteUtil.TakePhoto(var_4_3)
				var_4_2 = BackYardThemeTempalteUtil.TakeIcon(var_4_3)

				arg_1_0:sendNotification(var_0_0.END_TAKE_THEME_PHOTO)
				arg_5_0()
			end,
			function(arg_6_0)
				onNextTick(arg_6_0)
			end,
			function(arg_7_0)
				if not var_4_1 or not var_4_2 then
					return
				end

				BackYardThemeTempalteUtil.SavePhoto(var_4_0, var_4_1, var_4_2, arg_7_0)
			end,
			function(arg_8_0)
				onNextTick(arg_8_0)
			end,
			function(arg_9_0)
				local var_9_0 = BackYardThemeTempalteUtil.GetMd5(var_4_0)
				local var_9_1 = BackYardThemeTempalteUtil.GetIconMd5(var_4_0)
				local var_9_2 = _courtyard:GetController():GetStoreyData()

				pg.UIMgr.GetInstance():LoadingOff()
				arg_1_0:sendNotification(GAME.BACKYARD_SAVE_THEME_TEMPLATE, {
					id = arg_4_1,
					name = arg_4_2,
					furnitureputList = var_9_2,
					iconMd5 = var_9_1,
					imageMd5 = var_9_0
				})
				arg_9_0()
			end
		})
	end)
	arg_1_0:bind(var_0_0.DELETE_THEME, function(arg_10_0, arg_10_1)
		arg_1_0:sendNotification(GAME.BACKYARD_DELETE_THEME_TEMPLATE, {
			templateId = arg_10_1
		})
	end)
	arg_1_0:bind(var_0_0.GET_CUSTOM_THEME, function(arg_11_0, arg_11_1)
		arg_1_0:sendNotification(GAME.BACKYARD_GET_THEME_TEMPLATE, {
			type = BackYardConst.THEME_TEMPLATE_TYPE_CUSTOM,
			callback = arg_11_1
		})
	end)
	arg_1_0:bind(var_0_0.OPEN_SHOP, function(arg_12_0)
		_courtyard:GetController():SaveFurnitures()
		arg_1_0.viewComponent:emit(BaseUI.ON_CLOSE)
		arg_1_0:sendNotification(GAME.OPEN_BACKYARD_SHOP)
	end)
	arg_1_0:bind(var_0_0.SAVE_ALL, function(arg_13_0)
		_courtyard:GetController():SaveFurnitures()
	end)
	arg_1_0:bind(var_0_0.ClEAR_ALL, function(arg_14_0, arg_14_1)
		arg_1_0:sendNotification(GAME.ON_APPLY_SELF_THEME)
		_courtyard:GetController():ClearFurnitures()
	end)
	arg_1_0:bind(var_0_0.ADD_FURNITURE, function(arg_15_0, arg_15_1, arg_15_2)
		local var_15_0 = arg_1_0:GenUniqueID(arg_1_0.dorm, arg_15_1.configId)

		_courtyard:GetController():AddFurniture({
			selected = true,
			id = var_15_0,
			configId = arg_15_1.configId,
			date = arg_15_1.date
		})
		getProxy(DormProxy):_ClearNewFlag(arg_15_1.configId)

		local var_15_1 = arg_1_0.dorm:GetFurniture(arg_15_1.configId)

		var_15_1:ClearNewFlag()
		arg_1_0.viewComponent:UpdateFurnitrue(var_15_1)

		if arg_15_2 then
			arg_15_2()
		end
	end)
	arg_1_0:bind(var_0_0.ADD_FURNITURES, function(arg_16_0, arg_16_1, arg_16_2, arg_16_3)
		local var_16_0 = {}

		table.insert(var_16_0, function(arg_17_0)
			arg_1_0.viewComponent:emit(var_0_0.ClEAR_ALL)
			onNextTick(arg_17_0)
		end)

		local function var_16_1(arg_18_0)
			_courtyard:GetController():AddFurniture({
				id = arg_18_0.id,
				configId = arg_18_0.configId,
				parent = arg_18_0.parent,
				position = arg_18_0.position,
				dir = arg_18_0.dir,
				date = arg_18_0.date
			})
		end

		local var_16_2 = math.ceil(#arg_16_2 / 3)

		for iter_16_0, iter_16_1 in pairs(arg_16_2) do
			assert(iter_16_1.position)
			table.insert(var_16_0, function(arg_19_0)
				var_16_1(iter_16_1)

				if (iter_16_0 - 1) % var_16_2 == 0 then
					onNextTick(arg_19_0)
				else
					arg_19_0()
				end
			end)
		end

		pg.UIMgr.GetInstance():LoadingOn()
		seriesAsync(var_16_0, function()
			if arg_16_3 then
				arg_16_3(arg_16_2)
			end

			arg_1_0:sendNotification(GAME.ON_APPLY_SELF_THEME_DONE, {
				id = arg_16_1
			})
			pg.UIMgr.GetInstance():LoadingOff()
		end)
	end)
	arg_1_0:bind(var_0_0.REMOVE_PAPER, function(arg_21_0, arg_21_1)
		_courtyard:GetController():RemovePaper(arg_21_1.id)
	end)
	arg_1_0:bind(var_0_0.ON_SET_UP, function(arg_22_0)
		arg_1_0:SetUp()
	end)
end

function var_0_0.AnyFurnitureInFloor(arg_23_0, arg_23_1, arg_23_2)
	local var_23_0 = arg_23_1:GetThemeList()[arg_23_2]

	if not var_23_0 then
		return false
	end

	local var_23_1 = var_23_0:GetAllFurniture()

	return table.getCount(var_23_1) > 0
end

function var_0_0.GetCanPutFurnitureForTheme(arg_24_0, arg_24_1, arg_24_2)
	local var_24_0 = getProxy(DormProxy).floor
	local var_24_1 = arg_24_0:GetAllFloorFurnitures(arg_24_1)
	local var_24_2 = arg_24_2:IsOccupyed(var_24_1, var_24_0)
	local var_24_3 = {}
	local var_24_4 = false

	if var_24_2 then
		var_24_3 = arg_24_2:GetUsableFurnituresForFloor(var_24_1, var_24_0)
		var_24_4 = false
	else
		local var_24_5 = arg_24_2:GetAllFurniture()

		for iter_24_0, iter_24_1 in pairs(var_24_5) do
			table.insert(var_24_3, iter_24_1)
		end

		var_24_4 = true
	end

	local var_24_6 = arg_24_0:FilterOwnCount(var_24_3)

	table.sort(var_24_6, BackyardThemeFurniture._LoadWeight)

	return var_24_6, var_24_4
end

function var_0_0.FilterOwnCount(arg_25_0, arg_25_1)
	local var_25_0 = {}
	local var_25_1 = {}
	local var_25_2 = {}
	local var_25_3 = getProxy(DormProxy):getRawData()

	for iter_25_0, iter_25_1 in ipairs(arg_25_1) do
		var_25_1[iter_25_1.configId] = (var_25_1[iter_25_1.configId] or 0) + 1

		if var_25_3:GetOwnFurnitureCount(iter_25_1.configId) >= var_25_1[iter_25_1.configId] then
			table.insert(var_25_0, iter_25_1)
		else
			table.insert(var_25_2, iter_25_1.id)
		end
	end

	for iter_25_2, iter_25_3 in ipairs(var_25_2) do
		for iter_25_4, iter_25_5 in ipairs(var_25_0) do
			if iter_25_5.parent == iter_25_3 then
				iter_25_5.parent = 0
			end
		end
	end

	return var_25_0
end

function var_0_0.GetAllFloorFurnitures(arg_26_0, arg_26_1)
	local var_26_0 = {}

	for iter_26_0, iter_26_1 in pairs(arg_26_1:GetThemeList()) do
		for iter_26_2, iter_26_3 in pairs(iter_26_1:GetAllFurniture()) do
			var_26_0[iter_26_2] = iter_26_3
		end
	end

	return var_26_0
end

function var_0_0.GenUniqueID(arg_27_0, arg_27_1, arg_27_2)
	local var_27_0 = arg_27_0:GetAllFloorFurnitures(arg_27_1)
	local var_27_1 = arg_27_1:GetOwnFurnitureCount(arg_27_2)

	for iter_27_0 = 0, var_27_1 - 1 do
		local var_27_2 = BackyardThemeFurniture.GetUniqueId(arg_27_2, iter_27_0)

		if not var_27_0[var_27_2] then
			return var_27_2
		end
	end

	return BackyardThemeFurniture.GetUniqueId(arg_27_2, 0)
end

function var_0_0.SetUp(arg_28_0)
	seriesAsync({
		function(arg_29_0)
			local var_29_0 = getProxy(DormProxy)

			arg_28_0.dorm = var_29_0:getData()

			arg_28_0.viewComponent:SetDorm(arg_28_0.dorm)
			arg_28_0.viewComponent:SetThemes(var_29_0:GetCustomThemeTemplates())
			onNextTick(arg_29_0)
		end,
		function(arg_30_0)
			if arg_28_0.viewComponent.themes then
				arg_30_0()

				return
			end

			arg_28_0.viewComponent:emit(BackYardDecorationMediator.GET_CUSTOM_THEME, arg_30_0)
		end
	}, function()
		arg_28_0.viewComponent:InitPages()
	end)
end

function var_0_0.listNotificationInterests(arg_32_0)
	return {
		CourtYardEvent._SYN_FURNITURE,
		CourtYardEvent._EXIT_MODE,
		CourtYardEvent._FURNITURE_SELECTED,
		DormProxy.THEME_TEMPLATE_ADDED,
		DormProxy.THEME_TEMPLATE_DELTETED,
		GAME.BACKYARD_GET_THEME_TEMPLATE_DONE,
		GAME.ON_APPLY_SELF_THEME,
		GAME.ON_APPLY_SELF_THEME_DONE,
		CourtYardEvent._DRAG_ITEM,
		CourtYardEvent._DRAG_ITEM_END,
		var_0_0.START_TAKE_THEME_PHOTO,
		var_0_0.END_TAKE_THEME_PHOTO
	}
end

function var_0_0.handleNotification(arg_33_0, arg_33_1)
	local var_33_0 = arg_33_1:getName()
	local var_33_1 = arg_33_1:getBody()

	if var_33_0 == CourtYardEvent._SYN_FURNITURE then
		local var_33_2 = var_33_1[1]
		local var_33_3 = var_33_1[2]
		local var_33_4 = getProxy(DormProxy).floor
		local var_33_5 = arg_33_0.dorm:GetTheme(var_33_4)

		for iter_33_0, iter_33_1 in ipairs(var_33_2) do
			local var_33_6 = var_33_5:GetFurniture(iter_33_1.id)

			if var_33_6 then
				var_33_6:UpdatePosition(iter_33_1.position)
				var_33_6:UpdateDir(iter_33_1.dir)
				var_33_6:UpdateParent(iter_33_1.parent)
				var_33_6:UpdateChildList(iter_33_1.child)
				var_33_6:UpdateFloor(var_33_4)
			else
				local var_33_7 = var_33_5:AddFurniture(iter_33_1, var_33_4)
			end

			arg_33_0.viewComponent:UpdateDorm(arg_33_0.dorm)
			arg_33_0.viewComponent:UpdateFurnitrue(arg_33_0.dorm:GetFurniture(iter_33_1.configId))
		end

		for iter_33_2, iter_33_3 in ipairs(var_33_3) do
			local var_33_8 = var_33_5:GetFurniture(iter_33_3)

			var_33_5:DeleteFurniture(iter_33_3)

			if var_33_8 then
				arg_33_0.viewComponent:UpdateDorm(arg_33_0.dorm)
				arg_33_0.viewComponent:UpdateFurnitrue(arg_33_0.dorm:GetFurniture(var_33_8.configId))
			end
		end
	elseif var_33_0 == DormProxy.THEME_TEMPLATE_ADDED then
		arg_33_0.viewComponent:CustomThemeAdded(var_33_1.template)
	elseif var_33_0 == DormProxy.THEME_TEMPLATE_DELTETED then
		arg_33_0.viewComponent:CustomThemeDeleted(var_33_1.templateId)
	elseif var_33_0 == GAME.BACKYARD_GET_THEME_TEMPLATE_DONE then
		local var_33_9 = getProxy(DormProxy)

		arg_33_0.viewComponent:SetThemes(var_33_9:GetCustomThemeTemplates())
	elseif var_33_0 == GAME.ON_APPLY_SELF_THEME then
		arg_33_0.viewComponent:OnApplyThemeBefore()
	elseif var_33_0 == GAME.ON_APPLY_SELF_THEME_DONE then
		arg_33_0.viewComponent:OnApplyThemeAfter(var_33_1.id)
	elseif var_33_0 == CourtYardEvent._EXIT_MODE then
		arg_33_0.viewComponent:emit(BaseUI.ON_CLOSE)
	elseif var_33_0 == CourtYardEvent._DRAG_ITEM then
		GetOrAddComponent(arg_33_0.viewComponent._tf, typeof(CanvasGroup)).blocksRaycasts = false
	elseif var_33_0 == CourtYardEvent._DRAG_ITEM_END then
		GetOrAddComponent(arg_33_0.viewComponent._tf, typeof(CanvasGroup)).blocksRaycasts = true
	elseif var_33_0 == var_0_0.START_TAKE_THEME_PHOTO then
		GetOrAddComponent(arg_33_0.viewComponent._tf, typeof(CanvasGroup)).alpha = 0
	elseif var_33_0 == var_0_0.END_TAKE_THEME_PHOTO then
		GetOrAddComponent(arg_33_0.viewComponent._tf, typeof(CanvasGroup)).alpha = 1
	elseif var_33_0 == CourtYardEvent._FURNITURE_SELECTED then
		arg_33_0.viewComponent:emit(BackYardDecrationLayer.INNER_SELECTED_FURNITRUE, var_33_1)
	end
end

return var_0_0
