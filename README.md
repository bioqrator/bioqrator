# bioqrator


## Tables

### Sample

| name           | dtype     | contraint    | example values                                          |
|----------------|-----------|--------------|---------------------------------------------------------|
| id             | CHAR(8)   | NOT NULL, PK | SM486AYH, SM326JKS                                      |
| organism       | CHAR(32)  | NOT NULL     | Human, Mouse, Rat, Monkey, Zebrafish, Worm              |
| biosample      | CHAR(32)  | NOT NULL     | HeLa, HepG2, HEK293T, HCT116                            |
| condition      | CHAR(255) |              | WT, Parental, DICER KO, DROSHA KO, PCBP2 KO, IGF2BP1 KO |
| treatment      | CHAR(255) |              | hsa-miR-155-5p, SARS-CoV-2                              |
| treatment_time | CHAR(32)  |              | 24hr, 24hpi                                             |
| treatment_conc | CHAR(32)  |              | 100nM, 200nM, 300nM                                     |
| target         | CHAR(32)  |              | AARS, RBFOX2                                            |
| assay          | CHAR(32)  |              | mRNA-seq, RPF-seq, QTI-seq, sRNA-seq, eCLIP-seq         |
| layout         | CHAR(32)  |              | 1x51, 1x101, 2x51, 2x101, 51+101                        |
| platform       | CHAR(32)  |              | HiSeq, MiSeq                                            |
| date           | DATE      |              | 2017-03-06, 2018-10-08, 2021-03-29                      |

Accession id format: 'SM000AAA' (10x10x10x26x26x26 = 17,576,000 combinations)

### SamplePair

| name           | dtype     | contraint      | example values   |
|----------------|-----------|----------------|------------------|
| id1            | CHAR(8)   | FK (Sample.id) | SM486AYH         |
| id2            | CHAR(8)   | FK (Sample.id) | SM326JKS         |
| similarity     | FLOAT     | NOT NULL       | 0.97             |