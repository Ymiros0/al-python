local var_0_0 = class("Dorm3dFurnitureAcessesWindow", import("view.base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "Dorm3dFurnitureAcessesWindow"

def var_0_0.init(arg_2_0):
	return

def var_0_0.didEnter(arg_3_0):
	onButton(arg_3_0, arg_3_0._tf.Find("Mask"), function()
		existCall(arg_3_0.contextData.onClose)
		arg_3_0.closeView())
	onButton(arg_3_0, arg_3_0._tf.Find("Window/Close"), function()
		existCall(arg_3_0.contextData.onClose)
		arg_3_0.closeView(), SFX_CANCEL)
	setText(arg_3_0._tf.Find("Window/Title"), arg_3_0.contextData.title)
	setText(arg_3_0._tf.Find("Window/Acesses/Text"), i18n("dorm3d_furniture_window_acesses"))
	arg_3_0.ShowSingleItemBox(arg_3_0.contextData)
	arg_3_0.ShowCommonObtainWindow(arg_3_0.contextData)

def var_0_0.ShowSingleItemBox(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_0._tf.Find("Window/Icon")

	updateDrop(var_6_0, arg_6_1.drop)

	local var_6_1 = arg_6_1.name or arg_6_1.drop.cfg.name or ""

	setText(arg_6_0._tf.Find("Window/Name"), var_6_1)
	setText(arg_6_0._tf.Find("Window/Count"), i18n("child_msg_owned", setColorStr(arg_6_1.drop.count, "#39bfff")))

	local var_6_2 = arg_6_0._tf.Find("Window/Content")

	setText(var_6_2, arg_6_1.drop.cfg.desc)

def var_0_0.ShowCommonObtainWindow(arg_7_0, arg_7_1):
	local var_7_0 = defaultValue(arg_7_1.showGOBtn, False)

	arg_7_0.obtainSkipList = arg_7_0.obtainSkipList or UIItemList.New(arg_7_0._tf.Find("Window/List"), arg_7_0._tf.Find("Window/List").GetChild(0))

	arg_7_0.obtainSkipList.make(function(arg_8_0, arg_8_1, arg_8_2)
		if arg_8_0 == UIItemList.EventUpdate:
			local var_8_0 = arg_7_1.list[arg_8_1 + 1]
			local var_8_1 = var_8_0[1]
			local var_8_2 = var_8_0[2]
			local var_8_3 = var_8_0[3]
			local var_8_4 = HXSet.hxLan(var_8_1)

			arg_8_2.Find("Mask/Text").GetComponent("ScrollText").SetText(var_8_4)
			setActive(arg_8_2.Find("Button"), var_7_0 and var_8_2[1] != "" and var_8_2[1] != "COLLECTSHIP")

			if var_8_2[1] != "":
				onButton(arg_7_0, arg_8_2.Find("Button"), function()
					if var_8_3 and var_8_3 != 0:
						local var_9_0 = getProxy(ActivityProxy).getActivityById(var_8_3)

						if not var_9_0 or var_9_0.isEnd():
							pg.TipsMgr.GetInstance().ShowTips(i18n("collection_way_is_unopen"))

							return
					elif var_8_2[1] == "SHOP" and var_8_2[2].warp == NewShopsScene.TYPE_MILITARY_SHOP and not pg.SystemOpenMgr.GetInstance().isOpenSystem(getProxy(PlayerProxy).getData().level, "MilitaryExerciseMediator"):
						pg.TipsMgr.GetInstance().ShowTips(i18n("military_shop_no_open_tip"))

						return
					elif var_8_2[1] == "LEVEL" and var_8_2[2]:
						local var_9_1 = var_8_2[2].chapterid
						local var_9_2 = getProxy(ChapterProxy)
						local var_9_3 = var_9_2.getChapterById(var_9_1)

						if var_9_3.isUnlock():
							local var_9_4 = var_9_2.getActiveChapter()

							if var_9_4 and var_9_4.id != var_9_1:
								pg.TipsMgr.GetInstance().ShowTips(i18n("collect_chapter_is_activation"))

								return
							else
								local var_9_5 = {
									mapIdx = var_9_3.getConfig("map")
								}

								if var_9_3.active:
									var_9_5.chapterId = var_9_3.id
								else
									var_9_5.openChapterId = var_9_1

								pg.m02.sendNotification(GAME.GO_SCENE, SCENE.LEVEL, var_9_5)
						else
							pg.TipsMgr.GetInstance().ShowTips(i18n("acquisitionmode_is_not_open"))

							return
					elif var_8_2[1] == "COLLECTSHIP":
						if arg_7_1.mediatorName == CollectionMediator.__cname:
							pg.m02.sendNotification(CollectionMediator.EVENT_OBTAIN_SKIP, {
								toggle = 2,
								displayGroupId = var_8_2[2].shipGroupId
							})
						else
							pg.m02.sendNotification(GAME.GO_SCENE, SCENE.COLLECTSHIP, {
								toggle = 2,
								displayGroupId = var_8_2[2].shipGroupId
							})
					elif var_8_2[1] == "SHOP":
						pg.m02.sendNotification(GAME.GO_SCENE, SCENE[var_8_2[1]], var_8_2[2])
					else
						pg.m02.sendNotification(GAME.GO_SCENE, SCENE[var_8_2[1]], var_8_2[2])

					arg_7_0.closeView(), SFX_PANEL))
	arg_7_0.obtainSkipList.align(#arg_7_1.list)

def var_0_0.willExit(arg_10_0):
	return

return var_0_0
