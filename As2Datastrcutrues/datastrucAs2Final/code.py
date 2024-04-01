import random

#creating classes
class Patient:
    def __init__(self, id, name, age, medical_history, current_condition):
        self.id = id
        self.name = name
        self.age = age
        self.medical_history = medical_history
        self.current_condition = current_condition
        self.doctor = None
        self.appointment_date = None
        self.appointment_time = None

class Doctor:
    def __init__(self, id, name, specialization):
        self.id = id
        self.name = name
        self.specialization = specialization

class Prescription:
    def __init__(self, patient_id, medication):
        self.patient_id = patient_id
        self.medication = medication

class Hospital:
    def __init__(self):
        self.patients = []
        self.prescriptions = []
        self.consultation_queue = []
        self.newly_added_consultation_queue = []  # New queue for newly added patients
        self.authenticated = False

    #creating a function that authorizes the user, in order to ensure the privacy and integrity of the patients data 
    def authenticate(self, username, password):
        if username == "admin" and password == "1234":
            self.authenticated = True
            print("Authentication successful.")
        else:
            print("Authentication failed.")

    def logout(self):
        self.authenticated = False
        print("Logged out successfully.")

    def check_authentication(self):
        return self.authenticated

    #adding new patients
    def add_patient(self, patient):
        self.patients.append(patient)
    #function to update patient info
    def update_patient(self, patient_id, new_info):
        for patient in self.patients:
            if patient.id == patient_id:
                patient.__dict__.update(new_info)
    #removing/deleting patients
    def remove_patient(self, patient_id):
        self.patients = [patient for patient in self.patients if patient.id != patient_id]
    #scheduling appointments
    def schedule_appointment(self, patient_id, doctor_id, appointment_date, appointment_time):
        for patient in self.patients:
            if patient.id == patient_id:
                patient.doctor = doctor_id
                patient.appointment_date = appointment_date
                patient.appointment_time = appointment_time
                break
#issuing a prescription
    def add_prescription(self, prescription):
        self.prescriptions.append(prescription)
#adding to consultation queue
    def add_to_consultation_queue(self, patient_id):
        self.consultation_queue.append(patient_id)
        self.newly_added_consultation_queue.append(patient_id)  # Add to the new queue as well

    def remove_from_consultation_queue(self):
        if self.consultation_queue:
            return self.consultation_queue.pop(0)
        else:
            print("No patients in the consultation queue.")
            return None
