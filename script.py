import random
import time
import cv2 as cv
import numpy as np
import pyautogui
import win32api
import win32con


def load_image(image_path):
    img = cv.imread(image_path, cv.IMREAD_UNCHANGED)
    if img is None:
        raise FileNotFoundError(f"Image at path '{image_path}' not found.")
    return img


def find_template(main_img, template_img):
    result = cv.matchTemplate(main_img, template_img, cv.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv.minMaxLoc(result)
    return max_loc, max_val


def find_multiple_templates(main_img, template_img, max_instances=6, threshold=0.8):
    instances = []
    img_gray = cv.cvtColor(main_img, cv.COLOR_BGR2GRAY)
    template_gray = cv.cvtColor(template_img, cv.COLOR_BGR2GRAY)
    w, h = template_img.shape[1], template_img.shape[0]

    for _ in range(max_instances):
        res = cv.matchTemplate(img_gray, template_gray, cv.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv.minMaxLoc(res)

        if max_val < threshold:
            break

        instances.append((max_loc, max_val))
        # Mask out the found location
        cv.rectangle(img_gray, max_loc, (max_loc[0] + w, max_loc[1] + h), 0, -1)

    return instances


def display_result(main_img, template_img, location, window_name='Result'):
    top_left = location
    bottom_right = (top_left[0] + template_img.shape[1], top_left[1] + template_img.shape[0])
    cv.rectangle(main_img, top_left, bottom_right, (0, 0, 255), 2)
    cv.imshow(window_name, main_img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def display_results(main_img, template_img, locations, window_name='Result'):
    for loc, _ in locations:
        top_left = loc
        bottom_right = (top_left[0] + template_img.shape[1], top_left[1] + template_img.shape[0])
        cv.rectangle(main_img, top_left, bottom_right, (0, 0, 255), 2)
    cv.imshow(window_name, main_img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def kbPress(key):
    pyautogui.keyDown(key)
    time.sleep(random.uniform(1, 3))
    pyautogui.keyUp(key)


def main():
    try:
        village_img = load_image('main village.png')
        start_button_img = load_image('start button.png')
        start_img = load_image('start.png')
        find_button_img = load_image('find button.png')
        first_village_img = load_image('first village.png')
        macchina_img = load_image('macchina da guerra.png')
        superpekka_img = load_image('superpekka.png')
    except FileNotFoundError as e:
        print(e)
        return

    start_loc, start_conf = find_template(village_img, start_button_img)
    print("Start button found")
    print(f'Best match top left position: {start_loc}')
    print(f'Best match confidence: {start_conf}')

    find_loc, find_conf = find_template(start_img, find_button_img)
    print("Find button found")
    print(f'Best match top left position: {find_loc}')
    print(f'Best match confidence: {find_conf}')

    macc_loc, macc_conf = find_template(first_village_img, macchina_img)
    print("Macchina da guerra found")
    print(f'Best match top left position: {macc_loc}')
    print(f'Best match confidence: {macc_conf}')

    superpekka_locs = find_multiple_templates(first_village_img, superpekka_img, max_instances=6)
    print("Superpekka found in multiple locations:")
    for i, (loc, conf) in enumerate(superpekka_locs):
        print(f'Location {i + 1}: {loc}, Confidence: {conf}')

    display_result(village_img, start_button_img, start_loc, 'Start Button')
    display_result(start_img, find_button_img, find_loc, 'Find Button')
    display_result(first_village_img, macchina_img, macc_loc, 'Macchina da guerra')
    display_results(first_village_img, superpekka_img, superpekka_locs, 'Superpekka')


if __name__ == "__main__":
    main()
