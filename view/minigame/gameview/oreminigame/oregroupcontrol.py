local var_0_0 = class("OreGroupControl")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	arg_1_0.binder = arg_1_1
	arg_1_0._tf = arg_1_2
	arg_1_0.collisionMgr = arg_1_3
	arg_1_0.tpls = findTF(arg_1_0._tf, "tpl")
	arg_1_0.oresTF = findTF(arg_1_0._tf, "ores")
	arg_1_0.oreList = {}
	arg_1_0.poolTF = findTF(arg_1_0._tf, "pool")

	arg_1_0.AddListener()

def var_0_0.AddListener(arg_2_0):
	arg_2_0.binder.bind(OreGameConfig.EVENT_ORE_NEW, function(arg_3_0, arg_3_1)
		arg_2_0.NewOre(arg_3_1.index, arg_3_1.pos))
	arg_2_0.binder.bind(OreGameConfig.EVENT_ORE_DESTROY, function(arg_4_0, arg_4_1)
		arg_2_0.oreList[arg_4_1.index] = None

		arg_2_0.ReturnOre(findTF(arg_2_0.oresTF, arg_4_1.index), arg_4_1.id))

def var_0_0.NewOre(arg_5_0, arg_5_1, arg_5_2):
	if not findTF(arg_5_0.oresTF, arg_5_1):
		local var_5_0, var_5_1 = arg_5_0.GetNewOreConfig()
		local var_5_2 = arg_5_0.GetOre(var_5_0)

		var_5_2.SetParent(arg_5_0.oresTF, False)

		var_5_2.name = arg_5_1

		SetActive(var_5_2, True)

		local var_5_3 = Ore.New(arg_5_0.binder, var_5_2, arg_5_0.collisionMgr, var_5_0, arg_5_2)

		arg_5_0.oreList[arg_5_1] = var_5_3

		arg_5_0.binder.emit(OreGameConfig.EVENT_ORE_EF_MINED, {
			index = arg_5_1
		})

def var_0_0.Reset(arg_6_0):
	for iter_6_0, iter_6_1 in pairs(arg_6_0.oreList):
		iter_6_1.Dispose()

	arg_6_0.oreList = {}

	removeAllChildren(arg_6_0.oresTF)

	arg_6_0.weightTable = OreGameConfig.ORE_REFRESH_WEIGHT[math.random(#OreGameConfig.ORE_REFRESH_WEIGHT)]
	arg_6_0.count = 0
	arg_6_0.pools = {}

	removeAllChildren(arg_6_0.poolTF)

def var_0_0.GetNewOreConfig(arg_7_0):
	if arg_7_0.count == OreGameConfig.DIAMOND_CONFIH.count:
		local var_7_0 = OreGameConfig.DIAMOND_CONFIH.probability[1] > math.random() and 7 or 8

		arg_7_0.count = 0

		return var_7_0, OreGameConfig.ORE_CONFIG[var_7_0]

	local var_7_1 = OreGameHelper.GetOreIDWithWeight(arg_7_0.weightTable)
	local var_7_2 = OreGameConfig.ORE_CONFIG[var_7_1]

	arg_7_0.count = var_7_2.type == 4 and 0 or arg_7_0.count + 1

	return var_7_1, var_7_2

def var_0_0.OnTimer(arg_8_0, arg_8_1):
	for iter_8_0, iter_8_1 in pairs(arg_8_0.oreList):
		iter_8_1.OnTimer(arg_8_1)

def var_0_0.GetOre(arg_9_0, arg_9_1):
	if arg_9_0.pools[arg_9_1] and #arg_9_0.pools[arg_9_1] > 0:
		return table.remove(arg_9_0.pools[arg_9_1])

	return (tf(Instantiate(findTF(arg_9_0.tpls, "tpl_" .. arg_9_1))))

def var_0_0.ReturnOre(arg_10_0, arg_10_1, arg_10_2):
	if not arg_10_0.pools[arg_10_2]:
		arg_10_0.pools[arg_10_2] = {}

	arg_10_1.SetParent(tf(arg_10_0.poolTF), False)
	setActive(arg_10_1, False)
	table.insert(arg_10_0.pools[arg_10_2], tf(arg_10_1))

return var_0_0
