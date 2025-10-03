# Cuevasm AI Agent: Stacks Treasury Committee System Prompt

## 🎯 Main Deliverable

**[cuevasm-system-prompt.md](cuevasm-system-prompt.md)** - A production-ready AI system prompt that embodies the persona of a skeptical, technically competent treasury committee head for Stacks SIP31 grants.

This system prompt creates an AI agent that:
- **Protects the Stacks treasury** from grifters and bad investments
- **Evaluates grant proposals** with technical rigor and business acumen
- **Challenges applicants** with direct, no-nonsense questions
- **Ensures ecosystem benefit** from every funded project

## 📋 What is Cuevasm?

Cuevasm is an AI persona designed to be the hardened gatekeeper of the Stacks treasury. Built from analyzing 92 real comments across 33 grant applications, this system prompt captures:

- **Technical skepticism** - "Show me the code"
- **Business scrutiny** - "What's your burn rate?"
- **Ecosystem focus** - "How does this help other Stacks projects?"
- **Results orientation** - "I need to see traction, not roadmaps"

## 🚀 Usage

Deploy this system prompt with any LLM (Claude, GPT-4, etc.) to create an AI agent that evaluates grant proposals, challenges assumptions, and protects treasury resources.

```plaintext
System: [Insert cuevasm-system-prompt.md content]
User: [Grant proposal or funding request]
Assistant: [Cuevasm's skeptical evaluation]
```

## 📊 Supporting Materials

### Data Analysis
- `github_extractor.py` - Extracts GitHub issues and comments from SIP31 repo
- `comment_analyzer.py` - Analyzes cuevasm's comment patterns
- `data_processor.py` - Structures data for visualization
- `github_issues_data.json` - Raw extracted data (33 issues, 92 cuevasm comments)

### Dashboard Application
Interactive web application for browsing grant proposals and cuevasm's decisions:
- `App.jsx` / `dashboard.html` - React dashboard interface
- `data.json` / `web_app_data.json` - Processed grant data
- See [SIP31 Interim Grants Dashboard.md](SIP31%20Interim%20Grants%20Dashboard.md) for details

### Documentation
- `github_issues_analysis.md` - Overview of SIP31 grant repository
- `Developer Setup Guide - SIP31 Grants Dashboard.md` - Setup instructions
- `SIP31 Grants Dashboard - Testing Results.md` - Test results
- `fixed-mortem.md` / `fuck-react.md` - Development notes

## 🔬 Research Foundation

The Cuevasm system prompt is derived from real-world data:
- **33 grant applications** from stacksgov/sip31-interim-grants
- **92 comments** from cuevasm across all issues
- **100% coverage** - cuevasm commented on every proposal
- **Patterns identified** through systematic comment analysis

## 💡 Key Features of the System Prompt

### Decision Framework
- **40%** Technical Assessment (code quality, security, scalability)
- **30%** Business Viability (revenue model, team capability, market timing)
- **20%** Ecosystem Impact (community benefit, network effects)
- **10%** Risk Management (technical, market, regulatory risks)

### Response Patterns
- Direct, blunt communication style
- Technical depth with business pragmatism
- Specific, actionable feedback
- Clear approval/rejection criteria

### Built-in Red Flags
- No working code or poor documentation
- Unrealistic projections or vague deliverables
- No community engagement or market research
- Excessive funding requests or inflated budgets

## 📈 Use Cases

1. **Grant Review AI** - Automate initial screening of funding proposals
2. **Due Diligence Assistant** - Challenge teams with tough questions
3. **Treasury Protection** - Flag potentially problematic applications
4. **Ecosystem Analysis** - Evaluate projects for community benefit
5. **Training Tool** - Teach grant applicants what committees look for

## 🛠 Quick Start

### Use the System Prompt
1. Open `cuevasm-system-prompt.md`
2. Copy the entire content
3. Paste into your LLM's system prompt field
4. Submit grant proposals for evaluation

### Run the Dashboard
```bash
npm install
npm run dev
```
Open `http://localhost:5173` to view the grant dashboard.

### Extract Latest Data
```bash
python3 github_extractor.py
python3 comment_analyzer.py
python3 data_processor.py
```

## 📖 Context

This project analyzes the Stacks SIP31 interim grants program, where cuevasm served as the primary decision-maker. The system prompt distills their decision-making approach into a reusable AI agent.

**Repository analyzed**: [stacksgov/sip31-interim-grants](https://github.com/stacksgov/sip31-interim-grants)

## 🎓 Lessons Learned

The Cuevasm persona embodies effective treasury management:
- **Skepticism protects resources** - Assume grift until proven otherwise
- **Technical depth matters** - Understand what you're funding
- **Results over promises** - Working code beats roadmaps
- **Ecosystem first** - Individual success must benefit the community
- **Financial discipline** - Every dollar must show clear value

---

**Main deliverable: [cuevasm-system-prompt.md](cuevasm-system-prompt.md)**

Built for the Stacks ecosystem to protect treasury resources while supporting genuine builders.

