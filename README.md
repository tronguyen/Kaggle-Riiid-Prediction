# Kaggle-Riiid-Prediction

## Method-1: 

**DeepFM** for [Riiid! Answer Correctness Prediction](https://www.kaggle.com/c/riiid-test-answer-prediction)

1. Training
- Incremental training for incoming data batches
- DeepFM model applied with Pooling Bi-Interaction features (NeuralFM).

2. References
- [DeepFM](https://arxiv.org/pdf/1703.04247.pdf)
- [NeuralFM](https://arxiv.org/pdf/1708.05027.pdf)


## Method-2:

Apply **Transformer** for modeling sequential user interactions.

1. Training
- Incremental training style, all user data will be stored as dictionary.
- Data loader is under the form as below:
    - Historical user data (encoder)
    - New user-data for prediction (decoder)

- Params:
    - Max-seq-length: 32
    - Model size: equivalent to *Bert-Mini*
    - Data size: 3mil instances

2. References

- [Transformer](https://arxiv.org/abs/1706.03762)
- [SAINT+](https://arxiv.org/pdf/2010.12042.pdf)