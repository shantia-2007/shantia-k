
import random
mn=random.randrange (1,100)
c=0
max = 100
min = 0
print("کامپيوتر عددي بين صفر و صد انتخاب مي کند")
print("شما بايد با حداکثر هفت حدس آن عدد را بيابيد")
print("---------------------------------")
while(c<8):
    print(f"حدس {c+1}:")
    n=  int(input("حدس خود را وارد کنيد = "))
    if (n< mn ):
        min = n
        print("اشتباه--حدس شما کوچک است ")
        print(f"{min} < Number < {max}")
        print("------------------------------")
    elif (n > mn):
        max = n
        print("اشتباه---حدس شما بزرگ است")
        print(f"{min} < Number < {max}")
        print("------------------------------")
    else :
        print("تبريک..شما درست حدس زديد")
        break
    c= c+1
if (c == 8):
    print ("شما بازي رو باختيد")     
        
