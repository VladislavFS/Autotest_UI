from pages.drag_a_drop_page import DragAndDropPage


def test_drag_a_drop_boxes(browser):
    dp = DragAndDropPage(browser)
    dp.open_drag_drop_page()
    dp.drag_and_drop(dp.drag_me(), dp.drop_here())
    assert dp.result_drop().text == 'Dropped!'


def test_drag_a_drop_image(browser):
    dp = DragAndDropPage(browser)
    dp.open_drag_drop_page()
    dp.image_tab_click()
    dp.drag_and_drop(dp.drag_image(), dp.drop_image())
    assert dp.result_drop_image().text == 'Dropped!'
