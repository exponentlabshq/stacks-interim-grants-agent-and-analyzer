# Developer Setup Guide - SIP31 Grants Dashboard

This guide will help any developer quickly set up and run the SIP31 Grants Dashboard project.

## 🎯 What You'll Get

A fully functional dashboard that displays:
- All 33 GitHub issues from the SIP31 interim grants repository
- 92 comments from cuevasm (the decision maker)
- Interactive filtering and search capabilities
- Mobile-responsive design
- Professional UI with modern components

## 🛠 Prerequisites

Before you start, make sure you have:

- **Node.js 18+** ([Download here](https://nodejs.org/))
- **Python 3.7+** (for data extraction scripts)
- **Git** ([Download here](https://git-scm.com/))
- A code editor (VS Code recommended)

## 🚀 Quick Setup (5 minutes)

### Step 1: Get the Code
```bash
# If you have the project files
cd sip31-grants-dashboard

# Or clone from repository (if available)
git clone <repository-url>
cd sip31-grants-dashboard
```

### Step 2: Install Dependencies
```bash
# Install Node.js dependencies
npm install

# Install Python dependencies (for data updates)
pip3 install requests
```

### Step 3: Run the Application
```bash
# Start the development server
npm run dev

# Open your browser to http://localhost:5173
```

That's it! The dashboard should now be running with the existing data.

## 📊 Updating with Latest Data

To fetch the latest GitHub data and update the dashboard:

### Option 1: Automated Script (Recommended)
```bash
# Run the automated update script
./update-data.sh
```

### Option 2: Manual Steps
```bash
# 1. Extract GitHub data
python3 github_extractor.py

# 2. Analyze comments
python3 comment_analyzer.py

# 3. Process for web app
python3 data_processor.py

# 4. Copy to React app
cp web_app_data.json sip31-grants-dashboard/src/assets/data.json

# 5. Restart the dev server
npm run dev
```

## 🔧 Development Commands

```bash
# Start development server
npm run dev

# Start with network access (access from other devices)
npm run dev -- --host

# Build for production
npm run build

# Preview production build
npm run preview

# Run linting
npm run lint
```

## 📁 Project Structure Overview

```
sip31-grants-dashboard/
├── src/
│   ├── App.jsx           # Main dashboard component
│   ├── assets/
│   │   └── data.json     # GitHub issues data
│   └── components/ui/    # UI components
├── github_extractor.py   # Extracts GitHub data
├── comment_analyzer.py   # Analyzes cuevasm comments
├── data_processor.py     # Processes data for web
├── update-data.sh        # Automated update script
└── README.md            # Detailed documentation
```

## 🎨 Customization

### Changing Colors/Styling
- Edit `src/App.css` for custom styles
- Modify Tailwind classes in `src/App.jsx`
- Update color scheme in the CSS variables

### Adding New Features
- Components are in `src/components/ui/`
- Main logic is in `src/App.jsx`
- Data structure is defined in the JSON files

### Modifying Data Sources
- Edit `github_extractor.py` to change repository or user
- Update API endpoints in the extraction scripts
- Modify data processing logic in `data_processor.py`

## 🐛 Troubleshooting

### Common Issues

**Port 5173 already in use:**
```bash
# Kill the existing process
pkill -f vite
# Or use a different port
npm run dev -- --port 3000
```

**Python dependencies missing:**
```bash
pip3 install requests json datetime
```

**Data not updating:**
```bash
# Check if data files exist
ls -la *.json
# Restart the dev server
npm run dev
```

**Build errors:**
```bash
# Clear node modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

## 🌐 Deployment Options

### Vercel (Recommended)
1. Push code to GitHub
2. Connect repository to Vercel
3. Deploy automatically

### Netlify
1. Run `npm run build`
2. Upload `dist/` folder to Netlify
3. Configure redirects if needed

### GitHub Pages
1. Add deployment workflow
2. Push to main branch
3. Enable GitHub Pages

## 📝 Environment Variables

No environment variables are required for basic functionality. The application uses:
- Public GitHub API (no authentication needed)
- Static data files
- Client-side only processing

## 🤝 Contributing

1. **Fork** the repository
2. **Create** a feature branch
3. **Make** your changes
4. **Test** thoroughly
5. **Submit** a pull request

## 📞 Getting Help

If you encounter issues:

1. **Check the console** for error messages
2. **Verify prerequisites** are installed correctly
3. **Try the troubleshooting steps** above
4. **Create an issue** with detailed information

## 🎉 Success Checklist

- [ ] Node.js and Python installed
- [ ] Dependencies installed successfully
- [ ] Development server starts without errors
- [ ] Dashboard loads at http://localhost:5173
- [ ] Can see 33 issues with cuevasm comments
- [ ] Search and filtering work correctly
- [ ] Modal opens when clicking issue cards
- [ ] Mobile responsive design works

## 📚 Additional Resources

- [React Documentation](https://react.dev/)
- [Tailwind CSS Docs](https://tailwindcss.com/docs)
- [shadcn/ui Components](https://ui.shadcn.com/)
- [GitHub API Documentation](https://docs.github.com/en/rest)

---

**Happy coding! 🚀**

*If this guide helped you get set up, consider giving the project a star ⭐*
