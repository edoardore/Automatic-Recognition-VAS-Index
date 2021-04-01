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

# Original Code by: [Alessandro Arezzo](https://github.com/AlessandroArezzo/Automatic-Recognition-VAS-Index) (2021)


