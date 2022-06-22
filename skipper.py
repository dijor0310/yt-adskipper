#from operator import truediv
#import pyautogui

#THIS IS AD SKIPPER FOR YOUTUBE
import pyautogui
pyautogui.FAILSAFE = True


def findAndClick():
    while True:
        #print(pyautogui.locateCenterOnScreen("image.png", grayscale=True))
        image = pyautogui.locateCenterOnScreen("image.png")
        #image2 = pyautogui.locateCenterOnScreen("image2.png")
        #image3 = pyautogui.locateCenterOnScreen("image3.png")
        #image4 = pyautogui.locateCenterOnScreen("image4.png")
        if image is not None:  
            break
    
    if image is not None:
        print(image[0])
        pyautogui.click(image[0]+5, image[1]-60)

        while True:
            image2 = pyautogui.locateCenterOnScreen("image2.png")
            if image2 is not None:
                break
        pyautogui.click(image2)

        while True:
            image3 = pyautogui.locateCenterOnScreen("image3.png")
            if image3 is not None:
                break
        #image3 = pyautogui.locateCenterOnScreen("image3.png")
        pyautogui.click(image3)
        #while True:
            #image4 = pyautogui.locateCenterOnScreen("image4.png")
            #if image4 is not None:
                #break
        pyautogui.click(0,500)
    findAndClick()

if __name__ == "__main__":
    findAndClick()
