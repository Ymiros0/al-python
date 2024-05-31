local var_0_0 = class("NewYearHotSpringMediator", import("view.base.ContextMediator"))

var_0_0.UNLOCK_SLOT = "UNLOCK_SLOT"
var_0_0.OPEN_INFO = "OPEN_INFO"
var_0_0.OPEN_CHUANWU = "NewYearHotSpringMediator:Open chuanwu"

function var_0_0.register(arg_1_0)
	arg_1_0:bind(var_0_0.UNLOCK_SLOT, function(arg_2_0, arg_2_1)
		local var_2_0, var_2_1 = arg_1_0.activity:GetUpgradeCost()

		MsgboxMediator.ShowMsgBox({
			type = MSGBOX_TYPE_NORMAL,
			content = i18n("hotspring_expand", var_2_1),
			contextSprites = {
				{
					name = "wenquanbi",
					path = "props/wenquanbi"
				}
			},
			onYes = function()
				if arg_1_0.activity:GetCoins() < var_2_1 then
					pg.TipsMgr.GetInstance():ShowTips(i18n("hotspring_tip2"))

					return
				end

				arg_1_0:sendNotification(GAME.ACTIVITY_OPERATION, {
					activity_id = arg_2_1,
					cmd = SpringActivity.OPERATION_UNLOCK
				})
			end
		})
	end)
	arg_1_0:bind(var_0_0.OPEN_CHUANWU, function(arg_4_0, arg_4_1, arg_4_2)
		arg_1_0:OnSelShips(arg_4_1, arg_4_2)
	end)

	local var_1_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_HOTSPRING)

	arg_1_0.activity = var_1_0

	arg_1_0.viewComponent:SetActivity(var_1_0)
	arg_1_0:bind(var_0_0.OPEN_INFO, function()
		arg_1_0:addSubLayers(Context.New({
			mediator = NewYearHotSpringShipSelectMediator,
			viewComponent = NewYearHotSpringShipSelectLayer,
			data = {
				actId = var_1_0.id
			}
		}))
	end)
end

function var_0_0.OnSelShips(arg_6_0, arg_6_1, arg_6_2)
	local var_6_0 = arg_6_0:GetSelectedShipIds(arg_6_2)
	local var_6_1 = {
		callbackQuit = true,
		selectedMax = arg_6_0.activity:GetSlotCount(),
		quitTeam = arg_6_2 ~= nil,
		ignoredIds = pg.ShipFlagMgr.GetInstance():FilterShips({
			isActivityNpc = true
		}),
		selectedIds = Clone(var_6_0),
		preView = arg_6_0.viewComponent.__cname,
		hideTagFlags = ShipStatus.TAG_HIDE_BACKYARD,
		blockTagFlags = ShipStatus.TAG_BLOCK_BACKYARD,
		onShip = function(arg_7_0, arg_7_1, arg_7_2)
			return arg_6_0:OnShip(arg_7_0, arg_7_1, arg_7_2)
		end,
		onSelected = function(arg_8_0, arg_8_1)
			arg_6_0:OnSelected(arg_6_1, arg_8_0, arg_8_1)
		end,
		priorEquipUpShipIDList = _.filter(arg_6_0.activity:GetShipIds(), function(arg_9_0)
			return arg_9_0 > 0
		end),
		leftTopWithFrameInfo = i18n("backyard_longpress_ship_tip")
	}

	var_6_1.isLayer = true
	var_6_1.energyDisplay = true

	arg_6_0:addSubLayers(Context.New({
		viewComponent = DockyardScene,
		mediator = DockyardMediator,
		data = var_6_1
	}))
end

function var_0_0.GetSelectedShipIds(arg_10_0, arg_10_1)
	local var_10_0 = arg_10_1 and arg_10_1.id or -1
	local var_10_1 = {}

	for iter_10_0, iter_10_1 in ipairs(arg_10_0.activity:GetShipIds()) do
		local var_10_2 = iter_10_1 > 0 and getProxy(BayProxy):RawGetShipById(iter_10_1)

		if var_10_2 and var_10_2.id ~= var_10_0 then
			table.insert(var_10_1, var_10_2.id)
		end
	end

	return var_10_1
end

