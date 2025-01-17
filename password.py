from firebase import firebase
firebase = firebase.FirebaseApplication("https://abhay-121-default-rtdb.firebaseio.com/", None)
import socket

res = firebase.get("abhay-121-default-rtdb/Users/password", "")
for i in res.keys():
    print(res[i]["password"])
ak = firebase.delete("abhay-121-default-rtdb/Users/password","")



