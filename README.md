# Cuevasm AI Agent: Stacks Treasury Committee System Prompt

## 🎯 Main Deliverable

**[cuevasm-system-prompt.md](cuevasm-system-prompt.md)** - A production-ready AI system prompt that embodies the persona of a skeptical, technically competent treasury committee head for Stacks SIP31 grants.

This system prompt creates an AI agent that:
- **Protects the Stacks treasury** from grifters and bad investments
- **Evaluates grant proposals** with technical rigor and business acumen
- **Challenges applicants** with direct, no-nonsense questions
- **Ensures ecosystem benefit** from every funded project

## 📋 What is Cuevasm?

Cuevasm is an AI persona designed to be the hardened gatekeeper of the Stacks treasury. Built from analyzing **92 real comments across 33 grant applications**, this system prompt captures:

- **Technical skepticism** - "Show me the code"
- **Business scrutiny** - "What's your burn rate?"
- **Ecosystem focus** - "How does this help other Stacks projects?"
- **Results orientation** - "I need to see traction, not roadmaps"

## 🚀 Usage

### Deploy the AI Agent

Copy the system prompt into any LLM (Claude, GPT-4, etc.) to create an AI agent that evaluates grant proposals:

```plaintext
System: [Insert cuevasm-system-prompt.md content]
User: [Grant proposal or funding request]
Assistant: [Cuevasm's skeptical evaluation]
```

### View the Dashboard

Open `index.html` in any browser to browse all 33 SIP31 grant proposals with cuevasm's decisions and comments. No installation required.

## 📊 Project Files

### Core Deliverables
- **`cuevasm-system-prompt.md`** - The AI system prompt (main output)
- **`index.html`** - Interactive grant viewer (open in browser)
- **`web_app_data.json`** - Processed data (33 issues, 92 cuevasm comments)

### Data Extraction Scripts
- `github_extractor.py` - Pulls issues from GitHub API
- `comment_analyzer.py` - Analyzes cuevasm's comment patterns
- `data_processor.py` - Structures data for visualization
- `github_issues_data.json` - Raw extracted data

### Documentation
- `github_issues_analysis.md` - SIP31 grant repository overview
- `SIP31 Interim Grants Dashboard.md` - Project background
- `Developer Setup Guide - SIP31 Grants Dashboard.md` - Setup details
- `SIP31 Grants Dashboard - Testing Results.md` - Test results

## 🔬 Research Foundation

The system prompt is derived from real-world data:
- **33 grant applications** from [stacksgov/sip31-interim-grants](https://github.com/stacksgov/sip31-interim-grants)
- **92 comments** from cuevasm across all issues
- **100% coverage** - cuevasm commented on every proposal
- **Pattern analysis** identified decision-making framework

## 💡 Decision Framework

The AI uses a weighted scoring system:
- **40%** Technical Assessment (code quality, security, scalability)
- **30%** Business Viability (revenue model, team capability, market timing)
- **20%** Ecosystem Impact (community benefit, network effects)
- **10%** Risk Management (technical, market, regulatory risks)

### Built-in Red Flags
- No working code or poor documentation
- Unrealistic projections or vague deliverables
- No community engagement or market research
- Excessive funding requests or inflated budgets

## 📈 Use Cases

1. **Grant Screening** - Automate initial review of funding proposals
2. **Due Diligence** - Challenge teams with tough questions before approval
3. **Treasury Protection** - Flag potentially problematic applications
4. **Applicant Training** - Teach what committees look for in proposals
5. **Ecosystem Analysis** - Evaluate projects for community benefit

## 🛠 Quick Start

### Use the System Prompt
1. Open `cuevasm-system-prompt.md`
2. Copy entire content
3. Paste into your LLM's system prompt
4. Submit grant proposals for evaluation

### View Grant Data
1. Open `index.html` in any browser
2. Search, filter, and browse all 33 grant proposals
3. Read cuevasm's comments and decisions

### Update Data (Optional)
```bash
python3 github_extractor.py      # Pull latest from GitHub
python3 comment_analyzer.py      # Analyze comment patterns
python3 data_processor.py        # Generate web_app_data.json
```

## 🎓 Key Insights

The Cuevasm persona embodies effective treasury management:
- **Skepticism protects resources** - Assume grift until proven otherwise
- **Technical depth matters** - Understand what you're funding
- **Results over promises** - Working code beats roadmaps
- **Ecosystem first** - Individual success must benefit the community
- **Financial discipline** - Every dollar must show clear value

---

**Main deliverable: [cuevasm-system-prompt.md](cuevasm-system-prompt.md)**

Built for the Stacks ecosystem to protect treasury resources while supporting genuine builders.

