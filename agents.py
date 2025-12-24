# -*- coding: utf-8 -*-
#intelligence
import time
from google import genai
import tools

#This class creates an 'Agent' thta can talk to Google Gemini AI

class SimpleAgent:
    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions
        #This is the API key used to talk to the google
		#I used My_API_KEY instead of my original API KEY- I didn't want that to be public
        self.api_key = "My_API_KEY"
        self.client = genai.Client(api_key=self.api_key)

    def run(self, task):
        # we wait for 5 seconds to communicate with the server
        time.sleep(5) 
        print(f"--- AI: {self.name} is thinking... ---")
        
		#we send the task and the rules to the AI
        response = self.client.models.generate_content(
            model="gemini-1.5-flash",
            contents=self.instructions + "\n\nTask: " + task
        )
        return response.text

# --- ADD THIS PART BELOW ---
# the purpose of this Supervisor class is to manage the workflow between different AI agents
class Supervisor:
    def run(self, test_case):
        # 1.Planner agent creates a list of steps to follow
        planner = SimpleAgent("Planner", "You are a mobile QA planner. Create a step-by-step plan.")
        plan = planner.run(test_case)
        print(f"PLAN:\n{plan}")
        
        # 2.take a screenshot of your phone, so AI can see it
        print("\nCapturing device screen...")
        tools.get_screenshot() 
        
        # 3.Executor Agent looks at the plan and the photo to give the final answer
        executor = SimpleAgent("Executor", "You are a mobile QA executor. Decide the next ADB command.")
        result = executor.run("Follow this plan: " + plan)
        return result
#create one supervisor for the main scipt to use
supervisor = Supervisor()
