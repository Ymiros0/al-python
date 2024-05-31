local var_0_0 = class("MainBannerView", import("...base.MainBaseView"))

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0.scrollSnap = BannerScrollRect.New(findTF(arg_1_1, "mask/content"), findTF(arg_1_1, "dots"))

def var_0_0.Init(arg_2_0):
	local var_2_0 = getProxy(ActivityProxy).getBannerDisplays()

	arg_2_0.UpdateItems(var_2_0)

	arg_2_0.banners = var_2_0

def var_0_0.Refresh(arg_3_0):
	local var_3_0 = getProxy(ActivityProxy).getBannerDisplays()

	if #arg_3_0.banners != #var_3_0:
		arg_3_0.Clear()
		arg_3_0.Init()
	else
		arg_3_0.scrollSnap.Resume()

def var_0_0.UpdateItems(arg_4_0, arg_4_1):
	for iter_4_0 = 0, #arg_4_1 - 1:
		local var_4_0 = arg_4_1[iter_4_0 + 1]
		local var_4_1 = arg_4_0.scrollSnap.AddChild()

		LoadImageSpriteAsync("activitybanner/" .. var_4_0.pic, var_4_1)

		local var_4_2 = var_4_0.type == 3 and tonumber(var_4_0.param) == None and getProxy(ActivityProxy).readyToAchieveByType(ActivityConst.ACTIVITY_TYPE_LEVELAWARD)

		setActive(findTF(var_4_1, "red"), var_4_2)
		onButton(arg_4_0, var_4_1, function()
			arg_4_0.Tracking(var_4_0.id)
			MainBaseActivityBtn.Skip(arg_4_0, var_4_0), SFX_MAIN)

	arg_4_0.scrollSnap.SetUp()

def var_0_0.Tracking(arg_6_0, arg_6_1):
	TrackConst.TrackingTouchBanner(arg_6_1)

def var_0_0.GetDirection(arg_7_0):
	return Vector2(1, 0)

def var_0_0.Disable(arg_8_0):
	arg_8_0.scrollSnap.Puase()

def var_0_0.Clear(arg_9_0):
	arg_9_0.scrollSnap.Reset()

def var_0_0.Dispose(arg_10_0):
	var_0_0.super.Dispose(arg_10_0)
	arg_10_0.Clear()
	arg_10_0.scrollSnap.Dispose()

	arg_10_0.scrollSnap = None

return var_0_0
