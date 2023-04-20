#creating parent class with method
class Character:
    name = "Evelyn"
    species = "Human"
    charClass = "Archer"
    weapon = "Bow"
    level = "15"

    def charSheet(self):
        msg = "\n I am {}, the {} .\n With my trusty {}, I will surpass level {},\n and complete fetch quests across the land!".format(self.name, self.charClass, self.weapon, self.level)
        return msg

        
#child class
class NPC(Character):
    name = "Mary"
    charClass = "Barmaid"
    weapon = "conversation"
    level = "1"

#passing in self info into wildcards
    def charSheet(self):
        msg = "\nI am {} the {} {}. My weapon is {} , and I am  level {}".format(self.name, self.charClass, self.species, self.weapon, self.level)
        return msg

    
#child class
class Companion(Character):
    name = "Gwendolyn"
    charClass = "Barbarian"
    weapon = "Axe"
    questLine = "Mountain Wars"
    level = "10"

    def charSheet(self):
        msg = "\nI am {}, the {}. With my mighty {}, I assist {} on their quests.\n I am available in the {} quest line".format(self.name, self.charClass, self.weapon, character.name, self.questLine)
        return msg

#polymorphism on a function
def on_a_quest(fodderQuest):
    fodderQuest.charSheet()
    


if __name__ =="__main__":
    character = Character()
    npc = NPC()
    companion = Companion()
    print(character.charSheet())
    print(npc.charSheet())

    print(companion.charSheet())

    for self in (character, npc, companion):
        print(self.charSheet())
#calling the poly function
    on_a_quest(companion)

    
    

