#!/usr/bin/env python3
# hospital_manager.py
# Compact, working Hospital Patient Management System (single-file)
# Name: ALKA
# Roll No: 2501060083
# Course: BCA (AI & DS)
# Semester: 1st
# Assignment: Unit-3

import json
import logging
from pathlib import Path

# -----------------------
# Setup logging & paths
# -----------------------
logging.basicConfig(filename="hospital.log",
                    level=logging.INFO,
                    format="%(asctime)s %(levelname)s: %(message)s")

DATA_PATH = Path("data")
DATA_FILE = DATA_PATH / "records.json"

# Ensure data folder & file exist
DATA_PATH.mkdir(parents=True, exist_ok=True)
if not DATA_FILE.exists():
    DATA_FILE.write_text(json.dumps({"patients": [], "doctors": [], "assignments": {}}, indent=4))


# -----------------------
# Domain classes
# -----------------------
class Patient:
    def __init__(self, name, age, patient_id, disease, status="Admitted"):
        self.name = name
        self.age = int(age)
        self.patient_id = str(patient_id)
        self.disease = disease
        self.status = status

    def admit(self):
        self.status = "Admitted"

    def discharge(self):
        self.status = "Discharged"

    def is_admitted(self):
        return self.status == "Admitted"

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "patient_id": self.patient_id,
            "disease": self.disease,
            "status": self.status
        }

    @staticmethod
    def from_dict(d):
        return Patient(d["name"], d["age"], d["patient_id"], d["disease"], d.get("status", "Admitted"))

    def __str__(self):
        return f"{self.patient_id} | {self.name} | Age: {self.age} | {self.disease} | {self.status}"


class Doctor:
    def __init__(self, name, specialization, doctor_id):
        self.name = name
        self.specialization = specialization
        self.doctor_id = str(doctor_id)

    def to_dict(self):
        return {"name": self.name, "specialization": self.specialization, "doctor_id": self.doctor_id}

    @staticmethod
    def from_dict(d):
        return Doctor(d["name"], d["specialization"], d["doctor_id"])

    def __str__(self):
        return f"{self.doctor_id} | Dr. {self.name} | {self.specialization}"


# -----------------------
# Management class
# -----------------------
class HospitalManagement:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.assignments = {}
        self.load()

    def load(self):
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
            for pd in data.get("patients", []):
                p = Patient.from_dict(pd)
                self.patients[p.patient_id] = p
            for dd in data.get("doctors", []):
                d = Doctor.from_dict(dd)
                self.doctors[d.doctor_id] = d
            self.assignments = data.get("assignments", {})
            logging.info("Loaded data from records.json")
        except Exception as e:
            logging.error(f"Load error: {e}")
            print("Error loading data!")

    def save(self):
        try:
            payload = {
                "patients": [p.to_dict() for p in self.patients.values()],
                "doctors": [d.to_dict() for d in self.doctors.values()],
                "assignments": self.assignments
            }
            with open(DATA_FILE, "w") as f:
                json.dump(payload, f, indent=4)
            logging.info("Saved data to records.json")
        except Exception as e:
            logging.error(f"Save error: {e}")
            print("Error saving data!")

    # Patient methods
    def add_patient(self, name, age, patient_id, disease):
        if patient_id in self.patients:
            print("Patient ID already exists.")
            return False
        p = Patient(name, age, patient_id, disease)
        self.patients[patient_id] = p
        self.save()
        return True

    def search_patient(self, pid):
        return self.patients.get(pid)

    def display_patients(self):
        if not self.patients:
            print("No patients recorded.")
            return
        print("\n--- Patients ---")
        for p in self.patients.values():
            doctor = self.assignments.get(p.patient_id, "None")
            print(f"{p} | Assigned Doctor: {doctor}")
        print()

    def discharge_patient(self, pid):
        p = self.search_patient(pid)
        if not p:
            print("Patient not found.")
            return False
        p.discharge()
        self.assignments.pop(pid, None)
        self.save()
        return True

    # Doctor methods
    def add_doctor(self, name, specialization, doctor_id):
        if doctor_id in self.doctors:
            print("Doctor ID already exists.")
            return False
        d = Doctor(name, specialization, doctor_id)
        self.doctors[doctor_id] = d
        self.save()
        return True

    def search_doctor(self, did):
        return self.doctors.get(did)

    def display_doctors(self):
        if not self.doctors:
            print("No doctors recorded.")
            return
        print("\n--- Doctors ---")
        for d in self.doctors.values():
            print(d)
        print()

    # Assign doctor
    def assign_doctor(self, pid, did):
        if pid not in self.patients:
            print("Patient not found.")
            return False
        if did not in self.doctors:
            print("Doctor not found.")
            return False
        self.assignments[pid] = did
        self.save()
        return True

    def borrowed_list_like(self):
        return [f"{pid} -> {did}" for pid, did in self.assignments.items()]


# -----------------------
# Menu System (CLI)
# -----------------------
def get_nonempty(prompt):
    while True:
        v = input(prompt).strip()
        if v:
            return v
        print("Input cannot be empty!")


def main_menu():
    hm = HospitalManagement()
    while True:
        print("\n====== HOSPITAL MENU ======")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Assign Doctor to Patient")
        print("4. Search Patient")
        print("5. Search Doctor")
        print("6. View All Patients")
        print("7. View All Doctors")
        print("8. Discharge Patient")
        print("9. View Assignments")
        print("0. Exit")
        print("===========================\n")

        ch = input("Enter choice: ")

        if ch == "1":
            ok = hm.add_patient(get_nonempty("Name: "), int(get_nonempty("Age: ")),
                                get_nonempty("Patient ID: "), get_nonempty("Disease: "))
            print("Patient added." if ok else "Failed.")

        elif ch == "2":
            ok = hm.add_doctor(get_nonempty("Name: "), get_nonempty("Specialization: "),
                               get_nonempty("Doctor ID: "))
            print("Doctor added." if ok else "Failed.")

        elif ch == "3":
            if hm.assign_doctor(get_nonempty("Patient ID: "), get_nonempty("Doctor ID: ")):
                print("Doctor assigned.")

        elif ch == "4":
            p = hm.search_patient(get_nonempty("Patient ID: "))
            print(p if p else "Not found.")

        elif ch == "5":
            d = hm.search_doctor(get_nonempty("Doctor ID: "))
            print(d if d else "Not found.")

        elif ch == "6":
            hm.display_patients()

        elif ch == "7":
            hm.display_doctors()

        elif ch == "8":
            if hm.discharge_patient(get_nonempty("Patient ID: ")):
                print("Patient discharged.")

        elif ch == "9":
            lst = hm.borrowed_list_like()
            print("Assignments:", lst if lst else "None")

        elif ch == "0":
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main_menu()
