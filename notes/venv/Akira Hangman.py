import random
word_bank = ["Devil", "Elixir", "Angel", "Office", "Dust", "Monday", "School", "Pawn", "King", "Queen",
             "Turtle's"]
random_word = random.choices(word_bank)
guessed_words = []
Hearts = 8
while Hearts <= 0:
    hidden_word = []
word_bank.append = []