# 🤖 AI-Powered Automated Grading System for C++ Code



## 📋 Project Overview

An intelligent automated grading system that leverages multi-agent AI architecture to evaluate student C++ programming assignments with human-level accuracy. The system employs advanced LangChain orchestration, OpenAI's GPT models, and an intuitive Streamlit interface to provide consistent, detailed, and fair grading at scale.

## 🎯 Core Purpose

- **Automate Code Evaluation** - Reduce manual grading workload for instructors
- **Ensure Consistency** - Provide objective and standardized assessment across all submissions
- **Deliver Detailed Feedback** - Generate comprehensive explanations for scores and improvement suggestions
- **Scale Efficiently** - Grade multiple submissions simultaneously without quality degradation

## 🚀 Key Features

### Multi-Agent Architecture
- **Analysis Agent** - Comprehensive code analysis and comparison with reference solutions
- **Evaluator Agents** - Independent grading based on rubric criteria
- **Meta-Evaluator Agent** - Quality control and fairness verification
- **Voter Agent** - Consensus-based score aggregation
- **Optimizer Agent** - Score refinement and normalization

### Dual Workflow System
- **Parallelization Workflow (Voting Mechanism)** - Multiple independent evaluators with median-based consensus
- **Sequential Optimization Workflow** - Iterative refinement with meta-evaluation

### Advanced AI Capabilities
- **Chain-of-Thought Prompting** - Enhanced reasoning and accuracy
- **Few-Shot Learning** - Context-aware grading examples
- **LangChain Integration** - Robust agent orchestration and state management
- **OpenAI GPT-4 Integration** - State-of-the-art language understanding

### Interactive Interface
- **Streamlit Web App** - User-friendly interface for submission and results
- **Real-time Grading** - Instant feedback generation
- **Visualization** - Score breakdowns and performance metrics

## 🏗️ Architecture
```
┌──────────────┐
│  Student     │
│  Submission  │
└──────┬───────┘
       │
       ▼
┌──────────────────────────────────────┐
│     Analysis Agent                   │
│  (Code Analysis & Comparison)        │
└──────┬───────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────┐
│   Multi-Agent Evaluation             │
├──────────────────────────────────────┤
│  Evaluator 1  │  Evaluator 2  │ ... │
└──────┬────────┴──────┬────────┴──────┘
       │               │
       ▼               ▼
┌──────────────────────────────────────┐
│       Voter Agent                    │
│   (Consensus & Aggregation)          │
└──────┬───────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────┐
│    Meta-Evaluator Agent              │
│   (Quality Control)                  │
└──────┬───────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────┐
│     Optimizer Agent                  │
│   (Score Refinement)                 │
└──────┬───────────────────────────────┘
       │
       ▼
┌──────────────┐
│ Final Grade  │
│ + Feedback   │
└──────────────┘
```

## 🛠️ Technology Stack

### AI & ML
- **OpenAI GPT-4** - Advanced language model for code understanding
- **LangChain** - Agent orchestration and workflow management
- **Python 3.10+** - Core programming language

### Frontend & Interface
- **Streamlit** - Interactive web application framework
- **Plotly** - Data visualization and charts

### Development Tools
- **Git** - Version control
- **Virtual Environment** - Dependency isolation

## 🔄 Grading Workflows

### Workflow 1: Parallelization (Voting Mechanism)
1. **Analysis**: Code analyzed against reference solution
2. **Independent Evaluation**: Multiple agents grade simultaneously
3. **Voting**: Median score calculated from all evaluators
4. **Meta-Evaluation**: Quality control verification
5. **Optimization**: Final score refinement

### Workflow 2: Sequential Optimization
1. **Initial Evaluation**: First-pass grading
2. **Meta-Evaluation**: Quality assessment and feedback
3. **Iterative Refinement**: Score optimization based on meta-feedback
4. **Final Output**: Optimized grade with detailed justification

## 📊 Performance Metrics

- **Grading Accuracy**: Comparable to human instructors
- **Processing Time**: Real-time evaluation (< 30 seconds per submission)
- **Consistency**: Standardized assessment across all submissions
- **Scalability**: Handles multiple concurrent grading sessions

## 🚦 Getting Started

### Prerequisites
```bash
Python 3.10+
OpenAI API Key
Git
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/ai-grading-system.git
cd ai-grading-system
```

2. **Set up environment**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Configure API keys**
```bash
# Create .env file
OPENAI_API_KEY=your_openai_api_key_here
```

4. **Run the application**
```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

## 📡 Usage

### Grading a Submission

1. **Upload Files**
   - Student's C++ code
   - Reference solution
   - Grading rubric

2. **Select Workflow**
   - Choose between Voting Mechanism or Sequential Optimization

3. **Run Grading**
   - System analyzes code
   - Agents evaluate independently
   - Consensus reached
   - Final grade generated

4. **Review Results**
   - View final score
   - Read detailed feedback
   - See score breakdown by criteria

## 📂 Project Structure
```
ai-grading-system/
├── agents/
│   ├── analysis_agent.py      # Code analysis
│   ├── evaluator_agent.py     # Grading agents
│   ├── meta_evaluator.py      # Quality control
│   ├── voter_agent.py         # Consensus mechanism
│   └── optimizer_agent.py     # Score refinement
├── workflows/
│   ├── voting_workflow.py     # Parallelization flow
│   └── sequential_workflow.py # Optimization flow
├── app.py                     # Streamlit interface
├── requirements.txt           # Dependencies
└── README.md
```

## 🎯 Key Advantages

### For Instructors
- ✅ Reduce grading time by 80%
- ✅ Consistent evaluation standards
- ✅ Detailed feedback generation
- ✅ Handle large class sizes efficiently

### For Students
- ✅ Instant feedback on submissions
- ✅ Detailed improvement suggestions
- ✅ Fair and objective assessment
- ✅ Learning-oriented feedback

### For Institutions
- ✅ Scalable grading infrastructure
- ✅ Quality assurance mechanisms
- ✅ Data-driven insights on student performance
- ✅ Reduced administrative overhead

## 🔮 Future Enhancements

- [ ] Support for multiple programming languages (Java, Python, JavaScript)
- [ ] Integration with Learning Management Systems (Canvas, Moodle)
- [ ] Advanced plagiarism detection
- [ ] Custom rubric builder interface
- [ ] Batch grading for entire classes
- [ ] Analytics dashboard for instructors

## 👥 Team

**AI/ML Developer** - Multi-agent architecture and LangChain integration  
**Frontend Developer** - Streamlit interface design  
**Education Specialist** - Rubric design and grading standards

## 📄 License

This project is developed as part of an AI/ML course assignment.

## 🙏 Acknowledgments

- **OpenAI** for GPT-4 API
- **LangChain** for agent orchestration framework
- **Streamlit** for rapid interface development

