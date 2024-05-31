local var_0_0 = class("TowerClimbingCollectionLayer", import("...base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "TowerClimbingCollectionUI"

def var_0_0.SetData(arg_2_0, arg_2_1):
	arg_2_0.miniGameData = arg_2_1

	local var_2_0 = arg_2_0.miniGameData.GetRuntimeData("kvpElements")
	local var_2_1, var_2_2 = TowerClimbingGameView.GetTowerClimbingPageAndScore(var_2_0)

	arg_2_0.score = var_2_1
	arg_2_0.pageIndex = var_2_2

	assert(var_2_1)
	assert(var_2_2)

	arg_2_0.config = pg.mini_game[MiniGameDataCreator.TowerClimbingGameID].simple_config_data

local function var_0_1(arg_3_0, arg_3_1, arg_3_2)
	if arg_3_1 < arg_3_0.pageIndex:
		return True
	elif arg_3_1 == arg_3_0.pageIndex:
		return arg_3_2 <= arg_3_0.score
	else
		return False

local var_0_2 = 0
local var_0_3 = 1
local var_0_4 = 2

def var_0_0.IsGotAward(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_0.miniGameData.GetRuntimeData("kvpElements")[1] or {}

	for iter_4_0, iter_4_1 in ipairs(var_4_0):
		if iter_4_1.key == arg_4_1 and iter_4_1.value == 1:
			return True

	return False

def var_0_0.GetAwardState(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_0.config[arg_5_1][1]
	local var_5_1 = var_5_0[#var_5_0]

	if arg_5_1 < arg_5_0.pageIndex:
		if arg_5_0.IsGotAward(arg_5_1):
			return var_0_4
		else
			return var_0_3
	elif arg_5_1 == arg_5_0.pageIndex:
		local var_5_2 = arg_5_0.IsGotAward(arg_5_1)

		if var_5_2:
			return var_0_4
		elif var_5_1 <= arg_5_0.score and not var_5_2:
			return var_0_3
		elif var_5_1 > arg_5_0.score:
			return var_0_2
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

	for iter_9_0, iter_9_1 in ipairs(arg_9_0.books):
		local var_9_0 = iter_9_0 <= arg_9_0.pageIndex

		setActive(iter_9_1.Find("lock"), not var_9_0)

		iter_9_1.GetComponent(typeof(Image)).color = var_9_0 and Color.New(1, 1, 1, 1) or Color.New(0.46, 0.46, 0.46, 1)

		onButton(arg_9_0, iter_9_1, function()
			if var_9_0:
				arg_9_0.OpenBook(iter_9_0)
			else
				pg.TipsMgr.GetInstance().ShowTips(i18n("towerclimbing_book_tip")), SFX_PANEL)

	arg_9_0.UpdateTip()

def var_0_0.UpdateTip(arg_11_0):
	for iter_11_0, iter_11_1 in ipairs(arg_11_0.books):
		local var_11_0 = arg_11_0.GetAwardState(iter_11_0) == var_0_3

		setActive(iter_11_1.Find("tip"), var_11_0)

def var_0_0.OpenBook(arg_12_0, arg_12_1):
	arg_12_0.isOpenBook = True

	setActive(arg_12_0.bookContainer, False)
	setActive(arg_12_0.book, True)
	setActive(arg_12_0.book.Find("1"), arg_12_1 == 1)
	setActive(arg_12_0.book.Find("2"), arg_12_1 == 2)
	setActive(arg_12_0.book.Find("3"), arg_12_1 == 3)

	local var_12_0 = arg_12_0.config[arg_12_1][1]

	onButton(arg_12_0, arg_12_0.nextPageBtn, function()
		setActive(arg_12_0.nextPageBtn, False)
		setActive(arg_12_0.prevPageBtn, True)

		local var_13_0 = _.slice(var_12_0, 4, 2)

		arg_12_0.UpdatePage(arg_12_1, var_13_0, 3), SFX_PANEL)
	onButton(arg_12_0, arg_12_0.prevPageBtn, function()
		setActive(arg_12_0.nextPageBtn, True)
		setActive(arg_12_0.prevPageBtn, False)

		local var_14_0 = _.slice(var_12_0, 1, 3)

		arg_12_0.UpdatePage(arg_12_1, var_14_0, 0), SFX_PANEL)

	local var_12_1 = arg_12_0.GetAwardState(arg_12_1)

	setActive(arg_12_0.getBtn, var_12_1 == var_0_3)
	setActive(arg_12_0.gotBtn, var_12_1 == var_0_4)
	setActive(arg_12_0.goBtn, var_12_1 == var_0_2)
	onButton(arg_12_0, arg_12_0.getBtn, function()
		arg_12_0.emit(TowerClimbingCollectionMediator.ON_GET, arg_12_1), SFX_PANEL)
	onButton(arg_12_0, arg_12_0.goBtn, function()
		pg.TipsMgr.GetInstance().ShowTips(i18n("towerclimbing_reward_tip")), SFX_PANEL)
	triggerButton(arg_12_0.prevPageBtn)

def var_0_0.UpdatePage(arg_17_0, arg_17_1, arg_17_2, arg_17_3):
	arg_17_0.scoreList.make(function(arg_18_0, arg_18_1, arg_18_2)
		if arg_18_0 == UIItemList.EventUpdate:
			local var_18_0 = arg_17_2[arg_18_1 + 1]
			local var_18_1 = "TowerClimbingCollectionIcon/" .. arg_17_1 .. "_" .. arg_18_1 + 1 + arg_17_3

			GetImageSpriteFromAtlasAsync(var_18_1, "", arg_18_2.Find("icon"))
			setActive(arg_18_2.Find("lock"), not var_0_1(arg_17_0, arg_17_1, var_18_0)))
	arg_17_0.scoreList.align(#arg_17_2)

def var_0_0.CloseBook(arg_19_0):
	arg_19_0.isOpenBook = False

	setActive(arg_19_0.bookContainer, True)
	setActive(arg_19_0.book, False)

def var_0_0.willExit(arg_20_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_20_0._tf, arg_20_0.parent)

return var_0_0
