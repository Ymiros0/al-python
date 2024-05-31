local var_0_0 = import(".LevelGrid")
local var_0_1 = Vector2(-60, 84.8)
local var_0_2 = Vector2(-50, 20)

function var_0_0.PlaySubAnimation(arg_1_0, arg_1_1, arg_1_2, arg_1_3)
	if not arg_1_1 then
		arg_1_3()

		return
	end

	local var_1_0 = arg_1_1:GetSpineRole()

	if not var_1_0 then
		arg_1_3()

		return
	end

	local var_1_1 = arg_1_0.contextData.chapterVO

	var_1_0:SetAction(arg_1_2 and ChapterConst.ShipSwimAction or ChapterConst.ShipIdleAction)
	arg_1_1:PlayShuiHua()

	local var_1_2 = var_1_1:GetQuickPlayFlag() and 0.1 or 0.3
	local var_1_3 = arg_1_2 and 1 or 0
	local var_1_4 = arg_1_2 and 0 or 1

	arg_1_0:frozen()
	var_1_0:TweenShining(var_1_2, nil, var_1_3, var_1_4, Color.New(1, 1, 1, 0), Color.New(1, 1, 1, 1), false, false, function(arg_2_0)
		if not IsNil(arg_1_1.tfAmmo) then
			arg_1_1.tfAmmo.anchoredPosition = Vector2.Lerp(var_0_2, var_0_1, arg_2_0)
		end
	end, function()
		if arg_1_0.exited then
			return
		end

		arg_1_0:unfrozen()
		arg_1_1:SetActiveModel(not arg_1_2)

		if arg_1_3 then
			arg_1_3()
		end
	end)
end

function var_0_0.TeleportCellByPortalWithCameraMove(arg_4_0, arg_4_1, arg_4_2, arg_4_3, arg_4_4)
	local var_4_0

	local function var_4_1(arg_5_0)
		var_4_0 = arg_5_0
	end

	local function var_4_2(arg_6_0)
		arg_4_0:TeleportFleetByPortal(arg_4_2, arg_4_3, function()
			arg_4_0:focusOnCell(arg_4_1.line, var_4_0)
		end, arg_6_0)
	end

	parallelAsync({
		var_4_1,
		var_4_2
	}, arg_4_4)
end

function var_0_0.TeleportFleetByPortal(arg_8_0, arg_8_1, arg_8_2, arg_8_3, arg_8_4)
	local var_8_0 = arg_8_0.contextData.chapterVO
	local var_8_1 = arg_8_2[1]
	local var_8_2 = arg_8_2[2]

	if not var_8_1 or not var_8_2 then
		arg_8_4()

		return
	end

	local var_8_3 = arg_8_1:GetSpineRole()

	if not var_8_3 then
		arg_8_4()

		return
	end

	arg_8_0:frozen()

	local var_8_4 = var_8_0:GetQuickPlayFlag() and 0.1 or 0.3

	var_8_3:TweenShining(var_8_4, nil, 1, 0, Color.New(1, 1, 1, 0), Color.New(1, 1, 1, 1), false, false, nil, function()
		if arg_8_0.exited then
			return
		end

		if arg_8_3 then
			arg_8_3()
		end

		arg_8_0:updateFleet(table.indexof(arg_8_0.cellFleets, arg_8_1))
		var_8_3:TweenShining(var_8_4, nil, 0, 1, Color.New(1, 1, 1, 0), Color.New(1, 1, 1, 1), false, false, nil, function()
			if arg_8_0.exited then
				return
			end

			arg_8_0:unfrozen()
			existCall(arg_8_4)
		end)
	end)
end

function var_0_0.adjustCameraFocus(arg_11_0, arg_11_1)
	local var_11_0 = arg_11_0.contextData.chapterVO
	local var_11_1 = var_11_0.fleets[var_11_0.findex].id
	local var_11_2 = arg_11_0.cellFleets[var_11_1]

	if var_11_2 then
		arg_11_0:cameraFocus(var_11_2.tf.position, arg_11_1)
	else
		existCall(arg_11_1)
	end
end

function var_0_0.focusOnCell(arg_12_0, arg_12_1, arg_12_2)
	local var_12_0 = ChapterCell.Line2Name(arg_12_1.row, arg_12_1.column)
	local var_12_1 = arg_12_0.cellRoot:Find(var_12_0)

	arg_12_0:cameraFocus(var_12_1.position, arg_12_2)
end

