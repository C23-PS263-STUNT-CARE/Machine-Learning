# Stunting Detection

This repository contains notebooks documenting our research and modeling for stunting detection. 
The model structure is composed of pre-trained embedding layers followed by five dense layers, with the final dense layer using a sigmoid activation function.

| Information     | Value                                                                           |
|-----------------|---------------------------------------------------------------------------------|
| Model Structure | Dense - Dense- Dense - Dense - Dense(Sigmoid)                                                               |
| Model Input     | List of each feature                                                                                       |
| Model Output    | Sigmoid values ranging from 0 to 1, where 0 represents negative stunting and 1 represents positive stunting|

This model is being implemented on out system.

C23-PS263 Machine Learning Teams.
