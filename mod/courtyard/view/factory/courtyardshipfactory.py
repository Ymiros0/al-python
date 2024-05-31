local var_0_0 = class("CourtYardShipFactory")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.poolMgr = arg_1_1

def var_0_0.Make(arg_2_0, arg_2_1):
	local var_2_0 = arg_2_0.poolMgr.GetShipPool().Dequeue()
	local var_2_1 = SpineRole.New(arg_2_1)
	local var_2_2

	if arg_2_1.GetShipType() == CourtYardConst.SHIP_TYPE_OTHER:
		var_2_2 = CourtYardOtherPlayerShipModule.New(arg_2_1, var_2_0, var_2_1)
	else
		var_2_2 = ({
			CourtYardShipModule,
			CourtYardVisitorShipModule,
			CourtYardFeastShipModule
		})[arg_2_1.GetShipType()].New(arg_2_1, var_2_0, var_2_1)

	local var_2_3 = arg_2_1.GetPrefab()

	seriesAsync({
		function(arg_3_0)
			var_2_1.Load(arg_3_0, True),
		function(arg_4_0)
			arg_2_0.MakeAttachments(var_2_0, arg_2_1, arg_4_0)
	}, function()
		if IsNil(var_2_0):
			return

		local var_5_0 = var_2_1.modelRoot

		var_5_0.name = "model"
		var_5_0.transform.localScale = Vector3.one
		rtf(var_5_0).sizeDelta = Vector2.New(200, 500)

		SetParent(var_5_0, var_2_0)
		var_5_0.transform.SetSiblingIndex(2)
		setActive(var_2_0, True)
		var_2_2.OnIconLoaed()
		var_2_2.Init())

	return var_2_2

def var_0_0.MakeAttachments(arg_6_0, arg_6_1, arg_6_2, arg_6_3):
	if arg_6_2.GetShipType() == CourtYardConst.SHIP_TYPE_FEAST:
		ResourceMgr.Inst.getAssetAsync("ui/CourtYardFeastAttachments", "", typeof(GameObject), UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_7_0)
			if arg_6_0.exited:
				return

			Object.Instantiate(arg_7_0, arg_6_1.transform).name = "feastAttachments"

			arg_6_3()), True, True)
	else
		arg_6_3()

def var_0_0.Dispose(arg_8_0):
	arg_8_0.exited = True

return var_0_0
