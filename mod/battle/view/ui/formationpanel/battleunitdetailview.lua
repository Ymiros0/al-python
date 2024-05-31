﻿ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleAttr
local var_0_2 = var_0_0.Battle.BattleDataFunction
local var_0_3 = var_0_0.Battle.BattleConst
local var_0_4 = var_0_0.Battle.BattleUnitEvent
local var_0_5 = var_0_0.Battle.BattleConst.EquipmentType
local var_0_6 = class("BattleUnitDetailView")

var_0_0.Battle.BattleUnitDetailView = var_0_6
var_0_6.__name = "BattleUnitDetailView"
var_0_6.DefaultActive = {}
var_0_6.EnemyMarkList = {}
var_0_6.HIGH_LIGHT_BUFF = {}
var_0_6.PrimalAttr = {
	"cannonPower",
	"torpedoPower",
	"airPower",
	"antiAirPower",
	"antiSubPower",
	"loadSpeed",
	"dodgeRate",
	"attackRating",
	"velocity"
}
var_0_6.BaseEnhancement = {
	damageRatioByCannon = "damage/damageRatioByCannon",
	injureRatioByBulletTorpedo = "injure/injureRatioByBulletTorpedo",
	damageRatioByBulletTorpedo = "damage/damageRatioByBulletTorpedo",
	injureRatioByCannon = "injure/injureRatioByCannon",
	damageRatioBullet = "damage/damageRatioBullet",
	injureRatio = "injure/injureRatio",
	injureRatioByAir = "injure/injureRatioByAir",
	damageRatioByAir = "damage/damageRatioByAir"
}
var_0_6.SecondaryAttrListener = {}

function var_0_6.Ctor(arg_1_0)
	pg.DelegateInfo.New(arg_1_0)
end

function var_0_6.SetUnit(arg_2_0, arg_2_1)
	var_0_0.EventListener.AttachEventListener(arg_2_0)

	arg_2_0._unit = arg_2_1

	if arg_2_0._unit:GetUnitType() == var_0_3.UnitType.PLAYER_UNIT then
		local var_2_0 = var_0_0.Battle.BattleResourceManager.GetInstance():GetCharacterQIcon(arg_2_0._unit:GetTemplate().painting)

		setImageSprite(arg_2_0._icon, var_2_0)

		for iter_2_0 = 1, arg_2_0._unit:GetTemplate().star do
			local var_2_1 = cloneTplTo(arg_2_0._starTpl, arg_2_0._stars)

			setActive(var_2_1, true)
		end
	end

	setText(arg_2_0._templateID, arg_2_0._unit:GetTemplate().id)
	setText(arg_2_0._name, arg_2_0._unit:GetTemplate().name)
	setText(arg_2_0._lv, arg_2_0._unit:GetAttrByName("level"))

	arg_2_0._preAttrList = {}

	for iter_2_1, iter_2_2 in ipairs(var_0_6.PrimalAttr) do
		local var_2_2 = var_0_1.GetBase(arg_2_0._unit, iter_2_2)

		setText(arg_2_0._attrView:Find(iter_2_2 .. "/base"), var_2_2)

		arg_2_0._preAttrList[iter_2_2] = var_2_2
	end

	arg_2_0._baseEhcList = {}

	for iter_2_3, iter_2_4 in pairs(var_0_6.BaseEnhancement) do
		arg_2_0._baseEhcList[iter_2_3] = 0
	end

	arg_2_0._secondaryAttrList = {}
	arg_2_0._buffList = {}
	arg_2_0._aaList = {}
	arg_2_0._weaponList = {}
	arg_2_0._skillList = {}

	arg_2_0:updateWeaponList()
end

function var_0_6.Update(arg_3_0)
	for iter_3_0, iter_3_1 in ipairs(var_0_6.PrimalAttr) do
		arg_3_0:updatePrimalAttr(iter_3_1)
	end

	for iter_3_2, iter_3_3 in pairs(var_0_6.BaseEnhancement) do
		arg_3_0:updateBaseEnhancement(iter_3_2, iter_3_3)
	end

	local var_3_0 = arg_3_0._unit:GetAttr()

	for iter_3_4, iter_3_5 in pairs(var_3_0) do
		if string.find(iter_3_4, "DMG_TAG_EHC_") or string.find(iter_3_4, "DMG_FROM_TAG_") or table.contains(var_0_6.SecondaryAttrListener, iter_3_4) then
			arg_3_0:updateSecondaryAttr(iter_3_4, iter_3_5)
		end
	end

	arg_3_0:updateHP()
	arg_3_0:updateBuffList()
	arg_3_0:updateWeaponProgress()
	arg_3_0:updateSkillList()
