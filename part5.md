## SG

```bash
/usr/local/bin/python3 "hmm_part5.py"
100%|███████████████████| 18559/18559 [00:00<00:00, 150654.72it/s]
100%|█████████████████████| 2650/2650 [00:00<00:00, 339262.12it/s]
100%|████████████████████████| 2650/2650 [00:16<00:00, 161.88it/s]
```bash
/usr/local/bin/python3 "EvalScript/evalResult.py" SG/dev.out SG/dev.p5.out

#Entity in gold data: 4301
#Entity in prediction: 3520

#Correct Entity : 1921
Entity  precision: 0.5457
Entity  recall: 0.4466
Entity  F: 0.4912

#Correct Sentiment : 1657
Sentiment  precision: 0.4707
Sentiment  recall: 0.3853
Sentiment  F: 0.4237
```


## EN

```bash
/usr/local/bin/python3 "hmm_part4.py"
100%|██████████████████████| 7663/7663 [00:00<00:00, 84179.16it/s]
100%|█████████████████████| 1094/1094 [00:00<00:00, 226182.71it/s]
100%|█████████████████████████| 1094/1094 [03:16<00:00,  5.57it/s]
```

```bash
/usr/local/bin/python3 "EvalScript/evalResult.py" EN/dev.out EN/dev.p5.out

#Entity in gold data: 13179
#Entity in prediction: 14059

#Correct Entity : 10503
Entity  precision: 0.7471
Entity  recall: 0.7969
Entity  F: 0.7712

#Correct Sentiment : 9570
Sentiment  precision: 0.6807
Sentiment  recall: 0.7262
Sentiment  F: 0.7027
```
## CN

```bash
/usr/local/bin/python3 "hmm_part4.py"
100%|███████████████████████████████████| 2410/2410 [00:00<00:00, 48565.01it/s]
100%|████████████████████████████████████| 344/344 [00:00<00:00, 143924.25it/s]
100%|████████████████████████████████████████| 344/344 [00:06<00:00, 56.09it/s]
```

```bash
/usr/local/bin/python3 "EvalScript/evalResult.py" CN/dev.out CN/dev.p5.out

#Entity in gold data: 700
#Entity in prediction: 1277

#Correct Entity : 194
Entity  precision: 0.1519
Entity  recall: 0.2771
Entity  F: 0.1963

#Correct Sentiment : 102
Sentiment  precision: 0.0799
Sentiment  recall: 0.1457
Sentiment  F: 0.1032
```