# Pentecost University RAG Knowledge Assistant - Project Portfolio

## Executive Summary

This project is an advanced **Retrieval-Augmented Generation (RAG)** application designed specifically for Pentecost University. It provides an intelligent, AI-powered knowledge assistant that allows students, staff, and administrators to interact with university documents through a natural language chat interface. The system leverages OpenAI's state-of-the-art language models and vector search technology to deliver accurate, contextual answers grounded in official university documentation.

**Key Achievement**: Successfully implemented a production-ready RAG system that makes institutional knowledge accessible, searchable, and interactive through conversational AI.

---

## 🎯 Project Overview

### What is RAG (Retrieval-Augmented Generation)?

RAG is a cutting-edge AI architecture that combines two powerful capabilities:

1. **Retrieval**: Intelligent search through a document collection to find relevant information
2. **Generation**: Using Large Language Models (LLMs) to craft coherent, accurate answers based on retrieved content

This approach significantly reduces AI hallucinations by grounding responses in actual documents, making the system reliable for institutional use.

### Purpose and Use Cases

The Pentecost University RAG Knowledge Assistant serves multiple purposes:

- **Student Support**: Quick access to university statutes, policies, and academic information
- **Administrative Efficiency**: Staff can instantly query institutional documents
- **Knowledge Democratization**: Makes university information accessible to all stakeholders
- **24/7 Availability**: Provides instant answers without waiting for human support
- **Scalable Information Retrieval**: Handles multiple simultaneous users querying large document collections

---

## 🏗️ Architecture and Technical Implementation

### System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    User Interface                        │
│              (Streamlit Web Application)                 │
└───────────────────┬─────────────────────────────────────┘
                    │
                    ├─ User queries in natural language
                    │
┌───────────────────▼─────────────────────────────────────┐
│              OpenAI Assistants API                       │
│         (GPT-4o-mini / GPT-3.5-turbo)                   │
└───────────────────┬─────────────────────────────────────┘
                    │
                    ├─ file_search tool invocation
                    │
┌───────────────────▼─────────────────────────────────────┐
│           OpenAI Vector Stores                           │
│    (Document embeddings + semantic search)               │
└───────────────────┬─────────────────────────────────────┘
                    │
                    ├─ Retrieves relevant passages
                    │
