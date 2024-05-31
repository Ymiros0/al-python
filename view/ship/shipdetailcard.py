local var_0_0 = class("ShipDetailCard")
local var_0_1 = 0.5

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.go = arg_1_1
	arg_1_0.tr = arg_1_1.transform
	arg_1_0.tagFlags = arg_1_2 or {}
	arg_1_0.toggle = GetOrAddComponent(arg_1_0.tr, typeof(Toggle))
	arg_1_0.content = findTF(arg_1_0.tr, "content").gameObject
	arg_1_0.quit = findTF(arg_1_0.tr, "quit_button").gameObject
	arg_1_0.detail = findTF(arg_1_0.tr, "content/dockyard/detail").gameObject
	arg_1_0.detailLayoutTr = findTF(arg_1_0.detail, "layout")
	arg_1_0.imageQuit = arg_1_0.quit.GetComponent("Image")
	arg_1_0.imageFrame = findTF(arg_1_0.tr, "content/front/frame").GetComponent("Image")
	arg_1_0.labelName = findTF(arg_1_0.tr, "content/info/name_mask/name")
	arg_1_0.npc = findTF(arg_1_0.tr, "content/dockyard/npc")

	setActive(arg_1_0.npc, False)

	arg_1_0.lock = findTF(arg_1_0.tr, "content/dockyard/container/lock")
	arg_1_0.maskStatusOb = findTF(arg_1_0.tr, "content/front/status_mask")
	arg_1_0.iconStatus = findTF(arg_1_0.tr, "content/dockyard/status")
	arg_1_0.iconStatusTxt = findTF(arg_1_0.tr, "content/dockyard/status/Text").GetComponent("Text")
	arg_1_0.selectedGo = findTF(arg_1_0.tr, "content/front/selected").gameObject
	arg_1_0.energyTF = findTF(arg_1_0.tr, "content/dockyard/container/energy")
	arg_1_0.proposeTF = findTF(arg_1_0.tr, "content/dockyard/propose")

	arg_1_0.selectedGo.SetActive(False)

	arg_1_0.hpBar = findTF(arg_1_0.tr, "content/dockyard/blood")

def var_0_0.update(arg_2_0, arg_2_1):
	if arg_2_0.shipVO != arg_2_1:
		arg_2_0.shipVO = arg_2_1

		arg_2_0.flush()

def var_0_0.updateSelected(arg_3_0, arg_3_1):
	arg_3_0.selected = arg_3_1

	arg_3_0.selectedGo.SetActive(arg_3_0.selected)

	if arg_3_0.selected:
		if not arg_3_0.selectedTw:
			arg_3_0.selectedTw = LeanTween.alpha(arg_3_0.selectedGo.transform, 1, var_0_1).setFrom(0).setEase(LeanTweenType.easeInOutSine).setLoopPingPong()
	elif arg_3_0.selectedTw:
		LeanTween.cancel(arg_3_0.selectedTw.uniqueId)

		arg_3_0.selectedTw = None

def var_0_0.flush(arg_4_0):
	local var_4_0 = arg_4_0.shipVO
	local var_4_1 = tobool(var_4_0)

	if var_4_1:
		if not var_4_0.getConfigTable():
			return

		flushShipCard(arg_4_0.tr, var_4_0)

		local var_4_2 = var_4_0.isActivityNpc()

		setActive(arg_4_0.npc, var_4_2)

		if arg_4_0.lock:
			arg_4_0.lock.gameObject.SetActive(var_4_0.GetLockState() == Ship.LOCK_STATE_LOCK)

		local var_4_3 = var_4_0.energy <= Ship.ENERGY_MID

		if var_4_3:
			local var_4_4 = GetSpriteFromAtlas("energy", var_4_0.getEnergyPrint())

			if not var_4_4:
				warning("找不到疲劳")

			setImageSprite(arg_4_0.energyTF, var_4_4)

		setActive(arg_4_0.energyTF, var_4_3)
		setScrollText(arg_4_0.labelName, var_4_0.getName())

		local var_4_5 = ShipStatus.ShipStatusToTag(var_4_0, arg_4_0.tagFlags)

		if var_4_5:
			arg_4_0.iconStatusTxt.text = var_4_5[3]

			GetSpriteFromAtlasAsync(var_4_5[1], var_4_5[2], function(arg_5_0)
				setImageSprite(arg_4_0.iconStatus, arg_5_0, True)
				setActive(arg_4_0.iconStatus, True)

				if var_4_5[1] == "shipstatus":
					arg_4_0.iconStatus.sizeDelta = Vector2(195, 36)
					arg_4_0.iconStatusTxt.fontSize = 30)
		else
			setActive(arg_4_0.iconStatus, False)

		local var_4_6, var_4_7 = var_4_0.getIntimacyIcon()

		setActive(arg_4_0.proposeTF, tobool(var_4_7 and not var_4_2))

	arg_4_0.content.SetActive(var_4_1)

def var_0_0.clear(arg_6_0):
	if arg_6_0.selectedTw:
		LeanTween.cancel(arg_6_0.selectedTw.uniqueId)

		arg_6_0.selectedTw = None

return var_0_0
