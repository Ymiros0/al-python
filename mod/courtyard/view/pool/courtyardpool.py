local var_0_0 = class("CourtYardPool")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4):
	arg_1_0.prefab = arg_1_2
	arg_1_0.parentTF = arg_1_1

	GetOrAddComponent(arg_1_0.prefab, typeof(CanvasGroup))
	arg_1_0.prefab.transform.SetParent(arg_1_0.parentTF, False)

	arg_1_0.layer = arg_1_0.parentTF.gameObject.layer
	arg_1_0.items = {}
	arg_1_0.max = arg_1_4
	arg_1_0.initCnt = arg_1_3

	arg_1_0.Init()

def var_0_0.Init(arg_2_0):
	for iter_2_0 = 1, arg_2_0.initCnt:
		arg_2_0.NewItem()

def var_0_0.Enqueue(arg_3_0, arg_3_1):
	if #arg_3_0.items >= arg_3_0.max:
		Object.Destroy(arg_3_1)
	else
		arg_3_1.transform.localPosition = Vector3.one

		setActiveViaLayer(arg_3_1.transform, False)
		arg_3_1.transform.SetParent(arg_3_0.parentTF, True)
		table.insert(arg_3_0.items, arg_3_1)

def var_0_0.Dequeue(arg_4_0):
	if #arg_4_0.items <= 0:
		arg_4_0.NewItem()

	local var_4_0 = table.remove(arg_4_0.items, 1)

	setActiveViaLayer(var_4_0.transform, True)

	return var_4_0

def var_0_0.NewItem(arg_5_0):
	local var_5_0 = Object.Instantiate(arg_5_0.prefab)

	var_5_0.transform.localScale = Vector3.one

	arg_5_0.Enqueue(var_5_0)

def var_0_0.Dispose(arg_6_0):
	for iter_6_0, iter_6_1 in ipairs(arg_6_0.items):
		Object.Destroy(iter_6_1)

	arg_6_0.items = None
	arg_6_0.prefab = None

return var_0_0
