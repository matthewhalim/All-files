o = (input("Please input a Richter scale value:")) #we ask the user to input the Richter scale
print("Richter scale value: ", o)  #we first print the scale value
T = 4.184 * (10**9) #One ton of exploded TNT yields this value of joules
s = 2930200 #one nutritious lunch contains this value of joules
e = 10**((1.5 * float(o))+4.8)#formula to find the energy in joules
l = e/s # convertion of joules to nutritious lunch
y = e / T # convertion of joules to ton
print("Equivalence in Joules: ", e)
print("Equivalence in tons of TNT:", y)
print("Equivalence in the number of nutritious lunches:", l)
