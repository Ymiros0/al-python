local var_0_0 = class("RandomDockYardCard")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0._go = arg_1_1
	arg_1_0._tf = arg_1_1.transform
	arg_1_0.npcTr = findTF(arg_1_0._tf, "content/dockyard/npc")
	arg_1_0.nameTF = findTF(arg_1_0._tf, "content/info/name_mask/name")
	arg_1_0.lockTr = findTF(arg_1_0._tf, "content/dockyard/container/lock")
	arg_1_0.selected = findTF(arg_1_0._tf, "content/front/selected")
	arg_1_0.existAnim = False

	ClearTweenItemAlphaAndWhite(arg_1_0._go)

def var_0_0.Update(arg_2_0, arg_2_1, arg_2_2):
	TweenItemAlphaAndWhite(arg_2_0._go)

	if not arg_2_0.ship or arg_2_0.ship.id != arg_2_1.id:
		arg_2_0.ship = arg_2_1

		arg_2_0.Flush()

	arg_2_0.UpdateSelected(arg_2_2)

def var_0_0.UpdateSelected(arg_3_0, arg_3_1):
	setActive(arg_3_0.selected, arg_3_1)

	if not arg_3_1:
		arg_3_0.existAnim = False

		LeanTween.cancel(arg_3_0.selected.gameObject)
	elif arg_3_0.existAnim:
		-- block empty
	else
		arg_3_0.existAnim = True

		blinkAni(arg_3_0.selected, 0.6, -1, 0.3).setFrom(1)

def var_0_0.Flush(arg_4_0):
	local var_4_0 = arg_4_0.ship

	flushShipCard(arg_4_0._tf, var_4_0)
	setActive(arg_4_0.npcTr, var_4_0.isActivityNpc())
	setText(arg_4_0.nameTF, var_4_0.GetColorName(shortenString(var_4_0.getName(), PLATFORM_CODE == PLATFORM_US and 6 or 7)))
	arg_4_0.lockTr.gameObject.SetActive(var_4_0.GetLockState() == Ship.LOCK_STATE_LOCK)

def var_0_0.Dispose(arg_5_0):
	ClearTweenItemAlphaAndWhite(arg_5_0._go)
	arg_5_0.UpdateSelected(False)

return var_0_0
