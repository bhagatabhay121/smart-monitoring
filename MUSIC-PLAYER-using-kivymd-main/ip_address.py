from firebase import firebase
firebase = firebase.FirebaseApplication("https://abhay-121-default-rtdb.firebaseio.com/", None)

res = firebase.get("abhay-121-default-rtdb/Users/Threat", "")
try:
    for i in res.keys():
        print(res[i]["ip_address"])

        ak = res[i]["ip_address"]

    bk = input("Do you want to remove :")
    if bk == "y":
        ak = firebase.delete("abhay-121-default-rtdb/Users/Threat","")
    else:
        pass


except:
    print("There is not an ip address")