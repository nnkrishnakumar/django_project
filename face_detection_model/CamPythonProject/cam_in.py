# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# import the opencv library
import cv2
from requests import Response

face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def detect_bounding_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces

def post_to_host(host, port, filename):
    import requests
    url = f'http://{host}:{port}/uploadfile'
    files = {'file': open(filename, 'rb')}
    response:Response = requests.post(url, files=files)
    print(f"body={response.json()}")

def call_cam(cam_name):
    # define a video capture object
    vid = cv2.VideoCapture(0)

    while (True):

        # Capture the video frame
        # by frame
        ret, frame = vid.read()
        frame2= frame.copy()

        faces = detect_bounding_box(
            frame
        )  # apply the function we created to the video frame

        if len(faces) == 1:
            #print(f"faces = {faces}")
            filepath = "/tmp/frame.png"
            cv2.imwrite(filepath, frame2)
            post_to_host("localhost",8000, filepath)


        # Display the resulting frameq
        cv2.imshow('frame', frame)

        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    call_cam('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
