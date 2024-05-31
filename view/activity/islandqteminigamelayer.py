local var_0_0 = class("IslandQTEMiniGameLayer", import("..base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "IslandQTEGameUI"

def var_0_0.init(arg_2_0):
	pg.UIMgr.GetInstance().BlurPanel(arg_2_0._tf)
	eachChild(arg_2_0._tf, function(arg_3_0)
		setActive(arg_3_0, arg_3_0.name == arg_2_0.contextData.mark)

		if arg_3_0.name == arg_2_0.contextData.mark:
			arg_2_0.rtGame = arg_3_0)

def var_0_0.didEnter(arg_4_0):
	switch(arg_4_0.contextData.mark, {
		def Qgame1:()
			local var_5_0 = arg_4_0.rtGame.Find("content")
			local var_5_1 = math.random(3, 7)
			local var_5_2 = {}
			local var_5_3 = {}

			for iter_5_0 = var_5_0.childCount, 1, -1:
				table.insert(var_5_3, iter_5_0)

			local var_5_4 = arg_4_0.rtGame.Find("res")

			for iter_5_1 = 1, var_5_1:
				local var_5_5 = table.remove(var_5_3, math.random(#var_5_3))

				table.insert(var_5_2, var_5_5)

				local var_5_6 = cloneTplTo(var_5_4.Find(math.random(var_5_4.childCount)), var_5_0.GetChild(var_5_5 - 1))
				local var_5_7 = var_5_6.Find("Image")

				var_5_7.GetComponent(typeof(DftAniEvent)).SetEndEvent(function(arg_6_0)
					var_5_1 = var_5_1 - 1

					table.removebyvalue(var_5_2, var_5_5)
					Destroy(var_5_6)

					if var_5_1 == 0:
						if arg_4_0.timer:
							arg_4_0.timer.Stop()

							arg_4_0.timer = None

						arg_4_0.finishGame())
				onButton(arg_4_0, var_5_7, function()
					SetCompomentEnabled(var_5_7, typeof(Animator), True), SFX_PANEL)

			setText(arg_4_0.rtGame.Find("btn_hint/Text"), i18n("islandnode_tips2"))
			onButton(arg_4_0, arg_4_0.rtGame.Find("btn_hint"), function()
				local var_8_0 = 10

				arg_4_0.timer = Timer.New(function()
					if var_8_0 == 0:
						setText(arg_4_0.rtGame.Find("btn_hint/Text"), i18n("islandnode_tips2"))
						setButtonEnabled(arg_4_0.rtGame.Find("btn_hint"), True)

						arg_4_0.timer = None
					else
						setText(arg_4_0.rtGame.Find("btn_hint/Text"), setColorStr(i18n("islandnode_tips2") .. string.format("(%ds)", var_8_0), "#4E4E4EFF"))

						var_8_0 = var_8_0 - 1, 1, var_8_0)

				arg_4_0.timer.func()
				arg_4_0.timer.Start()
				setButtonEnabled(arg_4_0.rtGame.Find("btn_hint"), False)
				setActive(var_5_0.GetChild(var_5_2[1] - 1).GetChild(0).Find("light"), True), SFX_CONFIRM),
		def Qgame2:()
			local var_10_0 = 1
			local var_10_1 = 0
			local var_10_2 = arg_4_0.rtGame.Find("char")
			local var_10_3 = var_10_2.GetChild(math.random(var_10_2.childCount) - 1)

			eachChild(var_10_2, function(arg_11_0)
				setActive(arg_11_0, arg_11_0 == var_10_3))

			local var_10_4 = {
				arg_4_0.rtGame.Find("vine"),
				arg_4_0.rtGame.Find("vine_f"),
				var_10_3
			}

			for iter_10_0, iter_10_1 in ipairs(var_10_4):
				SetActionCallback(iter_10_1, function(arg_12_0)
					if arg_12_0 == "finish" and var_10_0 == 3:
						var_10_1 = var_10_1 - 1

						if var_10_1 == 0:
							arg_4_0.finishGame(0))

			local var_10_5 = 0
			local var_10_6 = 0

			local function var_10_7()
				if (var_10_5 - var_10_6) * (var_10_5 - var_10_6) < 0.010000000000000002:
					var_10_1 = var_10_1 + 1

					if var_10_1 >= 3:
						setButtonEnabled(arg_4_0.rtGame.Find("btn_l"), False)
						setButtonEnabled(arg_4_0.rtGame.Find("btn_r"), False)

						var_10_0 = 3

						for iter_13_0, iter_13_1 in ipairs(var_10_4):
							SetAction(iter_13_1, "hd_action" .. var_10_0)

			onButton(arg_4_0, arg_4_0.rtGame.Find("btn_l"), function()
				if var_10_0 == 1:
					var_10_0 = 2

					for iter_14_0, iter_14_1 in ipairs(var_10_4):
						SetAction(iter_14_1, "hd_action" .. var_10_0)

				var_10_5 = Time.realtimeSinceStartup

				var_10_7(), SFX_PANEL)
			onButton(arg_4_0, arg_4_0.rtGame.Find("btn_r"), function()
				if var_10_0 == 1:
					var_10_0 = 2

					for iter_15_0, iter_15_1 in ipairs(var_10_4):
						SetAction(iter_15_1, "hd_action" .. var_10_0)

				var_10_6 = Time.realtimeSinceStartup

				var_10_7(), SFX_PANEL)
			onButton(arg_4_0, arg_4_0.rtGame.Find("btn_back"), function()
				arg_4_0.closeView(), SFX_CANCEL)

			if IsUnityEditor and not arg_4_0.handle:
				arg_4_0.handle = UpdateBeat.CreateListener(function(arg_17_0)
					if Input.GetKeyUp(KeyCode.F) and arg_17_0.rtGame.Find("btn_l").GetComponent(typeof(Button)).interactable:
						triggerButton(arg_17_0.rtGame.Find("btn_l"))

					if Input.GetKeyUp(KeyCode.J) and arg_17_0.rtGame.Find("btn_r").GetComponent(typeof(Button)).interactable:
						triggerButton(arg_17_0.rtGame.Find("btn_r")), arg_4_0)

				UpdateBeat.AddListener(arg_4_0.handle),
		def Qgame3:()
			local var_18_0 = 0.5
			local var_18_1 = {
				{
					1,
					2,
					3
				},
				{
					1,
					3,
					2
				},
				{
					2,
					1,
					3
				},
				{
					2,
					3,
					1
				},
				{
					3,
					1,
					2
				},
				{
					3,
					2,
					1
				}
			}
			local var_18_2 = math.random(3)
			local var_18_3 = 3
			local var_18_4 = 0
			local var_18_5
			local var_18_6 = 0
			local var_18_7 = 1
			local var_18_8
			local var_18_9 = {}

			for iter_18_0 = 1, 3:
				table.insert(var_18_9, arg_4_0.rtGame.Find(iter_18_0))
				onButton(arg_4_0, var_18_9[iter_18_0].Find("click"), function()
					if var_18_8:
						LeanTween.cancel(var_18_8)

					setCanvasGroupAlpha(arg_4_0.rtGame.Find("Image"), 1)
					setActive(arg_4_0.rtGame.Find("Text"), True)

					var_18_5 = iter_18_0

					if iter_18_0 == var_18_2:
						SetAction(var_18_9[iter_18_0], "action3")
						setText(arg_4_0.rtGame.Find("Text"), i18n("islandnode_tips4"))
					else
						SetAction(var_18_9[iter_18_0], "action4")
						setText(arg_4_0.rtGame.Find("Text"), i18n("islandnode_tips5"))

					for iter_19_0, iter_19_1 in ipairs(var_18_9):
						setButtonEnabled(iter_19_1.Find("click"), False), SFX_PANEL)
				setButtonEnabled(var_18_9[iter_18_0].Find("click"), False)
				SetActionCallback(var_18_9[iter_18_0], function(arg_20_0)
					if arg_20_0 == "finish":
						if iter_18_0 == var_18_5:
							arg_4_0.finishGame(var_18_2 == var_18_5 and 1 or 0)
						elif var_18_6 > 0 or var_18_4 == 5:
							return
						elif var_18_3 > 1:
							var_18_3 = var_18_3 - 1
						else
							var_18_4 = var_18_4 + 1
							var_18_3 = 3

							local function var_20_0()
								local var_21_0 = var_18_7

								var_18_7 = (var_18_7 + math.random(#var_18_1 - 1) - 1) % #var_18_1 + 1

								for iter_21_0, iter_21_1 in ipairs(var_18_1[var_18_7]):
									var_18_6 = var_18_6 + 1

									local var_21_1 = {}

									if iter_21_1 != var_18_1[var_21_0][iter_21_0]:
										SetAction(var_18_9[iter_21_0], iter_21_1 > var_18_1[var_21_0][iter_21_0] and "move_right" or "move_left")
										table.insert(var_21_1, function(arg_22_0)
											LeanTween.moveX(var_18_9[iter_21_0], (iter_21_1 - 2) * 350, var_18_0).setOnComplete(System.Action(arg_22_0)))

									seriesAsync(var_21_1, function()
										SetAction(var_18_9[iter_21_0], "normal1")

										var_18_6 = var_18_6 - 1)

							switch(var_18_4, {
								function()
									for iter_24_0 = 1, 3:
										SetAction(var_18_9[iter_24_0], iter_24_0 == var_18_2 and "action1" or "action2", False),
								var_20_0,
								var_20_0,
								var_20_0,
								function()
									for iter_25_0 = 1, 3:
										setButtonEnabled(var_18_9[iter_25_0].Find("click"), True)

									var_18_8 = LeanTween.alphaCanvas(arg_4_0.rtGame.Find("Image").GetComponent(typeof(CanvasGroup)), 1, 0.5).uniqueId
							}))
				SetAction(var_18_9[iter_18_0], iter_18_0 == var_18_2 and "normal2" or "normal1")

			setText(arg_4_0.rtGame.Find("Image/Text"), i18n("islandnode_tips3"))
			setCanvasGroupAlpha(arg_4_0.rtGame.Find("Image"), 0)
			setActive(arg_4_0.rtGame.Find("Text"), False),
		def Qgame4:()
			local var_26_0 = 5
			local var_26_1 = 0
			local var_26_2 = arg_4_0.rtGame.Find("vine")
			local var_26_3 = var_26_2.GetChild(math.random(var_26_2.childCount) - 1)

			eachChild(var_26_2, function(arg_27_0)
				setActive(arg_27_0, arg_27_0 == var_26_3))
			SetAction(var_26_3, "action1")
			SetActionCallback(var_26_3, function(arg_28_0)
				if arg_28_0 == "finish" and var_26_0 == 0:
					arg_4_0.finishGame(0))
			onButton(arg_4_0, arg_4_0.rtGame.Find("btn"), function()
				local var_29_0 = Time.realtimeSinceStartup

				if var_29_0 - var_26_1 < 1:
					var_26_0 = var_26_0 - 1

					if var_26_0 > 0:
						-- block empty
					else
						setButtonEnabled(arg_4_0.rtGame.Find("btn"), False)
						SetAction(var_26_3, "action2")
				else
					var_26_0 = 4

				var_26_1 = var_29_0, SFX_PANEL),
		def Qgame5:()
			local var_30_0 = 10
			local var_30_1 = 3
			local var_30_2 = 30
			local var_30_3 = 60

			setLocalEulerAngles(arg_4_0.rtGame.Find("hitter/hit_prefect"), {
				z = var_30_2 / 2
			})

			arg_4_0.rtGame.Find("hitter/hit_prefect").GetComponent(typeof(Image)).fillAmount = var_30_2 / 360

			setLocalEulerAngles(arg_4_0.rtGame.Find("hitter/hit_good"), {
				z = var_30_3 / 2
			})

			arg_4_0.rtGame.Find("hitter/hit_good").GetComponent(typeof(Image)).fillAmount = var_30_3 / 360

			local var_30_4 = arg_4_0.rtGame.Find("char")
			local var_30_5 = var_30_4.GetChild(math.random(var_30_4.childCount) - 1)

			eachChild(var_30_4, function(arg_31_0)
				setActive(arg_31_0, arg_31_0 == var_30_5))
			SetAction(var_30_5, "kaorouaction1")

			local var_30_6 = 3
			local var_30_7 = {
				[0] = 0
			}

			for iter_30_0 = 1, var_30_6:
				table.insert(var_30_7, var_30_7[iter_30_0 - 1] + var_30_0 / 3 - 0.1)

			local var_30_8 = arg_4_0.rtGame.Find("Slider")
			local var_30_9 = var_30_8.Find("content")
			local var_30_10 = var_30_9.rect.width
			local var_30_11 = UIItemList.New(var_30_9, var_30_9.Find("mark"))

			var_30_11.make(function(arg_32_0, arg_32_1, arg_32_2)
				arg_32_1 = arg_32_1 + 1

				if arg_32_0 == UIItemList.EventUpdate:
					arg_32_2.name = arg_32_1

					setAnchoredPosition(arg_32_2, {
						x = var_30_10 * var_30_7[arg_32_1] / var_30_0
					}))
			var_30_11.align(#var_30_7)

			local var_30_12 = 0
			local var_30_13
			local var_30_14

			var_30_13 = LeanTween.value(go(var_30_5), 0, var_30_0, var_30_0).setOnUpdate(System.Action_float(function(arg_33_0)
				setSlider(var_30_8, 0, var_30_0, arg_33_0)

				if var_30_7[1] and arg_33_0 >= var_30_7[1]:
					table.remove(var_30_7, 1)
					LeanTween.pause(var_30_13)

					local function var_33_0(arg_34_0)
						if var_30_14:
							LeanTween.cancel(var_30_14)

							var_30_14 = None

						setActive(arg_4_0.rtGame.Find("hitter"), False)
						setActive(arg_4_0.rtGame.Find("click"), False)

						var_30_12 = var_30_12 + arg_34_0

						LeanTween.resume(var_30_13)

					setActive(arg_4_0.rtGame.Find("hitter"), True)

					local var_33_1 = arg_4_0.rtGame.Find("hitter/pointer")

					var_30_14 = LeanTween.value(go(var_33_1), 73.44, -73.44, var_30_1).setOnUpdate(System.Action_float(function(arg_35_0)
						setLocalEulerAngles(var_33_1, {
							z = arg_35_0
						}))).setOnComplete(System.Action(function()
						var_33_0(0))).uniqueId

					setActive(arg_4_0.rtGame.Find("click"), True)
					onButton(arg_4_0, arg_4_0.rtGame.Find("click"), function()
						local var_37_0 = math.min(math.abs(var_33_1.localEulerAngles.z), math.abs(var_33_1.localEulerAngles.z - 360))

						if var_37_0 > var_30_3 / 2:
							var_33_0(0)
						elif var_37_0 > var_30_2 / 2:
							var_33_0(1)
						else
							var_33_0(2), SFX_PANEL))).setOnComplete(System.Action(function()
				local var_38_0 = 2 * math.floor(var_30_12 / (var_30_6 + var_30_6)) + (var_30_12 % (var_30_6 + var_30_6) > 0 and 1 or 0)

				SetAction(var_30_5, "kaorouaction" .. 4 - var_38_0, False)
				SetActionCallback(var_30_5, function(arg_39_0)
					if arg_39_0 == "finish":
						arg_4_0.finishGame(var_38_0)))).uniqueId

			setActive(arg_4_0.rtGame.Find("hitter"), False)
			setActive(arg_4_0.rtGame.Find("click"), False)
	})

def var_0_0.finishGame(arg_40_0, arg_40_1):
	arg_40_0.emit(IslandQTEMiniGameMediator.GAME_FINISH, arg_40_1 or 0)
	arg_40_0.closeView()

def var_0_0.onBackPressed(arg_41_0):
	return

def var_0_0.willExit(arg_42_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_42_0._tf)

	if arg_42_0.handle:
		UpdateBeat.RemoveListener(arg_42_0.handle)

		arg_42_0.handle = None

return var_0_0
