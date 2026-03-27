# Cognitive Diagnostic Assistant 

##  Why I built this
As a high school politics teacher, I've seen a growing trend: students use AI to get "perfect" answers without actually thinking. In my classroom, I want to see struggle and inquiry, not just copy-pasted results.

I built this assistant to change the conversation. Instead of giving answers, it acts as a " questioner". It takes a student's statement and pushes back, forcing them to define their terms and defend their logic.

##  Core Methodology
Instead of providing direct answers, the assistant employs a diagnostic framework based on three pillars:
1. **Premise Excavation**: Identifying unstated assumptions in the student's viewpoint.
2. **Definitional Precision**: Forcing a clear boundary for abstract social science concepts.
3. **Consistency Verification**: Testing the internal logical coherence of the argument.

##  Technical Implementation
- **Architecture**: Python 3.13 / OpenAI-compatible SDK.
- **Model**: DeepSeek-V3 (via API).
- **Security**: Designed for API-key-based deployment with focus on low-latency response.

##  Deployment
Ensure Python 3.12+ and `openai` library are installed. Replace the `api_key` placeholder in the source code with a valid DeepSeek key.
