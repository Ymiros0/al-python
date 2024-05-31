local var_0_0 = class("DialogueStep", import(".StoryStep"))

var_0_0.SIDE_LEFT = 0
var_0_0.SIDE_RIGHT = 1
var_0_0.SIDE_MIDDLE = 2
var_0_0.ACTOR_TYPE_PLAYER = 0
var_0_0.ACTOR_TYPE_FLAGSHIP = -1
var_0_0.ACTOR_TYPE_TB = -2
var_0_0.PAINTING_ACTION_MOVE = "move"
var_0_0.PAINTING_ACTION_SHAKE = "shake"
var_0_0.PAINTING_ACTION_ZOOM = "zoom"
var_0_0.PAINTING_ACTION_ROTATE = "rotate"

local var_0_1 = pg.ship_skin_template

local function var_0_2(arg_1_0)
	local var_1_0 = string.lower(arg_1_0)

	if var_1_0 == "#a9f548" or var_1_0 == "#a9f548ff" then
		return "#5CE6FF"
	elseif var_1_0 == "#ff5c5c" then
		return "#FF9B93"
	elseif var_1_0 == "#ffa500" then
		return "#FFC960"
	elseif var_1_0 == "#ffff4d" then
		return "#FEF15E"
	elseif var_1_0 == "#696969" then
		return "#BDBDBD"
	elseif var_1_0 == "#a020f0" then
		return "#C3ABFF"
	elseif var_1_0 == "#ffffff" then
		return "#FFFFFF"
	else
		return arg_1_0
	end
end

function var_0_0.Ctor(arg_2_0, arg_2_1)
	var_0_0.super.Ctor(arg_2_0, arg_2_1)

	arg_2_0.actor = arg_2_1.actor

	if arg_2_1.nameColor then
		arg_2_0.nameColor = var_0_2(arg_2_1.nameColor)
	else
		arg_2_0.nameColor = COLOR_WHITE
	end

	arg_2_0.specialTbId = nil

	if arg_2_1.tbActor then
		arg_2_0.specialTbId = arg_2_0.actor
		arg_2_0.actor = var_0_0.ACTOR_TYPE_TB
	end

	arg_2_0.actorName = arg_2_1.actorName
	arg_2_0.subActorName = arg_2_1.factiontag
	arg_2_0.subActorNameColor = arg_2_1.factiontagColor or "#FFFFFF"
	arg_2_0.withoutActorName = arg_2_1.withoutActorName
	arg_2_0.say = arg_2_1.say
	arg_2_0.dynamicBgType = arg_2_1.dynamicBgType
	arg_2_0.fontSize = arg_2_1.fontsize
	arg_2_0.side = arg_2_1.side
	arg_2_0.dir = arg_2_1.dir

	if arg_2_0.dir == 0 then
		arg_2_0.dir = 1
	end

	arg_2_0.expression = arg_2_1.expression
	arg_2_0.typewriter = arg_2_1.typewriter
	arg_2_0.painting = arg_2_1.painting
	arg_2_0.fadeInPaintingTime = arg_2_1.fadeInPaintingTime or 0.15
	arg_2_0.fadeOutPaintingTime = arg_2_1.fadeOutPaintingTime or 0.15
	arg_2_0.actorPosition = arg_2_1.actorPosition
	arg_2_0.dialogShake = arg_2_1.dialogShake
	arg_2_0.moveSideData = arg_2_1.paintingFadeOut
	arg_2_0.paingtingGray = arg_2_1.paingtingGray
	arg_2_0.glitchArt = arg_2_1.paintingNoise
	arg_2_0.hideOtherPainting = arg_2_1.hideOther
	arg_2_0.subPaintings = arg_2_1.subActors
	arg_2_0.disappearSeq = {}
	arg_2_0.disappearTime = {
		0,
		0
	}

	if arg_2_0.subPaintings and #arg_2_0.subPaintings > 0 and arg_2_1.disappearSeq then
		arg_2_0.disappearSeq = arg_2_1.disappearSeq
		arg_2_0.disappearTime = arg_2_1.disappearTime or {
			0,
			0
		}
	end

	arg_2_0.hideRecordIco = arg_2_1.hideRecordIco
	arg_2_0.paingtingScale = arg_2_1.actorScale
	arg_2_0.hidePainting = arg_2_1.withoutPainting
	arg_2_0.actorShadow = arg_2_1.actorShadow
	arg_2_0.actorAlpha = arg_2_1.actorAlpha
	arg_2_0.showNPainting = arg_2_1.hidePaintObj
	arg_2_0.hasPaintbg = arg_2_1.hasPaintbg
	arg_2_0.showWJZPainting = arg_2_1.hidePaintEquip
	arg_2_0.nohead = arg_2_1.nohead
	arg_2_0.live2d = arg_2_1.live2d
	arg_2_0.live2dIdleIndex = arg_2_1.live2dIdleIndex
	arg_2_0.spine = arg_2_1.spine
	arg_2_0.spineOrderIndex = arg_2_1.spineOrderIndex
	arg_2_0.live2dOffset = arg_2_1.live2dOffset
	arg_2_0.contentBGAlpha = arg_2_1.dialogueBgAlpha or 1
	arg_2_0.canMarkNode = arg_2_1.canMarkNode
	arg_2_0.portrait = arg_2_1.portrait
	arg_2_0.glitchArtForPortrait = arg_2_1.portraitNoise

	if arg_2_0.hidePainting or arg_2_0.actor == nil then
		arg_2_0.actor = nil
		arg_2_0.hideOtherPainting = true
	end

	arg_2_0.paintRwIndex = arg_2_1.paintRwIndex or 0
	arg_2_0.action = arg_2_1.action or {}
