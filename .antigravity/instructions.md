# AI Agent Instruction Guide

## 1. Project Context
- **Course**: KMITL Data Structure & Algorithms (01276122)
- **Student ID**: 68011309

## 2. Portal & Data Import Workflow
- **Authentication**: Authenticate to the KMITL portal `https://python.compro.kmitl.ac.th` via CodeIgniter session using a POST request for login.
- **Session Maintenance**: Fetch exercises via a GET request to `/index.php/student/exercise_home` to maintain an active session.

## 3. Solution Code Formatting Standards
When generating or modifying solution code, adhere to the following structure:
1. **Remove Site Header Comments**: Do not include any site-specific header comments.
2. **Top of File**: Include a problem statement docstring detailing Inputs, Outputs, and a brief Description.
3. **Middle**: Provide clean, well-commented Python solution code.
4. **Bottom**: Add a "How it works" section with a step-by-step breakdown of the algorithm.
5. **File Naming**: Use exact, descriptive titles (e.g., `item_1_Rabbit_Turtle_Fly.py`). Do not use generic names like `item_1_Item_1.py`.

## 4. Secure Credential Handling
- **Environment Variables**: Use environment variables (`KMITL_STUDENT_ID`, `KMITL_PASS`, `GITHUB_TOKEN`) for all credentials.
- **Data Masking**: Mask sensitive data (such as environment variables or use secure prompt fallbacks) to ensure raw passwords are never pushed to public repositories.

## 6. Quiz & Scope Guidelines
- **Quiz 1 Focus**: Primary focus on Chapter 3 (Stack), Chapter 4 (Queue), and Chapter 5 (Linked List).
- **Refresher Scope**: Chapters 1 & 2 (Python basics & OOP) serve as foundational refresher reference notes.
- **Verification**: Ensure all markdown and app content are free of mangled characters or broken symbols (plain ASCII / clean UTF-8).

