## SG

```bash
/usr/local/bin/python3 "hmm_part4.py"
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 18559/18559 [00:00<00:00, 141056.86it/s]
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2650/2650 [00:00<00:00, 322816.81it/s]```

```bash
/usr/local/bin/python3 "EvalScript/evalResult.py" SG/dev.out SG/dev.p4.out

#Entity in gold data: 4301
#Entity in prediction: 34191

#Correct Entity : 2308
Entity  precision: 0.0675
Entity  recall: 0.5366
Entity  F: 0.1199

#Correct Sentiment : 123
Sentiment  precision: 0.0036
Sentiment  recall: 0.0286
Sentiment  F: 0.0064
```


## EN

```bash
/usr/local/bin/python3 "hmm_part4.py"
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 7663/7663 [00:00<00:00, 81017.74it/s]
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1094/1094 [00:00<00:00, 247122.39it/s]```

```bash
/usr/local/bin/python3 "EvalScript/evalResult.py" EN/dev.out EN/dev.p4.out

#Entity in gold data: 13179
#Entity in prediction: 26131

#Correct Entity : 7310
Entity  precision: 0.2797
Entity  recall: 0.5547
Entity  F: 0.3719

#Correct Sentiment : 175
Sentiment  precision: 0.0067
Sentiment  recall: 0.0133
Sentiment  F: 0.0089
```
## CN

```bash
/usr/local/bin/python3 "hmm_part4.py"
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2410/2410 [00:00<00:00, 58492.21it/s]
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 344/344 [00:00<00:00, 169228.31it/s]```

```bash
/usr/local/bin/python3 "EvalScript/evalResult.py" CN/dev.out CN/dev.p4.out

#Entity in gold data: 700
#Entity in prediction: 13060

#Correct Entity : 347
Entity  precision: 0.0266
Entity  recall: 0.4957
Entity  F: 0.0504

#Correct Sentiment : 15
Sentiment  precision: 0.0011
Sentiment  recall: 0.0214
Sentiment  F: 0.0022
```