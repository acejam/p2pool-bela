from p2pool.bitcoin import networks

PARENT = networks.nets['belacoin']
SHARE_PERIOD=20
CHAIN_LENGTH=24*60*60//20
REAL_CHAIN_LENGTH=12*60*60//20
TARGET_LOOKBEHIND=20
SPREAD=50
IDENTIFIER='1bfe031e711a1dbb'.decode('hex')
PREFIX='1bfe031e71b2b43c'.decode('hex')
P2P_PORT=7877
MIN_TARGET=0
MAX_TARGET=2**256//2**20 - 1
PERSIST=True
WORKER_PORT=7878
BOOTSTRAP_ADDRS='crypto.office-on-the.net p2p-spb.xyz'.split(' ')
ANNOUNCE_CHANNEL='#p2pool-bela'
VERSION_CHECK=lambda v: True
