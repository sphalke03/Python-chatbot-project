import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("path/to/firebase_credentials.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection("chats").document("example")
doc_ref.set({"user_message": "Hello", "bot_response": "Hi there!"})

print("Data stored in Firebase!")
