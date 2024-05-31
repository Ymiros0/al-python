local var_0_0 = class("WorldBossScene", import("...base.BaseUI"))

var_0_0.PAGE_ENTRANCE = 0
var_0_0.PAGE_CHALLENGE = 1
var_0_0.PAGE_CURRENT = 2
var_0_0.PAGE_ARCHIVES_CHALLENGE = 3
var_0_0.PAGE_ARCHIVES = 4
var_0_0.PAGE_ARCHIVES_LIST = 5
var_0_0.ON_SWITCH = "WorldBossScene.ON_SWITCH"
var_0_0.ON_QUIT_ARCHIVES_LIST = "WorldBossScene.ON_QUIT_ARCHIVES_LIST"
var_0_0.Listeners = {
	onBossUpdated = "OnBossUpdated"
}

def var_0_0.getUIName(arg_1_0):
	return "WorldBossUI"

def var_0_0.SetBossProxy(arg_2_0, arg_2_1, arg_2_2):
	assert(not arg_2_0.bossProxy)

	arg_2_0.bossProxy = arg_2_1
	arg_2_0.metaCharacterProxy = arg_2_2
	arg_2_0.boss = arg_2_0.bossProxy.GetBoss()
	arg_2_0.entrancePage = WorldBossEntrancePage.New(arg_2_0.pagesTF, arg_2_0.event, arg_2_0.contextData)

	arg_2_0.entrancePage.Setup(arg_2_0.bossProxy)

	arg_2_0.challengeCurrentBossPage = CurrentWorldBossChallengePage.New(arg_2_0.pagesTF, arg_2_0.event, arg_2_0.contextData)

	arg_2_0.challengeCurrentBossPage.Setup(arg_2_0.bossProxy)

	arg_2_0.currentEmptyPage = CurrentWorldBossEmptyPage.New(arg_2_0.pagesTF, arg_2_0.event)

	arg_2_0.currentEmptyPage.Setup(arg_2_0.bossProxy)

	arg_2_0.currentBossDetailPage = CurrentWorldBossDetailPage.New(arg_2_0.pagesTF, arg_2_0.event)

	arg_2_0.currentBossDetailPage.Setup(arg_2_0.bossProxy)

	arg_2_0.challengeArchivesBossPage = ArchivesWorldBossChallengePage.New(arg_2_0.pagesTF, arg_2_0.event, arg_2_0.contextData)

	arg_2_0.challengeArchivesBossPage.Setup(arg_2_0.bossProxy)

	arg_2_0.archivesListPage = ArchivesWorldBossListPage.New(arg_2_0.pagesTF, arg_2_0.event)

	arg_2_0.archivesListPage.Setup(arg_2_0.bossProxy)

	arg_2_0.archivesEmptyPage = ArchivesWorldBossEmptyPage.New(arg_2_0.pagesTF, arg_2_0.event)

	arg_2_0.archivesEmptyPage.Setup(arg_2_0.bossProxy)

	arg_2_0.archivesDetailPage = ArchivesWorldBossDetailPage.New(arg_2_0.pagesTF, arg_2_0.event)

	arg_2_0.archivesDetailPage.Setup(arg_2_0.bossProxy)

	arg_2_0.formationPreviewPage = WorldBossFormationPreViewPage.New(arg_2_0.pagesTF, arg_2_0.event)

	arg_2_0.bossProxy.AddListener(WorldBossProxy.EventBossUpdated, arg_2_0.onBossUpdated)

def var_0_0.AddListeners(arg_3_0):
	arg_3_0.bind(var_0_0.ON_SWITCH, function(arg_4_0, arg_4_1)
		arg_3_0.SwitchPage(arg_4_1))
	arg_3_0.bind(var_0_0.ON_QUIT_ARCHIVES_LIST, function()
		arg_3_0.OnBack())

def var_0_0.RemoveListeners(arg_6_0):
	arg_6_0.bossProxy.RemoveListener(WorldBossProxy.EventBossUpdated, arg_6_0.onBossUpdated)

def var_0_0.OnBossUpdated(arg_7_0):
	arg_7_0.boss = arg_7_0.bossProxy.GetBoss()

	if arg_7_0.page == arg_7_0.currentBossDetailPage or arg_7_0.page == arg_7_0.archivesDetailPage or arg_7_0.page == arg_7_0.currentEmptyPage or arg_7_0.page == arg_7_0.archivesEmptyPage:
		arg_7_0.SwitchPage(var_0_0.PAGE_ENTRANCE)

