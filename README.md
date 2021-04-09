# Automatic-Recognition-VAS-Index

Nel progetto si implementa di un sistema di riconoscimento automatico del dolore provato da una persona in scala VAS da 0 a 10(Visual Analog Scale).
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

# Risultati ottenuti:
Si mostra di seguito la matrice di confusione con 3 livelli di dolore nella versione originale proposta da Arezzo:
![originale](https://github.com/edoardore/Automatic-Recognition-VAS-Index/blob/master/ImplementazioneOriginale.png)

L'aggiunta delle modifiche in __get_velocity_frames() degrada sfortunatamente le performance nella predizione.
![modifiche](https://github.com/edoardore/Automatic-Recognition-VAS-Index/blob/master/Modifiche.png)

# Modifiche Realizzate 2:
* Modifica di selected landmark con quelli di occhi + sopracciglia
* In PreliminaryClustering.py nel metodo __generate_histograms(self) si traccia il frame della sequenza che è al centro del cluster considerando l'elemento massimo che infulisce nella somma dei FisherVector per costituire l'istogramma. I frame relativi al centro cluster vengono salvati in un nuovo attributo self.centroids_frame_of_sequence ovvero un array di dimensione (#sequenze x #kernel GMM).
*  È stato implementato un nuovo metodo def __test_centroid_cluster_frame_velocity(self) che considerando i frame di centro cluster estratti precedentemente preleva le velocità medie dei landmark nei frame dei centroidi e le inserisce in un file excel. Il relativo file [cluster_velocity.xlsx](https://github.com/edoardore/Automatic-Recognition-VAS-Index/blob/master/cluster_velocity.xlsx) nello specifico mostra la velocità media dei vettori di moto nei frame centro cluster nelle 200 sequenze. Si ha dunque: #righe=#kernel della GMM 16, #colonne=#sequenze 200. confrontando le colonne del file tenendo fissa una riga si nota che ogni cluster ha associata una velocità media nelle varie sequenze costanti con alcuni lievi picchi, il che fa ben sperare dal punto di vista della clusterizzazione che si comporta in modo corretto.
* Scrittura di plot.py utile per comprendere la corrispondenza tra un landmark e id associato, mostra in modo visuale il plot dei landmarks (questo file non è interessante ai fini del miglioramento delle prestazioni)
# Original Code by: [Alessandro Arezzo](https://github.com/AlessandroArezzo/Automatic-Recognition-VAS-Index) (2021)


