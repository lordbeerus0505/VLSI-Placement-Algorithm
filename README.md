# VLSI-Placement-Algorithm

### Objective

To build a fully-integrated, cloud-based solution for optimal VLSI placement both using a highly data-driven processing pipeline.

### Concept

VSLI placement can be performed by using several algorithms such as partition-based techniques, analytic methods, simulated annealing, and so on. Our solution constitutes a metaheuristic which determines the algorithm to be used in two phases:

determining optimal placement algorithm based on the constraints of power, speed and space:
#### a. Power: 
The power concentration is calculated by segmenting the circuit footprint into clusters. The power dissipation for each of these clusters is calculated following which a heatmap of the power concentrated regions is generated. In this case, the placement design with the least amount of power concentration is selected as the most efficient and is the desired design.

Power Concentration of Cluster=PiAreai Pi= Maximum Power dissipated by net or block Areai=Area of Blocki

#### b. Speed: 
Speed optimisation is achieved by implementing a placement design with minimum amount of clock skew. Clock skew is calculated by measuring length of nets based on which the path impedance is calculated which is proportional to the clock skew. A higher clock skew implies lower speeds due to time lost for synchronization. A placement design with minimum total clock skew is selected as the desired design. A possible extension we plan to work on is to weigh the clock skew values based on the importance of the block, for instance a block with critical functionality is given a higher weight parameter hence relating in a small change in its time skew resulting a huge overall skew value of the circuit

Weighted Time Skew=wi.ti skew

#### c. Space: 
The placement design with the smallest footprint is used.

modelling each of these variable correlations for the type of input configuration, as well as the selected algorithm performance metrics and storing them in memory so that they may be used in subsequent jobs to prune the search space. This results in a memory-based model that preemptively reduces computational expsense as well as producing the most optimal list of methods using the learned correlations.
Further in the metaheuristic pipeline we also incorporate a variation of an adversarial autoencoder with multiple learned priors to model possible topologies. From recent literature, generative machine learning models, specifically convolutional autoencoders have been found to synthesize VLSI layout patterns with high diversity more effectively than state-of-the-art algorithms, capturing simple design rules and geometry information of existing topolgies. This will capture an input configuration requiring a diverse array of placement layouts, further adding to the capabilities of the core metaheuristic.

### Implementation

Our solution supports both a Python-Tkinter offline application, as well as a larger-scale cloud application for distributed production workloads with Python-Flask, various graphing libraries such as Bokeh, and Docker with AWS ECS. This application has a completely serverless backend, with its various pipelines modelled in AWS Step Functions, resulting in a highly resilient, scalable, cost-efficient architecture.
There are two access methods: a REST API endpoint where JSON requests encapsulating the input parameters may be submitted to retrieve an output web page containing the relevant reporting; and, an interactive wizard-based web application that performs the same function.
On the first input of user parameters, the metaheuristic (running either locally or on serverless containers) determines the most optimal algorithms and generates placement configurations, simultaneously logging learned constraint (speed, power and space) correlations and performance metrics for different algorithms for the given input configuration. The cloud setup fully leverages the microservices paradigm of logging sidecars with several single-use distributed containers running jobs parallely. For understanding these "meta" parameters learnt, we utilize a simple Elasticsearch-Logstash-Kibana stack.
On subsequent trials, the metaheuristic traverses this memory store based on similarity of the current input configuration to past inputs as well as the learned constraint correlations, so as to prune the algorithm pool further. This eliminates redundant computation and reinforces the metaheuristic using a dynamic programming approach.
The output obtained is a web-based report containing a ranked list of optimal placements with graphical representations, as well as useful visualizations such as estimated heatmaps of power and clock skew.
The efficacy of past placement jobs can further be automatically validated by the Step Functions workflow, depending on whether it is discarded by the user, selected for routing, and so on so as to further strengthen the metaheuristic - these are very easily setup as they operate on simple, light-weight triggers.
Our own model of adversarial autoencoders is also trained in tandem with Keras-Theano with the above data points, after an initial training with the existing dataset.
### Applications

Being a cloud-oriented serverless solution with an easily accessible REST endpoint, the possibilities of optimized process automation when integrated into existing systems/IoT are immense.
The solution combines established methods as well as new experimental methods observed to better state-of-the-art techniques such that they form an algorithm pool that the best fit for a given input configuration is chosen from.
Hence they can be used for a variety of placement jobs and can learn the nuances of the circuitry being fabricated by a manufacturer over time.
Viewing the correlations and algorithmic performance metrics can provide valuable insight into not-immediately-apparent ways in which design constraints influence VLSI placement.




### Execution
Make changes to the 
##### main.cc 
file and run the Makefile. The compiled output can be visualised by running the perl command -
##### tofig.pl -a 1.0 -f 22 $1 | fig2dev -L ps | ps2pdf -dEPSCrop - $1.pdf
replacing $1 with file name. Run the 
##### pdftoimg.py
to convert into a png.
Run 
##### findArea.py
to calculate the area.
