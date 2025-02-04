# Full Storyline Generator

## Overview
The Full Storyline Generator is a web-based application built with **Streamlit** that allows users to generate detailed, creative storylines based on provided inputs such as lore, plot twists, and character development. The application leverages the power of **LangChain** and a custom RAG (Retrieval-Augmented Generation) chain to create coherent and engaging narratives.

### Features:
- **Input Fields**: Users can provide inputs for **lore**, **plot twists**, and **character development**.
- **Story Generation**: Upon clicking a button, the app will combine these inputs and generate a full storyline.
- **Downloadable Story**: After generating the story, users can download the full storyline as a `.txt` file.

## How It Works:
1. **User Input**: Users input text for lore, plot twists, and character development into text areas.
2. **Story Generation**: After clicking the "Generate Full Story" button, the app processes these inputs and combines them into a cohesive narrative.
3. **Download**: The generated story can then be downloaded as a `.txt` file.

## Technologies Used:
- **Streamlit**: For creating the interactive web application.
- **LangChain**: For language model integration and prompt management.
- **Groq API**: Used in conjunction with LangChain to generate text-based stories based on the input.
- **pyttsx3** (Removed in this version): Initially used for text-to-speech, but has been excluded from the current version.

---

## Setup Instructions

### Requirements:
To run this application, you'll need to have the following dependencies installed:

1. **Python**: Version 3.8 or higher is recommended.

### Installation Steps:
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/full-storyline-generator.git
   cd full-storyline-generator
