
a = {
    "2010": [2],
    "2009": [4,7],
    "1989": [8]
}




d = dict()  
years = []  


#(get 2 column list of years and values)

for line in a:    
    year = line[0]   
    value = line[1]  

for line in a:  
    if year in d.keys():  
        d[value].append(value)  
    else:  
        d[value] = value  
        d[year] = year  