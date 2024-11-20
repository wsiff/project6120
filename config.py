from sqlalchemy import create_engine
from pathlib import Path

# Database configuration
engine = create_engine(rf"sqlite:///waf_comparison.db")

# Data set paths
LEGITIMATE_URL_PATH = "https://downloads.openappsec.io/waf-comparison-project/legitimate.zip"
MALICIOUS_URL_PATH = "https://downloads.openappsec.io/waf-comparison-project/malicious.zip"

# Data set Path
DATA_PATH = Path('Data')
LEGITIMATE_PATH = DATA_PATH / 'Legitimate'
MALICIOUS_PATH = DATA_PATH / 'Malicious'

PLAYGROUND_URL = 'https://openappsec-vm-80-xodpg3bx1yd8.env.play.instruqt.com/'

# WAF configuration
WAFS_DICT = {
    "ATTACK MODEL WITH PAYLOADS":                          PLAYGROUND_URL
}
