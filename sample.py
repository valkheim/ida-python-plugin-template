import idaapi

from sample import NAME
from sample.utils import debug, error, info


class Plugin(idaapi.plugin_t):
    NAME = NAME
    VERSION = "0.0.1"
    AUTHORS = f"The {NAME} team."

    flags = idaapi.PLUGIN_UNL
    comment = f"The {NAME} plugin."
    help = ""
    wanted_name = NAME
    wanted_hotkey = ""

    @staticmethod
    def description() -> str:
        return f"{Plugin.NAME} v{Plugin.VERSION}"

    def print_banner(self) -> None:
        description = f"{Plugin.NAME} v{Plugin.VERSION}"
        copyright = f"(c) {Plugin.AUTHORS}"
        info("-" * 80)
        info(f"{description} — {copyright}")
        info("-" * 80)

    def init(self):
        debug("Init")
        try:
            # some initialization routines
            pass

        except Exception as err:
            error(str(err))
            return idaapi.PLUGIN_SKIP

        self.print_banner()
        return idaapi.PLUGIN_KEEP

    def run(self, arg):
        debug("Run")
        pass

    def term(self):
        debug("Term")
        pass


def PLUGIN_ENTRY():
    return Plugin()
