# MFUtility

This project scraps data for various mutual funds and creates a portfolio,
depending on the weights provided. Using this, anyone can create a average of a
portfolio of stocks of a class of mutual funds to be invested in markets without
paying the extra expense ratio.

# Analysis on a few of the mutual fund categories dated on 1 June, 2019.

## Small Cap Funds in India.
```
                                   funds  weights
0                    Axis Small Cap Fund     0.04
1                   Kotak Small Cap Fund     0.10
2           L&T Emerging Businesses Fund     0.20
3                    Tata Small Cap Fund     0.10
4                    HDFC Small Cap Fund     0.30
5                     SBI Small Cap Fund     0.10
6                Reliance Small Cap Fund     0.06
7  Franklin India Smaller Companies Fund     0.10
                                Company  Weight
13                Kalpataru Power Trans  1.1880
133                     Sharda Cropchem  1.1100
140                   NIIT Technologies  1.0996
106                    Aurobindo Pharma  1.0380
144                        Chalet Hotel  0.9882
117           Tube Investments Of India  0.9800
35                Balkrishna Industries  0.9600
134                     Sonata Software  0.9300
105                           JK Cement  0.8764
77          Chambal Fertilisers & Chem.  0.8340
2               Gujarat Fluorochemicals  0.8040
22                        Indian Hotels  0.7962
64                            HDFC Bank  0.7940
38                   Galaxy Surfactants  0.7894
78              Repco Home Finance Ltd.  0.7770
79                     JMC Projects (I)  0.7590
125                   Vardhman Textiles  0.7380
57                     Grindwell Norton  0.7376
147                         Sheela Foam  0.7330
16                          Indian Bank  0.7230
139                   The Ramco Cements  0.7210
31                            SKF India  0.7050
121       Techno Electric & Engineering  0.6940
60   Future Supply Chain Solutions Ltd.  0.6830
10                    KEC International  0.6300
59                         NRB Bearings  0.6240
58                  Sadbhav Engineering  0.6180
73                            Blue Star  0.6112
153               Firstsource Solutions  0.6090
```

## Thematic(Infra) funds in India
```
                                           funds  weights
0                      Franklin Build India Fund     0.15
1                        UTI Infrastructure Fund     0.15
2                        L&T Infrastructure Fund     0.10
3                       IDFC Infrastructure Fund     0.10
4              Invesco India Infrastructure Fund     0.10
5  Kotak Infrastructure and Economic Reform Fund     0.10
6         Sundaram Infrastructure Advantage Fund     0.10
7                        SBI Infrastructure Fund     0.10
8    BOI AXA Manufacturing & Infrastructure Fund     0.10
                                   Company  Weight
86                         Larsen & Toubro  6.5645
111                             ICICI Bank  2.8060
20                           Bharti Airtel  2.7505
30                     State Bank of India  2.5230
2                                Axis Bank  2.3305
55                                    NTPC  2.2550
22                            Shree Cement  2.2295
21                        Ultratech Cement  2.0300
104                    Reliance Industries  1.9380
92                         Container Corp.  1.8540
95                       The Ramco Cements  1.5520
10                   Kalpataru Power Trans  1.4185
7                                     GAIL  1.4045
110                          PNC Infratech  1.3550
43                               HDFC Bank  1.2200
52                               Blue Star  1.2135
4                   Power Grid Corporation  1.1500
91                        Indraprastha Gas  1.1295
40   Adani Ports and Special Economic Zone  1.0890
59                        JMC Projects (I)  1.0400
98                         AIA Engineering  1.0260
```

## Thematic(Consumption) funds
```
                                      funds  weights
0                    Quant Consumption Fund    0.125
1        SBI Consumption Opportunities Fund    0.125
2                 Reliance Consumption Fund    0.125
3       Sundaram Rural and Consumption Fund    0.125
4  Aditya Birla Sun Life India GenNext Fund    0.125
5                  Tata India Consumer Fund    0.125
6           Mirae Asset Great Consumer Fund    0.125
7        Canara Robeco Consumer Trends Fund    0.125
                                   Company   Weight
76                                     ITC  6.67000
26                      Hindustan Unilever  3.76375
4                             Asian Paints  2.78500
38                               HDFC Bank  2.74000
94                            Nestle India  2.41625
102                             ICICI Bank  2.40750
72                       Colgate-Palmolive  2.19000
96                             Dabur India  1.99500
78                     Maruti Suzuki India  1.96625
64                           Titan Company  1.90750
16                     Mahindra & Mahindra  1.57875
2                           United Spirits  1.57750
40                              Bata India  1.51250
28                      Jubilant FoodWorks  1.49750
66                                  Marico  1.43125
50                                  Voltas  1.38625
33                     State Bank of India  1.32625
45                        United Breweries  1.24625
11                           Indian Hotels  1.14250
70                       Stylam Industries  1.14000
52                           Havells India  1.01625
```

## Eaxample command:
```
python analyzer.py --config '{"data/hdfc-small-cap-fund-direct-plan-growth.csv": 0.6, "data/kotak-small-cap-fund-direct-plan-growth.csv": 0.4}' --to_json
```