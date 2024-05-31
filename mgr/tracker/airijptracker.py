local var_0_0 = class("AiriJPTracker")

def var_0_0.Ctor(arg_1_0):
	arg_1_0.mapping = {
		[TRACKING_ROLE_CREATE] = "role_create",
		[TRACKING_ROLE_LOGIN] = "role_login",
		[TRACKING_TUTORIAL_COMPLETE_1] = "tutorial_complete_1",
		[TRACKING_TUTORIAL_COMPLETE_2] = "tutorial_complete_2",
		[TRACKING_TUTORIAL_COMPLETE_3] = "tutorial_complete_3",
		[TRACKING_TUTORIAL_COMPLETE_4] = "tutorial_complete_4",
		[TRACKING_USER_LEVELUP] = "user_levelup",
		[TRACKING_ROLE_LOGOUT] = "role_logout",
		[TRACKING_PURCHASE_FIRST] = "purchase_first",
		[TRACKING_PURCHASE_CLICK] = "purchase_click",
		[TRACKING_PURCHASE_CLICK_MONTHLYCARD] = "purchase_click_monthlycard",
		[TRACKING_PURCHASE_CLICK_GIFTBAG] = "purchase_click_giftbag",
		[TRACKING_PURCHASE_CLICK_DIAMOND] = "purchase_click_diamond",
		[TRACKING_2D_RETENTION] = "2d_retention",
		[TRACKING_7D_RETENTION] = "7d_retention",
		[TRACKING_BUILD_SHIP] = "construct",
		[TRACKING_SHIP_INTENSIFY] = "strengthen",
		[TRACKING_SHIP_LEVEL_UP] = "levelup",
		[TRACKING_SHIP_HIGHEST_LEVEL] = "character_Max_level",
		[TRACKING_CUBE_ADD] = "cube_acquisition",
		[TRACKING_CUBE_CONSUME] = "cube_Consumption",
		[TRACKING_USER_LEVEL_THIRTY] = "level_30",
		[TRACKING_USER_LEVEL_FORTY] = "level_40",
		[TRACKING_PROPOSE_SHIP] = "married",
		[TRACKING_REMOULD_SHIP] = "remodeled",
		[TRACKING_HARD_CHAPTER] = "hard_clear",
		[TRACKING_KILL_BOSS] = "stage_laps",
		[TRACKING_HIGHEST_CHAPTER] = "stage",
		[TRACKING_FIRST_PASS_3_4] = "3-4_clear",
		[TRACKING_FIRST_PASS_4_4] = "4-4_clear",
		[TRACKING_FIRST_PASS_5_4] = "5-4_clear",
		[TRACKING_FIRST_PASS_6_4] = "6-4_clear",
		[TRACKING_FIRST_PASS_12_4] = "12-4_clear",
		[TRACKING_FIRST_PASS_13_1] = "13-1_clear",
		[TRACKING_FIRST_PASS_13_2] = "13-2_clear",
		[TRACKING_FIRST_PASS_13_3] = "13-3_clear",
		[TRACKING_FIRST_PASS_13_4] = "13-4_clear",
		[TRACKING_CLASS_LEVEL_UP_8] = "auditoriumLV_8",
		[TRACKING_CLASS_LEVEL_UP_9] = "auditoriumLV_9",
		[TRACKING_CLASS_LEVEL_UP_10] = "auditoriumLV_10"
	}

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
	elif arg_2_1 == TRACKING_BUILD_SHIP:
		local var_2_5 = AiriUserEvent.New(var_2_0)

		var_2_5.AddParam("user_id", arg_2_2)
		var_2_5.AddParam("Cons_Num", arg_2_3)
		pg.SdkMgr.GetInstance().UserEventUpload(var_2_5)
	elif arg_2_1 == TRACKING_SHIP_INTENSIFY:
		local var_2_6 = AiriUserEvent.New(var_2_0)

		var_2_6.AddParam("user_id", arg_2_2)
		var_2_6.AddParam("Cost_Num", arg_2_3)
		pg.SdkMgr.GetInstance().UserEventUpload(var_2_6)
	elif arg_2_1 == TRACKING_SHIP_LEVEL_UP:
		local var_2_7 = AiriUserEvent.New(var_2_0)

		var_2_7.AddParam("user_id", arg_2_2)
		var_2_7.AddParam("Lvup_Num", arg_2_3)
		pg.SdkMgr.GetInstance().UserEventUpload(var_2_7)
	elif arg_2_1 == TRACKING_SHIP_HIGHEST_LEVEL:
		local var_2_8 = AiriUserEvent.New(var_2_0)

		var_2_8.AddParam("user_id", arg_2_2)
		var_2_8.AddParam("Ship_Max_level", arg_2_3)
		pg.SdkMgr.GetInstance().UserEventUpload(var_2_8)
	elif arg_2_1 == TRACKING_CUBE_ADD:
		local var_2_9 = AiriUserEvent.New(var_2_0)

		var_2_9.AddParam("user_id", arg_2_2)
		var_2_9.AddParam("Aqui_Num", arg_2_3)
		pg.SdkMgr.GetInstance().UserEventUpload(var_2_9)
	elif arg_2_1 == TRACKING_CUBE_CONSUME:
		local var_2_10 = AiriUserEvent.New(var_2_0)

		var_2_10.AddParam("user_id", arg_2_2)
		var_2_10.AddParam("Consum_Num", arg_2_3)
		pg.SdkMgr.GetInstance().UserEventUpload(var_2_10)
	elif arg_2_1 == TRACKING_PROPOSE_SHIP:
		local var_2_11 = AiriUserEvent.New(var_2_0)

		var_2_11.AddParam("user_id", arg_2_2)
		var_2_11.AddParam("Married_Id", arg_2_3)
		pg.SdkMgr.GetInstance().UserEventUpload(var_2_11)
	elif arg_2_1 == TRACKING_REMOULD_SHIP:
		local var_2_12 = AiriUserEvent.New(var_2_0)

		var_2_12.AddParam("user_id", arg_2_2)
		var_2_12.AddParam("Remodel_Id", arg_2_3)
		pg.SdkMgr.GetInstance().UserEventUpload(var_2_12)
	elif arg_2_1 == TRACKING_HARD_CHAPTER:
		local var_2_13 = AiriUserEvent.New(var_2_0)

		var_2_13.AddParam("user_id", arg_2_2)
		var_2_13.AddParam("Clear_Stage_Id", arg_2_3)
		pg.SdkMgr.GetInstance().UserEventUpload(var_2_13)
	elif arg_2_1 == TRACKING_HIGHEST_CHAPTER:
		local var_2_14 = AiriUserEvent.New(var_2_0)

		var_2_14.AddParam("user_id", arg_2_2)
		var_2_14.AddParam("Clear_Stage_Id", arg_2_3)
		pg.SdkMgr.GetInstance().UserEventUpload(var_2_14)
	else
		local var_2_15 = AiriUserEvent.New(var_2_0)

		var_2_15.AddParam("user_id", arg_2_2)
		pg.SdkMgr.GetInstance().UserEventUpload(var_2_15)

return var_0_0
