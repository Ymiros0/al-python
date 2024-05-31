﻿local var_0_0 = class("SingleBuffDetailLayer", import("..base.BaseUI"))

function var_0_0.getUIName(arg_1_0)
	return "TechnologyTreeSingleBuffDetailUI"
end

function var_0_0.init(arg_2_0)
	arg_2_0:initData()
	arg_2_0:findUI()
end

function var_0_0.didEnter(arg_3_0)
	pg.UIMgr.GetInstance():BlurPanel(arg_3_0._tf)
	arg_3_0:addListener()
	arg_3_0:updateDetail()
end

function var_0_0.willExit(arg_4_0)
	pg.UIMgr.GetInstance():UnblurPanel(arg_4_0._tf)
end

function var_0_0.initData(arg_5_0)
	arg_5_0.groupID = arg_5_0.contextData.groupID
	arg_5_0.maxLV = arg_5_0.contextData.maxLV
	arg_5_0.star = arg_5_0.contextData.star
	arg_5_0.classID = pg.fleet_tech_ship_template[arg_5_0.groupID].class
	arg_5_0.shipID = arg_5_0.groupID * 10 + 1
	arg_5_0.rarity = pg.ship_data_statistics[arg_5_0.shipID].rarity
	arg_5_0.shipPaintName = Ship.getPaintingName(arg_5_0.shipID)
	arg_5_0.shipType = pg.fleet_tech_ship_class[arg_5_0.classID].shiptype
	arg_5_0.classLevel = pg.fleet_tech_ship_class[arg_5_0.classID].t_level
	arg_5_0.typeToColor = {
		[ShipType.QuZhu] = Color.New(0.25882352941176473, 0.9215686274509803, 1, 1),
		[ShipType.QingXun] = Color.New(1, 0.9137254901960784, 0.4470588235294118, 1),
		[ShipType.ZhongXun] = Color.New(1, 0.9137254901960784, 0.4470588235294118, 1),
		[ShipType.ChaoXun] = Color.New(1, 0.9137254901960784, 0.4470588235294118, 1),
		[ShipType.ZhanXun] = Color.New(0.9529411764705882, 0.396078431372549, 0.396078431372549, 1),
		[ShipType.ZhanLie] = Color.New(0.9529411764705882, 0.396078431372549, 0.396078431372549, 1),
		[ShipType.HangXun] = Color.New(0.9529411764705882, 0.396078431372549, 0.396078431372549, 1),
		[ShipType.HangZhan] = Color.New(0.9529411764705882, 0.396078431372549, 0.396078431372549, 1),
		[ShipType.LeiXun] = Color.New(0.9529411764705882, 0.396078431372549, 0.396078431372549, 1),
		[ShipType.ZhongPao] = Color.New(0.9529411764705882, 0.396078431372549, 0.396078431372549, 1),
		[ShipType.QingHang] = Color.New(0.8745098039215686, 0.6588235294117647, 1, 1),
		[ShipType.ZhengHang] = Color.New(0.8745098039215686, 0.6588235294117647, 1, 1),
		[ShipType.QianTing] = Color.New(0.7215686274509804, 1, 0.23529411764705882, 1),
		[ShipType.QianMu] = Color.New(0.7215686274509804, 1, 0.23529411764705882, 1),
		[ShipType.WeiXiu] = Color.New(0.7215686274509804, 1, 0.23529411764705882, 1),
		[ShipType.Yunshu] = Color.New(0.7215686274509804, 1, 0.23529411764705882, 1),
		[ShipType.FengFanS] = Color.New(0.7215686274509804, 1, 0.23529411764705882, 1),
		[ShipType.FengFanV] = Color.New(0.7215686274509804, 1, 0.23529411764705882, 1),
		[ShipType.FengFanM] = Color.New(0.7215686274509804, 1, 0.23529411764705882, 1)
	}
end

