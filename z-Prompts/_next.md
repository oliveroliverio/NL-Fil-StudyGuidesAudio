## Questionining this entire workflow

Next, I'd like to extend this story...But first.. I wonder if this gemini prompt, copy paste prompt workflow is inefficient... I wonder if I can n8n this workflow to make it more efficient. I'm hoping to solve these painpoints
- initial prompt development I write, then having an LLM make that prompt "better" to get "better" output whether it be code basees, or in this case, "distilled content" from "raw content"
- project pivoting whiplash:  I have ADHD and I want to do so many things simultaneously: (TTS_model_distilation, story extension, prompt organization and managing raw content vs distilled content).  I need a system that can be accomodating and flexible for this scattered thinking.  
- what do you recommend?  I only thought of n8n because of the "node-like" workflow that allows me to plug and play various parts of the system (prompts, APIs, services, etc), but I'm not married to any particular technology.  I just need a methodology of taming my chaotic mind and creating a system that produces good content/results

Write a markdown document that explains my plight, asssess the issues and explores potential solutions, and then converts this entire workflow into an n8n workflow, and place inside @z-Dev-Docs 

---

This is great!  But what about the issue of experimenting with various prompts?  Note, how I have various prompts depending on the kind of audiobook I'd like to create, is there a way to add this into the n8n workflow whilst minimizing complexity?  

## creating distilled content

How do we move forward with this project?  I renamed content directories to z-Content-Raw and z-Content-Distilled where raw content is original markdown files containing unstructured lessons, and z-Content-Distilled is where you (or another LLM) processes the raw-content and distills it into a structured format (in this case, transcriptions that will be sent to Elevenlabs for audio generation).  I have example distilled content in... but this was for generating PDF study guides.  The question is, how should this content be structured for audio generation?  And what prompt should I give you (or another LLM) to generate this distilled content? 

what prompts did you use (and which/what do you recommend for generating distilled content?).  Note: I'd like to have multiple types of audio:
- audiobook stories implementing the lessons
- audiobook lessons themselves where the content is more "expository."

---

# Archive

## 251125

I think I want to switch to the Gemini 3 API rather than OpenAI. 

This is a great first start!  But I think I want a 3rd party API for audio file generation that specializes in audiobook creation for more natural sounding oral audio.  We can keep the the current LLM (or switch to Gemini 3) for creating the transcripts for stories and lessons.  But for oral audio generation, I want to explore better options, possibly even paid ones if the output is audible audiobook sounding. 

Don't code anything for now, simply write your ideas and next steps in this file.  
