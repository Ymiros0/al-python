﻿local var_0_0 = class("BeatMonsterNianConst")

var_0_0.INPUT_TIME = 3
var_0_0.ACTION_NAME_L = "L"
var_0_0.ACTION_NAME_R = "R"
var_0_0.ACTION_NAME_A = "A"
var_0_0.ACTION_NAME_B = "B"
var_0_0.MotionCombinations = {
	BLB = "isAttack7",
	BRA = "isAttack6",
	ARA = "isAttack6",
	BBB = "isAttack1",
	ABB = "isAttack4",
	RBA = "isAttack8",
	LRB = "isAttack6",
	LBA = "isAttack8",
	RAB = "isAttack4",
	AAA = "isAttack1",
	LLA = "isAttack1",
	ALB = "isAttack7",
	RLA = "isAttack2",
	LLB = "isAttack5",
	LAB = "isAttack4",
	BRB = "isAttack8",
	ARB = "isAttack8",
	RRA = "isAttack1",
	BBA = "isAttack2",
	LRA = "isAttack2",
	BAB = "isAttack3",
	LBB = "isAttack7",
	ABA = "isAttack3",
	AAB = "isAttack2",
	LAA = "isAttack3",
	ALA = "isAttack5",
	RAA = "isAttack3",
	RLB = "isAttack6",
	BLA = "isAttack5",
	RBB = "isAttack7",
	BAA = "isAttack4",
	RRB = "isAttack5"
}

function var_0_0.MatchAction(arg_1_0)
	return var_0_0.MotionCombinations[arg_1_0] ~= nil
end

function var_0_0.GetMatchAction(arg_2_0)
	return var_0_0.MotionCombinations[arg_2_0]
end

function var_0_0.GetMonsterAction(arg_3_0)
	return "isAttack"
end

return var_0_0
