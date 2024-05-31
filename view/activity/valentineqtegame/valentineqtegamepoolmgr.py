local var_0_0 = class("ValentineQteGamePoolMgr")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	arg_1_0.tpl = arg_1_1
	arg_1_0.initCnt = arg_1_2
	arg_1_0.maxCnt = arg_1_3
	arg_1_0.items = {}

	setActive(arg_1_0.tpl, False)
	arg_1_0.Init()

def var_0_0.Init(arg_2_0):
	for iter_2_0 = 1, arg_2_0.initCnt:
		local var_2_0 = arg_2_0.NewItem()

		table.insert(arg_2_0.items, var_2_0)

def var_0_0.NewItem(arg_3_0):
	local var_3_0 = Instantiate(arg_3_0.tpl)

	SetParent(var_3_0, arg_3_0.tpl.transform.parent)

	return var_3_0

def var_0_0.Dequeue(arg_4_0):
	local var_4_0

	if #arg_4_0.items > 0:
		var_4_0 = table.remove(arg_4_0.items, 1)
	else
		var_4_0 = arg_4_0.NewItem()

	setActive(var_4_0, True)

	return var_4_0

def var_0_0.Enqueue(arg_5_0, arg_5_1):
	if #arg_5_0.items >= arg_5_0.maxCnt:
		arg_5_0.DestroyItem(arg_5_1)
	else
		setActive(arg_5_1, False)
		SetParent(arg_5_1, arg_5_0.tpl.transform.parent)
		table.insert(arg_5_0.items, arg_5_1.gameObject)

def var_0_0.DestroyItem(arg_6_0, arg_6_1):
	Object.Destroy(go(arg_6_1))

def var_0_0.Destroy(arg_7_0):
	for iter_7_0, iter_7_1 in ipairs(arg_7_0.items):
		arg_7_0.DestroyItem(iter_7_1)

	arg_7_0.items = None

return var_0_0
