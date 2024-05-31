ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleBulletEvent
local var_0_2 = var_0_0.Battle.BattleResourceManager
local var_0_3 = var_0_0.Battle.BattleConfig
local var_0_4 = class("BattleLaserArea", var_0_0.Battle.BattleBullet)

var_0_0.Battle.BattleLaserArea = var_0_4
var_0_4.__name = "BattleLaserArea"

function var_0_4.Update(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_0._bulletData:GetSpeed()

	if var_1_0.x ~= 0 or var_1_0.z ~= 0 or var_1_0.y ~= 0 then
		arg_1_0:UpdatePosition()
	end
end
