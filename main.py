import PySimpleGUI as sg
import game_logic

def main():
    lower_limit, upper_limit = game_logic.get_limits()
    secret_number, attempts = game_logic.initialize_game(lower_limit, upper_limit)

    layout = [
        [sg.Text("Виберіть рівень складності:")],
        [sg.Radio('Легкий (1-10)', "RADIO1", default=True, key='-EASY-'), sg.Radio('Середній (1-50)', "RADIO1", key='-MEDIUM-'), sg.Radio('Складний (1-100)', "RADIO1", key='-HARD-')],
        [sg.Text(f"Введіть число: ")],
        [sg.InputText(key='-INPUT-')],
        [sg.Button('ОК?'), sg.Button('Вийти')]
    ]

    window = sg.Window('Гра "Вгадай число"', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Вийти':
            break

        user_guess = values['-INPUT-']
        
        # Определение уровня сложности
        if values['-EASY-']:
            lower_limit, upper_limit = 1, 10
        elif values['-MEDIUM-']:
            lower_limit, upper_limit = 1, 50
        elif values['-HARD-']:
            lower_limit, upper_limit = 1, 100

        if event == 'ОК?':
            try:
                user_guess = int(user_guess)
                attempts += 1

                if user_guess < secret_number:
                    sg.popup("Число більше.")
                elif user_guess > secret_number:
                    sg.popup("Число менше.")
                else:
                    sg.popup(f"Виграв {secret_number} за {attempts} спроб!")
                    # Начать новую игру
                    secret_number, attempts = game_logic.initialize_game(lower_limit, upper_limit)
            except ValueError:
                sg.popup("-_- нормалье число напишіть.")

    window.close()

if __name__ == "__main__":
    main()
