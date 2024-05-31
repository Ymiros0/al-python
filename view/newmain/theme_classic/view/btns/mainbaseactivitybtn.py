local var_0_0 = class("MainBaseActivityBtn")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	arg_1_0.tpl = arg_1_1

	pg.DelegateInfo.New(arg_1_0)

	arg_1_0.event = arg_1_2

	if arg_1_3:
		arg_1_0._tf = arg_1_0.tpl

def var_0_0.GetLinkConfig(arg_2_0):
	local var_2_0 = arg_2_0.GetEventName()
	local var_2_1 = pg.activity_link_button
	local var_2_2 = var_2_1.get_id_list_by_name[var_2_0] or {}
	local var_2_3 = _.select(var_2_2, function(arg_3_0)
		local var_3_0 = var_2_1[arg_3_0].time

		if type(var_3_0) == "table" and var_3_0[1] and var_3_0[1] == "default":
			return arg_2_0.InActTime(var_3_0[2])
		else
			return pg.TimeMgr.GetInstance().inTime(var_3_0))

	if #var_2_3 > 0:
		table.sort(var_2_3, function(arg_4_0, arg_4_1)
			return var_2_1[arg_4_0].order < var_2_1[arg_4_1].order)

		return var_2_1[var_2_3[1]]

def var_0_0.InActTime(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_1 or arg_5_0.GetActivityID()

	if var_5_0:
		local var_5_1 = getProxy(ActivityProxy).getActivityById(var_5_0)

		return var_5_1 and not var_5_1.isEnd()

	return False

def var_0_0.InShowTime(arg_6_0):
	local var_6_0 = arg_6_0.GetLinkConfig()

	if var_6_0 != None:
		arg_6_0.config = var_6_0

		return True
	else
		return False

def var_0_0.NewGameObject(arg_7_0):
	return arg_7_0._tf or Object.Instantiate(arg_7_0.tpl, arg_7_0.tpl.parent).transform

def var_0_0.Init(arg_8_0, arg_8_1):
	arg_8_0._tf = arg_8_0.NewGameObject()
	arg_8_0._tf.gameObject.name = arg_8_0.__cname
	arg_8_0.image = arg_8_0._tf.Find("Image").GetComponent(typeof(Image))
	arg_8_0.subImage = arg_8_0._tf.Find("sub_Image").GetComponent(typeof(Image))
	arg_8_0.tipTr = arg_8_0._tf.Find("Tip").GetComponent(typeof(Image))
	arg_8_0.tipTxt = arg_8_0._tf.Find("Tip/Text").GetComponent(typeof(Text))

	setActive(arg_8_0._tf, True)

	arg_8_0.tipTxt.text = ""

	arg_8_0.InitTipImage()
	arg_8_0.UpdatePosition(arg_8_1)
	arg_8_0.InitSubImage()
	arg_8_0.InitImage(function()
		arg_8_0.OnInit()
		arg_8_0.Register())

def var_0_0.Register(arg_10_0):
	onButton(arg_10_0, arg_10_0._tf, function()
		if arg_10_0.config.type <= 0:
			arg_10_0.CustomOnClick()
		else
			arg_10_0.OnClick(), SFX_MAIN)

def var_0_0.OnClick(arg_12_0):
	var_0_0.Skip(arg_12_0, arg_12_0.config)

def var_0_0.InitImage(arg_13_0, arg_13_1):
	local var_13_0 = arg_13_0.config.pic

	if not var_13_0 or var_13_0 == arg_13_0.imgName:
		arg_13_1()

		return

	LoadSpriteAtlasAsync(arg_13_0.ResPath() .. "/" .. var_13_0, "", function(arg_14_0)
		arg_13_0.imgName = var_13_0
		arg_13_0.image.sprite = arg_14_0

		arg_13_0.image.SetNativeSize()
		arg_13_1())

def var_0_0.InitSubImage(arg_15_0):
	local var_15_0 = arg_15_0.config.text_pic

	setActive(arg_15_0.subImage.gameObject, var_15_0 != None and var_15_0 != "")

	if not var_15_0 or var_15_0 == arg_15_0.subImgName:
		return

	LoadSpriteAtlasAsync(arg_15_0.ResPath() .. "/" .. var_15_0, "", function(arg_16_0)
		arg_15_0.subImgName = var_15_0
		arg_15_0.subImage.sprite = arg_16_0

		arg_15_0.subImage.SetNativeSize())

def var_0_0.GetTipImage(arg_17_0):
	return "tip"

def var_0_0.InitTipImage(arg_18_0):
	local var_18_0 = arg_18_0.GetTipImage()

	if not var_18_0 or var_18_0 == arg_18_0.tipImageName:
		return

	LoadSpriteAtlasAsync("LinkButton/" .. var_18_0, "", function(arg_19_0)
		arg_18_0.tipImageName = var_18_0
		arg_18_0.tipTr.sprite = arg_19_0

		arg_18_0.tipTr.SetNativeSize())

def var_0_0.UpdatePosition(arg_20_0, arg_20_1):
	local var_20_0 = -20
	local var_20_1 = -150 - (arg_20_1 - 1) * (arg_20_0._tf.sizeDelta.y + var_20_0)

	arg_20_0._tf.anchoredPosition = Vector2(arg_20_0._tf.anchoredPosition.x, var_20_1, 0)

def var_0_0.Clear(arg_21_0):
	if arg_21_0._tf:
		setActive(arg_21_0._tf, False)

def var_0_0.emit(arg_22_0, ...):
	arg_22_0.event.emit(...)

def var_0_0.Dispose(arg_23_0):
	pg.DelegateInfo.Dispose(arg_23_0)

	if arg_23_0._tf:
		Destroy(arg_23_0._tf.gameObject)

		arg_23_0._tf = None

def var_0_0.Skip(arg_24_0, arg_24_1):
	if arg_24_1.type == GAMEUI_BANNER_1:
		Application.OpenURL(arg_24_1.param)
	elif arg_24_1.type == GAMEUI_BANNER_2:
		arg_24_0.emit(NewMainMediator.SKIP_SCENE, arg_24_1.param)
	elif arg_24_1.type == GAMEUI_BANNER_3:
		arg_24_0.emit(NewMainMediator.SKIP_ACTIVITY, tonumber(arg_24_1.param))
	elif arg_24_1.type == GAMEUI_BANNER_4:
		arg_24_0.emit(NewMainMediator.SKIP_SHOP, arg_24_1.param)
	elif arg_24_1.type == GAMEUI_BANNER_5:
		-- block empty
	elif arg_24_1.type == GAMEUI_BANNER_6:
		arg_24_0.emit(NewMainMediator.GO_SCENE, SCENE.SELTECHNOLOGY)
	elif arg_24_1.type == GAMEUI_BANNER_7:
		arg_24_0.emit(NewMainMediator.GO_MINI_GAME, arg_24_1.param[1])
	elif arg_24_1.type == GAMEUI_BANNER_8:
		if getProxy(GuildProxy).getRawData():
			arg_24_0.emit(NewMainMediator.GO_SCENE, SCENE.GUILD)
		else
			arg_24_0.emit(NewMainMediator.GO_SCENE, SCENE.NEWGUILD)

def var_0_0.ResPath(arg_25_0):
	return "LinkButton"

def var_0_0.GetActivityID(arg_26_0):
	assert(False, "策划配置default类型 必须重写这个方法")

def var_0_0.CustomOnClick(arg_27_0):
	assert(False, "策划配置type = 0 这个按钮必须自己定义跳转行为")

def var_0_0.GetEventName(arg_28_0):
	assert(False, "overwrite me !!!")

def var_0_0.OnInit(arg_29_0):
	return

return var_0_0
