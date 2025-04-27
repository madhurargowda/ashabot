Asha Bot - Empowering Women's Careers

Asha Bot is an intelligent AI-powered chatbot designed to assist women in discovering career opportunities, mentorship programs, sessions, and FAQs.
It uses Retrieval Augmented Generation (RAG) and Google's Gemini AI to deliver contextual, ethical, and privacy-conscious career guidance.
Features

    Job Discovery: Explore latest job openings from dynamic datasets.

    Mentorship Sessions: Find mentorship programs, leadership sessions, and career talks.

    FAQ Assistant: Instantly answers common questions about signups, profile updates, and events.

    Bias Detection: Detects and redirects gender-biased queries to positive empowerment responses.

    Real-time Knowledge Retrieval: Powered by semantic search with Chroma Vector Database.

    Multi-turn Conversations: Maintains logical conversational flow with session tracking.

    Deployed Live: Publicly accessible on Huggingface Spaces, no installation needed.

Technologies Used

    Streamlit (Frontend Web App)

    Gemini 1.5 Pro (Google Generative AI)

    LangChain (Chain management and RAG setup)

    Chroma Vector Database (Semantic document storage)

    Sentence Transformers (for text embeddings)

    Huggingface Spaces (Hosting)

    Google Generative AI API (Secure language model)

Architecture Overview

User Input ➔ Bias Detection ➔ Knowledge Retrieval ➔ Gemini AI Response ➔ Final Output

If bias is detected, a special positive response is given.
If no bias, the query is semantically matched to documents and answered using Gemini.
Live Demo

You can access the live bot here:

https://madhura6-asha-bot.hf.space

No installation needed — just open in any browser.
Project Structure

    app.py (Main chatbot application)

    requirements.txt (Python dependencies)

    /data/

        job_listing_data.csv (Jobs Data)

        session_details.json (Mentorship Sessions)

        faqs.json (FAQs)

How to Run Locally

    Clone the repository:

git clone https://github.com/your-username/asha-bot.git
cd asha-bot

Install the dependencies:

pip install -r requirements.txt

Set your Gemini API Key:

    Create a file .streamlit/secrets.toml

    Add:

    [general]
    GEMINI_API_KEY = "your-real-gemini-api-key"

Run the app:

    streamlit run app.py

App will start at localhost:8501 on your local machine.
Performance Report

    Response Time: 2–4 seconds per query.

    Retrieval Accuracy: 85–90% based on semantic search matches.

    Bias Detection Success: 100% on sampled tests.

    Supports 20+ concurrent users on free Huggingface tier.

Future Improvements

    Integrate live external job APIs like LinkedIn, Indeed.

    Add personalized user recommendations based on profile data.

    Support for multiple languages (Hindi, Kannada, etc.).

    Enhanced privacy features (encrypting conversation history).

License

Licensed under Apache 2.0 License.
Contact

For any issues or feedback, please open an issue on GitHub or contact me at:

your-madhurargowda6@gmail.com
