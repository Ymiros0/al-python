local var_0_0 = class("Dorm3dSceneMediator", import("view.base.ContextMediator"))

var_0_0.TRIGGER_FAVOR = "Dorm3dSceneMediator.TRIGGER_FAVOR"
var_0_0.FAVOR_LEVEL_UP = "Dorm3dSceneMediator.FAVOR_LEVEL_UP"
var_0_0.TALKING_EVENT_FINISH = "Dorm3dSceneMediator.TALKING_EVENT_FINISH"
var_0_0.DO_TALK = "Dorm3dSceneMediator.DO_TALK"
var_0_0.COLLECTION_ITEM = "Dorm3dSceneMediator.COLLECTION_ITEM"
var_0_0.OPEN_FURNITURE_SELECT = "Dorm3dSceneMediator.OPEN_FURNITURE_SELECT"
var_0_0.OPEN_LEVEL_LAYER = "Dorm3dSceneMediator.OPEN_LEVEL_LAYER"
var_0_0.OPEN_GIFT_LAYER = "Dorm3dSceneMediator.OPEN_GIFT_LAYER"
var_0_0.OPEN_CAMERA_LAYER = "Dorm3dSceneMediator.OPEN_CAMERA_LAYER"
var_0_0.OPEN_DROP_LAYER = "Dorm3dSceneMediator.OPEN_DROP_LAYER"
var_0_0.OPEN_COLLECTION_LAYER = "Dorm3dSceneMediator.OPEN_COLLECTION_LAYER"
var_0_0.ON_CLICK_FURNITURE_SLOT = "Dorm3dSceneMediator.ON_CLICK_FURNITURE_SLOT"
var_0_0.OTHER_DO_TALK = "Dorm3dSceneMediator.OTHER_DO_TALK"
var_0_0.OTHER_CHECK_LEVEL_UP = "Dorm3dSceneMediator.OTHER_CHECK_LEVEL_UP"
var_0_0.CHAMGE_TIME_RELOAD_SCENE = "Dorm3dSceneMediator.CHAMGE_TIME_RELOAD_SCENE"

function var_0_0.register(arg_1_0)
	arg_1_0:bind(var_0_0.TRIGGER_FAVOR, function(arg_2_0, arg_2_1, arg_2_2)
		arg_1_0:sendNotification(GAME.APARTMENT_TRIGGER_FAVOR, {
			groupId = arg_2_1,
			triggerId = arg_2_2
		})
	end)
	arg_1_0:bind(var_0_0.FAVOR_LEVEL_UP, function(arg_3_0, arg_3_1)
		arg_1_0:sendNotification(GAME.APARTMENT_LEVEL_UP, {
			groupId = arg_3_1
		})
	end)
	arg_1_0:bind(var_0_0.TALKING_EVENT_FINISH, function(arg_4_0, arg_4_1, arg_4_2)
		arg_1_0:sendNotification(arg_4_1, arg_4_2)
	end)
	arg_1_0:bind(var_0_0.OPEN_FURNITURE_SELECT, function(arg_5_0)
		arg_1_0:addSubLayers(Context.New({
			mediator = Dorm3dFurnitureSelectMediator,
			viewComponent = Dorm3dFurnitureSelectLayer,
			data = arg_1_0.contextData,
			onRemoved = function()
				arg_1_0.viewComponent:ShowBaseView()
			end
		}), nil, function()
			arg_1_0.viewComponent:HideBaseView()
		end)
	end)
	arg_1_0:bind(var_0_0.ON_CLICK_FURNITURE_SLOT, function(arg_8_0, arg_8_1)
		arg_1_0:sendNotification(arg_8_0, arg_8_1)
	end)
	arg_1_0:bind(var_0_0.OPEN_LEVEL_LAYER, function(arg_9_0)
		arg_1_0:addSubLayers(Context.New({
			viewComponent = Dorm3dLevelLayer,
			mediator = Dorm3dLevelMediator,
			data = {
				groupId = arg_1_0.contextData.groupId,
				timeIndex = arg_1_0.contextData.timeIndex
			},
			onRemoved = function()
				arg_1_0.viewComponent:ShowBaseView()
			end
		}), nil, function()
			arg_1_0.viewComponent:HideBaseView()
		end)
	end)
	arg_1_0:bind(var_0_0.OPEN_GIFT_LAYER, function(arg_12_0)
		arg_1_0:addSubLayers(Context.New({
			viewComponent = Dorm3dGiftLayer,
			mediator = Dorm3dGiftMediator,
			data = {
				groupId = arg_1_0.contextData.groupId
			},
			onRemoved = function()
				arg_1_0:SetBlackboardValue("inLockLayer", false)
				arg_1_0.viewComponent:ShowBaseView()
			end
		}), nil, function()
			arg_1_0:SetBlackboardValue("inLockLayer", true)
			arg_1_0.viewComponent:HideBaseView()
		end)
	end)
	arg_1_0:bind(var_0_0.OPEN_CAMERA_LAYER, function(arg_15_0)
		arg_1_0:addSubLayers(Context.New({
			viewComponent = Dorm3dPhotoLayer,
			mediator = Dorm3dPhotoMediator,
			data = arg_1_0.contextData,
			onRemoved = function()
				arg_1_0.viewComponent:ShowBaseView()
			end
		}), nil, function()
			arg_1_0.viewComponent:HideBaseView()
		end)
	end)
	arg_1_0:bind(var_0_0.OPEN_DROP_LAYER, function(arg_18_0, arg_18_1, arg_18_2)
		arg_1_0:addSubLayers(Context.New({
			viewComponent = Dorm3dAwardInfoLayer,
			mediator = Dorm3dAwardInfoMediator,
			data = {
				items = arg_18_1
			},
			onRemoved = arg_18_2
		}))
	end)
	arg_1_0:bind(var_0_0.OPEN_COLLECTION_LAYER, function(arg_19_0)
		arg_1_0:addSubLayers(Context.New({
			viewComponent = Dorm3dCollectionLayer,
			mediator = Dorm3dCollectionMediator,
			data = arg_1_0.contextData
		}))
	end)
	arg_1_0:bind(var_0_0.DO_TALK, function(arg_20_0, arg_20_1, arg_20_2)
		arg_1_0:sendNotification(GAME.APARTMENT_DO_TALK, {
			talkId = arg_20_1,
			callback = arg_20_2
		})
	end)
	arg_1_0:bind(var_0_0.COLLECTION_ITEM, function(arg_21_0, arg_21_1, arg_21_2)
		arg_1_0:sendNotification(GAME.APARTMENT_COLLECTION_ITEM, {
			groupId = arg_21_1,
			itemId = arg_21_2
		})
	end)
