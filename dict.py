dict={
    "car":"Swift" ,
    "Model": "2020",
    "Price": { 2000, ("20 % flat available")  }
}

print(dict)
print(dict["car"])
dict["BRand"]="suzuki"
print(dict) 
print(dict.get('Model'))

disct1={"car":"ford"}
print(dict.update(disct1))
print(dict)


del dict['car']
print(dict)