┌───────────────────▼─────────────────────────────────────┐
│          Response Generation                             │
│  (Contextual answer with source citations)               │
└──────────────────────────────────────────────────────────┘
```

### Technology Stack

**Frontend & Application Framework:**
- **Streamlit** (v1.53.0): Modern Python web framework for rapid application development
- Custom CSS for professional, university-branded UI/UX

**AI & Machine Learning:**
- **OpenAI API**: Provides LLM capabilities and vector search
  - GPT-4o-mini: Cost-effective, high-quality language model
  - GPT-3.5-turbo: Fast, efficient fallback option
  - text-embedding-3-small: Document embedding model
- **OpenAI Assistants API**: Orchestrates conversation flow and tool usage
- **Vector Stores**: Manages document indexing and semantic search

**Backend & Infrastructure:**
- **Python 3.x**: Core programming language
- **python-dotenv**: Environment configuration management
- **OpenAI Python SDK**: Official API client library

**Data Processing:**
- **NumPy**: Numerical computing
- **Pandas**: Data manipulation and analysis
- **scikit-learn**: Machine learning utilities

**Visualization:**
- **Matplotlib**: Data visualization
- **Altair**: Declarative statistical visualizations

### Data Flow and Processing

1. **Document Ingestion**:
   - Documents are uploaded to OpenAI Vector Stores
   - Each document is automatically chunked and embedded
   - Metadata is attached (title, version, classification, source URLs)
   
2. **Query Processing**:
   - User submits natural language question
   - Query is sent to OpenAI Assistant
   - Assistant invokes `file_search` tool
   - Vector store performs semantic similarity search
   - Relevant document chunks are retrieved

3. **Response Generation**:
   - Retrieved passages are provided as context to LLM
   - LLM generates coherent answer based on context
   - System extracts citations and source references
   - Response includes links to source documents

4. **Session Management**:
   - Each conversation maintains a thread for context continuity
   - Session state persists across interactions
   - Users can switch between knowledge bases without losing context

---

## ✨ Key Features and Capabilities

### Core Functionality

1. **Multi-Knowledge Base Support**
   - Select from multiple document collections
   - Dedicated vector stores for different topics
   - Easy switching between knowledge bases

2. **Intelligent Conversational Interface**
   - Natural language question answering
   - Context-aware follow-up questions
   - Conversation history maintained throughout session

3. **Source Citations and Verification**
   - Every answer includes source references
   - Direct links to original documents
   - "View Source" functionality for transparency

4. **User Access Control**
   - Guest mode with daily query limits (25 queries/day)
   - Admin mode with unlimited access
   - Guest identification for usage tracking

5. **Document Management**
   - View files in current knowledge base
   - File type indicators (PDF, DOCX, etc.)
   - Document metadata display

6. **Smart Suggestions**
   - Pre-configured question templates
   - Context-appropriate prompts
   - Guides users to effective queries

### Advanced Features

1. **Automatic Link Detection**
   - Recognizes when users ask for document links
   - Returns comprehensive list of source documents
   - Handles various phrasings ("links", "URLs", "sources", etc.)

2. **Model Fallback Logic**
   - Automatically selects compatible models
   - Graceful degradation if preferred model unavailable
   - Cost optimization through model selection

3. **Flexible Configuration**
   - Environment-based configuration (.env)
   - Streamlit secrets integration for cloud deployment
   - Multiple configuration paths for different environments

4. **Rich UI/UX**
   - Custom CSS with university branding
   - Dark mode optimized design
   - Responsive layout for various screen sizes
   - Professional color scheme and typography

5. **Error Handling and Recovery**
   - Graceful error messages
   - Automatic retry mechanisms
   - Clear user guidance on issues

---

## 📂 Repository Structure

```
RAG_PU/
├── streamlit_app.py           # Main Streamlit application (931 lines)
├── requirements.txt           # Python dependencies
├── README.md                  # Comprehensive technical documentation
├── PROJECT_PORTFOLIO.md       # This portfolio document (you are here)
├── LICENSE                    # Project license
│
├── scripts/                   # Utility scripts for vector store management
│   ├── creating_vector_store.py          # Create/retrieve vector stores
│   ├── uploading_file_toVS.py            # Upload documents with metadata
│   ├── clear_files_inVS.py               # Remove all files from store
│   ├── checking_no_files_attached.py     # Verify file attachments
│   └── check_no_ofVS.py                  # List available vector stores
│
├── notebooks/                 # Jupyter notebooks for development
│   └── openai_1.ipynb         # Interactive vector store management
│
├── pu_repo/                   # Document repository (knowledge base)
│   └── [university documents] # PDF, DOCX, and other document files
│
├── .streamlit/                # Streamlit configuration
│
└── .github/
    └── workflows/
        └── ping-streamlit.yml # CI/CD workflow
```

### File Descriptions

**streamlit_app.py**: The core application implementing:
- User authentication (guest/admin)
- Vector store selection and management
- Chat interface and message handling
- OpenAI API integration
- Session state management
- UI rendering and styling

**scripts/**: Helper utilities for:
- Creating and managing vector stores
- Uploading documents with rich metadata
- Clearing and refreshing document collections
- Verifying system state

**notebooks/**: Interactive development environment for:
- Experimenting with OpenAI API
- Managing vector stores
- Testing document uploads
- Debugging and troubleshooting

---

## 🚀 Setup and Installation

### Prerequisites

- Python 3.8 or higher
- OpenAI API account with credits
- Git for version control

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/hatieku-boateng-pu/RAG_PU.git
   cd RAG_PU
   ```