#linear search to look for patient using their ID 
    def search_patient(self, patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                return patient

    def display_patient_summary(self, patient_id):
        patient = self.search_patient(patient_id)
        doctor = None
        if patient:
            for d in self.doctors:
                if d.id == patient.doctor:
                    doctor = d
                    break
            medications = [prescription.medication for prescription in self.prescriptions if prescription.patient_id == patient_id]
            return {
                "Patient Name": patient.name,
                "Age": patient.age,
                "Medical History": patient.medical_history,
                "Current Condition": patient.current_condition,
                "Doctor": doctor.name if doctor else "Not scheduled yet",
                "Appointment Date": patient.appointment_date if patient.appointment_date else "Not scheduled yet",
                "Appointment Time": patient.appointment_time if patient.appointment_time else "Not scheduled yet",
                "Medications": medications
            }
        else:
            return "Patient not found"
#generating random patients 
    def generate_random_patients(self, num_patients):
        names = ["Khaled", "Salma", "Sultan", "Mohamed", "Saif", "Mahra", "Salem", "Ahmed", "Rawdha", "Maryam",
                 "Maitha", "Ghanem", "Abdulla", "Rashed"]
        medical_histories = ["Diabetes", "Heart Conditions", "Cholesterol", "Cancer", "Blood Pressure"]
        current_conditions = ["Critical", "Urgent", "Stable", "Good"]
        for i in range(num_patients):
            id = len(self.patients) + 1
            name = random.choice(names)
            age = random.randint(20, 80)
            medical_history = random.choice(medical_histories)
            current_condition = random.choice(current_conditions)
            patient = Patient(id, name, age, medical_history, current_condition)
            self.add_patient(patient)  # Add patient directly to existing patients list
# This function sorts patients by their medical condition using merge sort algorithm
def merge_sort(self, patient_list):
    # Base case: if the list has 0 or 1 element, it's already sorted
    if len(patient_list) <= 1:
        return patient_list

    # Split the list into two halves
    mid = len(patient_list) // 2
    left_half = patient_list[:mid]
    right_half = patient_list[mid:]

    # Recursively sort each half
    left_half = self.merge_sort(left_half)
    right_half = self.merge_sort(right_half)

    # Merge the sorted halves
    return self.merge(left_half, right_half)

# This function merges two sorted lists into one sorted list
def merge(self, left, right):
    merged = []
    left_index = right_index = 0

    # Compare elements from both lists and append the smaller one to the merged list
    while left_index < len(left) and right_index < len(right):
        if sort_by_medical_condition(left[left_index]) <= sort_by_medical_condition(right[right_index]):
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append any remaining elements from the left and right lists
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

# This function extracts the first character from the medical history for sorting
def sort_by_medical_condition(patient):
    return patient.medical_history[0]

def main():
    hospital = Hospital()
    hospital.generate_random_patients(5)

    while True:
        if hospital.check_authentication():
            if hospital.patients:
                print("Existing Patients:")
                for patient in hospital.patients:
                    print(f"ID: {patient.id}, Name: {patient.name}")
#displaying the option in a menu interface for the user
                print("\n1. Add Patient")
                print("2. Update Patient")
                print("3. Remove Patient")
                print("4. Schedule Appointment")
                print("5. Add patient to Consultation queue")
                print("6. Add Prescription")
                print("7. Display Patient Summary")
                print("8. Sort Patients by Medical Record")
                print("9. Search for Patient")
                print("10. Remove from consultation queue")
                print("11. Logout")

                choice = input("\nEnter your choice: ")

            if choice == '1':
                name = input("Enter patient's name: ")
                age = int(input("Enter patient's age: "))
                medical_history = input("Enter patient's existing medical conditions (comma-separated): ")
                current_condition = input("Enter patient's current condition: ")
                medical_history_list = [condition.strip() for condition in medical_history.split(",")]
                patient = Patient(len(hospital.patients) + 1, name, age, medical_history_list, current_condition)
                hospital.add_patient(patient)
                hospital.add_to_consultation_queue(patient.id)  # Add to consultation queue
                print("Patient added successfully!")

            elif choice == '2':
                patient_id = int(input("Enter patient ID to update: "))
                new_info = {}
                new_info['name'] = input("Enter new name: ")
                new_info['age'] = int(input("Enter new age: "))
                new_info['medical_history'] = input("Enter new medical history: ")
                new_info['current_condition'] = input("Enter new current condition: ")
                hospital.update_patient(patient_id, new_info)
                print("Patient updated successfully!")

            elif choice == '3':
                patient_id = int(input("Enter patient ID to remove: "))
                hospital.remove_patient(patient_id)
                print("Patient removed successfully!")

            elif choice == '4':
                patient_id = int(input("Enter patient ID: "))
                doctor_id = int(input("Enter doctor ID: "))
                appointment_date = input("Enter appointment date (e.g., YYYY-MM-DD): ")
                appointment_time = input("Enter appointment time: ")
                hospital.schedule_appointment(patient_id, doctor_id, appointment_date, appointment_time)
                print("Appointment scheduled successfully!")



            elif choice == '5':
                num_patients_to_add = int(input("Enter the number of patients to add to the consultation queue: "))
                hospital.generate_random_patients(num_patients_to_add)
                print("\nPatients added to existing patients list successfully!")
                print("\nExisting Patients:")
                for patient in hospital.patients:
                    print(f"ID: {patient.id}, Name: {patient.name}")




            elif choice == '6':
                patient_id = int(input("Enter patient ID to add prescription: "))
                medication = input("Enter medication: ")
                prescription = Prescription(patient_id, medication)
                hospital.add_prescription(prescription)
                print("Prescription added successfully!")

            elif choice == '7':
                patient_id = int(input("Enter patient ID to display summary: "))
                summary = hospital.display_patient_summary(patient_id)
                if summary:
                  print(summary)
                else:
                    print("Patient not found!")

            elif choice == '8':
                # Use merge sort to sort patients by medical condition
                sorted_patients_by_condition = hospital.merge_sort(hospital.patients)

                # Display sorted patients
                print("\nPatients Sorted by Medical Condition:")
                for patient in sorted_patients_by_condition:
                    print(f"ID: {patient.id}, Name: {patient.name}, Medical Condition: {patient.medical_history}")

            elif choice == '9':
                # Searching for a patient
                patient_id = int(input("Enter patient ID to search: "))
                patient = hospital.search_patient(patient_id)
                if patient:
                    print("Patient found!")
                    print("Patient Details:")
                    print(f"ID: {patient.id}")
                    print(f"Name: {patient.name}")
                    print(f"Age: {patient.age}")
                    print(f"Medical History: {', '.join(patient.medical_history)}")
                    print(f"Current Condition: {patient.current_condition}")
                else:
                    print("Patient not found!")


            elif choice == '10':
                num_patients_to_remove = int(
                    input("Enter the number of patients to remove from the existing patients list: "))
                for _ in range(num_patients_to_remove):
                    removed_patient = hospital.patients.pop(0)  # Remove the first patient from the list
                    print(
                        f"Patient with ID {removed_patient.id} and name {removed_patient.name} removed from existing patients list.")


            elif choice == '11':
                hospital.logout()
                print("Logged out successfully")
                continue


            else:
                print("Invalid choice. Please enter a valid option.")

        else:
            print("\n- Authentication Required -")
            username = input("Enter username: ")
            password = input("Enter password: ")
            hospital.authenticate(username, password)

#calling function
if __name__ == "__main__":
    main()
