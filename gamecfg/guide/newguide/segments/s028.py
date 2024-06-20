local var_0_0 = {
	"Commander, please Tap <color=#ff7d36>Attack</color>",
	"Enemy flagship ahead! Tap the target to continue moving!",
	"Tap <color=#ff7d36>Battle</color> to start the battle!"
}

return {
	id = "S028",
	events = {
		{
			alpha = 0.454,
			style = {
				dir = 1,
				mode = 2,
				posY = -42,
				posX = 243,
				text = var_0_0[1]
			},
			ui = {
				pathIndex = -1,
				def dynamicPath:()
					if getProxy(SettingsProxy).IsMellowStyle():
						return "/OverlayCamera/Overlay/UIMain/NewMainMellowTheme(Clone)/frame/right/1/battle"
					else
						return "/OverlayCamera/Overlay/UIMain/NewMainClassicTheme(Clone)/frame/right/combatBtn",
				triggerType = {
					1
				},
				fingerPos = {
					posY = -19.7,
					posX = 88.9
				}
			},
			code = {
				2
			}
		},
		{
			alpha = 0.211,
			style = {
				dir = 1,
				mode = 2,
				posY = 171.89,
				posX = 32.25,
				text = var_0_0[2]
			},
			baseui = {
				path = "/LevelCamera/Canvas/UIMain/LevelGrid/DragLayer/plane/cells/chapter_cell_4_7/attachment",
				pathIndex = 0
			},
			ui = {
				path = "/LevelCamera/Canvas/UIMain/LevelGrid/DragLayer/plane/cells/chapter_cell_4_7/attachment",
				eventPath = "LevelCamera/Canvas/UIMain/LevelGrid/DragLayer/plane/quads/chapter_cell_quad_4_7",
				isLevelPoint = True,
				delay = 0.8,
				scale = 1.8,
				pathIndex = -1,
				triggerType = {
					1
				},
				fingerPos = {
					posY = -20,
					posX = 50
				}
			},
			code = {
				2,
				4
			}
		},
		{
			alpha = 0.409,
			style = {
				dir = 1,
				mode = 2,
				posY = -68.93,
				posX = 241.87,
				text = var_0_0[3]
			},
			ui = {
				path = "/OverlayCamera/Overlay/UIMain/ChapterPreCombatUI(Clone)/right/start",
				pathIndex = -1,
				triggerType = {
					1
				},
				fingerPos = {
					posY = -30.21,
					posX = 116.3
				}
			}
		}
	}
}