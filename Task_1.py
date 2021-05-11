user_time = int(input("Enter duration: "))
d = user_time // 86400
h = user_time // 60 // 60 % 24
m = user_time // 60 % 60
s = user_time % 60
print (d, "days", h, "hours", m, "minutes", s, "seconds")
