import random
#Defining classes
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
        self.doctors = []
        self.prescriptions = []
        self.consultation_queue = []
        self.authenticated = False  # Initializing authenticated attribute to False

    #Adding the functions to the patient record managing system
    #creating a username and password to ensure privacy and integrity of the patients data
    def authenticate(self, username, password):
        # Created a username and password to authenticate the person whos trying to make the changes
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
    def add_patient(self, patient):
        #adding patients
        self.patients.append(patient)

    def update_patient(self, patient_id, new_info):
        #updating patient information utilziing dictonaries
        for patient in self.patients:
            if patient.id == patient_id:
                patient.__dict__.update(new_info)

    def remove_patient(self, patient_id):
        #removing a patient
        self.patients = [patient for patient in self.patients if patient.id != patient_id]

    def schedule_appointment(self, patient_id, doctor_id, appointment_date, appointment_time):
        #scheduling an appointment
        for patient in self.patients:
            if patient.id == patient_id:
                patient.doctor = doctor_id
                #asking for appointment information
                patient.appointment_date = appointment_date
                patient.appointment_time = appointment_time
                break

    def add_doctor(self, doctor):
        #adding doctors
        self.doctors.append(doctor)

    def add_prescription(self, prescription):
        self.prescriptions.append(prescription)

    def add_to_consultation_queue(self, patient_id):
        self.consultation_queue.append(patient_id)

    def remove_from_consultation_queue(self):
        return self.consultation_queue.pop(0)

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
            #Gathers the medications presrbied to a specific patient (making sure it is = to the patient id)
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
    #Using a radom generator to generate a list of objects (patients)
    def generate_random_patients(self, num_patients):
        names = ["Khaled", "Salma", "Sultan", "Mohamed", "Saif", "Mahra"]
        medical_histories = ["Diabetes", "Heart Conditions", "Cholesterol", "Cancer", "Blood Pressure"]
        current_conditions = ["Critical", "Urgent", "Stable", "Good"]
        for i in range(num_patients):
            id = len(self.patients) + 1
            name = random.choice(names)
            age = random.randint(20, 80)
            medical_history = random.choice(medical_histories)
            current_condition = random.choice(current_conditions)
            patient = Patient(id, name, age, medical_history, current_condition)
            self.add_patient(patient)
    #Utilizing mergesort to sort the patients based on their medical condition
    def merge_sort(self, patient_list):
        if len(patient_list) <= 1:
            return patient_list

        # Divide the list into two halves
        mid = len(patient_list) // 2
        left_half = patient_list[:mid]
        right_half = patient_list[mid:]

        # Recursively sort each half
        left_half = self.merge_sort(left_half)
        right_half = self.merge_sort(right_half)

        # Merge the sorted halves
        return self.merge(left_half, right_half)

    def merge(self, left, right):
        merged = []
        left_index = right_index = 0

        # Merge the two lists by comparing elements
        while left_index < len(left) and right_index < len(right):
            if sort_by_medical_condition(left[left_index]) <= sort_by_medical_condition(right[right_index]):
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        # Append remaining elements
        merged.extend(left[left_index:])
        merged.extend(right[right_index:])

        return merged

def sort_by_medical_condition(patient):
    return patient.medical_history[0]  # Assuming the first medical condition is the primary one

def main():
    hospital = Hospital()

    # Generate 5 random patients initially
    hospital.generate_random_patients(5)

    while True:
        print("\n- Hospital Management System -")
        # Check if authenticated before displaying options
        if hospital.check_authentication():
            print("Existing Patients:")
            for patient in hospital.patients:
                print(f"ID: {patient.id}, Name: {patient.name}")

            # Provifing the list of options (menu based interface where the user could choose which one they want)
            print("\n1. Add Patient")
            print("2. Update Patient")
            print("3. Remove Patient")
            print("4. Schedule Appointment")
            print("5. Add Doctor")
            print("6. Add Prescription")
            print("7. Display Patient Summary")
            print("8. Sort Patients by Medical Record")
            print("9. Logout")
            print("10. Exit")

            # Allowing the user to input which option they would like
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter patient's name: ")
                age = int(input("Enter patient's age: "))
                medical_history = input("Enter patient's existing medical conditions (comma-separated): ")
                current_condition = input("Enter patient's current condition: ")
                medical_history_list = [condition.strip() for condition in medical_history.split(",")]
                patient = Patient(len(hospital.patients) + 1, name, age, medical_history_list, current_condition)
                hospital.add_patient(patient)
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
                name = input("Enter doctor's name: ")
                specialization = input("Enter doctor's specialization: ")
                doctor_id = len(hospital.doctors) + 1
                doctor = Doctor(doctor_id, name, specialization)
                hospital.add_doctor(doctor)
                print("Doctor added successfully!")

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
                hospital.logout()
                print("Logged out successfully!")
                continue

            elif choice == '10':
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please enter a valid option.")

        else:
            print("\n- Authentication Required -")
            username = input("Enter username: ")
            password = input("Enter password: ")
            hospital.authenticate(username, password)

#calling the funciton to run
if __name__ == "__main__":
    main()
