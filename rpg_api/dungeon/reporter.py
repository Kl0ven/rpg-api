from io import StringIO as StringBuffer
import logging
from config import CONFIG
import shutil, os, uuid
import gzip

class Reporter(object):
    def __init__(self):
        super(Reporter, self).__init__()
        self.ch = None
        self.reporter = None
        self.report = None

    def __enter__(self):
        self.reporter = logging.getLogger('reporter')
        self.report = StringBuffer()
        self.ch = logging.StreamHandler(self.report)

        ### Optionally add a formatter
        formatter = logging.Formatter('%(message)s')
        self.ch.setFormatter(formatter)

        self.ch.setLevel(logging.INFO)
        self.reporter.setLevel(logging.INFO)
        ### Add the console handler to the logger
        self.reporter.addHandler(self.ch)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.reporter.removeHandler(self.ch)

    def log(self, message, users=None):
        if users is None:
            self.reporter.info(message)
        elif isinstance(users, list):
            self.reporter.info("{}: {}".format(
                ", ".join(u.name for u in users), message))
        else:
            self.reporter.info("{}: {}".format(users.name, message))

    def sep(self, length=50):
        self.log("#"*length)

    def get_log(self):
        return self.report.getvalue()

    def save(self):
        uid = uuid.uuid4() 
        name = "{}.txt.gz".format(uid)
        with gzip.open(os.path.join(CONFIG['reports_output_directory'], name), 'wt') as fd:
            self.report.seek(0)
            shutil.copyfileobj(self.report, fd)
        return uid
