contacts = {
    "David": ["123-321-88", "david@test.com"],
    "James": ["241-879-093", "james@test.com"],
    "Bob": ["987-004-322", "bob@test.com"],
    "Amy": ["340-999-213", "a@test.com"]
}

search_name = input()

if search_name not in contacts:
    print("Not found")
else:
    print(contacts[search_name][1])