from function import*
#Выбор функции
def Command (cmd):
    if cmd == 1:
        PrintBook(phones)
        
    elif cmd == 2:
        addContact(phones)
        
    elif cmd == 3 or cmd == 4:
        Search(phones, cmd)
    elif cmd == 5:
        Edit(phones)
    elif cmd == 6:
        Delete(phones)
    elif cmd == 0:
        exit()    
    else:
        print("Неизвестная команда")
    return True  

#Присваиваем словарь
phones = LoadData()


#Постоянный цикл для справочника          
PrintHelp()
while True:
    try:
        choice = int(input("Выберите функцию: "))
        if (not Command(choice)):
            break
    except ValueError:
        print("Неизвестная команда")    