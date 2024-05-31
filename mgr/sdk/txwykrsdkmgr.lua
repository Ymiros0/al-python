local var_0_0 = {}
local var_0_1 = TxwyKrSdkMgr.inst

function var_0_0.CheckPretest()
	return NetConst.GATEWAY_HOST == "bl-kr-test.xdg.com" and NetConst.GATEWAY_PORT == 30001 or IsUnityEditor
end

function var_0_0.GoSDkLoginScene()
	var_0_1:GoLoginScene()
end

function var_0_0.LoginSdk(arg_3_0)
	var_0_1:Login(0)
end

function var_0_0.SdkGateWayLogined()
	var_0_1:OnGatewayLogined()
end

function var_0_0.SdkLoginGetaWayFailed()
	var_0_1:OnLoginGatewayFailed()
end

function var_0_0.LogoutSDK()
	var_0_1:LocalLogout()
end

function var_0_0.EnterServer(arg_7_0, arg_7_1, arg_7_2, arg_7_3, arg_7_4, arg_7_5, arg_7_6)
	var_0_1:EnterServer(arg_7_0, arg_7_1, arg_7_2, arg_7_3, arg_7_4 * 1000, arg_7_5, "vip0", arg_7_6)
end

function var_0_0.SdkLevelUp(arg_8_0, arg_8_1)
	var_0_1:LevelUp(arg_8_1, arg_8_0)
end

function var_0_0.UserCenter()
	local var_9_0 = getProxy(PlayerProxy)
	local var_9_1 = "未登入"

	if var_9_0 then
		var_9_1 = var_9_0:getData().name
	end

	local var_9_2 = BundleWizard.Inst:GetGroupMgr("DEFAULT_RES").CurrentVersion:ToString()

	var_0_1:UserCenter(var_9_1, var_9_2, "1")
end

function var_0_0.BugReport()
	local var_10_0 = getProxy(UserProxy):getData()
	local var_10_1 = getProxy(ServerProxy):getLastServer(var_10_0.uid)
	local var_10_2 = getProxy(PlayerProxy)
	local var_10_3 = ""

	if var_10_2 then
		var_10_3 = var_10_2:getData().name
	end

	local var_10_4 = BundleWizard.Inst:GetGroupMgr("DEFAULT_RES").CurrentVersion:ToString()

	var_0_1:BugReport(var_10_3, var_10_4, var_10_1.id)
end

function var_0_0.StoreReview()
	var_0_1:StoreReview()
end

function var_0_0.ShareImg(arg_12_0, arg_12_1)
	var_0_1:ShareImg(arg_12_0, arg_12_1)
end

function var_0_0.CompletedTutorial()
	var_0_1:CompletedTutorial()
end

function var_0_0.UnlockAchievement()
	var_0_1:UnlockAchievement()
end

function var_0_0.QueryWithProduct()
	local function var_15_0()
		local var_16_0 = ""

		for iter_16_0, iter_16_1 in ipairs(pg.pay_data_display.all) do
			local var_16_1 = pg.pay_data_display[iter_16_1]

			var_16_0 = var_16_0 .. var_16_1.id_str .. ";"
		end

		return var_16_0
	end

	local function var_15_1(arg_17_0, arg_17_1)
		for iter_17_0, iter_17_1 in ipairs(pg.pay_data_display.all) do
			local var_17_0 = pg.pay_data_display[iter_17_1]

			if var_17_0.id_str == arg_17_0 and var_17_0.money ~= arg_17_1 then
				originalPrint(string.format("<color=#ff0000>%s的商品价格和本地的价格不同</color> 本地价格：%s, 服务器价格：%s", var_17_0.name, var_17_0.money, arg_17_1))
			end
		end
	end

	var_0_1:QueryWithProduct(var_15_0(), function(arg_18_0)
		local var_18_0 = string.split(arg_18_0, ";")

		for iter_18_0, iter_18_1 in ipairs(var_18_0) do
			local var_18_1 = string.split(iter_18_1, "|")
			local var_18_2 = var_18_1[1]
			local var_18_3 = var_18_1[2]

			var_15_1(var_18_2, var_18_3)
		end
	end)
end

function var_0_0.SdkPay(arg_19_0, arg_19_1, arg_19_2, arg_19_3, arg_19_4, arg_19_5, arg_19_6, arg_19_7, arg_19_8, arg_19_9)
	local var_19_0 = getProxy(PlayerProxy):getRawData().level

	var_0_1:Pay(arg_19_0, arg_19_1, arg_19_2, arg_19_3, arg_19_4, arg_19_5, arg_19_6, arg_19_7, var_19_0)
end

function var_0_0.BindCPU()
	var_0_1:callSdkApi("bindCpu", nil)
end

function var_0_0.SwitchAccount()
	var_0_1:SwitchAccount()
end

function var_0_0.GetBiliServerId()
	local var_22_0 = var_0_1.serverId

	originalPrint("serverId : " .. var_22_0)

	return var_22_0
end

function var_0_0.GetChannelUID()
	local var_23_0 = var_0_1.channelUID

	originalPrint("channelUID : " .. var_23_0)

	return var_23_0
end

function var_0_0.GetLoginType()
	return var_0_1.loginType
end

function var_0_0.GetIsPlatform()
	return var_0_1.isPlatform
end

function var_0_0.GetDeviceModel()
	return var_0_1:GetDeviceModel()
end

function var_0_0.OnAndoridBackPress()
	PressBack()
end

function GoLoginScene()
	if not pg.m02 then
		originalPrint("game is not start")

		return
	end

	pg.m02:sendNotification(GAME.GO_SCENE, SCENE.LOGIN)
	gcAll()
end

function SDKLogined(arg_29_0, arg_29_1, arg_29_2, arg_29_3)
	if not pg.m02 then
		originalPrint("game is not start")

		return
	end

	local var_29_0 = User.New({
		type = 1,
		arg1 = arg_29_0,
		arg2 = arg_29_1,
		arg3 = arg_29_2,
		arg4 = arg_29_3
	})

	pg.m02:sendNotification(GAME.PLATFORM_LOGIN_DONE, {
		user = var_29_0
	})
end

function SDKLogouted(arg_30_0)
	if not pg.m02 then
		originalPrint("game is not start")

		return
	end

	pg.m02:sendNotification(GAME.LOGOUT, {
		code = arg_30_0
	})
end

function PaySuccess(arg_31_0, arg_31_1)
	if not pg.m02 then
		originalPrint("game is not start")

		return
	end

	getProxy(ShopsProxy):removeWaitTimer()
end

function PayFailed(arg_32_0, arg_32_1)
	getProxy(ShopsProxy):removeWaitTimer()

	arg_32_1 = tonumber(arg_32_1)

	if not arg_32_1 then
		return
	end

	pg.m02:sendNotification(GAME.CHARGE_FAILED, {
		payId = arg_32_0,
		code = arg_32_1
	})

	if arg_32_1 == -202 then
		pg.TipsMgr.GetInstance():ShowTips(i18n("pay_cancel") .. arg_32_1)
	end
end

return var_0_0
