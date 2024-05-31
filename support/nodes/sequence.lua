ys = ys or {}

local var_0_0 = class("Sequence")

ys.Sequence = var_0_0
var_0_0.Name = ""
var_0_0._list = nil
var_0_0.Center = nil
var_0_0._wait = false

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	arg_1_0.Name = arg_1_1
	arg_1_0._list = ys.LinkList.New()
	arg_1_0.Center = arg_1_2

	arg_1_2:AddSeq(arg_1_0)
end

function var_0_0.Dispose(arg_2_0)
	local var_2_0 = arg_2_0._list.Head

	for iter_2_0 = 1, arg_2_0._list.Count do
		var_2_0.Data:Dispose()

		var_2_0 = var_2_0.Next
	end

	arg_2_0._list:Clear()
end

function var_0_0.Add(arg_3_0, arg_3_1)
	arg_3_0._list:AddLast(arg_3_1)
end

function var_0_0.Wait(arg_4_0)
	arg_4_0._wait = true
end

function var_0_0.Resume(arg_5_0)
	arg_5_0._wait = false
end

function var_0_0.Update(arg_6_0)
	if arg_6_0._wait then
		return false
	end

	while arg_6_0._list.Count > 0 do
		local var_6_0 = arg_6_0._list.Head.Data

		if not var_6_0.Finish then
			var_6_0:UpdateNode()

			if not var_6_0.Finish then
				return false
			else
				arg_6_0._list:RemoveFirst()
			end
		else
			arg_6_0._list:RemoveFirst()
		end
	end

	return true
end

function var_0_0.IsFinish(arg_7_0)
	local var_7_0 = arg_7_0._list.Head

	for iter_7_0 = 1, arg_7_0._list.Count do
		if not var_7_0.Data.Finish then
			return false
		end
	end

	return true
end