end

function var_0_0.GetBgName(arg_3_0)
	if arg_3_0.dynamicBgType and arg_3_0.dynamicBgType == var_0_0.ACTOR_TYPE_TB and getProxy(EducateProxy) and not pg.NewStoryMgr.GetInstance():IsReView() then
		local var_3_0, var_3_1, var_3_2 = getProxy(EducateProxy):GetStoryInfo()

		return (arg_3_0:Convert2StoryBg(var_3_2))
	else
		return var_0_0.super.GetBgName(arg_3_0)
	end
end

function var_0_0.Convert2StoryBg(arg_4_0, arg_4_1)
	return ({
		educate_tb_1 = "bg_project_tb_room1",
		educate_tb_2 = "bg_project_tb_room2",
		educate_tb_3 = "bg_project_tb_room3"
	})[arg_4_1] or arg_4_1
end

function var_0_0.GetPaintingRwIndex(arg_5_0)
	if not arg_5_0.glitchArt then
		return 0
	end

	if not arg_5_0.expression then
		return 0
	end

	return arg_5_0.paintRwIndex
end

function var_0_0.ExistPortrait(arg_6_0)
	return arg_6_0.portrait ~= nil
end

function var_0_0.GetPortrait(arg_7_0)
	if type(arg_7_0.portrait) == "number" then
		return pg.ship_skin_template[arg_7_0.portrait].painting
	elseif type(arg_7_0.portrait) == "string" then
		return arg_7_0.portrait
	else
		return nil
	end
end

function var_0_0.ShouldGlitchArtForPortrait(arg_8_0)
	return arg_8_0.glitchArtForPortrait
end

function var_0_0.GetMode(arg_9_0)
	return Story.MODE_DIALOGUE
end

function var_0_0.GetContentBGAlpha(arg_10_0)
	return arg_10_0.contentBGAlpha
end

function var_0_0.GetSpineExPression(arg_11_0)
	if arg_11_0.expression then
		return arg_11_0.expression
	end
end

function var_0_0.GetExPression(arg_12_0)
	if arg_12_0.expression then
		return arg_12_0.expression
	else
		local var_12_0 = arg_12_0:GetPainting()

		if var_12_0 and ShipExpressionHelper.DefaultFaceless(var_12_0) then
			return ShipExpressionHelper.GetDefaultFace(var_12_0)
		end
	end
