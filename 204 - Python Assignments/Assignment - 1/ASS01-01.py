Principal = int(input("Enter Principal : "))
Rate = int(input("Enter Rate of Interest : "))
year = int(input("Enter Numbers of Year : "))
print("Principal Amount : RS. ", Principal)
print("Rate of Interset : ", Rate, "%")
print("Numbers of Years : ", year)
Simple_Interest = (Principal * Rate * year) /100
print("Simple Interest : RS. ", Simple_Interest)
print("Maturity Amount : RS. ", (Principal + Simple_Interest))