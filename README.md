# Automatic-Recognition-VAS-Index

Nel progetto si implementa di un sistema di riconoscimento automatico del dolore provato da una persona in scala VAS da 0 a 10 (Visual Analog Scale).
* Analisi della sequenza di frames in cui la faccia del soggetto viene mostrata
* Predizione del dolore percepito in base alla posizione di landmarks facciali

# Prerequisites
```python
pip install scikit-learn v.0.23.1
pip install pandas v.1.0.5
pip install matplotlib v.3.2.2
pip install numpy v.1.19.0
pip install seaborn v.0.11.0
```

# Modifiche Realizzate:
* Decomposto il moulo dei vettori di moto dei landmark facciali in singole componenti x ed y nel file: PreliminaryClustering.py in __get_velocities_frames()
* Aggiunte le due componenti x ed y del moto della punta del naso corrispondenti al landmark numero 30, modificata la lista dei landmark considerati in: config.py
* Risultati ottenuti: l'aggiunta delle modifiche in __get_velocity_frames() degrada sfortunatamente le performance nella predizione rispetto alla versione originale.

# Modifiche Realizzate 2:
* Aggiunta di: 
```python         
self.__test_kernel_frames(11, [199, 200, 201, 202])
```
estrae i kernel di appartenenza dei frames nella lista della sequenza 11 e mostra successivamente per ogni cluster quali altri frames, anche di altre sequenze vi appartengono. 

# Modifiche Realizzate 3:
* Si effettua il clustering solamente su elementi del dataset con VAS >= della soglia presente in config.py

# Modifiche Realizzate 4:
* Aggiunto vel_plot.py che riceve in ingresso il nome di una sequenza ed un elenco dei landmarks di interesse, produce un grafico a barre con il numero di frame nell'asse X e sull'asse Y la somma dei moduli della velocità dei landmarks di interesse. Le velocità dei landmarks si misurano rispetto al baricentro del volto e alla punta del naso si associa la velocità del baricentro. 

# Modifiche Realizzate 5:
* Aggiunta sogliatura dei frame per cui si effettua il training nel clustering preliminare. Il metodo __get_relevant_frame(self) permette di estrarre i frame rilevanti andando a sogliare il grafico realizzato in modifiche 4 dopo un processo di smoothing con moving average. Al posto di calcolare le velocità rispetto alla punta del naso si calcolano rispetto al baricentro dei landmarks e si aggiunge alla punta del naso la velocità del baricentro stesso.
* Attualmente la versione con performance migliori ha i seguenti parametri:
* 32 kernels, threshold_VAS>=9, threshold_vel_frames>6, Landmarks come in Arezzo + 30 (nose tip)
 
 # Modifiche Realizzate 6:
 * Concatenato al vettore velocità anche il vettore posizione dei landmark di interesse. Nel clustering preliminare si calcola la GMM con l'aggiunta delle coordinate x ed y per i frames delle sequenze di interesse. I risultati mostrano un peggioramento, la versione migliore rimane attualmente la numero 5.
 
 # Modifiche Realizzate 7:
 * Implementato il nuovo modulo python tesy_accuracy.py: esegue in sequenza i test in vari scenari.
 * Test with landmarks: 1) eyes, 2) mouth, 3) eyes + mouth, 4) all, standard
 * Test with different number of kernel in clusters: 16, 32, 64, 128
 * Getting clusters: 1) with all the sequences of train, 2) only with sequences with VAS greater than K = 6, 7, 8, 9
 * Landmark's description with: 1) only position, 2) only velocity, 3) position and velocity
 * Sequence's description with: 1) all the available frames, 2) a window of N frmaes centered in the frame with max dynamic
 
 ## Risultati dei 16 esperimenti visibili in ./test_accuracy
 
### Original Code by: [Alessandro Arezzo](https://github.com/AlessandroArezzo/Automatic-Recognition-VAS-Index) (2021)


