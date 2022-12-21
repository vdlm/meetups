# 46th Deep Learning Meetup in Vienna

* Date: 2022-11-17
* Venue: Technikum Wien
* Meetup Page: https://www.meetup.com/vienna-deep-learning-meetup/events/289599174/

[[Slides](<./slides/20221117 46th VDLM.pdf>)]

## Details

Hi everyone,

please join us next week on Nov 17 for our next meetup!

Following an overview by Bernhard Knapp over the research and teaching activities of the FH Technikum in the field of Machine Learning, will be have Marc Javin (emotion3d.ai) presenting

Eye Analysis: Designing a Neural Network for the Automotive Industry,

followed his colleague Georg Braun with

Going Embedded: Real-time Deep Learning for automotive applications.

They will highlight how a Vienniese company is providing large scale state of the art solutions, comprising tightly integrated software & hardware, to the automotive industry. You can find the detailled abstract for their talks below!

____

After the break we will have a Hot Papers session covering a wide range of topics, this time presented by Liad Magen, Franz Fürbass and René Donner.

Hope to see you there! For the VDLM team,

Rene

_________________________________________________________

Marc Javin, emotion3d.ai
Eye Analysis : Designing a Neural Network for the Automotive Industry

According to the WHO, 94% of road accidents are caused by human error. Driver Monitoring Systems detect dangerous situations such as driver drowsiness and distraction and thus help avoid a majority of accidents. Numerous regulators around the world, among them the European Commission, have recognized this and implemented road safety policies mandating driver monitoring systems into new cars.

One crucial element of a Driver Monitoring System is determining what the driver is looking at in real-time. Designing an algorithm predicting the eye gaze vector of a driver poses multiple challenges, especially in an automotive context: We must fulfill stringent safety requirements, run on low-power embedded devices in real time with high accuracy and generate large amounts of difficult to obtain high-quality training data.

During our presentation, we will give insights in how we develop this algorithm, tackling multitask learning, runtime optimization and data generation under the challenging conditions of the automotive industry.

Georg Braun, emotion3d.ai
Going Embedded: Real-time Deep Learning for automotive applications

When developing Deep Learning based algorithms, the initial focus is typically on optimizing the accuracy of the neural networks´ predictions. However, for deploying the networks in commercial automotive products, in most cases it is equally important that a network can be executed efficiently on resource constrained embedded edge devices.

We will present a state-of-art workflow for developing deep learning algorithms for high-performing automotive-grade embedded platforms. Both higher end devices, such as Nvidia´s CUDA-enabled Jetson platform, as well as less powerful devices, equipped with an ARM-processor and dedicated neural network accelerators, are considered.

Furthermore, we present the inference runtimes of our in-house developed networks on various embedded devices and the quality loss we experienced due to model quantization.
