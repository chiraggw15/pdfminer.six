from shutil import rmtree
from tempfile import NamedTemporaryFile, mkdtemp

from helpers import absolute_sample_path
from tools import dumppdf


def run(filename, options=None):
    absolute_path = absolute_sample_path(filename)
    with NamedTemporaryFile() as output_file:
        if options:
            s = 'dumppdf -o %s %s %s' % (output_file.name,
                                         options, absolute_path)
        else:
            s = 'dumppdf -o %s %s' % (output_file.name, absolute_path)
        dumppdf.main(s.split(' ')[1:])


class TestDumpPDF():
    def test_1(self):
        run('jo.pdf', '-t -a')
        run('simple1.pdf', '-t -a')
        run('simple2.pdf', '-t -a')
        run('simple3.pdf', '-t -a')

    def test_2(self):
        run('nonfree/dmca.pdf', '-t -a')

    def test_3(self):
        run('nonfree/f1040nr.pdf')

    def test_4(self):
        run('nonfree/i1040nr.pdf')

    def test_5(self):
        run('nonfree/kampo.pdf', '-t -a')

    def test_6(self):
        run('nonfree/naacl06-shinyama.pdf', '-t -a')

    def test_embedded_font_filename(self):
        """If UF font file name does not exist, then F should be used

        Related issue: https://github.com/pdfminer/pdfminer.six/issues/152
        """
        output_dir = mkdtemp()
        try:
            run('contrib/issue-00152-embedded-pdf.pdf',
                '--extract-embedded %s' % output_dir)
        finally:
            rmtree(output_dir)
