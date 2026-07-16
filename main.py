import cv2

# Open the default camera
cam = cv2.VideoCapture(0)

# Get the default frame width and height

#REMOVE COMMENTS LATER WHEN THIS IS WORKING

# Define the codec and create VideoWriter object
#fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

while True:
    ret, frame = cam.read()

    # Write the frame to the output file
    #out.write(frame)
    x1 = 140
    y1 = 140
    x2 = 440
    y2 = 440
    width = (x2 - x1)//3
    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
    cv2.line(frame, (x1 + width, y1), (x1 + width, y2), (255, 0, 255), 4)
    cv2.line(frame, (x1 + 2*width, y1), (x1 + 2*width, y2), (255, 0, 255), 4)
    cv2.line(frame, (x1, y1 + width), (x2, y1 + width), (255, 0, 255), 4)
    cv2.line(frame, (x1, y1 + 2*width), (x2, y1 + 2*width), (255, 0, 255), 4)
    # Display the captured frame
    cv2.imshow('Rubliks Cube Solver', frame)



    if cv2.waitKey(1) == ord('s'): 
            cv2.imwrite(filename='rubicks_face.jpg', img=frame)
            break

img = cv2.imread('rubicks_face.jpg')
h, w, _ = img.shape          
center = img[h//2, w//2]     
print(center) 

b = center[0] / 255 * 100 // 1
g = center[1] / 255 * 100 // 1
r = center[2] / 255 * 100 // 1

print(f"Red: {r}, Green: {g}, Blue: {b}")


if r > g and r > b and  g < 40 and  b < 25:
    print("The color is Orange")
elif r > g and r > b and  g <= 40 and  b < 40:
    print("The color is Red")
elif r > b and  g > b and abs(r - g) < 10:
    print("The color is Yellow")
elif g > r and g > b:
    print("The color is Green")
elif b > r and b > g:
    print("The color is Blue")
elif abs(r - g) < 10 and abs(r - b) < 10 and abs(g - b)  < 10:
    print("The color is White")

# Release the capture and writer objects
cam.release()
#out.release()
cv2.destroyAllWindows()