
import time
import random
import matplotlib.pyplot as plt

# Defining classes
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

    def add_patient(self, patient):
        self.patients.append(patient)

    def schedule_appointment(self, patient_id, doctor_id, appointment_date, appointment_time):
        for patient in self.patients:
            if patient.id == patient_id:
                patient.doctor = doctor_id
                patient.appointment_date = appointment_date
                patient.appointment_time = appointment_time
                break

def measure_time_complexity_add_patient(hospital, num_patients):
    start_time = time.time()
    for i in range(num_patients):
        id = len(hospital.patients) + 1
        name = "Patient " + str(id)
        age = random.randint(20, 80)
        medical_history = "Random Medical History"
        current_condition = "Random Condition"
        patient = Patient(id, name, age, medical_history, current_condition)
        hospital.add_patient(patient)
    end_time = time.time()
    return end_time - start_time

def measure_time_complexity_schedule_appointment(hospital, num_appointments):
    start_time = time.time()
    for i in range(num_appointments):
        patient_id = random.randint(1, len(hospital.patients))
        doctor_id = random.randint(1, 10)  # Assuming 10 doctors exist
        appointment_date = "2024-04-02"  # Random date
        appointment_time = "10:00"  # Random time
        hospital.schedule_appointment(patient_id, doctor_id, appointment_date, appointment_time)
    end_time = time.time()
    return end_time - start_time

def main():
    hospital = Hospital()

    # Generate 100 random patients initially
    num_patients = 100
    time_taken_add_patient = measure_time_complexity_add_patient(hospital, num_patients)
    print(f"Time taken to add {num_patients} patients: {time_taken_add_patient} seconds")

    # Generate 100 random appointments
    num_appointments = 100
    time_taken_schedule_appointment = measure_time_complexity_schedule_appointment(hospital, num_appointments)
    print(f"Time taken to schedule {num_appointments} appointments: {time_taken_schedule_appointment} seconds")

    # Plotting time complexity for add_patient function
    num_patients_list = [10, 50, 100, 200, 500]
    time_taken_add_patient_list = []
    for num in num_patients_list:
        time_taken = measure_time_complexity_add_patient(hospital, num)
        time_taken_add_patient_list.append(time_taken)

    plt.plot(num_patients_list, time_taken_add_patient_list)
    plt.xlabel('Number of Patients')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Time Complexity of add_patient Function')
    plt.show()

    # Plotting time complexity for schedule_appointment function
    num_appointments_list = [10, 50, 100, 200, 500]
    time_taken_schedule_appointment_list = []
    for num in num_appointments_list:
        time_taken = measure_time_complexity_schedule_appointment(hospital, num)
        time_taken_schedule_appointment_list.append(time_taken)

    plt.plot(num_appointments_list, time_taken_schedule_appointment_list)
    plt.xlabel('Number of Appointments')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Time Complexity of schedule_appointment Function')
    plt.show()

if __name__ == "__main__":
    main()


