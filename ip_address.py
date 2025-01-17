from firebase import firebase
firebase = firebase.FirebaseApplication("https://abhay-121-default-rtdb.firebaseio.com/", None)

res = firebase.get("abhay-121-default-rtdb/Users/Threat", "")

print(res)

bk = input("Do you want to remove :")
if bk == "y":
    ak = firebase.delete("abhay-121-default-rtdb/Users/Threat","")
else:
    pass
