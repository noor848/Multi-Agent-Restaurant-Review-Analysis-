# AI-Powered Restaurant Review Analysis System (Hierarchical)

An advanced multi-agent system with intelligent manager coordination that automatically collects, analyzes, and generates comprehensive business insights from restaurant customer reviews.

## Overview

This system uses **5 specialized AI agents** working under a **Manager LLM coordinator** to provide comprehensive restaurant analysis:
```
                    Manager (GPT-3.5-turbo)
                            ↓
        ┌───────────────────┼───────────────────┐
        ↓                   ↓                   ↓
  Review Collector → Sentiment Analyzer → Competitive Analyst
        ↓                   ↓                   ↓
        └──────────→ Insights Generator ←───────┘
                            ↓
                     Report Writer
```

### The Team

1. **Review Data Collector**: Gathers reviews from multiple platforms
2. **Sentiment Analysis Expert**: Analyzes emotional patterns
3. **Competitive Intelligence Specialist**: Benchmarks against competitors
4. **Business Strategy Consultant**: Creates actionable recommendations
5. **Senior Report Writer**: Compiles executive-ready reports

**Manager LLM**: Coordinates workflow, enables collaboration, ensures quality

## Key Features

### 🎯 Hierarchical Process
- **Manager coordinates all agents** - intelligent workflow management
- **Dynamic task delegation** - manager adapts based on findings
- **Quality control** - manager reviews each output
- **Cross-agent collaboration** - agents can consult each other

### 🤝 Agent Delegation Enabled
- Agents can request help from teammates (`allow_delegation=True`)
- Review Collector can ask Sentiment Analyzer about patterns
- Competitive Analyst can request additional data from Collector
- Insights Generator can consult all agents for comprehensive recommendations
- Report Writer can request clarifications from any agent

### 📊 Comprehensive Analysis
- Multi-platform review collection (Google, Yelp, TripAdvisor, social media)
- Deep sentiment and trend analysis
- Competitive benchmarking and positioning
- Strategic business recommendations
- Professional executive reports

## How It Works

### Hierarchical Coordination
```
Manager Planning Phase:
├─ Analyzes the overall goal
├─ Plans optimal workflow
├─ Assigns tasks to appropriate agents
└─ Monitors progress continuously

Execution Phase:
├─ Reviews each agent's output
├─ Facilitates collaboration between agents
├─ Requests revisions if quality issues found
├─ Ensures consistency across all findings
└─ Synthesizes final comprehensive report
```

### Agent Collaboration Examples

**Scenario 1: Pattern Clarification**
```
Sentiment Analyzer: "I see mixed signals about 'pasta quality'"
    ↓ (delegates to Review Collector)
Review Collector: "Let me get more pasta-specific reviews"
    ↓ (collects additional data)
Sentiment Analyzer: "Now clear - pasta quality dropped 2 months ago"
```

**Scenario 2: Competitive Context**
```
Insights Generator: "Need competitive context for pricing strategy"
    ↓ (delegates to Competitive Analyst)
Competitive Analyst: "Competitors charge 15-20% less for similar dishes"
    ↓ (reports findings)
Insights Generator: "Recommendation: Adjust pricing or emphasize quality"
```

**Scenario 3: Manager Quality Control**
```
Manager reviews Sentiment Analysis:
├─ "Good analysis, but need more data on weekend service"
├─ Sends back to Sentiment Analyzer
├─ Sentiment Analyzer requests weekend reviews from Collector
├─ Updated analysis returned
└─ Manager approves and proceeds
```

## Installation
```bash
pip install crewai==0.28.8 crewai_tools==0.1.6 langchain_community==0.0.29
```

## Prerequisites

- Python 3.7+
- OpenAI API key
- Serper API key

## Configuration
```python
from utils import get_openai_api_key, get_serper_api_key

openai_api_key = get_openai_api_key()
os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'
os.environ["SERPER_API_KEY"] = get_serper_api_key()
```

## Usage

### Basic Usage
```python
restaurant_details = {
    'restaurant_name': 'The Golden Fork',
    'city': 'San Francisco',
    'time_period': '6 months'
}

result = restaurant_analysis_crew.kickoff(inputs=restaurant_details)
```

