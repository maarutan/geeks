while True:
    countryFlags = {
        'kyrgyzstan': {'red', 'yellow'},  
        'russia': {'white', 'blue', 'red'},  
        'usa': {'red', 'white', 'blue'},  
        'germany': {'black', 'red', 'yellow'},  
        'france': {'blue', 'white', 'red'},  
        'italy': {'green', 'white', 'red'},  
        'japan': {'white', 'red'},  
    }
    
    print("\nМеню:")
    print("1. Добавить страну и её цвета")
    print("2. Найти страну по цвету")
    print("3. Выход")
    print("------------------------------")
    
    userChoice = input("Введите номер команды: ").lower()
    
    if userChoice == '1':
        newCountry = input("Введите полное название страны (на английском): ").lower()
        colorsInput = input("Введите цвета флага через запятую: ").lower()

        colorSet = set()
        i = 0
        while i < len(colorsInput):
            while i < len(colorsInput) and colorsInput[i] == ' ':
                i += 1
            if i >= len(colorsInput):
                break
            color = ''
            while i < len(colorsInput) and colorsInput[i] not in ', ':
                color += colorsInput[i]
                i += 1
            colorSet.add(color)
            while i < len(colorsInput) and colorsInput[i] in ', ':
                i += 1
        
        countryFlags[newCountry] = colorSet
        print(f"\nСтрана '{newCountry}' добавлена с цветами: {', '.join(colorSet)}")
        print("---------------------------------")
    
    elif userChoice == '2':
        searchColorsInput = input("Введите цвет или несколько цветов через запятую: ").lower()

        colorQuery = set()
        i = 0
        while i < len(searchColorsInput):
            while i < len(searchColorsInput) and searchColorsInput[i] == ' ':
                i += 1
            if i >= len(searchColorsInput):
                break
            color = ''
            while i < len(searchColorsInput) and searchColorsInput[i] not in ', ':
                color += searchColorsInput[i]
                i += 1
            colorQuery.add(color)
            while i < len(searchColorsInput) and searchColorsInput[i] in ', ':
                i += 1
        
        if len(colorQuery) == 1:
            singleColor = next(iter(colorQuery))
            matchedCountries = [domain for domain, flagColors in countryFlags.items() if singleColor in flagColors]
            
            if matchedCountries:
                print(f"\nСтраны с цветом '{singleColor}': {', '.join(matchedCountries)}")
            else:
                print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print(f"Цвет '{singleColor}' не найден в флагах стран.")
                print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
        
        else:
            matchedCountries = [domain for domain, flagColors in countryFlags.items() if colorQuery.issubset(flagColors)]
            
            if matchedCountries:
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print(f"\nСтраны с цветами {', '.join(colorQuery)}: {', '.join(matchedCountries)}")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            else:
                print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print(f"Нет стран с цветами {', '.join(colorQuery)}.")
                print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    
    elif userChoice == '3':
        print("\nВыход из программы.")
        break
    
    else:
        print("\nНеверный выбор, пожалуйста, попробуйте снова.")
