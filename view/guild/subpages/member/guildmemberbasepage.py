local var_0_0 = class("GuildMemberBasePage", import("....base.BaseSubView"))

def var_0_0.SetCallBack(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.onShowCallBack = arg_1_1
	arg_1_0.onHideCallBack = arg_1_2

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.buttonContainer = arg_2_0.findTF("frame/opera")

	local var_2_0 = pg.UIMgr.GetInstance().OverlayMain.transform.InverseTransformPoint(arg_2_0.buttonContainer.position)

	arg_2_0.buttonPos = Vector3(var_2_0.x, var_2_0.y, 0)

def var_0_0.Show(arg_3_0, arg_3_1, arg_3_2, arg_3_3, arg_3_4):
	if arg_3_4:
		arg_3_4()

	arg_3_0.guildVO = arg_3_1
	arg_3_0.playerVO = arg_3_2
	arg_3_0.memberVO = arg_3_3

	if not arg_3_0.ShouldShow():
		return

	arg_3_0.OnShow()
	pg.UIMgr.GetInstance().BlurPanel(arg_3_0._tf)
	var_0_0.super.Show(arg_3_0)
	arg_3_0._tf.SetAsLastSibling()
	arg_3_0.onShowCallBack(arg_3_0.buttonPos)

def var_0_0.Hide(arg_4_0):
	if arg_4_0.isShowing():
		pg.UIMgr.GetInstance().UnblurPanel(arg_4_0._tf, arg_4_0._parentTf)

	if arg_4_0.circle.childCount > 0:
		local var_4_0 = arg_4_0.circle.GetChild(0).gameObject

		PoolMgr.GetInstance().ReturnPrefab("IconFrame/" .. var_4_0.name, var_4_0.name, var_4_0)

	var_0_0.super.Hide(arg_4_0)
	arg_4_0.onHideCallBack()

def var_0_0.OnDestroy(arg_5_0):
	arg_5_0.Hide()

def var_0_0.ShouldShow(arg_6_0):
	return True

def var_0_0.OnShow(arg_7_0):
	return

return var_0_0