end

function var_0_0.ShouldAddHeadMaskWhenFade(arg_13_0)
	if arg_13_0:ShouldAddGlitchArtEffect() then
		return false
	end

	if arg_13_0:IsNoHeadPainting() then
		return false
	end

	if not arg_13_0:GetExPression() then
		return false
	end

	return true
end

function var_0_0.ShouldGrayingPainting(arg_14_0, arg_14_1)
	return arg_14_1:GetPainting() ~= nil and not arg_14_0:IsSameSide(arg_14_1)
end

function var_0_0.ShouldGrayingOutPainting(arg_15_0, arg_15_1)
	return arg_15_0:GetPainting() ~= nil and not arg_15_0:IsSameSide(arg_15_1)
end

function var_0_0.ShouldFadeInPainting(arg_16_0)
	if not arg_16_0:GetPainting() then
		return false
	end

	if arg_16_0:IsLive2dPainting() or arg_16_0:IsSpinePainting() then
		return false
	end

	local var_16_0 = arg_16_0:GetFadeInPaintingTime()

	if not var_16_0 or var_16_0 <= 0 then
		return false
	end

	return true
end

function var_0_0.GetTypewriter(arg_17_0)
	return arg_17_0.typewriter
end

function var_0_0.ShouldFaceBlack(arg_18_0)
	return arg_18_0.actorShadow
end

function var_0_0.GetPaintingData(arg_19_0)
	local var_19_0 = arg_19_0.painting or {}

	return {
		alpha = var_19_0.alpha or 0.3,
		time = var_19_0.time or 1
	}
end

function var_0_0.GetFadeInPaintingTime(arg_20_0)
	return arg_20_0.fadeInPaintingTime
end

function var_0_0.GetFadeOutPaintingTime(arg_21_0)
	return arg_21_0.fadeOutPaintingTime
end

function var_0_0.GetPaintingDir(arg_22_0)
	local var_22_0 = arg_22_0.paingtingScale or 1

	return (arg_22_0.dir or 1) * var_22_0
end

function var_0_0.GetTag(arg_23_0)
	if arg_23_0.glitchArt == true then
		return 2
	else
		return 1
	end
end

function var_0_0.GetPaintingAlpha(arg_24_0)
	return arg_24_0.actorAlpha
end

function var_0_0.GetPaitingOffst(arg_25_0)
	return arg_25_0.actorPosition
end

function var_0_0.GetSound(arg_26_0)
	return arg_26_0.sound
end

function var_0_0.GetPaintingActions(arg_27_0)
	return arg_27_0.action
end

function var_0_0.GetPaintingMoveToSide(arg_28_0)
	return arg_28_0.moveSideData
end

function var_0_0.ShouldMoveToSide(arg_29_0)
	return arg_29_0.moveSideData ~= nil
end

function var_0_0.GetPaintingAction(arg_30_0, arg_30_1)
	local var_30_0 = {}
	local var_30_1 = arg_30_0:GetPaintingActions()

	for iter_30_0, iter_30_1 in ipairs(var_30_1) do
		if iter_30_1.type == arg_30_1 then
			table.insert(var_30_0, iter_30_1)
		end
	end

	return var_30_0
end

function var_0_0.GetSide(arg_31_0)
	return arg_31_0.side
end

function var_0_0.GetContent(arg_32_0)
	if not arg_32_0.say then
		return "..."
	end

	local var_32_0 = arg_32_0.say

	if arg_32_0:ShouldReplacePlayer() then
		var_32_0 = arg_32_0:ReplacePlayerName(var_32_0)
	end

	if arg_32_0:ShouldReplaceTb() then
		var_32_0 = arg_32_0:ReplaceTbName(var_32_0)
	end

	if PLATFORM_CODE ~= PLATFORM_US then
		var_32_0 = SwitchSpecialChar(HXSet.hxLan(var_32_0), true)
	else
		var_32_0 = HXSet.hxLan(var_32_0)
	end

	return var_32_0
end

