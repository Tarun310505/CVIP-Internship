class AppointmentScheduler:
    def __init__(self):
        self.appointments = {}
    
    def schedule_appointment(self, date, time, patient_name):
        if (date, time) in self.appointments:
            print("This time slot is already taken.")
        else:
            self.appointments[(date, time)] = patient_name
            print(f"Appointment scheduled for {patient_name} on {date} at {time}.")
    
    def view_appointments(self):
        if not self.appointments:
            print("No appointments scheduled.")
        else:
            for (date, time), patient_name in self.appointments.items():
                print(f"Date: {date}, Time: {time}, Patient: {patient_name}")
    
    def cancel_appointment(self, date, time):
        if (date, time) in self.appointments:
            del self.appointments[(date, time)]
            print(f"Appointment on {date} at {time} has been canceled.")
        else:
            print("No appointment found at the given time.")

def main():
    scheduler = AppointmentScheduler()
    
    while True:
        print("\nAppointment Scheduler")
        print("1. Schedule an appointment")
        print("2. View appointments")
        print("3. Cancel an appointment")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            patient_name = input("Enter patient name: ")
            scheduler.schedule_appointment(date, time, patient_name)
        elif choice == '2':
            scheduler.view_appointments()
        elif choice == '3':
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            scheduler.cancel_appointment(date, time)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
