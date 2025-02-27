---
layout: page
title: 
permalink: /projects/smfqseries/
description: 
nav: false
nav_order: 
display_categories: [work, fun]
horizontal: false
---
## Pari Scripts for Holomorphic Degree 2 Siegel Modular Forms
<br>
#### Usage of Pari scripts

These scripts were written by Abhiram Kidambi. 
<a href = "../../files/SMF_q-series.zip">Click here to download</a>.

**If you use these scripts, please cite them as follows:**
```
@url{kidambi:2023SMF,
	author = {Abhiram Kidambi},
	lastchecked = {<Date Last >},
	title = {Pari/GP Scripts for Holomorphic Degree 2 Siegel Modular Forms},
	urldate = {2023}}

```

#### Installing Pari/GP

To install Pari/GP, have a look at [https://pari.math.u-bordeaux.fr/download.html](https://pari.math.u-bordeaux.fr/download.html).

Once Pari/GP is installed, open a terminal and navigate to the folder in which the pari scripts are. Changing path to where the scripts are is not necessary to do this but will make your life easier
```
	$ gp
```

This will enter the gp shell. To load the files, 

```
	$ \r deg2smf.gp
```

This may need to be loaded twice depending on your terminal profile. 

Now, you may notice the following error upon load: 

```
	%13 = (k,ord)-	>my(K=posdisc(ord),len=length(K),t=0);for(i=2,len,n=K[i][1];l=K[i][2];m=K[i][3];t=t+C(n,l,m,k)*q^(n)*y^(l)*p^(m));return(t)
	Printing coefficients up to order lim for weight k=wt Siegel EEisenstein series
  	***   at top-level: SiegelEisensteinCoeffs(wt,lim)
  	***                 ^------------------------------
  	***   in function SiegelEisensteinCoeffs: 	my(K=posdisc(ord),len=length(K));for(i=2,len,x
  	***                                            	^-----------------------------------------
  	***   in function posdisc: 	my(k=listcreate());for(a=0,n,for(b=0,n,for(c=0
  	***                                           	^---------------------------
 	 *** for: forbidden comparison t_POL , t_INT.
  	***   Break loop: type 'break' to go back to GP prompt
	break>
```

This is because the weight of the Siegel Eisenstein series, as well as the limit to which the expansion should be done have not been defined. By limit here, we mean the following:

Every holomorphic Siegel modular form admits the following Fourier expansion:

$$ F(\Omega) = \sum_{W \in M_{2\times 2}^+} C(a,b,c) e^{2 \pi i \textrm{Tr}(W\cdot \Omega)},$$
where 
$$ M_{2\times 2}^+ $$ 
is the set of all $$ 2\times 2 $$ positive definite matrices and $$ W $$ is of the form

$$ W = \begin{pmatrix} a & \frac b2 \\ \frac b2 & c\end{pmatrix}, \ \det W \geq 0, \ a,b,c \geq 0~.$$

The limit of the expansion is therefore the highest values of $$ a,b,c $$ we allow above such that the determinant and positive definiteness are met. 

**It is important to let $$ a,b,c $$ have the same maximum values, or else the $$ q $$ series gets messed up.**


#### Running the code correctly

```
	$ cd ~/PATH/TO/PARI/SCRIPTS 
	$ gp
	$ wt = <ENTER WEIGHT>;
	$ lim = <ENTER LIM>;
	$ \r deg2smf.gp
```	
You may need to run the load command one more time to get a output. 

##### Example: Coefficients of $$ E_4(\Omega) $$ up to order 3 in $$ q $$-series:
```
	$ cd ~/PATH/TO/PARI/SCRIPTS 
	$ gp
	$ wt = 4;
	$ lim = 3;
	$ \r deg2smf.gp
```	
Will generate:

```
	Printing coefficients up to order 3 for weight k=4 	Siegel Eisenstein series
	[0, 0, 1]: 240
	[0, 0, 2]: 2160
	[0, 0, 3]: 6720
	[1, 0, 0]: 240
	[1, 0, 1]: 30240
	[1, 0, 2]: 181440
	[1, 0, 3]: 497280
	[1, 1, 1]: 13440
	[1, 1, 2]: 138240
	[1, 1, 3]: 362880
	[1, 2, 1]: 240
	[1, 2, 2]: 30240
	[1, 2, 3]: 181440
	[1, 3, 3]: 13440
	[2, 0, 0]: 2160
	[2, 0, 1]: 181440
	[2, 0, 2]: 1239840
	[2, 0, 3]: 2782080
	[2, 1, 1]: 138240
	[2, 1, 2]: 967680
	[2, 1, 3]: 2903040
	[2, 2, 1]: 30240
	[2, 2, 2]: 604800
	[2, 2, 3]: 1814400
	[2, 3, 2]: 138240
	[2, 3, 3]: 967680
	[3, 0, 0]: 6720
	[3, 0, 1]: 497280
	[3, 0, 2]: 2782080
	[3, 0, 3]: 8467200
	[3, 1, 1]: 362880
	[3, 1, 2]: 2903040
	[3, 1, 3]: 6531840
	[3, 2, 1]: 181440
	[3, 2, 2]: 1814400
	[3, 2, 3]: 5987520
	[3, 3, 1]: 13440
	[3, 3, 2]: 967680
	[3, 3, 3]: 3642240
	Coefficients up to order 3 for weight k=4 Siegel Eisenstein series	
```	