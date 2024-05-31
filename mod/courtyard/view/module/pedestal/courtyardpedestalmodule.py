local var_0_0 = class("CourtYardPedestalModule", import("..CourtYardBaseModule"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.storey = arg_1_0.data
	arg_1_0.scrollView = arg_1_0._tf.parent.Find("scroll_view")
	arg_1_0.wallPaper = CourtYardPedestalWallPaper.New(arg_1_0)
	arg_1_0.floorPaper = CourtYardPedestalFloorPaper.New(arg_1_0)
	arg_1_0.road = CourtYardPedestalRoad.New(arg_1_0)
	arg_1_0.wallBase = CourtYardPedestalWallBase.New(arg_1_0)
	arg_1_0.msgBox = CourtYardExtendTipPage.New(arg_1_0)

def var_0_0.AddListeners(arg_2_0):
	arg_2_0.AddListener(CourtYardEvent.UPDATE_STOREY, arg_2_0.OnUpdate)
	arg_2_0.AddListener(CourtYardEvent.UPDATE_WALLPAPER, arg_2_0.OnWallPaperUpdate)
	arg_2_0.AddListener(CourtYardEvent.UPDATE_FLOORPAPER, arg_2_0.OnFloorPaperUpdate)

def var_0_0.RemoveListeners(arg_3_0):
	arg_3_0.RemoveListener(CourtYardEvent.UPDATE_STOREY, arg_3_0.OnUpdate)
	arg_3_0.RemoveListener(CourtYardEvent.UPDATE_WALLPAPER, arg_3_0.OnWallPaperUpdate)
	arg_3_0.RemoveListener(CourtYardEvent.UPDATE_FLOORPAPER, arg_3_0.OnFloorPaperUpdate)

def var_0_0.OnWallPaperUpdate(arg_4_0, arg_4_1):
	arg_4_0.wallPaper.Update(arg_4_1, arg_4_0.level)

def var_0_0.OnFloorPaperUpdate(arg_5_0, arg_5_1):
	arg_5_0.floorPaper.Update(arg_5_1, arg_5_0.level)

def var_0_0.OnUpdate(arg_6_0, arg_6_1):
	arg_6_0.level = arg_6_1

	arg_6_0.road.Update(arg_6_1)
	arg_6_0.wallBase.Update(arg_6_1)
	arg_6_0.InitScrollRect(arg_6_1)

def var_0_0.InitScrollRect(arg_7_0, arg_7_1):
	local var_7_0 = 1080 + (arg_7_1 - 1) * 150

	arg_7_0._tf.sizeDelta = Vector2(arg_7_0._tf.sizeDelta.x, var_7_0)

	scrollTo(arg_7_0.scrollView, 0.508, 0.655)

def var_0_0.OnDispose(arg_8_0):
	arg_8_0.msgBox.Destroy()

	arg_8_0.msgBox = None

	arg_8_0.wallPaper.Dispose()

	arg_8_0.wallPaper = None

	arg_8_0.floorPaper.Dispose()

	arg_8_0.floorPaper = None

	arg_8_0.road.Dispose()

	arg_8_0.road = None

	arg_8_0.wallBase.Dispose()

	arg_8_0.wallBase = None

return var_0_0
