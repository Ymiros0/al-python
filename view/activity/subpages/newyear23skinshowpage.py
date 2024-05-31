local var_0_0 = class("NewYear23SkinShowPage", import("...base.BaseActivityPage"))

def var_0_0.OnLoaded(arg_1_0):
	return

def var_0_0.OnInit(arg_2_0):
	arg_2_0.goBtn = arg_2_0.findTF("BtnGO")
	arg_2_0.skinShopBtn = arg_2_0.findTF("BtnShop")

	onButton(arg_2_0, arg_2_0.skinShopBtn, function()
		arg_2_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.SKINSHOP), SFX_PANEL)
	onButton(arg_2_0, arg_2_0.goBtn, function()
		arg_2_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.NEWYEAR_BACKHILL_2023), SFX_PANEL)

	arg_2_0.rtBg = arg_2_0._tf.Find("AD")
	arg_2_0.rtFront = arg_2_0.rtBg.Find("front")

def var_0_0.OnDataSetting(arg_5_0):
	local var_5_0 = pg.TimeMgr.GetInstance()

	arg_5_0.showList = {}

	for iter_5_0, iter_5_1 in ipairs(arg_5_0.activity.getConfig("config_client").display_link):
		if iter_5_1[2] == 0 or var_5_0.inTime(pg.shop_template[iter_5_1[2]].time):
			table.insert(arg_5_0.showList, math.random(#arg_5_0.showList + 1), iter_5_1[1])

def var_0_0.OnFirstFlush(arg_6_0):
	arg_6_0.ActionInvoke("ShowOrHide", False)

	arg_6_0.index = 1

	GetSpriteFromAtlasAsync("clutter/newyear23skinshowpage_" .. arg_6_0.showList[arg_6_0.index], "", function(arg_7_0)
		if arg_6_0._state == var_0_0.STATES.DESTROY:
			return

		setImageSprite(arg_6_0.rtBg, arg_7_0)
		setImageAlpha(arg_6_0.rtFront, 0)
		arg_6_0.ActionInvoke("ShowOrHide", True)
		arg_6_0.DelayCall())

def var_0_0.DelayCall(arg_8_0):
	local var_8_0 = {}

	table.insert(var_8_0, function(arg_9_0)
		arg_8_0.uniqueId = LeanTween.delayedCall(3, System.Action(arg_9_0)).uniqueId)
	table.insert(var_8_0, function(arg_10_0)
		arg_8_0.index = arg_8_0.index % #arg_8_0.showList + 1

		GetSpriteFromAtlasAsync("clutter/newyear23skinshowpage_" .. arg_8_0.showList[arg_8_0.index], "", function(arg_11_0)
			if arg_8_0._state == var_0_0.STATES.DESTROY:
				return

			arg_8_0.nextSprite = arg_11_0

			arg_10_0()))
	parallelAsync(var_8_0, function()
		setImageSprite(arg_8_0.rtFront, getImageSprite(arg_8_0.rtBg))
		setImageAlpha(arg_8_0.rtFront, 1)
		setImageSprite(arg_8_0.rtBg, arg_8_0.nextSprite)

		arg_8_0.uniqueId = LeanTween.alpha(arg_8_0.rtFront, 0, 0.5).setEase(LeanTweenType.easeOutSine).setOnComplete(System.Action(function()
			arg_8_0.DelayCall())).uniqueId)

def var_0_0.OnDestroy(arg_14_0):
	if arg_14_0.uniqueId:
		LeanTween.cancel(arg_14_0.uniqueId)

return var_0_0
