# 🎯 ATS Resume Expert

 **Smart Resume Analysis & Job Matching Tool**  
 Leverage the power of AI to optimize your resume for Applicant Tracking Systems and land your dream job!

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io)
[![Google AI](https://img.shields.io/badge/Google%20AI-Gemini%201.5-green.svg)](https://ai.google.dev)


## 🚀 What is ATS Resume Expert?

ATS Resume Expert is an intelligent web application that helps job seekers optimize their resumes for Applicant Tracking Systems (ATS). Using Google's powerful Gemini AI, it analyzes your resume against job descriptions and provides actionable insights to improve your chances of getting noticed by recruiters.

### ✨ Key Features

- **📊 Resume Analysis**: Get professional evaluation of your resume against specific job requirements
- **🎯 ATS Score**: Receive a percentage match score showing how well your resume aligns with the job description
- **💡 Skill Improvement**: Get personalized recommendations on how to enhance your skills and resume
- **🔍 Keyword Analysis**: Identify missing keywords that ATS systems look for
- **📱 User-Friendly Interface**: Clean, intuitive Streamlit interface for easy navigation

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI/ML**: Google Gemini 1.5 Flash
- **PDF Processing**: PyMuPDF (fitz)
- **Image Processing**: PIL (Pillow)
- **Environment Management**: python-dotenv

## 📋 Prerequisites

Before running this application, make sure you have:

- Python 3.8 or higher
- Google AI API key (from [Google AI Studio](https://ai.google.dev))
- Required packages (see installation section)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ats-resume-expert.git
   cd ats-resume-expert
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required packages**
   ```bash
   pip install streamlit google-generativeai PyMuPDF python-dotenv pillow pdf2image
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 🎮 How to Use

### Step 1: Launch the Application
- Run the Streamlit app and navigate to the local URL (usually `http://localhost:8501`)

### Step 2: Input Job Description
- Paste the job description for the position you're applying to in the text area

### Step 3: Upload Your Resume
- Upload your resume in PDF format using the file uploader

### Step 4: Choose Your Analysis
- Click on one of the three analysis options:

#### 📝 **"Tell Me About the Resume"**
- Get a comprehensive professional evaluation
- Understand strengths and weaknesses
- Receive HR manager perspective

#### 🚀 **"How Can I Improvise my Skills"**
- Get personalized skill improvement recommendations
- Learn what skills to develop
- Understand market demands

#### 📊 **"Percentage Match"**
- See your ATS compatibility score
- Identify missing keywords
- Get final recommendations

## 📁 Project Structure

```
ats-resume-expert/
├── app.py                 # Main Streamlit application
├── .env                   # Environment variables (create this)
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── .gitignore           # Git ignore rules
```

## 🔍 How It Works

1. **PDF Processing**: The app converts your PDF resume to an image using PyMuPDF
2. **AI Analysis**: Google Gemini 1.5 Flash analyzes the resume image against the job description
3. **Smart Evaluation**: The AI acts as an HR manager, ATS scanner, or career advisor based on your choice
4. **Actionable Insights**: Get specific, actionable feedback to improve your resume

## 🎯 Core Functions

### `get_gemini_response(input, pdf_content, prompt)`
- Interfaces with Google Gemini AI
- Processes resume image and job description
- Returns AI-generated analysis

### `input_pdf_setup(uploaded_file)`
- Converts PDF to processable image format
- Handles first page extraction
- Prepares data for AI analysis

## 🚀 Future Enhancements

- Multi-page PDF support
- Resume template suggestions
-  Industry-specific analysis
- Resume builder integration
- Batch processing for multiple resumes
- Export analysis reports
- Integration with job boards

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- Google AI for providing the Gemini API
- Streamlit for the amazing web framework
- PyMuPDF developers for PDF processing capabilities


---

