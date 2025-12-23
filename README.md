# mobile-QA-Multi-Agent
QualGent Research Intern Coding Challenge
This project is my solution to the QualGent Mobile QA Multi‑Agent Challenge. It uses a Supervisor–Planner–Executor agent system to run natural‑language QA tests on the Obsidian Android app. The agents plan actions, execute ADB commands on a real device, and report whether each test passes or fails. I chose Google’s Agent Development Kit (ADK) for its clean multi‑agent structure and easy tool integration. The repository includes the Part 2 decision memo, the test cases, and the code for running the automated tests.

Challenge Tasks:
Part 1 — Environment Setup
  -Set up everything needed to run mobile automation:

  -Install Android Studio

  -Create an Android Virtual Device (or use a real device)

  -Install the Obsidian APK

Part 2 — Framework Analysis
Choose the best agent framework for building the multi‑agent system:

  -Read Part 3 to understand the requirements

  -Compare frameworks (e.g., Agent S3 vs Google ADK)

  -Write a short decision memo explaining which one you chose and why

Part 3 — Multi‑Agent Implementation
Build the actual automation system:

  -Create three agents: Supervisor, Planner, Executor

  -Give them natural‑language test cases

  -Use ADB commands to interact with the Obsidian app

  -Run both passing and failing tests

  -Supervisor reports Pass/Fail with reasoning