end

function var_0_6.ConfigSkin(arg_4_0, arg_4_1)
	arg_4_0._go = arg_4_1

	local var_4_0 = arg_4_1.transform

	arg_4_0._tf = var_4_0
	arg_4_0._iconView = var_4_0:Find("icon")
	arg_4_0._icon = arg_4_0._iconView:Find("icon")
	arg_4_0._stars = arg_4_0._iconView:Find("stars")
	arg_4_0._starTpl = arg_4_0._stars:Find("star_tpl")
	arg_4_0._templateView = var_4_0:Find("template")
	arg_4_0._templateID = arg_4_0._templateView:Find("template/text")
	arg_4_0._name = arg_4_0._templateView:Find("name/text")
	arg_4_0._lv = arg_4_0._templateView:Find("level/text")
	arg_4_0._totalHP = arg_4_0._templateView:Find("totalHP/text")
	arg_4_0._currentHP = arg_4_0._templateView:Find("currentHP/text")
	arg_4_0._shield = arg_4_0._templateView:Find("shield/text")
	arg_4_0._attrView = var_4_0:Find("attr_panels/primal_attr")
	arg_4_0._baseEnhanceView = var_4_0:Find("attr_panels/basic_ehc")
	arg_4_0._secondaryAttrView = var_4_0:Find("attr_panels/tag_ehc")
	arg_4_0._secondaryAttrContainer = arg_4_0._secondaryAttrView:Find("tag_container")
	arg_4_0._secondaryAttrTpl = arg_4_0._secondaryAttrView:Find("tag_attr_tpl")
	arg_4_0._buffView = var_4_0:Find("attr_panels/buff")
	arg_4_0._buffContainer = arg_4_0._buffView:Find("buff_container")
	arg_4_0._buffTpl = arg_4_0._buffView:Find("buff_tpl")
	arg_4_0._weaponView = var_4_0:Find("panel_container/weapon_panels")
	arg_4_0._weaponContainer = arg_4_0._weaponView:Find("weapon_container")
	arg_4_0._weaponTpl = arg_4_0._weaponView:Find("weapon_tpl")
	arg_4_0._skillView = var_4_0:Find("panel_container/skill_panel")
	arg_4_0._skillContainer = arg_4_0._skillView:Find("skill_container")
	arg_4_0._skillTpl = arg_4_0._skillView:Find("skill_tpl")

	SetActive(arg_4_0._go, true)

	for iter_4_0, iter_4_1 in ipairs(var_0_6.DefaultActive) do
		SetActive(var_4_0:Find(iter_4_1), true)
	end
end

function var_0_6.updateHP(arg_5_0)
	local var_5_0, var_5_1 = arg_5_0._unit:GetHP()
	local var_5_2 = arg_5_0._unit:GetHPRate()

	setText(arg_5_0._totalHP, var_5_1)
	setText(arg_5_0._currentHP, var_5_0)

	local var_5_3 = arg_5_0._unit:GetBuffList()
	local var_5_4 = 0

	for iter_5_0, iter_5_1 in pairs(var_5_3) do
		for iter_5_2, iter_5_3 in ipairs(iter_5_1:GetEffectList()) do
			if iter_5_3.__name == "BattleBuffShield" or iter_5_3.__name == "BattleBuffRecordShield" then
				var_5_4 = var_5_4 + math.max(0, iter_5_3:GetEffectAttachData())
			end
		end
	end

	setText(arg_5_0._shield, var_5_4)
end

function var_0_6.updatePrimalAttr(arg_6_0, arg_6_1)
	local var_6_0 = arg_6_0._unit:GetAttrByName(arg_6_1)

	setText(arg_6_0._attrView:Find(arg_6_1 .. "/current"), var_6_0)

	local var_6_1 = var_6_0 - arg_6_0._preAttrList[arg_6_1]

	if var_6_1 ~= 0 then
		local var_6_2 = arg_6_0._attrView:Find(arg_6_1 .. "/change")

		var_0_6.setDeltaText(var_6_2, var_6_1)

		arg_6_0._preAttrList[arg_6_1] = var_6_0
	end

	local var_6_3 = var_6_0 - var_0_1.GetBase(arg_6_0._unit, arg_6_1)

	if var_6_3 ~= 0 then
		local var_6_4 = arg_6_0._attrView:Find(arg_6_1 .. "/delta")

		var_0_6.setDeltaText(var_6_4, var_6_3)
	end
