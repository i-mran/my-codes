import random
def lucky(names,number):
    selected=[]
    participants=names
    for i in range(0,number):
        guess=random.randrange(0,len(participants))
        selected.append(participants[guess])
        participants.remove(participants[guess])
    return selected
    
    
        
   
   
   
   
   
   
   
   
def main():
    participants=["Mani","Akhil","Babu","Sasi","Shibu"]
    print(lucky(participants,3))
     
     
     
     
     
     

main()
