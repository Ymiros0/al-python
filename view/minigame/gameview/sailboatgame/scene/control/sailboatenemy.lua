local var_0_0 = class("SailBoatEnemy")
local var_0_1

var_0_0.fire_cd = 0.2

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	var_0_1 = SailBoatGameVo
	arg_1_0._tf = arg_1_1
	arg_1_0._eventCall = arg_1_2
	arg_1_0._collider = GetComponent(findTF(arg_1_0._tf, "bound"), typeof(BoxCollider2D))
	arg_1_0._animator = GetComponent(findTF(arg_1_0._tf, "img"), typeof(Animator))
	arg_1_0._leftWeapons, arg_1_0._rightWeapons = {}, {}
end

function var_0_0.setData(arg_2_0, arg_2_1)
	arg_2_0._data = arg_2_1
end

function var_0_0.start(arg_3_0)
	arg_3_0._removeFlag = false
	arg_3_0._sceneWidth, arg_3_0._sceneHeight = var_0_1.scene_width, var_0_1.scene_height
	arg_3_0._maxRemoveHeight = -arg_3_0._sceneHeight
	arg_3_0._maxRemoveWidth = arg_3_0._sceneWidth
	arg_3_0._speed = arg_3_0:getConfig("speed")
	arg_3_0._targetX = nil
	arg_3_0._targetY = nil
	arg_3_0._targetIndex = 1
	arg_3_0._hp = arg_3_0:getConfig("hp")

	arg_3_0:updateTarget()

	arg_3_0._destroyFlag = false

	arg_3_0:setInteger("dead_type", arg_3_0:getConfig("dead_type") or 0)
	arg_3_0:setVisible(true)

	arg_3_0._stopFlag = false
	arg_3_0._fireCd = var_0_0.fire_cd
end