def var_0_0.OnShowFormationPreview(arg_8_0, arg_8_1):
	arg_8_0.formationPreviewPage.ExecuteAction("Show", arg_8_1)

def var_0_0.OnRemoveLayers(arg_9_0):
	if arg_9_0.currentBossDetailPage and arg_9_0.currentBossDetailPage.GetLoaded() and arg_9_0.currentBossDetailPage.isShowing():
		arg_9_0.currentBossDetailPage.TryPlayGuide()

def var_0_0.OnAutoBattleResult(arg_10_0, arg_10_1):
	if arg_10_0.archivesDetailPage and arg_10_0.archivesDetailPage.isShowing():
		arg_10_0.archivesDetailPage.OnAutoBattleResult(arg_10_1)

def var_0_0.OnAutoBattleStart(arg_11_0, arg_11_1):
	if arg_11_0.archivesDetailPage and arg_11_0.archivesDetailPage.isShowing():
		arg_11_0.archivesDetailPage.OnAutoBattleStart(arg_11_1)

def var_0_0.OnSwitchArchives(arg_12_0):
	if arg_12_0.archivesListPage and arg_12_0.archivesListPage.GetLoaded() and arg_12_0.archivesListPage.isShowing():
		arg_12_0.archivesListPage.OnSwitchArchives()

def var_0_0.OnGetMetaAwards(arg_13_0):
	if arg_13_0.archivesListPage and arg_13_0.archivesListPage.GetLoaded() and arg_13_0.archivesListPage.isShowing():
		arg_13_0.archivesListPage.OnGetMetaAwards()

def var_0_0.getAwardDone(arg_14_0):
	if arg_14_0.page == arg_14_0.challengeCurrentBossPage:
		arg_14_0.challengeCurrentBossPage.ExecuteAction("CloseGetPage")

	if (arg_14_0.page == arg_14_0.currentEmptyPage or arg_14_0.page == arg_14_0.currentBossDetailPage) and arg_14_0.page.GetLoaded():
		arg_14_0.page.metaWorldbossBtn.Update()

def var_0_0.init(arg_15_0):
	for iter_15_0, iter_15_1 in pairs(var_0_0.Listeners):
		arg_15_0[iter_15_0] = function(...)
			var_0_0[iter_15_1](arg_15_0, ...)

	arg_15_0.backBtn = arg_15_0.findTF("back_btn")
	arg_15_0.pagesTF = arg_15_0.findTF("pages")

	arg_15_0.AddListeners()

def var_0_0.didEnter(arg_17_0):
	arg_17_0.pageStack = {}

	onButton(arg_17_0, arg_17_0.backBtn, function()
		arg_17_0.OnBack(), SOUND_BACK)
	arg_17_0.emit(WorldBossMediator.ON_FETCH_BOSS)

