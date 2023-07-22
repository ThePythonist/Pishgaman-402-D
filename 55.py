info = {
    "name": "titanic",
    "rate": 7.8,
    "director": "james cameron",
    "release": 1997,
}

key = input("Search for key : ")

if key in info:
    print("Found :", info[key])
else:
    print("Key Not Found")
