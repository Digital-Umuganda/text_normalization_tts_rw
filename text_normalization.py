from pynini.lib import pynutil
import pynini
import nemo_text_processing
from pynini.lib import pynutil
import os
import argparse

parser = argparse.ArgumentParser(description='Normalize and print a text argument provided by the user.')

parser.add_argument('-t','--text', type=str, help='The text to normalize.')

args = parser.parse_args()
import re
def normalize_spaces(text):
    # Replace occurrences of one or more spaces with a single space
    normalized_text = re.sub(r'\s+', ' ', text)
    return normalized_text

def compress_consecutive_spaced_na(text):

    pattern = r"(?:\b|(?<=\s))(na )+na(?=\s|$)"
    # Replace found patterns with a single " na "
    result = re.sub(pattern, ' na ', text)
    return result

def apply_fst(text, fst):
    try:
        return pynini.shortestpath(text @ fst).string()

    except pynini.FstOpError:
        print(f"Error: no valid output with given input: '{text}'")
PATH="."
text = args.text
classify_far_file = os.path.join(PATH, "tokenize_and_classify.far")
verbalize_far_file = os.path.join(PATH, "verbalize.far")

classify = pynini.Far(classify_far_file, mode="r")["TOKENIZE_AND_CLASSIFY"]
verbalize = pynini.Far(verbalize_far_file,mode="r")["ALL"]

# classes = classes.replace("'"," ")
#print("processed: ",classes)
#print("\nverbalizing")
try:
    classes = apply_fst(text,classify)

    verbalized_text = apply_fst(classes,verbalize)
    normalized_text = normalize_spaces(verbalized_text)
    compressed_text = compress_consecutive_spaced_na(normalized_text)
    print(normalize_spaces(compressed_text))
    # print("\n******************************************\n")
    # print("and then we are here")
except Exception as E:
    print("Failed to process the string........")
    print(text)
