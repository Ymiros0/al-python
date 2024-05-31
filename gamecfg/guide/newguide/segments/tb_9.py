return {
	id = "tb_9",
	isWorld = False,
	events = {
		{
			alpha = 0,
			style = {
				text = "You have unlocked a new location.",
				mode = 2,
				dir = -1,
				char = 1,
				posY = -108.2,
				posX = 441.1,
				uiset = {}
			}
		},
		{
			alpha = 0.4,
			style = {
				text = "Tap the Go Outside button.",
				mode = 2,
				dir = -1,
				char = 1,
				posY = 0,
				posX = 0,
				uiset = {}
			},
			ui = {
				path = "OverlayCamera/Overlay/UIMain/blur_panel/bottom/right/EducateBottomPanel(Clone)/content/btns/map",
				pathIndex = -1,
				fingerPos = {
					posY = 48.24,
					posX = -91.3
				}
			}
		},
		{
			alpha = 0.4,
			style = {
				text = "Let's go to the newly unlocked Trendy Market.",
				mode = 2,
				dir = 1,
				char = 1,
				posY = -320.7,
				posX = -339.2,
				uiset = {}
			},
			ui = {
				path = "UICamera/Canvas/UIMain/EducateMapUI(Clone)/map/content/130",
				pathIndex = -1,
				fingerPos = {
					posY = -14,
					posX = 40.3
				}
			}
		},
		{
			alpha = 0.4,
			style = {
				text = "Tap the Photo Studio button.",
				mode = 2,
				dir = 1,
				char = 1,
				posY = -266.23,
				posX = 0,
				uiset = {}
			},
			ui = {
				path = "OverlayCamera/Overlay/UIMain/EducateSiteDetailUI(Clone)/anim_root/window/options/content/2",
				pathIndex = -1,
				fingerPos = {
					posY = -44.62,
					posX = 163.7
				}
			}
		},
		{
			delay = 0.5,
			alpha = 0,
			style = {
				text = "Here, you can take all sorts of themed photos, which will affect TB's personality.",
				mode = 2,
				posY = -146.2,
				char = 1,
				dir = 1,
				posX = 48.74
			}
		},
		{
			alpha = 0.4,
			style = {
				text = "Taking TB to watch different plays at Seaside Park's Stellar Stage will also affect TB's personality.",
				mode = 2,
				dir = -1,
				char = 1,
				posY = -67.43,
				posX = -516.04,
				uiset = {
					{
						lineMode = 2,
						path = "UICamera/Canvas/UIMain/EducateMapUI(Clone)/map/content/140",
						pathIndex = -1
					}
				}
			}
		}
	}
}
