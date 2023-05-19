import pyautogui
import win32gui

coords = {
    "16:9": {
        "light_cone": {
            "stats": (0.11, 0.72, 0.25, 0.755),
            "quantity": (0.89, 0.46, 0.13, 0.06),
            "stats_attr": {
                "_name": (0, 0, 1, 0.08),
                "_level": (0.13, 0.3, 0.35, 0.35),
                "_superimposition": (0.1, 0.48, 0.7, 0.55)
            }
        }
    }
}


class Screenshot:

    def __init__(self, hwnd, aspect_ratio="16:9"):
        self._aspect_ratio = aspect_ratio

        self._width, self._height = win32gui.GetClientRect(hwnd)[2:]
        self._left, self._top = win32gui.ClientToScreen(hwnd, (0, 0))

    def screenshot_light_cone_stats(self):
        lc_coords = coords[self._aspect_ratio]["light_cone"]

        img = self._take_screenshot(*lc_coords["stats"])

        lc_stats_coords = {
            k: tuple([int(v * img.width) if i % 2 == 0 else int(v * img.height) for i, v in enumerate(v)]) for k, v in lc_coords["stats_attr"].items()}

        name = img.crop(lc_stats_coords["_name"])
        level = img.crop(lc_stats_coords["_level"])
        superimposition = img.crop(lc_stats_coords["_superimposition"])

        return name, level, superimposition

    def screenshot_light_cone_quantity(self):
        return self._take_screenshot(
            *coords[self._aspect_ratio]["light_cone"]["quantity"])

    def _take_screenshot(self, top, left, width, height):
        x = self._left + int(self._width * left)
        y = self._top + int(self._height * top)
        width = int(self._width * width)
        height = int(self._height * height)

        screenshot = pyautogui.screenshot(region=(x, y, width, height))
        return screenshot