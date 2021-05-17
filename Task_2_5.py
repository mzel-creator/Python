price = [57.08, 46.51, 97, 15.45, 77.01, 99.99, 105.09, 34.90, 9.11, 17.77]
#-----A-----
for i in price:
    r, kk = str(f"{i:.2f}").split(".")
    print(f"{r} руб. {int(kk):02d} коп.,", end=" ")

print(id(price))

#-----B-----
price.sort()
print(price)
print(id(price))

#-----C-----
price.sort(reverse=True)
print(price)

#-----D-----
the_most_expensive = price[:5]
print(the_most_expensive)



