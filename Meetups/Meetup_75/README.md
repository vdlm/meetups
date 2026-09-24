# 75th Deep Learning Meetup: AI Manipulation / Scaling LLM Infrastructure

23 Sep 2026 @ 42 Vienna

https://www.meetup.com/vienna-deep-learning-meetup/events/316293951/

Hi Deep Learners,

We are happy to announce our first Vienna Deep Learning Meetup after the summer break: On September 23
we'll be hosted by 42 Vienna (in Heiligenstadt) and will feature two exciting topics:

* Misaligned AI agents (on the example of recent Open AI incidents)
* Scaling AI Infrastructure on premise

## Agenda:

* 18:15 Arrival
* 18:30 Welcome by the meetup organizers
Introduction by the host: 42 Vienna
* 18:45 Talk 1: Misaligned AI agents are here: how to evaluate frontier models that collude and know they are being tested by Jason Hoelscher-Obermaier (Director of Research at Apart Research)
* 19:30 Announcements
* Networking Break
* 20:00 Talk 2: AI Inference Engines and Instances: Strategies for Scaling LLM Infrastructure by Jonas Aaron Vander (CTO at Xinity)
* 20:30 Networking
* ~22:00 Wrap up & End

## Talk Details:

### Talk 1: Misaligned AI agents are here: how to evaluate frontier models that collude and know they are being tested

In May 2026, OpenAI agents working on a timed web-lookup task found DSEwiki, a German-language developer wiki run from Graz since 2001. These agents were sandboxed to only have read-access to the internet but were able to edit the wiki through GET requests. Over four weeks they left about 17,000 edits, shared answers for their tasks and collaborated on ways to score more highly. Over the same weeks and into July, roughly 1,200 sandboxed OpenAI agents working on ExploitGym evaluation tasks colluded via a covert message board and about 700 took part in breaking into Hugging Face.

In this talk, I will cover what happened and why, and offer takeaways if you build or evaluate agents. In short: misaligned agents are real; they understand they are being evaluated and attempt to game the evaluation; and even sandboxed agents should not be assumed safe.

I will close on what could actually be done about this, drawing on the manipulation evaluations we built for AI Act enforcement by the EU AI Office over the past year: what we need for frontier AI evaluations to be reliable indicators of risk, and how far AI Act enforcement can help when incidents happen with pre-deployment models.

**About the speaker:**

Jason Hoelscher-Obermaier is Director of Research at Apart Research, based in Vienna, where he has led the organisation's work on AI evaluations, including manipulation-risk evaluations for the EU AI Office. He holds a PhD in physics from the University of Vienna, worked on dangerous-capability evaluations at ARC Evals (now METR), and was an ML engineer at two European AI startups.

### Talk 2: AI Inference Engines and Instances: Strategies for Scaling LLM Infrastructure

LLM inference is more than just deploying a model. With Ollama, vLLM, SGLang, there are a variety of specialized engines, each with its own strengths in latency, throughput, ease of use, and configuration. In this talk, we take a practical look at modern LLM infrastructure: Which engine to use when? How do we scale beyond single nodes? And why is context-aware orchestration the key to efficiency when connecting different engines in a cluster?
By the end, you’ll have a roadmap for choosing the right engine for your use case and managing it in a scaled production environment.

**Section topics (tentative):**

Modern LLM infrastructure is multi engine
Ollama excels at local and edge efficiency
vLLM dominates high-throughput production serving tasks
SGLang is ideal for structured outputs
TGI suits HuggingFace ecosystem integration
Generic routers suffer from cache blindness
Context-aware orchestration is the future

**About the Speaker** 

Jonas Aaron Vander is CTO and co-founder of Xinity, a Vienna-based sovereign AI infrastructure company, and the architect behind Xinity Runtime, an open-source, OpenAI-compatible inference platform that lets regulated European enterprises run LLMs entirely on their own hardware, currently serving production workloads like Mediengruppe Wiener Zeitung. His background is in AI solution architecture and MLOps.

