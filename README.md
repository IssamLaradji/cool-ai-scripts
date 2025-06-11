# 🎥 YouTube RAG Chat Application

A powerful Retrieval-Augmented Generation (RAG) system that lets you chat with YouTube video content using AI. Extract transcripts from YouTube videos, create a searchable knowledge base, and ask questions about the video content through an intuitive web interface.

## ✨ Features

- **YouTube Video Processing**: Automatically extract transcripts from YouTube videos
- **Smart Chunking**: Intelligently split video transcripts into overlapping chunks for better context
- **Vector Search**: Use FAISS for fast semantic search across video content
- **AI-Powered Chat**: Ask questions and get contextual answers using Llama 3 via Together AI
- **Beautiful Web Interface**: Clean, modern Gradio interface with real-time chat
- **Source Citations**: Automatically cite which videos information comes from
- **Multi-Video Support**: Add multiple videos and ask comparative questions

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Together AI API key (get one at [together.ai](https://together.ai))

### Installation

1. **Clone or download the repository**
```bash
git clone <repository-url>
cd cool-ai-scripts
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python rag.py -k YOUR_TOGETHER_API_KEY
```

4. **Open your browser** to `http://localhost:7860`

### Usage

1. **Add YouTube Videos**: 
   - Paste YouTube URLs in the left panel
   - Click "Add Video" to process the transcript
   - Wait for processing to complete

2. **Start Chatting**:
   - Ask questions about the video content
   - Get AI-powered answers with source citations
   - Ask comparative questions across multiple videos

### Example Questions

- "What are the main points discussed in the video?"
- "Summarize the key takeaways"
- "What did they say about machine learning?"
- "Compare the opinions from different videos"
- "Give me specific quotes about artificial intelligence"

## 🛠️ Technical Details

### Architecture

- **Frontend**: Gradio web interface
- **Backend**: Python with FastAPI-style async processing
- **Vector Database**: FAISS for similarity search
- **Embeddings**: SentenceTransformers (all-MiniLM-L6-v2)
- **LLM**: Meta Llama 3 8B via Together AI API
- **Video Processing**: yt-dlp for metadata, youtube-transcript-api for transcripts

### How it Works

1. **Video Processing**: Extract video ID, fetch metadata and transcripts
2. **Text Chunking**: Split transcripts into overlapping chunks (500 words, 50 word overlap)
3. **Embedding Creation**: Generate vector embeddings for each chunk
4. **Vector Storage**: Store embeddings in FAISS index for fast retrieval
5. **Query Processing**: Convert user questions to embeddings and find similar chunks
6. **Response Generation**: Use retrieved context to generate informed AI responses

### Configuration Options

```bash
python rag.py -k YOUR_API_KEY [OPTIONS]

Options:
  -k, --api_key          Together AI API key (required)
  --embedding_model      Embedding model name (default: all-MiniLM-L6-v2)
  --share               Create shareable Gradio link
  -h, --help            Show help message
```

## 📋 Requirements

See `requirements.txt` for full dependency list. Key requirements:

- `gradio>=4.0.0` - Web interface
- `together>=0.2.0` - AI API integration  
- `youtube-transcript-api>=0.6.0` - YouTube transcript extraction
- `yt-dlp>=2023.1.0` - YouTube metadata extraction
- `faiss-cpu>=1.7.0` - Vector similarity search
- `sentence-transformers>=2.2.0` - Text embeddings
- `nltk>=3.8` - Text processing

## ⚠️ Limitations

- Only works with YouTube videos that have available transcripts/captions
- Requires active internet connection for video processing
- Processing time depends on video length and transcript availability
- Together AI API usage limits apply

## 🔧 Troubleshooting

### Common Issues

1. **"Could not get transcript" error**:
   - Video doesn't have captions/transcripts available
   - Try videos with auto-generated or manual captions

2. **API Key errors**:
   - Ensure your Together AI API key is valid
   - Check API usage limits

3. **Installation issues**:
   - Use Python 3.8 or higher
   - Install in a virtual environment if needed

### Debug Mode

Run with verbose output:
```bash
python rag.py -k YOUR_API_KEY --debug
```

## 🤝 Contributing

Contributions welcome! Areas for improvement:

- Support for other video platforms
- Better chunking strategies
- Additional embedding models
- Enhanced UI features
- Batch video processing

## 📄 License

See LICENSE file for details.

## 🙏 Acknowledgments

- [Together AI](https://together.ai) for LLM API
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api) for transcript extraction
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for YouTube metadata
- [FAISS](https://github.com/facebookresearch/faiss) for vector search
- [Gradio](https://gradio.app) for the web interface