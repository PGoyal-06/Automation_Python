import cv2
import time
import dropbox
import random

starttime = time.time()

def takeSnapshot():
    number = random.randint(0,100)
    capture_object = cv2.VideoCapture(0)
   
    result = True
    while(result):
        ret,frame = capture_object.read()
        imageName = "img" + str(number) + ".png"
        cv2.imwrite(imageName,frame)
        starttime = time.time
        result = False
    return imageName
    color_change = cv2.cvtColor(imageName,cv2.COLOR_BGR2HSV)
    print("imageTaken")
    capture_object.release()
    cv2.destroyAllWindows()

def uploadFiles(imageName):
    accessToken = "sl.BMkbnWAQ8cgaFSKKW3VNMFnUlQzN6UG3eTG6onfd-dj0PpJNQ4oUwh0XkBd-zK7iM7cHO0xdmOvhw1kLi_Q5er1Qst4FCPklFXMT_8kaGmgIOsVpG8gKqONMUdnIOOLq0Hs1hFKDgeVE"
    file = imageName
    file_from = file
    fileto = "/ColorChange/" + (imageName)
    db = dropbox.Dropbox(accessToken)
    with open(file_from,'rb') as f:
        db.files_upload(f.read(),fileto,mode = dropbox.files.WriteMode.overwrite)
        print("File has been uploaded")

def main():
    while(True):
        if((time.time()- starttime)>= 5):
            name = takeSnapshot()
            uploadFiles(name)
main()