import PySimpleGUI as sg


class WindowHandler:

    def __init__(self):
        self.windows = {}

    def create_layout(self, target):
        status_text = f"Number of windows: {len(self.windows) + 1}"
        layout = [
            [sg.Text(f"Window {target}")],
            [sg.Button(f"up {target}"), sg.Button(f"down {target}"), sg.Button("Exit")],
            [sg.Input(key='Input'), sg.Button(f"Update Status Text"), sg.Combo([], key='list', size=(15, 1))],
            # Empty combo initially
            [sg.Text(status_text, key='-STATUS-')]
        ]
        return layout

    def update_all_status_texts(self):
        status_text = f"Number of windows: {len(self.windows)}"
        y = [str(x) for x in range(1, len(self.windows) + 1)]  # Convert to strings
        for window in self.windows.values():
            window['-STATUS-'].update(status_text)
            window['list'].update(values=y)

    def update_specific_status_texts(self, window_title, updatetext, element):
        window = self.windows.get(window_title)
        if window and window[element]:
            window[element].update(updatetext)
        elif not window:
            print("Window doesn't exist")
        elif not element:
            print("Element doesn't exist")

    def create_window(self, title, layout):
        if title in self.windows:
            print(f"Window with title '{title}' already exists!")
            return self.windows[title]

        window = sg.Window(title, layout, resizable=True, finalize=True)
        self.windows[title] = window
        self.update_all_status_texts()
        return window

    def close_window(self, title):
        if title in self.windows:
            self.windows[title].close()
            del self.windows[title]
            self.update_all_status_texts()

    def close_all_windows(self):
        for window in self.windows.values():
            window.close()
        self.windows.clear()
