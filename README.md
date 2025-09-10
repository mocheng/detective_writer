# Detective Novel Generator

AI-powered detective novel generator with step-by-step outline and chapter creation.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set Gemini API key in `.env` file:
```bash
GEMINI_API_KEY=your-api-key-here
```

## Usage

### Config Mode (Default)
```bash
python -m generator.outline
```
Uses settings from `config.yaml`

### Interactive Mode
```bash
python -m generator.outline --interactive
```
Prompts for story parameters

## Output

Generated outlines are saved to:
```
./outputs/[story-name]/outline.md
```

## Configuration

Edit `config.yaml` to change default story parameters:
- title: Story title
- genre: cozy_mystery, noir, or police_procedural  
- setting: Time and place setting
