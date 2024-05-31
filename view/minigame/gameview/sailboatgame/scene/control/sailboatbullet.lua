local var_0_0 = class("SailBoatBullet")
local var_0_1

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	var_0_1 = SailBoatGameVo
	arg_1_0._tf = arg_1_1
	arg_1_0._eventCall = arg_1_2
	arg_1_0._collider = GetComponent(findTF(arg_1_0._tf, "bound"), typeof(BoxCollider2D))
	arg_1_0._img = GetComponent(findTF(arg_1_0._tf, "img"), typeof(Image))
	arg_1_0._weaponData = nil
end

function var_0_0.setData(arg_2_0, arg_2_1)
	arg_2_0._data = arg_2_1
end

function var_0_0.start(arg_3_0)
	arg_3_0._removeFlag = false

	arg_3_0:setSprite(var_0_1.GetBulletSprite(arg_3_0._data.image))
	arg_3_0:setVisible(true)

	arg_3_0._moveDistance = 0
	arg_3_0._lifeTime = 0

	arg_3_0:setPosition(arg_3_0._fireData.pos)
	arg_3_0:setMove(arg_3_0._fireData.move)
	arg_3_0:setHitGroup(arg_3_0._fireData.hit)

	local var_3_0 = arg_3_0._fireData.content

	if var_3_0 then
		arg_3_0:setContent(var_3_0)
	end

	if arg_3_0:getConfig("fire_effect") then
		local var_3_1 = arg_3_0:getConfig("fire_effect")
		local var_3_2 = arg_3_0._fireData.effect_content
		local var_3_3 = arg_3_0._fireData.effect_pos

		arg_3_0._eventCall(SailBoatGameEvent.CREATE_EFFECT, {
			effect = var_3_1,
			direct = Vector3(arg_3_0._move.x, 1, 1),
			position = var_3_3,
			content = var_3_2
		})
	end
end

function var_0_0.getWorld(arg_4_0)
	return arg_4_0._tf.position
end

function var_0_0.step(arg_5_0, arg_5_1)
	local var_5_0 = arg_5_0._tf.anchoredPosition

	var_5_0.x = var_5_0.x + arg_5_0._move.x * arg_5_1 * arg_5_0._speed
	var_5_0.y = var_5_0.y + arg_5_0._move.y * arg_5_1 * arg_5_0._speed
	arg_5_0._tf.anchoredPosition = var_5_0

	if arg_5_0._life and arg_5_0._life > 0 then
		arg_5_0._life = arg_5_0._life - arg_5_1

		if arg_5_0._life <= 0 then
			arg_5_0._life = 0

			arg_5_0:setRemoveFlag(true)
		end
	end

	if math.abs(var_5_0.x) > SailBoatGameVo.scene_width then
		arg_5_0._removeFlag = true
	elseif math.abs(var_5_0.y) > SailBoatGameVo.scene_height then
		arg_5_0._removeFlag = true
	end
end

function var_0_0.getDamage(arg_6_0)
	return {
		num = arg_6_0._weaponData.damage,
		position = arg_6_0._tf.position
	}
end

function var_0_0.setMove(arg_7_0, arg_7_1)
	arg_7_0._move = arg_7_1
end

function var_0_0.setPosition(arg_8_0, arg_8_1)
	arg_8_0._tf.anchoredPosition = arg_8_1
end

function var_0_0.hit(arg_9_0)
	if arg_9_0:getConfig("hit_effect") then
		local var_9_0 = arg_9_0:getConfig("hit_effect")

		arg_9_0._eventCall(SailBoatGameEvent.CREATE_EFFECT, {
			effect = var_9_0,
			direct = Vector3(1, 1, 1),
			position = arg_9_0._tf.anchoredPosition
		})
	end

	arg_9_0._removeFlag = true
end

function var_0_0.setHitGroup(arg_10_0, arg_10_1)
	arg_10_0._hitGroup = arg_10_1
end

function var_0_0.getHitGroup(arg_11_0)
	if not arg_11_0._hitGroup then
		arg_11_0._hitGroup = {}
	end

	return arg_11_0._hitGroup
end

function var_0_0.setSprite(arg_12_0, arg_12_1)
	arg_12_0._img.sprite = arg_12_1

	arg_12_0._img:SetNativeSize()
end

function var_0_0.getSpeed(arg_13_0)
	return arg_13_0._speed
end

function var_0_0.setFireData(arg_14_0, arg_14_1)
	arg_14_0._fireData = arg_14_1
end

function var_0_0.setWeapon(arg_15_0, arg_15_1)
	arg_15_0._weaponData = arg_15_1
	arg_15_0._speed = arg_15_0._weaponData.speed
	arg_15_0._damage = arg_15_0._weaponData.damage
	arg_15_0._life = arg_15_0._weaponData.life
end

function var_0_0.setContent(arg_16_0, arg_16_1)
	arg_16_0._content = arg_16_1

	SetParent(arg_16_0._tf, arg_16_1)
end

function var_0_0.getId(arg_17_0)
	return arg_17_0._data.id
end

function var_0_0.setVisible(arg_18_0, arg_18_1)
	setActive(arg_18_0._tf, arg_18_1)
end

function var_0_0.setPosition(arg_19_0, arg_19_1)
	arg_19_0._tf.anchoredPosition = arg_19_1
end

function var_0_0.clear(arg_20_0)
	arg_20_0:setVisible(false)
end

function var_0_0.setRemoveFlag(arg_21_0, arg_21_1)
	arg_21_0._removeFlag = arg_21_1
end

function var_0_0.getRemoveFlag(arg_22_0)
	return arg_22_0._removeFlag
end

function var_0_0.dispose(arg_23_0)
	var_0_1 = nil
end

function var_0_0.getColliderData(arg_24_0)
	local var_24_0 = arg_24_0._content:InverseTransformPoint(arg_24_0._collider.bounds.min)

	if not arg_24_0._boundData then
		local var_24_1 = arg_24_0._content:InverseTransformPoint(arg_24_0._collider.bounds.max)

		arg_24_0._boundData = {
			width = math.floor(var_24_1.x - var_24_0.x),
			height = math.floor(var_24_1.y - var_24_0.y)
		}
	end

	return var_24_0, arg_24_0._boundData
end

function var_0_0.checkPositionInRange(arg_25_0, arg_25_1)
	local var_25_0 = arg_25_0._tf.anchoredPosition
	local var_25_1 = math.abs(var_25_0.x - arg_25_1.x)
	local var_25_2 = math.abs(var_25_0.y - arg_25_1.y)
	local var_25_3 = arg_25_0:getConfig("range")

	if var_25_1 < var_25_3.x and var_25_2 < var_25_3.y then
		return true
	end

	return false
end

function var_0_0.getPosition(arg_26_0)
	return arg_26_0._tf.anchoredPosition
end

function var_0_0.getConfig(arg_27_0, arg_27_1)
	return arg_27_0._data[arg_27_1]
end

function var_0_0.getWeaponConfig(arg_28_0, arg_28_1)
	return arg_28_0._weaponData[arg_28_1]
end

return var_0_0
