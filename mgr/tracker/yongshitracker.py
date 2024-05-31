local var_0_0 = class("YongshiTracker")

def var_0_0.Ctor(arg_1_0):
	arg_1_0.mapping = {}
	arg_1_0.mapping[TRACKING_ROLE_CREATE] = "role_create"
	arg_1_0.mapping[TRACKING_ROLE_LOGIN] = "role_login"
	arg_1_0.mapping[TRACKING_TUTORIAL_COMPLETE_1] = "tutorial_complete_1"
	arg_1_0.mapping[TRACKING_TUTORIAL_COMPLETE_2] = "tutorial_complete_2"
	arg_1_0.mapping[TRACKING_TUTORIAL_COMPLETE_3] = "tutorial_complete_3"
	arg_1_0.mapping[TRACKING_TUTORIAL_COMPLETE_4] = "tutorial_complete_4"
	arg_1_0.mapping[TRACKING_USER_LEVELUP] = "user_levelup"
	arg_1_0.mapping[TRACKING_ROLE_LOGOUT] = "role_logout"
	arg_1_0.mapping[TRACKING_PURCHASE_FIRST] = "purchase_first"
	arg_1_0.mapping[TRACKING_PURCHASE_CLICK] = "purchase_click"
	arg_1_0.mapping[TRACKING_PURCHASE_CLICK_MONTHLYCARD] = "purchase_click_monthlycard"
	arg_1_0.mapping[TRACKING_PURCHASE_CLICK_GIFTBAG] = "purchase_click_giftbag"
	arg_1_0.mapping[TRACKING_PURCHASE_CLICK_DIAMOND] = "purchase_click_diamond"
	arg_1_0.mapping[TRACKING_2D_RETENTION] = "2d_retention"
	arg_1_0.mapping[TRACKING_7D_RETENTION] = "7d_retention"

def var_0_0.Tracking(arg_2_0, arg_2_1, arg_2_2, arg_2_3):
	local var_2_0 = arg_2_0.mapping[arg_2_1]

	if var_2_0 == None:
		return

	if arg_2_1 == TRACKING_USER_LEVELUP:
		originalPrint("tracking lvl." .. arg_2_3)

		local var_2_1 = AiriUserEvent.New(var_2_0)

		var_2_1.AddParam("lvl", arg_2_3)
		var_2_1.AddParam("user_id", arg_2_2)
		pg.SdkMgr.GetInstance().UserEventUpload(var_2_1)
	elif arg_2_1 == TRACKING_PURCHASE_CLICK:
		local var_2_2 = AiriUserEvent.New(var_2_0)

		var_2_2.AddParam("user_id", arg_2_2)
		pg.SdkMgr.GetInstance().UserEventUpload(var_2_2)
	elif arg_2_1 == TRACKING_PURCHASE_FIRST:
		originalPrint("order id . " .. arg_2_3)

		local var_2_3 = AiriUserEvent.New(var_2_0)

		var_2_3.AddParam("user_id", arg_2_2)
		var_2_3.AddParam("order_id", arg_2_3)
		pg.SdkMgr.GetInstance().UserEventUpload(var_2_3)
	elif arg_2_1 == TRACKING_2D_RETENTION or arg_2_1 == TRACKING_7D_RETENTION:
		local var_2_4 = AiriUserEvent.New(var_2_0)

		var_2_4.AddParam("user_id", arg_2_2)
		pg.SdkMgr.GetInstance().UserEventUpload(var_2_4)
	elif arg_2_1 == TRACKING_ROLE_LOGIN:
		local var_2_5 = AiriUserEvent.New(var_2_0)

		var_2_5.AddParam("user_id", arg_2_2)
		var_2_5.AddParam("airi_uid", pg.SdkMgr.GetInstance().airi_uid)
		pg.SdkMgr.GetInstance().UserEventUpload(var_2_5)
	else
		local var_2_6 = AiriUserEvent.New(var_2_0)

		var_2_6.AddParam("user_id", arg_2_2)
		pg.SdkMgr.GetInstance().UserEventUpload(var_2_6)

return var_0_0
