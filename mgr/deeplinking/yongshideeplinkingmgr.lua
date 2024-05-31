pg = pg or {}

local var_0_0 = pg

var_0_0.YongshiDeepLinkingMgr = singletonClass("YongshiDeepLinkingMgr")

local var_0_1 = var_0_0.YongshiDeepLinkingMgr
local var_0_2 = true

local function var_0_3(arg_1_0)
	if var_0_2 then
		originalPrint(arg_1_0)
	end
end

function var_0_1.SetData(arg_2_0, arg_2_1)
	var_0_3("SetData......")

	arg_2_0.deepLinking = arg_2_1

	arg_2_0:SwitchScene()
end

function var_0_1.ShouldSwitchScene(arg_3_0)
	if arg_3_0.deepLinking == nil or arg_3_0.deepLinking:IsEmpty() then
		var_0_3("deepLinking is empty")

		return false
	end

	if not var_0_0.m02 then
		var_0_3("game is not start")

		return false
	end

	local var_3_0 = getProxy(ContextProxy):getCurrentContext()

	if not var_3_0 then
		var_0_3("game is not start")

		return false
	end

	if var_3_0.mediator == LoginMediator then
		var_0_3("player is not created")

		return false
	end

	if var_3_0.mediator == CombatLoadMediator or var_3_0.mediator == BattleMediator then
		var_0_3("game is in battle")
		arg_3_0:Clear()

		return false
	end

	return true
end

local function var_0_4(arg_4_0, arg_4_1)
	var_0_3("Switch......" .. arg_4_0 .. "-" .. arg_4_1)

	if arg_4_0 == "1" then
		var_0_0.m02:sendNotification(GAME.GO_SCENE, SCENE.DOCKYARD)
	end
end

function var_0_1.SwitchScene(arg_5_0)
	var_0_3("SwitchScene......")

	if arg_5_0:ShouldSwitchScene() then
		local var_5_0 = arg_5_0.deepLinking.page
		local var_5_1 = arg_5_0.deepLinking.arg

		var_0_4(var_5_0, var_5_1)
		arg_5_0:Clear()
	end
end

function var_0_1.Clear(arg_6_0)
	var_0_3("Clear......")
	arg_6_0.deepLinking:Clear()

	arg_6_0.deepLinking = nil
end