2. **Create Virtual Environment**
   ```bash
   # Windows
   python -m venv .venv
   .\.venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   
   Create a `.env` file in the project root:
   ```env
   # Required
   OPENAI_API_KEY=sk-your-api-key-here
   
   # Optional
   OPENAI_MODEL=gpt-4o-mini
   OPENAI_MODEL_EMBEDDING=text-embedding-3-small
   VECTOR_STORE_ID=vs-your-vector-store-id
   ADMIN_PASSWORD=your-secure-password
   
   # Document Metadata (optional)
   DOCUMENT_VERSION=1.0
   DOCUMENT_SOURCE=pu_repo
   VIEW_SOURCE_URL=https://your-document-url.com
   ```

5. **Prepare Knowledge Base**
   
   Use the notebook or scripts to create vector stores:
   ```bash
   # Create/retrieve vector store
   python scripts/creating_vector_store.py
   
   # Upload documents
   python scripts/uploading_file_toVS.py
   ```

6. **Run the Application**
   ```bash
   streamlit run streamlit_app.py
   ```

7. **Access the Application**
   
   Open your browser to the URL shown (typically `http://localhost:8501`)

---

## 💡 Usage Guide

### For End Users

1. **Select Access Mode**
   - Choose "Guest" for limited daily access (25 queries)
   - Choose "Admin" for unlimited access (requires password)

2. **Select Knowledge Base**
   - Use sidebar to choose from available document collections
   - View file list to see what's in each knowledge base

3. **Ask Questions**
   - Type questions in natural language
   - Use suggested questions for inspiration
   - Ask follow-up questions for deeper understanding

4. **Review Answers**
   - Read AI-generated response
   - Check source citations for verification
   - Click "View Source" links to access original documents

5. **Request Document Links**
   - Ask: "Can you give me the document links?"
   - System provides complete list of available sources

### For Administrators

1. **Manage Vector Stores**
   ```bash
   # List existing stores
   python scripts/check_no_ofVS.py
   
   # Create new store
   python scripts/creating_vector_store.py
   
   # Check files in store
   python scripts/checking_no_files_attached.py
   ```

2. **Upload Documents**
   ```bash
   # Upload all files from pu_repo/
   python scripts/uploading_file_toVS.py
   ```

3. **Refresh Content**
   ```bash
   # Clear existing files
   python scripts/clear_files_inVS.py
   
   # Re-upload updated documents
   python scripts/uploading_file_toVS.py
   ```

4. **Monitor Usage**
   - Track guest query counts
   - Review conversation logs
   - Monitor API costs in OpenAI dashboard

---

## 🔧 Configuration and Customization

### Environment Variables

**Required:**
- `OPENAI_API_KEY`: Your OpenAI API key

**Optional:**
- `OPENAI_MODEL`: Default model (gpt-4o-mini, gpt-3.5-turbo, etc.)
- `OPENAI_MODEL_EMBEDDING`: Embedding model for vector search
- `VECTOR_STORE_ID`: Specific vector store to use
- `ADMIN_PASSWORD`: Password for admin access
- `DOCUMENT_VERSION`: Version metadata for uploaded docs
- `DOCUMENT_SOURCE`: Source system/repository name
- `VIEW_SOURCE_URL`: Base URL for document viewing
- `DOCUMENT_CLASSIFICATION`: Access level (public/student/staff/admin)

### Model Selection

The system supports multiple OpenAI models:
- **gpt-4o**: Most capable, highest cost
- **gpt-4o-mini**: Balanced performance and cost (recommended)
- **gpt-4-turbo**: Fast, capable predecessor
- **gpt-3.5-turbo**: Cost-effective, lower capability

**Cost Optimization Tips:**
- Use gpt-4o-mini for most use cases
- Reserve gpt-4o for complex queries requiring higher reasoning
- Monitor token usage in OpenAI dashboard
- Set query limits for guest users

### UI Customization

The application uses custom CSS for branding. Key variables in `streamlit_app.py`:

```css
--brand: #0b3d91;        /* Primary brand color */
--brand-2: #0a2a63;      /* Secondary brand color */
--accent: #f5b301;       /* Accent color (gold) */
--bg: #020617;           /* Background */
--text: #e5e7eb;         /* Text color */
```

Modify these in the `st.markdown()` CSS section to match your branding.

---

## 🎓 Use Cases and Impact

### Educational Applications

1. **Student Support**
   - Quick answers to policy questions
   - Course information retrieval
   - Academic regulation clarification
   - Statute and guideline lookup

2. **Faculty Assistance**
   - Teaching policy reference
   - Academic calendar queries
   - Administrative procedure lookup

3. **Administrative Efficiency**
   - Fast policy verification
   - Consistent information dissemination
   - Reduced support ticket volume

### Business Value