function var_0_0.GetNameWithColor(arg_33_0)
	local var_33_0 = arg_33_0:GetName()

	if not var_33_0 then
		return nil
	end

	local var_33_1 = arg_33_0:GetNameColor()

	return setColorStr(var_33_0, var_33_1)
end

function var_0_0.GetNameColor(arg_34_0)
	return arg_34_0.nameColor or COLOR_WHITE
end

function var_0_0.GetNameColorCode(arg_35_0)
	local var_35_0 = arg_35_0:GetNameColor()

	return string.gsub(var_35_0, "#", "")
end

function var_0_0.GetCustomActorName(arg_36_0)
	if type(arg_36_0.actorName) == "number" and arg_36_0.actorName == 0 and getProxy(PlayerProxy) then
		return getProxy(PlayerProxy):getRawData().name
	elseif type(arg_36_0.actorName) == "string" then
		return arg_36_0.actorName
	else
		return ""
	end
end

function var_0_0.GetName(arg_37_0)
	local var_37_0 = arg_37_0.actorName and arg_37_0:GetCustomActorName() or arg_37_0:GetPaintingAndName() or ""

	if not var_37_0 or var_37_0 == "" or arg_37_0.withoutActorName then
		return nil
	end

	if arg_37_0:ShouldReplacePlayer() then
		var_37_0 = arg_37_0:ReplacePlayerName(var_37_0)
	end

	if arg_37_0:ShouldReplaceTb() then
		var_37_0 = arg_37_0:ReplaceTbName(var_37_0)
	end

	return (HXSet.hxLan(var_37_0))
end

function var_0_0.GetPainting(arg_38_0)
	local var_38_0, var_38_1 = arg_38_0:GetPaintingAndName()

	return var_38_1
end

function var_0_0.ExistPainting(arg_39_0)
	return arg_39_0:GetPainting() ~= nil
end

function var_0_0.ShouldShakeDailogue(arg_40_0)
	return arg_40_0.dialogShake ~= nil
end

function var_0_0.GetShakeDailogueData(arg_41_0)
	return arg_41_0.dialogShake
end

function var_0_0.IsSameSide(arg_42_0, arg_42_1)
	local var_42_0 = arg_42_0:GetPrevSide(arg_42_1)
	local var_42_1 = arg_42_0:GetSide()

	return var_42_0 ~= nil and var_42_1 ~= nil and var_42_0 == var_42_1
end

function var_0_0.GetPrevSide(arg_43_0, arg_43_1)
	local var_43_0 = arg_43_1:GetSide()

	if arg_43_0.moveSideData then
		var_43_0 = arg_43_0.moveSideData.side
	end

	return var_43_0
end

function var_0_0.GetPaintingIcon(arg_44_0)
	local var_44_0

	if arg_44_0.actor == var_0_0.ACTOR_TYPE_FLAGSHIP then
		local var_44_1 = getProxy(PlayerProxy):getRawData().character

		var_44_0 = getProxy(BayProxy):getShipById(var_44_1):getPrefab()
	else
		var_44_0 = (arg_44_0.actor ~= var_0_0.ACTOR_TYPE_PLAYER or nil) and (arg_44_0.actor ~= var_0_0.ACTOR_TYPE_TB or nil) and (arg_44_0.actor or nil) and (not arg_44_0.hideRecordIco or nil) and var_0_1[arg_44_0.actor].prefab
	end

	if var_44_0 == nil and arg_44_0:ExistPortrait() then
		var_44_0 = arg_44_0:GetPortrait()
	end

	return var_44_0
end

