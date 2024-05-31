ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleUnitEvent
local var_0_2 = class("BattleBossCharacter", var_0_0.Battle.BattleEnemyCharacter)

var_0_0.Battle.BattleBossCharacter = var_0_2
var_0_2.__name = "BattleBossCharacter"

def var_0_2.Ctor(arg_1_0):
	var_0_2.super.Ctor(arg_1_0)

def var_0_2.Dispose(arg_2_0):
	if not arg_2_0._chargeTimer.paused:
		arg_2_0._chargeTimer.Stop()

	if arg_2_0._castClock:
		arg_2_0._castClock.Dispose()

		arg_2_0._castClock = None

	if arg_2_0._aimBiarBar:
		local var_2_0 = arg_2_0._aimBiarBar.GetGO()

		arg_2_0._factory.GetHPBarPool().DestroyObj(var_2_0)
		arg_2_0._aimBiarBar.Dispose()

		arg_2_0._aimBiarBar = None

	LeanTween.cancel(arg_2_0._HPBar)
	var_0_2.super.Dispose(arg_2_0)

def var_0_2.Update(arg_3_0):
	var_0_2.super.Update(arg_3_0)
	arg_3_0.UpdateCastClockPosition()

	if arg_3_0._armor:
		arg_3_0.UpdateCastClock()

	arg_3_0.UpdateBarrierClockPosition()

	if arg_3_0._barrier:
		arg_3_0.updateBarrierClock()

def var_0_2.UpdateVigilantBarPosition(arg_4_0):
	local var_4_0 = arg_4_0._referenceVector + arg_4_0._hpBarOffset

	arg_4_0._vigilantBar.UpdateVigilantBarPosition(var_4_0)

def var_0_2.RegisterWeaponListener(arg_5_0, arg_5_1):
	var_0_2.super.RegisterWeaponListener(arg_5_0, arg_5_1)
	arg_5_1.RegisterEventListener(arg_5_0, var_0_1.WEAPON_INTERRUPT, arg_5_0.onWeaponInterrupted)

def var_0_2.UnregisterWeaponListener(arg_6_0, arg_6_1):
	var_0_2.super.UnregisterWeaponListener(arg_6_0, arg_6_1)
	arg_6_1.UnregisterEventListener(arg_6_0, var_0_1.WEAPON_INTERRUPT)

def var_0_2.AddHPBar(arg_7_0, arg_7_1, arg_7_2):
	arg_7_0._HPBar = arg_7_1
	arg_7_0._HPBarTf = arg_7_1.transform

	arg_7_1.SetActive(True)
	arg_7_0._unitData.RegisterEventListener(arg_7_0, var_0_1.UPDATE_HP, arg_7_0.OnUpdateHP)

	arg_7_0._HPBarCountText = arg_7_0._HPBarTf.Find("HPBarCount").GetComponent(typeof(Text))
	arg_7_0._activeVernier = arg_7_2

	arg_7_0.SetTemplateInfo()
	arg_7_0.initBarComponent()
	arg_7_0.SetHPBarCountText(arg_7_0._HPBarTotalCount)

	arg_7_0._cacheHP = arg_7_0._unitData.GetMaxHP()

	arg_7_0.UpdateHpBar()
	arg_7_0.initBarrierBar()

def var_0_2.SetTemplateInfo(arg_8_0):
	local var_8_0 = arg_8_0._unitData.GetTemplate()
	local var_8_1 = ""

	if var_8_0:
		var_8_1 = var_8_0.name

	changeToScrollText(arg_8_0._HPBarTf.Find("BossName"), var_8_1)

	arg_8_0._HPBarTf.Find("BossLv").GetComponent(typeof(Text)).text = "Lv." .. arg_8_0._unitData.GetLevel()

	local var_8_2 = pg.enemy_data_by_type[var_8_0.type].type
	local var_8_3 = GetSpriteFromAtlas("shiptype", shipType2Battleprint(var_8_2))

	setImageSprite(arg_8_0._HPBarTf.Find("BossIcon/typeIcon/icon"), var_8_3, True)

	local var_8_4 = var_0_0.Battle.BattleResourceManager.GetInstance().GetCharacterSquareIcon(arg_8_0._bossIcon)

	setImageSprite(findTF(arg_8_0._HPBarTf, "BossIcon/icon"), var_8_4)

	arg_8_0._armorBar = arg_8_0._HPBarTf.Find("ArmorBar")
	arg_8_0._armorProgress = arg_8_0._HPBarTf.Find("ArmorBar/armorProgress").GetComponent(typeof(Image))

	SetActive(arg_8_0._armorBar, False)

	arg_8_0._barrierBar = arg_8_0._HPBarTf.Find("ShieldBar")
	arg_8_0._barrierProgress = arg_8_0._barrierBar.Find("shieldProgress").GetComponent(typeof(Image))

	SetActive(arg_8_0._barrierBar, False)

