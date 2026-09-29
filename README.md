\# M\&A Integration Memory Agent



Built for HackwithHyderabad 3.0, using Hindsight (Vectorize) as the memory layer.



\## The problem

When two companies merge, integration decisions get made in scattered meetings over weeks.

Nobody has perfect recall of what was decided, by whom, or when. Conflicting proposals

slip through because the person who made them didn't know a decision already existed.



\## What this agent does

It retains every integration meeting note into a Hindsight memory bank. When a new proposal

comes in, it reflects against that memory and catches contradictions with prior decisions,

citing exactly who decided what and when.



\## Demo

Run `demo.py` for a four-part demo:

1\. A question asked against an empty memory bank (no context)

2\. The same question after 19 meeting notes are loaded, correctly identifying the

&#x20;  Azure migration decision made by VP of Engineering Derek Huang

3\. A new proposal that contradicts that decision, caught and explained with full context

4\. A query surfacing every integration decision still unresolved



\## Setup

1\. `pip install -r requirements.txt`

2\. Copy `.env.example` to `.env`, add your Hindsight API key

3\. `python ingest.py` to load the seed data

4\. `python demo.py` to run the demo



\## Stack

Python, Hindsight Cloud (retain/reflect), FastAPI + vanilla HTML for the optional web demo.

