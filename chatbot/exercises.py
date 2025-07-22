import time

def guided_breathing_exercise():
    """
    A simple, text-based guided breathing exercise.
    """
    print("\nLet's try a simple breathing exercise to help you relax.")
    print("We'll do a cycle of 4 breaths.")
    time.sleep(2)
    for i in range(1, 5):
        print(f"\n--- Cycle {i} of 4 ---")
        print("Breathe in deeply through your nose... (4 seconds)")
        time.sleep(4)
        print("Hold your breath... (4 seconds)")
        time.sleep(4)
        print("Now, exhale slowly through your mouth... (6 seconds)")
        time.sleep(6)
    print("\nWell done. I hope you're feeling a bit calmer.")
    time.sleep(2)