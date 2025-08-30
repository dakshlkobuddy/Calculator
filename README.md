# Calculator - A Simple Web Calculator

A clean and functional web-based calculator built with HTML, CSS, and JavaScript. This calculator provides basic arithmetic operations with a modern, responsive design.

## 🚀 Features

- **Basic Arithmetic Operations**: Addition (+), Subtraction (-), Multiplication (*), Division (/)
- **Percentage Calculations**: Calculate percentages with the % button
- **Memory Functions**: M+ and M- buttons for memory operations (TODO: Implementation pending)
- **Clear Function**: Reset calculator with the C button
- **Decimal Support**: Handle decimal numbers for precise calculations
- **Responsive Design**: Works on desktop and mobile devices
- **Modern UI**: Clean interface with hover effects and proper spacing

## 🛠️ Technologies Used

- **HTML5**: Structure and layout
- **CSS3**: Styling and responsive design
- **JavaScript**: Calculator logic and interactivity
- **Google Fonts**: Roboto font family for better typography

## 📁 Project Structure

```
Calculator/
├── index.html          # Main HTML file
├── script.js           # JavaScript functionality
├── style.css           # Main stylesheet
├── utils.css           # Utility CSS classes
└── README.md           # Project documentation
```

## 🎯 How to Use

1. **Basic Operations**:
   - Click number buttons (0-9) to input values
   - Use operation buttons (+, -, *, /) for calculations
   - Press '=' to see the result
   - Press 'C' to clear the calculator

2. **Percentage**:
   - Enter a number and press '%' to calculate percentage

3. **Memory Functions** (Coming Soon):
   - M+: Add current value to memory
   - M-: Subtract current value from memory

## 🚀 Live Demo

[View Live Calculator](https://your-username.github.io/Calculator/)

## 💻 Local Development

### Prerequisites
- A modern web browser (Chrome, Firefox, Safari, Edge)
- No additional dependencies required

### Running Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Calculator.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Calculator
   ```

3. Open `index.html` in your web browser:
   - Double-click the file, or
   - Drag and drop into your browser, or
   - Use a local server (recommended):
     ```bash
     # Using Python 3
     python -m http.server 8000
     
     # Using Node.js (if you have http-server installed)
     npx http-server
     ```

4. Visit `http://localhost:8000` in your browser

## 📝 Code Analysis

### HTML Structure
- Semantic HTML5 with proper meta tags
- Responsive viewport configuration
- Clean button layout organized in rows
- Input field for displaying calculations and results

### CSS Styling
- **Main Styles** (`style.css`):
  - Google Fonts integration (Roboto)
  - Button styling with hover effects
  - Input field styling
  - Responsive layout with proper spacing

- **Utility Classes** (`utils.css`):
  - Flexbox utilities for layout
  - Text alignment classes
  - Margin and alignment helpers

### JavaScript Functionality
- Event-driven architecture using event listeners
- String-based calculation handling
- Real-time display updates
- Clear functionality implementation

## 🔧 Future Enhancements

- [ ] Implement memory functions (M+, M-, MC)
- [ ] Add keyboard support
- [ ] Include scientific calculator functions
- [ ] Add calculation history
- [ ] Implement error handling for invalid expressions
- [ ] Add dark/light theme toggle

## 📋 Deployment to GitHub Pages

### Step 1: Create GitHub Repository
1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Name your repository `Calculator`
5. Make it public (required for GitHub Pages)
6. Don't initialize with README (we already have one)
7. Click "Create repository"

### Step 2: Initialize Git and Push Code
1. Open your terminal/command prompt
2. Navigate to your project directory:
   ```bash
   cd "path/to/your/Calculator"
   ```

3. Initialize Git repository:
   ```bash
   git init
   ```

4. Add all files to Git:
   ```bash
   git add .
   ```

5. Commit your changes:
   ```bash
   git commit -m "Initial commit: Calculator project"
   ```

6. Add your GitHub repository as remote:
   ```bash
   git remote add origin https://github.com/your-username/Calculator.git
   ```

7. Push to GitHub:
   ```bash
   git branch -M main
   git push -u origin main
   ```

### Step 3: Enable GitHub Pages
1. Go to your repository on GitHub
2. Click on "Settings" tab
3. Scroll down to "Pages" section in the left sidebar
4. Under "Source", select "Deploy from a branch"
5. Choose "main" branch
6. Select "/ (root)" folder
7. Click "Save"

### Step 4: Access Your Live Site
- GitHub Pages will automatically build and deploy your site
- Your calculator will be available at: `https://your-username.github.io/Calculator/`
- It may take a few minutes for the changes to appear

### Step 5: Update README with Live Link
1. Update the "Live Demo" section in your README with your actual GitHub Pages URL
2. Commit and push the changes:
   ```bash
   git add README.md
   git commit -m "Update README with live demo link"
   git push
   ```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

Created by Daksh Agarwal

---

**Note**: Replace `dakshlkobuddy` with your actual GitHub username throughout this README.
