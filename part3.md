## SG

```bash
/usr/local/bin/python3 "hmm_part3.py"
100%|████████████████████████████████████████████| 18559/18559 [00:00<00:00, 133388.55it/s]
100%|██████████████████████████████████████████████| 2650/2650 [00:00<00:00, 322929.36it/s]
```

```bash
/usr/local/bin/python3 "EvalScript/evalResult.py" SG/dev.out SG/dev.p3.out

#Entity in gold data: 4301
#Entity in prediction: 4583

#Correct Entity : 2217
Entity  precision: 0.4837
Entity  recall: 0.5155
Entity  F: 0.4991

#Correct Sentiment : 1808
Sentiment  precision: 0.3945
Sentiment  recall: 0.4204
Sentiment  F: 0.4070
```


## EN

```bash
/usr/local/bin/python3 "hmm_part3.py"
100%|███████████████████████████████████████████████| 7663/7663 [00:00<00:00, 79173.10it/s]
100%|██████████████████████████████████████████████| 1094/1094 [00:00<00:00, 267695.50it/s]
```

```bash
/usr/local/bin/python3 "EvalScript/evalResult.py" EN/dev.out EN/dev.p3.out

#Entity in gold data: 13179
#Entity in prediction: 14283

#Correct Entity : 10635
Entity  precision: 0.7446
Entity  recall: 0.8070
Entity  F: 0.7745

#Correct Sentiment : 9670
Sentiment  precision: 0.6770
Sentiment  recall: 0.7337
Sentiment  F: 0.7042
```
## CN

```bash
/usr/local/bin/python3 "hmm_part3.py"
100%|███████████████████████████████████████████████| 2410/2410 [00:00<00:00, 53860.80it/s]
100%|████████████████████████████████████████████████| 344/344 [00:00<00:00, 155579.10it/s]
```

```bash
/usr/local/bin/python3 "EvalScript/evalResult.py" CN/dev.out CN/dev.p3.out

#Entity in gold data: 700
#Entity in prediction: 1446

#Correct Entity : 224
Entity  precision: 0.1549
Entity  recall: 0.3200
Entity  F: 0.2088

#Correct Sentiment : 121
Sentiment  precision: 0.0837
Sentiment  recall: 0.1729
Sentiment  F: 0.1128
```