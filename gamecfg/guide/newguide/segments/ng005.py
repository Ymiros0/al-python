return {
	id = "NG005",
	events = {
		{
			ui = {
				def dynamicPath:()
					if getProxy(SettingsProxy).IsMellowStyle():
						return "/OverlayCamera/Overlay/UIMain/NewMainMellowTheme(Clone)/frame/bottom/frame/live"
					else
						return "/OverlayCamera/Overlay/UIMain/NewMainClassicTheme(Clone)/frame/bottom/liveButton"
			}
		},
		{
			ui = {
				def dynamicPath:()
					if USE_OLD_MAIN_LIVE_AREA_UI:
						return "/OverlayCamera/Overlay/UIMain/MainLiveAreaOldUI(Clone)/commander_btn"
					else
						return "/OverlayCamera/Overlay/UIMain/MainLiveAreaUI(Clone)/commander_btn"
			}
		}
	}
}
