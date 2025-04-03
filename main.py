class Health:
     def _init_(self,max_hp):
          self.max_hp=max_hp
          self.current_hp=max_hp
          self.max_hp=100
     def take_damage(self,amount):
          previous_hp=self.current_hp
          self.current_hP-=amount
          self.current_hp=max(self.current_hp-amount,0)
          print("get {amount} damage, current hp:{self.current_hp}/{self.max_hp}")
          if previous_hp>self.current_hp:
               self.on_damage_taken(amount)
     def heal_health(self,amount):
          previous_hp=self.current_hp         
          self.current_hp+=amount
          self.current_HP=max(self.current_hp+amount,0)
          print("heal {amount} health,current hp:{self.current_hp}/{self.max_hp}")
          if previous_hp<self.current_hp:
               self.on_heal_health(amount)


player=Health(100)
player.take_damage(20)
player.take_damage(50)

class Stamina:
     def _init_(self,max_stamina):
          self.max_stamina=max_stamina
          self.current_stamina=max_stamina
          self.max_stamina=100
          self.base_regen_rate=5
          self.current_regen_rate=self.base_regen_rate
          self.is_exhausted=False
     def consume(self,amount):
          if self.current_stamina<amount:
               print("you don't have enough stamina")
               return False
          self.current_stamina-=amount
          print("consume {amount} stamina,current stamina:{self.current_stamina}/{self.max_stamina}")
          if self.current_stamina==0:
               self.is_exhausted=True
               print("you are exhausted")
          return True   
     def heal_stamina(self,amount)  
     def activity(self,activity):
          if activity=="don't move":
              self.current_regen_rate=self.base_regen_rate*1.5
          if activity=="eat something":
              self.current_regen_rate=self.base_regen_rate*2.0
          else:self.current_regen_rate=self.base_regen_rate*0.5
          if self.current_stamina>10:
               self.is_exhausted=False
          return False