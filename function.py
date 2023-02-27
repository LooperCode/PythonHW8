import json
file = "/home/loopercode/PythonCourse/HW8/phones.json"
countID = "/home/loopercode/PythonCourse/HW8/countID.txt"
#Загрузка файла со словарем
def LoadData():
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)

# Вызов HELP листа
def PrintHelp():
    helpList = ''' Функции справочника: 
1 - открыть справочник
2 - добавить контакт
3 - поиск по фамилии/имени
4 - поиск по номеру телефона
5 - изменить контакт
0 - выход
'''
    print(helpList)


    #Сохранение словаря
def Save(phones):
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(phones, ensure_ascii=False))


def addContact(phones): 
    with open (countID, "r", encoding="utf-8") as cd:     #txt файл, куда записывается и откуда берется текущий ID
        count_id = int(cd.read())
        count_id += 1
    with open (countID, "w", encoding="utf-8") as cd:
        cd.write(str(count_id))
        cd.close()
    fstName = input("Введите имя: ")
    scndName = input("Введите фамилию: ")
    numName = input("Введите номер: ")
    tmpList = {}
    tmpList[count_id] = {f'Фамилия': scndName, 'Имя': fstName, 'Телефон': numName}
    print(tmpList)
    phones.append(tmpList)
    return Save(phones) 
    
    
# Поиск по номеру
def SearchNum(phones, insertFind):
    
    #проходим по приходящему словарю из def Search
    for value in phones.values():
        if value.get("Телефон") == insertFind:
            return True
    return False


#Поиск по имени/фамилии
def Search(phones, choice):
    strTmp = "Введите "
    if choice == 3:
        strTmp += "фамилию/имя: "
    elif choice == 4:
        strTmp += "номер: "  
    text = input(strTmp)    
             
    #циклы по списку-словарей
    res = []
    for i in phones:
        for value in i.values(): 
            if choice == 3:
                if value.get("Фамилия") == text:
                    res.append(i)
                elif value.get("Имя") == text:
                    res.append(i)        
    # Вызов функции поиска по номеру
       
            elif choice == 4:
                    isExist = SearchNum(i, text)
                    if (isExist): 
                        res.append(i)
    print(res)  
              
    #Изменение номера по ключу ID
def Edit (phones):
    get_id = input("Введите ID контакта: ")
    get_num = input("Введите новый номер телефона: ")
    for i in phones:
        for id, numb in i.items():
            if id == get_id:
                numb["Телефон"] = get_num
    return Save(phones) 

def PrintBook (phones):
    strPrint = '''    ID  Фамилия             Имя                 Телефон''' 
    print(strPrint)
    for i in phones:
        for id, value in i.items():
            print("\n%5s" %(id), end = "\t")
            for key in value.values():
                print("{0:<20}".format(key), end="")
                
def Delete (phones):
    get_id = input("Введите ID контакта: ")
    for i in phones:
        
        i.pop(get_id, None)
        
    return Save(phones)