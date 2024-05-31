local var_0_0 = class("Dorm3dFurnitureSelectLayer", import("view.base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "Dorm3dFurnitureSelectUI"

var_0_0.SELECT_MODE = {
	SLOT = 1,
	FURNITURE = 2,
	NONE = 0
}

def var_0_0.init(arg_2_0):
	arg_2_0.zoneList = arg_2_0._tf.Find("ZoneList")

	setActive(arg_2_0.zoneList, False)

	local var_2_0 = arg_2_0._tf.Find("Right/Panel/Furnitures")

	arg_2_0.furnitureScroll = var_2_0.Find("Scroll").GetComponent("LScrollRect")
	arg_2_0.furnitureEmpty = var_2_0.Find("Empty")
	arg_2_0.lableTrans = arg_2_0._tf.Find("Main/Label")

	setActive(arg_2_0.lableTrans, False)

	arg_2_0.blockActive = False

	local var_2_1 = arg_2_0.furnitureScroll.prefabItem.transform

	setText(var_2_1.Find("Unfit/Icon/Text"), i18n("dorm3d_furniture_unfit"))
	setText(var_2_1.Find("Lack/Icon/Text"), i18n("ryza_tip_control_buff_not_obtain"))

def var_0_0.SetSceneRoot(arg_3_0, arg_3_1):
	arg_3_0.scene = arg_3_1

def var_0_0.SetApartment(arg_4_0, arg_4_1):
	arg_4_0.apartment = arg_4_1.clone()

def var_0_0.didEnter(arg_5_0):
	local var_5_0 = arg_5_0.apartment.GetNormalZones()

	arg_5_0.zoneIndex = 1

	local var_5_1 = arg_5_0.scene.GetAttachedFurnitureName()

	if var_5_1:
		table.Ipairs(var_5_0, function(arg_6_0, arg_6_1)
			if arg_6_1.GetWatchCameraName() == var_5_1:
				arg_5_0.zoneIndex = arg_6_0)

	onButton(arg_5_0, arg_5_0._tf.Find("Right/Panel/Zone/Switch"), function()
		setActive(arg_5_0.zoneList, True), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.zoneList.Find("Mask"), function()
		setActive(arg_5_0.zoneList, False))
	onButton(arg_5_0, arg_5_0._tf.Find("Top/Back"), function()
		arg_5_0.onBackPressed())
	onButton(arg_5_0, arg_5_0._tf.Find("Right/Save"), function()
		arg_5_0.ShowReplaceWindow(), SFX_PANEL)

	local var_5_2 = arg_5_0._tf.Find("Right").rect.width

	local function var_5_3(arg_11_0)
		setCanvasGroupAlpha(arg_5_0._tf.Find("Right"), 1)
		shiftPanel(arg_5_0._tf.Find("Right"), arg_11_0 and var_5_2 or 0, None, 0.5, None, None, None, None, function()
			return)
		setActive(arg_5_0._tf.Find("Right/Popup"), arg_11_0)
		setActive(arg_5_0._tf.Find("Right/Collapse"), not arg_11_0)

	setActive(arg_5_0._tf.Find("Right/Popup"), False)
	onButton(arg_5_0, arg_5_0._tf.Find("Right/Popup"), function()
		var_5_3(False), SFX_PANEL)
	onButton(arg_5_0, arg_5_0._tf.Find("Right/Collapse"), function()
		var_5_3(True), SFX_PANEL)
	onButton(arg_5_0, arg_5_0._tf.Find("Right/Auto"), function()
		arg_5_0.AutoReplaceFurniture(), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.lableTrans, function()
		arg_5_0.CleanSlot())

	arg_5_0.furnitureItems = {}

	function arg_5_0.furnitureScroll.onUpdateItem(arg_17_0, arg_17_1)
		arg_17_0 = arg_17_0 + 1
		arg_5_0.furnitureItems[arg_17_0] = arg_17_1

		arg_5_0.UpdateFurnitureItem(arg_17_0)

	arg_5_0.replaceFurnitures = {}

	arg_5_0.scene.EnterFurnitureWatchMode()
	arg_5_0.UpdateZone()
	arg_5_0.UpdateView()

def var_0_0.UpdateZone(arg_18_0):
	local var_18_0 = arg_18_0.apartment
	local var_18_1 = var_18_0.GetNormalZones()[arg_18_0.zoneIndex]
	local var_18_2 = {
		var_18_1,
		unpack(var_18_0.GetGlobalZones())
	}
	local var_18_3 = _.reduce(var_18_2, {}, function(arg_19_0, arg_19_1)
		table.insertto(arg_19_0, arg_19_1.GetSlots())

		return arg_19_0)

	arg_18_0.activeFurnitureTypes = {}

	local var_18_4 = 99

	_.each(var_18_3, function(arg_20_0)
		arg_18_0.activeFurnitureTypes[arg_20_0.GetType()] = True
		var_18_4 = math.min(var_18_4, arg_20_0.GetType()))

	arg_18_0.activeFurnitureTypes = _.keys(arg_18_0.activeFurnitureTypes)

	var_18_1.SortTypes(arg_18_0.activeFurnitureTypes)

	arg_18_0.furnitureType = arg_18_0.activeFurnitureTypes[1]

	setText(arg_18_0._tf.Find("Right/Panel/Zone/Name"), var_18_1.GetName())
	arg_18_0.UpdateDisplayFurnitures()

def var_0_0.UpdateDisplayFurnitures(arg_21_0):
	local var_21_0 = arg_21_0.apartment
	local var_21_1 = arg_21_0.furnitureType

	arg_21_0.selectMode = var_0_0.SELECT_MODE.NONE
	arg_21_0.selectFurnitureId = None
	arg_21_0.selectSlotId = None

	local var_21_2 = var_21_0.GetFurnitures()
	local var_21_3 = {}
	local var_21_4 = {}

	_.each(var_21_2, function(arg_22_0)
		local var_22_0 = arg_22_0.GetConfigID()

		if var_21_3[var_22_0]:
			table.insert(var_21_4[var_21_3[var_22_0]].instances, arg_22_0)

			return

		if arg_22_0.GetType() != var_21_1:
			return

		table.insert(var_21_4, {
			useable = 0,
			id = var_22_0,
			instances = {
				arg_22_0
			}
		})

		var_21_3[var_22_0] = #var_21_4)

	arg_21_0.displayFurnitures = var_21_4

	_.each(arg_21_0.displayFurnitures, function(arg_23_0)
		arg_23_0.useable = _.reduce(arg_23_0.instances, 0, function(arg_24_0, arg_24_1)
			return arg_24_0 + (arg_24_1.GetSlotID() == 0 and 1 or 0)))
	arg_21_0.FilterFurnitures()

def var_0_0.FilterFurnitures(arg_25_0):
	local var_25_0 = {
		function(arg_26_0)
			return arg_26_0.useable > 0 and 0 or 1,
		function(arg_27_0)
			return -arg_27_0.instances[1].GetRarity(),
		function(arg_28_0)
			return -arg_28_0.id
	}

	if arg_25_0.selectMode == var_0_0.SELECT_MODE.SLOT:
		local var_25_1 = Dorm3dFurnitureSlot.New({
			configId = arg_25_0.selectSlotId
		})

		_.each(arg_25_0.displayFurnitures, function(arg_29_0)
			local var_29_0 = arg_29_0.instances[1]

			arg_29_0.fit = var_25_1.CanUseFurniture(var_29_0))

	table.sort(arg_25_0.displayFurnitures, CompareFuncs(var_25_0))

def var_0_0.UpdateView(arg_30_0):
	local var_30_0 = arg_30_0.apartment
	local var_30_1 = var_30_0.GetNormalZones()

	UIItemList.StaticAlign(arg_30_0.zoneList.Find("List"), arg_30_0.zoneList.Find("List").GetChild(0), #var_30_1, function(arg_31_0, arg_31_1, arg_31_2)
		if arg_31_0 != UIItemList.EventUpdate:
			return

		arg_31_1 = arg_31_1 + 1

		local var_31_0 = var_30_1[arg_31_1]

		setText(arg_31_2.Find("Name"), var_31_0.GetName())
		onButton(arg_30_0, arg_31_2, function()
			arg_30_0.zoneIndex = arg_31_1

			arg_30_0.UpdateZone()
			arg_30_0.UpdateView()
			setActive(arg_30_0.zoneList, False), SFX_PANEL)
		setActive(arg_31_2.Find("Line"), arg_31_1 < #var_30_1)

		local var_31_1 = arg_31_2.Find("Name").GetComponent(typeof(Text)).color
		local var_31_2 = arg_30_0.zoneIndex == arg_31_1 and Color.NewHex("39bfff") or Color.white

		var_31_2.a = var_31_1.a

		setTextColor(arg_31_2.Find("Name"), var_31_2))
	UIItemList.StaticAlign(arg_30_0._tf.Find("Right/Panel/Types"), arg_30_0._tf.Find("Right/Panel/Types").GetChild(0), #arg_30_0.activeFurnitureTypes, function(arg_33_0, arg_33_1, arg_33_2)
		if arg_33_0 != UIItemList.EventUpdate:
			return

		arg_33_1 = arg_33_1 + 1

		local var_33_0 = arg_30_0.activeFurnitureTypes[arg_33_1]

		setText(arg_33_2.Find("Name"), i18n(Dorm3dFurniture.TYPE2NAME[var_33_0]))
		setActive(arg_33_2.Find("Selected"), arg_30_0.furnitureType == var_33_0)
		onButton(arg_30_0, arg_33_2, function()
			if arg_30_0.furnitureType == var_33_0:
				return

			arg_30_0.furnitureType = var_33_0

			arg_30_0.UpdateDisplayFurnitures()
			arg_30_0.UpdateView()
			setActive(arg_30_0.zoneList, False), SFX_PANEL))
	arg_30_0.furnitureScroll.SetTotalCount(#arg_30_0.displayFurnitures)
	setActive(arg_30_0.furnitureEmpty, #arg_30_0.displayFurnitures == 0)

	local var_30_2 = {}
	local var_30_3 = var_30_1[arg_30_0.zoneIndex]
	local var_30_4 = arg_30_0.furnitureType
	local var_30_5 = {
		var_30_3,
		unpack(var_30_0.GetGlobalZones())
	}
	local var_30_6 = _.reduce(var_30_5, {}, function(arg_35_0, arg_35_1)
		table.insertto(arg_35_0, arg_35_1.GetSlots())

		return arg_35_0)
	local var_30_7 = _.select(var_30_6, function(arg_36_0)
		return arg_36_0.GetType() == var_30_4)

	_.each(var_30_7, function(arg_37_0)
		local var_37_0 = arg_37_0.GetConfigID()

		if arg_30_0.selectMode == var_0_0.SELECT_MODE.NONE:
			var_30_2[var_37_0] = 0
		elif arg_30_0.selectMode == var_0_0.SELECT_MODE.FURNITURE:
			local var_37_1 = arg_37_0.CanUseFurniture(Dorm3dFurniture.New({
				configId = arg_30_0.selectFurnitureId
			}))

			var_30_2[var_37_0] = var_37_1 and 1 or 2
		elif arg_30_0.selectMode == var_0_0.SELECT_MODE.SLOT:
			var_30_2[var_37_0] = arg_30_0.selectSlotId == var_37_0 and 1 or 0)

	local var_30_8 = False

	if arg_30_0.selectMode == var_0_0.SELECT_MODE.SLOT:
		local var_30_9 = Dorm3dFurnitureSlot.New({
			configId = arg_30_0.selectSlotId
		})

		if var_30_9.GetType() == Dorm3dFurniture.TYPE.DECORATION:
			local var_30_10 = arg_30_0.apartment.GetFurnitures()

			if _.detect(var_30_10, function(arg_38_0)
				return arg_38_0.GetSlotID() == var_30_9.GetConfigID()):
				local var_30_11 = arg_30_0.scene.GetSlotByID(var_30_9.GetConfigID())
				local var_30_12 = arg_30_0.scene.GetScreenPosition(var_30_11) or Vector2.New(-10000, -10000)

				setAnchoredPosition(arg_30_0.lableTrans, var_30_12)

				var_30_8 = True

	setActive(arg_30_0.lableTrans, var_30_8)

	if arg_30_0.activeZoneId != var_30_3.GetConfigID():
		arg_30_0.blockActive = True

		arg_30_0.scene.SwitchZone(var_30_3, function()
			arg_30_0.blockActive = False)

		arg_30_0.activeZoneId = var_30_3.GetConfigID()

	arg_30_0.scene.DisplayFurnitureSlots(_.map(var_30_7, function(arg_40_0)
		return arg_40_0.GetConfigID()))
	arg_30_0.scene.UpdateDisplaySlots(var_30_2)
	arg_30_0.scene.RefreshSlots(arg_30_0.apartment)

def var_0_0.UpdateFurnitureItem(arg_41_0, arg_41_1):
	local var_41_0 = arg_41_0.furnitureItems[arg_41_1]
	local var_41_1 = arg_41_0.displayFurnitures[arg_41_1]

	if not var_41_0:
		return

	local var_41_2 = tf(var_41_0)

	updateDrop(var_41_2.Find("Item/Icon"), {
		type = DROP_TYPE_DORM3D_FURNITURE,
		id = var_41_1.id
	})
	setText(var_41_2.Find("Item/Name"), var_41_1.instances[1].GetName())

	local var_41_3 = i18n("dorm3d_furniture_count", var_41_1.useable .. "/" .. #var_41_1.instances)

	if var_41_1.useable < #var_41_1.instances:
		var_41_3 = i18n("dorm3d_furniture_used") .. var_41_3

	setText(var_41_2.Find("Item/Count"), var_41_3)
	setActive(var_41_2.Find("Selected"), arg_41_0.selectFurnitureId == var_41_1.id)

	local var_41_4 = arg_41_0.selectMode == var_0_0.SELECT_MODE.SLOT and not var_41_1.fit

	setActive(var_41_2.Find("Unfit"), var_41_4)

	local var_41_5 = not var_41_4 and var_41_1.useable == 0

	setActive(var_41_2.Find("Lack"), var_41_5)
	setCanvasGroupAlpha(var_41_2.Find("Item"), (var_41_4 or var_41_5) and 0.3 or 1)
	onButton(arg_41_0, var_41_2.Find("Item/Tip"), function()
		arg_41_0.emit(Dorm3dFurnitureSelectMediator.SHOW_FURNITURE_ACESSES, {
			showGOBtn = True,
			title = i18n("courtyard_label_detail"),
			drop = {
				type = DROP_TYPE_DORM3D_FURNITURE,
				id = var_41_1.id,
				count = #var_41_1.instances
			},
			list = var_41_1.instances[1].GetAcesses()
		}), SFX_PANEL)
	onButton(arg_41_0, var_41_2, function()
		local var_43_0 = var_41_1.instances[1].GetType()

		local function var_43_1()
			local var_44_0 = _.detect(arg_41_0.apartment.GetGlobalZones()[1].GetSlots(), function(arg_45_0)
				return arg_45_0.GetType() == var_43_0)

			if not var_44_0:
				return

			arg_41_0.apartment.ReplaceFurniture(var_44_0.GetConfigID(), var_41_1.id)
			table.insert(arg_41_0.replaceFurnitures, {
				slotId = var_44_0.GetConfigID(),
				furnitureId = var_41_1.id
			})
			arg_41_0.UpdateDisplayFurnitures()

		if arg_41_0.selectMode == var_0_0.SELECT_MODE.NONE:
			if var_41_1.useable > 0:
				if var_43_0 == Dorm3dFurniture.TYPE.FLOOR or var_43_0 == Dorm3dFurniture.TYPE.WALLPAPER:
					var_43_1()
				else
					arg_41_0.selectMode = var_0_0.SELECT_MODE.FURNITURE
					arg_41_0.selectFurnitureId = var_41_1.id

				arg_41_0.UpdateView()

			return

		if arg_41_0.selectMode == var_0_0.SELECT_MODE.SLOT:
			if var_41_1.fit and var_41_1.useable > 0:
				arg_41_0.apartment.ReplaceFurniture(arg_41_0.selectSlotId, var_41_1.id)
				table.insert(arg_41_0.replaceFurnitures, {
					slotId = arg_41_0.selectSlotId,
					furnitureId = var_41_1.id
				})
				arg_41_0.UpdateDisplayFurnitures()
				arg_41_0.UpdateView()

			return

		if arg_41_0.selectMode == var_0_0.SELECT_MODE.FURNITURE:
			if arg_41_0.selectFurnitureId == var_41_1.id:
				arg_41_0.selectMode = var_0_0.SELECT_MODE.NONE
				arg_41_0.selectFurnitureId = None

				arg_41_0.UpdateView()
			elif var_41_1.useable > 0:
				if var_43_0 == Dorm3dFurniture.TYPE.FLOOR or var_43_0 == Dorm3dFurniture.TYPE.WALLPAPER:
					var_43_1()
				else
					arg_41_0.selectFurnitureId = var_41_1.id

					arg_41_0.UpdateView()

			return, SFX_PANEL)

def var_0_0.OnClickFurnitureSlot(arg_46_0, arg_46_1):
	if arg_46_0.selectMode == var_0_0.SELECT_MODE.FURNITURE:
		local var_46_0 = _.detect(arg_46_0.displayFurnitures, function(arg_47_0)
			return arg_47_0.id == arg_46_0.selectFurnitureId)
		local var_46_1 = Dorm3dFurnitureSlot.New({
			configId = arg_46_1
		})

		if var_46_0 and var_46_0.useable > 0 and var_46_1.CanUseFurniture(var_46_0.instances[1]):
			arg_46_0.apartment.ReplaceFurniture(arg_46_1, var_46_0.id)
			table.insert(arg_46_0.replaceFurnitures, {
				slotId = arg_46_1,
				furnitureId = var_46_0.id
			})
			arg_46_0.UpdateDisplayFurnitures()
		else
			return
	elif arg_46_0.selectMode == var_0_0.SELECT_MODE.NONE:
		arg_46_0.selectMode = var_0_0.SELECT_MODE.SLOT
		arg_46_0.selectSlotId = arg_46_1

		arg_46_0.FilterFurnitures()
	elif arg_46_0.selectMode == var_0_0.SELECT_MODE.SLOT:
		if arg_46_0.selectSlotId == arg_46_1:
			arg_46_0.selectMode = var_0_0.SELECT_MODE.NONE
			arg_46_0.selectSlotId = None
		else
			arg_46_0.selectSlotId = arg_46_1

		arg_46_0.FilterFurnitures()

	arg_46_0.UpdateView()

def var_0_0.CleanSlot(arg_48_0):
	if arg_48_0.selectMode != var_0_0.SELECT_MODE.SLOT:
		return

	local var_48_0 = arg_48_0.selectSlotId

	arg_48_0.apartment.ReplaceFurniture(var_48_0, 0)
	table.insert(arg_48_0.replaceFurnitures, {
		furnitureId = 0,
		slotId = var_48_0
	})
	arg_48_0.UpdateDisplayFurnitures()
	arg_48_0.UpdateView()

def var_0_0.OnReplaceFurnitureDone(arg_49_0):
	arg_49_0.replaceFurnitures = {}

	existCall(arg_49_0.replaceFurnitureCallback)

	arg_49_0.replaceFurnitureCallback = None

def var_0_0.OnReplaceFurnitureError(arg_50_0):
	arg_50_0.replaceFurnitureCallback = None

def var_0_0.AutoReplaceFurniture(arg_51_0):
	local var_51_0 = arg_51_0.apartment.GetNormalZones()[arg_51_0.zoneIndex].GetSlots()

	_.each(var_51_0, function(arg_52_0)
		if arg_52_0.GetType() == Dorm3dFurniture.TYPE.FLOOR or arg_52_0.GetType() == Dorm3dFurniture.TYPE.WALLPAPER:
			return

		local var_52_0 = arg_51_0.apartment.GetFurnitures()
		local var_52_1 = _.detect(var_52_0, function(arg_53_0)
			return arg_53_0.GetSlotID() == arg_52_0.GetConfigID())

		if var_52_1 and var_52_1.GetConfigID() != arg_52_0.GetDefaultFurniture():
			return

		local var_52_2 = table.shallowCopy(var_52_0)
		local var_52_3 = {
			function(arg_54_0)
				return arg_54_0.GetSlotID() == 0 and arg_52_0.CanUseFurniture(arg_54_0) and 0 or 1,
			function(arg_55_0)
				return -arg_55_0.GetRarity(),
			function(arg_56_0)
				return -arg_56_0.GetConfigID()
		}

		table.sort(var_52_2, CompareFuncs(var_52_3))

		local var_52_4 = var_52_2[1]

		if not var_52_4 or var_52_4.GetSlotID() != 0 or not arg_52_0.CanUseFurniture(var_52_4):
			return

		arg_51_0.apartment.ReplaceFurniture(arg_52_0.GetConfigID(), var_52_4.GetConfigID())
		table.insert(arg_51_0.replaceFurnitures, {
			slotId = arg_52_0.GetConfigID(),
			furnitureId = var_52_4.GetConfigID()
		}))
	arg_51_0.UpdateView()

def var_0_0.ShowReplaceWindow(arg_57_0, arg_57_1, arg_57_2):
	local var_57_0 = arg_57_0.replaceFurnitures

	if #var_57_0 == 0:
		return existCall(arg_57_1)

	arg_57_0.emit(Dorm3dFurnitureSelectMediator.SHOW_CONFIRM_WINDOW, {
		title = i18n("title_info"),
		content = i18n("dorm3d_replace_furniture_confirm"),
		def onYes:()
			arg_57_0.emit(GAME.APARTMENT_REPLACE_FURNITURE, {
				shipGroupId = arg_57_0.apartment.GetConfigID(),
				furnitures = var_57_0
			})

			arg_57_0.replaceFurnitureCallback = arg_57_1,
		onNo = arg_57_2
	})

def var_0_0.onBackPressed(arg_59_0):
	if arg_59_0.blockActive:
		return

	seriesAsync({
		function(arg_60_0)
			arg_59_0.ShowReplaceWindow(arg_60_0, arg_60_0),
		function(arg_61_0)
			var_0_0.super.onBackPressed(arg_59_0)
	})

def var_0_0.willExit(arg_62_0):
	arg_62_0.scene.ExitFurnitureWatchMode()

return var_0_0
