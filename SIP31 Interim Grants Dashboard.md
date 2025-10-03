# SIP31 Interim Grants Dashboard

A comprehensive single-page application that displays all GitHub issues from the SIP31 interim grants repository with cuevasm's comments and decisions, presented in a user-friendly and mobile-responsive interface.

## 🎯 Overview

This dashboard provides stakeholders with an intuitive way to browse and analyze grant applications, view cuevasm's decision-making process, and understand the status of all SIP31 interim grant proposals. The application extracts data from GitHub's REST API and presents it through a modern, interactive interface.

## ✨ Features

- **Interactive Dashboard** with real-time search and filtering
- **Summary Statistics** showing grant status breakdown and comment counts
- **Responsive Design** optimized for desktop and mobile devices
- **Detailed Issue Cards** with project information and status badges
- **Modal Interface** with tabbed views for comprehensive project details
- **cuevasm Activity Highlighting** showing decision-maker's involvement
- **Professional UI** with smooth animations and modern design principles

## 🛠 Tech Stack

- **Frontend**: React 18 with Vite
- **Styling**: Tailwind CSS
- **UI Components**: shadcn/ui
- **Icons**: Lucide React
- **Animations**: Framer Motion
- **Data Source**: GitHub REST API
- **Package Manager**: npm/pnpm

## 📊 Data Overview

- **33 Total Issues** from stacksgov/sip31-interim-grants repository
- **92 Comments** from cuevasm across all issues
- **100% Coverage** - cuevasm has commented on every issue
- **Real-time Data** extracted via GitHub REST API

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ 
- npm or pnpm
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd sip31-grants-dashboard
   ```

2. **Install dependencies**
   ```bash
   npm install
   # or
   pnpm install
   ```

3. **Start the development server**
   ```bash
   npm run dev
   # or
   pnpm run dev
   ```

4. **Open your browser**
   Navigate to `http://localhost:5173`

### Development Server with Network Access

To access the development server from other devices on your network:

```bash
npm run dev -- --host
# or
pnpm run dev -- --host
```

## 📁 Project Structure

```
sip31-grants-dashboard/
├── public/                 # Static assets
├── src/
│   ├── assets/            # Data files and static assets
│   │   └── data.json      # Processed GitHub issues data
│   ├── components/
│   │   └── ui/            # shadcn/ui components
│   ├── hooks/             # Custom React hooks
│   ├── lib/               # Utility functions
│   ├── App.jsx            # Main application component
│   ├── App.css            # Application styles
│   ├── index.css          # Global styles
│   └── main.jsx           # Application entry point
├── components.json        # shadcn/ui configuration
├── package.json           # Dependencies and scripts
├── tailwind.config.js     # Tailwind CSS configuration
├── vite.config.js         # Vite bundler configuration
└── README.md              # This file
```

## 🔧 Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

## 📱 Features Breakdown

### Dashboard Overview
- Summary cards showing grant status distribution
- Total comment count from cuevasm
- Clean, professional header with branding

### Search & Filtering
- **Search Bar**: Filter by title, applicant, or project goal
- **Status Filters**: All, Awarded, In Review, Pending, With Comments
- **Real-time Results**: Instant filtering as you type

### Issue Cards
- **Status Badges**: Color-coded status indicators
- **Applicant Information**: Avatar, username, and application date
- **cuevasm Activity**: Highlighted sections showing decision-maker involvement
- **Comment Previews**: Latest cuevasm comment excerpts

### Detail Modal
- **Overview Tab**: Project description and applicant details
- **Comments Tab**: Complete cuevasm comment history with timestamps
- **Project Details Tab**: Budget, team, contact information, and GitHub links

## 🎨 Design System

The application uses a consistent design system with:
- **Color Palette**: Professional grays with accent colors for status
- **Typography**: Clear hierarchy with readable fonts
- **Spacing**: Consistent padding and margins throughout
- **Animations**: Subtle transitions and hover effects
- **Responsive Breakpoints**: Mobile-first design approach

## 📊 Data Processing

The application includes several Python scripts for data extraction and processing:

### GitHub Data Extraction
```python
# Extract all issues and comments from GitHub API
python3 github_extractor.py
```

### Comment Analysis
```python
# Analyze cuevasm's comment patterns and categorize them
python3 comment_analyzer.py
```

### Web Data Processing
```python
# Structure data for web application consumption
python3 data_processor.py
```

## 🔄 Data Updates

To update the dashboard with the latest GitHub data:

1. **Run the data extraction scripts**:
   ```bash
   python3 github_extractor.py
   python3 comment_analyzer.py
   python3 data_processor.py
   ```

2. **Copy the updated data**:
   ```bash
   cp web_app_data.json src/assets/data.json
   ```

3. **Restart the development server** to see changes

## 🌐 Deployment

### Production Build
```bash
npm run build
```

The build output will be in the `dist/` directory, ready for deployment to any static hosting service.

### Deployment Options
- **Vercel**: Connect your GitHub repository for automatic deployments
- **Netlify**: Drag and drop the `dist/` folder or connect via Git
- **GitHub Pages**: Use GitHub Actions for automated deployment
- **AWS S3**: Upload the `dist/` contents to an S3 bucket

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🐛 Issues & Support

If you encounter any issues or have questions:
1. Check the existing issues on GitHub
2. Create a new issue with detailed information
3. Include steps to reproduce any bugs

## 🙏 Acknowledgments

- **Stacks Foundation** for the SIP31 interim grants program
- **cuevasm** for detailed grant review comments
- **shadcn/ui** for the excellent component library
- **GitHub API** for providing access to issue data

---

**Built with ❤️ for the Stacks ecosystem**
