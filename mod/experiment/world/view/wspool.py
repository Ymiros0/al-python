local var_0_0 = class("WSPool", import("...BaseEntity"))

var_0_0.Fields = {
	tplDic = "table",
	pooltf = "userdata",
	pools = "table"
}

def var_0_0.Setup(arg_1_0, arg_1_1):
	arg_1_0.pools = {}
	arg_1_0.pooltf = GameObject.Find("__Pool__").transform

	local var_1_0 = GetComponent(arg_1_1, "ItemList").prefabItem

	arg_1_0.tplDic = {}

	for iter_1_0 = 0, var_1_0.Length - 1:
		arg_1_0.tplDic[var_1_0[iter_1_0].name] = var_1_0[iter_1_0]

	setActive(arg_1_1, False)

def var_0_0.Dispose(arg_2_0):
	for iter_2_0, iter_2_1 in pairs(arg_2_0.pools):
		_.each(iter_2_1, function(arg_3_0)
			Destroy(arg_3_0))

	arg_2_0.Clear()

def var_0_0.Get(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_0.pools
	local var_4_1 = var_4_0[arg_4_1]

	if not var_4_1:
		var_4_1 = {}
		var_4_0[arg_4_1] = var_4_1

	local var_4_2

	if #var_4_1 > 0:
		var_4_2 = table.remove(var_4_1, #var_4_1)
	else
		var_4_2 = Instantiate(arg_4_0.tplDic[arg_4_1])

	setActive(var_4_2, True)
	tf(var_4_2).SetParent(arg_4_0.pooltf, False)

	return var_4_2

def var_0_0.Return(arg_5_0, arg_5_1, arg_5_2):
	setActive(arg_5_2, False)
	arg_5_2.transform.SetParent(arg_5_0.pooltf, False)

	local var_5_0 = arg_5_0.pools[arg_5_1]

	table.insert(var_5_0, arg_5_2)

return var_0_0