end

function var_0_6.updateBaseEnhancement(arg_7_0, arg_7_1, arg_7_2)
	local var_7_0 = arg_7_0._baseEnhanceView:Find(arg_7_2)
	local var_7_1 = arg_7_0._unit:GetAttrByName(arg_7_1)
	local var_7_2 = var_7_1 - arg_7_0._baseEhcList[arg_7_1]

	setText(var_7_0:Find("current"), var_7_1)

	if var_7_2 ~= 0 then
		var_0_6.setDeltaText(var_7_0:Find("change"), var_7_2)
	end
end

function var_0_6.updateSecondaryAttr(arg_8_0, arg_8_1, arg_8_2)
	if not arg_8_0._secondaryAttrList[arg_8_1] then
		local var_8_0 = cloneTplTo(arg_8_0._secondaryAttrTpl, arg_8_0._secondaryAttrContainer)

		Canvas.ForceUpdateCanvases()
		setText(var_8_0:Find("tag_name"), arg_8_1)
		setActive(var_8_0, true)

		local var_8_1 = {
			value = 0,
			tf = var_8_0
		}

		arg_8_0._secondaryAttrList[arg_8_1] = var_8_1
	end

	local var_8_2 = arg_8_0._secondaryAttrList[arg_8_1].tf
	local var_8_3 = arg_8_0._unit:GetAttrByName(arg_8_1)
	local var_8_4 = arg_8_0._secondaryAttrList[arg_8_1].value

	if var_8_4 ~= arg_8_2 then
		setText(var_8_2:Find("current"), arg_8_2)

		local var_8_5 = var_8_3 - var_8_4

		var_0_6.setDeltaText(var_8_2:Find("delta"), var_8_5)
	end
end

function var_0_6.updateBuffList(arg_9_0)
	local var_9_0 = arg_9_0._unit:GetBuffList()

	for iter_9_0, iter_9_1 in pairs(arg_9_0._buffList) do
		if not var_9_0[iter_9_0] then
			GameObject.Destroy(iter_9_1.gameObject)

			arg_9_0._buffList[iter_9_0] = nil
		end
	end

	for iter_9_2, iter_9_3 in pairs(var_9_0) do
		if not arg_9_0._buffList[iter_9_2] then
			arg_9_0:addBuff(iter_9_2, iter_9_3)
		else
			local var_9_1 = arg_9_0._buffList[iter_9_2]

			if iter_9_3._stack > 1 then
				local var_9_2 = var_9_1:Find("buff_stack")

				setActive(var_9_2, true)
				setText(var_9_2, "x" .. iter_9_3._stack)
			end
		end
	end

	for iter_9_4, iter_9_5 in pairs(var_9_0) do
		local var_9_3 = iter_9_5:GetEffectList()

		for iter_9_6, iter_9_7 in ipairs(var_9_3) do
			if iter_9_7.__name == var_0_0.Battle.BattleBuffCastSkill.__name and (not arg_9_0._skillList[iter_9_7._skill_id] or not table.contains(arg_9_0._skillList[iter_9_7._skill_id].effectList, iter_9_7)) then
				arg_9_0:addSkillCaster(iter_9_7)
			end
		end
	end
end

