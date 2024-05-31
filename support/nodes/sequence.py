ys = ys or {}

local var_0_0 = class("Sequence")

ys.Sequence = var_0_0
var_0_0.Name = ""
var_0_0._list = None
var_0_0.Center = None
var_0_0._wait = False

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.Name = arg_1_1
	arg_1_0._list = ys.LinkList.New()
	arg_1_0.Center = arg_1_2

	arg_1_2.AddSeq(arg_1_0)

def var_0_0.Dispose(arg_2_0):
	local var_2_0 = arg_2_0._list.Head

	for iter_2_0 = 1, arg_2_0._list.Count:
		var_2_0.Data.Dispose()

		var_2_0 = var_2_0.Next

	arg_2_0._list.Clear()

def var_0_0.Add(arg_3_0, arg_3_1):
	arg_3_0._list.AddLast(arg_3_1)

def var_0_0.Wait(arg_4_0):
	arg_4_0._wait = True

def var_0_0.Resume(arg_5_0):
	arg_5_0._wait = False

def var_0_0.Update(arg_6_0):
	if arg_6_0._wait:
		return False

	while arg_6_0._list.Count > 0:
		local var_6_0 = arg_6_0._list.Head.Data

		if not var_6_0.Finish:
			var_6_0.UpdateNode()

			if not var_6_0.Finish:
				return False
			else
				arg_6_0._list.RemoveFirst()
		else
			arg_6_0._list.RemoveFirst()

	return True

def var_0_0.IsFinish(arg_7_0):
	local var_7_0 = arg_7_0._list.Head

	for iter_7_0 = 1, arg_7_0._list.Count:
		if not var_7_0.Data.Finish:
			return False

	return True
