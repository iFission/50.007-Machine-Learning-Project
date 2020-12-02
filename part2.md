## SG

```bash
/usr/local/bin/python3 "hmm_part2.py"
100%|█| 18559/18559 [00:00<00:00, 1439
100%|█| 2650/2650 [00:00<00:00, 391259
```

```bash
/usr/local/bin/python3 "EvalScript/evalResult.py" SG/dev.out SG/dev.p2.out

#Entity in gold data: 4301
Entity in prediction: 12237
#Correct Entity : 2386
Entity  precision: 0.1950
Entity  recall: 0.5548
Entity  F: 0.2885

#Correct Sentiment : 1531
Sentiment  precision: 0.1251
Sentiment  recall: 0.3560
Sentiment  F: 0.1851
```


## EN

```bash
/usr/local/bin/python3 "hmm_part2.py"
100%|█| 7663/7663 [00:00<00:00, 76288.
100%|█| 1094/1094 [00:00<00:00, 226271
```

```bash
/usr/local/bin/python3 "EvalScript/evalResult.py" EN/dev.out EN/dev.p2.out

#Entity in gold data: 13179
#Entity in prediction: 18650

#Correct Entity : 9542
Entity  precision: 0.5116
Entity  recall: 0.7240
Entity  F: 0.5996

#Correct Sentiment : 8456
Sentiment  precision: 0.4534
Sentiment  recall: 0.6416
Sentiment  F: 0.5313
```
## CN

```bash
/usr/local/bin/python3 "hmm_part2.py"
100%|█| 2410/2410 [00:00<00:00, 55432.
100%|█| 344/344 [00:00<00:00, 108476.1
```

```bash
/usr/local/bin/python3 "EvalScript/evalResult.py" CN/dev.out CN/dev.p2.out

#Entity in gold data: 700
#Entity in prediction: 4248

#Correct Entity : 345
Entity  precision: 0.0812
Entity  recall: 0.4929
Entity  F: 0.1395

#Correct Sentiment : 167
Sentiment  precision: 0.0393
Sentiment  recall: 0.2386
Sentiment  F: 0.0675
```