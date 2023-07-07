import cv2
import datetime

# 画像の読み込み
img = cv2.imread("Binarization_YZ\yozo_facebook.jpg", 0)

# 閾値の設定
threshold = 100

resize_height = 500
width = img.shape[1]
height = img.shape[0]
magnification = resize_height/height
img = cv2.resize(img, dsize=None, fx=magnification , fy=magnification)


while True:
    # 二値化(閾値100を超えた画素を255にする。)
    ret, img_thresh = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    
    cv2.destroyAllWindows()
    cv2.imshow("img_th", img_thresh)
    key = cv2.waitKeyEx()
    print(key)
    if key == 2490368: #上矢印
        threshold += 1
        print("ue " + str(key))
        print("threshold:",threshold)
    if key == 2621440: #下矢印
        threshold -= 1
        print("sita " + str(key))
        print("threshold:",threshold)

    if key == 13: #enter
        date = datetime.datetime.now(
            datetime.timezone(datetime.timedelta(hours=9))
        )
        path = "Binarization_YZ/" + date.strftime('%Y%m%d_%H%M%S') + ".jpg"
        print(path)
        cv2.imwrite(path , img_thresh, [cv2.IMWRITE_JPEG_QUALITY, 100])
        print("Saved!!", "threshold =", threshold)
        
    
    if key == 27: #esc
        print("")
        print("threshold =", threshold)
        print("")
        cv2.destroyAllWindows()
        break
    



cv2.destroyAllWindows()


