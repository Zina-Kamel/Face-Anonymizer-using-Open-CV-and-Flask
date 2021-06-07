from flask import Flask, render_template, request
import cv2

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/after', methods=['GET', 'POST'])
def after():
    img = request.files['file_input']

    img.save('static/file.jpg')

    image = cv2.imread('static/file.jpg')

    cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = cascade.detectMultiScale(image, 1.1, 3)

    for (x, y, w, h) in faces:
        #cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi = image[y:y+h, x:x+w]
        roi = cv2.GaussianBlur(roi, (23, 23), 30)
        image[y:y+roi.shape[0], x:x+roi.shape[1]] = roi

    cv2.imwrite('static/after.jpg', image)

    try:
        cv2.imwrite('static/after.jpg', image)

    except:
        pass

    return render_template('after.html')

if __name__ == "__main__":
    app.run(debug=True)