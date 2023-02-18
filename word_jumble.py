from tkinter import *
from random import choice
from random import shuffle

root = Tk()
root.title('Word Jumble Game')
root.geometry("700x500")
root.configure(background='aqua')

my_label = Label(root, text="", font=("Arial", 48), bg='aqua')
my_label.pack(pady=20)

def shuffler():
    hint_label.config(text='')
    global hint_count
    hint_count = 0
    entry_answer.delete(0, END)
    answer_label.config(text='', bg='aqua')

    fruits = ['apple', 'banana', 'strawberry', 'watermelon', 'kiwi']
    global word
    word = choice(fruits)
    break_apart_word = list(word)
    shuffle(break_apart_word)
    global shuffled_word
    shuffled_word = ''
    for letter in break_apart_word:
        shuffled_word += letter
    my_label.config(text=shuffled_word)

def answer():
    if word == entry_answer.get():
        answer_label.config(text="Correct answer!", bg='aqua', fg='green')
    else:
        answer_label.config(text="Wrong answer, please try again.", bg='aqua', fg='red')

global hint_count
hint_count = 0

def hint(count):
    global hint_count
    hint_count = count
    word_length = len(word)
    if count < word_length:
        hint_label.config(text=f'{hint_label["text"]} {word[count]}', bg='aqua')
        hint_count += 1


entry_answer = Entry(root, font=("Arial", 24))
entry_answer.pack(pady=20)
button_frame = Frame(root, bg='aqua')
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Answer", command=answer, bg='orange', width=8, font=10)
answer_button.grid(row=0, column=0, padx=10)
my_button = Button(button_frame, text="Pick Another Word", command=shuffler, bg='orange', width=15, font=10)
my_button.grid(row=0, column=1, padx=10)
hint_button = Button(button_frame, text="Hint", command=lambda: hint(hint_count), bg='orange', width=5, font=10)
hint_button.grid(row=0, column=2, padx=10)

answer_label = Label(root, text='', font=("Arial", 22))
answer_label.pack(pady=20)
hint_label = Label(root, text='', font=("Arial", 22), bg='aqua')
hint_label.pack(pady=10)

shuffler()
root.mainloop()
