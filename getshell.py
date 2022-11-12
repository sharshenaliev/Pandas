from lalafo import mylists
import re
from datetime import datetime
from rumonths import rumonths 

def fillshell():
 
    for i in range(0, 10):
        user_url = mylists[i][2]
        if len(mylists[i][6])>0:
           user_name = mylists[i][6]
        else:
            user_name = user_url
        if len(mylists[i][5][5])>0:
            images = mylists[i][5][5]
        else:
            images = "None"
        if len(mylists[i][0][0])>0:
            date = mylists[i][0][0]
            date = re.findall(r"\d.*\d", date)
            date = ''.join(date)

            for k, v in rumonths.items():
                date = date.replace(k, str(v))
    
            date = datetime.strptime(date, '%d %m %Y')
        else:
            date = "2021-01-22 00:00:00"
    
        title = mylists[i][5][0]
        url = mylists[i][5][1]
        currency = mylists[i][5][2]
        price = mylists[i][5][3]
        content = mylists[i][5][4]

        t = []
        for item in mylists[i][3]:
            t += item
				
        text = ''.join(t)

        category = re.findall(r"arenda", text)
        if len(category)>0:
            category = ''.join(category)
            category = re.findall(r"posutochn", category)
            if len(category)>0:
                category = 2
            else:
                category = 1
        else:
            categories = ["snimu", "kuplu", "prodazha"]    
            for a in range(0,2):
                category = re.findall(categories[a], text)
                if len(category) >0:
                    category = a + 3
                    break
                else:
                    category = 5
        
        with open("estates.txt", 'r') as f:
            estates = f.read().splitlines()
        
        for a in range(0, len(estates)):
            estate = re.findall(estates[a], text)
            if len(estate) >0:
                estate = a + 1
                break

        with open("towns.txt", 'r') as f:
            towns = f.read().splitlines()

        for a in range(0, len(towns)):
            town = re.findall(towns[a], text)
            if len(town) >0:
                town = a + 1
                break

        phonenums = mylists[i][4]    
        
        
        square = re.findall(r"Площадь\s[(]м[.]\sкв[.][)][:]\d+", text)
        square = ''.join(square)
        square = re.split(r"[:]", square)
        square2 = re.findall(r"Площадь участка [(]соток[)][:]\d+", text)
        square2 = ''.join(square2)
        square2 = re.split(r"[:]", square2)
        rooms = re.findall(r"\d[-]bedrooms", text)
        rooms = ''.join(rooms)
        rooms = re.sub(r"[-]bedrooms", "", rooms)
        if len(rooms)==0:
            rooms = 0

        rooms_key = re.findall(r"Количество комнат[:].*?\d[-]bedrooms", text)
        if len(rooms_key)>0:
            rooms_key = ''.join(rooms_key)
            rooms_key = re.split(r"[:]", rooms_key)
        else:
            rooms_key = ["Количество комнат", "отсутствует"]

        parameter_name = [rooms_key[0]]
        parameter_value = [rooms]
        parameter_key = [rooms_key[1]]

        if len(square)>1:
            parameter_name.append(square[0])
            parameter_value.append(square[1])
            parameter_key.append("отсутствует")

        if len(square2)>1:
            parameter_name.append(square2[0])
            parameter_value.append(square2[1])
            parameter_key.append("отсутствует")

            
        district = re.findall(r"Район[:].*Был|Район[:].*Онлайн", text)
        district = ''.join(district)
        district = re.findall(r'[А-я].*?[^\s][/]|[А-я].*?[^\s][А-Я]', district)
        district = ''.join(district)
        district = district[0:-1]
        district = re.split(r"Район[:]/", district)
        district = ''.join(district)
        districts = re.split(r"/", district)
    
        district_key = re.findall(r"Район[:].*Был|Район[:].*Онлайн", text)
        district_key = ''.join(district_key)
        district_key = re.findall(r"[/].*?[А-Я]", district_key)
        district_keys = []
        for a in district_key:
            district_keys.append(a[0:-1])

        if districts[0] =='':
            districts = ['Район не указан']
            district_keys = ['отсутствует']

        print(parameter_name, parameter_value, parameter_key, sep="\n")
            
            
            
            
      
 
