# rhymes
Some simple calculations about rhyming in English.

This uses `nltk` to find all the English words that, as per the CMUDict, have no rhymes.

It then uses `wikiwords` to find, per frequencies in the 2012 edition of wikipedia, the most common unrhymeable words.

The output as of 2.15.17:


    29.23% of English words are unrhymeable.

    The 10 most common unrhymeable words are: also, january, april, category, comments, album, several, subsequent, district, modify.

    761 words end in the stem "EY1 SH AH0 N".

(re: the inclusion of 'modify': it looks like CMUDict doesn't have the most normal pronunciation of 'codify')
