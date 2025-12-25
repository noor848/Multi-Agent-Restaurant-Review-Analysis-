# Installation
# !pip install crewai==0.28.8 crewai_tools==0.1.6 langchain_community==0.0.29

# Warning control
import warnings
warnings.filterwarnings('ignore')

from crewai import Agent, Task, Crew, Process
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from langchain_openai import ChatOpenAI
import os
from utils import get_openai_api_key, get_serper_api_key

# Setup API keys
openai_api_key = get_openai_api_key()
os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'
os.environ["SERPER_API_KEY"] = get_serper_api_key()

# Initialize tools
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

# ============================================
# AGENTS DEFINITION (With Delegation Enabled)
# ============================================

# Agent 1: Review Collector
review_collector = Agent(
    role="Review Data Collector",
    goal="Gather comprehensive customer reviews from multiple sources "
         "for {restaurant_name} in {city}",
    backstory=(
        "You are an expert at finding and collecting customer feedback "
        "from various platforms including Google, Yelp, TripAdvisor, and social media. "
        "You have a keen eye for authentic reviews and can filter out fake ones. "
        "Your thorough research ensures no valuable feedback is missed. "
        "You work closely with the team and can ask for help when needed."
    ),
    verbose=True,
    allow_delegation=True,  # Can ask other agents for help
    tools=[search_tool, scrape_tool]
)

# Agent 2: Sentiment Analyzer
sentiment_analyzer = Agent(
    role="Sentiment Analysis Expert",
    goal="Analyze the emotional tone and sentiment of customer reviews "
         "to identify patterns in customer satisfaction",
    backstory=(
        "With a background in natural language processing and psychology, "
        "you excel at understanding customer emotions behind their words. "
        "You can detect subtle hints of satisfaction, frustration, delight, "
        "or disappointment. Your analysis helps businesses understand the "
        "emotional journey of their customers. You collaborate with team members "
        "to ensure your analysis is comprehensive and accurate."
    ),
    verbose=True,
    allow_delegation=True,  # Can consult with other agents
    tools=[search_tool]
)

# Agent 3: Competitive Analyst
competitive_analyst = Agent(
    role="Competitive Intelligence Specialist",
    goal="Compare {restaurant_name} performance against competitors "
         "in {city} to identify market positioning",
    backstory=(
        "You are a market research expert specializing in the restaurant industry. "
        "You know how to benchmark restaurants against their competitors, "
        "identify market gaps, and spot opportunities. Your insights help "
        "restaurants understand where they stand in the competitive landscape "
        "and what makes them unique. You work collaboratively to provide context "
        "for other team members' findings."
    ),
    verbose=True,
    allow_delegation=True,  # Can request data from collectors
    tools=[search_tool, scrape_tool]
)

# Agent 4: Insights Generator
insights_generator = Agent(
    role="Business Strategy Consultant",
    goal="Transform analysis into actionable business recommendations "
         "that can improve {restaurant_name}'s performance",
    backstory=(
        "You are a seasoned business consultant who specializes in the "
        "restaurant industry. You've helped dozens of restaurants turn "
        "around their businesses by identifying key improvement areas. "
        "You know how to translate customer feedback and market data into practical, "
        "implementable strategies that drive results. You coordinate with "
        "all team members to ensure recommendations are well-informed."
    ),
    verbose=True,
    allow_delegation=True,  # Can request additional analysis
    tools=[search_tool]
)

# Agent 5: Report Writer
report_writer = Agent(
    role="Senior Report Documentation Specialist",
    goal="Create comprehensive, executive-ready reports that present "
         "all findings in a clear and professional manner",
    backstory=(
        "You are a professional report writer with expertise in data "
        "visualization and storytelling. You transform complex analysis "
        "into easy-to-understand reports that executives and managers love. "
        "Your reports are known for being thorough yet concise, with "
        "clear recommendations and beautiful formatting. You work with "
        "the entire team to ensure nothing is missed in the final report."
    ),
    verbose=True,
    allow_delegation=True,  # Can request clarifications
    tools=[]
)

