phone_book = {
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla"
}

number = input("Enter a phone number: ")

if len(number) != 10 or not number.isascii() or not number.isdigit():
    print("This is invalid number")
else:
    print(phone_book.get(number, "Sorry, the number is not found"))