def length_of_last_word(sentence):
  list = sentence.split()
  last_element = len(list) - 1
  return len(list[last_element])