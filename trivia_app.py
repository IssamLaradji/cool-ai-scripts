"""
Trivia Game Application

This script creates an interactive trivia game with multiple choice questions
and generates relevant images for each question using AI.

Requires: HuggingFace API token for authentication and access to language models.
"""

import json
import random, shutil

from smolagents import Tool, MultiStepAgent, HfApiModel, LiteLLMModel
from huggingface_hub import login

# Load the config file and login to HuggingFace with token
with open("config.json", "r") as f:
    config = json.load(f)
    login(config["huggingface_api_key"])

MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.2"
# MODEL_ID = "mistralai/Mixtral-8x7B-Instruct-v0.1"

model = HfApiModel(model_id=MODEL_ID)
model = LiteLLMModel(
    model_id="gpt-4o-mini",  # Specify the model to use
    api_base="https://api.openai.com/v1",  # OpenAI API endpoint
    api_key="YOUR_API_KEY",
)

# Tool Definitions
image_generator = Tool.from_space(
    "black-forest-labs/FLUX.1-schnell",
    name="image_generator",
    description="Generate an image from a prompt",
)


def get_topic():
    """Get the topic of interest from the user"""
    return "vancouver"


def create_trivia_game():
    """Create and run the trivia game"""
    topic = get_topic()
    questions_history = []

    # Create question generator agent
    question_agent = MultiStepAgent(
        tools=[],
        max_steps=1,
        verbosity_level=0,
        model=model,
        system_prompt="""You are a knowledgeable trivia master.
        Generate an interesting and unique trivia question about the given topic.
        Consider the previous questions to avoid repetition.
        
        Your output should be just the question text, nothing else. 
        Format your output as follows:
        Question: "The question text"
        
        It should be an open ended question that can be answered with a single word or phrase. 
        Do not provide any options or choices.
        DO NOT PROVIDE THE ANSWER TO THE QUESTION.
        {{managed_agents_descriptions}}
        {{authorized_imports}}
        """,
    )

    # Create answer generator agent
    answer_agent = MultiStepAgent(
        tools=[],
        max_steps=1,
        verbosity_level=0,
        model=model,
        system_prompt="""You are a knowledgeable trivia expert.
        Provide the correct answer to the given question.
        
        Your output should be just the answer text, nothing else. 
        Format your output as follows:
        Answer: "The answer text"
        {{managed_agents_descriptions}}
        {{authorized_imports}}
        """,
    )

    # Create answer checker agent
    answer_checker = MultiStepAgent(
        tools=[],
        max_steps=1,
        verbosity_level=0,
        model=model,
        system_prompt="""You are a fair and precise trivia judge.
        Evaluate the user's answer to the question and provide a score from 0 to 100.
        
        {{managed_agents_descriptions}}
        {{authorized_imports}}
        """,
    )

    score = 0

    for i in range(3):
        # Generate question
        question = question_agent.run(
            f"Generate a trivia question about {topic}, do not provide the answer. Previous questions: {questions_history}"
        )
        questions_history.append(question)

        # Generate correct answer
        correct_answer = answer_agent.run(
            f"What is the correct answer to this question: {question}, provide the answer only"
        )

        # # Generate image
        def generate_image(prompt="a basic image"):
            image_generator = Tool.from_space(
                "black-forest-labs/FLUX.1-schnell",
                name="image_generator",
                description="Generate an image from a prompt",
            )

            image = image_generator(f"An image related to this question: {question}")

            # Move the image to the current directory
            shutil.move(image, "generated_image.png")
            print("Image generated successfully!")

        # Display question
        print(f"\nQuestion {i+1}:")
        print(question)

        # Get user's answer
        user_answer = input("\nYour answer: ")

        # Check answer using the checker agent
        check_result = answer_checker.run(
            f"""
            How good is my answer to this question: {question}
            My answer is: {user_answer}
            """
        )
        print(check_result)
    # Display final score
    print(f"\nGame Over! Your score: {score}/3")


if __name__ == "__main__":
    create_trivia_game()
