matrix=[]
developersList=[]
managersList=[]

def compute():
    


def main():
    global developersList,managersList
    dimesion,developers,managers=0,0,0
    f=open("a_solar.txt","r")
    f1=f.readlines()
    for line in range(0,len(f1)):
        if line ==0:
            dimesion=list(map(int, f1[line].split()))[1]
        elif dimesion>0:
            matrix.append(list(map(str, f1[line].split())))
            dimesion=dimesion-1
        elif dimesion==0:
            developers=list(map(int, f1[line].split()))[0]
            dimesion=-1
        elif developers>0:
            developersList.append(list(map(str, f1[line].split())))
            developers=developers-1
        elif developers==0:
            managers=list(map(int, f1[line].split()))[0]
            developers=-1
        elif managers>0:
            managersList.append(list(map(str, f1[line].split())))
            managers=managers-1
            
        
    compute()
            


if __name__=="__main__":
    main()