**Quantifiable Benefits:**
- **Time Savings**: Reduces information lookup time from minutes to seconds
- **Scalability**: Handles unlimited simultaneous queries
- **Consistency**: Provides accurate, standardized answers
- **Accessibility**: 24/7 availability without human intervention
- **Cost Efficiency**: Reduces burden on support staff

**Strategic Advantages:**
- Modern, AI-powered university infrastructure
- Enhanced student and staff experience
- Data-driven insights into common queries
- Foundation for future AI initiatives

---

## 🔒 Security and Privacy

### Data Protection

1. **API Key Security**
   - Never commit `.env` files to version control
   - Use environment variables or secrets management
   - Rotate keys regularly
   - Monitor for unauthorized access

2. **Document Handling**
   - Documents are sent to OpenAI for processing
   - Data subject to OpenAI's data usage policies
   - Consider data classification before upload
   - Use appropriate access controls

3. **User Privacy**
   - Guest IDs tracked for quota management only
   - No personal information collected beyond guest ID
   - Conversation history not persisted between sessions
   - Admin mode requires password authentication

### Best Practices

- Review OpenAI's data usage and retention policies
- Classify documents before uploading (public/internal)
- Implement proper access controls for sensitive documents
- Regular security audits of environment configuration
- Monitor API usage for anomalies

---

## 📊 Performance and Scalability

### Current Performance

- **Response Time**: 2-5 seconds average for typical queries
- **Concurrent Users**: Supports multiple simultaneous users via Streamlit
- **Document Capacity**: Tested with 100+ documents per vector store
- **Query Throughput**: Limited by OpenAI API rate limits

### Optimization Strategies

1. **Caching**
   - Vector store data cached with 60-second TTL
   - Reduces API calls for frequently accessed metadata
   - Streamlit's built-in caching for expensive operations

2. **Model Selection**
   - Use cost-effective models (gpt-4o-mini)
   - Automatic fallback to supported models
   - Balance between quality and cost

3. **Rate Limiting**
   - Guest users limited to 25 queries/day
   - Prevents abuse and controls costs
   - Tracks usage per guest ID per day

### Scalability Considerations

**Current Limitations:**
- Single Streamlit instance (can be scaled horizontally)
- OpenAI API rate limits apply
- Cost scales with usage

**Future Scaling Options:**
- Deploy on cloud platforms (Streamlit Cloud, AWS, Azure)
- Implement load balancing for high traffic
- Add Redis for distributed caching
- Implement queue system for query management
- Consider self-hosted LLM alternatives for cost reduction

---

## 🔄 Future Enhancements

### Short-term Improvements

1. **Enhanced Citations**
   - Display actual text chunks retrieved
   - Highlight relevant passages in responses
   - Show confidence scores for citations

2. **File Upload Interface**
   - Direct file upload through UI
   - Drag-and-drop document management
   - Real-time vector store updates

3. **Analytics Dashboard**
   - Query statistics and trends
   - Popular questions identification
   - Usage patterns by user type
   - Cost monitoring and alerts

4. **Multi-language Support**
   - Detect user language preference
   - Translate queries and responses
   - Support for local languages

### Long-term Vision

1. **Advanced RAG Techniques**
   - Hybrid search (keyword + semantic)
   - Query expansion and reformulation
   - Multi-hop reasoning for complex queries
   - Contextual chunk retrieval

2. **Integration Capabilities**
   - LMS integration (Moodle, Canvas)
   - Student information system connection
   - Email notification system
   - Calendar and event integration

3. **Personalization**
   - User profiles and preferences
   - Learning paths based on query history
   - Customized suggestions per user role
   - Adaptive difficulty levels

4. **Migration to Newer APIs**
   - Adopt OpenAI Responses API when available
   - Explore function calling capabilities
   - Implement streaming responses for better UX

5. **Self-hosted Options**
   - Evaluate open-source LLMs (Llama, Mistral)
   - On-premises deployment for data sovereignty
   - Cost reduction for high-volume usage

---

## 🧪 Testing and Quality Assurance

### Current Testing Approach

1. **Manual Testing**
   - Functional testing of all features
   - UI/UX validation
   - Error handling verification
   - Cross-browser compatibility

