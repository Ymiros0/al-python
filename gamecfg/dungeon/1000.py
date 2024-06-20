from luatable import table
from Vector3 import Vector3
data = table(
	map_id = 10008,
	id = 1000,
	stages = table(
		table(
			stageIndex = 1,
			failCondition = 1,
			timeCount = 90,
			passCondition = 1,
			backGroundStageID = 1,
			totalArea = table(
				-70,
				20,
				90,
				70
			),
			playerArea = table(
				-70,
				20,
				37,
				68
			),
			enemyArea = table(),
			mainUnitPosition = table({
				1: table(
					Vector3(-105, 0, 58),
					Vector3(-105, 0, 78),
					Vector3(-105, 0, 38)
				),
				-1: table(
					Vector3(15, 0, 58),
					Vector3(15, 0, 78),
					Vector3(15, 0, 38)
				)
			}),
			fleetCorrdinate = table(
				-80,
				0,
				75
			),
			waves = table(
				table(
					triggerType = 1,
					waveIndex = 100,
					preWaves = table(),
					triggerParams = table(
						timeout = 0.5
					)
				),
				table(
					triggerType = 1,
					waveIndex = 200,
					preWaves = table(),
					triggerParams = table(
						timeout = 21.5
					)
				),
				table(
					triggerType = 0,
					waveIndex = 101,
					conditionType = 1,
					preWaves = table(
						100
					),
					triggerParam = table(),
					spawn = table(
						table(
							monsterTemplateID = 802,
							moveCast = True,
							delay = 0,
							corrdinate = table(
								-12,
								0,
								80
							),
							buffList = table(
								8001,
								8007
							)
						),
						table(
							monsterTemplateID = 802,
							moveCast = True,
							delay = 0,
							corrdinate = table(
								-12,
								0,
								64
							),
							buffList = table(
								8001,
								8007
							)
						),
						table(
							monsterTemplateID = 803,
							moveCast = True,
							delay = 0,
							corrdinate = table(
								-12,
								0,
								48
							),
							buffList = table(
								8001,
								8007,
								8102
							)
						),
						table(
							monsterTemplateID = 802,
							moveCast = True,
							delay = 0,
							corrdinate = table(
								-12,
								0,
								32
							),
							buffList = table(
								8001,
								8007
							)
						),
						table(
							monsterTemplateID = 800,
							moveCast = True,
							delay = 3,
							corrdinate = table(
								-6,
								0,
								75
							),
							buffList = table(
								8001,
								8007,
								8101
							)
						),
						table(
							monsterTemplateID = 801,
							moveCast = True,
							delay = 6,
							corrdinate = table(
								-6,
								0,
								55
							),
							buffList = table(
								8001,
								8007,
								8608
							)
						),
						table(
							monsterTemplateID = 803,
							moveCast = True,
							delay = 9,
							corrdinate = table(
								0,
								0,
								55
							),
							buffList = table(
								8001,
								8007,
								8102
							)
						),
						table(
							monsterTemplateID = 802,
							moveCast = True,
							delay = 9,
							corrdinate = table(
								0,
								0,
								40
							),
							buffList = table(
								8001,
								8007
							)
						),
						table(
							monsterTemplateID = 802,
							moveCast = True,
							delay = 9,
							corrdinate = table(
								0,
								0,
								25
							),
							buffList = table(
								8001,
								8007
							)
						),
						table(
							monsterTemplateID = 803,
							moveCast = True,
							delay = 12,
							corrdinate = table(
								6,
								0,
								80
							),
							buffList = table(
								8001,
								8007,
								8102
							)
						),
						table(
							monsterTemplateID = 802,
							moveCast = True,
							delay = 12,
							corrdinate = table(
								6,
								0,
								65
							),
							buffList = table(
								8001,
								8007
							)
						),
						table(
							monsterTemplateID = 803,
							moveCast = True,
							delay = 12,
							corrdinate = table(
								6,
								0,
								50
							),
							buffList = table(
								8001,
								8007,
								8102
							)
						),
						table(
							monsterTemplateID = 802,
							moveCast = True,
							delay = 15,
							corrdinate = table(
								12,
								0,
								75
							),
							buffList = table(
								8001,
								8007
							)
						),
						table(
							monsterTemplateID = 803,
							moveCast = True,
							delay = 15,
							corrdinate = table(
								12,
								0,
								55
							),
							buffList = table(
								8001,
								8007,
								8102
							)
						),
						table(
							monsterTemplateID = 802,
							moveCast = True,
							delay = 15,
							corrdinate = table(
								12,
								0,
								35
							),
							buffList = table(
								8001,
								8007
							)
						),
						table(
							monsterTemplateID = 800,
							moveCast = True,
							delay = 18,
							corrdinate = table(
								18,
								0,
								35
							),
							buffList = table(
								8001,
								8007,
								8101
							)
						)
					)
				),
				table(
					triggerType = 0,
					key = True,
					waveIndex = 201,
					conditionType = 1,
					preWaves = table(
						200
					),
					triggerParam = table(),
					spawn = table(
						table(
							monsterTemplateID = 801,
							moveCast = True,
							delay = 0,
							corrdinate = table(
								18,
								0,
								55
							),
							buffList = table(
								8001,
								8007,
								8608
							)
						)
					)
				),
				table(
					triggerType = 8,
					waveIndex = 900,
					preWaves = table(
						201
					),
					triggerParams = table()
				),
				table(
					triggerType = 1,
					waveIndex = 205,
					preWaves = table(
						201
					),
					triggerParams = table(
						timeout = 1
					)
				)
			)
		)
	),
	fleet_prefab = table()
)
