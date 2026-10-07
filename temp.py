temp=float(input("Enter temprature:"))
if temp>=35:
    dicision="It is very hot.Stay indores & drink water..."
    
elif temp>=25:
     dicision="Weather is pleasant..."
     
elif temp>=15:
     dicision="It is cool.Carry a jacket..."
     
else:
     dicision="It is cold.Wear Warm Clothes..."
     
print("AI Dicision:",dicision)