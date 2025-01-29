import base64
import json
from io import BytesIO
from PIL import Image
from firebase import firebase
firebase = firebase.FirebaseApplication("https://abhay-121-default-rtdb.firebaseio.com/", None)

# Convert Image to JSON

#with open("2.jpg", "rb") as image_file:
 #   image_bytes = image_file.read()
#image_base64 = base64.b64encode(image_bytes).decode('utf-8')
#image_json = json.dumps(image_base64)
#data = {
 #   "image": image_json
#}

res = firebase.get("abhay-121-default-rtdb/Users/photo", "")
for i in res.keys():
    ak = res[i]["image"]

    image_data = json.loads(ak)
    image_bytes = base64.b64decode(image_data)
    image = Image.open(BytesIO(image_bytes))
    image.save("output.jpg")


