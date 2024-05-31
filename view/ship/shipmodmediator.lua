local var_0_0 = class("ShipModMediator", import("..base.ContextMediator"))

var_0_0.ON_SELECT_MATERIAL_SHIPS = "ShipModMediator:ON_SELECT_MATERIAL_SHIPS"
var_0_0.ON_AUTO_SELECT_SHIP = "ShipModMediator:ON_AUTO_SELECT_SHIP"
var_0_0.MOD_SHIP = "ShipModMediator:MOD_SHIP"
var_0_0.ON_SKILL = "ShipModMediator:ON_SKILL"
var_0_0.LOADEND = "ShipModMediator:LOADEND"

function var_0_0.register(arg_1_0)
	local var_1_0 = getProxy(BayProxy)
	local var_1_1 = var_1_0:getRawData()

	arg_1_0.viewComponent:setShipVOs(var_1_1)

	local var_1_2 = var_1_0:getShipById(arg_1_0.contextData.shipId)

	arg_1_0.viewComponent:setShip(var_1_2)
	arg_1_0:bind(var_0_0.ON_SELECT_MATERIAL_SHIPS, function(arg_2_0)
		local var_2_0 = pg.ShipFlagMgr.GetInstance():FilterShips(ShipStatus.FILTER_SHIPS_FLAGS_1)

		table.insert(var_2_0, 1, arg_1_0.contextData.shipId)
		arg_1_0:sendNotification(GAME.GO_SCENE, SCENE.DOCKYARD, {
			blockLock = true,
			destroyCheck = true,
			selectedMin = 0,
			selectedMax = 12,
			leftTopInfo = i18n("word_equipment_intensify"),
			mode = DockyardScene.MODE_MOD,
			onShip = ShipStatus.canDestroyShip,
			ignoredIds = var_2_0,
			selectedIds = arg_1_0.contextData.materialShipIds,
			onSelected = function(arg_3_0)
				arg_1_0.contextData.materialShipIds = arg_3_0
			end,
			sortData = {
				Asc = true,
				sort = 1
			},
			hideTagFlags = ShipStatus.TAG_HIDE_DESTROY
		})
	end)
	arg_1_0:bind(var_0_0.ON_AUTO_SELECT_SHIP, function(arg_4_0)
		local var_4_0 = var_1_0:getModRecommendShip(arg_1_0.viewComponent.shipVO, arg_1_0.contextData.materialShipIds or {})

		if #var_4_0 > 0 then
			arg_1_0.contextData.materialShipIds = var_4_0

			arg_1_0.viewComponent:initSelectedShips()
			arg_1_0.viewComponent:initAttrs()
		else
			pg.TipsMgr.GetInstance():ShowTips(i18n("without_selected_ship"))
		end
	end)
	arg_1_0:bind(var_0_0.MOD_SHIP, function(arg_5_0, arg_5_1)
		arg_1_0:sendNotification(GAME.MOD_SHIP, {
			shipId = arg_5_1,
			shipIds = arg_1_0.contextData.materialShipIds
		})
	end)
	arg_1_0:bind(var_0_0.ON_SKILL, function(arg_6_0, arg_6_1, arg_6_2)
		arg_1_0:addSubLayers(Context.New({
			mediator = SkillInfoMediator,
			viewComponent = SkillInfoLayer,
			data = {
				skillOnShip = arg_6_2,
				skillId = arg_6_1
			}
		}))
	end)
	arg_1_0:bind(var_0_0.LOADEND, function(arg_7_0, arg_7_1)
		arg_1_0:sendNotification(var_0_0.LOADEND, arg_7_1)
	end)
end

function var_0_0.listNotificationInterests(arg_8_0)
	return {
		GAME.MOD_SHIP_DONE
	}
end

function var_0_0.handleNotification(arg_9_0, arg_9_1)
	local var_9_0 = arg_9_1:getName()
	local var_9_1 = arg_9_1:getBody()

	if var_9_0 == GAME.MOD_SHIP_DONE then
		arg_9_0.contextData.materialShipIds = nil

		arg_9_0.viewComponent:setShip(var_9_1.newShip)
		arg_9_0.viewComponent:modAttrAnim(var_9_1.newShip, var_9_1.oldShip)
		pg.TipsMgr.GetInstance():ShowTips(i18n("ship_shipModLayer_modSuccess"))

		if table.getCount(var_9_1.equipments) > 0 then
			local var_9_2 = {}

			for iter_9_0, iter_9_1 in pairs(var_9_1.equipments) do
				table.insert(var_9_2, iter_9_1)
			end

			arg_9_0:addSubLayers(Context.New({
				viewComponent = ResolveEquipmentLayer,
				mediator = ResolveEquipmentMediator,
				data = {
					Equipments = var_9_2
				}
			}))
		end
	end
end

return var_0_0
