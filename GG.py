class GG:
    def __init__(self, name):
        self.name = name
        self.hungry = 20
        self.health = 80
        self.courage = 50
        self.humor = 50
        self.age = 1
    def Changename(self, newname):
        self.name = newname
    def Changehungry(self, valueF):
        self.hungry += valueF
        if self.hungry > 100:
            self.hungry = 100
        elif self.hungry < 0:
            self.hungry = 0
    def Changehealth(self, valueS):
        self.health += valueS
        if self.health > 100:
            self.health = 100
        elif self.health < 0:
            self.health = 0
    def Changecourage(self, valueC):
        self.courage += valueC
        if self.courage > 100:
            self.courage = 100
        elif self.courage < 0:
            self.courage = 0
    def Changehumor(self):
        self.humor += valueH
        if self.humor > 100:
            self.humor = 100
        elif self.humor < 0:
            self.humor = 0
    def Changeage(self):
        self.age += 1
    def runname(self):
        return self.name
    def runhungry(self):
        return self.hungry
    def runhealth(self):
        return self.health
    def runage(self):
        return self.age
    def runhumor(self):
        return self.humor
    def runcourage(self):
        return self.courage

nameB = input('主人，初次見面，請問您要幫我取甚麼名字呢? ˳⚆ɞ⚆˳ ')
Chicken = GG(name = nameB)
while (Chicken.health > 0) and (Chicken.hungry < 100) and (Chicken.courage > 0 ) and (Chicken.humor > 0 ):
    Chicken.Changehungry(+2)
    Chicken.Changehealth(-2)
    Chicken.Changeage()
    Chicken.Changeage()
    command = input(f"""\n------------------------------------------\n 
    /""\      ,
   <>^  L____/|
    `) /`   , /
     \ `---' /
      `'";\)`
       _/_Y
     \n哈摟主人!我的名字是{Chicken.name}. 請問我們現在要幹嘛呢? \n
     1- 改名字\n
     2- 吃飯\n
     3- 睡覺(健康程度+10)\n
     4- 練練膽識 \n
     5- 運動\n
     6- 查看{Chicken.name}狀況\n
     每次輸入都會使我的飢餓程度增加、健康程度減少、並且歲數增加喔!\n
     請輸入選項1~6: """)
    print('\n')
    if command == '1':
        name2 = input('您想要把我改成甚麼名字呢 \n')
        Chicken.Changename(name2)
    elif command == '2':
        eat =(input("主人要我吃啥~ 1.吃蟲 2.吃鮭魚 3.吃垃圾"))
        if  eat =='1':
            Chicken.Changehungry(-10) and Chicken.Changehealth(+10)
            print("這是所謂正常的一餐嗎? 飢餓程度-10 健康程度+10!")
        elif eat =='2':
            Chicken.Changehungry(+10) and Chicken.Changehealth(-10)
            print("鮭魚不新鮮...拉拉... 飢餓程度+10 健康程度-10!")
        elif eat =='3':
            Chicken.Changehealth(-10) and Chicken.Changehumor(-10) and Chicken.Changecourage(-10)
            print("真的麥啊餒欸 不吃啦 健康程度-10! 心情狀態-10 膽識-10")
    elif command =='3':
        Chicken.Changehealth(+10)
        print("睡得好飽喔!謝謝主人! 健康程度+10!")
    elif command =='4':
        gut =(input("要練膽識喔 我怕我嚇鼠餒 好啦要練啥 1.逛屠宰場 2.拍照不開美雞 3.學狗叫"))
        if  gut == '1':
            Chicken.Changecourage(-10) and Chicken.Changehumor(-10)
            print("嚇爛了啦! 膽識-10! 心情程度-10")
        elif gut == '2':
            Chicken.Changecourage(+10) 
            print("這個ㄇㄞ雞雞是誰 我才不怕勒! 膽識+10")
        elif gut == '3':
            Chicken.Changecourage(+10) and Chicken.Changehungry(+10)
            print("狗追上來啦!跑喔!! 膽識+10! 飢餓程度+10")
    elif command == '5':
        sport =(input(print("我想當醉雞 不想當大肌雞...要動啥1.曬太陽 2.生蛋 3.玩老鷹抓小雞")))
        if  sport == '1':
            Chicken.Changehealth(+10) and Chicken.Changehumor(-10) and Chicken.Changehungry(+10)
            print("如果曬到皮膚都黑了我會不會變成烏骨雞 健康程度+10 心情狀態-10 飢餓程度+10")
        elif sport == '2':
            print("我是公的 不要指望我喔主人 ")
        elif sport == '3':
            Chicken.Changehealth(-10) and Chicken.Changehumor(+10)
            print("老鷹快來把這些東西抓走!!我不想當現成爸 健康程度-10 心情狀態+10")
    elif command == '6':
        print("年紀: ", Chicken.runage())
        print("心情狀態: ", Chicken.runhumor())
        print("飢餓程度: ", Chicken.runhungry())
        print("健康狀況: ", Chicken.runhealth())
        print("膽識狀況: ", Chicken.runcourage())

    else:
        print('請輸入數字1~6!')
else:
    print("""\n------------------------------------------\n
     /""\    ，
   <>X  L____/|
     \ `---' /
      `'";\)`
       _/_Y\n你害我死掉了!\n""")
    