function var_0_0.cameraFocus(arg_13_0, arg_13_1, arg_13_2)
	local var_13_0 = arg_13_0.contextData.chapterVO.theme
	local var_13_1 = arg_13_0._tf:Find(ChapterConst.PlaneName)

	assert(var_13_1, "plane not exist.")
	LeanTween.cancel(arg_13_0._tf.gameObject, true)

	local var_13_2 = arg_13_0._tf.parent:InverseTransformVector(arg_13_1 - var_13_1.position)

	var_13_2.x = var_13_2.x + var_13_1.localPosition.x
	var_13_2.y = var_13_2.y + var_13_1.localPosition.y - var_13_1.localPosition.z * math.tan(math.pi / 180 * var_13_0.angle)
	var_13_2.x = math.clamp(-var_13_2.x, arg_13_0.leftBound, arg_13_0.rightBound)
	var_13_2.y = math.clamp(-var_13_2.y, arg_13_0.bottomBound, arg_13_0.topBound)
	var_13_2.z = 0
	arg_13_0.dragTrigger.enabled = false

	LeanTween.moveLocal(arg_13_0._tf.gameObject, var_13_2, 0.4):setEase(LeanTweenType.easeInOutSine):setOnComplete(System.Action(function()
		if arg_13_0.exited then
			return
		end

		arg_13_0.dragTrigger.enabled = true

		existCall(arg_13_2)
	end))
end

function var_0_0.PlayChampionSubmarineAnimation(arg_15_0, arg_15_1, arg_15_2, arg_15_3)
	local var_15_0 = arg_15_0.contextData.chapterVO:getChampionIndex(arg_15_1.row, arg_15_1.column)

	if not var_15_0 or var_15_0 <= 0 then
		if arg_15_3 then
			arg_15_3()
		end

		return
	end

	local var_15_1 = arg_15_0.cellChampions[var_15_0]

	if not var_15_1 then
		if arg_15_3 then
			arg_15_3()
		end

		return
	end

	arg_15_0:PlaySubAnimation(var_15_1, arg_15_2, arg_15_3)
end

function var_0_0.shakeCell(arg_16_0, arg_16_1, arg_16_2)
	local var_16_0 = arg_16_0.contextData.chapterVO
	local var_16_1
	local var_16_2 = var_16_0:getChampion(arg_16_1.row, arg_16_1.column)
	local var_16_3 = var_16_0:getChapterCell(arg_16_1.row, arg_16_1.column)

	if var_16_2 and var_16_2.flag == ChapterConst.CellFlagActive then
		local var_16_4 = var_16_0:getChampionIndex(arg_16_1.row, arg_16_1.column)

		var_16_1 = arg_16_0.cellChampions[var_16_4].tf
	elseif ChapterConst.IsEnemyAttach(var_16_3.attachment) then
		local var_16_5 = ChapterCell.Line2Name(arg_16_1.row, arg_16_1.column)

		var_16_1 = arg_16_0.attachmentCells[var_16_5].tf
	else
		existCall(arg_16_2)

		return
	end

	local var_16_6 = var_16_1.localPosition.x
	local var_16_7 = var_16_1.localPosition

	var_16_7.x = var_16_6 + 10
	var_16_1.localPosition = var_16_7

	LeanTween.moveX(var_16_1, var_16_6 - 10, 0.05):setEase(LeanTweenType.easeInOutSine):setLoopPingPong(3):setOnComplete(System.Action(function()
		local var_17_0 = var_16_1.localPosition

		var_17_0.x = var_16_6
		var_16_1.localPosition = var_17_0

		if arg_16_2 then
			arg_16_2()
		end
	end))
	arg_16_0:PlayAttachmentEffect(arg_16_1.row, arg_16_1.column, "huoqiubaozha", Vector2.zero)

	return var_16_1
end

function var_0_0.PlayShellFx(arg_18_0, arg_18_1, arg_18_2)
	local var_18_0 = ChapterCell.Line2Name(arg_18_1.row, arg_18_1.column)
	local var_18_1 = arg_18_0.cellRoot:Find(var_18_0):Find(ChapterConst.ChildAttachment)
	local var_18_2 = arg_18_1.row * ChapterConst.PriorityPerRow + ChapterConst.CellPriorityUpperEffect
	local var_18_3

	seriesAsync({
		function(arg_19_0)
			arg_18_0.loader:GetPrefab("effect/ATdun_full_SLG", "ATdun_full_SLG", function(arg_20_0)
				setParent(arg_20_0, var_18_1)
				pg.ViewUtils.SetSortingOrder(arg_20_0, var_18_2)

				var_18_3 = arg_20_0

				arg_19_0()
			end)
		end,
		function(arg_21_0)
			Timer.New(arg_21_0, 1, nil, true):Start()
		end,
		function(arg_22_0)
			if arg_18_0.exited then
				return
			end

			arg_18_0.loader:ReturnPrefab(var_18_3)
			existCall(arg_18_2)
		end
	})
