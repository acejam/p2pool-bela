import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

P2P_PREFIX = 'f7c7b1d6'.decode('hex')
P2P_PORT = 10554
ADDRESS_VERSION = 25
RPC_PORT = 10555
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'BelaCoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC=lambda height: 50*100000000 >> (height + 1)//730000
POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD=120
SYMBOL='BELA'
CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'BelaCoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/BelaCoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.BelaCoin'), 'BelaCoin.conf')
BLOCK_EXPLORER_URL_PREFIX='https://chainz.cryptoid.info/bela/block.dws?'
ADDRESS_EXPLORER_URL_PREFIX='https://chainz.cryptoid.info/bela/address.dws?'
TX_EXPLORER_URL_PREFIX='https://chainz.cryptoid.info/bela/tx.dws?'
SANE_TARGET_RANGE = (2**256//2**32 - 1, 2**256//2**29 - 1)
DUMB_SCRYPT_DIFF=2**16
DUST_THRESHOLD=0.03e8
