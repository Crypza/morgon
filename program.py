#start

#vakna upp

vaken = "n"

while vaken == "n":
    print("Du sover som en stock. Zzz")
    vaken = input("Vaknar du? [y/n]").lower()

#duscha
print("Du masar dig upp och släpar in dig i duschen")
print("Någon har lömnat en brödrost i din dusch")
duscha = input("Flyttar du på brödrosten? [y/n]").lower()
if duscha == "n":
    exit("Du elchokas till döds.")
elif duscha == "y":
    print("Du blir ren")
else:
    print ("ERROR")

#årstid
season = False
while season == False:

    season = input("Vilken årstid är det? [vinter, vår, sommar, höst]").lower()

    if season == "vår" or season == "vinter" or season == "höst":

        print("Det är kallt som fan")
        print("Du tar på dig en vinterjacka")

    elif season == "sommar":

        print("Du svettas satan")
        print("Du tar på dig en t-shirt och shorts")
    
    else:

        season = False