function var_0_0.GetPaintingAndName(arg_45_0)
	local var_45_0
	local var_45_1

	if not UnGamePlayState and arg_45_0.actor == var_0_0.ACTOR_TYPE_FLAGSHIP then
		local var_45_2 = getProxy(PlayerProxy):getRawData().character
		local var_45_3 = getProxy(BayProxy):getShipById(var_45_2)

		var_45_0 = var_45_3:getName()
		var_45_1 = var_45_3:getPainting()
	elseif not UnGamePlayState and arg_45_0.actor == var_0_0.ACTOR_TYPE_PLAYER then
		if getProxy(PlayerProxy) then
			var_45_0 = getProxy(PlayerProxy):getRawData().name
		else
			var_45_0 = ""
		end
	elseif not UnGamePlayState and arg_45_0.actor == var_0_0.ACTOR_TYPE_TB then
		if pg.NewStoryMgr.GetInstance():IsReView() then
			assert(arg_45_0.defaultTb and arg_45_0.defaultTb > 0, "<<< defaultTb is nil >>>")

			local var_45_4 = pg.secretary_special_ship[arg_45_0.defaultTb]

			var_45_0 = var_45_4.name or ""
			var_45_1 = var_45_4.prefab
		elseif arg_45_0.specialTbId then
			local var_45_5 = pg.secretary_special_ship[arg_45_0.specialTbId]

			assert(var_45_5)

			var_45_0 = var_45_5.name or ""
			var_45_1 = var_45_5.prefab
		elseif EducateProxy and getProxy(EducateProxy) then
			var_45_1, var_45_0 = getProxy(EducateProxy):GetStoryInfo()
		else
			var_45_0 = ""
		end
	elseif not arg_45_0.actor or var_0_1[arg_45_0.actor] == nil then
		var_45_0, var_45_1 = nil
	else
		local var_45_6 = var_0_1[arg_45_0.actor]
		local var_45_7 = var_45_6.ship_group
		local var_45_8 = ShipGroup.getDefaultShipConfig(var_45_7)

		if not var_45_8 then
			var_45_0 = var_45_6.name
		else
			var_45_0 = Ship.getShipName(var_45_8.id)
		end

		var_45_1 = var_45_6.painting
	end

	return HXSet.hxLan(var_45_0), var_45_1
end

function var_0_0.GetShipSkinId(arg_46_0)
	if arg_46_0.actor == var_0_0.ACTOR_TYPE_FLAGSHIP then
		local var_46_0 = getProxy(PlayerProxy):getRawData().character

		return getProxy(BayProxy):getShipById(var_46_0).skinId
	elseif arg_46_0.actor == var_0_0.ACTOR_TYPE_PLAYER then
		return nil
	elseif not arg_46_0.actor then
		return nil
	else
		return arg_46_0.actor
	end
end

function var_0_0.IsShowNPainting(arg_47_0)
	return arg_47_0.showNPainting
end

function var_0_0.IsShowWJZPainting(arg_48_0)
	return arg_48_0.showWJZPainting
end

function var_0_0.ShouldGrayPainting(arg_49_0)
	return arg_49_0.paingtingGray
end

function var_0_0.ShouldAddGlitchArtEffect(arg_50_0)
	return arg_50_0.glitchArt
end

function var_0_0.HideOtherPainting(arg_51_0)
	return arg_51_0.hideOtherPainting
end

function var_0_0.GetSubPaintings(arg_52_0)
	return _.map(arg_52_0.subPaintings or {}, function(arg_53_0)
		local var_53_0 = pg.ship_skin_template[arg_53_0.actor]

		assert(var_53_0)

		return {
			actor = arg_53_0.actor,
			name = var_53_0.painting,
			expression = arg_53_0.expression,
			pos = arg_53_0.pos,
			dir = arg_53_0.dir or 1,
			paintingNoise = arg_53_0.paintingNoise or false,
			showNPainting = arg_53_0.hidePaintObj or false
		}
	end)
end

function var_0_0.NeedDispppearSubPainting(arg_54_0)
	return #arg_54_0.disappearSeq > 0
end

function var_0_0.GetDisappearSeq(arg_55_0)
	return arg_55_0.disappearSeq
end

function var_0_0.GetDisappearTime(arg_56_0)
	return arg_56_0.disappearTime[1], arg_56_0.disappearTime[2]
end

function var_0_0.IsNoHeadPainting(arg_57_0)
	return arg_57_0.nohead
end

function var_0_0.GetFontSize(arg_58_0)
	return arg_58_0.fontSize
end

