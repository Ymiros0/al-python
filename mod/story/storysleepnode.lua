ys = ys or {}
ys.Story.StorySleepNode = class("StorySleepNode", ys.ISeqNode)

local var_0_0 = ys.Story.StorySleepNode

pg.NodeMgr.RigisterNode("StorySleep", var_0_0)

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	arg_1_0._time = arg_1_2[2]
end

function var_0_0.Init(arg_2_0)
	arg_2_0._end = os.time() + arg_2_0._time
end

function var_0_0.Update(arg_3_0)
	if os.time() >= arg_3_0._end then
		arg_3_0:Dispose()
	end
end
