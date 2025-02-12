# Can't generate with stubgen because:
# "ImportError: This must be an MFC application - try 'import win32ui' first"

"""A module for Dynamic Data Exchange support"""

APPCLASS_MONITOR: int
APPCLASS_STANDARD: int
APPCMD_CLIENTONLY: int
APPCMD_FILTERINITS: int
CBF_FAIL_ADVISES: int
CBF_FAIL_ALLSVRXACTIONS: int
CBF_FAIL_CONNECTIONS: int
CBF_FAIL_EXECUTES: int
CBF_FAIL_POKES: int
CBF_FAIL_REQUESTS: int
CBF_FAIL_SELFCONNECTIONS: int
CBF_SKIP_ALLNOTIFICATIONS: int
CBF_SKIP_CONNECT_CONFIRMS: int
CBF_SKIP_DISCONNECTS: int
CBF_SKIP_REGISTRATIONS: int

def CreateConversation(*args): ...  # incomplete
def CreateServer(*args): ...  # incomplete
def CreateServerSystemTopic(*args): ...  # incomplete
def CreateStringItem(*args): ...  # incomplete
def CreateTopic(*args): ...  # incomplete

MF_CALLBACKS: int
MF_CONV: int
MF_ERRORS: int
MF_HSZ_INFO: int
MF_LINKS: int
MF_POSTMSGS: int
MF_SENDMSGS: int

class error(Exception): ...