function var_0_0.IsSpinePainting(arg_59_0)
	local var_59_0 = arg_59_0:GetPainting()

	return tobool(var_59_0 ~= nil and arg_59_0.spine)
end

function var_0_0.IsHideSpineBg(arg_60_0)
	return arg_60_0.spine == 1
end

function var_0_0.GetSpineOrderIndex(arg_61_0)
	if arg_61_0:IsSpinePainting() then
		return arg_61_0.spineOrderIndex
	else
		return nil
	end
end

function var_0_0.IsLive2dPainting(arg_62_0)
	local var_62_0 = arg_62_0:GetPainting()

	return tobool(var_62_0 ~= nil and arg_62_0.live2d)
end

function var_0_0.GetLive2dPos(arg_63_0)
	if arg_63_0.live2dOffset then
		return Vector3(arg_63_0.live2dOffset[1], arg_63_0.live2dOffset[2], arg_63_0.live2dOffset[3])
	end
end

function var_0_0.GetVirtualShip(arg_64_0)
	local var_64_0 = arg_64_0:GetShipSkinId()
	local var_64_1 = pg.ship_skin_template[var_64_0].ship_group

	return StoryShip.New({
		skin_id = var_64_0
	})
end

function var_0_0.GetLive2dAction(arg_65_0)
	if type(arg_65_0.live2d) == "string" then
		local var_65_0 = pg.character_voice[arg_65_0.live2d]

		if var_65_0 then
			return var_65_0.l2d_action
		end

		return arg_65_0.live2d
	else
		return nil
	end
end

function var_0_0.GetL2dIdleIndex(arg_66_0)
	return arg_66_0.live2dIdleIndex
end

function var_0_0.GetSubActorName(arg_67_0)
	if arg_67_0.subActorName and arg_67_0.subActorName ~= "" then
		local var_67_0 = HXSet.hxLan(arg_67_0.subActorName)

		return " " .. setColorStr(var_67_0, arg_67_0.subActorNameColor)
	else
		return ""
	end
end

function var_0_0.IsSamePainting(arg_68_0, arg_68_1)
	local function var_68_0()
		return arg_68_1:ShouldAddGlitchArtEffect() or arg_68_0:ShouldAddGlitchArtEffect()
	end

	return (function()
		return arg_68_0:GetPainting() == arg_68_1:GetPainting() and arg_68_0:IsShowNPainting() == arg_68_1:IsShowNPainting() and arg_68_0:IsShowWJZPainting() == arg_68_1:IsShowWJZPainting()
	end)() and arg_68_0:IsLive2dPainting() == arg_68_1:IsLive2dPainting() and arg_68_0:IsSpinePainting() == arg_68_1:IsSpinePainting() and not var_68_0()
end

function var_0_0.ExistCanMarkNode(arg_71_0)
	return arg_71_0.canMarkNode ~= nil and type(arg_71_0.canMarkNode) == "table" and arg_71_0.canMarkNode[1] and arg_71_0.canMarkNode[1] ~= "" and arg_71_0.canMarkNode[2] and type(arg_71_0.canMarkNode[2]) == "table"
end

function var_0_0.GetCanMarkNodeData(arg_72_0)
	local var_72_0 = {}

	for iter_72_0, iter_72_1 in ipairs(arg_72_0.canMarkNode[2] or {}) do
		table.insert(var_72_0, iter_72_1 .. "")
	end

	return {
		name = arg_72_0.canMarkNode[1],
		marks = var_72_0
	}
end

function var_0_0.OnClear(arg_73_0)
	return
end

function var_0_0.GetUsingPaintingNames(arg_74_0)
	local var_74_0 = {}
	local var_74_1 = arg_74_0:GetPainting()

	if var_74_1 ~= nil then
		table.insert(var_74_0, var_74_1)
	end

	local var_74_2 = arg_74_0:GetSubPaintings()

	for iter_74_0, iter_74_1 in ipairs(var_74_2) do
		local var_74_3 = iter_74_1.name

		table.insert(var_74_0, var_74_3)
	end

	return var_74_0
end

return var_0_0
