import os
import sys
import yaml
import dspy
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class OutlineGenerator(dspy.Signature):
    """Generate a detective story outline with background, characters, and plot."""
    
    title = dspy.InputField(desc="Story title")
    genre = dspy.InputField(desc="Genre: cozy mystery, noir, or police procedural")
    setting = dspy.InputField(desc="Time and place setting")
    
    outline = dspy.OutputField(desc="Complete story outline in markdown format following the structure: Background, Characters (Detective, Victim, Suspects), Plot (Crime, Clues, Red Herrings, Solution)")

def load_config():
    """Load configuration from config.yaml"""
    with open('config.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def setup_ai(config):
    """Setup DSPy with Gemini"""
    api_key = os.getenv('GEMINI_API_KEY') or config['ai']['api_key']
    if not api_key:
        raise ValueError("Please set GEMINI_API_KEY in .env file")
    
    model_name = 'gemini-2.5-flash'
    lm = dspy.LM(f'gemini/{model_name}', api_key=api_key)
    dspy.settings.configure(lm=lm)

def generate_outline(title, genre, setting):
    """Generate story outline using AI"""
    generator = dspy.Predict(OutlineGenerator)
    
    result = generator(
        title=title,
        genre=genre, 
        setting=setting
    )
    
    return result.outline

def format_outline(title, genre, setting, ai_content):
    """Format the outline according to specification using AI-generated content"""
    # Use AI-generated content directly, just ensure proper markdown formatting
    outline = f"# {title}\n\n"
    
    # Add basic metadata
    outline += f"## Background\n"
    outline += f"- Genre: {genre}\n"
    outline += f"- Setting: {setting}\n\n"
    
    # Add AI-generated content
    outline += ai_content
    
    return outline

def save_outline(title, outline_content):
    """Save outline to outputs folder"""
    # Create outputs directory
    output_dir = Path('./outputs') / title
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Save outline
    outline_path = output_dir / 'outline.md'
    with open(outline_path, 'w', encoding='utf-8') as f:
        f.write(outline_content)
    
    return outline_path

def interactive_mode():
    """Interactive mode for story parameters"""
    print("=== 侦探小说大纲生成器 ===")
    title = input("故事标题: ") or "神秘案件"
    
    print("\n选择类型:")
    print("1. cozy_mystery (温馨推理)")
    print("2. noir (黑色小说)")  
    print("3. police_procedural (警察程序)")
    genre_choice = input("选择 (1-3): ") or "1"
    
    genre_map = {"1": "cozy_mystery", "2": "noir", "3": "police_procedural"}
    genre = genre_map.get(genre_choice, "cozy_mystery")
    
    setting = input("背景设定: ") or "现代都市"
    
    return title, genre, setting

def main():
    """Main program"""
    try:
        # Load config
        config = load_config()
        setup_ai(config)
        
        # Get story parameters
        if len(sys.argv) > 1 and sys.argv[1] == '--interactive':
            title, genre, setting = interactive_mode()
        else:
            # Use config file
            story_config = config['story']
            title = story_config['title']
            genre = story_config['genre']
            setting = story_config['setting']
        
        print(f"\n生成大纲: {title}")
        print(f"类型: {genre}")
        print(f"背景: {setting}")
        
        # Generate outline
        print("\n正在生成大纲...")
        ai_content = generate_outline(title, genre, setting)
        outline_content = format_outline(title, genre, setting, ai_content)
        
        # Save outline
        outline_path = save_outline(title, outline_content)
        print(f"\n大纲已保存到: {outline_path}")
        
        # Display for review
        print("\n=== 生成的大纲 ===")
        print(outline_content)
        
        # Get approval
        approval = input("\n是否批准此大纲? (y/n): ").lower()
        if approval == 'y':
            print("大纲已批准，可以开始生成章节。")
        else:
            print("大纲未批准，请重新生成或修改。")
            
    except Exception as e:
        print(f"错误: {e}")

if __name__ == "__main__":
    main()
