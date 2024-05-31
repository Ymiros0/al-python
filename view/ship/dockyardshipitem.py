local var_0_0 = class("DockyardShipItem")

var_0_0.DetailType0 = 0
var_0_0.DetailType1 = 1
var_0_0.DetailType2 = 2
var_0_0.DetailType3 = 3
var_0_0.SKILL_COLOR = {
	COLOR_RED,
	COLOR_BLUE,
	COLOR_YELLOW
}

local var_0_1 = 0.8

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	arg_1_0.go = arg_1_1
	arg_1_0.tr = arg_1_1.transform
	arg_1_0.hideTagFlags = arg_1_2 or {}
	arg_1_0.blockTagFlags = arg_1_3 or {}
	arg_1_0.btn = GetOrAddComponent(arg_1_1, "Button")
	arg_1_0.content = findTF(arg_1_0.tr, "content").gameObject

	setActive(findTF(arg_1_0.content, "dockyard"), True)
	setActive(findTF(arg_1_0.content, "collection"), False)

	arg_1_0.quit = findTF(arg_1_0.tr, "quit_button").gameObject
	arg_1_0.detail = findTF(arg_1_0.tr, "content/dockyard/detail").gameObject
	arg_1_0.detailLayoutTr = findTF(arg_1_0.detail, "layout")
	arg_1_0.imageQuit = arg_1_0.quit.GetComponent("Image")
	arg_1_0.imageFrame = findTF(arg_1_0.tr, "content/front/frame").GetComponent("Image")
	arg_1_0.nameTF = findTF(arg_1_0.tr, "content/info/name_mask/name")
	arg_1_0.npc = findTF(arg_1_0.tr, "content/dockyard/npc")

	setActive(arg_1_0.npc, False)

	arg_1_0.lock = findTF(arg_1_0.tr, "content/dockyard/container/lock")
	arg_1_0.maskStatusOb = findTF(arg_1_0.tr, "content/front/status_mask")
	arg_1_0.iconStatus = findTF(arg_1_0.tr, "content/dockyard/status")
	arg_1_0.iconStatusMask = arg_1_0.iconStatus.GetComponent(typeof(RectMask2D))
	arg_1_0.iconStatusTxt = findTF(arg_1_0.tr, "content/dockyard/status/Text").GetComponent("Text")
	arg_1_0.selectedGo = findTF(arg_1_0.tr, "content/front/selected").gameObject
	arg_1_0.energyTF = findTF(arg_1_0.tr, "content/dockyard/container/energy")
	arg_1_0.proposeTF = findTF(arg_1_0.tr, "content/dockyard/propose")

	arg_1_0.selectedGo.SetActive(False)

	arg_1_0.hpBar = findTF(arg_1_0.tr, "content/dockyard/blood")
	arg_1_0.expBuff = findTF(arg_1_0.tr, "content/expbuff")
	arg_1_0.intimacyTF = findTF(arg_1_0.tr, "content/intimacy")
	arg_1_0.detailType = var_0_0.DetailType0
	arg_1_0.proposeModel = arg_1_0.proposeTF.Find("heartShipCard(Clone)")

	if arg_1_0.proposeModel:
		arg_1_0.sg = GetComponent(arg_1_0.proposeModel, "SkeletonGraphic")

	arg_1_0.activityProxy = getProxy(ActivityProxy)
	arg_1_0.userTF = findTF(arg_1_0.tr, "content/user")

	if arg_1_0.userTF:
		arg_1_0.userIconTF = arg_1_0.userTF.Find("icon").GetComponent(typeof(Image))
		arg_1_0.userIconFrame = arg_1_0.userTF.Find("frame")
		arg_1_0.userNameTF = findTF(arg_1_0.tr, "content/user_name/Text").GetComponent(typeof(Text))
		arg_1_0.levelTF = findTF(arg_1_0.tr, "content/dockyard/lv")

	arg_1_0.tagRecommand = findTF(arg_1_0.tr, "content/recommand")
	arg_1_0.palyerId = getProxy(PlayerProxy).getRawData().id

	ClearTweenItemAlphaAndWhite(arg_1_0.go)

