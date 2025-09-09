# Outline Generation Design - US-001

## User Story
As a writer, I want to generate a detailed story outline, so that I can review the story structure before chapter generation.

## Acceptance Criteria
- Generate outline with background, characters, plot, mystery elements
- Present in reviewable format with clear sections  
- User can approve/modify before proceeding

## Design

**Input**: Story parameters (genre, setting, etc.)
**Output**: `./outputs/[story-name]/outline.md`
**Storage**: File-based only, no database

## Outline Structure
```markdown
# [Story Title]

## Background
- Genre: [cozy mystery/noir/police procedural]
- Setting: [time and place]
- Premise: [core concept]

## Characters
### Detective
- Name: [name]
- Background: [details]

### Victim  
- Name: [name]
- Background: [details]

### Suspects
1. [Name] - [motive and background]
2. [Name] - [motive and background]  
3. [Name] - [motive and background]

## Plot
- Crime: [what happened]
- Clues: [evidence list]
- Red Herrings: [false leads]
- Solution: [who did it and why]
```

## Implementation Instructions
-. Generate outline content via AI
-. Suppport both config from config file and interactive mode.
-. The config and outline should support Chinese character.
-. Use DSPy libraray to interact with gemini for content generation
-. Format according to the structure above
-. Save as markdown to `./outputs/[story-name]/outline.md`
