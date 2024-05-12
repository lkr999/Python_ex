import cv2
import numpy as np

def count_panels(img):
    # 이미지를 그레이스케일로 변환합니다.
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Canny 알고리즘을 사용하여 윤곽선을 추출합니다.
    edges = cv2.Canny(gray_img, 50, 150)

    # 윤곽선 중에서 판넬 형태의 윤곽선을 찾습니다.
    panels = []
    for i in range(len(edges)):
        x, y, w, h = cv2.boundingRect(edges[i])
        if w > 50 and h > 50:
            panels.append((x, y, w, h))

    cv2.imshow(gray_img)

    # 찾은 판넬의 갯수를 반환합니다.
    return len(panels)


# 테스트 이미지를 로드합니다.
img = cv2.imread("asset/test_img.jpg")

# 판넬의 갯수를 세어줍니다.
count = count_panels(img)

# 결과를 출력합니다.
print("판넬의 갯수:", count)