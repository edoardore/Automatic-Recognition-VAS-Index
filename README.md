# Automatic-Recognition-VAS-Index

This project contains the implementation of an automatic recognition system for pain perceived by a person. <br>
The goal of the system is therefore to analyze a sequence of frames in which the face of a subject is represented 
and then predict his perceived pain level based on the position of the subject's facial landmarks. 
The pain level is represented with an integer index between 0 and 10 called VAS (Visual Analog Scale).

<h2>Prerequisites</h2>
To use the code you need to have the following libraries installed:
<ul>
  <li>scikit-learn v.0.23.1</li>
  <li>pandas v.1.0.5</li>
  <li>matplotlib v.3.2.2</li>
  <li>numpy v.1.19.0</li>
  <li>seaborn v.0.11.0</li>
</ul>

# Modifiche Realizzate:
* Decomposto il moulo dei vettori di moto dei landmark facciali in singole componenti x ed y nel file: PreliminaryClustering.py in __get_velocities_frames()
* Aggiunte le due componenti x ed y del moto della punta del naso corrispondenti al landmark numero 30, modificata la lista dei landmark considerati in: config.py

# Risultati ottenuti:

* Original Code by: [Alessandro Arezzo](https://github.com/AlessandroArezzo/Automatic-Recognition-VAS-Index) (2021)


