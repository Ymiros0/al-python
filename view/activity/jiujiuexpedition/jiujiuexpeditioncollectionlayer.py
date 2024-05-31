local var_0_0 = class("JiuJiuExpeditionCollectionLayer", import("...base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "JiuJiuExpeditionCollectionUI"

def var_0_0.SetData(arg_2_0, arg_2_1, arg_2_2, arg_2_3, arg_2_4):
	arg_2_0.allDatas = arg_2_1
	arg_2_0.completeDatas = arg_2_2
	arg_2_0.getRewardIndex = arg_2_3
	arg_2_0.gotRewardIndex = arg_2_4

local function var_0_1(arg_3_0, arg_3_1, arg_3_2)
	return table.contains(arg_3_0.completeDatas, arg_3_2)

local var_0_2 = 0
local var_0_3 = 1
local var_0_4 = 2

def var_0_0.IsGotAward(arg_4_0, arg_4_1):
	if arg_4_1 <= arg_4_0.gotRewardIndex:
		return True

	return False

def var_0_0.GetAwardState(arg_5_0, arg_5_1):
	if arg_5_1 > arg_5_0.gotRewardIndex + 1:
		return var_0_2
	elif arg_5_1 <= arg_5_0.gotRewardIndex:
		return var_0_4
	elif arg_5_1 == arg_5_0.gotRewardIndex + 1 and arg_5_1 <= arg_5_0.getRewardIndex:
		return var_0_3
	else
		return var_0_2

def var_0_0.init(arg_6_0):
	arg_6_0.bookContainer = arg_6_0.findTF("books")
	arg_6_0.book = arg_6_0.findTF("book")
	arg_6_0.nextPageBtn = arg_6_0.findTF("book/next")
	arg_6_0.prevPageBtn = arg_6_0.findTF("book/prev")
	arg_6_0.scoreList = UIItemList.New(arg_6_0.findTF("book/list"), arg_6_0.findTF("book/list/tpl"))
	arg_6_0.getBtn = arg_6_0.findTF("book/get")
	arg_6_0.gotBtn = arg_6_0.findTF("book/got")
	arg_6_0.goBtn = arg_6_0.findTF("book/go")
	arg_6_0.books = {
		arg_6_0.findTF("books/1"),
		arg_6_0.findTF("books/2"),
		arg_6_0.findTF("books/3")
	}
	arg_6_0.parent = arg_6_0._tf.parent

	pg.UIMgr.GetInstance().BlurPanel(arg_6_0._tf)

def var_0_0.didEnter(arg_7_0):
	onButton(arg_7_0, arg_7_0._tf, function()
		if arg_7_0.isOpenBook:
			arg_7_0.CloseBook()
		else
			arg_7_0.emit(var_0_0.ON_CLOSE), SFX_CANCEL)
	arg_7_0.InitBooks()

def var_0_0.InitBooks(arg_9_0):
	setActive(arg_9_0.bookContainer, True)
	setActive(arg_9_0.book, False)
	arg_9_0.updateBooks()
	arg_9_0.UpdateTip()

def var_0_0.updateBooks(arg_10_0):
	for iter_10_0, iter_10_1 in ipairs(arg_10_0.books):
		local var_10_0 = iter_10_0 <= arg_10_0.gotRewardIndex + 1

		setActive(iter_10_1.Find("lock"), not var_10_0)

		iter_10_1.GetComponent(typeof(Image)).color = var_10_0 and Color.New(1, 1, 1, 1) or Color.New(0.46, 0.46, 0.46, 1)

		onButton(arg_10_0, iter_10_1, function()
			if var_10_0:
				arg_10_0.OpenBook(iter_10_0)
			else
				pg.TipsMgr.GetInstance().ShowTips(i18n("jiujiu_expedition_book_tip")), SFX_PANEL)

def var_0_0.UpdateTip(arg_12_0):
	for iter_12_0, iter_12_1 in ipairs(arg_12_0.books):
		local var_12_0 = arg_12_0.GetAwardState(iter_12_0) == var_0_3

		setActive(iter_12_1.Find("tip"), var_12_0)

def var_0_0.OpenBook(arg_13_0, arg_13_1):
	arg_13_0.isOpenBook = True

	setActive(arg_13_0.bookContainer, False)
	setActive(arg_13_0.book, True)
	setActive(arg_13_0.book.Find("1"), arg_13_1 == 1)
	setActive(arg_13_0.book.Find("2"), arg_13_1 == 2)
	setActive(arg_13_0.book.Find("3"), arg_13_1 == 3)

	local var_13_0 = arg_13_0.allDatas[arg_13_1]

	onButton(arg_13_0, arg_13_0.nextPageBtn, function()
		setActive(arg_13_0.nextPageBtn, False)
		setActive(arg_13_0.prevPageBtn, True)

		local var_14_0 = _.slice(var_13_0, 4, 2)

		arg_13_0.UpdatePage(arg_13_1, var_14_0, 3), SFX_PANEL)
	onButton(arg_13_0, arg_13_0.prevPageBtn, function()
		setActive(arg_13_0.nextPageBtn, True)
		setActive(arg_13_0.prevPageBtn, False)

		local var_15_0 = _.slice(var_13_0, 1, 3)

		arg_13_0.UpdatePage(arg_13_1, var_15_0, 0), SFX_PANEL)

	local var_13_1 = arg_13_0.GetAwardState(arg_13_1)

	setActive(arg_13_0.getBtn, var_13_1 == var_0_3)
	setActive(arg_13_0.gotBtn, var_13_1 == var_0_4)
	setActive(arg_13_0.goBtn, var_13_1 == var_0_2)
	onButton(arg_13_0, arg_13_0.getBtn, function()
		arg_13_0.emit(JiuJiuExpeditionCollectionMediator.ON_GET, arg_13_1), SFX_PANEL)
	onButton(arg_13_0, arg_13_0.goBtn, function()
		pg.TipsMgr.GetInstance().ShowTips(i18n("jiujiu_expedition_reward_tip")), SFX_PANEL)
	triggerButton(arg_13_0.prevPageBtn)

def var_0_0.UpdatePage(arg_18_0, arg_18_1, arg_18_2, arg_18_3):
	arg_18_0.scoreList.make(function(arg_19_0, arg_19_1, arg_19_2)
		if arg_19_0 == UIItemList.EventUpdate:
			local var_19_0 = arg_18_2[arg_19_1 + 1]
			local var_19_1 = "JiuJiuExpeditionCollectionIcon/" .. arg_18_1 .. "_" .. arg_19_1 + 1 + arg_18_3

			GetImageSpriteFromAtlasAsync(var_19_1, "", arg_19_2.Find("icon"))
			setActive(arg_19_2.Find("lock"), not var_0_1(arg_18_0, arg_18_1, var_19_0)))
	arg_18_0.scoreList.align(#arg_18_2)

def var_0_0.CloseBook(arg_20_0):
	arg_20_0.isOpenBook = False

	setActive(arg_20_0.bookContainer, True)
	setActive(arg_20_0.book, False)

def var_0_0.willExit(arg_21_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_21_0._tf, arg_21_0.parent)

return var_0_0
