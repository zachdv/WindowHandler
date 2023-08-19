import PySimpleGUI as sg
import re
from windowclass import WindowHandler



if __name__ == "__main__":

    handler = WindowHandler()

    # Create initial window
    x = 1
    layout = handler.create_layout(x)
    handler.create_window(f'Window {x}', layout)

    while True:
        # Check events for each window
        for title, window in list(handler.windows.items()):  # Use list to allow modification of dictionary during iteration
            event, values = window.read(timeout=5)
            if event != '__TIMEOUT__':
                print(f"Window: {title}, Event: {event}, Values: {values}")

            if event == sg.WINDOW_CLOSED or event == "Exit":
                handler.close_window(title)
            elif event == 'Update Status Text':
                target_title = f'Window {values["list"]}'
                handler.update_specific_status_texts(window_title=target_title, updatetext=values['Input'], element='-STATUS-')
            elif event.startswith('up') or event.startswith('down'):
                # Extract the number from the event name
                num = int(re.findall(r'\d+', event)[0])
                if num > 0:
                    if event.startswith('up'):
                        num += 1
                    else:
                        num -= 1
                    layout = handler.create_layout(num)
                    handler.create_window(f'Window {num}', layout)

        # Exit the loop if no windows remain
        if not handler.windows:
            break
