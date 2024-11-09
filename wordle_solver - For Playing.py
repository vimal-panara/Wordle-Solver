# import json
from random import randint
import os


os.chdir(os.path.dirname(os.path.realpath(__file__)))


# Finalized function.
def load_words(all_word=1):
	word_list = []
	# with open("word_list_frequency.txt", "r") as file:
	# 	data = json.load(file)
	# 	data = sorted(data.items(), key=lambda x:x[1], reverse=True)
	# 	word_list = data[:][1]
	# return word_list
	if all_word:
		txt_file = "word_list.txt"
	else:
		txt_file = "possible_word_list.txt"

	with open(txt_file, "r", newline="\n") as file:
		for line in file:
			word_list.append(line.strip())
	return sorted(word_list)


# Finalized function.
def compare_with_ans(ans_word, guess_word, debug=False):
	# 1 = green, 2 = yellow, 3 = grey
	truth_seq = ""
	for i in range(5):
		if guess_word[i] in ans_word:
			if guess_word[i] == ans_word[i]:
				truth_seq += "1"
			else:
				truth_seq += "2"
		else:
			truth_seq += "3"
	if debug:
		print(truth_seq)
	return truth_seq


# Function to tell weather or not given word has repeated letters
def repeated_char(word):
	char_word_list = []
	flag = 0
	for char in word:
		if char not in char_word_list:
			char_word_list.append(char)
		else:
			flag = 1
			break
	return flag


# Change according to need.
def get_word(debug=False):
	# word = word_list[randint(0, len(word_list) - 1)]
	flag = 1
	word_pos = 0
	while flag:
		word = word_list[word_pos]
		if repeated_char(word) and word != word_list[-1]:
			word_pos += 1
		else:
			flag = 0
	if debug:
		print("Need to choose from {} words".format(len(word_list)))
		print("Guessed word is : {}".format(word))
	return word


# Finalized Function.
def filter_words(guess_res, guess_word, word_list):
	total_number_words = len(word_list)
	current_word_number = 0

	while current_word_number < total_number_words:
		word = word_list[current_word_number]

		for index in range(5):
			ch_guessed = guess_word[index]
			ch_word = word[index]
			ch_guessed_res = guess_res[index]

			if (ch_guessed_res == "1") and (ch_guessed != ch_word):
				word_list.pop(current_word_number)
				total_number_words -= 1
				break

			elif (ch_guessed_res == "2") and ((ch_guessed == ch_word) or (ch_guessed not in word)):
				word_list.pop(current_word_number)
				total_number_words -= 1
				break

			elif (ch_guessed_res == "3") and (ch_guessed in word):
				if repeated_char(guess_word):
					if ch_guessed == ch_word:
						word_list.pop(current_word_number)
						total_number_words -= 1
						break
				else:
					word_list.pop(current_word_number)
					total_number_words -= 1
					break

			else:
				if index == 4:
					current_word_number += 1

	return word_list


# Finalized function.
def play_game(word_list):
	global total_iteration, max_iteration
	number_of_iteration = 0
	guess_res = "33333"
	while guess_res != "11111":
		print("You can try : {}".format(get_word()))
		guess_word = input("Enter your guessed word : ")
		guess_res = input("Enter the result : ")
		word_list = filter_words(guess_res, guess_word, word_list)
		number_of_iteration += 1
	else:
		print("\n\nYou did it. Fantastic!")
		print("Total number of iterations performed = {}".format(number_of_iteration))


all_words_need = 0
word_list = load_words(all_word=all_words_need)
total_iteration = 0
play_game(word_list)
