import nltk
import operator
import re
import wikiwords

entries = nltk.corpus.cmudict.entries()

pronunciations = {}
letters_only = re.compile('[\W_]+')
for entry in entries:
    word = letters_only.sub('', entry[0])  # for odd entries like 'a.'
    pronunciations[word] = pronunciations.setdefault(word, []) + [entry[1]]

rhyme_stems_dict = {}
for word, pronunciation_list in pronunciations.items():
    def make_rhyme(pronunciation):
        accent_index = next((index for index, syllable in enumerate(pronunciation) if '1' in syllable), 0)
        return ' '.join(pronunciation[accent_index:])

    rhyme_stems_dict[word] = set([make_rhyme(pronunciation) for pronunciation in pronunciation_list])

rhyme_stem_totals = {}
for rhyme_stems in rhyme_stems_dict.values():
    for rhyme_stem in rhyme_stems:
        rhyme_stem_totals[rhyme_stem] = rhyme_stem_totals.setdefault(rhyme_stem, 0) + 1


unrhymeable_words = []
for word, rhyme_stems in rhyme_stems_dict.items():
    if all(rhyme_stem_totals[rhyme_stem] == 1 for rhyme_stem in rhyme_stems):
        unrhymeable_words.append(word)

unrhymeable_percentage = round(len(unrhymeable_words)/len(pronunciations)*100, 2)
unrhymeable_words.sort(key=wikiwords.freq, reverse=True)
best_stem, best_stem_total = max(rhyme_stem_totals.items(), key=operator.itemgetter(1))

print('{0}% of English words are unrhymeable.'.format(unrhymeable_percentage))
print()
print('The 10 most common unrhymeable words are: {0}.'.format(', '.join(unrhymeable_words[:10])))
print()
print('{0} words end in the most common stem, "{1}".'.format(best_stem_total, best_stem))
