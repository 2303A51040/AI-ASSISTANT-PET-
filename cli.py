from memory_meeting_ai.store import init_db, add_note, recent_notes
from memory_meeting_ai.meeting import save_meeting

def main():
    init_db()
    while True:
        print("\nNEXUS Memory & Meeting AI\n1. Add note\n2. Show recent notes\n3. Summarize/save meeting transcript\n4. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_note(input("Title: "), input("Note: "))
            print("Note saved.")
        elif choice == "2":
            for row in recent_notes():
                print("\n", row[0], "-", row[2], "\n", row[1])
        elif choice == "3":
            title = input("Meeting title: ")
            print("Paste transcript; finish with a line containing END:")
            lines = []
            while True:
                line = input()
                if line.strip() == "END":
                    break
                lines.append(line)
            print("Summary:", save_meeting(title, "\n".join(lines)))
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