def var_0_2.SetBossData(arg_9_0, arg_9_1):
	arg_9_0._bossBarInfoList = {}
	arg_9_0._HPBarTotalCount = arg_9_1.hpBarNum or 1
	arg_9_0._hideBarNum = arg_9_1.hideBarNum
	arg_9_0._bossIcon = arg_9_0.GetUnitData().GetTemplate().icon
	arg_9_0._bossIndex = arg_9_1.bossCount

def var_0_2.GetBossIndex(arg_10_0):
	return arg_10_0._bossIndex

def var_0_2.initBarComponent(arg_11_0):
	arg_11_0._stepHP = arg_11_0.GetUnitData().GetMaxHP() / arg_11_0._HPBarTotalCount

	local var_11_0 = 1

	arg_11_0._resTotalCount = 5
	arg_11_0._bossBarInfoList = {}

	while var_11_0 <= arg_11_0._resTotalCount:
		local var_11_1 = {}
		local var_11_2 = "bloodBarContainer/hp_" .. var_11_0
		local var_11_3 = var_11_2 .. "_delta"
		local var_11_4 = arg_11_0._HPBarTf.Find(var_11_2)
		local var_11_5 = arg_11_0._HPBarTf.Find(var_11_3)

		var_11_1.progressImage = var_11_4.GetComponent(typeof(Image))
		var_11_1.deltaImage = var_11_5.GetComponent(typeof(Image))
		var_11_1.progressTF = var_11_4.transform
		var_11_1.deltaTF = var_11_5.transform
		var_11_1.progressImage.fillAmount = 1
		var_11_1.deltaImage.fillAmount = 1
		arg_11_0._bossBarInfoList[var_11_0] = var_11_1
		var_11_0 = var_11_0 + 1

	arg_11_0._topBarIndex = arg_11_0._HPBarTf.childCount - 1
	arg_11_0._currentFmod = math.fmod(arg_11_0._HPBarTotalCount, arg_11_0._resTotalCount)

	if arg_11_0._currentFmod == 0:
		arg_11_0._currentFmod = arg_11_0._resTotalCount

	if arg_11_0._HPBarTotalCount < 5:
		local var_11_6 = arg_11_0._resTotalCount

		while var_11_6 > arg_11_0._HPBarTotalCount:
			local var_11_7 = "bloodBarContainer/hp_" .. var_11_6

			SetActive(arg_11_0._HPBarTf.Find(var_11_7), False)
			SetActive(arg_11_0._HPBarTf.Find(var_11_7 .. "_delta"), False)

			var_11_6 = var_11_6 - 1
	else
		local var_11_8 = arg_11_0._resTotalCount

		while var_11_8 > arg_11_0._currentFmod:
			local var_11_9 = "bloodBarContainer/hp_" .. var_11_8

			arg_11_0._HPBarTf.Find(var_11_9).transform.SetSiblingIndex(0)
			arg_11_0._HPBarTf.Find(var_11_9 .. "_delta").transform.SetSiblingIndex(0)

			var_11_8 = var_11_8 - 1

	if arg_11_0._activeVernier:
		arg_11_0._vernier = arg_11_0._HPBarTf.Find("vernier/tag")

		SetActive(arg_11_0._HPBarTf.Find("vernier"), arg_11_0._activeVernier)

	arg_11_0._chargeTimer = Timer.New(function()
		arg_11_0._currentTween = arg_11_0.generateTween(), 1)

def var_0_2.UpdateHpBar(arg_13_0):
	local var_13_0 = arg_13_0._unitData.GetCurrentHP()

	if arg_13_0._cacheHP == var_13_0:
		return

	if not arg_13_0._chargeTimer.paused:
		arg_13_0._chargeTimer.Stop()
		arg_13_0._chargeTimer.Stop()
		arg_13_0._chargeTimer.Reset()

	local var_13_1, var_13_2, var_13_3 = arg_13_0.GetCurrentFmod()

	arg_13_0.SortBar(var_13_1, var_13_3)

	arg_13_0._currentFmod = var_13_1
	arg_13_0._currentDivision = var_13_3

	if var_13_0 < arg_13_0._cacheHP:
		if arg_13_0._currentDivision != var_13_3:
			LeanTween.cancel(arg_13_0._HPBar)

		arg_13_0._chargeTimer.Start()

	arg_13_0._bossBarInfoList[var_13_1].progressImage.fillAmount = var_13_2

	if arg_13_0._activeVernier:
		arg_13_0._vernier.anchorMin = Vector2(currentRate, 0.5)
		arg_13_0._vernier.anchorMax = Vector2(currentRate, 0.5)

	arg_13_0.SetHPBarCountText(var_13_3)

	arg_13_0._cacheHP = var_13_0