function var_0_0.findUI(arg_6_0)
	arg_6_0.backBtn = arg_6_0:findTF("BG")
	arg_6_0.detailPanel = arg_6_0:findTF("DetailPanel")
	arg_6_0.baseImg = arg_6_0:findTF("Info/BaseImg", arg_6_0.detailPanel)
	arg_6_0.modelImg = arg_6_0:findTF("ModelImg", arg_6_0.baseImg)
	arg_6_0.top = arg_6_0:findTF("Info/top", arg_6_0.detailPanel)
	arg_6_0.levelImg = arg_6_0:findTF("LevelImg", arg_6_0.top)
	arg_6_0.typeTextImg = arg_6_0:findTF("TypeTextImg", arg_6_0.top)
	arg_6_0.nameText = arg_6_0:findTF("Name/NameText", arg_6_0.top)
	arg_6_0.buffItemTpl = arg_6_0:findTF("Info/BuffItemTpl", arg_6_0.detailPanel)
	arg_6_0.buffGetItem = arg_6_0:findTF("Info/BuffGetItemTop", arg_6_0.detailPanel)
	arg_6_0.statusGetImg = arg_6_0:findTF("StatusBG/StatusImg", arg_6_0.buffGetItem)
	arg_6_0.pointNumGetText = arg_6_0:findTF("Point/PointNumText", arg_6_0.buffGetItem)
	arg_6_0.buffGetItemContainer = arg_6_0:findTF("Info/BuffGetItemContainer", arg_6_0.detailPanel)
	arg_6_0.buffCompleteItem = arg_6_0:findTF("Info/BuffCompleteItemTop", arg_6_0.detailPanel)
	arg_6_0.statusCompleteImg = arg_6_0:findTF("StatusBG/StatusImg", arg_6_0.buffCompleteItem)
	arg_6_0.pointNumCompleteText = arg_6_0:findTF("Point/PointNumText", arg_6_0.buffCompleteItem)
	arg_6_0.buffCompleteItemContainer = arg_6_0:findTF("Info/BuffCompleteItemContainer", arg_6_0.detailPanel)
	arg_6_0.allStarStatusImg = arg_6_0:findTF("Info/AllStarTop/StatusBG/StatusImg", arg_6_0.detailPanel)
	arg_6_0.allStarPointText = arg_6_0:findTF("Info/AllStarTop/Point/PointNumText", arg_6_0.detailPanel)
end

function var_0_0.onBackPressed(arg_7_0)
	triggerButton(arg_7_0.backBtn)
end

function var_0_0.addListener(arg_8_0)
	onButton(arg_8_0, arg_8_0.backBtn, function()
		arg_8_0:emit(var_0_0.ON_CLOSE)
	end, SFX_CANCEL)
end

