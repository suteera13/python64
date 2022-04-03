import face_recognition
image = face_recognition.load_image_file("test1.jpg")
face_location = face_recognition.face_locations(image)
print(face_location)
print(f"Number of Face:{len(face_location)}")