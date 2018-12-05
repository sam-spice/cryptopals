
from binascii import unhexlify, b2a_base64
from collections import Counter
'''
letter_frequency = {'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253, 	
 
e	12.702%	
 
f	2.228%	
 
g	2.015%	
 
h	6.094%	
 
i	6.966%	
 
j	0.153%	
 
k	3.872%	
 
l	4.025%	
 
m	2.406%	
 
n	6.749%	
 
o	7.507%	
 
p	1.929%	
 
q	0.095%	
 
r	5.987%	
 
s	6.327%	
 
t	9.256%	
 
u	2.758%	
 
v	0.978%	
 
w	5.370%	
 
x	0.150%	
 
y	3.978%	
 
z	0.074%}
'''
ALPHA_LENGTH = 27
def hex2b64(hex_str):
    byte_str = unhexlify(hex_str)
    return b2a_base64(byte_str, newline=False)

def exor(first, second):
    assert len(first) == len(second)
    return bytearray([first_bytes ^ second_bytes for (first_bytes, second_bytes) in zip(first, second)])

def single_byte_exor(to_decode, char):
    return exor(to_decode, bytearray([ord(char)] * len(to_decode)))

def rank_solution(solution):
    solution_string = ''.join([chr(x) for x in solution])
    alpha_string = ''.join([letter for letter in solution_string if letter.isalpha()])
    freq_string = 'EARIOTNSLCUDPMHGBFYWKVXZJQ'.lower()

    counter_array = Counter(alpha_string.lower()).most_common(None)

    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    score = sum([character_frequencies.get(x, 0) for x in solution_string.lower()])

    return score

def brute_force_char_xor(to_check):
    scores = []
    possible_chars = ''.join([chr(x) for x in range(256)])
    for char in possible_chars:
        xored = single_byte_exor(to_check, char)
        score = rank_solution(xored)
        scores.append((score, xored, char))

    sorted_based_on_score = sorted(scores, key=lambda score : score[0], reverse=True)
    return sorted_based_on_score[0]

def find_xord_string(strings_to_check):
    evaluated = list()
    for entry in strings_to_check:
        evaluated.append(brute_force_char_xor(entry))

    sorted_based_on_score = sorted(evaluated, key=lambda score: score[0], reverse=True)
    return sorted_based_on_score[0]



def main():
    opened_file = open("strings.txt", 'r')
    contents = opened_file.read().split('\n')
    hexed_contents = [unhexlify(x) for x in contents]
    print(find_xord_string(hexed_contents))

if __name__== "__main__":
  main()