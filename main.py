ADDRESSBOOK = {}


def input_error(wrap):
    def inner(*args):
        try:
            return wrap(*args)
        except IndexError:
            return "Give me name and phone please"
        except KeyError:
            return "Contact not found"
        except ValueError:
            return "Invalid input. Please provide name and phone number separated by space."
    return inner


@input_error
def add_handler(data):  # Функції обробники команд
    name = data[0].title()
    phone = data[1]
    ADDRESSBOOK[name] = phone
    return f"Contact {name} with phone {phone} was saved"


@input_error
def change_handler(data):
    name = data[0].title()
    phone = data[1]
    if name not in ADDRESSBOOK:
        raise KeyError
    ADDRESSBOOK[name] = phone
    return f"Phone number for contact {name} was changed to {phone}"


@input_error
def phone_handler(data):
    name = data[0].title()
    if name not in ADDRESSBOOK:
        raise KeyError
    phone = ADDRESSBOOK[name]
    return f"The phone number for contact {name} is {phone}"


@input_error
def show_all_handler(*args):
    if not ADDRESSBOOK:
        return "The address book is empty"
    contacts = "\n".join([f"{name}: {phone}" for name, phone in ADDRESSBOOK.items()])
    return contacts


def exit_handler(*args):
    return "Good bye!"


def hello_handler(*args):
    return "How can I help you?"


def command_parser(raw_str: str):  # Парсер команд
    elements = raw_str.split()
    for func, cmd_list in COMMANDS.items():
        for cmd in cmd_list:
            if elements[0].lower() == cmd:
                return func, elements[1:]
    return None, None


COMMANDS = {
    add_handler: ["add", "додай", "+"],
    change_handler: ["change", "змінити"],
    phone_handler: ["phone", "телефон"],
    show_all_handler: ["show all", "показати все", "всі контакти"],
    exit_handler: ["good bye", "close", "exit"],
    hello_handler: ["hello"]
}


def main():   # цикл запит-відповідь
    while True:
        user_input = input(">>> ")
        if not user_input:
            continue
        func, data = command_parser(user_input)
        if not func:
            print("Unknown command. Type 'hello' for available commands.")
        else:
            result = func(data)
            print(result)
            if func == exit_handler:
                break


if __name__ == "__main__":
    main()