def var_0_0.OnBack(arg_19_0):
	if #arg_19_0.pageStack <= 1:
		arg_19_0.emit(var_0_0.ON_BACK)

		return

	table.remove(arg_19_0.pageStack, #arg_19_0.pageStack)

	local var_19_0 = arg_19_0.pageStack[#arg_19_0.pageStack]

	arg_19_0._SwitchPage(var_19_0)

def var_0_0.SwitchPage(arg_20_0, arg_20_1):
	arg_20_0._SwitchPage(arg_20_1)

	if #arg_20_0.pageStack > 1 and arg_20_0.pageStack[#arg_20_0.pageStack - 1] == arg_20_1:
		table.remove(arg_20_0.pageStack, #arg_20_0.pageStack)
	else
		table.insert(arg_20_0.pageStack, arg_20_1)

def var_0_0.GetTargetPageType(arg_21_0, arg_21_1, arg_21_2):
	if arg_21_1 == var_0_0.PAGE_CHALLENGE:
		return arg_21_0.challengeCurrentBossPage
	elif arg_21_1 == var_0_0.PAGE_ARCHIVES_CHALLENGE:
		return arg_21_0.challengeArchivesBossPage
	elif arg_21_1 == var_0_0.PAGE_ENTRANCE:
		return arg_21_0.entrancePage
	elif arg_21_1 == var_0_0.PAGE_CURRENT:
		if arg_21_0.boss and arg_21_2:
			return arg_21_0.currentBossDetailPage
		else
			return arg_21_0.currentEmptyPage
	elif arg_21_1 == var_0_0.PAGE_ARCHIVES:
		if arg_21_0.boss and not arg_21_2:
			return arg_21_0.archivesDetailPage
		else
			return arg_21_0.archivesEmptyPage
	elif arg_21_1 == var_0_0.PAGE_ARCHIVES_LIST:
		return arg_21_0.archivesListPage

def var_0_0._SwitchPage(arg_22_0, arg_22_1):
	if arg_22_0.page:
		arg_22_0.page.ExecuteAction("Hide")

	local var_22_0 = False

	if arg_22_0.boss:
		var_22_0 = WorldBossConst._IsCurrBoss(arg_22_0.boss)

	if arg_22_1 == var_0_0.PAGE_ENTRANCE and arg_22_0.boss:
		arg_22_1 = var_22_0 and var_0_0.PAGE_CURRENT or var_0_0.PAGE_ARCHIVES

	if LOCK_WORLDBOSS_ARCHIVES and (arg_22_1 == var_0_0.PAGE_ENTRANCE or arg_22_1 > var_0_0.PAGE_CURRENT):
		arg_22_1 = var_0_0.PAGE_CURRENT

	arg_22_0.page = arg_22_0.GetTargetPageType(arg_22_1, var_22_0)

	arg_22_0.page.ExecuteAction("Update")

	arg_22_0.pageType = arg_22_1

	setActive(arg_22_0.backBtn, arg_22_0.pageType != var_0_0.PAGE_ENTRANCE and arg_22_0.pageType != var_0_0.PAGE_ARCHIVES_LIST)
	arg_22_0.LoadEffect(arg_22_1)

def var_0_0.LoadEffect(arg_23_0, arg_23_1):
	local var_23_0 = arg_23_1 == var_0_0.PAGE_CURRENT and arg_23_0.boss or arg_23_1 == var_0_0.PAGE_CHALLENGE and arg_23_0.bossProxy.ExistCacheBoss()

	if var_23_0 and not arg_23_0.fireEffect:
		pg.UIMgr.GetInstance().LoadingOn()
		PoolMgr.GetInstance().GetUI("gondouBoss_huoxing", True, function(arg_24_0)
			pg.UIMgr.GetInstance().LoadingOff()

			arg_23_0.fireEffect = arg_24_0

			setParent(arg_23_0.fireEffect, arg_23_0._tf)
			setActive(arg_23_0.fireEffect, True))
	elif arg_23_0.fireEffect:
		setActive(arg_23_0.fireEffect, var_23_0)

def var_0_0.willExit(arg_25_0):
	if arg_25_0.fireEffect:
		PoolMgr.GetInstance().ReturnUI("gondouBoss_huoxing", arg_25_0.fireEffect)

	if arg_25_0.bossProxy:
		arg_25_0.RemoveListeners()

	if arg_25_0.challengeCurrentBossPage:
		arg_25_0.challengeCurrentBossPage.Destroy()

		arg_25_0.challengeCurrentBossPage = None

	if arg_25_0.currentEmptyPage:
		arg_25_0.currentEmptyPage.Destroy()

		arg_25_0.currentEmptyPage = None

	if arg_25_0.currentBossDetailPage:
		arg_25_0.currentBossDetailPage.Destroy()

		arg_25_0.currentBossDetailPage = None

	if arg_25_0.formationPreviewPage:
		arg_25_0.formationPreviewPage.Destroy()

		arg_25_0.formationPreviewPage = None

	if arg_25_0.archivesListPage:
		arg_25_0.archivesListPage.Destroy()

		arg_25_0.archivesListPage = None

	if arg_25_0.archivesDetailPage:
		arg_25_0.archivesDetailPage.Destroy()

		arg_25_0.archivesDetailPage = None

	if arg_25_0.entrancePage:
		arg_25_0.entrancePage.Destroy()

		arg_25_0.entrancePage = None

	if arg_25_0.archivesEmptyPage:
		arg_25_0.archivesEmptyPage.Destroy()

		arg_25_0.archivesEmptyPage = None

	if arg_25_0.challengeArchivesBossPage:
		arg_25_0.challengeArchivesBossPage.Destroy()

		arg_25_0.challengeArchivesBossPage = None

return var_0_0
