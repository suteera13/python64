from PIL import Image
import face_recognition
image = face_recognition.load_image_file("test1.jpg")
face_locations = face_recognition.face_locations(image)
for f in face_locations:
    top, right, bottom, left = f
    face_img = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_img)
    pil_image.show()
print(face_location)
print(f"Number of Face:{len(face_location)}")