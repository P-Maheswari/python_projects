import personal_details
def madlib():
    school = input("enter your school name:")
    s_city= input("enter your schooling city:")
    cgpa1= input("enter your cgpa:")
    college= input("enter your college")
    c_city= input("enter your college city:")
    cgpa2= input("enter your percentage: ")
    univer= input("enter your university(graduation/degree):")
    u_city= input("enter your graduation city:")
    cgpa3= input("enter your cgpa:")
    personal_details.madlib()
    madlib= f" I completed my schooling at {school} in {s_city} with {cgpa1} CGPA. \n I completed my plus 2 at {college} in {c_city} with {cgpa2} percentage.\n Currently, I am persuing my Graduation at {univer} in {u_city} with {cgpa3} CGPA."
     
    print(madlib)

