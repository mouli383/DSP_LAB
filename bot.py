from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus

CORPUS_FILE = "/content/chat.txt"

chatbot = ChatBot("Chatpot", read_only=True)

trainer = ListTrainer(chatbot)
trainer.train(clean_corpus(CORPUS_FILE))

exit_conditions = (":q", "quit", "exit")

print("Bot ready. Type 'exit' to quit.")

while True:
    query = input("> ")
    if query.lower() in exit_conditions:
        break
    print("🪴", chatbot.get_response(query))
