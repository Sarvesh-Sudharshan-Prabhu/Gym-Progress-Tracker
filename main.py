def display_interface():
    print("Gym Progress Tracker")
    print("1. Add a new workout")
    print("2. View workout history")
    print("3. Exit")

def main():
    while (True):
        display_interface()
        choice = input("Enter your choice: ")
        if (choice == "1"):
            workout = log_workout()
            print("Workout logged:", workout)
            
        elif choice == "2":
            print("View workout history")
            
        elif choice == "3":
            print("Goodbye!")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() #Basically executes the program when the file is run directly.

def log_workout():
    exercise = input("Enter exercise name: ")
    weight = float(input("Enter weight in lbs: "))
    sets = int(input("Enter number of sets: "))
    reps = int(input("Enter number of reps: "))

    workout = {
        "exercise": exercise,
        "weight": weight,
        "sets": sets,
        "reps": reps
    }

    return workout