### Different Scenarios
```python
# Quick recent analysis
restaurant_details = {
    'restaurant_name': 'Bistro Modern',
    'city': 'New York',
    'time_period': '3 months'
}

# Long-term trend analysis
restaurant_details = {
    'restaurant_name': 'Family Diner',
    'city': 'Chicago',
    'time_period': '12 months'
}

# New restaurant analysis
restaurant_details = {
    'restaurant_name': 'Fusion Kitchen',
    'city': 'Austin',
    'time_period': '2 months'
}
```

## Workflow Timeline

### Hierarchical Execution 
```
00:00 - Manager Planning
├─ Analyzes restaurant context
├─ Plans optimal workflow
└─ Assigns initial tasks

00:02 - Review Collection
├─ Search multiple platforms
├─ Collect 25-35 reviews
├─ Manager reviews collection
└─ If insufficient, request more

00:14 - Sentiment Analysis 
├─ Analyze all reviews
├─ Identify patterns
├─ May consult collector for clarification
├─ Manager reviews sentiment findings
└─ Approve or request deeper analysis

00:26 - Competitive Analysis 
├─ Research competitors
├─ Compare performance
├─ May request sentiment data for context
├─ Manager reviews competitive positioning
└─ Approve findings

00:38 - Insights Generation
├─ Synthesize all findings
├─ Consult all agents for comprehensive view
├─ Develop recommendations
├─ Manager reviews strategy
└─ Refine based on feedback

00:50 - Report Creation 
├─ Compile all sections
├─ May request clarifications from any agent
├─ Format professionally
├─ Manager final review
└─ Deliver executive report
```

## The Five Agents Explained

### 1. Review Data Collector
**Role**: Multi-platform review gatherer  
**Delegation**: Can ask sentiment analyzer about patterns  
**Tools**: Web search, web scraping  
**Output**: 25-35 reviews with metadata

**Example Task**:
```
Collect reviews → Organize by platform → 
If unclear patterns: Ask Sentiment Analyzer →
Collect more targeted reviews → Complete collection
```

### 2. Sentiment Analysis Expert
**Role**: Emotional pattern detector  
**Delegation**: Can request more data from collector  
**Tools**: Web search for context  
**Output**: Sentiment breakdown with trends

**Example Collaboration**:
```
Analyze reviews → Find ambiguous feedback →
Request collector get more specific reviews →
Complete comprehensive analysis
```

### 3. Competitive Intelligence Specialist
**Role**: Market positioning analyst  
**Delegation**: Can request data and sentiment insights  
**Tools**: Web search, web scraping  
**Output**: Competitive analysis report

**Example Delegation**:
```
Research competitors → Need context on strengths →
Ask Sentiment Analyzer for positive themes →
Complete competitive positioning
```

### 4. Business Strategy Consultant
**Role**: Strategic recommendations generator  
**Delegation**: Can consult all agents  
**Tools**: Web search  
**Output**: Prioritized action plan

**Example Multi-Agent Consultation**:
```
Draft recommendations →
Consult Sentiment Analyzer: "What's most critical?" →
Consult Competitive Analyst: "What's market gap?" →
Consult Collector: "Any recent changes?" →
Finalize comprehensive strategy
```

### 5. Senior Report Writer
**Role**: Executive report compiler  
**Delegation**: Can request clarifications  
**Tools**: None (synthesis role)  
**Output**: Professional markdown report

**Example Quality Check**:
```
Compile report → Unclear competitive data →
Request clarification from Competitive Analyst →
Finalize polished report
```

## Manager's Coordination

### What the Manager Does

**1. Strategic Planning**
```python
Manager: "For this restaurant analysis, optimal workflow is:
1. Collect reviews first (foundation)
2. Sentiment analysis (understand feedback)
3. Competitive analysis (context)
4. Insights generation (strategy)
5. Report creation (delivery)"
```

**2. Quality Assurance**
```python
Manager reviews Collector output:
"Only 15 reviews found - insufficient for reliable analysis"
→ Sends back to Collector
→ "Please search additional platforms and time ranges"
→ Collector returns with 30 reviews
→ Manager approves
```

**3. Facilitating Collaboration**
```python
Insights Generator needs competitive context:
Manager: "Competitive Analyst, please share your findings 
with Insights Generator"
→ Facilitates knowledge transfer
→ Ensures recommendations consider market positioning
```

**4. Adaptive Workflow**
```python
Manager notices sentiment is overwhelmingly negative:
→ Adjusts priorities
→ "Risk assessment is critical here"
→ Instructs Insights Generator to focus on crisis management
→ Adapts report structure to emphasize urgency
```

## Output: restaurant_analysis_report.md