function var_0_6.updateWeaponList(arg_10_0)
	local var_10_0 = arg_10_0._unit:GetAirAssistList()

	if var_10_0 then
		for iter_10_0, iter_10_1 in ipairs(var_10_0) do
			local var_10_1 = cloneTplTo(arg_10_0._weaponTpl, arg_10_0._weaponContainer)

			Canvas.ForceUpdateCanvases()

			local var_10_2 = var_10_1:Find("common/icon")

			GetImageSpriteFromAtlasAsync("skillicon/2130", "", var_10_2)
			setText(var_10_1:Find("common/index"), "空袭")
			setText(var_10_1:Find("common/templateID"), iter_10_1:GetStrikeSkillID())

			arg_10_0._aaList[iter_10_1] = var_10_1
		end
	end

	local var_10_3 = arg_10_0._unit:GetAllWeapon()

	for iter_10_2, iter_10_3 in ipairs(var_10_3) do
		local var_10_4 = iter_10_3:GetType()

		if var_10_4 ~= var_0_5.STRIKE_AIRCRAFT and var_10_4 ~= var_0_5.FLEET_ANTI_AIR then
			local var_10_5 = cloneTplTo(arg_10_0._weaponTpl, arg_10_0._weaponContainer)

			Canvas.ForceUpdateCanvases()
			setText(var_10_5:Find("common/index"), iter_10_3:GetEquipmentIndex())
			setText(var_10_5:Find("common/templateID"), iter_10_3:GetTemplateData().id)

			local var_10_6 = iter_10_3:GetSrcEquipmentID()
			local var_10_7 = var_10_5:Find("common/icon")

			if var_10_6 then
				local var_10_8 = var_0_2.GetWeaponDataFromID(var_10_6).icon

				GetImageSpriteFromAtlasAsync("equips/" .. var_10_8, "", var_10_7)
			else
				setActive(var_10_7, false)
			end

			arg_10_0._weaponList[iter_10_3] = {
				tf = var_10_5,
				data = {}
			}

			onToggle(arg_10_0, var_10_5:Find("common/sector"), function(arg_11_0)
				arg_10_0._unit:ActiveWeaponSectorView(iter_10_3, arg_11_0)
			end)
			arg_10_0:updateBulletAttrBuff(iter_10_3)
		end
	end

	local var_10_9 = arg_10_0._unit:GetFleetRangeAAWeapon()

	if var_10_9 then
		local var_10_10 = cloneTplTo(arg_10_0._weaponTpl, arg_10_0._weaponContainer)

		Canvas.ForceUpdateCanvases()

		local var_10_11 = var_10_10:Find("common/icon")

		GetImageSpriteFromAtlasAsync("skillicon/2130", "", var_10_11)
		setText(var_10_10:Find("common/index"), "远程防空")
		setText(var_10_10:Find("common/templateID"), "N/A")
		onToggle(arg_10_0, var_10_10:Find("common/sector"), function(arg_12_0)
			arg_10_0._unit:ActiveWeaponSectorView(var_10_9, arg_12_0)
		end)
	end
end

function var_0_6.updateWeaponProgress(arg_13_0)
	for iter_13_0, iter_13_1 in pairs(arg_13_0._weaponList) do
		local var_13_0 = iter_13_1.tf
		local var_13_1 = iter_13_0:GetReloadRate()

		arg_13_0.updateBarProgress(var_13_0, var_13_1)
		setText(var_13_0:Find("sum/damageSum"), iter_13_0:GetDamageSUM())
		setText(var_13_0:Find("sum/CTRate"), string.format("%.2f", iter_13_0:GetCTRate() * 100) .. "%")
		setText(var_13_0:Find("sum/ACCRate"), string.format("%.2f", iter_13_0:GetACCRate() * 100) .. "%")
		arg_13_0:updateBulletAttrBuff(iter_13_0)
	end

	for iter_13_2, iter_13_3 in pairs(arg_13_0._aaList) do
		local var_13_2 = iter_13_2:GetReloadRate()

		arg_13_0.updateBarProgress(iter_13_3, var_13_2)

		local var_13_3, var_13_4 = iter_13_2:GetDamageSUM()

		setText(iter_13_3:Find("sum/damageSum"), var_13_3 .. " + " .. var_13_4)
	end
end

function var_0_6.updateBarProgress(arg_14_0, arg_14_1)
	local var_14_0 = arg_14_0:Find("common/reload_progress/blood"):GetComponent(typeof(Image))

	var_14_0.fillAmount = 1 - arg_14_1

	if arg_14_1 == 0 then
		var_14_0.color = Color.green
	else
		var_14_0.color = Color.red
	end
end

function var_0_6.updateBulletAttrBuff(arg_15_0, arg_15_1)
	local var_15_0 = arg_15_0._weaponList[arg_15_1]
	local var_15_1 = var_15_0.tf
	local var_15_2 = var_15_0.data
	local var_15_3 = var_15_1:Find("weapon_attr_tpl")
	local var_15_4 = var_15_1:Find("weapon_attr_container")
	local var_15_5 = {}

	for iter_15_0, iter_15_1 in pairs(var_15_2) do
		var_15_5[iter_15_0] = true
	end

	for iter_15_2, iter_15_3 in pairs(arg_15_0._unit:GetBuffList()) do
		for iter_15_4, iter_15_5 in ipairs(iter_15_3:GetEffectList()) do
			if iter_15_5.__name == var_0_0.Battle.BattleBuffAddBulletAttr.__name then
				local var_15_6 = arg_15_1:GetEquipmentIndex()

				if iter_15_5:equipIndexRequire(var_15_6) then
					local var_15_7 = var_15_2[iter_15_5]

					if not var_15_7 then
						var_15_7 = cloneTplTo(var_15_3, var_15_4)

						setText(var_15_7:Find("tag_name"), iter_15_5._attr)
						setText(var_15_7:Find("src_buff"), iter_15_3:GetID())
						Canvas.ForceUpdateCanvases()

						var_15_7:Find("src_buff"):GetComponent(typeof(Text)).color = Color.green
						var_15_2[iter_15_5] = var_15_7
					end

					setText(var_15_7:Find("current"), iter_15_5._number)

					var_15_5[iter_15_5] = false
				end
			end
		end
	end

	for iter_15_6, iter_15_7 in pairs(var_15_5) do
		if iter_15_7 then
			local var_15_8 = var_15_2[iter_15_6]

			SetActive(var_15_8:Find("expire"), true)
		end
	end