def var_0_2.generateTween(arg_14_0):
	local var_14_0 = arg_14_0._bossBarInfoList[arg_14_0._currentFmod]
	local var_14_1 = var_14_0.deltaImage
	local var_14_2 = var_14_0.progressImage.fillAmount

	duration = duration or 0.7

	return (LeanTween.value(go(arg_14_0._HPBar), var_14_1.fillAmount, var_14_2, 0.7).setOnUpdate(System.Action_float(function(arg_15_0)
		var_14_1.fillAmount = arg_15_0)))

def var_0_2.GetCurrentFmod(arg_16_0):
	local var_16_0 = arg_16_0._unitData.GetCurrentHP()
	local var_16_1, var_16_2 = math.modf(var_16_0 / arg_16_0._stepHP)
	local var_16_3 = var_16_1 + 1
	local var_16_4 = math.fmod(var_16_3, arg_16_0._resTotalCount)

	if var_16_4 == 0:
		var_16_4 = 5

	return var_16_4, var_16_2, var_16_3

def var_0_2.SortBar(arg_17_0, arg_17_1, arg_17_2):
	if arg_17_1 == arg_17_0._currentFmod:
		return
	elif arg_17_1 > arg_17_0._currentFmod:
		local var_17_0 = arg_17_0._currentFmod

		arg_17_0._bossBarInfoList[var_17_0].progressImage.fillAmount = 1
		arg_17_0._bossBarInfoList[var_17_0].deltaImage.fillAmount = 1

		while var_17_0 < arg_17_1:
			var_17_0 = var_17_0 + 1

			local var_17_1 = arg_17_0._bossBarInfoList[var_17_0]

			var_17_1.deltaTF.SetSiblingIndex(arg_17_0._topBarIndex)
			var_17_1.progressTF.SetSiblingIndex(arg_17_0._topBarIndex)
			SetActive(var_17_1.progressImage, True)
			SetActive(var_17_1.deltaImage, True)
	elif arg_17_1 < arg_17_0._currentFmod:
		local var_17_2 = arg_17_0._currentFmod

		while arg_17_1 < var_17_2:
			local var_17_3 = arg_17_0._bossBarInfoList[var_17_2]

			var_17_3.progressImage.fillAmount = 1
			var_17_3.deltaImage.fillAmount = 1

			var_17_3.progressTF.SetSiblingIndex(0)
			var_17_3.deltaTF.SetSiblingIndex(0)

			if arg_17_2 < arg_17_0._resTotalCount:
				SetActive(var_17_3.progressImage, False)
				SetActive(var_17_3.deltaImage, False)

			var_17_2 = var_17_2 - 1

def var_0_2.SetHPBarCountText(arg_18_0, arg_18_1):
	if arg_18_0._hideBarNum:
		arg_18_0._HPBarCountText.text = "X??"
	else
		arg_18_0._HPBarCountText.text = "X " .. arg_18_1

def var_0_2.UpdateHPBarPosition(arg_19_0):
	if arg_19_0._normalHPTF and not arg_19_0._hideHP:
		arg_19_0._hpBarPos.Copy(arg_19_0._referenceVector).Add(arg_19_0._hpBarOffset)

		arg_19_0._normalHPTF.position = arg_19_0._hpBarPos

def var_0_2.onWeaponPreCast(arg_20_0, arg_20_1):
	var_0_2.super.onWeaponPreCast(arg_20_0, arg_20_1)

	local var_20_0 = arg_20_1.Data
	local var_20_1 = var_20_0.armor

	arg_20_0.initArmorBar(var_20_0.armor)

	if var_20_1 and var_20_1 != 0:
		arg_20_0.initCastClock(var_20_0.time, arg_20_1.Dispatcher)

def var_0_2.onWeaponPrecastFinish(arg_21_0, arg_21_1):
	var_0_2.super.onWeaponPrecastFinish(arg_21_0, arg_21_1)

	local var_21_0 = arg_21_1.Data.armor
	local var_21_1 = arg_21_1.Dispatcher

	if arg_21_0._castClock.GetCastingWeapon() == var_21_1 and var_21_0 and var_21_0 != 0:
		if arg_21_0._armor <= 0:
			arg_21_0._castClock.Interrupt(True)
		else
			arg_21_0._castClock.Interrupt(False)

		arg_21_0._armor = None

		SetActive(arg_21_0._armorBar, False)

