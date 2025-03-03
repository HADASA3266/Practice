#דוגמא לתוכנית ראשונה בפייתון
#פלט
#print("enter your name")
#קלט
name=input("enter your name\n")
#בכל פעם שקולטים מהמשתמש - באופן אוטומטי נקלט מחרוזת
#ולכן הגיל בכלל לא נקלט כמספר אלא כמחרוזת
age=int(input("enter your age\n"))

print("welcome to "+name)
#וכאן קיבלנו שגיאה כי ניסנו לחבר את המספר 2 למחרוזת.........
print("in 2 years you will be "+str(age+2))