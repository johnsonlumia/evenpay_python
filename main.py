#******************************************#
#              EvenPay(v1)                 #
#                                          #
#                main.py                   #
#         created by Renjie Zhu            #
#              on 7/20/16                  #
#******************************************#

# import
from participant import Participant


# constants
MAXPARTICIPANT = 10

# information input function, return number of participants
def info_input(participants):
    participant_number = 0
    # loop for information input
    for numParticipant in range(0,MAXPARTICIPANT+1):

        name = input("What is the name?\n")
        paid = input("How much did %s pay in total?\n" % (name))
        # insert into the participants list
        temp = Participant(name,float(paid))
        participants.append(temp)
        repeat = input("Add another participant? ")
        participant_number = participant_number + 1
        if repeat != "y" and repeat != "Y":
            break
    return participant_number

# get results and print results
def result(participants,average):
    for element in participants:
        element.difference(average)

    for element in participants:
        if element.get_pays() >= 0:
            print(element.get_name(),"should take $",
                  element.get_pays(),"from the pool.")
        else:
            print(element.get_name(),"should put $",
                  -element.get_pays(),"into the pool.")
    return

# main function
def main():
    print("Welcome to EvenPay(v1)")
    participants = []
    total_expenditure = 0
    participant_number = info_input(participants)

    # calculate total expenditure
    for element in participants:
        print(element.get_name(),":", element.get_paid())
        total_expenditure = total_expenditure + element.get_paid()

    print("The total expenditure is", total_expenditure)

    average = total_expenditure / participant_number

    result(participants,average)

    print("Thank you for using EvanPay(v1)")

    return


# run
if __name__ == '__main__':
    main()