end

function var_0_0.PlayMissileExplodAnim(arg_23_0, arg_23_1, arg_23_2)
	local var_23_0 = ChapterCell.Line2Name(arg_23_1.row, arg_23_1.column)
	local var_23_1 = arg_23_0.cellRoot:Find(var_23_0):Find(ChapterConst.ChildAttachment)
	local var_23_2 = arg_23_1.row * ChapterConst.PriorityPerRow + ChapterConst.CellPriorityAttachment
	local var_23_3
	local var_23_4
	local var_23_5

	parallelAsync({
		function(arg_24_0)
			arg_23_0.loader:GetPrefab("effect/dexiv4_SLG_missile", "dexiv4_SLG_missile", function(arg_25_0)
				setParent(arg_25_0, var_23_1)
				setActive(arg_25_0, false)
				pg.ViewUtils.SetSortingOrder(arg_25_0, var_23_2)

				var_23_3 = arg_25_0

				arg_24_0()
			end)
		end,
		function(arg_26_0)
			arg_23_0.loader:GetPrefab("effect/ShellHitBlue", "ShellHitBlue", function(arg_27_0)
				setParent(arg_27_0, var_23_1)
				setActive(arg_27_0, false)
				pg.ViewUtils.SetSortingOrder(arg_27_0, var_23_2)

				var_23_4 = arg_27_0

				arg_26_0()
			end)
		end
	}, function()
		seriesAsync({
			function(arg_29_0)
				local var_29_0 = Vector3(150, 600)

				setLocalPosition(var_23_3, var_29_0)

				tf(var_23_3).localRotation = Quaternion.FromToRotation(Vector3.right, -var_29_0)

				setActive(var_23_3, true)

				var_23_5 = LeanTween.moveLocal(go(var_23_3), Vector3.zero, 0.7):setEase(LeanTweenType.easeInOutSine):setOnComplete(System.Action(arg_29_0)).id
				arg_23_0.tweens[var_23_5] = true
			end,
			function(arg_30_0)
				arg_23_0.tweens[var_23_5] = nil

				arg_23_0.loader:ReturnPrefab(var_23_3)

				var_23_3 = nil

				setActive(var_23_4, true)
				setLocalScale(var_23_4, Vector3.one)

				local var_30_0 = go(var_23_4):GetComponent(typeof(ParticleSystemEvent))

				var_30_0:SetEndEvent(function(arg_31_0)
					var_30_0:SetEndEvent(nil)
					arg_23_0.loader:ReturnPrefab(var_23_4)

					var_23_4 = nil
				end)
				arg_30_0()
			end,
			arg_23_2
		})
	end)
end

function var_0_0.PlaySonarDetectAnim(arg_32_0, arg_32_1, arg_32_2)
	existCall(arg_32_2)
end

function var_0_0.PlayAttachmentEffect(arg_33_0, arg_33_1, arg_33_2, arg_33_3, arg_33_4, arg_33_5)
	local var_33_0 = ChapterCell.Line2Name(arg_33_1, arg_33_2)
	local var_33_1 = arg_33_0.cellRoot:Find(var_33_0)

	if not var_33_1 then
		existCall(arg_33_5)

		return
	end

	local var_33_2 = var_33_1:Find(ChapterConst.ChildAttachment)

	arg_33_0:PlayParticleSystem(arg_33_3, var_33_2, arg_33_4, arg_33_5)
end

function var_0_0.PlayParticleSystem(arg_34_0, arg_34_1, arg_34_2, arg_34_3, arg_34_4)
	arg_34_0.loader:GetPrefab("effect/" .. arg_34_1, arg_34_1, function(arg_35_0)
		setParent(arg_35_0, arg_34_2)

		if arg_34_3 then
			tf(arg_35_0).localPosition = arg_34_3
		end

		arg_35_0:GetComponent(typeof(ParticleSystem)):Play()

		local var_35_0 = arg_35_0:GetComponent(typeof(ParticleSystemEvent))

		if not IsNil(var_35_0) then
			var_35_0:SetEndEvent(function(arg_36_0)
				arg_34_0.loader:ReturnPrefab(arg_35_0)
				existCall(arg_34_4)
			end)
		end
	end)
end
