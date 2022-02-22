#This is the Main Function
def timetable(labcourses,labslots,thcourses,thslots):
    if (len(labslots)>=len(labcourses)) and (len(thslots)>=len(thcourses)):
        #If the number of slots are less than the number of courses the program will terminated
        timetable_d = {} 
        while thcourses != []:#This while loop will assign slots to the theory courses in descending order
            late_slot = max(thslots)
            timetable_d[thcourses[0]] = late_slot
            thcourses.remove(thcourses[0])
            thslots.remove(late_slot)
        

        while labcourses != []:#This while loop will assign slots to the theory courses in descending order
            late_slotlab = max(labslots)
            timetable_d[labcourses[0]] = late_slotlab
            labcourses.remove(labcourses[0])
            labslots.remove(late_slotlab)
        
        return timetable_d

    else:
        return "ERROR : SLOTS NOT AVAILABLE"





#This function seperates lab and theory courses and slots from the parent list

def seperate(courses,slots):
    labcourses,labslots,thcourses,thslots = [],[],[],[]
    for i in courses:
        if i[len(i)-1] == "P": 
            #If the last character of the course is P then the course is Practical(lab) for example BCHY101P
            labcourses.append(i)
        else:
            thcourses.append(i)
    
    for j in slots:
        if j[0] == "L":
            #If the last character of the course is L then the course is Lecture(theory) for example BCHY101L
            labslots.append(j)
        else:
            thslots.append(j)

    return labcourses,labslots,thcourses,thslots




# Program starts from here
if __name__ == "__main__":
    l1 = list(map(str,input("Enter courses:").rstrip().split())) #Inputing courses
    l2 = list(map(str,input("Enter Available Slots:").rstrip().split())) #Inputing available slots

    l1lab,l2lab,l1th,l2th = seperate(l1,l2)   #Moving to seperate function

    print(timetable(l1lab,l2lab,l1th,l2th))   #Calling a function



"""********************************OUTPUT SIMULATION********************************
Enter courses:BCHY101P BCHY101L BMAT101L BMAT101P BEEE101P BEEE101L
Enter Available Slots:A4 A3 B4 A1 L33 L34 L21 L1

OUTPUT:
{"BCHY101L":"B4","BMAT101L":"A4","BEEE101L":"A3","BCHY101P":"L34","BMAT101P":"L33","BEEE101P":"L21"}


#*********************************************************************************"""



'''NOTE: I tried this with C++, but i am not able to accomplish the result. I apologize for the same, i know
my skills are not polished as i learned most of the things from the internet.'''