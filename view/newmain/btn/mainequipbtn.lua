﻿local var_0_0 = class("MainEquipBtn", import(".MainBaseBtn"))

function var_0_0.OnClick(arg_1_0)
	arg_1_0:emit(NewMainMediator.GO_SCENE, SCENE.EQUIPSCENE)
end

return var_0_0
