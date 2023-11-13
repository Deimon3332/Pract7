import PySimpleGUI as sg
import game_logic

def create_layout():
    # Створення макету інтерфейса
    return [
        [sg.Text("Виберіть рівень складності:")],
        [sg.Radio('Легкий (1-10)', "RADIO1", default=True, key='-EASY-'),
         sg.Radio('Середній (1-50)', "RADIO1", key='-MEDIUM-'),
         sg.Radio('Складний (1-100)', "RADIO1", key='-HARD-')],
        [sg.Text(f"Введіть число: ")],
        [sg.InputText(key='-INPUT-')],
        [sg.Button('ОК?'), sg.Button('Вийти')]
    ]

def main():
    lower_limit, upper_limit = game_logic.get_limits()
    secret_number, attempts = game_logic.initialize_game(lower_limit, upper_limit)

    # Використані функції для створення макету
    layout = create_layout()

    window = sg.Window('Гра "Вгадай число"', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Вийти':
            break

        user_guess = values['-INPUT-']

        # Виявлення рівня складності
        difficulty_levels = {'-EASY-': 10, '-MEDIUM-': 50, '-HARD-': 100}
        for key, value in difficulty_levels.items():
            if values[key]:
                lower_limit, upper_limit = 1, value
                break

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
                    # Почати нову гру
                    secret_number, attempts = game_logic.initialize_game(lower_limit, upper_limit)
            except ValueError:
                sg.popup("-_- нормалье число напишіть.")

    window.close()

if __name__ == "__main__":
    main()
