# Workflow Automation Strategy: Taming the Chaos

## 1. The Plight: "Project Pivoting Whiplash"
You are dealing with a common but challenging friction point in development: **High-Cognitive-Load Context Switching**.

*   **The ADHD Factor**: Your mind wants to jump between "High-Level Creative" (Story Extension) and "Low-Level Engineering" (Model Distillation).
*   **The Friction**: The current workflow requires you to:
    1.  Write a prompt in a file.
    2.  Run a terminal command.
    3.  Wait.
    4.  Check a file.
    5.  Copy-paste if you want to iterate.
*   **The Result**: By the time step 3 is done, your brain has already jumped to a new idea, and the "waiting" breaks your flow. You need a system that **captures** your intent and **executes** it asynchronously, so you can dump the idea and move on without "babysitting" the process.

## 2. Assessment of Current Workflow
| Feature | Current (CLI Scripts) | Proposed (n8n / Visual) |
| :--- | :--- | :--- |
| **Trigger** | Manual command (`python script.py`) | Automatic (File Save / Webhook) |
| **Prompting** | Hardcoded or CLI arg | Visual Node (Easy to edit/version) |
| **Visibility** | Black box (Logs) | Visual Flow (See data pass through) |
| **Flexibility** | Requires coding to change logic | Drag-and-drop nodes |
| **Cognitive Load** | High (Remembering args/paths) | Low (Set and forget) |

**Conclusion**: The CLI scripts are great for *production* (when the pipeline is fixed), but terrible for *exploration* (when you are still figuring out what you want). You need a **"Rapid Prototyping Pipeline"**.

## 3. The Solution: n8n "Factory" Architecture
We will treat your content generation like a factory line. You just put raw material (Markdown) into a box, and the factory spits out the finished product (Audio).

### Core Philosophy: "File-System as UI"
Since you are already editing Markdown files, we should use **File Changes** as the trigger. You shouldn't have to leave your editor (VS Code) to run the pipeline.

### Proposed n8n Workflow
We will build a workflow that watches your `z-Content-Raw` folder.

#### **Phase 1: The Distiller (Raw -> Script)**
1.  **Trigger**: `Local File Trigger` (Watch `z-Content-Raw/*.md` for changes).
2.  **Read File**: Read the content of the modified file.
3.  **Router**: Check the file tag or folder (e.g., is it `#story` or `#lesson`?).
4.  **LLM Chain (Gemini)**:
    *   **Input**: Raw Content + System Prompt (loaded dynamically).
    *   **Task**: "Distill this into a script."
    *   **Refinement Loop (Optional)**: "Critique this script. Is it natural? If not, rewrite."
5.  **Write File**: Save the output to `z-Content-Distilled/[filename]_script.md`.

### Dynamic Prompting: Experimentation without Complexity
To handle your need for different prompts (Stories vs. Lessons) or experimental ones, we will use a **Tag-Based Routing System**.

1.  **The Trigger**: You add a tag to your raw filename or content (e.g., `my_story_#story.md` or `my_lesson_#lesson.md`).
2.  **The Router**: The n8n workflow detects this tag.
3.  **The Loader**: n8n reads the corresponding prompt file from `z-Prompts/`.
    *   `#story` -> loads `05_Distill_Story_Script.md`
    *   `#lesson` -> loads `04_Distill_Lesson_Script.md`
    *   `#experimental` -> loads `06_Experimental.md`
4.  **The Benefit**: You don't change the workflow to test a new idea. You just:
    *   Create `z-Prompts/07_New_Idea.md`.
    *   Save your content as `test_#newidea.md`.
    *   The system automatically pairs them.

#### **Phase 2: The Producer (Script -> Audio)**
1.  **Trigger**: `Local File Trigger` (Watch `z-Content-Distilled/*.md` for changes).
2.  **Parser**: Extract `**Speaker**:` blocks (using a Code Node or Regex).
3.  **Iterator**: Loop through each segment.
4.  **ElevenLabs API**:
    *   **Input**: Text segment + Voice ID (mapped from Speaker name).
    *   **Action**: Generate Audio.
5.  **Stitcher**: (Optional) Combine segments using `ffmpeg` (via Execute Command node).
6.  **Write File**: Save final MP3 to `output/`.

## 4. Implementation Steps
1.  **Install n8n**: `npm install n8n -g` (or Docker).
2.  **Setup Credentials**: Add Gemini and ElevenLabs API keys in n8n.
3.  **Build "The Distiller"**:
    *   Create a workflow that listens to your raw folder.
    *   Connect it to the Gemini node.
    *   Test it by saving a file in VS Code and watching the script appear automatically.
4.  **Build "The Producer"**:
    *   Create a workflow that listens to the distilled folder.
    *   Connect it to ElevenLabs.

## 5. Why this helps your ADHD
*   **Instant Gratification**: You hit "Save", and 30 seconds later, audio appears.
*   **Separation of Concerns**:
    *   When you feel creative? Just write Markdown in `z-Content-Raw`.
    *   When you feel like engineering? Go into n8n and tweak the nodes.
*   **No Context Switching**: You stay in your text editor for the creative work. The "terminal" is gone.
