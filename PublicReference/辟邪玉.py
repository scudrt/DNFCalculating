##辟邪玉属性部分

class 辟邪玉():
    名称 = ''
    编号 = 0
    最小值 = -5
    最大值 = 5
    间隔 = 0.2
    当前值 = 0
    def 进图属性(self, 属性):
        pass

class 辟邪玉0(辟邪玉):
    名称 = '无'
    编号 = 0
    最小值 = 0
    最大值 = 0

class 辟邪玉1(辟邪玉):
    名称 = '附加伤害增加增幅'
    编号 = 1
    def 进图属性(self, 属性):
        if 属性.附加伤害 >= 2:
            属性.附加伤害 += self.当前值 / 50
        else:
            属性.附加伤害 *= 1 + self.当前值 / 100

class 辟邪玉2(辟邪玉):
    名称 = '属性附加伤害增加增幅'
    编号 = 2
    def 进图属性(self, 属性):
        if 属性.属性附加 >= 2:
            属性.属性附加 += self.当前值 / 50
        else:
            属性.属性附加 *= 1 + self.当前值 / 100

class 辟邪玉3(辟邪玉):
    名称 = '光属性附加伤害增加增幅(未生效)'
    编号 = 3

class 辟邪玉4(辟邪玉):
    名称 = '火属性附加伤害增加增幅(未生效)'
    编号 = 4

class 辟邪玉5(辟邪玉):
    名称 = '冰属性附加伤害增加增幅(未生效)'
    编号 = 5

class 辟邪玉6(辟邪玉):
    名称 = '技能伤害增加增幅(待测试)'
    编号 = 6
    def 进图属性(self, 属性):
        属性.技能攻击力 *= 1 + self.当前值 / 100   #待测试

class 辟邪玉7(辟邪玉):
    名称 = '暴击伤害增加增幅'
    编号 = 7
    def 进图属性(self, 属性):
        if 属性.暴击伤害 >= 2:
            属性.暴击伤害 += self.当前值 / 50
        else:
            属性.暴击伤害 *= 1 + self.当前值 / 100

class 辟邪玉8(辟邪玉):
    名称 = '伤害增加增幅'
    编号 = 8
    def 进图属性(self, 属性):
        if 属性.伤害增加 >= 2:
            属性.伤害增加 += self.当前值 / 50
        else:
            属性.伤害增加 *= 1 + self.当前值 / 100

class 辟邪玉9(辟邪玉):
    名称 = '最终伤害增加增幅'
    编号 = 9
    def 进图属性(self, 属性):
        if 属性.最终伤害 >= 2:
            属性.最终伤害 += self.当前值 / 50
        else:
            属性.最终伤害 *= 1 + self.当前值 / 100

class 辟邪玉10(辟邪玉):
    名称 = '力量智力增加增幅'
    编号 = 10
    def 进图属性(self, 属性):
        if 属性.百分比力智 >= 2:
            属性.百分比力智 += self.当前值 / 50
        else:
            属性.百分比力智 *= 1 + self.当前值 / 100

class 辟邪玉11(辟邪玉):
    名称 = '物理魔法攻击力增加增幅'
    编号 = 11
    def 进图属性(self, 属性):
        if 属性.百分比三攻 >= 2:
            属性.百分比三攻 += self.当前值 / 50
        else:
            属性.百分比三攻 *= 1 + self.当前值 / 100

class 辟邪玉12(辟邪玉):
    名称 = '所有属性强化增加'
    编号 = 12
    最大值 = 20
    最小值 = -20
    间隔 = 1
    def 进图属性(self, 属性):
        属性.所有属性强化(self.当前值)

class 辟邪玉13(辟邪玉):
    名称 = 'BUFF物理、魔法攻击力增加'
    编号 = 13

class 辟邪玉14(辟邪玉):
    名称 = 'BUFF物理、魔法攻击力增加量增加'
    编号 = 14

class 辟邪玉15(辟邪玉):
    名称 = 'BUFF力量、智力增加'
    编号 = 15

class 辟邪玉16(辟邪玉):
    名称 = 'BUFF力量、智力增加量增加'
    编号 = 16

class 辟邪玉17(辟邪玉):
    名称 = '一觉力量、智力增加'
    编号 = 17

class 辟邪玉18(辟邪玉):
    名称 = '一觉力量、智力增加量增加'
    编号 = 18

class 辟邪玉19(辟邪玉):
    名称 = 'HP最大增加增幅'
    编号 = 19

class 辟邪玉20(辟邪玉):
    名称 = 'MP最大增加增幅'
    编号 = 20

class 辟邪玉21(辟邪玉):
    名称 = '物理防御力增加增幅'
    编号 = 21

class 辟邪玉22(辟邪玉):
    名称 = '魔法防御力增加增幅'
    编号 = 22

class 辟邪玉23(辟邪玉):
    名称 = '物理暴击率增加'
    编号 = 23

