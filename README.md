# Agentic LinkedIn Poster

An automated LinkedIn posting system that helps you manage and schedule professional content on LinkedIn with ease.

## ✨ Features

- **Automated Posting**: Schedule and post content to LinkedIn automatically
- **Content Management**: Organize posts in different states (pending/approved/posted)
- **Trending Topics**: Automatically fetches trending topics for content generation
- **Approval Workflow**: Review and approve posts before they go live
- **Post Tracking**: Keep track of all posted content with timestamps

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd agentic-linkedin-poster
   ```

2. **Create and activate a virtual environment** (recommended)
   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuration

1. **Environment Variables**
   Create a `.env` file in the root directory with the following variables:
   ```
   OPENAI_API_KEY=your_openai_api_key
   LINKEDIN_ACCESS_TOKEN=your_linkedin_access_token
   ```

2. **Obtain API Keys**
   - Get your OpenAI API key from [OpenAI Platform](https://platform.openai.com/account/api-keys)
   - Generate a LinkedIn Access Token from [LinkedIn Developers](https://www.linkedin.com/developers/)

## 📁 Project Structure

```
agentic-linkedin-poster/
├── agent/                    # Core application modules
│   ├── google_trend_fetcher.py  # Fetches trending topics from Google
│   ├── planner.py            # Post scheduling logic
│   ├── post_approver.py      # Manages post approval workflow
│   ├── poster.py             # Handles LinkedIn API interactions
│   ├── researcher.py         # Researches content topics
│   ├── topic_fetcher.py      # Fetches trending topics
│   └── writer.py             # Generates post content using AI
├── memory/                   # Data storage
│   ├── approved/             # Approved posts ready for posting
│   ├── pending/              # Posts waiting for approval
│   └── posted/               # Successfully posted content
├── .env.example             # Example environment variables
├── .gitignore               # Git ignore file
├── main.py                  # Main application entry point
├── README.md                # This file
└── requirements.txt         # Project dependencies
```

## 🛠 Usage

### 1. Generate a New Post
```bash
python main.py generate
```
This will:
- Fetch a trending topic
- Generate a post using AI
- Save it to the pending directory for approval

### 2. Review and Approve Posts
1. Check the `memory/pending/` directory
2. Review the generated posts
3. To approve a post, rename it to include `.approved` before the file extension
   ```
   post_20230801_120000.txt -> post_20230801_120000.approved.txt
   ```

### 3. Post to LinkedIn
```bash
python main.py post
```
This will:
1. Find the next approved post
2. Publish it to LinkedIn
3. Move it to the `memory/posted/` directory
4. Mark the original file as posted by appending `.posted`

## 🔄 Workflow

1. **Content Generation**
   - The system generates posts based on trending topics
   - Posts are saved in `memory/pending/` for review

2. **Approval Process**
   - Review pending posts
   - Rename with `.approved` to mark for posting

3. **Publishing**
   - Approved posts are published to LinkedIn
   - Original files are marked with `.posted`
   - Copies are saved in `memory/posted/` with timestamps

## 🔒 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |
| `LINKEDIN_ACCESS_TOKEN` | LinkedIn OAuth token | Yes |

## 📦 Dependencies

- `openai` - For AI-powered content generation
- `requests` - For making HTTP requests
- `python-dotenv` - For managing environment variables
- `ddgs` - For fetching trending topics

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Made with ❤️ by Your Name
</p>
