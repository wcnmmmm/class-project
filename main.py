class Health:
     def _init_(self,max_hp):
          self.max_hp=max_hp
          self.current_hp=max_hp
     def take_damage(self,amount):
          previous_hp=self.curremt_hp
          self.current_hp=max(self.current_hp-amount,0)
          print("get {amount} damage, current hp:{self.current_hp}/{self.max_hp}")
          if previous_hp>self.current_hp:
               self.on_damage_taken(amount)
 
player=Health(100)
player.take_damage(20)
player.take_damage(50)
player.take_damage(50)



