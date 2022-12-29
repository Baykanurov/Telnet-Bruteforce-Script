from .arguments import parser
from .file_manager import FileManager
from .telnet_manager import TelnetManager

args = parser.parse_args()
file_manager = FileManager()
telnet_manager = TelnetManager()
