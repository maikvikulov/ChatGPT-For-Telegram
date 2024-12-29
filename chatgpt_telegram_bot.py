Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import openai
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Вставь сюда свой API-ключ OpenAI
openai.api_key = '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'

# Вставь сюда свой токен Telegram
TELEGRAM_API_TOKEN = '6477982536:AAHK5ICr8MpEypjADetLJzufjrGQbBHs8eE'

... # Функция для общения с ChatGPT
... def chatgpt_response(message: str) -> str:
...     try:
...         # Отправляем запрос к OpenAI API
...         response = openai.Completion.create(
...             engine="gpt-3.5-turbo",  # Или используйте другую модель, если требуется
...             prompt=message,
...             max_tokens=150,  # Ограничение на длину ответа
...             temperature=0.7  # Температура для разнообразия ответов
...         )
...         return response.choices[0].text.strip()
...     except Exception as e:
...         return f"Произошла ошибка: {e}"
... 
... # Функция для обработки сообщений
... def handle_message(update: Update, context: CallbackContext):
...     user_message = update.message.text  # Сообщение от пользователя
...     response = chatgpt_response(user_message)  # Получаем ответ от ChatGPT
...     update.message.reply_text(response)  # Отправляем ответ пользователю
... 
... # Основная функция для запуска бота
... def main():
...     # Создаем экземпляр Updater и передаем токен
...     updater = Updater(TELEGRAM_API_TOKEN, use_context=True)
...     
...     # Получаем диспетчера для регистрации обработчиков
...     dispatcher = updater.dispatcher
...     
...     # Обработчик для всех текстовых сообщений
...     dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
...     
...     # Запускаем бота
...     updater.start_polling()
...     updater.idle()
... 
... if __name__ == '__main__':
...     main()