class 辟邪玉24(辟邪玉):
    名称 = '魔法暴击率增加'
    编号 = 24

class 辟邪玉25(辟邪玉):
    名称 = '暗属性抗性增加'
    编号 = 25

class 辟邪玉26(辟邪玉):
    名称 = '光属性抗性增加'
    编号 = 26

class 辟邪玉27(辟邪玉):
    名称 = '火属性抗性增加'
    编号 = 27

class 辟邪玉28(辟邪玉):
    名称 = '冰属性抗性增加'
    编号 = 28

class 辟邪玉29(辟邪玉):
    名称 = '攻击、移动、施放速度增加'
    编号 = 29

class 辟邪玉30(辟邪玉):
    名称 = '回避率增加'
    编号 = 30

class 辟邪玉31(辟邪玉):
    名称 = '命中率增加'
    编号 = 31

class 辟邪玉32(辟邪玉):
    名称 = '跳跃力增加'
    编号 = 32

class 辟邪玉33(辟邪玉):
    名称 = 'HP恢复量增加'
    编号 = 33

class 辟邪玉34(辟邪玉):
    名称 = 'MP恢复量增加'
    编号 = 34

class 辟邪玉35(辟邪玉):
    名称 = '暗属性赋予'
    编号 = 35
    最小值 = 0
    最大值 = 0

class 辟邪玉36(辟邪玉):
    名称 = '光属性赋予'
    编号 = 36
    最小值 = 0
    最大值 = 0

class 辟邪玉37(辟邪玉):
    名称 = '火属性赋予'
    编号 = 37
    最小值 = 0
    最大值 = 0

class 辟邪玉38(辟邪玉):
    名称 = '冰属性赋予'
    编号 = 38
    最小值 = 0
    最大值 = 0

class 辟邪玉39(辟邪玉):
    名称 = '10~15技能Lv增加'
    编号 = 39
    最小值 = 1
    间隔 = 1
    def 进图属性(self, 属性):
        属性.技能等级加成('所有', 10, 15, self.当前值)
        pass

class 辟邪玉40(辟邪玉):
    名称 = '20~25技能Lv增加'
    编号 = 40
    最小值 = 1
    间隔 = 1
    def 进图属性(self, 属性):
        属性.技能等级加成('所有', 20, 25, self.当前值)
        pass

class 辟邪玉41(辟邪玉):
    名称 = '30~35技能Lv增加'
    编号 = 41
    最小值 = 1
    间隔 = 1
    def 进图属性(self, 属性):
        属性.技能等级加成('所有', 30, 35, self.当前值)
        pass
 
class 辟邪玉42(辟邪玉):
    名称 = '40~45技能Lv增加'
    编号 = 42
    最小值 = 1
    间隔 = 1
    def 进图属性(self, 属性):
        属性.技能等级加成('所有', 40, 45, self.当前值)
        pass
 
class 辟邪玉43(辟邪玉):
    名称 = '55~60技能Lv增加'
    编号 = 43
    最小值 = 1
    间隔 = 1
    def 进图属性(self, 属性):
        属性.技能等级加成('所有', 55, 60, self.当前值)
        pass
 
class 辟邪玉44(辟邪玉):
    名称 = '65~70技能Lv增加'
    编号 = 44
    最小值 = 1
    间隔 = 1
    def 进图属性(self, 属性):
        属性.技能等级加成('所有', 65, 70, self.当前值)
        pass
 
class 辟邪玉45(辟邪玉):
    名称 = '75~80技能Lv增加'
    编号 = 45
    最小值 = 1
    间隔 = 1
    def 进图属性(self, 属性):
        属性.技能等级加成('所有', 75, 80, self.当前值)
        pass
 
class 辟邪玉46(辟邪玉):
    名称 = '1次觉醒技能Lv增加'
    编号 = 46
    最小值 = 1
    间隔 = 1
    def 进图属性(self, 属性):
        属性.技能等级加成('所有', 50, 50, self.当前值)
        pass
 
class 辟邪玉47(辟邪玉):
    名称 = '2次觉醒技能Lv增加'
    编号 = 47
    最小值 = 1
    间隔 = 1
    def 进图属性(self, 属性):
        属性.技能等级加成('所有', 85, 85, self.当前值)
        pass
 
class 辟邪玉48(辟邪玉):
    名称 = '3次觉醒技能Lv增加'
    编号 = 48
    最小值 = 1
    间隔 = 1
    def 进图属性(self, 属性):
        属性.技能等级加成('所有', 100, 100, self.当前值)
        pass
 
class 辟邪玉49(辟邪玉):
    名称 = '物品栏负重增加'
    编号 = 49


辟邪玉列表 = []
i = 0
while i >= 0:
    try:
        exec('辟邪玉列表.append(辟邪玉'+str(i)+'())')
        i += 1
    except:
        i = -1

辟邪玉序号 = dict()
for i in range(len(辟邪玉列表)):
    辟邪玉序号[辟邪玉列表[i].名称] = i
