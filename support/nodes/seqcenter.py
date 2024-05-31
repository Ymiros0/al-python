ys = ys or {}

local var_0_0 = class("SeqCenter")

ys.SeqCenter = var_0_0
var_0_0._list = None
var_0_0._destroyed = False

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0._list = ys.LinkList.New()

def var_0_0.NewSeq(arg_2_0, arg_2_1):
	return ys.Sequence.New(arg_2_1, arg_2_0)

def var_0_0.AddSeq(arg_3_0, arg_3_1):
	arg_3_0._list.AddLast(arg_3_1)

def var_0_0.Update(arg_4_0):
	if arg_4_0._destroyed:
		return

	local var_4_0 = arg_4_0._list.Head

	while var_4_0 != None:
		local var_4_1 = var_4_0.Data

		var_4_1.Update()

		if arg_4_0._destroyed:
			return

		if var_4_1.IsFinish():
			local var_4_2 = var_4_0

			var_4_0 = var_4_0.Next

			arg_4_0._list.Remove(var_4_2)
		else
			var_4_0 = var_4_0.Next

def var_0_0.Dispose(arg_5_0):
	local var_5_0 = arg_5_0._list.Head

	for iter_5_0 = 1, arg_5_0._list.Count:
		var_5_0.Data.Dispose()

		var_5_0 = var_5_0.Next

	arg_5_0._list = None
	arg_5_0._destroyed = True

def var_0_0.IsFinish(arg_6_0):
	if arg_6_0._list == None:
		return True

	local var_6_0 = arg_6_0._list.Head

	for iter_6_0 = 1, arg_6_0._list.Count:
		if not var_6_0.Data.IsFinish():
			return False

		var_6_0 = var_6_0.Next

	return True
