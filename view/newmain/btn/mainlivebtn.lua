﻿local var_0_0 = class("MainLiveBtn", import(".MainBaseBtn"))

function var_0_0.OnClick(arg_1_0)
	arg_1_0:emit(NewMainScene.OPEN_LIVEAREA)
end

return var_0_0
