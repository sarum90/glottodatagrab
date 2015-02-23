
from pyglottolog.glottodata import GlottoData

db = GlottoData()
print len(db.GetLanguages())
print db.GetLanguages()[:10]
