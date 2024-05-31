pg = pg or {}

local var_0_0 = pg

var_0_0.NodeCanvasMgr = singletonClass("NodeCanvasMgr")

local var_0_1 = var_0_0.NodeCanvasMgr

function var_0_1.Ctor(arg_1_0)
	arg_1_0:Clear()
end

function var_0_1.Init(arg_2_0, arg_2_1)
	print("initializing NodeCanvas manager...")
	existCall(arg_2_1)
end

function var_0_1.SetOwner(arg_3_0, arg_3_1)
	assert(not arg_3_0.mainOwner)

	arg_3_0.mainOwner = GetComponent(arg_3_1, "GraphOwner")
	arg_3_0.mainBlackboard = GetComponent(arg_3_1, "Blackboard")
end

function var_0_1.SetBlackboradValue(arg_4_0, arg_4_1, arg_4_2, arg_4_3)
	arg_4_3 = arg_4_3 or arg_4_0.mainBlackboard

	if arg_4_2 == nil then
		arg_4_3:RemoveVariable(arg_4_1)
	else
		arg_4_3:SetVariableValue(arg_4_1, arg_4_2)
	end
end

function var_0_1.SendEvent(arg_5_0, arg_5_1, arg_5_2, arg_5_3)
	arg_5_3 = arg_5_3 or arg_5_0.mainOwner

	if arg_5_2 == nil then
		arg_5_3:SendEvent(arg_5_1)
	else
		arg_5_3:SendEvent(arg_5_1, arg_5_2, nil)
	end
end

function var_0_1.SendGlobalEvent(arg_6_0, arg_6_1, arg_6_2)
	arg_6_0.mainOwner.graph:SendGlobalEvent(arg_6_1, arg_6_2, nil)
end

function var_0_1.RegisterFunc(arg_7_0, arg_7_1, arg_7_2)
	arg_7_0.functionDic[arg_7_1] = arg_7_2
end

function var_0_1.CallFunc(arg_8_0, arg_8_1, ...)
	assert(arg_8_0.functionDic[arg_8_1], "with out register call:" .. arg_8_1)
	arg_8_0.functionDic[arg_8_1](...)
end

function var_0_1.Clear(arg_9_0)
	arg_9_0.mainOwner = nil
	arg_9_0.functionDic = {}
end

function LuaActionTaskCall(arg_10_0, ...)
	local var_10_0 = var_0_0.NodeCanvasMgr.GetInstance()

	assert(var_10_0 and var_10_0.mainOwner)
	var_10_0:CallFunc(arg_10_0, ...)
end
