local var_0_0 = {
	"Our next mission is to support the Eagles' aviation fleet combat drills. Tap <color=#ff7d36>Attack</color> to get started.",
	"Feeling like you need more firepower? Let's <color=#ff7d36>retreat for now</color> and head back to port!",
	"Tap <color=#ff7d36>retreat</color>.",
	"Yes, yes... This is just a tactical retreat!"
}

return {
	id = "S009",
	events = {
		{
			alpha = 0.35,
			style = {
				dir = 1,
				mode = 2,
				posY = 0,
				posX = 0,
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
					posY = -28.31,
					posX = 19.34
				}
			},
			code = {
				2
			}
		},
		{
			alpha = 0.239,
			waitScene = "LevelScene",
			style = {
				dir = -1,
				mode = 2,
				posY = 0,
				posX = 0,
				text = var_0_0[2]
			}
		},
		{
			alpha = 0.326,
			style = {
				dir = -1,
				mode = 2,
				posY = 0,
				posX = 0,
				text = var_0_0[3]
			},
			ui = {
				path = "/OverlayCamera/Overlay/UIMain/top/LevelStageView(Clone)/bottom_stage/Normal/retreat_button",
				pathIndex = -1,
				triggerType = {
					1
				},
				fingerPos = {
					posY = -32.82,
					posX = 11.94
				}
			}
		},
		{
			alpha = 0.289,
			style = {
				dir = -1,
				mode = 2,
				posY = 104.45,
				posX = 203.04,
				text = var_0_0[4]
			},
			ui = {
				path = "OverlayCamera/Overlay/UIMain/Msgbox(Clone)/window/button_container/custom_button_1(Clone)",
				pathIndex = -1,
				triggerType = {
					1
				},
				fingerPos = {
					posY = -28.02,
					posX = 53.3
				}
			}
		}
	}
}
