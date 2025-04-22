# Africa Agile Hackathon Team 3 - DSML Team

## Project Overview
This project is part of the Africa Agile Hackathon, developed by Team 3 of the DSML (Data Science and Machine Learning) team. The project focuses on creating solutions for language detection, text-to-speech conversion, and chatbot functionalities to address specific challenges.

## Directory Structure
The project is organized into the following directories:

### Chatbot
Contains resources and models for building a chatbot system:
- **Data ~ Original/**: Original datasets for training the chatbot.
- **Data ~ Translated/**: Translated datasets for multilingual support.
- **Model ~ Examples/**: Example models for chatbot implementation.

#### Key Files:
- **Chatbot/Chat/chat.js**:
  - Implements a simple AngularJS-based chatbot interface.
  - Contains a `MessageCtrl` controller that manages a list of predefined messages from users like "George Clooney" and "Seth Rogen."
  - This is a basic implementation and can be extended to integrate with a backend for dynamic responses.

- **Chatbot/Chat/chat.html**:
  - Provides the HTML structure for the chatbot interface.
  - Includes Bootstrap for styling and a footer with copyright information.
  - Contains placeholders for integrating translation and backend interaction.

---

### Frontend
Includes frontend resources for user interaction:
- Various `.zip` files representing different UI components, such as:
  - Homepage
  - Incident reporting forms
  - Success screens

#### Key Files:
- **Frontend/Homepage/homepage_style.css**:
  - Defines the styles for the homepage, including layout, typography, and buttons.
  - Uses the `Marko One` font and includes various sections like "Get Help Immediately" and "Join the Club."

- **Frontend/Are you the victim or Are you a witness/style.css**:
  - Styles the "Are you the victim or Are you a witness?" page.
  - Includes absolute positioning for elements like buttons and text fields.

- **Frontend/successful/style.css**:
  - Styles the "Success" page displayed after a user completes an action.
  - Includes elements like `.button4` and `.topnav` for navigation and interaction.

- **Frontend/WHAT KIND OF VIOLENCE WOULD YOU LIKE TO REPORT?/style.css**:
  - Styles the page for reporting violence.
  - Includes a footer and menu for navigation.

- **Frontend/Please give us more details about the incident/style.css**:
  - Styles the page for providing additional details about an incident.
  - Includes a `.reportcard` class for the main content area.

---

### Language Detection System
Contains documentation and resources for the language detection system:
- **LDS Methodology.docx**: Detailed methodology for language detection.

#### Key Files:
- **Language Detection System/Model/translator_sys_backend.js**:
  - A Node.js backend that uses Python scripts for language translation.
  - Accepts POST requests at `/translate` with `text` and `target_lang` parameters.
  - Spawns a Python process (`translate.py`) to perform the translation and returns the result to the client.

---

### Text-to-Speech
Resources for implementing text-to-speech functionality.

#### Key Files:
- **Text-to-Speech/text_to_speech_sys_backend.js**:
  - A Node.js backend that integrates with Streamlit to run a Python-based text-to-speech system.
  - Starts a Streamlit process to serve the `text_to_speech_sys.py` application.
  - Provides a `/streamlit` endpoint to trigger the Streamlit app.

---

## Key Features
- **Chatbot**: A conversational AI system to assist users.
- **Language Detection**: Automatically detects the language of input text and translates it into a target language.
- **Text-to-Speech**: Converts text into natural-sounding speech.
- **Frontend**: User-friendly interfaces for interaction.

## Getting Started
1. Clone the repository:
   ```sh
   git clone https://github.com/IsraaMohamedHamid/Africa_Agile_Hacakthon_Team3_DSML_Team.git
   ```
2. Navigate to the desired directory to explore specific components.

## License
This project is licensed under the terms specified in the [LICENSE](LICENSE) file.

## Contributors
Team 3 - DSML Team, Africa Agile Hackathon.

## Contact
For more information, please refer to the documentation files or contact the project team.