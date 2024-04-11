from pynini.lib import pynutil
import pynini
import nemo_text_processing
from pynini.lib import pynutil
import os
import argparse

parser = argparse.ArgumentParser(description='Normalize and print a text argument provided by the user.')

parser.add_argument('-t','--text', type=str, help='The text to normalize.')

args = parser.parse_args()

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

classes = apply_fst(text,classify)
# print(classes)
# print("\n====================================\n")
# print("we are here")
try:
    print(apply_fst(classes,verbalize))
    # print("\n******************************************\n")
    # print("and then we are here")
except Exception as E:
    print(E)