def var_0_2.onWeaponInterrupted(arg_22_0, arg_22_1):
	arg_22_0._unitData.StateChange(var_0_0.Battle.UnitState.STATE_INTERRUPT)

def var_0_2.initArmorBar(arg_23_0, arg_23_1):
	if arg_23_1 and arg_23_1 != 0:
		arg_23_0._armor = arg_23_1
		arg_23_0._totalArmor = arg_23_1

		arg_23_0.updateWeaponArmor()
		SetActive(arg_23_0._armorBar, True)

def var_0_2.OnUpdateHP(arg_24_0, arg_24_1):
	local var_24_0 = arg_24_1.Data.preShieldHP

	if arg_24_0._barrier and var_24_0 < 0:
		arg_24_0._barrier = arg_24_0._barrier + var_24_0

		arg_24_0.updateBarrierBar()

	var_0_2.super.OnUpdateHP(arg_24_0, arg_24_1)

	local var_24_1 = arg_24_1.Data.dHP

	if arg_24_0._armor and var_24_1 < 0:
		arg_24_0._armor = arg_24_0._armor + var_24_1

		arg_24_0.updateWeaponArmor()

def var_0_2.updateWeaponArmor(arg_25_0):
	arg_25_0._armorProgress.fillAmount = arg_25_0._armor / arg_25_0._totalArmor

def var_0_2.initCastClock(arg_26_0, arg_26_1, arg_26_2):
	arg_26_0._castClock.Casting(arg_26_1, arg_26_2)

	arg_26_0._castFinishTime = pg.TimeMgr.GetInstance().GetCombatTime() + arg_26_1
	arg_26_0._castDuration = arg_26_1

def var_0_2.UpdateCastClock(arg_27_0):
	arg_27_0._castClock.UpdateCastClock()

def var_0_2.updateComponentDiveInvisible(arg_28_0):
	var_0_2.super.updateComponentDiveInvisible(arg_28_0)
	SetActive(arg_28_0._HPBarTf, True)

def var_0_2.updateComponentVisible(arg_29_0):
	var_0_2.super.updateComponentVisible(arg_29_0)
	SetActive(arg_29_0._HPBarTf, True)

def var_0_2.initBarrierBar(arg_30_0):
	arg_30_0._unitData.RegisterEventListener(arg_30_0, var_0_1.BARRIER_STATE_CHANGE, arg_30_0.onBarrierStateChange)

def var_0_2.onBarrierStateChange(arg_31_0, arg_31_1):
	local var_31_0 = arg_31_1.Data.barrierDurability
	local var_31_1 = arg_31_1.Data.barrierDuration

	SetActive(arg_31_0._barrierBar, var_31_0 > 0)

	if var_31_0 > 0:
		arg_31_0._totalBarrier = var_31_0
		arg_31_0._barrier = var_31_0

		arg_31_0.initBarrierClock(var_31_1)
		arg_31_0.updateBarrierBar()
		arg_31_0.updateBarrierClock()
	else
		arg_31_0._barrier = None
		arg_31_0._totalBarrier = None

		arg_31_0._barrierClock.Interrupt()

def var_0_2.updateBarrierBar(arg_32_0):
	arg_32_0._barrierProgress.fillAmount = arg_32_0._barrier / arg_32_0._totalBarrier

def var_0_2.updateBarrierClock(arg_33_0):
	arg_33_0._barrierClock.UpdateBarrierClockProgress()

def var_0_2.initBarrierClock(arg_34_0, arg_34_1):
	arg_34_0._barrierClock.Shielding(arg_34_1)

def var_0_2.AddAimBiasBar(arg_35_0, arg_35_1):
	arg_35_0._normalHPTF = arg_35_1
	arg_35_0._aimBiarBarTF = arg_35_1.Find("biasBar")
	arg_35_0._aimBiarBar = var_0_0.Battle.BattleAimbiasBar.New(arg_35_0._aimBiarBarTF)

	arg_35_0._aimBiarBar.ConfigAimBias(arg_35_0._unitData.GetAimBias())
	arg_35_0._aimBiarBar.UpdateAimBiasProgress()

def var_0_2.AddModel(arg_36_0, arg_36_1):
	var_0_2.super.AddModel(arg_36_0, arg_36_1)
	arg_36_0.UpdatePosition()