function var_0_0.OnShip(arg_11_0, arg_11_1, arg_11_2, arg_11_3)
	local var_11_0, var_11_1 = ShipStatus.ShipStatusCheck("inBackyard", arg_11_1, function(arg_12_0)
		arg_11_2()
	end)

	return var_11_0, var_11_1
end

function var_0_0.OnSelected(arg_13_0, arg_13_1, arg_13_2, arg_13_3)
	local var_13_0 = Clone(arg_13_0.activity:GetShipIds())

	_.each(_.range(arg_13_0.activity:GetSlotCount()), function(arg_14_0)
		var_13_0[arg_14_0] = var_13_0[arg_14_0] or 0
	end)

	if arg_13_2 == nil or #arg_13_2 == 0 then
		if var_13_0[arg_13_1] > 0 then
			arg_13_0:sendNotification(GAME.ACTIVITY_OPERATION, {
				activity_id = arg_13_0.activity.id,
				cmd = SpringActivity.OPERATION_SETSHIP,
				kvargs1 = {
					{
						value = 0,
						key = arg_13_1
					}
				}
			})
		end

		existCall(arg_13_3)

		return
	end

	local var_13_1 = _.filter(arg_13_2, function(arg_15_0)
		return not table.contains(var_13_0, arg_15_0)
	end)

	table.Foreach(var_13_0, function(arg_16_0, arg_16_1)
		if arg_16_1 == 0 or table.contains(arg_13_2, arg_16_1) then
			return
		end

		var_13_0[arg_16_0] = 0
	end)

	if #var_13_1 == 1 and var_13_0[arg_13_1] == 0 then
		var_13_0[arg_13_1] = var_13_1[1]
	else
		local var_13_2 = 0

		_.each(var_13_1, function(arg_17_0)
			while var_13_2 <= #var_13_0 do
				var_13_2 = var_13_2 + 1

				if var_13_0[var_13_2] == 0 then
					break
				end
			end

			var_13_0[var_13_2] = arg_17_0
		end)
	end

	local var_13_3 = {}
	local var_13_4 = arg_13_0.activity:GetShipIds()

	table.Foreach(var_13_0, function(arg_18_0, arg_18_1)
		if (var_13_4[arg_18_0] or 0) ~= arg_18_1 then
			table.insert(var_13_3, {
				key = arg_18_0,
				value = arg_18_1
			})
		end
	end)

	if #var_13_3 > 0 then
		arg_13_0:sendNotification(GAME.ACTIVITY_OPERATION, {
			activity_id = arg_13_0.activity.id,
			cmd = SpringActivity.OPERATION_SETSHIP,
			kvargs1 = var_13_3
		})
	end

	arg_13_3()
end

function var_0_0.listNotificationInterests(arg_19_0)
	return {
		PlayerProxy.UPDATED,
		ActivityProxy.ACTIVITY_UPDATED,
		ActivityProxy.ACTIVITY_SHOW_AWARDS,
		var_0_0.OPEN_CHUANWU,
		var_0_0.UNLOCK_SLOT
	}
end

function var_0_0.handleNotification(arg_20_0, arg_20_1)
	local var_20_0 = arg_20_1:getName()
	local var_20_1 = arg_20_1:getBody()

	if var_20_0 == nil then
		-- block empty
	elseif var_20_0 == ActivityProxy.ACTIVITY_SHOW_AWARDS then
		arg_20_0.viewComponent:emit(BaseUI.ON_ACHIEVE, var_20_1.awards, var_20_1.callback)
	elseif var_20_0 == ActivityProxy.ACTIVITY_UPDATED then
		if var_20_1:getConfig("type") == ActivityConst.ACTIVITY_TYPE_HOTSPRING then
			arg_20_0.activity = var_20_1

			arg_20_0.viewComponent:SetActivity(var_20_1)
			arg_20_0.viewComponent:UpdateView()
		end
	elseif var_20_0 == var_0_0.OPEN_CHUANWU then
		arg_20_0.viewComponent:emit(var_0_0.OPEN_CHUANWU, unpack(var_20_1))
	elseif var_20_0 == var_0_0.UNLOCK_SLOT then
		arg_20_0.viewComponent:emit(var_0_0.UNLOCK_SLOT, var_20_1)
	end
end

function var_0_0.remove(arg_21_0)
	return
end

return var_0_0