def var_0_0.update(arg_2_0, arg_2_1):
	TweenItemAlphaAndWhite(arg_2_0.go)

	if arg_2_0.proposeModel:
		LeanTween.cancel(arg_2_0.proposeModel)
		LeanTween.value(go(arg_2_0.proposeModel), 0, 1, 0.4).setOnUpdate(System.Action_float(function(arg_3_0)
			arg_2_0.sg.color = Color.New(1, 1, 1, arg_3_0)))

	if arg_2_1:
		arg_2_0.go.name = arg_2_1.configId

	if arg_2_0.shipVO != arg_2_1:
		arg_2_0.shipVO = arg_2_1

		arg_2_0.flush()
		arg_2_0.flushDetail()

	setActive(arg_2_0.nameTF, False)
	setActive(arg_2_0.nameTF, True)

	if not IsNil(arg_2_0.levelTF):
		setActive(arg_2_0.levelTF, False)
		setActive(arg_2_0.levelTF, True)

def var_0_0.updateDetail(arg_4_0, arg_4_1):
	arg_4_0.detailType = arg_4_1

	arg_4_0.flushDetail()

def var_0_0.updateSelected(arg_5_0, arg_5_1):
	arg_5_0.selected = arg_5_1

	arg_5_0.selectedGo.SetActive(arg_5_0.selected)

	if arg_5_0.selected:
		if not arg_5_0.selectedTwId:
			arg_5_0.selectedTwId = LeanTween.alpha(arg_5_0.selectedGo.transform, 0.5, var_0_1).setFrom(0).setEase(LeanTweenType.easeInOutSine).setLoopPingPong().uniqueId
	elif arg_5_0.selectedTwId:
		LeanTween.cancel(arg_5_0.selectedTwId)

		arg_5_0.selectedTwId = None

def var_0_0.flush(arg_6_0):
	local var_6_0 = arg_6_0.shipVO
	local var_6_1 = tobool(var_6_0)

	if var_6_1:
		if not var_6_0.getConfigTable():
			return

		flushShipCard(arg_6_0.tr, var_6_0)

		local var_6_2 = var_6_0.isActivityNpc()

		setActive(arg_6_0.npc, var_6_2)

		if arg_6_0.lock:
			arg_6_0.lock.gameObject.SetActive(var_6_0.GetLockState() == Ship.LOCK_STATE_LOCK)

		local var_6_3 = var_6_0.energy <= Ship.ENERGY_MID

		if var_6_3:
			local var_6_4 = GetSpriteFromAtlas("energy", var_6_0.getEnergyPrint())

			if not var_6_4:
				warning("找不到疲劳")

			setImageSprite(arg_6_0.energyTF, var_6_4)

		setActive(arg_6_0.energyTF, var_6_3)
		setText(arg_6_0.nameTF, var_6_0.GetColorName(shortenString(var_6_0.getName(), PLATFORM_CODE == PLATFORM_US and 6 or 7)))

		local var_6_5

		if var_6_0.user:
			local var_6_6 = Clone(var_6_0)

			var_6_6.id = GuildAssaultFleet.GetRealId(var_6_6.id)
			var_6_5 = ShipStatus.ShipStatusToTag(var_6_6, arg_6_0.hideTagFlags)
		else
			var_6_5 = ShipStatus.ShipStatusToTag(var_6_0, arg_6_0.hideTagFlags)

		if var_6_5:
			arg_6_0.iconStatusTxt.text = var_6_5[3]

			GetSpriteFromAtlasAsync(var_6_5[1], var_6_5[2], function(arg_7_0)
				setImageSprite(arg_6_0.iconStatus, arg_7_0, True)
				setActive(arg_6_0.iconStatus, True)

				if var_6_5[1] == "shipstatus":
					arg_6_0.iconStatus.sizeDelta = Vector2(195, 36)
					arg_6_0.iconStatusTxt.fontSize = 30
					arg_6_0.iconStatusTxt.transform.sizeDelta = Vector2(195, 36)

				arg_6_0.iconStatusMask.enabled = False)
		else
			setActive(arg_6_0.iconStatus, False)

		if not LOCK_PROPOSE:
			if arg_6_0.proposeModel:
				arg_6_0.sg.enabled = arg_6_0.CheckHeartState()
			elif arg_6_0.CheckHeartState() and not arg_6_0.heartLoading:
				arg_6_0.heartLoading = True

				pg.PoolMgr.GetInstance().GetUI("heartShipCard", False, function(arg_8_0)
					if arg_6_0.proposeModel:
						pg.PoolMgr.GetInstance().ReturnUI("heartShipCard", arg_8_0)
					else
						arg_6_0.proposeModel = arg_8_0
						arg_6_0.sg = GetComponent(arg_6_0.proposeModel, "SkeletonGraphic")

						arg_6_0.proposeModel.transform.SetParent(arg_6_0.proposeTF, False)

						arg_6_0.sg.enabled = arg_6_0.CheckHeartState()
						arg_6_0.heartLoading = False)

		if arg_6_0.hpBar:
			setActive(arg_6_0.hpBar, False)

		arg_6_0.UpdateExpBuff()
		arg_6_0.updateNpcTfPosY()

	if arg_6_0.userTF:
		arg_6_0.UpdateUser(var_6_0)

	arg_6_0.content.SetActive(var_6_1)
	arg_6_0.quit.SetActive(not var_6_1)

	arg_6_0.btn.targetGraphic = var_6_1 and arg_6_0.imageFrame or arg_6_0.imageQuit

