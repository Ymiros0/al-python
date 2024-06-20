return {
	id = "NG0037",
	events = {
		{
			alpha = 0,
			ui = {
				def dynamicPath:()
					if getProxy(SettingsProxy).IsMellowStyle():
						return "/OverlayCamera/Overlay/UIMain/NewMainMellowTheme(Clone)/frame/left/list/MainUINewServerBtn4Mellow(Clone)"
					else
						return "OverlayCamera/Overlay/UIMain/NewMainClassicTheme(Clone)/frame/link_top/layout/MainUINewServerBtn(Clone)",
				triggerType = {
					1
				},
				fingerPos = {
					posY = -49.02,
					posX = 59.75
				}
			},
			style = {
				text = "Go to the Event",
				mode = 1,
				posY = 204.69,
				dir = -1,
				posX = -329.7
			}
		},
		{
			alpha = 0,
			style = {
				text = "Clear event missions and earn points to exchange for a variety of great rewards.",
				mode = 1,
				posY = -102.33,
				dir = -1,
				posX = -29.1
			}
		}
	}
}