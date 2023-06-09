from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


BUTTON_HEALTHCHECK_TEXT: str = "PING"
button_healthcheck = KeyboardButton(text=BUTTON_HEALTHCHECK_TEXT)

BUTTON_START_HEALTHCHECK_PROCESS_TEXT: str = "START_POLLING"
button_start_healthcheck_process = KeyboardButton(text=BUTTON_START_HEALTHCHECK_PROCESS_TEXT)

kb = [
    [
        button_start_healthcheck_process,
        button_healthcheck,
    ],
]

# add buttons to keyboard
keyboard_base = ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие",
)
