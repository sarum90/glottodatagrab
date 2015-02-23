
import unittest
import fakeserver

from pyglottolog import server
from pyglottolog import glottodata


class TestGlottoData(unittest.TestCase):

    def setUp(self):
      self._num_languages = 2222
      self._server = fakeserver.FakeServer(self._num_languages)
      # We should have 6 files, 0-499, 500-999, 1000-1499, 1500-1999,
      # 2000-2499, and the first empty one: 2500-2999
      self._expected_files = 6

      log = []
      def SimpleLog(log_line):
        log.append(log_line)
      self._log = log

      self._data_dir = 'fake_data'
      self._data = glottodata.GlottoData(self._server, clear_cache=True,
                                         data_dir=self._data_dir,
                                         logger=SimpleLog)

    def testMakeData(self):
      self.assertEqual(self._expected_files, len(self._data._ListFiles()))

    def test2ndUsesCachedData(self):
      data = glottodata.GlottoData(None, clear_cache=False,
                                   data_dir=self._data_dir, logger=None)
      self.assertEqual(self._expected_files, len(self._data._ListFiles()))
    
    def testLanguageContents(self):
      languages = self._data.GetLanguages()
      self.assertEqual(self._num_languages, len(languages))
      for i in xrange(self._num_languages):
        self.assertEqual(i, languages[i].get('id'))

    def tearDown(self):
      self._data._ClearDataDirectory()


if __name__ == '__main__':
    unittest.main()
