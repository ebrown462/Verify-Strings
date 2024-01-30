def validation(sentence):
    # sets score to 0
    score = 0

# ------------------------------------------------------------------------
    # verification 1
    try:
        # detects if 1st item in sentence is uppercase
        if sentence[0].isupper():
            score += 1

    except Exception as e:
        print(f"\n- ERROR WITH VALIDATION 1: {e}")

# ------------------------------------------------------------------------
    # verification 2
    try:
        # temp variable to count how many '"' are in the sentence
        tempSentenceCount = sentence.count('"')

        # checks if the temp variable is even
        if tempSentenceCount % 2 == 0:
            score += 1

        del tempSentenceCount

    except Exception as e:
        print(f"\n- ERROR WITH VALIDATION 2: {e}")

# ------------------------------------------------------------------------
    # verification 3
    try:
        # temp variable to store a list of "termination" characters
        tempTermChar = [".", "?", "!"]

        # checks whether the final character is in the list
        if sentence[len(sentence) - 1] in tempTermChar:
            score +=1

        del tempTermChar

    except Exception as e:
        print(f"\n- ERROR WITH VALIDATION 3: {e}")

# ------------------------------------------------------------------------
    # verification 4
    try:
        # checks if "." is in the sentence at somewhere other than the end
        if "." in sentence[:-1]:
            pass

        # if not, then the sentence doesn't end in a period
        else:
            score += 1

    except Exception as e:
        print(f"\n- ERROR WITH VALIDATION 4: {e}")

# ------------------------------------------------------------------------
    # verification 5
    try:
        # creates a set of numbers through 1-12
        below_13_numbers = {"12", "11", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1"}

        # removes all "," and splits each word into a list
        tempSentence = sentence.replace(",", "")
        tempSentence = tempSentence.split()

        count = 0

        # loops through each word in the sentence, and checks if it matches any on the number list
        for i in tempSentence:
            for j in below_13_numbers:
                if i == str(j):
                    # increases count if there is a match
                    count += 1

        # if count is 0, no words match
        if count == 0:
            score += 1

        del below_13_numbers
        del tempSentence
        del count

    except Exception as e:
        print(f"\n- ERROR WITH VALIDATION 5: {e}")

# ------------------------------------------------------------------------
    # prints final score
    try:
        # checks if the string is valid
        if score == 5:
            del score
            return True
        else:
            del score
            return False

    except Exception as e:
        print(f"\n- ERROR WITH PRINTING SCORE: {e}")