def var_0_0.CheckHeartState(arg_9_0):
	if tobool(arg_9_0.shipVO):
		local var_9_0, var_9_1 = arg_9_0.shipVO.getIntimacyIcon()
		local var_9_2 = arg_9_0.shipVO.isActivityNpc()

		return var_9_1 and not var_9_2

	return False

local var_0_2 = {
	90,
	60,
	30
}

def var_0_0.updateNpcTfPosY(arg_10_0):
	if isActive(arg_10_0.npc):
		local var_10_0 = 1
		local var_10_1 = findTF(arg_10_0.tr, "content/energy")

		if isActive(var_10_1):
			var_10_0 = var_10_0 + 1

		if isActive(arg_10_0.intimacyTF):
			var_10_0 = var_10_0 + 1

		local var_10_2 = arg_10_0.npc.anchoredPosition

		var_10_2.y = var_0_2[var_10_0]
		arg_10_0.npc.anchoredPosition = var_10_2

def var_0_0.UpdateUser(arg_11_0, arg_11_1):
	if arg_11_0.userIconFrame.childCount > 0:
		local var_11_0 = arg_11_0.userIconFrame.GetChild(0).gameObject

		PoolMgr.GetInstance().ReturnPrefab("IconFrame/" .. var_11_0.name, var_11_0.name, var_11_0)

	local var_11_1 = tobool(arg_11_1) and arg_11_1.user
	local var_11_2 = var_11_1 and var_11_1.id != arg_11_0.palyerId

	setActive(arg_11_0.userTF, var_11_2 and arg_11_0.detailType == var_0_0.DetailType0)
	setActive(arg_11_0.userNameTF.gameObject.transform.parent, var_11_2)

	if var_11_2 and var_11_1 != arg_11_0.user:
		local var_11_3 = Ship.New({
			configId = var_11_1.icon
		})

		LoadSpriteAsync("qicon/" .. var_11_3.getPrefab(), function(arg_12_0)
			arg_11_0.userIconTF.sprite = arg_12_0)

		local var_11_4 = AttireFrame.attireFrameRes(var_11_1, False, AttireConst.TYPE_ICON_FRAME, var_11_1.propose)

		PoolMgr.GetInstance().GetPrefab("IconFrame/" .. var_11_4, var_11_4, True, function(arg_13_0)
			if IsNil(arg_11_0.tr):
				return

			if arg_11_0.userIconFrame:
				arg_13_0.name = var_11_4

				setParent(arg_13_0, arg_11_0.userIconFrame, False)
			else
				PoolMgr.GetInstance().ReturnPrefab("IconFrame/" .. var_11_4, var_11_4, arg_13_0))

		arg_11_0.userNameTF.text = var_11_1.name
		arg_11_0.user = var_11_1

		setAnchoredPosition(arg_11_0.levelTF, {
			x = -108
		})
	else
		setAnchoredPosition(arg_11_0.levelTF, {
			x = -16
		})

