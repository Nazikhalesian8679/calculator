import PySimpleGUI as sg


def create_window(theme):
    sg.theme(theme)
    sg.set_options(font="Calibre 20", button_element_size=(5, 2))
    button_size = (5, 2)
    layout = [
        [sg.Text("Out put", font="Franklin 26", justification="right", expand_x=True, pad=(10, 20),
                 right_click_menu=theme_menu, key="-TEXT-")],

        [sg.Button("clear", expand_x=True), sg.Button("Enter", expand_x=True)],
        [sg.Button("7", size=button_size), sg.Button("8", size=button_size), sg.Button("9", size=button_size),
         sg.Button("*", size=button_size)],
        [sg.Button("4", size=button_size), sg.Button("5", size=button_size), sg.Button("6", size=button_size),
         sg.Button("/", size=button_size)],
        [sg.Button("1", size=button_size), sg.Button("2", size=button_size), sg.Button("3", size=button_size),
         sg.Button("-", size=button_size)],
        [sg.Button("0", expand_x=True), sg.Button(".", size=button_size), sg.Button("+", size=button_size)]

    ]
    return sg.Window("Calculator", layout)


theme_menu = ["menu", ["dark", "black", "random"]]
window = create_window("BrownBlue")
curnnet_num = []
full_operation = []

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event in theme_menu[1]:
        window.close()
        window = create_window(event)
    if event in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
        curnnet_num.append(event)
        num_string = "".join(curnnet_num)
        window["-TEXT-"].update(num_string)
    if event in ["*", "/", "+", "-"]:
        full_operation.append("".join(curnnet_num))
        curnnet_num = []
        full_operation.append(event)
        window["-TEXT-"].update("")
    if event == "Enter":
        full_operation.append("".join(curnnet_num))
        result = eval(" ".join(full_operation))
        window["-TEXT-"].update(result)
        full_operation = []
    if event == "Clear":
        curnnet_num = []
        full_operation = []
        window["-TEXT-"].update("")
