# 73rd Deep Learning Meetup: Optimizers / Speech Recognition in Air Traffic

https://www.meetup.com/vienna-deep-learning-meetup/events/314528251/

Hi Deep Learners,

We are happy to announce our next Vienna Deep Learning Meetup on May 19 at Bosch. Our topics this time are: Improved Optimizers for Deep Learning and Automatic Speech Recognition in Air Traffic Management.

## Agenda:

* 18:15 Arrival
* 18:30 Introduction by the meetup organizers
* Welcome by the host: Bosch
* 18:45 Talk 1: Momentum, Preconditioning, and Beyond: Practical Advances in Optimization by Ionut-Vlad Modoranu (ISTA)
* 19:30 Announcements
* Networking Break
* 20:00 Talk 2: Cleared for Takeoff: Automatic Speech Recognition in Air Traffic Management by Christian Sobtzick & Sahebeh Dadboud (Frequentis)
* 20:45 Networking
* ~21:30 Wrap up & End

## Talk Details:

### Talk 1: Momentum, Preconditioning, and Beyond: Practical Advances in Optimization
Modern Deep Learning optimization is largely dominated by first-order methods such as Adam, yet their limitations in memory usage, scalability, and curvature awareness motivate the search for improved alternatives. This talk provides a practical perspective on optimization, starting from the roles of momentum and preconditioning and extending to recent advances that go beyond standard adaptive methods.

We present techniques that improve optimization along three key axes: memory, structure, and computational efficiency. In particular, we introduce MicroAdam, a memory-efficient variant of Adam based on compressed optimizer states; Trion, a low-rank method that replaces costly SVD/QR projections with efficient, rank-independent alternatives; and DASH, a GPU-efficient implementation of Shampoo that accelerates second-order preconditioning via improved parallelization and fast matrix inverse root approximations.

Together, these methods illustrate how careful algorithmic and systems-level design can overcome the practical limitations of existing optimizers, offering a path toward scalable, memory-efficient, and high-performance training beyond Adam.

**About the speaker:**
Ionut-Vlad Modoranu is a PhD student at the Institute of Science and Technology Austria (ISTA), specializing in efficient optimization for Deep Learning. His research focuses on reducing the memory usage and computational cost while maintaining the performance, including the development of practical optimizers for large-scale models, with publications at top tier international conferences.

### Talk 2: Cleared for Takeoff: Automatic Speech Recognition in Air Traffic Management
Automatic Speech Recognition (ASR) has made tremendous progress in recent years. However, its deployment in safety‑critical operational environments poses a fundamentally different set of challenges compared to demonstration systems or research prototypes. In this talk, we present how speech‑to‑text models are used in a real Air Traffic Management (ATM) product at Frequentis. We walk through the end‑to‑end lifecycle of an ASR system: how training data is collected and curated, how models are selected and evaluated, and what it takes to deploy and operate them reliably for customers in a regulated, safety‑critical domain. Beyond the models themselves, we discuss practical challenges from bringing ASR from research into production, where reliability and trust matter as much as accuracy.

**About the speakers:**
Sahebeh (Saba) Dadboud is an Expert Data Scientist at the Frequentis AI Competence Centre. With over eight years of experience in the tech industry, she specializes in bridging Deep Learning, MLOps, and product development to build trustworthy AI for safety-critical systems. At Frequentis, she plays a pivotal role in driving company-wide AI initiatives, supporting the adoption of advanced technologies in domains where reliability, safety, and strict regulatory constraints are absolutely critical. She holds a Master’s degree in Computational Science from the University of Vienna.
Christian Sobtzick is Audio Expert at Frequentis, leading the HET Audio Competence Centre. He is responsible for improving audio quality across all Frequentis voice communication products, drawing on more than 15 years of professional experience. In addition, he supports product development related to automatic speech recognition and contributes to research projects, such as the FFG “Next Generation Safety” project, which aimed to enable AI‑based automation in Air Traffic Management. His background is the field of acoustics, including electroacoustic transducers, acoustic measurements, and signal processing. He holds an MSc in Electrical Engineering and Audio Engineering from Graz University of Technology and the University of Music and Performing Arts Graz.

We are looking forward to welcoming you at our next meetup.
Your VDLM organizer team.