def var_0_0.flushDetail(arg_14_0):
	local var_14_0 = arg_14_0.shipVO
	local var_14_1 = tobool(var_14_0)

	if var_14_1 and arg_14_0.detailType > var_0_0.DetailType0:
		local var_14_2 = var_14_0.getShipProperties()
		local var_14_3 = {
			{
				AttributeType.Durability,
				AttributeType.Cannon,
				AttributeType.Torpedo,
				AttributeType.Air,
				AttributeType.Reload,
				AttributeType.Intimacy
			},
			{
				AttributeType.ArmorType,
				AttributeType.AntiAircraft,
				AttributeType.Dodge,
				AttributeType.AntiSub,
				AttributeType.Expend
			},
			{}
		}
		local var_14_4 = var_14_0.getShipCombatPower()
		local var_14_5
		local var_14_6

		if arg_14_0.detailType == var_0_0.DetailType3:
			var_14_5 = var_14_0.getDisplaySkillIds()
			var_14_6 = pg.skill_data_template

		for iter_14_0 = 1, 6:
			local var_14_7 = arg_14_0.detailLayoutTr.GetChild(iter_14_0 - 1)
			local var_14_8 = True
			local var_14_9 = var_14_7.GetChild(0).GetComponent("Text")
			local var_14_10 = var_14_7.GetChild(1).GetComponent("Text")

			var_14_9.alignment = TextAnchor.MiddleLeft
			var_14_10.alignment = TextAnchor.MiddleRight

			local var_14_11 = var_14_3[arg_14_0.detailType][iter_14_0]

			if arg_14_0.detailType == var_0_0.DetailType1:
				if iter_14_0 == 6:
					local var_14_12, var_14_13 = arg_14_0.shipVO.getIntimacyDetail()

					var_14_9.text = AttributeType.Type2Name(var_14_11)
					var_14_10.text = setColorStr(var_14_13, var_14_12 <= var_14_13 and COLOR_GREEN or COLOR_WHITE)
				else
					local var_14_14 = tostring(math.floor(var_14_2[var_14_11]))

					var_14_9.text = AttributeType.Type2Name(var_14_11)
					var_14_10.text = setColorStr(var_14_14, arg_14_0.canModAttr(var_14_0, var_14_11, var_14_2) and COLOR_GREEN or COLOR_WHITE)
			elif arg_14_0.detailType == var_0_0.DetailType2:
				if iter_14_0 == 1:
					var_14_9.alignment = TextAnchor.MiddleCenter
					var_14_9.text = var_14_0.getShipArmorName()
					var_14_10.text = ""
				elif iter_14_0 == 5:
					local var_14_15 = var_14_0.getBattleTotalExpend()

					var_14_9.text = AttributeType.Type2Name(AttributeType.Expend)
					var_14_10.text = tostring(math.floor(var_14_15))
				elif iter_14_0 == 6:
					var_14_9.text = setColorStr(i18n("word_synthesize_power"), COLOR_GREEN)
					var_14_10.text = tostring(var_14_4)
				else
					var_14_9.text = AttributeType.Type2Name(var_14_11)
					var_14_10.text = tostring(math.floor(var_14_2[var_14_11]))
			elif arg_14_0.detailType == var_0_0.DetailType3:
				local var_14_16 = var_14_5[iter_14_0]

				if var_14_16 and var_14_0.skills[var_14_16] and var_14_6[var_14_16].max_level != 1:
					local var_14_17 = var_14_0.skills[var_14_16]
					local var_14_18 = var_0_0.SKILL_COLOR[pg.skill_data_template[var_14_17.id].type] or COLOR_WHITE

					var_14_9.alignment = TextAnchor.MiddleLeft
					var_14_9.text = setColorStr(i18n("skill") .. iter_14_0, var_14_18)

					local var_14_19 = var_14_17.level == var_14_6[var_14_16].max_level and "Lv.Max" or "Lv." .. var_14_17.level

					var_14_10.text = setColorStr(var_14_19, var_14_18)
				else
					var_14_8 = False

			setActive(var_14_7, var_14_8)

	arg_14_0.detail.SetActive(var_14_1 and arg_14_0.detailType > var_0_0.DetailType0)

	if arg_14_0.userTF:
		arg_14_0.UpdateUser(var_14_0)

	arg_14_0.UpdateRecommandTag(var_14_0)

def var_0_0.UpdateRecommandTag(arg_15_0, arg_15_1):
	if arg_15_1 and arg_15_0.tagRecommand:
		local var_15_0 = defaultValue(arg_15_1.guildRecommand, False)

		setActive(arg_15_0.tagRecommand, var_15_0)

def var_0_0.canModAttr(arg_16_0, arg_16_1, arg_16_2, arg_16_3):
	if arg_16_1.isBluePrintShip():
		return arg_16_1.getBluePrint().isMaxIntensifyLevel()
	elif arg_16_1.isMetaShip():
		return arg_16_1.getMetaCharacter().isMaxRepairExp()
	elif not ShipModAttr.ATTR_TO_INDEX[arg_16_2]:
		return True
	elif arg_16_1.getModAttrTopLimit(arg_16_2) == 0:
		return True
	else
		local var_16_0 = arg_16_1.level >= 100 or arg_16_1.level == arg_16_1.getMaxLevel()
		local var_16_1 = arg_16_1.getModAttrBaseMax(arg_16_2)

		return var_16_0 and var_16_1 <= arg_16_3[arg_16_2]

