## SG

```bash
/usr/local/bin/python3 "hmm_part4.py"
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 18559/18559 [00:00<00:00, 141056.86it/s]
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2650/2650 [00:00<00:00, 322816.81it/s]```

```bash
/usr/local/bin/python3 "EvalScript/evalResult.py" SG/dev.out SG/dev.p4.out

#Entity in gold data: 4301
#Entity in prediction: 13063

#Correct Entity : 1450
Entity  precision: 0.1110
Entity  recall: 0.3371
Entity  F: 0.1670

#Correct Sentiment : 833
Sentiment  precision: 0.0638
Sentiment  recall: 0.1937
Sentiment  F: 0.0959
```


## EN

```bash
/usr/local/bin/python3 "hmm_part4.py"
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 7663/7663 [00:00<00:00, 81017.74it/s]
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1094/1094 [00:00<00:00, 247122.39it/s]```

```bash
/usr/local/bin/python3 "EvalScript/evalResult.py" EN/dev.out EN/dev.p4.out

#Entity in gold data: 13179
#Entity in prediction: 14264

#Correct Entity : 4854
Entity  precision: 0.3403
Entity  recall: 0.3683
Entity  F: 0.3538

#Correct Sentiment : 3194
Sentiment  precision: 0.2239
Sentiment  recall: 0.2424
Sentiment  F: 0.2328
```
## CN

```bash
/usr/local/bin/python3 "hmm_part4.py"
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2410/2410 [00:00<00:00, 58492.21it/s]
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 344/344 [00:00<00:00, 169228.31it/s]```

```bash
/usr/local/bin/python3 "EvalScript/evalResult.py" CN/dev.out CN/dev.p4.out

#Entity in gold data: 700
#Entity in prediction: 5119

#Correct Entity : 187
Entity  precision: 0.0365
Entity  recall: 0.2671
Entity  F: 0.0643

#Correct Sentiment : 66
Sentiment  precision: 0.0129
Sentiment  recall: 0.0943
Sentiment  F: 0.0227
```