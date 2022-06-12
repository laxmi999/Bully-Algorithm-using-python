leader = 1
numberProcess = int(input("Enter the number of processes : "))
numberProcessList = list()
for i in range(1,numberProcess+1):
    numberProcessList.append(i)
statuslist = list()
for i in range(numberProcess):
    n = int(input(f"Enter the status of the process {numberProcessList[i]} - active/inactive(1/0) : "))
    statuslist.append(n)
    if(statuslist[i]):
        leader = i+1

def display(leader):
    print("\n")
    print("\n")
    print("Processes : \n")
    for i in numberProcessList:
        print(f'{i}',end="\t")
    print('\n')
    print("Alive  : \n")
    for i in statuslist:
        print(f'{i}',end="\t")
    print("\n")
    print(f"The leader is : {leader}\n")

def bully(leader):
    print("Enter")
    print("1.Crash\n2.Activate\n3.Display\n4.Exit\n")
    bully = int(input())
    if bully == 1:
        crashID = int(input(f"Enter a process to crash : (1 to {numberProcessList[-1]}) : "))
        if(statuslist[crashID-1]):
            statuslist[crashID-1] = 0
            print(f"Process {crashID} is crashed.\n")
        elif(statuslist[crashID-1] ==0):
            print(f"Process {crashID} is already dead.\n")
        elecGenerator = int(input("Enter the process to generate the election leader : "))
        while(leader == elecGenerator):
            print("Enter a valid leader.")
            elecGenerator = int(input("Enter the process to generate the election leader : "))
        print('\n')
        if(leader == crashID):
            for i in range(elecGenerator+1,len(statuslist)):
                print(f"Message is sent from {elecGenerator} to {numberProcessList[i-1]}")
                if(statuslist[i-1]):
                    print(f"Response is sent from {numberProcessList[i-1]} to {elecGenerator}")
                    leader = numberProcessList[i-1]
            print('\n')
            print(f"The new leader is : {leader}\n")
        display(leader)
    elif bully==2:
        activateID = int(input(f"Enter a process to activate : (1 to {numberProcessList[-1]}) : "))
        if(statuslist[activateID-1]==0):
            statuslist[activateID-1]=1
            leader = activateID
        elif(statuslist[activateID-1]):
            print("The process is already alive. ")
        for i in range(activateID+1,len(statuslist)):
            print(f"Message is sent from {activateID} to {numberProcessList[i-1]}")
            if(statuslist[numberProcessList[i-1]]):
                print(f"Response is sent from {numberProcessList[i-1]} to {activateID}")
                leader = numberProcessList[i-1]
        print('\n')
        print(f'The new leader is : {leader}\n')
        display(leader)
    elif bully ==3:
        display(leader)
    elif bully ==4:
        exit()

print("Enter : ")
print("1.Bully Algorithm\n2.Display\n3.Exit\n")
decision = int(input())
while(decision!=1 or decision!=2 or decision!=3):
    if decision ==1:
        bully(leader)
    elif decision == 2:
        display(leader)
    elif decision ==3:
        exit()
    else:
        print("Enter correct input : ")
        print("1.Bully Algorithm\n2.Display\n3.Exit\n")
        decision = int(input())

