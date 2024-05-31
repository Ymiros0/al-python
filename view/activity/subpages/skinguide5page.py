local var_0_0 = class("SkinGuide5Page", import("...base.BaseActivityPage"))
local var_0_1 = {
	"guandao",
	"lafei2",
	"kelifulan",
	"xingzuo"
}
local var_0_2
local var_0_3 = "ui/activityuipage/skinguide5page_atlas"

def var_0_0.OnInit(arg_1_0):
	arg_1_0.ad = arg_1_0.findTF("AD")

	if PLATFORM_CODE == PLATFORM_JP:
		var_0_2 = {
			Vector2(-488, 52),
			Vector2(-420, -41),
			Vector2(102, -82),
			Vector2(-471, -128)
		}
	elif PLATFORM_CODE == PLATFORM_US:
		var_0_2 = {
			Vector2(-480, 189),
			Vector2(-445, -101),
			Vector2(-410, -101),
			Vector2(-354, -108)
		}
	else
		var_0_2 = {
			Vector2(-490, 130),
			Vector2(-400, -128),
			Vector2(89, 10),
			Vector2(-478, 57)
		}

	arg_1_0.paint = findTF(arg_1_0.ad, "paint")
	arg_1_0.paintGot = findTF(arg_1_0.paint, "show/got")
	arg_1_0.paintAnim = GetComponent(arg_1_0.paint, typeof(Animator))
	arg_1_0.itemContent = findTF(arg_1_0.ad, "items/content")
	arg_1_0.itemTpl = findTF(arg_1_0.ad, "items/content/itemTpl")

	setActive(arg_1_0.itemTpl, False)

	arg_1_0.iconContent = findTF(arg_1_0.ad, "iconContent")
	arg_1_0.iconTpl = findTF(arg_1_0.ad, "iconContent/IconTpl")

	setActive(arg_1_0.iconTpl, False)

	arg_1_0.desc = findTF(arg_1_0.ad, "desc")
	arg_1_0.got = findTF(arg_1_0.ad, "got")
	arg_1_0.get = findTF(arg_1_0.ad, "get")
	arg_1_0.getBound = findTF(arg_1_0.ad, "get_bound")
	arg_1_0.times = findTF(arg_1_0.ad, "times")

	onButton(arg_1_0, arg_1_0.get, function()
		if arg_1_0.selectIndex:
			local var_2_0 = getProxy(TaskProxy).getTaskById(arg_1_0.skinDatas[arg_1_0.selectIndex].task)

			arg_1_0.emit(ActivityMediator.ON_TASK_SUBMIT, var_2_0), sound, guideData)

def var_0_0.OnDataSetting(arg_3_0):
	arg_3_0.taskProxy = getProxy(TaskProxy)
	arg_3_0.taskList = arg_3_0.activity.getConfig("config_data")
	arg_3_0.totalCnt = #arg_3_0.taskList

	if not arg_3_0.skinDatas:
		arg_3_0.skinDatas = {}

		for iter_3_0 = 1, #arg_3_0.taskList:
			local var_3_0 = arg_3_0.taskList[iter_3_0]
			local var_3_1 = var_0_1[iter_3_0]
			local var_3_2 = tf(instantiate(arg_3_0.itemTpl))

			setParent(var_3_2, arg_3_0.itemContent)
			setActive(var_3_2, True)
			onButton(arg_3_0, var_3_2, function()
				arg_3_0.selectItem(iter_3_0), SFX_CONFIRM)

			GetComponent(var_3_2, typeof(Image)).sprite = GetSpriteFromAtlas(var_0_3, "item_" .. var_3_1)

			local var_3_3 = tf(Instantiate(arg_3_0.iconTpl))

			setParent(var_3_3, arg_3_0.iconContent)
			setActive(var_3_3, True)

			local var_3_4 = (arg_3_0.taskProxy.getTaskById(var_3_0) or arg_3_0.taskProxy.getFinishTaskById(var_3_0)).getConfig("award_display")[1]
			local var_3_5 = {
				type = var_3_4[1],
				id = var_3_4[2],
				count = var_3_4[3]
			}

			updateDrop(var_3_3, var_3_5)
			onButton(arg_3_0, var_3_3, function()
				arg_3_0.emit(BaseUI.ON_DROP, var_3_5), SFX_PANEL)
			table.insert(arg_3_0.skinDatas, {
				task = var_3_0,
				name = var_3_1,
				item = var_3_2,
				icon = var_3_3
			})

