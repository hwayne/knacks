load 'tables/csv'

NB. J uses a fixed seed for some reason

NB. 9!:1 */ i.4 { 6!:0 ''

csv =: readcsv 'path/to/friendlist.csv'

NB. head, second column, unbox
days =: >@(1&{"1)@}. 

NB. CSVs always imported as strings, use ". to get ints
x =: ". days csv

NB. reverse weight: take reciprocals, gen rand (0, 1) for each entry,
NB. then check if reciprocal is greater than rand
sample =: (> ?@$&0@#)@:%



NB. List of candidates to contact today
] ppl =: csv #~ 0 , sample x

NB. ?~@# is "random permutation of strings"
(shuffle =: (?~@# { ])) ppl

ppl
out =: (0{"1 ppl) ,. < 6!:0 'MM/DD/YY'
echo out

NB. 2!:55''

] sortedy =: g { y
NB. invert g
] ig =: /: g
NB. gives us back y
y = ig { sortedy
