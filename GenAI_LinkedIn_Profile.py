import openai
from openai import OpenAI
import os
os.environ['OPENAI_API_KEY'] = 'YOUR API KEY'

def linkedin_profile(long_cv: str) -> str:
    
    response = openai.responses.create(
        model = "gpt-4o",
        input = f"""
            you are a professional career assistant. 
            please write a professional and persuasive linkedin profile using the following 
            resume. Please emphasize relevant experience and skills. Use most current and 
            buzz worthy terminology from data analytics and AI job postings. 
            Keep the formatting professional. Please write the profile in a confident
            and enthusiastic tone.
            
            Resume:
            {long_cv}

            LinkedIn Profile:
            """,
        temperature=0.7
    )

    LinkedIn_Profile = response.output_text #['text']#[0]['message']['content']
    formatted_LinkedIn_Profile = LinkedIn_Profile.split('\n')
    return formatted_LinkedIn_Profile

    if __name__ == "__main__":    
        resume = """

        John Doe
        Software Engineer with 5 years of experience in web development, proficient in Python, JavaScript, and SQL. Worked at XYZ Corp and led a team of developers to build scalable backend systems.
        """

# To call the function:

# load a string with variable name 'long_cv' similar to the resume variable above
# e.g.,

# long_cv = """

# John Doe
# Software Engineer with 5 years of experience in web development ...
# """

# Run the cell

LinkedIn = linkedin_profile(long_cv)
for sentence in LinkedIn:
    print(sentence)

# Output will print in a copy/paste friendly format

# Tweak the prompt to further customize the output
