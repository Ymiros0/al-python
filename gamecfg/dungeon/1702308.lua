﻿return {
	id = 1702308,
	stages = {
		{
			stageIndex = 1,
			failCondition = 1,
			timeCount = 180,
			passCondition = 1,
			backGroundStageID = 1,
			totalArea = {
				-70,
				20,
				90,
				70
			},
			playerArea = {
				-70,
				20,
				37,
				68
			},
			enemyArea = {},
			fleetCorrdinate = {
				-80,
				0,
				75
			},
			waves = {
				{
					triggerType = 1,
					waveIndex = 100,
					preWaves = {},
					triggerParams = {
						timeout = 0.5
					}
				},
				{
					triggerType = 1,
					waveIndex = 202,
					preWaves = {},
					triggerParams = {
						timeout = 20
					}
				},
				{
					triggerType = 1,
					waveIndex = 203,
					preWaves = {},
					triggerParams = {
						timeout = 40
					}
				},
				{
					triggerType = 0,
					key = true,
					waveIndex = 101,
					conditionType = 1,
					preWaves = {
						100
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 16402208,
							reinforceDelay = 6,
							score = 0,
							delay = 0,
							moveCast = true,
							corrdinate = {
								-5,
								0,
								50
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 16402010,
							reinforceDelay = 6,
							score = 0,
							delay = 0,
							moveCast = true,
							corrdinate = {
								0,
								0,
								63
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 16402011,
							reinforceDelay = 6,
							score = 0,
							delay = 0,
							moveCast = true,
							corrdinate = {
								0,
								0,
								37
							},
							buffList = {
								8001,
								8007
							}
						}
					},
					reinforcement = {
						{
							monsterTemplateID = 16402001,
							moveCast = true,
							delay = 4,
							score = 0,
							corrdinate = {
								12,
								0,
								75
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 16402001,
							moveCast = true,
							delay = 4,
							score = 0,
							corrdinate = {
								12,
								0,
								25
							},
							buffList = {
								8001,
								8007
							}
						}
					}
				},
				{
					triggerType = 0,
					waveIndex = 2001,
					conditionType = 1,
					preWaves = {
						100
					},
					triggerParam = {},
					spawn = {},
					reinforcement = {
						{
							monsterTemplateID = 16402009,
							moveCast = true,
							delay = 8,
							corrdinate = {
								5,
								0,
								58
							},
							buffList = {
								8001
							},
							phase = {
								{
									switchParam = 20,
									dive = "STATE_RAID",
									switchTo = 1,
									index = 0,
									switchType = 1,
									setAI = 20005
								},
								{
									index = 1,
									switchType = 1,
									switchTo = 1,
									switchParam = 180
								}
							}
						},
						reinforceDuration = 180
					}
				},
				{
					triggerType = 0,
					waveIndex = 2002,
					conditionType = 1,
					preWaves = {
						100
					},
					triggerParam = {},
					spawn = {},
					reinforcement = {
						{
							monsterTemplateID = 16402009,
							moveCast = true,
							delay = 8,
							corrdinate = {
								0,
								0,
								26
							},
							buffList = {
								8001
							},
							phase = {
								{
									switchParam = 8,
									dive = "STATE_RAID",
									switchTo = 1,
									index = 0,
									switchType = 1,
									setAI = 20021
								},
								{
									switchParam = 5,
									dive = "STATE_FLOAT",
									switchTo = 2,
									index = 1,
									switchType = 1,
									setAI = 20006,
									addBuff = {
										8976
									}
								},
								{
									switchParam = 8,
									dive = "STATE_RAID",
									switchTo = 1,
									index = 2,
									switchType = 1,
									setAI = 20006,
									removeBuff = {
										8976
									}
								}
							}
						},
						{
							monsterTemplateID = 16402009,
							moveCast = true,
							delay = 8,
							corrdinate = {
								0,
								0,
								76
							},
							buffList = {
								8001
							},
							phase = {
								{
									switchParam = 8,
									dive = "STATE_RAID",
									switchTo = 1,
									index = 0,
									switchType = 1,
									setAI = 20021
								},
								{
									switchParam = 5,
									dive = "STATE_FLOAT",
									switchTo = 2,
									index = 1,
									switchType = 1,
									setAI = 20006,
									addBuff = {
										8976
									}
								},
								{
									switchParam = 8,
									dive = "STATE_RAID",
									switchTo = 1,
									index = 2,
									switchType = 1,
									setAI = 20006,
									removeBuff = {
										8976
									}
								}
							}
						},
						reinforceDuration = 180
					}
				},
				{
					triggerType = 0,
					waveIndex = 2003,
					conditionType = 1,
					preWaves = {
						100
					},
					triggerParam = {},
					spawn = {},
					reinforcement = {
						{
							monsterTemplateID = 16402008,
							delay = 4,
							corrdinate = {
								18,
								0,
								70
							},
							buffList = {
								8001
							},
							phase = {
								{
									switchParam = 6,
									dive = "STATE_RAID",
									switchTo = 1,
									index = 0,
									switchType = 1,
									setAI = 20005
								},
								{
									switchParam = 300,
									dive = "STATE_FLOAT",
									switchTo = 0,
									index = 1,
									switchType = 1,
									addBuff = {
										8002,
										8976
									}
								}
							}
						},
						{
							monsterTemplateID = 16402008,
							delay = 4,
							corrdinate = {
								18,
								0,
								30
							},
							buffList = {
								8001
							},
							phase = {
								{
									switchParam = 6,
									dive = "STATE_RAID",
									switchTo = 1,
									index = 0,
									switchType = 1,
									setAI = 20005
								},
								{
									switchParam = 300,
									dive = "STATE_FLOAT",
									switchTo = 0,
									index = 1,
									switchType = 1,
									addBuff = {
										8002,
										8976
									}
								}
							}
						},
						reinforceDuration = 180
					}
				},
				{
					triggerType = 8,
					waveIndex = 900,
					preWaves = {
						101
					},
					triggerParams = {}
				}
			}
		}
	},
	fleet_prefab = {}
}
