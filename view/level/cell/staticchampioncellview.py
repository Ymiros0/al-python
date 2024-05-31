local var_0_0 = import(".StaticCellView")
local var_0_1 = import(".ChampionCellView")
local var_0_2 = class("StaticChampionCellView", DecorateClass(var_0_0, var_0_1))

def var_0_2.Ctor(arg_1_0, arg_1_1):
	var_0_0.Ctor(arg_1_0, arg_1_1)
	var_0_1.Ctor(arg_1_0)

def var_0_2.GetOrder(arg_2_0):
	return ChapterConst.CellPriorityEnemy

def var_0_2.InitChampionCellTransform(arg_3_0):
	var_0_1.InitChampionCellTransform(arg_3_0)

	arg_3_0.textLV = arg_3_0.tf.Find("lv/Text")
	arg_3_0.tfBossIcon = arg_3_0.tf.Find("titleContain/bg_boss")
	arg_3_0.tfEffectFoundBoss = arg_3_0.tf.Find("effect_found_boss")

def var_0_2.Update(arg_4_0):
	local var_4_0 = arg_4_0.info
	local var_4_1 = arg_4_0.config
	local var_4_2 = var_4_0.trait != ChapterConst.TraitLurk

	if ChapterConst.IsEnemyAttach(var_4_0.attachment) and var_4_0.flag == ChapterConst.CellFlagActive and arg_4_0.chapter.existFleet(FleetType.Transport, var_4_0.row, var_4_0.column):
		var_4_2 = False

	if not IsNil(arg_4_0.go):
		setActive(arg_4_0.go, var_4_2)

	if not var_4_2:
		return

	if IsNil(arg_4_0.go):
		arg_4_0.GetLoader().GetPrefab("leveluiview/Tpl_StaticChampion", "Tpl_StaticChampion", function(arg_5_0)
			arg_5_0.name = "enemy_" .. var_4_0.attachmentId
			arg_4_0.go = arg_5_0
			arg_4_0.tf = tf(arg_5_0)

			setParent(arg_5_0, arg_4_0.parent)
			arg_4_0.OverrideCanvas()
			arg_4_0.ResetCanvasOrder()
			setAnchoredPosition(arg_4_0.tf, Vector2.zero)
			arg_4_0.InitChampionCellTransform()
			var_0_2.StartEggCellView(arg_4_0, var_4_1)
			SpineCellView.SetAction(arg_4_0, ChapterConst.ShipIdleAction)
			var_0_1.LoadSpine(arg_4_0, var_4_1.icon, var_4_1.scale, var_4_1.effect_prefab)
			arg_4_0.Update(), "Main")

		return

	arg_4_0.UpdateChampionCell(arg_4_0.chapter, var_4_0)

def var_0_2.UpdateChampionCell(arg_6_0, arg_6_1, arg_6_2, arg_6_3):
	local var_6_0 = arg_6_2.trait != ChapterConst.TraitLurk and arg_6_2.flag == ChapterConst.CellFlagActive and not arg_6_1.existFleet(FleetType.Transport, arg_6_2.row, arg_6_2.column)
	local var_6_1 = arg_6_1.existEnemy(ChapterConst.SubjectChampion, arg_6_2.row, arg_6_2.column)

	setActive(arg_6_0.tfFighting, var_6_0 and var_6_1)
	setActive(arg_6_0.tfDamageCount, var_6_0 and arg_6_2.data > 0)

	local var_6_2 = arg_6_2.trait == ChapterConst.TraitVirgin
	local var_6_3 = ChapterConst.IsBossCell(arg_6_2)

	setActive(arg_6_0.tfEffectFound, var_6_2 and not var_6_3)
	setActive(arg_6_0.tfEffectFoundBoss, var_6_2 and var_6_3)

	if var_6_2:
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_UI_WEIGHANCHOR_ENEMY)

	arg_6_0.tfShadow.localEulerAngles = Vector3(arg_6_1.theme.angle, 0, 0)

	if var_6_0:
		EnemyCellView.RefreshEnemyTplIcons(arg_6_0, arg_6_0.config, arg_6_1)

	arg_6_0.SetActive(var_6_0)
	existCall(arg_6_3)

def var_0_2.StartEggCellView(arg_7_0, arg_7_1, arg_7_2):
	if ChapterConst.EnemySize[arg_7_1.type] == 99:
		setActive(arg_7_0.tfBossIcon, True)
		arg_7_0.GetLoader().GetSpriteQuiet("ui/share/ship_gizmos_atlas", "enemy_boss", arg_7_0.tfBossIcon)
	elif ChapterConst.EnemySize[arg_7_1.type] == 98:
		setActive(arg_7_0.tfBossIcon, True)
		arg_7_0.GetLoader().GetSpriteQuiet("ui/share/ship_gizmos_atlas", "enemy_elite", arg_7_0.tfBossIcon)
	else
		setActive(arg_7_0.tfBossIcon, False)

	arg_7_0.tfBossIcon.localScale = Vector3(0.5, 0.5, 1)
	arg_7_0.tfBossIcon.anchoredPosition = Vector2(61.1, -30.6)

	setText(arg_7_0.textLV, arg_7_1.level)
	existCall(arg_7_2)

def var_0_2.Clear(arg_8_0):
	var_0_1.Clear(arg_8_0)
	var_0_0.Clear(arg_8_0)

return var_0_2
