# Image Content Analysis with CrewAI

This project demonstrates an AI-powered analysis system for restaurant management interfaces using CrewAI. It employs multiple AI agents working together to analyze, suggest improvements, and create user stories for UI/UX enhancement.

## Features

- Image content analysis
- Design improvement suggestions
- User story generation and prioritization
- Automated markdown report generation

## Technologies Used

- **Python 3.x**
- **CrewAI** - Framework for orchestrating multiple AI agents
- **OpenAI GPT-4** - Large Language Model for AI processing
- **Pillow (PIL)** - Image processing library
- **python-dotenv** - Environment variable management
- **IPython** - Interactive display capabilities

## Prerequisites

- Python 3.x installed
- OpenAI API key
- Required Python packages

## Setup

1. Clone the repository
2. Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
3. Install required packages:
   ```bash
   pip install crewai crewai_tools pillow python-dotenv
   ```

## Usage

1. Place your target image as `image1.png` in the project directory
2. Run the analysis:
   ```bash
   python main.py
   ```
3. Check the generated `output.md` file for results

## AI Agents

1. **Image Describer** - Analyzes and describes image content
2. **Design Improvement Agent** - Suggests UI/UX improvements
3. **Product Manager** - Creates and prioritizes user stories

## Output

The system generates a markdown file containing:

- Detailed image description
- Design improvement suggestions
- Prioritized user stories

## License

MIT License
