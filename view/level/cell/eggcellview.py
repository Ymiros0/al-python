local var_0_0 = class("EggCellView", import(".EnemyCellView"))

def var_0_0.InitEggCellTransform(arg_1_0):
	arg_1_0.tfIcon = arg_1_0.tf.Find("icon")
	arg_1_0.tfBufficons = arg_1_0.tf.Find("random_buff_container")
	arg_1_0.tfBossIcon = arg_1_0.tf.Find("titleContain/bg_boss")
	arg_1_0.textLV = arg_1_0.tf.Find("lv/Text")
	arg_1_0.tfEffectFound = arg_1_0.tf.Find("effect_found")
	arg_1_0.tfEffectFoundBoss = arg_1_0.tf.Find("effect_found_boss")
	arg_1_0.tfFighting = arg_1_0.tf.Find("fighting")

	setText(findTF(arg_1_0.tfFighting, "Text"), i18n("ui_word_levelui2_inevent"))

	arg_1_0.tfDamageCount = arg_1_0.tf.Find("damage_count")
	arg_1_0.animator = GetComponent(arg_1_0.go, typeof(Animator))
	arg_1_0.effectFireball = arg_1_0.tf.Find("huoqiubaozha")

def var_0_0.StartEggCellView(arg_2_0, arg_2_1, arg_2_2):
	if ChapterConst.EnemySize[arg_2_1.type] == 99:
		setActive(arg_2_0.tfBossIcon, True)
		arg_2_0.GetLoader().GetSpriteQuiet("ui/share/ship_gizmos_atlas", "enemy_boss", arg_2_0.tfBossIcon)
	elif ChapterConst.EnemySize[arg_2_1.type] == 98:
		setActive(arg_2_0.tfBossIcon, True)
		arg_2_0.GetLoader().GetSpriteQuiet("ui/share/ship_gizmos_atlas", "enemy_elite", arg_2_0.tfBossIcon)
	else
		setActive(arg_2_0.tfBossIcon, False)

	if ChapterConst.EnemySize[arg_2_1.type] == 98:
		arg_2_0.tfBossIcon.localScale = Vector3(0.5, 0.5, 1)
		arg_2_0.tfBossIcon.anchoredPosition = Vector2(61.1, -30.6)
	else
		arg_2_0.tfBossIcon.localScale = Vector3(1, 1, 1)
		arg_2_0.tfBossIcon.anchoredPosition = Vector2(39.5, -23)

	var_0_0.ClearExtraEffects(arg_2_0)
	var_0_0.LoadExtraEffects(arg_2_0, arg_2_1.effect_prefab)
	arg_2_0.GetLoader().GetSprite("enemies/" .. arg_2_1.icon, "", arg_2_0.tfIcon)
	setText(arg_2_0.textLV, arg_2_1.level)
	existCall(arg_2_2)

def var_0_0.UpdateEggCell(arg_3_0, arg_3_1, arg_3_2, arg_3_3, arg_3_4):
	local var_3_0 = arg_3_2.row
	local var_3_1 = arg_3_2.column
	local var_3_2 = arg_3_2.trait != ChapterConst.TraitLurk and arg_3_2.flag == ChapterConst.CellFlagActive and not arg_3_1.existFleet(FleetType.Transport, var_3_0, var_3_1)
	local var_3_3 = arg_3_1.existEnemy(ChapterConst.SubjectChampion, var_3_0, var_3_1)

	setActive(arg_3_0.tfFighting, var_3_2 and var_3_3)

	arg_3_0.animator.enabled = var_3_2 and arg_3_2.data > 0

	setActive(arg_3_0.tfDamageCount, var_3_2 and arg_3_2.data > 0)
	setActive(arg_3_0.effectFireball, False)

	if arg_3_2.trait == ChapterConst.TraitVirgin:
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_UI_WEIGHANCHOR_ENEMY)

	if var_3_2:
		EnemyCellView.RefreshEnemyTplIcons(arg_3_0, arg_3_3, arg_3_1)

	arg_3_0.SetActive(var_3_2)

	local var_3_4 = arg_3_2.trait == ChapterConst.TraitVirgin
	local var_3_5 = ChapterConst.IsBossCell(arg_3_2)

	setActive(arg_3_0.tfEffectFound, var_3_4 and not var_3_5)
	setActive(arg_3_0.tfEffectFoundBoss, var_3_4 and var_3_5)

	if var_3_4:
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_UI_WEIGHANCHOR_ENEMY)

	existCall(arg_3_4)

return var_0_0
