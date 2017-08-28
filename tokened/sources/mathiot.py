from . import fetch


class RemotePdf(object):
    def __init__(self, url, filename):
        fetch.ensure_pdf_source_exists(url, filename)


class Volume1(RemotePdf):
    URL = 'http://www.acsu.buffalo.edu/~mathiotm/Mathiot/Volume%20I.pdf'
    FILENAME = 'mathiot_volume_1.pdf'

    def __init__(self):
        super().__init__(Volume1.URL, Volume1.FILENAME)


class Volume2(RemotePdf):
    URL = 'http://www.acsu.buffalo.edu/~mathiotm/Mathiot/Volume%20II.pdf'
    FILENAME = 'mathiot_volume_1.pdf'

    def __init__(self):
        super().__init__(Volume2.URL, Volume2.FILENAME)