end

function var_0_6.addBuff(arg_16_0, arg_16_1, arg_16_2)
	local var_16_0 = cloneTplTo(arg_16_0._buffTpl, arg_16_0._buffContainer)

	Canvas.ForceUpdateCanvases()
	setText(var_16_0:Find("buff_id"), "buff_" .. arg_16_1)

	if table.contains(var_0_6.HIGH_LIGHT_BUFF, arg_16_1) then
		local var_16_1 = var_16_0:Find("high_light")

		setActive(var_16_1, true)
	end

	if arg_16_2._stack > 1 then
		local var_16_2 = var_16_0:Find("buff_stack")

		setActive(var_16_2, true)
		setText(var_16_2, "x" .. arg_16_2._stack)
	end

	setActive(var_16_0, true)

	arg_16_0._buffList[arg_16_1] = var_16_0
end

function var_0_6.addSkillCaster(arg_17_0, arg_17_1)
	local var_17_0 = arg_17_1._skill_id
	local var_17_1 = arg_17_1._srcBuff:GetLv()

	if not var_0_0.Battle.BattleSkillUnit.IsFireSkill(var_17_0, var_17_1) then
		return
	end

	local var_17_2 = arg_17_0._skillList[var_17_0]

	if not var_17_2 then
		local var_17_3 = cloneTplTo(arg_17_0._skillTpl, arg_17_0._skillContainer)
		local var_17_4 = var_17_3:Find("common")

		setText(var_17_4:Find("skillID"), arg_17_1._skill_id)

		local var_17_5 = var_17_3:Find("common/icon")
		local var_17_6 = arg_17_1._srcBuff._tempData.icon or 10120

		GetImageSpriteFromAtlasAsync("skillicon/" .. var_17_6, "", var_17_5)
		Canvas.ForceUpdateCanvases()

		var_17_2 = {
			tf = var_17_3,
			effectList = {}
		}
		arg_17_0._skillList[var_17_0] = var_17_2
	end

	table.insert(var_17_2.effectList, arg_17_1)
	arg_17_0:updateCastEffectTpl(var_17_0)
end

function var_0_6.updateSkillList(arg_18_0)
	for iter_18_0, iter_18_1 in pairs(arg_18_0._skillList) do
		arg_18_0:updateCastEffectTpl(iter_18_0)
	end
end

function var_0_6.updateCastEffectTpl(arg_19_0, arg_19_1)
	local var_19_0 = arg_19_0._skillList[arg_19_1]
	local var_19_1 = var_19_0.tf
	local var_19_2 = var_19_0.effectList
	local var_19_3 = 0
	local var_19_4 = 0

	for iter_19_0, iter_19_1 in ipairs(var_19_2) do
		var_19_3 = var_19_3 + iter_19_1:GetCastCount()
		var_19_4 = var_19_4 + iter_19_1:GetSkillFireDamageSum()
	end

	local var_19_5 = var_19_1:Find("common")

	setText(var_19_5:Find("count"), var_19_3)
	setText(var_19_5:Find("damageSum"), var_19_4)
end

function var_0_6.Dispose(arg_20_0)
	pg.DelegateInfo.Dispose(arg_20_0)

	arg_20_0._unit = nil
	arg_20_0._secondaryAttrList = nil
	arg_20_0._buffList = nil
	arg_20_0._weaponList = nil

	GameObject.Destroy(arg_20_0._go)
	var_0_0.EventListener.DetachEventListener(arg_20_0)
end

function var_0_6.setDeltaText(arg_21_0, arg_21_1)
	setText(arg_21_0, arg_21_1)

	local var_21_0 = arg_21_1 > 0 and Color.green or Color.red

	arg_21_0:GetComponent(typeof(Text)).color = var_21_0
end

var_0_6.WeaponForger = {}
var_0_6.BulletForger = {}
var_0_6.BarrageForger = {}
var_0_6.AircraftForger = {}
