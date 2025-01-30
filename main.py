'''
Author: Nick Heyer
KUID: 3142337
Date: 11/13/24
Lab: lab08
Last modified: 11/13/24
Purpose: uses maxheap to arrange patients in a hospital 
'''

from patient import Patient
from maxheap import MaxHeap
'''
The main file takes in a provided file and reads it line for line checking for the commands given and goes through individually doing the commands. 
The main file also is capable of knowing if the file is empty and knowing there are no patients to treat saying " no patients waiting
The file can also handle all errors without crashing and giving an explanation when necesary. 
'''
def main():
    hospital_queue = MaxHeap()
    arrival_counter = 1 
    '''
    Counter to track the order of patient arrival
    '''
    file_name = input('Enter the file containg patients and commands: ')
    '''
    Asks the user to enter a file name containing the elements needed to process
    '''
    try:
        '''
        Opens the specified file for reading
        '''
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split() 
                ''' 
                splits the line into parts basedd on the spaces 
                '''
                command = parts[0]
                try:
                    '''
                    Handles the arrive command ot add the patient to the Q 
                    '''
                    if command == 'ARRIVE':
                        '''
                        gets the patient info
                        '''
                        first_name = parts[1]
                        last_name = parts[2]
                        age = int(parts[3])
                        illness = parts[4]
                        severity = int(parts[5])
                        patient = Patient(first_name,last_name,age,illness,severity,arrival_counter)
                        hospital_queue.add(patient)
                        arrival_counter += 1
                        '''
                        arrival counter for next patient
                        '''
                    elif command == 'COUNT':
                        '''
                        Handles count command to display the count of patients waiting
                        '''
                        count = hospital_queue.count()
                        print(f'\nThere are {count} patients waiting.\n')
                    elif command == 'NEXT':
                        '''
                        Looks at the next patient without removing them
                        '''
                        try:
                            next_patient = hospital_queue.peek()
                            print("Next patient:")
                            print(f"  Name: {next_patient.last_name}, {next_patient.first_name}")
                            print(f"  Age: {next_patient.age}")
                            print(f"  Suffers from: {next_patient.illness}")
                            print(f"  Illness severity: {next_patient.severity}")
                            print(f"  Arrival order: {next_patient.arrival_order}\n")
                        except IndexError:
                            '''
                            Handles the case of no patients waiting
                            '''
                            print("No patients waiting.")
                    elif command == "TREAT":
                        '''
                        Handles the treat command to remove the patient from the Q
                        '''
                        try:
                            '''
                            removes patient from the Q and returns the highest 
                            '''
                            treated_patient = hospital_queue.pop()
                        except IndexError:
                            print("No patients to treat.")
                    else:
                        print('File contains improper commands or no commands')
                except IndexError:
                    print('File formated improperly')
                except ValueError:
                    print('File formated improperly')
    except FileNotFoundError:
        print('File not found.')
main()