# ============================================
# TASKS DEFINITION
# ============================================

# Task 1: Collect Reviews
collect_reviews_task = Task(
    description=(
        "Search and collect at least 25-35 recent customer reviews "
        "for {restaurant_name} located in {city}. "
        "Look for reviews from Google, Yelp, TripAdvisor, and social media. "
        "Focus on reviews from the past {time_period}. "
        "Organize reviews by platform and date. "
        "Include both positive and negative reviews for balanced analysis. "
        "If you encounter difficulties finding reviews, consult with team members."
    ),
    expected_output=(
        "A comprehensive collection of customer reviews organized by source, "
        "including review text, ratings, dates, and platform. "
        "Minimum 25 reviews with a mix of positive, neutral, and negative feedback. "
        "Summary statistics: total reviews, average rating, platform distribution."
    ),
    agent=review_collector
)

# Task 2: Analyze Sentiment
analyze_sentiment_task = Task(
    description=(
        "Analyze all collected reviews for {restaurant_name} and determine:\n"
        "1. Overall sentiment distribution (positive, neutral, negative percentages)\n"
        "2. Common themes in positive reviews (what customers love)\n"
        "3. Common complaints in negative reviews (what frustrates customers)\n"
        "4. Specific aspects mentioned: food quality, service, ambiance, price, cleanliness\n"
        "5. Trending sentiment patterns (improving or declining?)\n"
        "6. Most frequently mentioned dishes or menu items\n"
        "7. Staff and service quality feedback\n"
        "8. Peak complaint times or issues\n"
        "If patterns are unclear, request additional data from the review collector."
    ),
    expected_output=(
        "A detailed sentiment analysis report containing:\n"
        "- Sentiment breakdown with percentages and confidence scores\n"
        "- Top 5 positive themes with example quotes and frequency\n"
        "- Top 5 negative themes with example quotes and severity ratings\n"
        "- Ratings breakdown by aspect (food, service, ambiance, etc.) on 1-5 scale\n"
        "- Trend analysis with month-over-month comparison\n"
        "- Most and least mentioned menu items\n"
        "- Critical issues requiring immediate attention"
    ),
    agent=sentiment_analyzer
)

# Task 3: Competitive Analysis
competitive_analysis_task = Task(
    description=(
        "Research and analyze competitors of {restaurant_name} in {city}:\n"
        "1. Identify 3-5 direct competitors (similar cuisine, price range, location)\n"
        "2. Compare average ratings across platforms\n"
        "3. Analyze what competitors do better (based on their reviews)\n"
        "4. Identify what {restaurant_name} does better (competitive advantages)\n"
        "5. Find market gaps or underserved customer needs\n"
        "6. Compare pricing strategies if mentioned in reviews\n"
        "7. Analyze unique selling points of each competitor\n"
        "Coordinate with sentiment analyzer to understand comparative strengths."
    ),
    expected_output=(
        "A competitive intelligence report containing:\n"
        "- List of 3-5 main competitors with their ratings\n"
        "- Competitive positioning matrix\n"
        "- What competitors do better (with specific examples)\n"
        "- {restaurant_name}'s competitive advantages\n"
        "- Market gaps and opportunities\n"
        "- Pricing comparison insights\n"
        "- Strategic recommendations for differentiation"
    ),
    agent=competitive_analyst
)

