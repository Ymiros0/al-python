local var_0_0 = class("KFCPTPage", import(".TemplatePage.PtTemplatePage"))

var_0_0.SpineCharName = {
	"lafei_11",
	"lingbo_14"
}
var_0_0.SpineCharActionName = "stand_normal"
var_0_0.SpineShopActionSpeed = {
	0.8,
	1,
	1.2
}

def var_0_0.OnFirstFlush(arg_1_0):
	var_0_0.super.OnFirstFlush(arg_1_0)
	onButton(arg_1_0, arg_1_0.findTF("sdBtn", arg_1_0.bg), function()
		pg.m02.sendNotification(GAME.GO_SCENE, SCENE.SKINSHOP), SFX_PANEL)
	onButton(arg_1_0, arg_1_0.battleBtn, function()
		arg_1_0.emit(ActivityMediator.SPECIAL_BATTLE_OPERA), SFX_PANEL)
	onButton(arg_1_0, arg_1_0.getBtn, function()
		local var_4_0 = {}
		local var_4_1 = arg_1_0.ptData.GetAward()
		local var_4_2 = getProxy(PlayerProxy).getRawData()
		local var_4_3 = pg.gameset.urpt_chapter_max.description[1]
		local var_4_4 = LOCK_UR_SHIP and 0 or getProxy(BagProxy).GetLimitCntById(var_4_3)
		local var_4_5, var_4_6 = Task.StaticJudgeOverflow(var_4_2.gold, var_4_2.oil, var_4_4, True, True, {
			{
				var_4_1.type,
				var_4_1.id,
				var_4_1.count
			}
		})

		if var_4_5:
			table.insert(var_4_0, function(arg_5_0)
				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					type = MSGBOX_TYPE_ITEM_BOX,
					content = i18n("award_max_warning"),
					items = var_4_6,
					onYes = arg_5_0
				}))

		seriesAsync(var_4_0, function()
			local var_6_0, var_6_1 = arg_1_0.ptData.GetResProgress()

			arg_1_0.emit(ActivityMediator.EVENT_PT_OPERATION, {
				cmd = 1,
				activity_id = arg_1_0.ptData.GetId(),
				arg1 = var_6_1
			})
			arg_1_0.SetLocalData()), SFX_PANEL)

	arg_1_0.sdContainer = arg_1_0.findTF("sdcontainer", arg_1_0.bg)
	arg_1_0.sdSpine = None
	arg_1_0.sdName = arg_1_0.GetRandomName()
	arg_1_0.sdSpineLRQ = GetSpineRequestPackage.New(arg_1_0.sdName, function(arg_7_0)
		SetParent(arg_7_0, arg_1_0.sdContainer)

		arg_1_0.sdSpine = arg_7_0
		arg_1_0.sdSpine.transform.localScale = Vector3.one

		local var_7_0 = arg_1_0.sdSpine.GetComponent("SpineAnimUI")

		if var_7_0:
			var_7_0.SetAction(var_0_0.SpineCharActionName, 0)

		arg_1_0.sdSpineLRQ = None).Start()
	arg_1_0.shopSpine = arg_1_0.findTF("shop/shop", arg_1_0.bg)
	arg_1_0.shopAnim = arg_1_0.shopSpine.GetComponent("SpineAnimUI")
	arg_1_0.shopGraphic = arg_1_0.shopSpine.GetComponent("SkeletonGraphic")

	arg_1_0.shopAnim.SetAction("normal", 0)

def var_0_0.OnUpdateFlush(arg_8_0):
	var_0_0.super.OnUpdateFlush(arg_8_0)

	local var_8_0, var_8_1, var_8_2 = arg_8_0.ptData.GetResProgress()

	setText(arg_8_0.progress, (var_8_2 >= 1 and setColorStr(var_8_0, "#ffc563") or var_8_0) .. "/" .. var_8_1)

	if arg_8_0.ptData.CanGetMorePt():
		arg_8_0.GetLocalData()

		if arg_8_0.finishCount == 0:
			arg_8_0.shopAnim.SetAction("normal", 0)
		else
			arg_8_0.shopAnim.SetAction("action", 0)

			arg_8_0.shopGraphic.timeScale = var_0_0.SpineShopActionSpeed[arg_8_0.finishCount]
	else
		arg_8_0.shopAnim.SetAction("action", 0)

		arg_8_0.shopGraphic.timeScale = var_0_0.SpineShopActionSpeed[#var_0_0.SpineShopActionSpeed]

def var_0_0.GetLocalData(arg_9_0):
	arg_9_0.playerId = getProxy(PlayerProxy).getData().id

	local var_9_0 = pg.TimeMgr.GetInstance()

	arg_9_0.curDay = var_9_0.DiffDay(arg_9_0.ptData.startTime, var_9_0.GetServerTime()) + 1
	arg_9_0.finishCount = PlayerPrefs.GetInt("kfc_pt_" .. arg_9_0.playerId .. "_day_" .. arg_9_0.curDay)

def var_0_0.SetLocalData(arg_10_0):
	arg_10_0.finishCount = arg_10_0.finishCount + 1

	local var_10_0 = #var_0_0.SpineShopActionSpeed

	arg_10_0.finishCount = var_10_0 > arg_10_0.finishCount and arg_10_0.finishCount or var_10_0

	PlayerPrefs.SetInt("kfc_pt_" .. arg_10_0.playerId .. "_day_" .. arg_10_0.curDay, arg_10_0.finishCount)
	PlayerPrefs.Save()

def var_0_0.GetRandomName():
	return var_0_0.SpineCharName[math.random(#var_0_0.SpineCharName)]

def var_0_0.OnDestroy(arg_12_0):
	if arg_12_0.sdSpineLRQ:
		arg_12_0.sdSpineLRQ.Stop()

		arg_12_0.sdSpineLRQ = None

	if arg_12_0.sdSpine:
		arg_12_0.sdSpine.transform.localScale = Vector3.one

		pg.PoolMgr.GetInstance().ReturnSpineChar(arg_12_0.sdName, arg_12_0.sdSpine)

		arg_12_0.sdSpine = None
		arg_12_0.sdName = None

return var_0_0
