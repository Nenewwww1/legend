

print(''' ______                                                                 _        _                                    
(______)                                                               | |      | |                                   
 _     _  _   _  ____    ____  _____   ___   ____     _____  ____    __| |    __| |  ____  _____   ____   ___   ____  
| |   | || | | ||  _ \  / _  || ___ | / _ \ |  _ \   (____ ||  _ \  / _  |   / _  | / ___)(____ | / _  | / _ \ |  _ \ 
| |__/ / | |_| || | | |( (_| || ____|| |_| || | | |  / ___ || | | |( (_| |  ( (_| || |    / ___ |( (_| || |_| || | | |
|_____/  |____/ |_| |_| \___ ||_____) \___/ |_| |_|  \_____||_| |_| \____|   \____||_|    \_____| \___ | \___/ |_| |_|
                       (_____|                                                                   (_____|              
''')

print('Welcome to Dungeon Dragon')
player_name=print('What is your name,Adventurer?:')

health = 100
damage = 20

print('Welcome'+player_name+'your health is '+str(health)+'and can do damage'+str(damage))
print('you came across a dragon and what will you do?')
print('1.Fight')
print('2. Run') 
 
choice = int(input('Enter either 1 or 2: ')) 
if choice == 1: 
    print("Dragon run away ....") 
print("Dragon chase you!")