end

function var_0_0.initNotificationHandleDic(arg_22_0)
	arg_22_0.handleDic = {
		[GAME.APARTMENT_TRIGGER_FAVOR_DONE] = function(arg_23_0, arg_23_1)
			local var_23_0 = arg_23_1:getBody()

			arg_23_0.viewComponent.baseView:PopFavorTrigger(var_23_0.triggerId, var_23_0.delta, var_23_0.apartment)
			arg_23_0.viewComponent:SetApartment(var_23_0.apartment)
			arg_23_0.viewComponent.baseView:CheckFavorTrigger()
		end,
		[GAME.APARTMENT_LEVEL_UP_DONE] = function(arg_24_0, arg_24_1)
			local var_24_0 = arg_24_1:getBody()

			arg_24_0.viewComponent.baseView:PopFavorLevelUp(var_24_0, function()
				arg_24_0.viewComponent:SetApartment(var_24_0)
				arg_24_0.viewComponent.baseView:CheckFavorTrigger()
			end)
		end,
		[STORY_EVENT.TEST] = function(arg_26_0, arg_26_1)
			local var_26_0 = arg_26_1:getBody()

			arg_26_0.viewComponent.baseView:TalkingEventHandle(var_26_0)
		end,
		[ApartmentProxy.UPDATE_APARTMENT] = function(arg_27_0, arg_27_1)
			arg_27_0.viewComponent:SetApartment(arg_27_1:getBody())
		end,
		[var_0_0.OTHER_DO_TALK] = function(arg_28_0, arg_28_1)
			local var_28_0 = arg_28_1:getBody()

			arg_28_0.viewComponent.baseView:DoTalk(var_28_0.talkId, var_28_0.moveCamera, var_28_0.callback)
		end,
		[var_0_0.OTHER_CHECK_LEVEL_UP] = function(arg_29_0, arg_29_1)
			arg_29_0.viewComponent.baseView:CheckLevelUp()
		end,
		[GAME.APARTMENT_CHANGE_SKIN_DONE] = function(arg_30_0, arg_30_1)
			arg_30_0:ReloadScene()
		end,
		[GAME.APARTMENT_DO_TALK_DONE] = function(arg_31_0, arg_31_1)
			return
		end,
		[GAME.APARTMENT_COLLECTION_ITEM_DONE] = function(arg_32_0, arg_32_1)
			local var_32_0 = arg_32_1:getBody()

			arg_32_0:addSubLayers(Context.New({
				viewComponent = Dorm3dCollectAwardLayer,
				mediator = Dorm3dCollectAwardMediator,
				data = {
					itemId = var_32_0.itemId
				}
			}))
		end,
		[var_0_0.CHAMGE_TIME_RELOAD_SCENE] = function(arg_33_0, arg_33_1)
			local var_33_0 = arg_33_1:getBody()

			arg_33_0.contextData.timeIndex = var_33_0.timeIndex

			arg_33_0:ReloadScene()
		end
	}
end

function var_0_0.ReloadScene(arg_34_0)
	pg.SceneAnimMgr.GetInstance():Dorm3DSceneChange(function(arg_35_0)
		local var_35_0 = Clone(arg_34_0.contextData)

		var_35_0.resumeCallback = arg_35_0
		var_35_0.showLoading = false

		arg_34_0:sendNotification(GAME.RELOAD_SCENE, var_35_0)
	end)
end

function var_0_0.remove(arg_36_0)
	return
end

return var_0_0