def var_0_0.selectItem(arg_6_0, arg_6_1):
	for iter_6_0 = 1, #arg_6_0.skinDatas:
		local var_6_0 = arg_6_0.skinDatas[iter_6_0].item

		if LeanTween.isTweening(go(var_6_0)):
			return

	local var_6_1 = 0

	for iter_6_1 = arg_6_1 + 1, #arg_6_0.skinDatas:
		arg_6_0.skinDatas[iter_6_1].item.SetAsFirstSibling()
		setActive(arg_6_0.skinDatas[iter_6_1].item, iter_6_1 != arg_6_1)
		setActive(arg_6_0.skinDatas[iter_6_1].icon, iter_6_1 == arg_6_1)

		arg_6_0.skinDatas[iter_6_1].targetPos = Vector2(var_6_1 * 215, 0)
		var_6_1 = var_6_1 + 1

	for iter_6_2 = 1, arg_6_1:
		arg_6_0.skinDatas[iter_6_2].item.SetAsFirstSibling()
		setActive(arg_6_0.skinDatas[iter_6_2].item, iter_6_2 != arg_6_1)
		setActive(arg_6_0.skinDatas[iter_6_2].icon, iter_6_2 == arg_6_1)

		arg_6_0.skinDatas[iter_6_2].targetPos = Vector2(var_6_1 * 215, 0)
		var_6_1 = var_6_1 + 1

	local var_6_2 = arg_6_0.skinDatas[arg_6_1].task
	local var_6_3 = arg_6_0.skinDatas[arg_6_1].task
	local var_6_4 = arg_6_0.taskProxy.getFinishTaskById(var_6_3)

	setActive(arg_6_0.get, not var_6_4 and arg_6_0.remainCnt > 0)
	setActive(arg_6_0.getBound, not var_6_4 and arg_6_0.remainCnt > 0)
	setActive(arg_6_0.got, var_6_4)

	arg_6_0.paintGot.anchoredPosition = var_0_2[arg_6_1]

	setActive(arg_6_0.paintGot, var_6_4)

	local var_6_5 = GetComponent(findTF(arg_6_0.paint, "show"), typeof(Image))

	var_6_5.sprite = GetSpriteFromAtlas(var_0_3, "bg_" .. arg_6_0.skinDatas[arg_6_1].name)

	var_6_5.SetNativeSize()

	local var_6_6 = GetComponent(findTF(arg_6_0.paint, "temp"), typeof(Image))

	if arg_6_0.selectIndex:
		var_6_6.sprite = GetSpriteFromAtlas(var_0_3, "bg_" .. arg_6_0.skinDatas[arg_6_0.selectIndex].name)
	else
		var_6_6.sprite = GetSpriteFromAtlas(var_0_3, "bg_" .. arg_6_0.skinDatas[arg_6_1].name)

	var_6_6.SetNativeSize()

	if arg_6_0.selectIndex and arg_6_0.selectIndex != arg_6_1:
		local var_6_7
		local var_6_8 = (arg_6_0.selectIndex != 1 or arg_6_1 != #arg_6_0.skinDatas or False) and (arg_6_0.selectIndex == #arg_6_0.skinDatas and arg_6_1 == 1 and True or arg_6_1 > arg_6_0.selectIndex and True or False)

		arg_6_0.paintAnim.SetTrigger(var_6_8 and "next" or "pre")
		arg_6_0.updateItemPos(True, var_6_8)
	else
		arg_6_0.updateItemPos(False)

	arg_6_0.selectIndex = arg_6_1

def var_0_0.OnFirstFlush(arg_7_0):
	arg_7_0.usedCnt = arg_7_0.activity.getData1()
	arg_7_0.unlockCnt = pg.TimeMgr.GetInstance().DiffDay(arg_7_0.activity.getStartTime(), pg.TimeMgr.GetInstance().GetServerTime()) + 1
	arg_7_0.unlockCnt = arg_7_0.unlockCnt > arg_7_0.totalCnt and arg_7_0.totalCnt or arg_7_0.unlockCnt
	arg_7_0.remainCnt = arg_7_0.usedCnt >= arg_7_0.totalCnt and 0 or arg_7_0.unlockCnt - arg_7_0.usedCnt

	setText(arg_7_0.desc, i18n("skin_page_desc", arg_7_0.activity.getConfig("config_id")))
	setText(findTF(arg_7_0.get, "desc"), i18n("skin_page_sign"))

	local var_7_0 = 1

	for iter_7_0 = 1, #arg_7_0.skinDatas:
		local var_7_1 = arg_7_0.skinDatas[iter_7_0].task

		if not (arg_7_0.taskProxy.getFinishTaskById(var_7_1) or False):
			var_7_0 = var_7_0 or iter_7_0

	arg_7_0.selectItem(var_7_0)
	arg_7_0.updateItemData()

def var_0_0.OnUpdateFlush(arg_8_0):
	local var_8_0 = 0

	for iter_8_0, iter_8_1 in ipairs(arg_8_0.taskList):
		if arg_8_0.taskProxy.getFinishTaskById(iter_8_1) != None:
			var_8_0 = var_8_0 + 1

	if arg_8_0.usedCnt != var_8_0:
		arg_8_0.usedCnt = var_8_0

		local var_8_1 = arg_8_0.activity

		var_8_1.data1 = arg_8_0.usedCnt

		getProxy(ActivityProxy).updateActivity(var_8_1)

	arg_8_0.unlockCnt = (pg.TimeMgr.GetInstance().DiffDay(arg_8_0.activity.getStartTime(), pg.TimeMgr.GetInstance().GetServerTime()) + 1) * arg_8_0.activity.getConfig("config_id")
	arg_8_0.unlockCnt = arg_8_0.unlockCnt > arg_8_0.totalCnt and arg_8_0.totalCnt or arg_8_0.unlockCnt
	arg_8_0.remainCnt = arg_8_0.usedCnt >= arg_8_0.totalCnt and 0 or arg_8_0.unlockCnt - arg_8_0.usedCnt

	setText(findTF(arg_8_0.times, "desc"), i18n("last_times_sign", arg_8_0.remainCnt))

	local var_8_2 = arg_8_0.activity.getConfig("config_client").story

	for iter_8_2, iter_8_3 in ipairs(arg_8_0.taskList):
		if arg_8_0.taskProxy.getFinishTaskById(iter_8_3) and checkExist(var_8_2, {
			iter_8_2
		}, {
			1
		}):
			pg.NewStoryMgr.GetInstance().Play(var_8_2[iter_8_2][1])

	arg_8_0.selectItem(arg_8_0.selectIndex)
	arg_8_0.updateItemData()

local var_0_4 = 215

def var_0_0.updateItemPos(arg_9_0, arg_9_1, arg_9_2):
	local var_9_0 = Vector2(-var_0_4, 0)
	local var_9_1 = Vector2((#arg_9_0.skinDatas - 1) * var_0_4, 0)

	for iter_9_0 = 1, #arg_9_0.skinDatas:
		local var_9_2 = arg_9_0.skinDatas[iter_9_0].item

		if LeanTween.isTweening(go(var_9_2)):
			LeanTween.cancel(go(var_9_2))

		local var_9_3 = arg_9_0.skinDatas[iter_9_0].targetPos

		if arg_9_1:
			local var_9_4 = var_9_2.anchoredPosition
			local var_9_5 = {}

			if not arg_9_2 and var_9_4.x > var_9_3.x:
				table.insert(var_9_5, var_9_1)
				table.insert(var_9_5, var_9_0)
			elif arg_9_2 and var_9_4.x < var_9_3.x:
				table.insert(var_9_5, var_9_0)
				table.insert(var_9_5, var_9_1)

			table.insert(var_9_5, var_9_3)
			table.insert(var_9_5, var_9_3)
			arg_9_0.tweenItem(var_9_2, var_9_5)
		else
			var_9_2.anchoredPosition = var_9_3

def var_0_0.tweenItem(arg_10_0, arg_10_1, arg_10_2):
	if #arg_10_2 >= 2:
		local var_10_0 = arg_10_1.anchoredPosition
		local var_10_1 = table.remove(arg_10_2, 1)
		local var_10_2 = table.remove(arg_10_2, 1)
		local var_10_3 = math.abs(var_10_1.x - var_10_0.x) / var_0_4 * 0.25

		LeanTween.value(go(arg_10_1), var_10_0.x, var_10_1.x, var_10_3).setOnUpdate(System.Action_float(function(arg_11_0)
			var_10_0.x = arg_11_0
			arg_10_1.anchoredPosition = var_10_0)).setOnComplete(System.Action(function()
			arg_10_1.anchoredPosition = var_10_2

			arg_10_0.tweenItem(arg_10_1, arg_10_2)))

def var_0_0.updateItemData(arg_13_0):
	for iter_13_0 = 1, #arg_13_0.skinDatas:
		local var_13_0 = arg_13_0.skinDatas[iter_13_0].item
		local var_13_1 = arg_13_0.skinDatas[iter_13_0].task
		local var_13_2 = arg_13_0.taskProxy.getFinishTaskById(var_13_1) or False

		setActive(findTF(var_13_0, "got"), var_13_2)

def var_0_0.OnDestroy(arg_14_0):
	for iter_14_0 = 1, #arg_14_0.skinDatas:
		local var_14_0 = arg_14_0.skinDatas[iter_14_0].item

		if LeanTween.isTweening(go(var_14_0)):
			LeanTween.cancel(go(var_14_0), False)

return var_0_0
