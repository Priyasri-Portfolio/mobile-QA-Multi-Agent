# -*- coding: utf-8 -*-
#The manager
from agents import supervisor
import time

def run_test():
    # Load the test cases from the text file
    try:
        with open("test_cases.txt", "r") as f:
            test_cases = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("Error: test_cases.txt not found!")
        return

    print(f"Starting Multi-Agent Test Suite: {len(test_cases)} cases found.")

    # Run each test and catch errors so the script doesn't stop
    for i, test in enumerate(test_cases, 1):
        print(f"\n--- RUNNING TEST {i} ---")
        try:
            # Send the test case to the AI brain
            result = supervisor.run(test)
            print(f"RESULT: {result}")
        except Exception as e:
            # If a test fails (like a Quota error), print it and move to next
            print(f"Test {i} failed with error: {str(e)}")
            print("Cooling down for 30 seconds...")
            time.sleep(30) # Pause before trying next case

if __name__ == "__main__":
    run_test()