# Setting up MkDocs with GitHub Pages for colored_custom_logger

This guide will walk you through the process of setting up MkDocs for your colored_custom_logger project and hosting it on GitHub Pages.

## Prerequisites

- Python 3.x installed
- Git installed
- A GitHub account
- Your project repository on GitHub

## Step 1: Install MkDocs

1. Open a terminal or command prompt.
2. Install MkDocs using pip:

```bash
pip install mkdocs
```

## Step 2: Set up MkDocs in your project

1. Navigate to your project's root directory:

```bash
cd path/to/colored_custom_logger
```

2. Initialize MkDocs in your project:

```bash
mkdocs new .
```

This creates a new `mkdocs.yml` file and a `docs` directory.

## Step 3: Configure MkDocs

1. Open `mkdocs.yml` in a text editor.
2. Modify it to fit your project. Here's a basic example:

```yaml
site_name: Colored Custom Logger
theme: readthedocs
nav:
  - Home: index.md
  - Installation: installation.md
  - Usage: usage.md
  - API Reference: api.md
```

## Step 4: Write your documentation

1. In the `docs` directory, create Markdown files for each section of your documentation.
2. For example, create `installation.md`, `usage.md`, and `api.md`.
3. Write your documentation in these files using Markdown syntax.

## Step 5: Preview your documentation

1. In your project root, run:

```bash
mkdocs serve
```

2. Open a web browser and go to `http://127.0.0.1:8000/` to preview your documentation.

## Step 6: Push your changes to GitHub

1. Commit your changes:

```bash
git add .
git commit -m "Add MkDocs documentation"
```

2. Push to GitHub:

```bash
git push origin main
```

## Step 7: Set up GitHub Pages

1. In your GitHub repository, go to Settings > Pages.
2. Under "Source", select the branch `gh-pages` (create this branch if it doesn't exist)
3. Set the folder to `/ (root)`
4. Click Save.

## Step 8: Build and deploy your documentation

**Build your MkDocs site**:
   - Open your terminal
   - Navigate to your project directory
   - Run the following command:
     ```
     mkdocs build
     ```
   - This will create a `site` directory with your built documentation


**Deploy to GitHub Pages**:
   - Still in your project directory, run:
     ```
     mkdocs gh-deploy
     ```
   - This command builds your docs and pushes them to the `gh-pages` branch

1. Your documentation should now be available at `https://robin-collins.github.io/colored_custom_logger/`.

## Updating your documentation

Whenever you make changes to your documentation:

1. Edit the Markdown files in the `docs` directory.
2. Commit and push your changes to GitHub.
3. Run `mkdocs gh-deploy` to update your GitHub Pages site.

Remember to keep your documentation up-to-date as you make changes to your project!