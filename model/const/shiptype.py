from luatable import table, ipairs
from Framework.Include import underscore

QuZhu = 1
QingXun = 2
ZhongXun = 3
ZhanXun = 4
ZhanLie = 5
QingHang = 6
ZhengHang = 7
QianTing = 8
HangXun = 9
HangZhan = 10
LeiXun = 11
WeiXiu = 12
ZhongPao = 13
QianMu = 17
ChaoXun = 18
Yunshu = 19
DaoQuV = 20
DaoQuM = 21
FengFanS = 22
FengFanV = 23
FengFanM = 24
YuLeiTing = 14
JinBi = 15
ZiBao = 16
WeiZhi = 25
AllShipType = table(
	1,
	2,
	3,
	18,
	4,
	5,
	6,
	7,
	10,
	17,
	13,
	8,
	12,
	19,
	20,
	21,
	22,
	23,
	24
)
SpecificTypeTable = table(
	auxiliary = "AUX",
	gunner = "GNR",
	torpedo = "TORP"
)
SpecificTableTips = table(
	GNR = "breakout_tip_ultimatebonus_gunner",
	TORP = "breakout_tip_ultimatebonus_torpedo",
	AUX = "breakout_tip_ultimatebonus_aux"
)

def Type2Name(arg_1_0):
	return pg.ship_data_by_type[arg_1_0].type_name #Use api

def Type2Print(arg_2_0):
	if not prints:
		prints = table(
			"quzhu",
			"qingxun",
			"zhongxun",
			"zhanlie",
			"zhanlie",
			"hangmu",
			"hangmu",
			"qianting",
			"zhanlie",
			"hangzhan",
			"zhanlie",
			"weixiu",
			"zhongpao",
			"quzhu",
			"battle_jinbi",
			"battle_zibao",
			"qianmu",
			"chaoxun",
			"yunshu",
			"daoquv",
			"daoqum",
			"fengfans",
			"fengfanv",
			"fengfanm",
			"weizhi"
		)

	return prints[arg_2_0]

def Type2BattlePrint(arg_3_0):
	if not bprints:
		bprints = table(
			"battle_quzhu",
			"battle_qingxun",
			"battle_zhongxun",
			"battle_zhanlie",
			"battle_zhanlie",
			"battle_hangmu",
			"battle_hangmu",
			"battle_qianting",
			"battle_zhanlie",
			"battle_hangmu",
			"battle_zhanlie",
			"battle_weixiu",
			"battle_zhanlie",
			"battle_quzhu",
			"battle_jinbi",
			"battle_zibao",
			"battle_hangmu",
			"battle_zhanlie",
			"battle_yunshu",
			"battle_daoqu",
			"battle_daoqu",
			"battle_fengfans",
			"battle_fengfanv",
			"battle_fengfanm",
			"battle_weizhi"
		)

	return bprints[arg_3_0]

def Type2CNLabel(arg_4_0):
	if not cnLabel:
		cnLabel = table(
			"label_1",
			"label_2",
			"label_3",
			"label_4",
			"label_5",
			"label_6",
			"label_7",
			"label_19",
			"label_3",
			"label_10",
			"label_3",
			"label_20",
			"label_21",
			"label_1",
			"label_1",
			"label_1",
			"label_17",
			"label_18",
			"label_22",
			"label_23",
			"label_23",
			"label_24",
			"label_25",
			"label_26",
			fengfan = "label_27"
		)

	return cnLabel[arg_4_0]

BundleBattleShip = "zhan"
BundleAircraftCarrier = "hang"
BundleSubmarine = "qian"
BundleLargeCrusier = "zhong"
BundleAntiSubmarine = "fanqian"
BundleList = table(
	zhan = table(
		ZhanXun,
		ZhanLie
	),
	hang = table(
		QingHang,
		ZhengHang
	),
	qian = table(
		QianTing,
		QianMu,
		FengFanS
	),
	zhong = table(
		ZhongXun,
		ChaoXun
	),
	fanqian = table(
		QuZhu,
		QingXun,
		DaoQuV
	),
	quzhu = table(
		QuZhu,
		DaoQuM,
		DaoQuV
	),
	fengfan = table(
		FengFanS,
		FengFanV,
		FengFanM
	)
)

def BundleType2CNLabel(arg_5_0):
	if not bundleLabel:
		bundleLabel = table(
			zhong = "label_13",
			qian = "label_8",
			zhan = "label_11",
			fanqian = "label_55",
			hang = "label_12",
			quzhu = "label_1"
		)

	return bundleLabel[arg_5_0]

def ContainInLimitBundle(arg_6_0, arg_6_1):
	if type(arg_6_0) == str:
		for iter_6_0, iter_6_1 in ipairs(BundleList[arg_6_0]):
			if iter_6_1 == arg_6_1:
				return True
	elif type(arg_6_0) in (float, int):
		return arg_6_0 == 0 or arg_6_1 == arg_6_0

	return False

CloakShipTypeList = table(
	QingHang,
	ZhengHang,
	DaoQuM
)

def CloakShipType(arg_7_0):
	return table.contains(CloakShipTypeList, arg_7_0)

QuZhuShipType = table()

for iter_0_0, iter_0_1 in ipairs(BundleList.quzhu):
	QuZhuShipType[iter_0_1] = True

def IsTypeQuZhu(arg_8_0):
	return QuZhuShipType[arg_8_0]

def FilterOverQuZhuType(arg_9_0):
	var_9_0 = False
	def helper(arg_10_0):
		if not var_9_0 or not IsTypeQuZhu(arg_10_0):
			var_9_0 = var_9_0 or IsTypeQuZhu(arg_10_0)

			return True
		else:
			return False
	return underscore.filter(arg_9_0, helper)

FengFanType = table()

for iter_0_2, iter_0_3 in ipairs(BundleList.fengfan):
	FengFanType[iter_0_3] = True

def IsTypeFengFan(arg_11_0):
	return FengFanType[arg_11_0]

def FilterOverFengFanType(arg_12_0):
	var_12_0 = False

	def helper(arg_13_0):
		if not var_12_0 or not IsTypeFengFan(arg_13_0):
			var_12_0 = var_12_0 or IsTypeFengFan(arg_13_0)

			return True
		else:
			return False
	return underscore.filter(arg_12_0, helper)

def MergeFengFanType(arg_14_0, arg_14_1, arg_14_2):
	var_14_0 = BundleList.fengfan[1]

	if underscore.all(BundleList.fengfan, lambda arg_15_0: arg_14_1[var_14_0] == arg_14_1[arg_15_0] and arg_14_2[var_14_0] == arg_14_2[arg_15_0]):
		var_14_1 = table.indexof(arg_14_0, var_14_0)

		arg_14_0 = underscore.filter(arg_14_0, lambda arg_16_0: not table.contains(BundleList.fengfan, arg_16_0))

		table.insert(arg_14_0, var_14_1, "fengfan")

		arg_14_1.fengfan = arg_14_1[var_14_0]
		arg_14_2.fengfan = arg_14_2[var_14_0]

	return arg_14_0