2. **Integration Testing**
   - OpenAI API connectivity
   - Vector store operations
   - Document upload workflows

3. **User Acceptance Testing**
   - Pilot testing with real users
   - Feedback collection and iteration
   - Performance validation under load

### Quality Metrics

- **Accuracy**: Responses grounded in source documents
- **Relevance**: Retrieved chunks match query intent
- **Completeness**: Answers address full question scope
- **Clarity**: Responses are well-structured and understandable
- **Speed**: Average response time under 5 seconds

---

## 📈 Metrics and Success Indicators

### Key Performance Indicators (KPIs)

1. **User Engagement**
   - Daily active users
   - Queries per user session
   - Return user rate
   - Session duration

2. **System Performance**
   - Average response time
   - API success rate
   - Error rate and types
   - Uptime percentage

3. **Quality Metrics**
   - User satisfaction ratings
   - Answer accuracy rate
   - Source citation relevance
   - Feedback and improvement requests

4. **Business Impact**
   - Support ticket reduction
   - Time saved per query
   - User self-service rate
   - Cost per query vs. human support

---

## 🤝 Contributing and Development

### Development Workflow

1. **Local Setup**
   - Clone repository
   - Create feature branch
   - Make changes with tests
   - Submit pull request

2. **Code Standards**
   - Follow PEP 8 style guide
   - Add docstrings to functions
   - Comment complex logic
   - Keep functions focused and small

3. **Version Control**
   - Meaningful commit messages
   - Feature branches for new work
   - Code review before merge
   - Tag releases semantically

### Areas for Contribution

- UI/UX improvements
- Additional helper scripts
- Documentation enhancements
- Bug fixes and optimization
- New features and capabilities

---

## 📝 Lessons Learned

### Technical Insights

1. **RAG Architecture**
   - Vector search is highly effective for document retrieval
   - Proper chunking strategy is critical for accuracy
   - Metadata enhances retrieval relevance
   - Citation tracking requires careful implementation

2. **OpenAI Integration**
   - Assistants API simplifies conversation management
   - Model selection impacts both cost and quality
   - Rate limiting and error handling are essential
   - Deprecation warnings require proactive monitoring

3. **Streamlit Development**
   - Session state management is crucial
   - Custom CSS enhances professional appearance
   - Caching significantly improves performance
   - Cloud deployment requires secrets management

### Product Insights

1. **User Experience**
   - Natural language queries reduce friction
   - Source citations build trust
   - Suggested questions guide effective usage
   - Clear error messages improve satisfaction

2. **Access Control**
   - Daily limits prevent abuse while allowing exploration
   - Guest IDs provide accountability without privacy concerns
   - Admin access needed for power users

3. **Content Management**
   - Document quality directly impacts answer quality
   - Metadata enables better source attribution
   - Regular content updates maintain relevance

---

## 🎯 Conclusion

The Pentecost University RAG Knowledge Assistant represents a successful implementation of modern AI technology for institutional knowledge management. By combining OpenAI's powerful language models with Streamlit's accessible web framework, we've created a system that is:

- **Accessible**: Easy to use for all stakeholders
- **Accurate**: Grounded in authoritative documents
- **Scalable**: Handles growing user base and content
- **Maintainable**: Clean architecture and comprehensive documentation
- **Extensible**: Ready for future enhancements

This project demonstrates practical application of RAG technology, providing immediate value while establishing a foundation for continued innovation in AI-powered educational tools.

---

## 📞 Contact and Support

**Project Repository**: [https://github.com/hatieku-boateng-pu/RAG_PU](https://github.com/hatieku-boateng-pu/RAG_PU)

**Institution**: Pentecost University

**Technology**: Streamlit + OpenAI + RAG Architecture

**License**: See LICENSE file in repository

---

## 🙏 Acknowledgments

- **OpenAI**: For providing powerful AI APIs and models
- **Streamlit**: For the excellent web framework
- **Pentecost University**: For supporting innovative AI initiatives
- **Open Source Community**: For inspiration and best practices

---

*This documentation was created to showcase the Pentecost University RAG Knowledge Assistant project as a portfolio piece, demonstrating expertise in AI/ML, full-stack development, and practical application of RAG architecture.*

**Last Updated**: February 2026
**Version**: 1.0
