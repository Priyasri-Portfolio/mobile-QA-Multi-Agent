Priyasri Sankaran
Date: December 23,2025
Project: QualGent Mobile QA Multi-Agent System

Recommendation : Google Agent Development Kit (ADK)
After analyzing Part 3 requirements for building a Supervisor-Planner-Executor system for mobile QA automation, I recommend Google ADK as the optimal framework. The project explicitly requires three distinct agents with separate roles, and ADK natively supports this multi-agent orchestration pattern.
Part 3 Requirements Analysis
The project requires three distinct agent roles:
•	Planner: Analyzes test case + current state→ decides next action
•	Executor: Takes planned action → executes via ADB commands
•	Supervisor: Verifies state transitions → logs Pass/Fail, distinguishing execution failures from assertion failures
Critical evaluation criteria include accurate reporting, reasoning loops that distinguish "failed step" (execution error) vs "failed assertion" (test expectation mismatch), distinct prompt engineering for each agent, and modular code with easy LLM swapping.
Reasoning:
ADK:
•	ADK supports building applications by composing multiple distinct BaseAgent instances into a Multi-Agent System where agents collaborate in a hierarchy to achieve larger goals.
•	Supervisor-Planner-Executor Pattern: ADK documentation explicitly shows workflows where Supervisor delegates to LoopAgent that orchestrates step-by-step execution, with Planner generating next action and Executor performing it.
•	State Management: Agents share Session object via InvocationContext, allowing Planner to pass actions to Executor, and Executor to pass results to Supervisor. The output_key property automatically saves responses to shared state.
•	LLM-Agnostic Design: Model-agnostic architecture with BaseLLM interface enables easy swapping 
•	Custom Tool Integration: Supports pre-built tools, custom functions, and 3rd-party libraries, perfect for building ADB command tools (tap, swipe, screenshot, text input).

Agent S3: Does not support requirements
•	Single Unified Agent: Agent S3 streamlined by removing hierarchical manager 
•	No Orchestration Framework: Lacks built-in support for coordinating multiple agents 
•	Complex Setup: Requires OSWorld infrastructure for GUI automation. To implement Supervisor-Planner-Executor with Agent S3, you would build custom multi-agent system from scratch, defeating the purpose of using a framework.
