import time
import random
import tkinter

class Player:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.lvl = 1
        self.exp = 0
    def level(self):
        self.lvl += 1
        self.exp = 0
        self.hp += 5*self.lvl
        self.damage += 3*self.lvl
        print(f"you level up: {self.lvl}")
    @staticmethod
    def create_weapon():
        weapon_list = ["sword", "bow"]
        weapon_rare = {
            1: "common",
            1.75: "rare",
            2: "legendary",
            2.5: "mystical",
        }
        random_weapon = random.choice(weapon_list)
        random_rare = random.choice(list(weapon_rare.keys()))
        if weapon_list[0] == random_weapon:
            player.damage += 7 * random_rare
        elif weapon_list[1] == random_weapon:
            player.damage += 4 * random_rare
        return random_weapon, weapon_rare[random_rare]

    def create_heals(self):
        heals = {
            10: "little health",
            20: "normal health",
            30: "lots of health"
        }
        random_heals = random.choice(list(heals.keys()))
        player.hp += random_heals
        return heals[random_heals]



    def attack(self, victim):
        victim.hp -= self.damage
        print(f"Your damage: {self.damage}")
        if victim.hp <= 0:
            random_exp = 15*self.lvl
            print(f"{victim.name} defeated, you got {random_exp} exp")
            item = random.randint(0,2)
            if item == 0:
                print("you didn't get anything")
                time.sleep(1)
            elif item == 1:
                weapon = self.create_weapon()
                time.sleep(1)
                print(f'you got a weapon! \n'
                      f'{weapon[0]} {weapon[1]} \n'
                      f'your damage: {self.damage}')
                time.sleep(1)
            elif item == 2:
                heal = self.create_heals()
                time.sleep(1)
                print(f'you got a heal! \n'
                      f'{heal}  \n'
                      f'your hp: {self.hp}')
                time.sleep(1)
            self.exp += random_exp
            max_exp = 35*self.lvl
            if self.exp >= max_exp:
                self.level()
                max_exp = 35 * self.lvl
                print(f"up to new level {max_exp} exp")
                time.sleep(1)
            return False
        else:
            print(f"{victim.name} his health: {victim.hp}")
            time.sleep(1)
            return True

    @staticmethod
    def create_player(player_name, player_race, player_class):
        hp = 0
        damage = 0
        if player_race == races_list[0]:
            hp += 10
            damage += 5
        elif player_race == races_list[1]:
            hp += 20
            damage += 25
        elif player_race == races_list[2]:
            hp += 30
            damage += 100
        elif player_race == races_list[3]:
            hp += 15
            damage += 30
        else:
            print("Error race")
            quit()
        if player_class == class_list[0]:
            hp += 10
            damage += 15
        elif player_class == class_list[1]:
            hp += 15
            damage += 10
        else:
            print("Error class")
            quit()
        return Player(player_name, hp, damage)
class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    @staticmethod
    def create_enemy():
        enemy_names=["vamp", "goblin"]
        cla_list = ["magician", "swordsman"]
        enemy_hp = random.randint(10,40)
        enemy_damage = random.randint(12,37)
        enemy_name = random.choice(enemy_names)
        enemy_class = random.choice(cla_list)
        if enemy_class == cla_list[0]:
            enemy_hp += 5
            enemy_damage +=10
        elif enemy_class == cla_list[1]:
            enemy_hp += 10
            enemy_damage +=5
        return Enemy(enemy_name, enemy_hp, enemy_damage)

    def attack(self, victim):
        victim.hp -= self.damage
        print(f"{self.name}. damage: {self.damage}")
        time.sleep(1)
        if victim.hp>0:
            print(f"Your health: {victim.hp}")
            time.sleep(1)
        else:
            print("Game over")
            quit()








print("Hello, what's your name?")
name = input()
races_list=["human", "hobbit", "elf", "dwarf" ]
class_list=["archer", "knight"]
print("Choose a race")
for race in races_list:
    print(race , end=" ")
print()
race = input().lower()
print("Choose a class")
for clas in class_list:
    print(clas , end=" ")
print()
clas = input().lower()
player = Player.create_player(name, race, clas)
print(f"Your player is created:\n"
      f"Your name -> {player.name}\n"
      f"Your hp -> {player.hp}\n"
      f"Your damage -> {player.damage}")

def fight():
    print("fight or escape?(1 or 2)")
    answer = int(input())
    if answer == 1:
        result_attack = player.attack(enemy)
        if result_attack == True:
            enemy.attack(player)
            fight()
    elif answer == 2:
        plan = random.randint(0,1)
        if plan == 0:
            print("You escape")
            time.sleep(1)
        elif plan == 1:
            print(f"You grabbed {enemy.name}")
            fight()




while True:
    event = random.randint(0,1)
    if event == 0:
        print("You don't meet anyone")
        time.sleep(1)
    elif event == 1:
        enemy = Enemy.create_enemy()
        print(f"You noticed {enemy.name}\n"
              f"enemy hp -> {enemy.hp}\n"
              f"enemy damage -> {enemy.damage}")
        fight()
        time.sleep(1)