# Task 4: Generate Strategic Insights
generate_insights_task = Task(
    description=(
        "Based on sentiment analysis and competitive research, generate actionable strategies:\n"
        "1. Identify the restaurant's top 3 strengths to maintain and amplify\n"
        "2. Identify the top 5 weaknesses that need immediate attention\n"
        "3. Provide specific, implementable recommendations for each weakness\n"
        "4. Suggest menu optimizations based on customer feedback\n"
        "5. Recommend staff training areas if service issues are detected\n"
        "6. Propose marketing strategies leveraging competitive advantages\n"
        "7. Identify quick wins vs. long-term strategic initiatives\n"
        "8. Estimate ROI and impact of each recommendation\n"
        "9. Create implementation timeline with priorities\n"
        "Consult with all team members to ensure recommendations are comprehensive."
    ),
    expected_output=(
        "A strategic action plan document containing:\n"
        "- Top 3 Strengths with amplification strategies\n"
        "- Top 5 Weaknesses with severity ratings (Critical/High/Medium/Low)\n"
        "- Detailed action plan with 8-10 specific recommendations\n"
        "- Each recommendation includes: description, priority, estimated cost, "
        "expected impact, implementation difficulty, timeline\n"
        "- Quick wins (0-30 days) vs. strategic initiatives (3-6 months)\n"
        "- Resource requirements and budget considerations\n"
        "- Success metrics and KPIs for tracking progress"
    ),
    agent=insights_generator
)

# Task 5: Create Comprehensive Report
create_report_task = Task(
    description=(
        "Compile all findings into a professional, executive-ready report:\n"
        "1. Executive Summary (key findings, critical insights, top 3 recommendations)\n"
        "2. Methodology (data sources, review count, analysis approach)\n"
        "3. Review Collection Summary (platforms, date range, statistics)\n"
        "4. Detailed Sentiment Analysis with visual descriptions\n"
        "5. Competitive Analysis and Market Positioning\n"
        "6. Strengths and Weaknesses Analysis\n"
        "7. Strategic Recommendations with Implementation Plan\n"
        "8. Financial Impact Analysis\n"
        "9. Timeline and Milestones\n"
        "10. Conclusion and Next Steps\n"
        "11. Appendix with key review quotes\n"
        "Format in professional markdown with clear sections, tables, and emphasis. "
        "Ensure all team members' findings are represented accurately."
    ),
    expected_output=(
        "A complete, executive-ready markdown report (10-15 pages) including:\n"
        "- Professional structure with table of contents\n"
        "- Executive summary highlighting critical findings\n"
        "- All analysis findings with supporting data\n"
        "- Competitive positioning insights\n"
        "- Prioritized action plan with timelines and budgets\n"
        "- Visual data representations (described for charts/graphs)\n"
        "- Ready to present to restaurant ownership and management\n"
        "- Saved to restaurant_analysis_report.md"
    ),
    output_file="restaurant_analysis_report.md",
    agent=report_writer
)

# ============================================
# CREW SETUP (HIERARCHICAL WITH MANAGER)
# ============================================

# Create the crew with hierarchical process
restaurant_analysis_crew = Crew(
    agents=[
        review_collector,
        sentiment_analyzer,
        competitive_analyst,
        insights_generator,
        report_writer
    ],
    tasks=[
        collect_reviews_task,
        analyze_sentiment_task,
        competitive_analysis_task,
        generate_insights_task,
        create_report_task
    ],
    process=Process.hierarchical,  # Manager coordinates everything
    manager_llm=ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7
    ),
    verbose=True
)

# ============================================
# EXECUTION
# ============================================

# Define restaurant to analyze
restaurant_details = {
    'restaurant_name': 'The Golden Fork',
    'city': 'San Francisco',
    'time_period': '6 months'
}

# Run the analysis
print("=" * 70)
print("STARTING HIERARCHICAL RESTAURANT REVIEW ANALYSIS")
print("=" * 70)
print(f"\n📍 Restaurant: {restaurant_details['restaurant_name']}")
print(f"📍 Location: {restaurant_details['city']}")
print(f"📍 Time Period: {restaurant_details['time_period']}")
print(f"\n🤖 Manager: GPT-3.5-turbo (Coordinating 5 specialist agents)")
print(f"👥 Team: 5 AI agents with delegation enabled")
print("\n" + "-" * 70)
print("Manager is now coordinating the team...\n")

result = restaurant_analysis_crew.kickoff(inputs=restaurant_details)

# Display the result
print("\n" + "=" * 70)
print("✅ ANALYSIS COMPLETE!")
print("=" * 70)
print(f"📄 Report saved to: restaurant_analysis_report.md")
print("-" * 70)

from IPython.display import Markdown
Markdown(result)
