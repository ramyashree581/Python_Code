l = [{'state':'karnataka','city':'bangalore'},{'state':'kerala','city':'cochin'},{'state':'TN', 'city':'chennai'}]
inp = 'TN/M'
def get_city(inp):
     for item in l:
             if item['state'] == inp:
                     print "city is ",item['city']
                     break
     else:
             print "no city found"


get_city(inp)