def var_0_0.updateBlackBlock(arg_17_0, arg_17_1):
	local var_17_0 = False

	if arg_17_0.shipVO:
		for iter_17_0, iter_17_1 in pairs(arg_17_0.blockTagFlags):
			if iter_17_1 and arg_17_0.shipVO.getFlag(iter_17_0):
				var_17_0 = True

				break

		if not var_17_0 and arg_17_1:
			local var_17_1 = getProxy(BayProxy)

			for iter_17_2, iter_17_3 in ipairs(arg_17_1):
				local var_17_2 = var_17_1.getShipById(iter_17_3)

				if var_17_2 and arg_17_0.shipVO.isSameKind(var_17_2):
					var_17_0 = var_17_2.id != arg_17_0.shipVO.id

					break

	if arg_17_0.maskStatusOb:
		setActive(arg_17_0.maskStatusOb, var_17_0)

def var_0_0.updateWorld(arg_18_0):
	local var_18_0 = arg_18_0.shipVO

	if var_18_0.getFlag("inWorld"):
		local var_18_1 = WorldConst.FetchWorldShip(var_18_0.id)

		setActive(arg_18_0.hpBar, True)

		local var_18_2 = arg_18_0.hpBar.Find("fillarea/green")
		local var_18_3 = arg_18_0.hpBar.Find("fillarea/red")

		setActive(var_18_2, var_18_1.IsHpSafe())
		setActive(var_18_3, not var_18_1.IsHpSafe())

		arg_18_0.hpBar.GetComponent(typeof(Slider)).fillRect = var_18_1.IsHpSafe() and var_18_2 or var_18_3

		setSlider(arg_18_0.hpBar, 0, 10000, var_18_1.hpRant)
		setActive(arg_18_0.hpBar.Find("broken"), var_18_1.IsBroken())

		if arg_18_0.maskStatusOb:
			setActive(arg_18_0.maskStatusOb, not var_18_1.IsAlive())

def var_0_0.UpdateExpBuff(arg_19_0):
	local var_19_0 = arg_19_0.shipVO
	local var_19_1 = arg_19_0.activityProxy.getBuffShipList()[var_19_0.getGroupId()]

	setActive(arg_19_0.expBuff, False)
	setActive(arg_19_0.expBuff, var_19_1 != None)

	if var_19_1:
		local var_19_2 = var_19_1 / 100
		local var_19_3 = var_19_1 % 100
		local var_19_4 = tostring(var_19_2)

		if var_19_3 > 0:
			var_19_4 = var_19_4 .. "." .. tostring(var_19_3)

		setText(arg_19_0.expBuff.Find("text"), string.format("EXP +%s%%", var_19_4))

def var_0_0.clear(arg_20_0):
	ClearTweenItemAlphaAndWhite(arg_20_0.go)

	if arg_20_0.selectedTwId:
		LeanTween.cancel(arg_20_0.selectedTwId)

		arg_20_0.selectedTwId = None

def var_0_0.updateIntimacy(arg_21_0, arg_21_1):
	local var_21_0 = arg_21_0.shipVO

	if not var_21_0:
		return

	local var_21_1 = findTF(arg_21_0.tr, "content/energy")

	if isActive(var_21_1):
		arg_21_0.intimacyTF = findTF(arg_21_0.tr, "content/intimacy_with_energy")

		setActive(findTF(arg_21_0.tr, "content/intimacy"), False)
	else
		arg_21_0.intimacyTF = findTF(arg_21_0.tr, "content/intimacy")

		setActive(findTF(arg_21_0.tr, "content/intimacy_with_energy"), False)

	local var_21_2, var_21_3 = var_21_0.getIntimacyDetail()

	setText(findTF(arg_21_0.intimacyTF, "Text"), var_21_3)

	if var_21_3 == 100 or var_21_3 == 200:
		setText(findTF(arg_21_0.intimacyTF, "Text"), setColorStr(var_21_3, "#ff8d8d"))

	setActive(arg_21_0.intimacyTF, arg_21_1)
	arg_21_0.updateNpcTfPosY()

def var_0_0.updateIntimacyEnergy(arg_22_0, arg_22_1):
	local var_22_0 = arg_22_0.tr.Find("content/energy")
	local var_22_1 = arg_22_0.shipVO

	setActive(arg_22_0.tr.Find("content/energy"), var_22_1 and arg_22_1)

	if arg_22_1 and tobool(var_22_1):
		local var_22_2 = GetSpriteFromAtlas("energy", var_22_1.getEnergyPrint())

		setImageSprite(var_22_0.Find("icon/img"), var_22_2, True)
		setText(var_22_0.Find("Text"), var_22_1.getEnergy())

return var_0_0
