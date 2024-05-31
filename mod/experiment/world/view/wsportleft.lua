local var_0_0 = class("WSPortLeft", import("...BaseEntity"))

var_0_0.Fields = {
	map = "table",
	rtVanguard = "userdata",
	rtFleet = "userdata",
	gid = "number",
	rtShip = "userdata",
	transform = "userdata",
	rtBG = "userdata",
	rtMain = "userdata",
	fleet = "table"
}
var_0_0.Listeners = {
	onUpdateSelectedFleet = "OnUpdateSelectedFleet",
	onUpdateShip = "OnUpdateShip"
}

function var_0_0.Setup(arg_1_0)
	pg.DelegateInfo.New(arg_1_0)
	arg_1_0:Init()
end

function var_0_0.Dispose(arg_2_0)
	arg_2_0:RemoveMapListener()
	pg.DelegateInfo.Dispose(arg_2_0)
	arg_2_0:Clear()
end

function var_0_0.Init(arg_3_0)
	arg_3_0.rtBG = arg_3_0.transform:Find("bg")
	arg_3_0.rtFleet = arg_3_0.rtBG:Find("fleet")
	arg_3_0.rtMain = arg_3_0.rtFleet:Find("main")
	arg_3_0.rtVanguard = arg_3_0.rtFleet:Find("vanguard")
	arg_3_0.rtShip = arg_3_0.rtFleet:Find("shiptpl")

	setActive(arg_3_0.rtShip, false)
end

function var_0_0.UpdateMap(arg_4_0, arg_4_1)
	if arg_4_0.map ~= arg_4_1 or arg_4_0.gid ~= arg_4_1.gid then
		arg_4_0:RemoveMapListener()

		arg_4_0.map = arg_4_1
		arg_4_0.gid = arg_4_1.gid

		arg_4_0:AddMapListener()
		arg_4_0:OnUpdateSelectedFleet()
	end
end

function var_0_0.AddMapListener(arg_5_0)
	if arg_5_0.map then
		arg_5_0.map:AddListener(WorldMap.EventUpdateFIndex, arg_5_0.onUpdateSelectedFleet)
	end
end

function var_0_0.RemoveMapListener(arg_6_0)
	if arg_6_0.map then
		arg_6_0.map:RemoveListener(WorldMap.EventUpdateFIndex, arg_6_0.onUpdateSelectedFleet)
		arg_6_0:RemoveFleetListener(arg_6_0.fleet)
	end
end

function var_0_0.AddFleetListener(arg_7_0, arg_7_1)
	if arg_7_1 then
		_.each(arg_7_1:GetShips(true), function(arg_8_0)
			arg_8_0:AddListener(WorldMapShip.EventHpRantChange, arg_7_0.onUpdateShip)
		end)
	end
end

function var_0_0.RemoveFleetListener(arg_9_0, arg_9_1)
	if arg_9_1 then
		_.each(arg_9_1:GetShips(true), function(arg_10_0)
			arg_10_0:RemoveListener(WorldMapShip.EventHpRantChange, arg_9_0.onUpdateShip)
		end)
	end
end

function var_0_0.OnUpdateSelectedFleet(arg_11_0)
	local var_11_0 = arg_11_0.map:GetFleet()

	if arg_11_0.fleet ~= var_11_0 then
		arg_11_0:RemoveFleetListener(arg_11_0.fleet)

		arg_11_0.fleet = var_11_0

		arg_11_0:AddFleetListener(arg_11_0.fleet)
		arg_11_0:UpdateShipList(arg_11_0.rtMain, arg_11_0.fleet:GetTeamShipVOs(TeamType.Main, true))
		arg_11_0:UpdateShipList(arg_11_0.rtVanguard, arg_11_0.fleet:GetTeamShipVOs(TeamType.Vanguard, true))
	end
end

function var_0_0.OnUpdateShip(arg_12_0, arg_12_1, arg_12_2)
	local var_12_0 = arg_12_0.map:GetFleet(arg_12_2.fleetId)

	assert(var_12_0, "can not find fleet: " .. arg_12_2.fleetId)

	local var_12_1 = var_12_0:GetFleetType()

	if var_12_1 == FleetType.Normal then
		arg_12_0:UpdateShipList(arg_12_0.rtMain, arg_12_0.fleet:GetTeamShipVOs(TeamType.Main, true))
		arg_12_0:UpdateShipList(arg_12_0.rtVanguard, arg_12_0.fleet:GetTeamShipVOs(TeamType.Vanguard, true))
	elseif var_12_1 == FleetType.Submarine then
		arg_12_0:UpdateShipList(arg_12_0.rtSubmarine, arg_12_0.submarineFleet:GetTeamShipVOs(TeamType.Submarine, true))
	end
end

function var_0_0.UpdateShipList(arg_13_0, arg_13_1, arg_13_2)
	local var_13_0 = UIItemList.New(arg_13_1, arg_13_0.rtShip)

	var_13_0:make(function(arg_14_0, arg_14_1, arg_14_2)
		if arg_14_0 == UIItemList.EventUpdate then
			local var_14_0 = arg_13_2[arg_14_1 + 1]
			local var_14_1 = WorldConst.FetchWorldShip(var_14_0.id)

			updateShip(arg_14_2, var_14_0)

			local var_14_2 = findTF(arg_14_2, "HP_POP")

			setActive(var_14_2, true)
			setActive(findTF(var_14_2, "heal"), false)
			setActive(findTF(var_14_2, "normal"), false)

			local var_14_3 = findTF(arg_14_2, "blood")
			local var_14_4 = findTF(arg_14_2, "blood/fillarea/green")
			local var_14_5 = findTF(arg_14_2, "blood/fillarea/red")
			local var_14_6 = not var_14_1:IsHpSafe()

			setActive(var_14_4, not var_14_6)
			setActive(var_14_5, var_14_6)

			var_14_3:GetComponent(typeof(Slider)).fillRect = var_14_6 and var_14_5 or var_14_4

			setSlider(var_14_3, 0, 10000, var_14_1.hpRant)

			local var_14_7 = arg_14_2:Find("agony")

			setActive(var_14_7, var_14_6)

			local var_14_8 = arg_14_2:Find("broken")

			setActive(var_14_8, var_14_1:IsBroken())
		end
	end)
	var_13_0:align(#arg_13_2)
end

return var_0_0
