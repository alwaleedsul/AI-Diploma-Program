#!/usr/bin/env python3
"""
Remove empty quiz folders from modules/units since quizzes are now centralized in QUIZZES/ folders.
"""

from pathlib import Path

BASE_DIR = Path("/Users/abdullah/Downloads/AI Diploma")

def find_empty_quiz_folders():
    """Find all empty quizzes folders."""
    empty_folders = []
    
    for course_num in range(1, 7):
        course_dir = BASE_DIR / f"Course 0{course_num}"
        if not course_dir.exists():
            continue
        
        # Find all quizzes folders
        for quiz_folder in course_dir.rglob("quizzes"):
            if quiz_folder.is_dir():
                # Check if folder is empty
                files = list(quiz_folder.iterdir())
                if not files:
                    empty_folders.append(quiz_folder)
                else:
                    # Check if only has .gitkeep or similar
                    non_gitkeep = [f for f in files if f.name != '.gitkeep']
                    if not non_gitkeep:
                        empty_folders.append(quiz_folder)
    
    return empty_folders

def main():
    """Remove empty quiz folders."""
    print("=" * 80)
    print("Finding and Removing Empty Quiz Folders")
    print("=" * 80)
    print()
    
    empty_folders = find_empty_quiz_folders()
    
    if not empty_folders:
        print("✅ No empty quiz folders found")
        return
    
    print(f"Found {len(empty_folders)} empty quiz folders:\n")
    
    for folder in sorted(empty_folders):
        rel_path = folder.relative_to(BASE_DIR)
        print(f"  - {rel_path}")
    
    print(f"\n{'=' * 80}")
    response = input(f"\nRemove {len(empty_folders)} empty quiz folders? (yes/no): ")
    
    if response.lower() in ['yes', 'y']:
        removed = 0
        for folder in empty_folders:
            try:
                folder.rmdir()
                removed += 1
                print(f"  ✅ Removed: {folder.relative_to(BASE_DIR)}")
            except OSError as e:
                print(f"  ⚠️  Could not remove {folder.relative_to(BASE_DIR)}: {e}")
        
        print(f"\n✅ Removed {removed} empty quiz folders")
    else:
        print("Cancelled. No folders removed.")

if __name__ == "__main__":
    main()

