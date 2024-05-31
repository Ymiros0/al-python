ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleEnmeyHpBarView")

var_0_0.Battle.BattleEnmeyHpBarView = var_0_1
var_0_1.__name = "BattleEnmeyHpBarView"

def var_0_1.Ctor(arg_1_0, arg_1_1):
	arg_1_0._monsterTF = arg_1_1
	arg_1_0.orgPos = arg_1_1.anchoredPosition
	arg_1_0.HidePos = arg_1_0.orgPos + Vector2(0, 100)
	arg_1_0._hpBarTF = arg_1_1.Find("hpbar")
	arg_1_0._hpBar = arg_1_0._hpBarTF.gameObject
	arg_1_0._hpBarProgress = arg_1_0._hpBarTF.GetComponent(typeof(Image))
	arg_1_0._hpBarText = arg_1_0._hpBarTF.Find("Text").GetComponent(typeof(Text))
	arg_1_0._nameTF = arg_1_1.Find("nameContain/name")
	arg_1_0._lvText = arg_1_1.Find("nameContain/Text").GetComponent(typeof(Text))
	arg_1_0._level = arg_1_1.Find("level")
	arg_1_0._typeIcon = arg_1_1.Find("typeIcon/icon").GetComponent(typeof(Image))
	arg_1_0._eliteLabel = arg_1_1.Find("grade/elite")
	arg_1_0._generalLabel = arg_1_1.Find("grade/general")
	arg_1_0._flag = True
	arg_1_0._isExistBoos = False

	arg_1_0.Show(False)

def var_0_1.GetCurrentTarget(arg_2_0):
	return arg_2_0._targetUnit

def var_0_1.Show(arg_3_0, arg_3_1):
	if arg_3_0._curActive != arg_3_1:
		arg_3_0._curActive = arg_3_1

		if arg_3_1:
			arg_3_0._monsterTF.anchoredPosition = arg_3_0.orgPos
		else
			arg_3_0._monsterTF.anchoredPosition = arg_3_0.HidePos

def var_0_1.SetIconType(arg_4_0, arg_4_1):
	if arg_4_0._eliteType == arg_4_1:
		return

	arg_4_0._eliteType = arg_4_1

	setActive(arg_4_0._generalLabel, not arg_4_1)
	setActive(arg_4_0._eliteLabel, arg_4_1)

def var_0_1.SwitchTarget(arg_5_0, arg_5_1, arg_5_2):
	for iter_5_0, iter_5_1 in pairs(arg_5_2):
		if iter_5_1.IsBoss():
			arg_5_0._isExistBoos = True

			break

	if arg_5_0._flag == False or arg_5_0._isExistBoos == True:
		arg_5_0.Show(False)

		return

	arg_5_0._targetUnit = arg_5_1

	arg_5_0.Show(True)

	local var_5_0 = arg_5_1.GetHPRate()

	arg_5_0._hpBarProgress.fillAmount = var_5_0

	arg_5_0.UpdateHpText(arg_5_1)
	arg_5_0.SetIconType(arg_5_1.GetTemplate().icon_type != 0)

	local var_5_1 = var_0_0.Battle.BattleDataFunction.GetEnemyTypeDataByType(arg_5_1.GetTemplate().type).type
	local var_5_2 = GetSpriteFromAtlas("shiptype", shipType2Battleprint(var_5_1))

	arg_5_0._typeIcon.sprite = var_5_2

	arg_5_0._typeIcon.SetNativeSize()
	changeToScrollText(arg_5_0._nameTF, arg_5_1._tmpData.name)

	arg_5_0._lvText.text = " Lv." .. arg_5_1.GetLevel()

def var_0_1.UpdateHpText(arg_6_0):
	local var_6_0, var_6_1 = arg_6_0._targetUnit.GetHP()

	arg_6_0._hpBarText.text = tostring(math.floor(var_6_0) .. "/" .. math.floor(var_6_1))

def var_0_1.UpdateHpBar(arg_7_0):
	if arg_7_0._flag == False or arg_7_0._isExistBoos == True:
		return

	LeanTween.cancel(arg_7_0._hpBar)

	local var_7_0 = arg_7_0._targetUnit.GetHPRate()

	arg_7_0.UpdateHpText(target)

	local var_7_1 = arg_7_0._hpBarProgress.fillAmount

	if var_7_0 < var_7_1:
		LeanTween.value(arg_7_0._hpBar, var_7_1, var_7_0, 0.5).setOnUpdate(System.Action_float(function(arg_8_0)
			arg_7_0._hpBarProgress.fillAmount = arg_8_0))
	else
		arg_7_0._hpBarProgress.fillAmount = var_7_0

	if var_7_0 == 0:
		arg_7_0.RemoveUnit()

def var_0_1.RemoveUnit(arg_9_0, arg_9_1):
	arg_9_0._targetUnit = None
	arg_9_0._flag = False

	local function var_9_0()
		arg_9_0._flag = True

		arg_9_0.Show(False)

	if arg_9_1:
		arg_9_0._deathTimer = pg.TimeMgr.GetInstance().AddBattleTimer("death", 0, 1, function()
			var_9_0()
			pg.TimeMgr.GetInstance().RemoveBattleTimer(arg_9_0._deathTimer))
	else
		var_9_0()

def var_0_1.Dispose(arg_12_0):
	arg_12_0.Show(False)
	pg.TimeMgr.GetInstance().RemoveBattleTimer(arg_12_0._deathTimer)
	LeanTween.cancel(arg_12_0._hpBar)

	arg_12_0._hpBarProgress = None
	arg_12_0._hpBar = None
	arg_12_0._hpBarTF = None
	arg_12_0._monsterTF = None
	arg_12_0._monster = None
