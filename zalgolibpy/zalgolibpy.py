from diacritics import DOWN_MARKS, UP_MARKS, MID_MARKS, DOWN_LEN, UP_LEN, MID_LEN
from random import choices

# len(DOWN_MARKS) is 40
# len(UP_MARKS) is 46
# len(MID_MARKS) is 21

def enzalgofy(text="I summon Zalgo",intensity=50):
    '''Turns regular text into Zalgo text.
    intensity should be a number between 1 and 100
    '''
    # check type first, then value to raise the error without raising an error
    if not isinstance(intensity, int) or intensity < 0 or intensity > 100:
        raise ValueError("intensity, if provided, must be an int between 0 and 100")
    
    # adjust number of characters for each type by intensity
    down_count = round(DOWN_LEN * intensity / 100)
    up_count = round(UP_LEN * intensity / 100)
    mid_count = round(MID_LEN * intensity / 100)
    
    zalgo = ""
    
    for char in text:
        downlist = choices(DOWN_MARKS,k=down_count)
        uplist = choices(UP_MARKS,k=up_count)
        midlist = choices(MID_MARKS,k=mid_count)
        zalgo += char
        marks = [*uplist, *midlist, *downlist]
        for mark in marks:
            zalgo += mark.strip()
    return zalgo

def dezalgofy(text=""):
    '''Takes text and removes Zalgo diacritics from it then returns the cleaned
    up output
    '''
    marks = [*DOWN_MARKS, *UP_MARKS, *MID_MARKS]
    for mark in marks:
        nonzalgo = text.replace(mark.strip(), "")
    return nonzalgo