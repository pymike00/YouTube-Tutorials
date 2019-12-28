import face_recognition

known_image = face_recognition.load_image_file("volto_noto.jpg")
unknown_image = face_recognition.load_image_file("other.jpg")

known_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

face_distance = face_recognition.face_distance([known_encoding], unknown_encoding)
match = True if face_distance[0] <= 0.6 else False

print("Range Distanza: [0.0 - 1.0]")
print(f"I volti analizzati hanno una distanza di {face_distance[0]:.2} dall'immagine conosciuta")
print(f"Match: { match }")
