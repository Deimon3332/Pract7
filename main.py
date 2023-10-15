import PySimpleGUI as sg
import game_logic

def main():
    lower_limit, upper_limit = game_logic.get_limits()
    secret_number, attempts = game_logic.initialize_game(lower_limit, upper_limit)

    layout = [
        [sg.Text(f"Введіть число між {lower_limit} та {upper_limit}: ")],
        [sg.InputText(key='-INPUT-')],
        [sg.Button('ОК?'), sg.Button('Вийти')]
    ]

    window = sg.Window('Гра "Вгадай число"', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Вийти':
            break

        user_guess = values['-INPUT-']

        try:
            user_guess = int(user_guess)
            attempts += 1

            if user_guess < secret_number:
                sg.popup("Число більше.")
            elif user_guess > secret_number:
                sg.popup("Число менше.")
            else:
                sg.popup(f"Виграв {secret_number} за {attempts} спроб!")
                break
        except ValueError:
            sg.popup("-_- нормалье число напишіть.")

    window.close()

if __name__ == "__main__":
    main()
