from packages.luatable import table
from model.const import ShipType, TeamType, Nation, ShipRarity, ShipIndexConst
ShipIndexCfg = table(
	type = table(
		table(
			types = table()
		),
		table(
			types = table(
				TeamType.Vanguard
			),
			shipTypes = table(
				ShipType.DaoQuV
			)
		),
		table(
			types = table(
				TeamType.Main
			),
			shipTypes = table(
				ShipType.DaoQuM
			)
		),
		table(
			types = table(
				ShipType.QuZhu,
				ShipType.DaoQuM,
				ShipType.DaoQuV
			)
		),
		table(
			types = table(
				ShipType.QingXun
			)
		),
		table(
			types = table(
				ShipType.ZhongXun,
				ShipType.ChaoXun
			)
		),
		table(
			types = table(
				ShipType.ZhanXun,
				ShipType.ZhanLie
			)
		),
		table(
			types = table(
				ShipType.QingHang,
				ShipType.ZhengHang
			)
		),
		table(
			types = table(
				ShipType.WeiXiu
			)
		),
		table(
			types = table(
				ShipType.QianTing,
				ShipType.QianMu
			)
		),
		table(
			types = table(
				ShipType.HangXun,
				ShipType.HangZhan,
				ShipType.LeiXun,
				ShipType.ZhongPao,
				ShipType.Yunshu,
				ShipType.FengFanS,
				ShipType.FengFanV,
				ShipType.FengFanM
			)
		)
	),
	camp = table(
		table(
			types = table()
		),
		table(
			types = table(
				Nation.US
			)
		),
		table(
			types = table(
				Nation.EN
			)
		),
		table(
			types = table(
				Nation.JP
			)
		),
		table(
			types = table(
				Nation.DE
			)
		),
		table(
			types = table(
				Nation.CN
			)
		),
		table(
			types = table(
				Nation.ITA
			)
		),
		table(
			types = table(
				Nation.SN
			)
		),
		table(
			types = table(
				Nation.FF
			)
		),
		table(
			types = table(
				Nation.MNF
			)
		),
		table(
			types = table(
				Nation.META
			)
		),
		table(
			types = table(
				Nation.MOT
			)
		),
		table(
			types = table(
				Nation.CM,
				Nation.BURIN,
				Nation.LINK
			)
		)
	),
	rarity = table(
		table(
			types = table()
		),
		table(
			types = table(
				ShipRarity.Gray
			)
		),
		table(
			types = table(
				ShipRarity.Blue
			)
		),
		table(
			types = table(
				ShipRarity.Purple
			)
		),
		table(
			types = table(
				ShipRarity.Gold
			)
		),
		table(
			types = table(
				ShipRarity.SSR
			)
		)
	),
	sort = table(
		table(
			sortFuncs = ShipIndexConst.sortByCfg("rarity"),
			name = ShipIndexConst.SortNames[1]
		),
		table(
			sortFuncs = ShipIndexConst.sortByField("level"),
			name = ShipIndexConst.SortNames[2]
		),
		table(
			sortFuncs = ShipIndexConst.sortByCombatPower(),
			name = ShipIndexConst.SortNames[3]
		),
		table(
			sortFuncs = ShipIndexConst.sortByField("createTime"),
			name = ShipIndexConst.SortNames[4]
		),
		table(
			sortFuncs = ShipIndexConst.sortByIntimacy(),
			name = ShipIndexConst.SortNames[5]
		),
		table(
			sortFuncs = ShipIndexConst.sortByProperty("cannon"),
			name = ShipIndexConst.SortPropertyNames[2]
		),
		table(
			sortFuncs = ShipIndexConst.sortByProperty("air"),
			name = ShipIndexConst.SortPropertyNames[3]
		),
		table(
			sortFuncs = ShipIndexConst.sortByProperty("dodge"),
			name = ShipIndexConst.SortPropertyNames[4]
		),
		table(
			sortFuncs = ShipIndexConst.sortByProperty("antiaircraft"),
			name = ShipIndexConst.SortPropertyNames[5]
		),
		table(
			sortFuncs = ShipIndexConst.sortByProperty("torpedo"),
			name = ShipIndexConst.SortPropertyNames[6]
		),
		table(
			sortFuncs = ShipIndexConst.sortByProperty("reload"),
			name = ShipIndexConst.SortPropertyNames[7]
		),
		table(
			sortFuncs = ShipIndexConst.sortByProperty("durability"),
			name = ShipIndexConst.SortPropertyNames[8]
		),
		table(
			sortFuncs = ShipIndexConst.sortByProperty("antisub"),
			name = ShipIndexConst.SortPropertyNames[9]
		),
		table(
			sortFuncs = ShipIndexConst.sortByEnergy(),
			name = ShipIndexConst.SortNames[6]
		)
	)
)
