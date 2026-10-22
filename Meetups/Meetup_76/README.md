# 76th Deep Learning Meetup: LLM Fine-Tuning / Agent Harnesses

21 Oct 2026 @ FH Technikum Wien

https://www.meetup.com/vienna-deep-learning-meetup/events/316682904/

Hi Deep Learners,

We are happy to announce our upcoming Vienna Deep Learning Meetup on October 21 at FH Technikum Wien. Our Agenda:

## Agenda:

* 18:15 Arrival
* 18:30 Welcome by the meetup organizers
Introduction by the hosts
* 18:45 Talk 1: MatryoshkaLoRA: Learning Accurate Hierarchical Low-Rank Representations for LLM Fine-Tuning by Ionut-Vlad Modoranu (ISTA)
* 19:30 Announcements
* Networking Break
* 20:00 Talk 2: On Agent Harnesses and Finding New Abstractions by Benjamin Strasser and Jacob Palecek (aots)
* 20:30 Networking
* ~22:00 Wrap up & End

## Talk Details:

### Talk 1: MatryoshkaLoRA: Learning Accurate Hierarchical Low-Rank Representations for LLM Fine-Tuning

With the rise in scale for deep learning models to billions of parameters, the computational cost of fine-tuning remains a significant barrier to deployment. While Low-Rank Adaptation (LoRA) has become the standard for parameter-efficient fine-tuning, the need to set a predefined, static rank r requires exhaustive grid searches to balance efficiency and performance. Existing rank-adaptive solutions such as DyLoRA mitigate this by sampling ranks during the training from a predefined distribution. However, they often yield sub-optimal results at higher ranks due to lack of consistent gradient signals across the full hierarchy of ranks, thus making these methods data-inefficient.

In this talk, we propose MatryoshkaLoRA, a general, Matryoshka-inspired training framework for LoRA that learns accurate hierarchical low-rank representations by inserting a fixed, carefully crafted diagonal matrix P between the existing LoRA adapters to scale their sub-ranks accordingly. By introducing this simple modification, our general framework recovers LoRA and DyLoRA only by changing P and ensures all sub-ranks embed the available gradient information efficiently.

Our MatryoshkaLoRA supports dynamic rank selection with minimal degradation in accuracy. We further propose Area Under the Rank Accuracy Curve (AURAC), a metric that consistently evaluates the performance of hierarchical low-rank adapters. Our results demonstrate that MatryoshkaLoRA learns more accurate hierarchical low-rank representations than prior rank-adaptive approaches and achieves superior accuracy performance trade-offs across ranks on the evaluated datasets

**About the speaker:**

Ionut-Vlad Modoranu is a PhD student at the Institute of Science and Technology Austria (ISTA), specializing in efficient optimization for deep learning. His research focuses on reducing the memory usage and computational cost while maintaining the performance, including the development of practical optimizers for large-scale models, with publications at top tier international conferences.

### Talk 2: On Agent Harnesses and Finding New Abstractions

Teams and startups across the world have started to build their own custom LLM harnesses, and so have we. Harnesses are what truly enable some of LLMs' most powerful use-cases. Given our experience writing those, including through a OpenAI-hackathon-winning submission, we share lessons learned, engineering practices and helpful patterns. Along the way we’ll give insights into how we expect this to change our daily work, share what we’re currently building, and discuss the fundamental challenge of designing this type of software: finding fitting abstractions. Expect to walk away with a software engineering perspective on harnesses.

**About the speakers:**

Benjamin Strasser and Jacob Palecek are Lead Software Engineers and co-founders of Ahead of Time Software (aots), a Vienna-based software engineering agency building custom software, augmenting customer teams with specialized expertise, and delivering end-to-end services across the software development lifecycle. Benjamin Strasser holds an MSc in Computer Science and has a background in software engineering and Web3. His work focuses on full-stack software engineering across a wide range of clients, industries, and project roles. Jacob Palecek holds a Dipl.-Ing. in Computer Science and has a background in distributed systems research and security. He brings broad experience across the software stack, including work in the custom software industry and as a freelance software engineer.

We are looking forward to welcoming you at this meetup!
Your VDLM organizer team
