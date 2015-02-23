## Synopsis

A simple python library for downloading and using the data from glottolog.org.

## Code Example

Command line:

    # This takes a long time as all the data is downloaded and cached locally:
    $ python sample.py
    Creating a local data cache at .../pyglottolog/data.
    Downloading data for entries 0..499
    Downloading data for entries 500..999
    Downloading data for entries 1000..1499
    Downloading data for entries 1500..1999
    Downloading data for entries 2000..2499
    Downloading data for entries 2500..2999
    Downloading data for entries 3000..3499
    Downloading data for entries 3500..3999
    Downloading data for entries 4000..4499
    Downloading data for entries 4500..4999
    Downloading data for entries 5000..5499
    Downloading data for entries 5500..5999
    Downloading data for entries 6000..6499
    Downloading data for entries 6500..6999
    Downloading data for entries 7000..7499
    Downloading data for entries 7500..7999
    Downloading data for entries 8000..8499
    Empty results, download complete
    7350
    [{u'status': u'established', u'...

    # This takes a long time as all the data is downloaded and cached locally:
    $ python sample.py
    Using the local data cache at .../pyglottolog/data.
    7350
    [{u'status': u'established', u'...

The code:

    from pyglottolog.glottodata import GlottoData

    # Download data from glottolog.org if not already locally cached:
    db = GlottoData()

    # All the data should be available as a big list in db.GetLanguages()
    print db.GetLanguages()[0], len(db.GetLanguages())
