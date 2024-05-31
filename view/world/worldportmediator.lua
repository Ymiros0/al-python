local var_0_0 = class("WorldPortMediator", import("..base.ContextMediator"))

var_0_0.OnOpenBay = "WorldPortMediator.OnOpenBay"
var_0_0.OnTaskGoto = "WorldPortMediator.OnTaskGoto"
var_0_0.OnAccepetTask = "WorldPortMediator.OnAccepetTask"
var_0_0.OnSubmitTask = "WorldPortMediator.OnSubmitTask"
var_0_0.OnReqPort = "WorldPortMediator.OnReqPort"
var_0_0.OnBuyGoods = "WorldPortMediator.OnBuyGoods"
var_0_0.OnBuyNShopGoods = "WorldPortMediator.OnBuyNShopGoods"

function var_0_0.register(arg_1_0)
	arg_1_0:bind(var_0_0.OnOpenBay, function()
		arg_1_0:sendNotification(GAME.GO_SCENE, SCENE.DOCKYARD, {
			selectedMax = 1,
			selectedMin = 0,
			mode = DockyardScene.MODE_WORLD,
			hideTagFlags = ShipStatus.TAG_HIDE_WORLD
		})
	end)
	arg_1_0:bind(var_0_0.OnTaskGoto, function(arg_3_0, arg_3_1)
		arg_1_0.viewComponent:closeView()
		arg_1_0:sendNotification(WorldMediator.OnTriggerTaskGo, {
			taskId = arg_3_1
		})
	end)
	arg_1_0:bind(var_0_0.OnAccepetTask, function(arg_4_0, arg_4_1, arg_4_2)
		arg_1_0:sendNotification(GAME.WORLD_TRIGGER_TASK, {
			taskId = arg_4_1.id,
			portId = arg_4_2
		})
	end)
	arg_1_0:bind(var_0_0.OnSubmitTask, function(arg_5_0, arg_5_1)
		arg_1_0:sendNotification(GAME.WORLD_SUMBMIT_TASK, {
			taskId = arg_5_1.id
		})
	end)
	arg_1_0:bind(var_0_0.OnReqPort, function(arg_6_0, arg_6_1)
		arg_1_0:sendNotification(GAME.WORLD_PORT_REQ, {
			mapId = arg_6_1
		})
	end)
	arg_1_0:bind(var_0_0.OnBuyGoods, function(arg_7_0, arg_7_1)
		arg_1_0:sendNotification(GAME.WORLD_PORT_SHOPPING, {
			goods = arg_7_1
		})
	end)
	arg_1_0:bind(var_0_0.OnBuyNShopGoods, function(arg_8_0, arg_8_1, arg_8_2)
		arg_1_0:sendNotification(GAME.WORLD_PORT_NEW_SHOPPING, {
			goods = arg_8_1,
			count = arg_8_2
		})
	end)
	arg_1_0.viewComponent:SetPlayer(getProxy(PlayerProxy):getRawData())

	local var_1_0 = nowWorld()

	arg_1_0.viewComponent:SetAtlas(var_1_0:GetAtlas())
	arg_1_0.viewComponent:SetPort(var_1_0:GetActiveMap():GetPort())
	arg_1_0:CheckTaskNotify(var_1_0:GetTaskProxy())
end

function var_0_0.initNotificationHandleDic(arg_9_0)
	arg_9_0.handleDic = {
		[PlayerProxy.UPDATED] = function(arg_10_0, arg_10_1)
			arg_10_0.viewComponent:SetPlayer(getProxy(PlayerProxy):getRawData())
		end,
		[GAME.WORLD_PORT_SHOPPING_DONE] = function(arg_11_0, arg_11_1)
			local var_11_0 = arg_11_1:getBody()

			arg_11_0.viewComponent:emit(BaseUI.ON_ACHIEVE, var_11_0.drops)
			arg_11_0.viewComponent:UpdateCDTip()
		end,
		[GAME.WORLD_PORT_NEW_SHOPPING_DONE] = function(arg_12_0, arg_12_1)
			local var_12_0 = arg_12_1:getBody()

			arg_12_0.viewComponent:emit(BaseUI.ON_ACHIEVE, var_12_0.drops)
		end
	}
end

function var_0_0.CheckTaskNotify(arg_13_0, arg_13_1)
	local var_13_0 = arg_13_1:getTasks()

	for iter_13_0, iter_13_1 in pairs(var_13_0) do
		if iter_13_1:getState() == WorldTask.STATE_ONGOING and iter_13_1.config.complete_condition == WorldConst.TaskTypeArrivePort then
			local var_13_1 = WBank:Fetch(WorldMapOp)

			var_13_1.op = WorldConst.OpReqTask

			arg_13_0:sendNotification(GAME.WORLD_MAP_OP, var_13_1)
		end
	end
end

return var_0_0
