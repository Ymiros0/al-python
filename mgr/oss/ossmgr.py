pg = pg or {}
pg.OSSMgr = singletonClass("OSSMgr")

local var_0_0 = pg.OSSMgr

def var_0_0.Ctor(arg_1_0):
	if PLATFORM_CODE == PLATFORM_CH:
		arg_1_0.instance = OSSStarter.ins

	arg_1_0.isIninted = False

	if arg_1_0.instance:
		ReflectionHelp.RefSetField(typeof("OSSStarter"), "debug", arg_1_0.instance, False)

def var_0_0.InitConfig(arg_2_0):
	if PLATFORM_CODE == PLATFORM_CH:
		OSS_STS_URL = ""
		OSS_ENDPOINT = "oss-cn-hangzhou.aliyuncs.com"
		OSSBUCKETNAME = "blhx-dorm-oss"

		local var_2_0 = pg.SdkMgr.GetInstance().GetChannelUID()
		local var_2_1 = var_2_0 == "cps" or var_2_0 == "yun" or var_2_0 == "0"

		if getProxy(UserProxy).GetCacheGatewayInServerLogined() == PLATFORM_IPHONEPLAYER:
			FOLDERNAME = "dorm_ios/"
		elif var_2_1:
			FOLDERNAME = "dorm_bili/"
		else
			FOLDERNAME = "dorm_uo/"

		print("FOLDERNAME. ", FOLDERNAME)
	elif PLATFORM_CODE == PLATFORM_US:
		OSS_STS_URL = ""
		OSS_ENDPOINT = "oss-us-east-1.aliyuncs.com"
		OSSBUCKETNAME = "blhx-photo"
		FOLDERNAME = "dorm_us/"
	elif PLATFORM_CODE == PLATFORM_CHT:
		OSS_STS_URL = ""
		OSS_ENDPOINT = "oss-ap-southeast-1.aliyuncs.com"
		OSSBUCKETNAME = "blhx-gameupload-sts"
		FOLDERNAME = "dorm_tw/"
	elif PLATFORM_CODE == PLATFORM_KR:
		OSS_STS_URL = ""
		OSS_ENDPOINT = "ap-northeast-2"
		OSSBUCKETNAME = "blhx-s3-houzhai-upload"
		FOLDERNAME = "dorm_kr/"
	elif PLATFORM_CODE == PLATFORM_JP:
		OSS_STS_URL = ""
		OSS_ENDPOINT = "ap-northeast-1"
		OSSBUCKETNAME = "blhx-dorm-jp"
		FOLDERNAME = "dorm_jp/"

def var_0_0.Init(arg_3_0):
	arg_3_0.InitConfig()

	if not arg_3_0.isIninted:
		arg_3_0.isIninted = True

		arg_3_0.InitClinet()

def var_0_0.InitClinet(arg_4_0, arg_4_1):
	if not arg_4_0.instance:
		return

	local var_4_0 = arg_4_0.instance.initMode

	local function var_4_1(arg_5_0, arg_5_1)
		arg_4_0.AddExpireTimer(arg_5_1)
		arg_4_0.instance.InitWithArgs(unpack(arg_5_0))

	pg.m02.sendNotification(GAME.GET_OSS_ARGS, {
		mode = var_4_0,
		callback = var_4_1
	})

def var_0_0.UpdateLoad(arg_6_0, arg_6_1, arg_6_2, arg_6_3):
	if not arg_6_0.instance:
		arg_6_3()

		return

	local var_6_0 = OSSBUCKETNAME

	arg_6_0.instance.UpdateLoad(var_6_0, FOLDERNAME .. arg_6_1, arg_6_2, arg_6_3)

def var_0_0.AsynUpdateLoad(arg_7_0, arg_7_1, arg_7_2, arg_7_3):
	if not arg_7_0.instance:
		arg_7_3()

		return

	local var_7_0 = OSSBUCKETNAME

	arg_7_0.instance.AsynUpdateLoad(var_7_0, FOLDERNAME .. arg_7_1, arg_7_2, arg_7_3)

def var_0_0.DeleteObject(arg_8_0, arg_8_1, arg_8_2):
	if not arg_8_0.instance:
		arg_8_2()

		return

	local var_8_0 = OSSBUCKETNAME

	arg_8_0.instance.DeleteObject(var_8_0, FOLDERNAME .. arg_8_1, arg_8_2)

def var_0_0.GetSprite(arg_9_0, arg_9_1, arg_9_2, arg_9_3, arg_9_4, arg_9_5, arg_9_6):
	if not arg_9_0.instance:
		arg_9_6()

		return

	local var_9_0 = OSSBUCKETNAME

	arg_9_0.instance.GetSprite(var_9_0, FOLDERNAME .. arg_9_1, arg_9_2, arg_9_3, arg_9_4, arg_9_5, arg_9_6)

def var_0_0.GetTexture2D(arg_10_0, arg_10_1, arg_10_2, arg_10_3, arg_10_4, arg_10_5, arg_10_6):
	if not arg_10_0.instance:
		arg_10_6()

		return

	local var_10_0 = OSSBUCKETNAME

	arg_10_0.instance.GetTexture(var_10_0, FOLDERNAME .. arg_10_1, arg_10_2, arg_10_3, arg_10_4, arg_10_5, arg_10_6)

def var_0_0.AddExpireTimer(arg_11_0, arg_11_1):
	arg_11_0.RemoveExpireTimer()

	if not arg_11_1 or arg_11_1 == 0:
		return

	local var_11_0 = arg_11_1 - pg.TimeMgr.GetInstance().GetServerTime()

	if var_11_0 <= 0:
		var_11_0 = 300

	print("expireTime. ", var_11_0)

	arg_11_0.timer = Timer.New(function()
		arg_11_0.InitClinet(), var_11_0, 1)

	arg_11_0.timer.Start()

def var_0_0.RemoveExpireTimer(arg_13_0):
	if arg_13_0.timer:
		arg_13_0.timer.Stop()

		arg_13_0.timer = None

def var_0_0.Dispose(arg_14_0):
	arg_14_0.RemoveExpireTimer()

return var_0_0
