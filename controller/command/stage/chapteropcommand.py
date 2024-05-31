local var_0_0 = class("ChapterOpCommand", import(".ChapterOpRoutine"))

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()

	if (function()
		if var_1_0.type == ChapterConst.OpRetreat:
			return

		local var_2_0 = getProxy(ChapterProxy)
		local var_2_1 = var_2_0.getActiveChapter()

		if not var_2_1:
			return True

		if var_1_0.type == ChapterConst.OpSwitch:
			for iter_2_0, iter_2_1 in ipairs(var_2_1.fleets):
				if iter_2_1.id == var_1_0.id:
					var_2_1.findex = iter_2_0

					break

			var_2_0.updateChapter(var_2_1, bit.bor(ChapterConst.DirtyStrategy, ChapterConst.DirtyFleet))
			arg_1_0.sendNotification(GAME.CHAPTER_OP_DONE, {
				type = var_1_0.type
			})
			pg.TipsMgr.GetInstance().ShowTips(i18n("formation_switch_success", var_2_1.fleet.name))

			return True)():
		return

	pg.ConnectionMgr.GetInstance().Send(13103, {
		act = var_1_0.type,
		group_id = defaultValue(var_1_0.id, 0),
		act_arg_1 = var_1_0.arg1,
		act_arg_2 = var_1_0.arg2,
		act_arg_3 = var_1_0.arg3,
		act_arg_4 = var_1_0.arg4,
		act_arg_5 = var_1_0.arg5
	}, 13104, function(arg_3_0)
		if arg_3_0.result == 0:
			local var_3_0 = getProxy(ChapterProxy)
			local var_3_1 = var_3_0.getActiveChapter()

			if not var_3_1:
				return

			local var_3_2
			local var_3_3

			arg_1_0.initData(var_1_0, arg_3_0, var_3_1)
			arg_1_0.doDropUpdate()

			if arg_1_0.chapter:
				local var_3_4 = arg_1_0.items

				if var_1_0.type == ChapterConst.OpMove:
					arg_1_0.doCollectCommonAction()
					arg_1_0.doCollectAI()
					arg_1_0.doMove()
					arg_1_0.doTeleportByPortal()
					getProxy(ChapterProxy).SetExtendChapterData(var_3_1.id, "FleetMoveDistance", #arg_3_0.move_path)
				elif var_1_0.type == ChapterConst.OpBox:
					arg_1_0.AddBoxAction()
					arg_1_0.doCollectAI()
				else
					arg_1_0.doMapUpdate()
					arg_1_0.doAIUpdate()
					arg_1_0.doShipUpdate()
					arg_1_0.doBuffUpdate()
					arg_1_0.doCellFlagUpdate()
					arg_1_0.doExtraFlagUpdate()

					if var_1_0.type == ChapterConst.OpRetreat:
						if not var_1_0.id:
							var_1_0.win = arg_1_0.chapter.CheckChapterWillWin()

							if var_1_0.win:
								arg_1_0.chapter.UpdateProgressOnRetreat()
								var_3_0.addRemasterPassCount(arg_1_0.chapter.id)

							local var_3_5 = pg.TimeMgr.GetInstance()
							local var_3_6 = var_3_0.getMapById(var_3_1.getConfig("map"))

							if var_1_0.win and var_3_6.getMapType() == Map.ELITE and var_3_5.IsSameDay(var_3_1.getStartTime(), var_3_5.GetServerTime()):
								getProxy(DailyLevelProxy).EliteCountPlus()

							if var_3_4 and #var_3_4 > 0:
								getProxy(ChapterProxy).AddExtendChapterDataArray(arg_1_0.chapter.id, "ResultDrops", var_3_4)

								var_3_4 = None

							var_3_2 = var_3_0.FinishAutoFight(var_3_1.id)

							local var_3_7 = arg_1_0.chapter.GetRegularFleetIds()

							getProxy(ChapterProxy).SetLastFleetIndex(var_3_7, True)

						arg_1_0.doRetreat()

						if not var_1_0.id:
							var_3_3 = Clone(arg_1_0.chapter)

							arg_1_0.chapter.CleanLevelData()
					elif var_1_0.type == ChapterConst.OpStory:
						arg_1_0.doCollectAI()
						arg_1_0.doPlayStory()
					elif var_1_0.type == ChapterConst.OpAmbush:
						arg_1_0.doAmbush()
					elif var_1_0.type == ChapterConst.OpStrategy:
						arg_1_0.doCollectAI()
						arg_1_0.doStrategy()
					elif var_1_0.type == ChapterConst.OpRepair:
						arg_1_0.doRepair()
					elif var_1_0.type == ChapterConst.OpSupply:
						arg_1_0.doSupply()
					elif var_1_0.type == ChapterConst.OpEnemyRound:
						arg_1_0.doCollectAI()
						arg_1_0.doEnemyRound()
					elif var_1_0.type == ChapterConst.OpSubState:
						arg_1_0.doSubState()
					elif var_1_0.type == ChapterConst.OpBarrier:
						arg_1_0.doBarrier()
					elif var_1_0.type == ChapterConst.OpRequest:
						arg_1_0.doRequest()
					elif var_1_0.type == ChapterConst.OpSkipBattle:
						arg_1_0.chapter.UpdateProgressAfterSkipBattle()
						arg_1_0.doSkipBattle()
					elif var_1_0.type == ChapterConst.OpPreClear:
						arg_1_0.chapter.CleanCurrentEnemy()
						arg_1_0.doSkipBattle()
					elif var_1_0.type == ChapterConst.OpSubTeleport:
						arg_1_0.doTeleportSub()
						arg_1_0.doTeleportByPortal()

				if var_1_0.type == ChapterConst.OpEnemyRound or var_1_0.type == ChapterConst.OpMove:
					var_3_0.updateChapter(arg_1_0.chapter, arg_1_0.flag)
				else
					arg_1_0.flag = bit.bor(arg_1_0.flag, arg_1_0.extraFlag)

					var_3_0.updateChapter(arg_1_0.chapter, arg_1_0.flag)

				if var_1_0.type == ChapterConst.OpSkipBattle:
					arg_1_0.sendNotification(GAME.CHAPTER_BATTLE_RESULT_REQUEST, {
						isSkipBattle = True
					})

					return

				arg_1_0.sendNotification(GAME.CHAPTER_OP_DONE, {
					type = var_1_0.type,
					id = var_1_0.id,
					arg1 = var_1_0.arg1,
					arg2 = var_1_0.arg2,
					path = arg_3_0.move_path,
					fullpath = arg_1_0.fullpath,
					items = var_3_4,
					exittype = var_1_0.exittype or 0,
					aiActs = arg_1_0.aiActs,
					extraFlag = arg_1_0.extraFlag,
					oldLine = var_1_0.ordLine,
					win = var_1_0.win,
					teleportPaths = arg_1_0.teleportPaths,
					extendData = var_3_2,
					finalChapterLevelData = var_3_3
				})
		else
			errorMsg(string.format("SLG操作%d 请求失效，重新拉取信息", var_1_0.type))
			pg.TipsMgr.GetInstance().ShowTips(errorTip("levelScene_operation", arg_3_0.result))

			if var_1_0.type != ChapterConst.OpRequest and var_1_0.type != ChapterConst.OpRetreat and var_1_0.type != ChapterConst.OpSubTeleport:
				arg_1_0.sendNotification(GAME.CHAPTER_OP, {
					type = ChapterConst.OpRequest,
					id = var_1_0.id
				}))

def var_0_0.PrepareChapterRetreat(arg_4_0):
	seriesAsync({
		function(arg_5_0)
			local var_5_0 = getProxy(ChapterProxy).getActiveChapter()

			if var_5_0 and var_5_0.CheckChapterWillWin() and not var_5_0.IsRemaster():
				var_5_0.UpdateProgressOnRetreat()

				local var_5_1 = var_5_0.getConfig("defeat_story_count")
				local var_5_2 = var_5_0.getConfig("defeat_story")
				local var_5_3 = False

				table.SerialIpairsAsync(var_5_1, function(arg_6_0, arg_6_1, arg_6_2)
					if arg_6_1 > var_5_0.defeatCount:
						arg_6_2()

						return

					local var_6_0 = var_5_2[arg_6_0]

					if not var_6_0 or pg.NewStoryMgr.GetInstance().IsPlayed(tostring(var_6_0)):
						arg_6_2()

						return

					if type(var_6_0) == "number":
						pg.m02.sendNotification(GAME.BEGIN_STAGE, {
							system = SYSTEM_PERFORM,
							stageId = var_6_0
						})
					elif type(var_6_0) == "string":
						if ChapterOpCommand.PlayChapterStory(var_6_0, arg_6_2, not var_5_3 and var_5_0.IsAutoFight()):
							var_5_3 = True
					else
						arg_6_2(), arg_5_0)
			else
				arg_5_0(),
		function(arg_7_0)
			pg.m02.sendNotification(GAME.CHAPTER_OP, {
				type = ChapterConst.OpRetreat
			})
			arg_7_0()
	}, arg_4_0)

def var_0_0.PlayChapterStory(arg_8_0, arg_8_1, arg_8_2):
	local var_8_0 = pg.NewStoryMgr.GetInstance()

	var_8_0.Play(arg_8_0, arg_8_1)

	if not getProxy(SettingsProxy).GetStoryAutoPlayFlag() and arg_8_2 and var_8_0.IsRunning():
		var_8_0.Puase()

		local function var_8_1()
			var_8_0.Resume()

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			hideYes = True,
			parent = rtf(var_8_0._tf),
			type = MSGBOX_TYPE_STORY_CANCEL_TIP,
			def onYes:()
				var_8_1()
				var_8_0.TriggerAutoBtn(),
			onNo = var_8_1,
			weight = LayerWeightConst.TOP_LAYER
		})

		return True

return var_0_0