function var_0_0.step(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_0._tf.anchoredPosition
	local var_4_1 = var_0_1.GetSceneSpeed()
	local var_4_2
	local var_4_3
	local var_4_4
	local var_4_5

	if arg_4_0._targetIndex > 1 and arg_4_0:getLife() and not arg_4_0._targetX and not arg_4_0._targetY and (arg_4_0._targetListX and arg_4_0._targetIndex <= #arg_4_0._targetListX or arg_4_0._targetListY and arg_4_0._targetIndex <= #arg_4_0._targetListY) then
		arg_4_0:updateTarget()
	end

	local var_4_6 = false

	if arg_4_0._targetX then
		local var_4_7 = var_4_0.x >= arg_4_0._targetX and -1 or 1

		var_4_2 = arg_4_0._targetSpeed[1] * arg_4_1 * var_4_7

		if var_4_7 ~= (var_4_0.x + var_4_2 >= arg_4_0._targetX and -1 or 1) then
			arg_4_0._targetX = nil

			if arg_4_0._targetIndex > #arg_4_0._targetListX then
				arg_4_0:setTrigger("enter_end")
			end
		end
	else
		var_4_2 = arg_4_0._speed.x * arg_4_1 + var_4_1.x
	end

	if arg_4_0._targetY then
		local var_4_8 = var_4_0.y >= arg_4_0._targetY and -1 or 1

		var_4_3 = arg_4_0._targetSpeed[2] * arg_4_1 * var_4_8

		if var_4_8 ~= (var_4_0.y + var_4_3 >= arg_4_0._targetY and -1 or 1) then
			arg_4_0._targetY = nil
		end
	else
		var_4_3 = arg_4_0._speed.y * arg_4_1 + var_4_1.y
	end

	var_4_0.x = var_4_0.x + var_4_2
	var_4_0.y = var_4_0.y + var_4_3
	arg_4_0._tf.anchoredPosition = var_4_0

	if not arg_4_0._removeFlag then
		if var_4_0.y < arg_4_0._maxRemoveHeight then
			arg_4_0._removeFlag = true
		elseif math.abs(var_4_0.x) > arg_4_0._maxRemoveWidth then
			arg_4_0._removeFlag = true
		end
	end

	if arg_4_0._removeTime and arg_4_0._removeTime > 0 then
		arg_4_0._removeTime = arg_4_0._removeTime - arg_4_1

		if arg_4_0._removeTime <= 0 then
			arg_4_0._removeTime = nil
			arg_4_0._removeFlag = true
		end
	end

	for iter_4_0 = 1, #arg_4_0._leftWeapons do
		arg_4_0._leftWeapons[iter_4_0]:step(arg_4_1)
	end

	for iter_4_1 = 1, #arg_4_0._rightWeapons do
		arg_4_0._rightWeapons[iter_4_1]:step(arg_4_1)
	end

	if arg_4_0._fireCd and arg_4_0._fireCd > 0 then
		arg_4_0._fireCd = arg_4_0._fireCd - arg_4_1

		if arg_4_0._fireCd <= 0 then
			arg_4_0._fireCd = 0
		end
	end
end

function var_0_0.setWeapon(arg_5_0, arg_5_1, arg_5_2)
	if arg_5_0._leftWeapons and #arg_5_0._leftWeapons > 0 then
		for iter_5_0 = 1, #arg_5_0._leftWeapons do
			arg_5_0._leftWeapons[iter_5_0]:clear()
		end
	end

	if arg_5_0._rightWeapons and #arg_5_0._rightWeapons > 0 then
		for iter_5_1 = 1, #arg_5_0._rightWeapons do
			arg_5_0._rightWeapons[iter_5_1]:clear()
		end
	end

	arg_5_0._leftWeapons = arg_5_1
	arg_5_0._rightWeapons = arg_5_2
end

function var_0_0.setTarget(arg_6_0, arg_6_1, arg_6_2, arg_6_3)
	arg_6_0._targetListX = arg_6_1
	arg_6_0._targetListY = arg_6_2
	arg_6_0._targetSpeed = arg_6_3
end

function var_0_0.updateTarget(arg_7_0)
	if arg_7_0._targetX or arg_7_0._targetY then
		return
	end

	if arg_7_0._targetListX and not arg_7_0._targetX and arg_7_0._targetIndex <= #arg_7_0._targetListX then
		local var_7_0 = arg_7_0._targetListX[arg_7_0._targetIndex]

		arg_7_0._targetX = math.random(var_7_0[1], var_7_0[2])

		if arg_7_0:getConfig("tpl") == "Enemys/Enemy_S" or arg_7_0:getConfig("tpl") == "Enemys/Enemy_SS" then
			local var_7_1 = arg_7_0._tf.anchoredPosition.x < arg_7_0._targetX and 1 or -1

			arg_7_0:setInteger("direct_x", var_7_1)
			arg_7_0:setTrigger("enter")
		end
	end

	if arg_7_0._targetListY and not arg_7_0._targetY and arg_7_0._targetIndex <= #arg_7_0._targetListY then
		local var_7_2 = arg_7_0._targetListY[arg_7_0._targetIndex]

		arg_7_0._targetY = math.random(var_7_2[1], var_7_2[2])
	end

	arg_7_0._targetIndex = arg_7_0._targetIndex + 1
end

function var_0_0.setTrigger(arg_8_0, arg_8_1, arg_8_2)
	if arg_8_0:getLife() then
		arg_8_0._animator:SetTrigger(arg_8_1)
	elseif arg_8_2 then
		arg_8_0._animator:ResetTrigger("enter")
		arg_8_0._animator:ResetTrigger("enter_end")
		arg_8_0._animator:ResetTrigger("reset")
		arg_8_0._animator:SetTrigger(arg_8_1)
	end
end

function var_0_0.setInteger(arg_9_0, arg_9_1, arg_9_2)
	arg_9_0._animator:SetInteger(arg_9_1, arg_9_2)
end

function var_0_0.getDestroyData(arg_10_0)
	return {
		score = arg_10_0:getConfig("score"),
		boom = arg_10_0:getConfig("boom"),
		position = arg_10_0._tf.anchoredPosition,
		range = arg_10_0:getConfig("range")
	}
end

function var_0_0.damage(arg_11_0, arg_11_1)
	if arg_11_0._hp == 0 then
		return
	end

	arg_11_0._hp = arg_11_0._hp - arg_11_1.num

	if arg_11_0._hp <= 0 then
		arg_11_0:setTrigger("dead", true)

		arg_11_0._hp = 0
		arg_11_0._targetX = nil
		arg_11_0._targetY = nil

		pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_0_1.SFX_SOUND_BOOM)

		if arg_11_0:getConfig("remove_time") then
			arg_11_0._removeTime = arg_11_0:getConfig("remove_time")

			return true
		end
	end

	return false
end

function var_0_0.getLife(arg_12_0)
	return arg_12_0._hp > 0
end

function var_0_0.getDestroyFlag(arg_13_0)
	return arg_13_0._destroyFlag
end

function var_0_0.getSpeed(arg_14_0)
	return arg_14_0._speed
end

function var_0_0.setContent(arg_15_0, arg_15_1)
	arg_15_0._content = arg_15_1

	SetParent(arg_15_0._tf, arg_15_1)
end

function var_0_0.getId(arg_16_0)
	return arg_16_0._data.id
end

function var_0_0.setVisible(arg_17_0, arg_17_1)
	setActive(arg_17_0._tf, arg_17_1)
end

function var_0_0.setPosition(arg_18_0, arg_18_1)
	arg_18_0._tf.anchoredPosition = arg_18_1
end

function var_0_0.getPosition(arg_19_0)
	return arg_19_0._tf.anchoredPosition
end

function var_0_0.getWorld(arg_20_0)
	return arg_20_0._tf.position
end

function var_0_0.clear(arg_21_0)
	arg_21_0:setVisible(false)
end

function var_0_0.setRemoveFlag(arg_22_0, arg_22_1)
	arg_22_0._removeFlag = arg_22_1
end

function var_0_0.getGroup(arg_23_0)
	return arg_23_0:getConfig("group")
end

function var_0_0.getHitGroup(arg_24_0)
	return arg_24_0:getConfig("hit_group")
end

function var_0_0.getTargetFlag(arg_25_0)
	return arg_25_0._targetX or arg_25_0._targetY
end

function var_0_0.getTf(arg_26_0)
	return arg_26_0._tf
end

function var_0_0.getRemoveFlag(arg_27_0)
	return arg_27_0._removeFlag
end

function var_0_0.getRuleConfig(arg_28_0, arg_28_1)
	return arg_28_0._rule[arg_28_1]
end

function var_0_0.dispose(arg_29_0)
	var_0_1 = nil
end

function var_0_0.getColliderData(arg_30_0)
	local var_30_0 = arg_30_0._content:InverseTransformPoint(arg_30_0._collider.bounds.min)

	if not arg_30_0._boundData then
		local var_30_1 = arg_30_0._content:InverseTransformPoint(arg_30_0._collider.bounds.max)

		arg_30_0._boundData = {
			width = math.floor(var_30_1.x - var_30_0.x),
			height = math.floor(var_30_1.y - var_30_0.y)
		}
	end

	return var_30_0, arg_30_0._boundData
end

function var_0_0.getWorldColliderData(arg_31_0)
	local var_31_0 = arg_31_0._collider.bounds.min

	if not arg_31_0._worldBoundData then
		local var_31_1 = arg_31_0._collider.bounds.max

		arg_31_0._worldBoundData = {
			width = var_31_1.x - var_31_0.x,
			height = var_31_1.y - var_31_0.y
		}
	end

	return var_31_0, arg_31_0._worldBoundData
end

function var_0_0.getStop(arg_32_0)
	return arg_32_0._stopFlag
end

function var_0_0.stopTarget(arg_33_0, arg_33_1)
	if arg_33_0._stopFlag then
		return
	end

	if arg_33_0._targetX then
		arg_33_0._targetX = nil
	end

	if arg_33_0._targetY then
		arg_33_0._targetY = nil
	end

	arg_33_0._stopFlag = true

	arg_33_0._animator:ResetTrigger("enter")
	arg_33_0._animator:ResetTrigger("enter_end")
	arg_33_0:setTrigger("reset")

	arg_33_0._speed = arg_33_1
end

function var_0_0.getMinMaxPosition(arg_34_0)
	return arg_34_0._collider.bounds.min, arg_34_0._collider.bounds.max
end

function var_0_0.checkPositionInRange(arg_35_0, arg_35_1)
	local var_35_0 = arg_35_0._tf.anchoredPosition
	local var_35_1 = math.abs(var_35_0.x - arg_35_1.x)
	local var_35_2 = math.abs(var_35_0.y - arg_35_1.y)
	local var_35_3 = arg_35_0:getConfig("range")

	if var_35_1 < var_35_3.x and var_35_2 < var_35_3.y then
		return true
	end

	return false
end

function var_0_0.getWeaponMaxDistance(arg_36_0)
	if not arg_36_0._weaponMaxDistance then
		arg_36_0._weaponMaxDistance = 0

		for iter_36_0 = 1, #arg_36_0._leftWeapons do
			local var_36_0 = arg_36_0._leftWeapons[iter_36_0]

			if var_36_0:getDistance() > arg_36_0._weaponMaxDistance then
				arg_36_0._weaponMaxDistance = var_36_0:getDistance()
			end
		end

		for iter_36_1 = 1, #arg_36_0._rightWeapons do
			local var_36_1 = arg_36_0._rightWeapons[iter_36_1]

			if var_36_1:getDistance() > arg_36_0._weaponMaxDistance then
				arg_36_0._weaponMaxDistance = var_36_1:getDistance()
			end
		end
	end

	return arg_36_0._weaponMaxDistance
end

function var_0_0.getWeapons(arg_37_0)
	return arg_37_0._leftWeapons, arg_37_0._rightWeapons
end

function var_0_0.canFire(arg_38_0)
	return #arg_38_0._leftWeapons > 0 or #arg_38_0._rightWeapons > 0
end

function var_0_0.inFireCd(arg_39_0)
	return arg_39_0._fireCd > 0
end

function var_0_0.fire(arg_40_0)
	if arg_40_0._fireCd <= 0 then
		arg_40_0._fireCd = var_0_0.fire_cd

		return true
	end

	return false
end

function var_0_0.getFirePos(arg_41_0)
	if not arg_41_0._leftFireTf then
		arg_41_0._leftFireTf = findTF(arg_41_0._tf, "leftFire")
	end

	if not arg_41_0._rightFireTf then
		arg_41_0._rightFireTf = findTF(arg_41_0._tf, "rightFire")
	end

	return arg_41_0._content:InverseTransformPoint(arg_41_0._leftFireTf.position), arg_41_0._content:InverseTransformPoint(arg_41_0._rightFireTf.position)
end

function var_0_0.getFireContent(arg_42_0)
	return arg_42_0._leftFireTf, arg_42_0._rightFireTf
end

function var_0_0.getConfig(arg_43_0, arg_43_1)
	return arg_43_0._data[arg_43_1]
end

return var_0_0
