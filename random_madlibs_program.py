'''use the files from the folder we have created'''
from madlib_stories import story_1, story_2, story_3, story_4
import random #imports the random module

if __name__ == "__main__":
    m = random.choice([story_1,story_2,story_3,story_4])
    m.madlibs()