function var_0_0.updateDetail(arg_10_0)
	LoadSpriteAsync("shipmodels/" .. arg_10_0.shipPaintName, function(arg_11_0)
		if arg_11_0 then
			setImageSprite(arg_10_0.modelImg, arg_11_0, true)

			rtf(arg_10_0.modelImg).pivot = getSpritePivot(arg_11_0)
		end
	end)
	setImageSprite(arg_10_0.baseImg, GetSpriteFromAtlas("shipraritybaseicon", "base_" .. arg_10_0.rarity))
	setImageSprite(arg_10_0.typeTextImg, GetSpriteFromAtlas("ShipType", "ch_title_" .. arg_10_0.shipType), true)
	setText(arg_10_0.nameText, ShipGroup.getDefaultShipNameByGroupID(arg_10_0.groupID))

	if ShipGroup.IsMetaGroup(arg_10_0.groupID) or ShipGroup.IsMotGroup(arg_10_0.groupID) then
		setActive(arg_10_0.levelImg, false)
	else
		setImageSprite(arg_10_0.levelImg, GetSpriteFromAtlas("TecClassLevelIcon", "T" .. arg_10_0.classLevel), true)
		setActive(arg_10_0.levelImg, true)
	end

	local var_10_0 = pg.fleet_tech_ship_template[arg_10_0.groupID].pt_get
	local var_10_1 = pg.fleet_tech_ship_template[arg_10_0.groupID].pt_level

	setText(arg_10_0.pointNumGetText, "+" .. var_10_0)
	setText(arg_10_0.pointNumCompleteText, "+" .. var_10_1)
	setText(arg_10_0.allStarPointText, "+" .. pg.fleet_tech_ship_template[arg_10_0.groupID].pt_upgrage)

	if arg_10_0.star >= pg.fleet_tech_ship_template[arg_10_0.groupID].max_star then
		setImageColor(arg_10_0.allStarStatusImg, Color.New(1, 0.9137254901960784, 0.4470588235294118, 1))
	end

	if arg_10_0.maxLV >= TechnologyConst.SHIP_LEVEL_FOR_BUFF then
		setImageColor(arg_10_0.statusCompleteImg, Color.New(1, 0.9137254901960784, 0.4470588235294118, 1))
	end

	local var_10_2 = arg_10_0:getSpecialTypeList(pg.fleet_tech_ship_template[arg_10_0.groupID].add_get_shiptype)
	local var_10_3 = pg.fleet_tech_ship_template[arg_10_0.groupID].add_get_attr
	local var_10_4 = pg.fleet_tech_ship_template[arg_10_0.groupID].add_get_value
	local var_10_5 = UIItemList.New(arg_10_0.buffGetItemContainer, arg_10_0.buffItemTpl)

	var_10_5:make(function(arg_12_0, arg_12_1, arg_12_2)
		if arg_12_0 == UIItemList.EventUpdate then
			local var_12_0 = arg_10_0:findTF("Symbol/Left", arg_12_2)
			local var_12_1 = arg_10_0:findTF("Symbol/Right", arg_12_2)
			local var_12_2 = arg_10_0:findTF("TypeText", arg_12_2)
			local var_12_3 = arg_10_0:findTF("AttrText", arg_12_2)
			local var_12_4 = arg_10_0:findTF("ValueText", arg_12_2)
			local var_12_5 = var_10_2[arg_12_1 + 1]
			local var_12_6 = arg_10_0.typeToColor[var_12_5]

			setTextColor(var_12_0, var_12_6)
			setTextColor(var_12_1, var_12_6)
			setText(var_12_2, ShipType.Type2Name(var_12_5))
			setTextColor(var_12_2, var_12_6)
			setText(var_12_3, AttributeType.Type2Name(pg.attribute_info_by_type[var_10_3].name))
			setText(var_12_4, "+" .. var_10_4)
			setActive(arg_12_2, true)
		end
	end)
	var_10_5:align(#var_10_2)

	local var_10_6 = arg_10_0:getSpecialTypeList(pg.fleet_tech_ship_template[arg_10_0.groupID].add_level_shiptype)
	local var_10_7 = pg.fleet_tech_ship_template[arg_10_0.groupID].add_level_attr
	local var_10_8 = pg.fleet_tech_ship_template[arg_10_0.groupID].add_level_value
	local var_10_9 = UIItemList.New(arg_10_0.buffCompleteItemContainer, arg_10_0.buffItemTpl)

	var_10_9:make(function(arg_13_0, arg_13_1, arg_13_2)
		if arg_13_0 == UIItemList.EventUpdate then
			local var_13_0 = arg_10_0:findTF("Symbol/Left", arg_13_2)
			local var_13_1 = arg_10_0:findTF("Symbol/Right", arg_13_2)
			local var_13_2 = arg_10_0:findTF("TypeText", arg_13_2)
			local var_13_3 = arg_10_0:findTF("AttrText", arg_13_2)
			local var_13_4 = arg_10_0:findTF("ValueText", arg_13_2)
			local var_13_5 = arg_10_0:findTF("BG", arg_13_2)
			local var_13_6 = var_10_6[arg_13_1 + 1]
			local var_13_7

			if arg_10_0.maxLV >= TechnologyConst.SHIP_LEVEL_FOR_BUFF then
				var_13_7 = arg_10_0.typeToColor[var_13_6]

				setGray(var_13_5, false)
			else
				var_13_7 = Color.New(0.6392156862745098, 0.6392156862745098, 0.6392156862745098, 1)

				setTextColor(var_13_4, var_13_7)
				setTextColor(var_13_3, var_13_7)
				setGray(var_13_5, true)
			end

			setTextColor(var_13_0, var_13_7)
			setTextColor(var_13_1, var_13_7)
			setText(var_13_2, ShipType.Type2Name(var_13_6))
			setTextColor(var_13_2, var_13_7)
			setText(var_13_3, AttributeType.Type2Name(pg.attribute_info_by_type[var_10_7].name))
			setText(var_13_4, "+" .. var_10_8)
			setActive(arg_13_2, true)
		end
	end)
	var_10_9:align(#var_10_6)
end

function var_0_0.getSpecialTypeList(arg_14_0, arg_14_1)
	local var_14_0 = ShipType.FilterOverQuZhuType(arg_14_1)

	return (ShipType.FilterOverFengFanType(var_14_0))
end

return var_0_0
