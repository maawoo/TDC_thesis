<!--
Figures can be either referenced using @fig:mylabel, and can be auto-completed
to **Fig. number: mylabel** by prefixing with @ for mid-sentence references and * for the start of sentences. See https://github.com/tomduck/pandoc-fignos
-->

<!-- 
Figures can be added with the following syntax:
![main_text_caption](source/figures/my_image.pdf "short_caption(optional)"){#fig:mylabel}{ width=50% }

For details on setting attributes like width and height, see:
http://pandoc.org/MANUAL.html#extension-link_attributes
--> 

<!-- 
For italic, add _ on either side of the text
For bold, add ** on either side of the text
For bold and italic, add _** on either side of the text
-->

$f(x) = ax^3 + bx^2 + cx + d$ {#eq:my_equation}


```python
mood = 'happy'
if mood == 'happy':
    print("I am a happy robot")
```

-----------------------------------------------------------------------------------
Landmass      \%      Number of   Dolphins per    How Many     How Many    Forbidden
             stuff    Owls        Capita         Foos         Bars        Float
------------ ------- --------- -------------- ------------ ------------ -----------
    North       94%    20,028       17,465        12,084       20,659       1.71
 America                                                               

Central      91%     6564         6350         8,189        12,012       1.52
America                                                               

    South       86%     3902         4127         5,205        6,565        1.28
America                                                               

    Africa      84%     2892         3175         3,862        4,248         1.1

    Europe      92%    20,964       17,465        15,303       24,203       1.58

    Asia       87%     6852         6350         8,255        11,688       1.47

Oceania      87%     4044         4127         5,540        6,972        1.28

Antarctica    83%     2964         3175         4,402        4,941        1.13
-----------------------------------------------------------------------------------

Table: Important data for various land masses. {#tbl:random}

