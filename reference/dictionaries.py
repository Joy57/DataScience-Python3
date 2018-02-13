# Like a map or hash table in other languages
company = {}
company["Employee"] = "John"
company["Employee A"] = "Rohit"
company["Manager"] = "Ed"
company["CTO"] = "Jane"

print(company["CTO"]) #prints Jane

print(company.get("Employee")) #prints John

print(company.get("NX-01")) #prints None

for employees in company:
    print(employees + ": " + company[employees])

#prints:

#CTO: Jane
#Employee A: Rohit
#Employee: John
#Manager: Ed