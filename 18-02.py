def letter(name, date, email, place="Нефтекамск"):
    print(f"To:", email)
    print(f"Здравствуйте,", name)
    print(f"Были бы рады видеть вас на встрече начинающих программистов в {place}, которая пройдет {date}.")


letter("Larisa", "22.04.2022", "lara@yandex.ru")
