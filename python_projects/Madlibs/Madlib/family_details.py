import edu_details
def madlib():
    father=input("father:")
    f_occ=input("father's occupation:")
    mother=input("mother:")
    m_occ=input("mother's occupation:")
    sis=input("sister:")
    s_study=input("sister's study:")
    s_s_place= input("enter sister's study city:")
    edu_details.madlib()
    madlib= f" As my family concerned. \n My father's name is {father}. He is working as {f_occ}. \n My mother's name is {mother}. She is a {m_occ}. \n I have an younger sister and her name is {sis} and she is persuing {s_study} at {s_s_place}."
    print(madlib)

