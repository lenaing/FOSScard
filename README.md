<div align="center">

# 🎴 FOSScard

### _Your Open Source Contributions, Magic Card Style_

**At the crossroad of a business card and a CV**

[![Python](https://img.shields.io/badge/Python-3.6+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](http://makeapullrequest.com)

---

**FOSScard** transforms your open source portfolio into a beautiful, shareable Magic: The Gathering-style card. Perfect for recruiters, personal websites, and showcasing your contributions in style.

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Examples](#-examples) • [Contributing](#-contributing)

</div>

---

## 🤔 Why FOSScard?

- **🎯 Stand Out**: Turn your GitHub profile into eye-catching visual art
- **⚡ Fast**: Generate your card in seconds with a simple YAML file
- **📊 Complexity Indicators**: Show project difficulty with colored squares (🟩🟨🟥)
- **🔗 Optional Links**: Projects can have links or stand alone
- **🖼️ Custom Headers**: Add background images to personalize your card
- **📱 Responsive**: Looks great on any device

---

## ✨ Features

### 🎨 **Multiple Themes**
Choose from 4 carefully crafted color schemes:
- **Dark** - Classic Magic card aesthetic
- **Light** - Clean and professional
- **Matrix** - Hacker green on black
- **Molokai** - Inspired by the iconic Vim colorscheme
Or create your own!

### 📊 **Complexity Indicators**
Show the sophistication of your projects:
- 🟩🟩 **1-2**: Simple projects (green)
- 🟨🟨🟨 **3-4**: Moderate complexity (yellow)
- 🟥🟥🟥🟥🟥 **5+**: Advanced projects (red)

### 🎯 **Flexible Structure**
- **Categories**: Organize projects by type (OS, AI, Web, etc.)
- **Language Groups**: Group projects by programming language
- **Optional Links**: Not all projects need URLs
- **Custom Descriptions**: Highlight what makes each project special

### 🖼️ **Personalization**
- Add your logo
- Custom header backgrounds (images or gradients)
- Link to your website or portfolio
- Your name, your style

---

## 🛠️ Installation

### Requirements
- Python 3.6+
- PyYAML

### Quick Start

```bash
# Clone the repository
git clone https://github.com/iMilnb/FOSScard.git
cd FOSScard

# Install dependencies
pip install pyyaml

# Create your profile (see examples below)
${EDITOR} yourname.yaml

# Generate your card
python fosscard.py yourname.yaml > yourname.html

# Or pipe from stdin
cat yourname.yaml | python fosscard.py > yourname.html
```

---

## 🚀 Usage

### Basic YAML Structure

```yaml
name: Your Name
link: https://yourwebsite.com
logo: https://example.com/your-logo.png
header_background: https://example.com/header-bg.jpg
style: molokai

projects:
  Category Name:
    Language:
      Project Name:
        link: https://github.com/user/project
        description: A brief description of your project
        complexity: 3
```

### Minimal Example

```yaml
name: Jane Doe
style: dark

projects:
  Web Development:
    React Dashboard:
      description: Modern admin panel
      complexity: 2
```

### Advanced Example

```yaml
name: John Smith
link: https://johnsmith.dev
logo: https://avatars.githubusercontent.com/u/12345
header_background: "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
style: molokai

projects:
  Operating Systems:
    C:
      kernel-module:
        link: https://github.com/user/kernel-module
        description: Custom Linux kernel module for performance monitoring
        complexity: 5

      bootloader:
        link: https://github.com/user/bootloader
        description: Minimal x86 bootloader
        complexity: 4

  Web Development:
    TypeScript:
      react-dashboard:
        link: https://github.com/user/dashboard
        description: Enterprise-grade admin dashboard
        complexity: 3

      api-gateway:
        description: Microservices API gateway (private repo)
        complexity: 4

  AI/ML:
    Python:
      sentiment-analyzer:
        link: https://github.com/user/sentiment
        description: Real-time sentiment analysis engine
        complexity: 3
```

---

## 🎯 Field Reference

| Field | Required | Description | Example |
|-------|----------|-------------|---------|
| `name` | Yes | Your name | `"Jane Developer"` |
| `link` | No | Personal website/portfolio | `"https://jane.dev"` |
| `logo` | No | Profile image URL | `"https://..."` |
| `header_background` | No | Header background (image URL, color, or gradient) | `"https://..."` or `"#667eea"` |
| `style` | No | Theme name (default: dark) | `"molokai"` |
| `projects` | Yes | Project structure (see examples) | `{}` |

### Project Fields

| Field | Required | Description | Example |
|-------|----------|-------------|---------|
| `link` | No | Project URL | `"https://github.com/..."` |
| `description` | Yes | Brief project description | `"Web scraping tool"` |
| `complexity` | No | Difficulty level (1-10+) | `3` |

---

## 💡 Examples

### Header Backgrounds

```yaml
# Solid color
header_background: "#667eea"

# Gradient
header_background: "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"

# Remote image
header_background: https://images.unsplash.com/photo-1234567890

# Or wrap in url() manually
header_background: "url('https://example.com/image.jpg')"
```

### Project Organization

```yaml
# Direct projects under category
projects:
  Tools:
    cli-tool:
      link: https://github.com/user/tool
      description: Command-line utility
      complexity: 2

# Language-grouped projects
projects:
  Web Development:
    JavaScript:
      project-one:
        description: First project
        complexity: 2
      project-two:
        link: https://github.com/user/project-two
        description: Second project
        complexity: 3
```

---

## 🎪 Real-World Example

Check out `iMil.yaml` in this repository for a complete example featuring:
- Multiple categories (OS, AI, Misc)
- Language grouping (Go, NetBSD)
- Various projects with different complexity levels
- Molokai theme styling

---

## 🤸 Contributing

We love contributions! Whether it's:

- 🐛 Bug reports
- 💡 Feature requests
- 🎨 New themes
- 📝 Documentation improvements
- 🔧 Code contributions

**How to contribute:**

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### 🎴 Made with ❤️ for the FOSS community

**[⬆ Back to Top](#-fosscard)**

</div>
